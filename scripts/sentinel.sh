#!/bin/bash

fswatch /tmp/html --event=Created | while read file; do
    curl --location 'http://dispatcher:8002/dispatcher/deliver' \
    --header 'Authorization: Bearer MYTOKEN' \
    --header 'Content-Type: application/json' \
    --data "{
        \"broker\": \"rabbitmq\",
        \"file\": \"${file}\",
        \"event\": \"created\"
    }"
    echo "Event sent! $(date)" 
done
