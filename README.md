# thinkbox
A flask application which allows for messages to be submitted in the browser and viewed by other users. It has been created to serve as an exercise in building a flask application which interacts with a postgres database and deploying it using docker.

This website was designed to be a simple website which stores and gets user input from the database.

It can also be easily deployed using the included docker compose file. Simply rename `example.env` and assign values where needed.
Then use `docker build -t thinkbox .` to build the docker container and `docker compose up -d` to start both the container and the database. Also make sure you configure a reverse proxy if you would like to use https

Keep in mind that this docker compose file binds to the port and will override firewalls like ufw. See [here](https://askubuntu.com/questions/652556/uncomplicated-firewall-ufw-is-not-blocking-anything-when-using-docker) for more info.