# Using Docker Secrets

This project is a sample application, which is using Docker secrets. Blog post can be found [here](http://bit.ly/2kLd2Tw).

```
docker build -t amaksimov/docker_secrets_example::v0.1 . 
LC_ALL=C < /dev/urandom  tr -dc '_A-Z-a-z-0-9' | head -c 32 | docker secret create db-password -
docker service create --name docker_secrets_example -p 5000:5000 --secret db-password amaksimov/docker_secrets_example:v0.1
```
