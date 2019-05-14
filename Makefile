all: build run

build:
	docker build -t dnsapi:latest .

run:
	docker run -p 5000:5000 --rm dnsapi:latest

