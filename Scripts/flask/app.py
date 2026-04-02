import flask
import montydb

app = flask.Flask(__name__)


def get_conn(database):
    client = montydb.MontyClient()
    return client.get_database(database)

@app.route("/users", methods=["GET"])



@app.route("/", methods=["GET"])
def hello_from_flask(): 
    return flask.jsonify({
        'message': 'hello from flask'
    })

if __name__ == '__main__':
    app.run()