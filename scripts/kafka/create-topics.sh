#!/bin/sh
# create-topics.sh

ZOOKEEPER='zookeeper:2181'
CONFIG='/scripts/topics.config'

function logger() {
    echo $(date +'%d/%m/%Y %T') '>' $1'.'
}

function create_topics() {
    logger 'Creating topics'

    awk -F':' -v zookeeper="$ZOOKEEPER" '{system("kafka-topics --bootstrap-server=kafka:9092 --create --topic=" $1 " --partitions=" $2 " --replication-factor=" $3 " --if-not-exists") }' $CONFIG

    logger 'Topics were created'
}

function update_topics() {
    logger 'Updating topics'

    awk -F':' -v zookeeper="$ZOOKEEPER" '{system("kafka-topics --bootstrap-server=kafka:9092 --alter --topic=" $1 " --partitions=" $2) }' $CONFIG &> /tmp/errors.log

    logger 'Topics were updated'
}

function init_topics() {
    sleep 30
    create_topics
    update_topics
}

function start_kafka() {
    logger 'Starting kafka'
    /etc/confluent/docker/run
}

init_topics & start_kafka