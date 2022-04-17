# /bin/bash

docker-compose -f ./docker-compose.dev.yaml up  --build --force-recreate -d
docker-compose -f ./docker-compose.dev.yaml ps -a

