#python install----------
#FROM python:3.6 
#WORKDIR /usr/src/app

#COPY requirements.txt ./
#RUN pip install --no-cache-dir -r requirements.txt

#COPY . .

#CMD [ "python", "./loading_data.py" ]

#cron install----------
FROM ubuntu:latest

WORKDIR /usr/src/app

#apt-get install -y build-essential -y  python python-dev python-pip python-virtualenv libmysqlclient-dev curl&& \

RUN \
  apt-get update && \
  apt-get install -y build-essential -y git -y  python3.6 python-pip libproj-dev proj-data proj-bin libgeos++-dev libmysqlclient-dev curl&& \
  rm -rf /var/lib/apt/lists/*

COPY requirements.txt ./
RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

RUN  pip install pathlib    
RUN pip install git+https://github.com/xoolive/traffic

COPY . .

# Install cron
RUN apt-get update
RUN apt-get install cron

# Add crontab file in the cron directory
ADD crontab /etc/cron.d/simple-cron

# Add shell script and grant execution rights
ADD script.sh /script.sh
RUN chmod +x /script.sh

# Give execution rights on the cron job
RUN chmod 0644 /etc/cron.d/simple-cron

# Create the log file to be able to run tail
RUN touch /var/log/cron.log

# Run the command on container startup
CMD cron && tail -f /var/log/cron.log

