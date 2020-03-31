# docker_mysql_icarus

Project Icarus was built to track flight data from the OpenSky Network. Data is currently logged every minute to track trajectories. A second python cron container is nested in this repo. Future build will be set via docker compose for a simpler setup. Future ClickHouse integration coming.

General process information: Data is pulled with `python` in a dockerized container and loaded into another `mysql` docker container, specifically a staging table. Python also executes stored procedures to validate and move data into production as well as clear staging. Cron handles the execution of the python script. Edit the `python_container/crontab` file if you wish to change the frequency of the cronjob.

1. make sure you installed docker on your ubuntu machine
2. clone the repo
3. cd into repo
4. create a network bridge to link your containers `docker network create my-net`
5. Build a mysql container and then create a docker service for the mysql container 

```
  docker build -t mysql .
  docker create --name mysql \
    --network my-net \
    --publish 3306:3306 \
    -e MYSQL_ROOT_PASSWORD=password \
    mysql:latest
```

6. change directories `cd python_container` directory and repeat for python: 

```
  docker build -t docker-cron .
  docker create --name docker-cron \
    --network my-net \
    docker-cron:latest
```

7. run both containers: `docker start mysql` and `docker start docker-cron`
8. check that your containers are running with `docker ps`
9. double check the docker-cron logs by entering container 

```
   docker exec -i -t yourContainerId /bin/bash
   root@b149b5e7306d:/# cat /var/log/cron.log 
    i am running every minute...
    SUCCESSFULLY LOADED DATA INTO STAGING...
    SUCCESSFULLY INSERTED DATA INTO PRODUCTION...
    SUCCESSFULLY DELETED STAGE DATA...
```

10. If you ever want to stop or restart the database ETL procedure simply use `docker stop docker-cron` and `docker start docker-cron` 