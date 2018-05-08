
from pyspark import SparkContext
import MySQLdb

#------------------- SPARK RECOMMENDATION SECTION ----------------------#
sc = SparkContext("spark://spark-master:7077", "PopularItems")
data = sc.textFile("/tmp/data/data.txt", 2)  	# each worker loads a piece of the data file   			

#------ Read data in as pairs of (user_id, item_id clicked on by the user) ----------#
user_views = data.map(lambda line: line.split("\t"))	# tell each worker to split each line of it's partition					
user_views = user_views.mapValues(lambda id: int(id))	# turn the values into ints	

#------ Group data into (user_id, list of item ids they clicked on) ----------#
user_list = user_views.groupByKey()		

#------ Transform into (user_id, (item1, item2) where item1 and item2 are pairs of items the user clicked on ----------#			
pairs = user_list.mapValues(lambda items: [(x,y) for x in items for y in items if x != y])	# map values into pairs where every value is paired with another if they aren't equal
pairs = pairs.mapValues(lambda items: [(x,y) for x,y in items if x >= y])					# order pairs so highest value comes first
pairs = pairs.flatMap(lambda line: [ (line[0], line[1][i]) for i in range(len(line[1])) ] )	# split into multiple RDDs 										# switch user_id to be the value
pairs = pairs.map(lambda line: (line[1], line[0]))											# switch user id to be value

#------ Transform into ((item1, item2), list of user1, user2 etc) where users are all the ones who co-clicked (item1, item2) ----------#
views = pairs.distinct().groupByKey()		# group by page pairs that are distinct

#------ Transform into ((item1, item2), count of distinct users who co-clicked (item1, item2) ----------#
count = views.map(lambda line: (line[0], len(line[1])))	

#------ Filter out any results where less than 3 users co-clicked the same pair of items ----------#
final = count.filter(lambda line: line[1] >= 3)			# only include results with 3 or more matches
final = final.map(lambda line: line[0])					# get rid of the count and just have the pairs

#------ Collect results from workers ----------#
output = final.collect() 

# for page_id in output:
# 	print("pages: ")
# 	print(page_id[0])
# print ("Popular items done")

sc.stop()

#------------------- FORMATTING SECTION ----------------------#
# create a dictionary
rec_lists = {}

# loop through all pairs and place into dictionary as lists
for pair in output:
	# if value already is in dictionary
	if pair[0] in rec_lists:
		# add the next value onto the list
		rec_lists[pair[0]].append(pair[1])
	else:
		#create a new key-value pair
		rec_lists[pair[0]] = [pair[1]]

	# if value already is in dictionary
	if pair[1] in rec_lists:
		# add the next value onto the list
		rec_lists[pair[1]].append(pair[0])
	else:
		#create a new key-value pair
		rec_lists[pair[1]] = [pair[0]]

#turn the list into a string
for x in rec_lists:
	','.join(str(i) for i in rec_lists[x])

# for x in rec_lists:
#     print("item_id: %d" % x)
#     print(rec_lists[x])

    	
#------------------- SQL DATABASE SECTION ----------------------#
db = MySQLdb.connect(host="db",user="www", passwd="$3cureUS",db="cs4501") 
c = db.cursor()

# use the correct table
c.execute("use cs4501;")

# clear the recommendation table
c.execute("delete from posts_recommendation;")

# create execution string for each item and execute
for key, value in rec_lists.items():
	line = ("insert into posts_recommendation (item_id, rec_items) values (%d, \"%s\");" % (key, value))
	c.execute(line)

# commit changes
db.commit()

# c.execute("select * from posts_recommendation")
# print(c.fetchall())

db.close()



