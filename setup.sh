#!/bin/bash
# Script de setup para o ATLAS

echo "🏗️  Configurando o ATLAS - Suíte de Engenharia Civil Integrada"
echo ""

# Verificar Python
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 não encontrado. Por favor, instale Python 3.10 ou superior."
    exit 1
fi

echo "✅ Python encontrado: $(python3 --version)"
echo ""

# Criar ambiente virtual se não existir
if [ ! -d "venv" ]; then
    echo "📦 Criando ambiente virtual..."
    python3 -m venv venv
    echo "✅ Ambiente virtual criado"
else
    echo "✅ Ambiente virtual já existe"
fi

echo ""
echo "📥 Instalando dependências..."
source venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt

echo ""
echo "✅ Instalação concluída!"
echo ""
echo "🚀 Para executar a aplicação:"
echo "   1. Ative o ambiente virtual: source venv/bin/activate"
echo "   2. Execute: streamlit run app.py"
echo ""

