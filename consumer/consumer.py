from json import loads, dumps
from threading import Thread
from queue import Queue
from kafka import KafkaProducer
from kafka import KafkaConsumer


incoming_topic = 'input-topic'
outgoing_topic = 'output-topic'

clean_data = Queue()

consumer = KafkaConsumer(
	incoming_topic,
	bootstrap_servers=['kafka:9092'],
	group_id = 'my-group1',
	value_deserializer = lambda x: loads(x.decode('utf-8')),
	auto_offset_reset = 'earliest',
	enable_auto_commit = True,
	api_version=(5, 5, 0)
	)


new_producer = KafkaProducer(
	bootstrap_servers=['kafka:9092'],
	value_serializer=lambda x:dumps(x).encode('utf-8'),
	api_version=(5, 5, 0)
	)



def clean_read_data():
	print('processing malformed message')
	for msg in consumer:
		data = msg.value
		print(f'transforming {data}')
		if data['myTimestamp'] != '':
			a = data['myTimestamp'].split('T')
			b = a[1].replace('09','08')
			c = b.replace('+01','+00')
			data['myTimestamp'] = a[0]+'T'+c
		clean_data.put(data)

def new_publish():
	while True:
		new_producer.send(outgoing_topic, value=clean_data.get())
		new_producer.flush()


if __name__ == '__main__':
	process_thread = Thread(target=clean_read_data)
	process_thread.start()
	send_thread = Thread(target=new_publish)
	send_thread.start()


