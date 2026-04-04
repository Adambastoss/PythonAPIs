from flask import Flask, Blueprint, jsonify, request
from config.database import get_conn

update = Blueprint("update_users", __name__)

@update.route("/users/update/<username>", methods=["PUT"])
def update_user(username):
    db = get_conn('pessoa') #Conecta ao banco

    data = request.get_json() #Captura do payload, Converte o JSON recebido para dict:

    if not data: #Garante que o cliente enviou os dados e não atualiza com vazio
        return jsonify({'error': 'Payload inválido ou ausente'}), 400

    #Atualiza no banco
    result = db.users.update_one( 
        {'username': username}, #Filtra por username
        {'$set': data}          #Atualiza apenas os campos enviados
    )

    if result.matched_count == 0:
        return jsonify({'error': 'Usuário não encontrado'}), 404

    return jsonify({'message': 'Usuário atualizado com sucesso'}), 200

