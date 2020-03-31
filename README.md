# docker_mysql_icarus

Project Icarus was built to track flight data from the OpenSky Network. Data is urrently logged every minute to track trajectories. A second python cron container is nested in this repo. Future build will be set via docker compose. Future ClickHouse integration coming . . . 

1. make sure you installed docker on your ubuntu machine
2. clone the repo
3. cd into repo
4. build docker image `docker build -t mysql .`
5. create a network bridge to link your containers `docker network create my-net`
6. create a docker service for the mysql container 

```
  docker create --name mysql \
    --network my-net \
    --publish 3306:3306 \
    -e MYSQL_ROOT_PASSWORD=password \
    mysql:latest
```

7. change directories `cd python_container` directory and create another docker service for python: 

```
  docker create --name docker-cron \
    --network my-net \
    docker-cron:latest
```

8. run both containers: `docker start mysql` and `docker start docker-cron`
9. check that your containers are running with `docker ps`
10. double check the docker-cron logs by entering container 

```
   docker exec -i -t yourContainerId /bin/bash
   root@b149b5e7306d:/# cat /var/log/cron.log 
    i am running every minute...
    SUCCESSFULLY LOADED DATA INTO STAGING...
    SUCCESSFULLY INSERTED DATA INTO PRODUCTION...
    SUCCESSFULLY DELETED STAGE DATA...
```
