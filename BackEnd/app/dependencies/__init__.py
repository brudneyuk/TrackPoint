import subprocess
import sys

# Lista de pacotes necessários
REQUIRED_PACKAGES = [
    "flask",
    "flask-sqlalchemy",
    "cryptography",
    "pymysql",  # Para MySQL
]

def install_missing_packages():
    """Verifica e instala pacotes necessários automaticamente."""
    for package in REQUIRED_PACKAGES:
        try:
            __import__(package)
        except ImportError:
            print(f"📦 Instalando {package}...")
            subprocess.check_call([sys.executable, "-m", "pip", "install", package])

# Instala os pacotes ao importar o package
install_missing_packages()
