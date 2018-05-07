from elasticsearch import Elasticsearch
import time
import json

# Tries to get consumer freeze process if not able
while True:
    try:
        es = Elasticsearch(['es'])
        break
    except:
        print('elastic')
        time.sleep(5)
time.sleep(180)
with open('fixtures.json', encoding='utf-8') as data_file:
    data = json.loads(data_file.read())
for post in data:
    # print(post)
    try:
        if post['model'] == 'posts.post':
            print(post['fields'])
            print(post['pk'])
            es.index(index='listing_index', doc_type='listing', id=post['pk'], body=post['fields'])
            print(post['fields'])
            es.indices.refresh(index="listing_index")
    except:
        print('error in index')

# f = json.load(open('data.json'))
