import sys
import subprocess

# Funkce pro instalaci balíčků
def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

# Seznam balíčků k instalaci
required_packages = [
    "PyQt5",
    "selenium",
    "webdriver-manager"
]

# Instalace balíčků
for package in required_packages:
    try:
        __import__(package)
    except ImportError:
        install(package)
