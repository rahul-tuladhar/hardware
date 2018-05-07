from pyspark import SparkContext
# import _mysql

# db=_mysql.connect(host="db",user="www",
#                   passwd="$3cureUS",db="cs4501") 




sc = SparkContext("spark://spark-master:7077", "PopularItems")

data = sc.textFile("/tmp/data/access.log", 2)     		# each worker loads a piece of the data file

pairs = data.map(lambda line: line.split("\t"))   		# tell each worker to split each line of it's partition
user_list = pairs.groupByKey();							# group data into (user_id, list of item ids they clicked on)





output = user_list.collect() 				  		

for page_id, count in output:
	print("user_id %s items: " % page_id)
	print(list(count))

print ("Popular items done")

# pages = pairs.map(lambda pair: (pair[1], 1))      		# re-layout the data to ignore the user id
# count = pages.reduceByKey(lambda x,y: int(x)+int(y))    # shuffle the data so that each key is only on one worker
#                                                   		# and then reduce all the values by adding them together
# output = count.collect()                          		# bring the data back to the master node so we can print it out
# for page_id, count in output:
#     print ("page_id %s count %d" % (page_id, count))
# print ("Popular items done")

sc.stop()


# Read data in as pairs of (user_id, item_id clicked on by the user)
# 
# Transform into (user_id, (item1, item2) where item1 and item2 are pairs of items the user clicked on
# Transform into ((item1, item2), list of user1, user2 etc) where users are all the ones who co-clicked (item1, item2)
# Transform into ((item1, item2), count of distinct users who co-clicked (item1, item2)
# Filter out any results where less than 3 users co-clicked the same pair of items