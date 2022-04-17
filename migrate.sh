# /bin/bash

docker exec -i backend_server_1 /bin/bash -c "alembic stamp head"
docker exec -i backend_server_1 /bin/bash -c "alembic revision --message='Update migrate in github action' --autogenerate"
docker exec -i backend_server_1 /bin/bash -c "alembic upgrade head"