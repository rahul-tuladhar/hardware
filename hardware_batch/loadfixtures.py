from kafka import KafkaConsumer
from elasticsearch import Elasticsearch
import time
import json

time.sleep(20)
es = Elasticsearch(['es'])
consumer = KafkaConsumer('new-listings-topic', group_id='listing-indexer', bootstrap_servers=['kafka:9092'])

# f = json.load(open('data.json'))
with open('fixtures.json', encoding='utf-8') as data_file:
   data = json.loads(data_file.read())
for post in data:
    print(post)
    if post['model'] is 'posts.post':
        es.index(index='listing_index', doc_type='listing', id=post['fields']['id'], body=post['fields'])
es.indices.refresh(index="listing_index")

# while True:
#     print('true')
#     for message in consumer:
#         new_consumer = json.loads((message.value).decode('utf-8'))
#         print(json.loads((message.value).decode('utf-8')))
#         es.index(index='listing_index', doc_type='listing', id=new_consumer['result']['id'], body=new_consumer['result'])
#         es.indices.refresh(index="listing_index")