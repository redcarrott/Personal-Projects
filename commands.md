create Docker image
*The ’-t’ option allows you to define the name of your image.*
`$ docker build -t python-test . `

run Docker image
`docker run python-test`

## Useful commands for Docker

list images
`$ docker image ls`

delete a specific image
`$ docker image rm [image name]`

delete all existing images
`$ docker image rm $(docker images -a -q)`

list all existing containers (running and not running)
`$ docker ps -a`

stop a specific container
`$ docker stop [container name]`

stop all running containers
`$ docker stop $(docker ps -a -q)`

delete a specfic container (only if stopped)
`$ docker rm [container name]`

delete all containers (only if stopped)
`$ docker rm $(docker ps -a -q)`

display logs of a container
`$ docker logs [container name]`
