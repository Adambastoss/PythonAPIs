from flask import Blueprint, jsonify

home = Blueprint("home", __name__)

@home.route("/home", methods=["GET"])
def hello_from_flask(): 
    return jsonify({
        'message': 'hello from flask'
    })

