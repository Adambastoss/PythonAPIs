from flask import Flask, Blueprint, request, jsonify
from config.database import get_conn

insert = Blueprint("insert_users", __name__)


@insert.route("/users/insert", methods=["POST"])
def add_user():
    db = get_conn('pessoa')
    user = dict(request.json)
    db.users.insert_one(user)
    
    return jsonify({'ACK': 'Usuário inserido com sucesso', 'usuário': dict(request.json)})