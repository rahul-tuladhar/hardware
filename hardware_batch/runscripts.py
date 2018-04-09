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


while True:
    print('true')
    for message in consumer:
        new_consumer = json.loads((message.value).decode('utf-8'))
        print(json.loads((message.value).decode('utf-8')))
        es.index(index='listing_index', doc_type='listing', id=new_consumer['result']['id'], body=new_consumer['result'])
        es.indices.refresh(index="listing_index")