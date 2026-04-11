##### CREATING A DOCKER VOLUME
`docker volume create db`

##### LISTING VOLUMES
`docker volume ls`

##### CREATING A MONGO CONTAINER WITH AN ATTATCHED VOLUME
`docker run --name mongodb -v db:/data/db -d mongo:latest`

*-v* - indica que o container está sendo criado anexado ao volume db
*/data/db* - dir padrão utilizado pelo mongo para armazenar infos

##### REMOVING VOLUME
`docker volume rm db`

