#!/bin/bash

URL="http://localhost:8000/api/v1/joke/invoke"
MAX_RETRIES=5
DELAY=2

for i in $(seq 1 $MAX_RETRIES); do
    echo "Attempt $i: Checking server..."
    
    response=$(curl -s -o /dev/null -w "%{http_code}" --location --request POST "$URL" \
        --header 'Content-Type: application/json' \
        --data-raw '{
            "input": {
                "topic": "cats"
            }
        }')
    
    if [ "$response" -eq 200 ]; then
        echo "Server is up and running!"
        echo "Response:"
        curl -s --location --request POST "$URL" \
            --header 'Content-Type: application/json' \
            --data-raw '{
                "input": {
                    "topic": "cats"
                }
            }'
        echo ""
        exit 0
    else
        echo "Server responded with status code $response"
        if [ $i -lt $MAX_RETRIES ]; then
            echo "Retrying in $DELAY seconds..."
            sleep $DELAY
        fi
    fi
done

echo "Server validation failed after maximum retries."
exit 1