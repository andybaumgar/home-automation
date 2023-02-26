docker stop air-gradient-agent
docker rm air-gradient-agent
docker build -t air-gradient-agent .
docker run -d --name air-gradient-agent -p 9926:9926 --privileged --network=host --restart unless-stopped air-gradient-agent