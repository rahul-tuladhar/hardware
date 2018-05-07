from kafka import KafkaConsumer
import time
import json

while True:
    try:
        consumer = KafkaConsumer('co-view-topic', bootstrap_servers=['kafka:9092'])
        print(consumer)
        break
    except:
        time.sleep(5)
print('true1')

while True:
    print('true2')
    for message in consumer:
        with open("data.txt", "a+") as data:
            print('true3')
            new_consumer = json.loads(message.value.decode('utf-8'))
            print(new_consumer)
            print(new_consumer['result']['id'])
            print(new_consumer['user_id'])
            item_id = new_consumer['result']['id']
            user_id = new_consumer['user_id']
            data.write("%s \t %s \n" % (user_id, item_id))

