from kafka import KafkaConsumer
from elasticsearch import Elasticsearch
import time
import json
#
# # time.sleep(50)
#
es = Elasticsearch(['es'])
consumer = KafkaConsumer('new-listings-topic', group_id='listing-indexer', bootstrap_servers=['kafka:9092'])
while True:
    print('yes')

    # es.indices.refresh(index="listing_index")
    try:
        for message in consumer:
            new_consumer = json.loads(message).decode('utf-8')
            # print(new_consumer)
            # print(json.loads((message.value).decode('utf-8')))
            es.index(index='listing_index', doc_type='listing', id=new_consumer['result']['id'], body=new_consumer['result'])
            es.indices.refresh(index="listing_index")
    except RuntimeError:
        print('what the')