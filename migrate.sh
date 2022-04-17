# /bin/bash

docker exec -i api /bin/bash -c "alembic stamp head"
docker exec -i api /bin/bash -c "alembic revision --message='Update migrate in github action' --autogenerate"
docker exec -i api /bin/bash -c "alembic upgrade head"