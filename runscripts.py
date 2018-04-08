from kafka import KafkaConsumer
from elasticsearch import Elasticsearch

es = Elasticsearch(['es'])
while True:
    # index the message from the consumer in an infinite loop
    consumer = KafkaConsumer('new-listings-topic', group_id='listing-indexer', bootstrap_servers=['kafka:9092'])
    for message in consumer:
        es.index(index='listing_index', doc_type='listing', id=message['id'], body=message)
    es.indices.refresh(index="listing_index")
