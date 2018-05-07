from pyspark import SparkContext
import MySQLdb


#------------------- SPARK RECOMMENDATION SECTION ----------------------#
sc = SparkContext("spark://spark-master:7077", "PopularItems")
data = sc.textFile("/tmp/data/access.log", 2)  	# each worker loads a piece of the data file   			

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
final = count.filter(lambda line: line[1] >= 3)

#------ Collect results from workers ----------#
output = final.collect() 

# for page_id, count in output:
# 	print("pages: ")
# 	print(list(page_id))
# 	print(count)
# print ("Popular items done")

sc.stop()


#------------------- SQL DATABASE SECTION ----------------------#
db = MySQLdb.connect(host="db",user="www", passwd="$3cureUS",db="cs4501") 
c = db.cursor()

# use the correct table
c.execute("use cs4501;")










db.close()



