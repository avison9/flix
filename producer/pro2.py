from time import sleep
from json import dumps
from kafka import KafkaProducer


producer = KafkaProducer(
	bootstrap_servers=['kafka:9092'],
	value_serializer=lambda x:dumps(x).encode('utf-8'),
	api_version=(5, 5, 0)
	)
producing_topic = 'input-topic'
wrong_data = [
	{"myKey": 1, "myTimestamp": "2022-03-01T09:11:04+01:00"},
	{"myKey": 2, "myTimestamp": "2022-03-01T09:12:08+01:00"},
	{"myKey": 3, "myTimestamp": "2022-03-01T09:13:12+01:00"},
	{"myKey": 4, "myTimestamp": ""},
	{"myKey": 5, "myTimestamp": "2022-03-01T09:14:05+01:00"},
]

for idx, msg in enumerate(wrong_data):
	print(f'sending message {idx}')
	producer.send(producing_topic,value=msg)
	sleep(2)

def test():
	pass