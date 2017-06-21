# Download MySQL image from hub.docker.com.
#docker pull mysql/mysql-server

# Stop mysql-container
#[ "$(docker ps | grep mysql-container)" ] && docker stop mysql-container

# Remove mysql-container
#[ "$(docker ps | grep mysql-container)" ] && docker rm mysql-container


#[ "$(docker ps -a | grep mysql-container)" ] && docker ps -a| grep mysql-container| awk '{print $1}'| xargs docker rm

# Run MySQL container in user's system.
sudo docker run --name mysql-container -p 3306:3306 -e MYSQL_ROOT_PASSWORD=secret -e MYSQL_ROOT_HOST="%" -d mysql/mysql-server:latest
