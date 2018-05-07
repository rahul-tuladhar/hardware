from kafka import KafkaConsumer
from elasticsearch import Elasticsearch
import time
import json

# Tries to get consumer freeze process if not able
while True:
    try:
        consumer = KafkaConsumer('new-listings-topic', group_id='listing-indexer', bootstrap_servers=['kafka:9092'])
        es = Elasticsearch(['es'])
        break
    except:
        time.sleep(5)


# Receives a message from Kafka producer and indexes in es
#
# with open('fixtures.json', encoding='utf-8') as data_file:
#     data = json.loads(data_file.read())
# for post in data:
#     # print(post)
#     try:
#         if post['model'] == 'posts.post':
#             print(post['fields'])
#             print(post['pk'])
#             es.index(index='listing_index', doc_type='listing', id=post['pk'], body=post['fields'])
#             print(post['fields'])
#             es.indices.refresh(index="listing_index")
#     except:
#         print('error in index')
#

while True:
    print('true')
    for message in consumer:
        new_consumer = json.loads((message.value).decode('utf-8'))
        print(json.loads((message.value).decode('utf-8')))
        print(new_consumer['result']['id'])
        print(new_consumer['result'])
        es.index(index='listing_index', doc_type='listing', id=new_consumer['result']['id'], body=new_consumer['result'])
        es.indices.refresh(index="listing_index")