from flask import Blueprint, jsonify, request

from app.services.usuarioService import criar_usuario, buscar_usuarios, buscar_usuario_por_email

usuario_bp = Blueprint('usuario_bp', __name__)

BLACKLIST = set()

@usuario_bp.route("/usuarios", methods=["POST"])
def criar():
    dados = request.json

    # Verifica se todos os campos obrigatórios estão presentes
    if not all(k in dados for k in ["nome", "email", "senha", "cargo"]):
        return jsonify({"error": "Nome, e-mail, senha e cargo são obrigatórios"}), 400

    try:
        # Verifica se já existe um usuário com o e-mail fornecido
        if buscar_usuario_por_email(dados["email"]):  # Corrigido para passar apenas o e-mail
            return jsonify({"error": "E-mail já está em uso"}), 400

        # Criar usuário com os dados fornecidos
        usuario = criar_usuario(dados["nome"], dados["email"], dados["senha"], dados["cargo"])

        return jsonify({
            "message": "Usuário criado!",
            "usuario": {
                "nome": usuario.nome,
                "email": usuario.email,
                "cargo": usuario.cargo.value  # Certificando-se de retornar a string do Enum Cargo
            }
        }), 201  # Código 201 indica criação bem-sucedida

    except Exception as e:
        return jsonify({"error": str(e)}), 400  # Retorna erro caso algo dê errado


@usuario_bp.route("/usuarios", methods=["GET"])
def listar():
    usuarios = buscar_usuarios()
    return jsonify([
        {
            "nome": u.nome,
            "email": u.email,
            "cargo": u.cargo.value,  # Certificando-se de retornar a string do Enum Cargo
            "logado": u.logado,
            "data_criacao": u.data_criacao.strftime("%d/%m/%Y %H:%M:%S") if u.data_criacao else None,
            "data_atualizacao": u.data_atualizacao.strftime("%d/%m/%Y %H:%M:%S") if u.data_atualizacao else None,
            "data_ultimo_login": u.data_ultimo_login.strftime("%d/%m/%Y %H:%M:%S") if not u.logado else None
        }
        for u in usuarios
    ])

# @usuario_bp.route("/usuarios/listar-nome-ou-email", methods=["GET"])
# def listar_por_nome_ou_email():
#     nome = request.args.get("nome")
#     email = request.args.get("email")
#
#     if not nome and not email:
#         return jsonify({"error": "Nome ou e-mail devem ser fornecidos"}), 400
#
#     usuarios = buscar_usuarios()
#     usuarios_filtrados = [
#         {
#             "nome": u.nome,
#             "email": u.email,
#             "cargo": u.cargo.value,
#             "logado": u.logado,
#             "data_criacao": u.data_criacao.strftime("%d/%m/%Y %H:%M:%S") if u.data_criacao else None,
#             "data_atualizacao": u.data_atualizacao.strftime("%d/%m/%Y %H:%M:%S") if u.data_atualizacao else None,
#             "data_ultimo_login": u.data_ultimo_login.strftime("%d/%m/%Y %H:%M:%S") if not u.logado else None
#         }
#         for u in usuarios
#         if (nome and nome.lower() in u.nome.lower()) or (email and email.lower() in u.email.lower())
#     ]
#
#     return jsonify(usuarios_filtrados)
