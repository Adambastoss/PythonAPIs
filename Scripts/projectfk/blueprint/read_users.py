from flask import Flask, Blueprint, jsonify, render_template
from config.database import get_conn

read = Blueprint("read_users", __name__)

@read.route("/users") #Para indicarmos um campo que vai sempre variar de acordo com a chamada, utilizamos os sinais <> como em <username>
def get_users():
    db = get_conn('pessoa')
    users = [
        {
            'username': user.get('username'),
            'password': user.get('password'),
            'name': user.get('name')
        } for user in db.users.find()
    ]
    return render_template("users.html", context=users) #definindo o context que está fazendo a chamada no users.html