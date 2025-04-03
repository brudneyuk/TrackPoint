from app.repositories.usuarioRepository import salvar_usuario, listar_usuarios
from app.models.usuario import Usuario

def criar_usuario(nome, email):
    usuario = Usuario(nome=nome, email=email)
    return salvar_usuario(usuario)

def buscar_usuarios():
    return listar_usuarios()
