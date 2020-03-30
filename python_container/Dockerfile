#cron install----------
FROM ubuntu:latest

# Install cron
RUN apt-get update
RUN apt-get install cron

# Add crontab file in the cron directory
ADD crontab /etc/cron.d/simple-cron

# Add shell script and grant execution rights
#ADD script.sh /script.sh
#RUN chmod +x /script.sh
ADD  loading_data.py /loading_data.py
RUN chmod +x /loading_data.py

# Give execution rights on the cron job
RUN chmod 0644 /etc/cron.d/simple-cron

# Create the log file to be able to run tail
RUN touch /var/log/cron.log

# Run the command on container startup
CMD cron && tail -f /var/log/cron.log

#python install----------
FROM python:3.6 
WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD [ "python", "./loading_data.py" ]
