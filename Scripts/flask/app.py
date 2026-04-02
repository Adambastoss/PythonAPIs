import flask

app = flask.Flask(__name__)

@app.route("/", methods=["GET"])
def hello_from_flask(): 
    return flask.jsonify({
        'message': 'hello from flask'
    })

if __name__ == '__main__':
    app.run()