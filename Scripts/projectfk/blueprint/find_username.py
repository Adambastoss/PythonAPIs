from flask import Flask, Blueprint, jsonify, render_template
from config.database import get_conn

for_username = Blueprint("for_username", __name__)

@for_username.route("/users/<username>")
def get_user_by_username(username):
    db = get_conn('pessoa')
    users = [ 
        { 'username': user.get('username'), 
         'password': user.get('password'), 
         'name': user.get('name') 
         } for user in db.users.find({"username": username}) 
    ] 
    return jsonify(users)