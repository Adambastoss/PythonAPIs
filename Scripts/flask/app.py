import flask
import montydb

app = flask.Flask(__name__)


def get_conn(database):
    client = montydb.MontyClient()
    return client.get_database(database)

@app.route("/users", methods=["GET"])
def get_users():
    db = get_conn('pessoa')
    users = [
        {
            'username': user.get('username'),
            'password': user.get('password'),
            'name': user.get('name')
        } for user in db.users.find()
    ]


@app.route("/", methods=["GET"])
def hello_from_flask(): 
    return flask.jsonify({
        'message': 'hello from flask'
    })

if __name__ == '__main__':
    app.run()