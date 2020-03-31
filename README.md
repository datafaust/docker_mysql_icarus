# docker_mysql_icarus

Project Icarus was built to track flight data from the OpenSky Network. Data is urrently logged every minute to track trajectories. A second python cron container is nested in this repo. Future build will be set via docker compose. Future ClickHouse integration coming . . . 

1. make sure you installed docker on your ubuntu machine
2. clone the repo
3. cd into repo
4. build docker image `docker build -t mysql .`
5. create a network bridge to link your containers `docker network create my-net`
5. create a docker service for the mysql container ```docker create --name mysql \
  --network my-net \
  --publish 3306:3306 \
  -e MYSQL_ROOT_PASSWORD=password \
  mysql:latest```
6. cd into the `python_container` directory and create another docker service for python: `docker create --name docker-cron \
  --network my-net \
  docker-cron:latest`
7. run both containers: `docker start mysql` and `docker start docker-cron`
8. check that your containers are running with `docker ps`
9. double check the docker-cron logs by entering container `docker exec -i -t yourContainerId /bin/bash`
10. `root@b149b5e7306d:/# cat /var/log/cron.log Thu May 26 13:11:01 UTC 2016: executed script`
