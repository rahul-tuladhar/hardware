from kafka import KafkaConsumer
from elasticsearch import Elasticsearch
import time
import json
#
time.sleep(30)
#
es = Elasticsearch(['es'])
consumer = KafkaConsumer('new-listings-topic', group_id='listing-indexer', bootstrap_servers=['kafka:9092'])
while True:
    for message in consumer:
        print(json.loads(message.value).decode('utf-8'))
        new_consumer = json.loads(message.value).decode('utf-8')
        es.index(index='listing_index', doc_type='listing', id=new_consumer['id'],
             body=new_consumer)
    es.indices.refresh(index="listing_index")