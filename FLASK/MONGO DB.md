### Creating a local representation of MongoDB, without installation.

#### Instaling modules
**pip install montydb pymongo**

#### Creating a new connection
**client = montydb.MontyClient()**

#### Creating a new database
**db = client.get_database('*pessoa*')**

#### Creating a new collection
**db.*users*.insert_one({'username': '*adambastoss*', 'password': '*123456*' ,  'name': 'Adam Bastos'})**

#### Consulting all records
**for registro in db.users.find():**
	**print(registro)**



##### Running mongo container with docker
`docker run --name mongodb -d mongo:latest`

Access mongo container filesystem
`docker exec -it mongodb bash`

Access mongo shell
`mongosh`