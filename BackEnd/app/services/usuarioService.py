from app.repositories.usuarioRepository import salvar_usuario, listar_usuarios
from app.models.usuario import Usuario
from config.database import db

def criar_usuario(nome, email, senha, cargo):
    usuario = Usuario(nome=nome, email=email, cargo=cargo)
    usuario.set_senha(senha)  # Chama o método para criptografar a senha
    db.session.add(usuario)
    db.session.commit()
    return usuario

def buscar_usuarios():
    return listar_usuarios()

def buscar_usuario_por_email(email):
    return Usuario.query.filter_by(email=email).first()