from flask import Flask, jsonify, Blueprint
from config.database import get_conn

delete = Blueprint("delete_users", __name__)


@delete.route("/users/delete/<username>", methods=["DELETE"])
def delete_by_username(username):
    db = get_conn('pessoa')

    result = db.users.delete_one({'username': username})

    if result.deleted_count == 0:
        return jsonify({'error': 'Usuário não encontrado'}), 404

    return jsonify({'message': 'Usuário deletado com sucesso!'}), 200