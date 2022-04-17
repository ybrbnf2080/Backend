# /bin/bash

docker-compose -f ./docker-compose.dev.yaml up  --build -d #--force-recreate 
docker-compose -f ./docker-compose.dev.yaml ps -a

