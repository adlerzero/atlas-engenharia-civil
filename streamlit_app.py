"""
ATLAS - Suíte de Engenharia Civil Integrada
Arquivo alternativo para Streamlit Cloud (se necessário)
"""

# Este arquivo é um fallback - o app.py principal deve funcionar
# Se o Streamlit Cloud não detectar app.py, pode usar este arquivo

import sys
import os

# Garantir que o path está correto
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

# Importar o app principal
from app import main

if __name__ == "__main__":
    main()

