# docker_mysql_icarus

Project Icarus was built to track flight data from the OpenSky Network. Data is urrently logged every minute to track trajectories. Future ClickHouse integration coming.

1. make sure you installed docker on your ubuntu machine
2. clone the repo
3. cd into repo
4. build docker image `docker build -t mysql_docker_image .`
5. run docker container `docker run -p 3306:3306  -e MYSQL_ROOT_PASSWORD=yourPassword --name icarus -d mysql_docker_image`
