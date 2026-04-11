CREATE A NEW NETWORK
`docker network create --driver=bridge --subnet=200.100.0.0/16 nomerede`


CREATING A CONTAINER WITH A NETWORK ATTATCHED
`docker run -d --name flaskapp1 -v "$PWD":/app --network=novarede --ip=200.100.50.10 flaskapp`