## Steps to start up the application
This application is built on 1 broker and 2 topics architecture as stated in the problem statement.
Both "input-topic" and "output-topic" are created using the docker-compose environment variable available in the mage used
File structure include 
- producer.py
- consumer.py
- docker compose yml file
- Dockerfile
- Makefile
- requirement.txt file

### Docker
#### Starting cluster
I have mask my docker and kafka commands using "make" for easier access. If you have make installed, kindly run the following commands 
from the project root where the makefile resides
- to build the docker config file, run
	```bash 
	make build
	```
- to start the kafka cluster and application, run
	```bash 
	make up
	```
- to list all running containers, run
	```bash 
	make list
	```
- to list the malformed data to be cleaned, run
	```bash 
	make input-topic
	```
- to list the cleaned data run
	```bash 
	make output-topic
	```
- to stop and shut down the kafka cluster and application, run
	```bash 
	make down
	```

If you do not have "make" installed, please run the following command from your command prompt from the project root
- to build the docker config file, run
	```bash 
	docker-compose build
	```
- to start the kafka cluster and application, run
	```bash 
	docker-compose up -d
	```
- to list all running containers, run
	```bash 
	docker ps
	```
- to list the malformed data to be cleaned, run
	```bash 
	docker exec -it kafka opt/kafka_2.13-2.8.1/bin/kafka-console-consumer.sh --bootstrap-server kafka:9092 --topic input-topic --from-beginning
	```
- to list the cleaned data, run
	```bash 
	docker exec -it kafka opt/kafka_2.13-2.8.1/bin/kafka-console-consumer.sh --bootstrap-server kafka:9092 --topic output-topic --from-beginning
	```
- to stop and shut down the kafka cluster and application, run
	```bash 
	docker-compose down
	```

#### Reading the malformed data
The malformed data are passed into a list and the producer worker consume and publish it to the topic from the already specified list.
