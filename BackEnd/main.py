import subprocess
import sys

# Lista de pacotes necessários
REQUIRED_PACKAGES = [
    "flask",
    "flask-sqlalchemy",
    "cryptography",
    "pymysql",  # Se estiver usando MySQL
    "psycopg2-binary"  # Se estiver usando PostgreSQL
]

def install_missing_packages():
    """Verifica e instala pacotes necessários."""
    for package in REQUIRED_PACKAGES:
        try:
            __import__(package)
        except ImportError:
            print(f"📦 Instalando {package}...")
            subprocess.check_call([sys.executable, "-m", "pip", "install", package])

# Instala pacotes antes de rodar a aplicação
install_missing_packages()

from flask import Flask
from app.controllers.usuarioContrroller import usuario_bp
from config.database import init_db

app = Flask(__name__)

# Inicializar banco de dados
init_db(app)

# Registrar os controllers
app.register_blueprint(usuario_bp)

if __name__ == "__main__":
    app.run(debug=True)
