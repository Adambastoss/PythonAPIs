from flask import Flask
from blueprint.home import home
from blueprint.delete_users import delete
from blueprint.insert_users import insert
from blueprint.update_users import update
from blueprint.read_users import read
from blueprint.find_username import for_username


app = Flask(__name__)

app.register_blueprint(home)
app.register_blueprint(delete)
app.register_blueprint(insert)
app.register_blueprint(update)
app.register_blueprint(read)
app.register_blueprint(for_username)


if __name__ == '__main__':
    app.run()

