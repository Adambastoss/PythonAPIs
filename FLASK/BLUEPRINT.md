#### DESIGN STANDARD

##### IMPORT  in each route file
`from flask import Flask, Blueprint`


projectfk
│   ├── app.py
│   ├── blueprint
│   │   ├── delete_users.py
│   │   ├── *update_users.py*
│   │   ├── create_users.py
│   │   ├── read_users.py

##### CREATE in each route file an instance of blueprint ()
`update = Blueprint("update_users", __name__)`

##### BEFORE
`@app.route("/users/update/<username>", methods=["PUT"])`


##### LATER
`@update.route("/users/update/<username>", methods=["PUT"])`


#### IN app.py file
`from blueprint.update_users import update`
`app.register_blueprint(update)`


