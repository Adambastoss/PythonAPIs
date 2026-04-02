### Creating a local representation of MongoDB, without installation.

#### Instaling modules
**pip install montydb pymongo**

#### Creating a new connection
**client = montydb.MontyClient()**

#### Creating a new database
**db = client.get_database('*namedb*')**

#### Creating a new collection
**db.*name_collection*.insert_one({'username': '*nameuser*', 'password': '*passuser*' })**

#### Consulting all records
**for registro in db.users.find():**
	**print(registro)**

