from flask import Blueprint, jsonify, request
from app.services.usuarioService import criar_usuario, buscar_usuarios

usuario_bp = Blueprint('usuario_bp', __name__)

@usuario_bp.route("/usuarios", methods=["POST"])
def criar():
    dados = request.json
    usuario = criar_usuario(dados["nome"], dados["email"])
    return jsonify({"message": "Usuário criado!", "usuario": {"id": usuario.id, "nome": usuario.nome}})

@usuario_bp.route("/usuarios", methods=["GET"])
def listar():
    usuarios = buscar_usuarios()
    return jsonify([{"id": u.id, "nome": u.nome, "email": u.email} for u in usuarios])
