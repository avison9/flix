.PHONY: build
build:
	docker-compose build

.PHONY: down
down:
	@docker-compose down

.PHONY: up
up: 
	@docker-compose up -d

.PHONY: list
list: 
	docker ps

.PHONY: host
host: 
	docker exec -it kafka bash

.PHONY: input-topic
input-topic: 
	docker exec -it kafka opt/kafka_2.13-2.8.1/bin/kafka-console-consumer.sh --bootstrap-server kafka:9092 --topic input-topic --from-beginning

.PHONY: output-topic
output-topic: 
	docker exec -it kafka opt/kafka_2.13-2.8.1/bin/kafka-console-consumer.sh --bootstrap-server kafka:9092 --topic output-topic --from-beginning