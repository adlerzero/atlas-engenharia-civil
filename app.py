"""
ATLAS - Suíte de Engenharia Civil Integrada
Aplicação web para acompanhamento durante o curso de Engenharia Civil
"""

import streamlit as st
import random
import sys
import os

# Adicionar o diretório atual ao path para imports
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

# Configuração da página
st.set_page_config(
    page_title="ATLAS - Engenharia Civil",
    page_icon="🏗️",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': None,
        'Report a bug': None,
        'About': "ATLAS v1.0 - Suíte de Engenharia Civil Integrada"
    }
)

# CSS customizado para melhorar o visual
st.markdown("""
<style>
    /* Importar fonte moderna */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap');
    
    /* Aplicar fonte global */
    .stApp {
        font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
    }
    
    /* Melhorar títulos principais */
    h1 {
        color: #1f77b4 !important;
        font-weight: 800 !important;
        border-bottom: 4px solid #1f77b4;
        padding-bottom: 15px;
        margin-bottom: 25px;
        font-size: 2.5rem !important;
    }
    
    h2 {
        color: #2c3e50 !important;
        font-weight: 700 !important;
        margin-top: 35px;
        margin-bottom: 20px;
        font-size: 1.8rem !important;
    }
    
    h3 {
        color: #34495e !important;
        font-weight: 600 !important;
        font-size: 1.4rem !important;
    }
    
    /* Melhorar métricas */
    [data-testid="stMetricValue"] {
        font-size: 2.2rem !important;
        font-weight: 700 !important;
        color: #1f77b4 !important;
    }
    
    [data-testid="stMetricLabel"] {
        font-size: 0.95rem !important;
        color: #7f8c8d !important;
        font-weight: 500 !important;
        text-transform: uppercase;
        letter-spacing: 0.5px;
    }
    
    /* Melhorar botões */
    .stButton > button {
        background: linear-gradient(135deg, #1f77b4 0%, #1565c0 100%) !important;
        color: white !important;
        border-radius: 10px !important;
        padding: 0.6rem 2.5rem !important;
        font-weight: 600 !important;
        font-size: 1rem !important;
        transition: all 0.3s ease !important;
        border: none !important;
        box-shadow: 0 4px 6px rgba(31, 119, 180, 0.2) !important;
    }
    
    .stButton > button:hover {
        background: linear-gradient(135deg, #1565c0 0%, #0d47a1 100%) !important;
        transform: translateY(-2px);
        box-shadow: 0 6px 12px rgba(31, 119, 180, 0.4) !important;
    }
    
    /* Melhorar inputs */
    .stNumberInput > div > div > input,
    .stTextInput > div > div > input {
        border-radius: 8px !important;
        border: 2px solid #e0e0e0 !important;
        transition: all 0.3s ease !important;
        padding: 0.5rem !important;
    }
    
    .stNumberInput > div > div > input:focus,
    .stTextInput > div > div > input:focus {
        border-color: #1f77b4 !important;
        box-shadow: 0 0 0 4px rgba(31, 119, 180, 0.1) !important;
    }
    
    /* Melhorar sidebar */
    [data-testid="stSidebar"] {
        background: linear-gradient(180deg, #1f77b4 0%, #0d47a1 100%) !important;
    }
    
    [data-testid="stSidebar"] [data-testid="stMarkdownContainer"] {
        color: white !important;
    }
    
    [data-testid="stSidebar"] .stRadio label {
        color: white !important;
        font-weight: 500 !important;
    }
    
    [data-testid="stSidebar"] h1,
    [data-testid="stSidebar"] h2,
    [data-testid="stSidebar"] h3 {
        color: white !important;
    }
    
    /* Melhorar tabs */
    .stTabs [data-baseweb="tab-list"] {
        gap: 12px;
        background-color: #f8f9fa;
        padding: 8px;
        border-radius: 10px;
    }
    
    .stTabs [data-baseweb="tab"] {
        border-radius: 8px !important;
        padding: 12px 28px !important;
        font-weight: 600 !important;
        transition: all 0.3s ease !important;
    }
    
    .stTabs [aria-selected="true"] {
        background: linear-gradient(135deg, #1f77b4 0%, #1565c0 100%) !important;
        color: white !important;
        box-shadow: 0 4px 8px rgba(31, 119, 180, 0.3) !important;
    }
    
    /* Melhorar info boxes */
    .stInfo {
        background: linear-gradient(135deg, #e3f2fd 0%, #bbdefb 100%) !important;
        border-left: 5px solid #1f77b4 !important;
        border-radius: 10px !important;
        padding: 1.2rem !important;
        box-shadow: 0 2px 8px rgba(0,0,0,0.1) !important;
    }
    
    .stSuccess {
        background: linear-gradient(135deg, #e8f5e9 0%, #c8e6c9 100%) !important;
        border-left: 5px solid #4caf50 !important;
        border-radius: 10px !important;
        padding: 1.2rem !important;
    }
    
    .stWarning {
        background: linear-gradient(135deg, #fff3e0 0%, #ffe0b2 100%) !important;
        border-left: 5px solid #ff9800 !important;
        border-radius: 10px !important;
        padding: 1.2rem !important;
    }
    
    .stError {
        background: linear-gradient(135deg, #ffebee 0%, #ffcdd2 100%) !important;
        border-left: 5px solid #f44336 !important;
        border-radius: 10px !important;
        padding: 1.2rem !important;
    }
    
    /* Melhorar tabelas */
    [data-testid="stDataFrame"] {
        border-radius: 10px !important;
        overflow: hidden !important;
        box-shadow: 0 4px 12px rgba(0,0,0,0.1) !important;
    }
    
    /* Melhorar expansores */
    .streamlit-expanderHeader {
        background: linear-gradient(135deg, #f8f9fa 0%, #e9ecef 100%) !important;
        border-radius: 8px !important;
        font-weight: 600 !important;
        color: #1f77b4 !important;
        padding: 12px !important;
    }
    
    /* Cards de métricas com hover */
    [data-testid="metric-container"] {
        background: linear-gradient(135deg, #ffffff 0%, #f8f9fa 100%) !important;
        border-radius: 15px !important;
        padding: 1.5rem !important;
        box-shadow: 0 4px 12px rgba(0,0,0,0.1) !important;
        transition: all 0.3s ease !important;
        border: 1px solid #e0e0e0 !important;
    }
    
    [data-testid="metric-container"]:hover {
        transform: translateY(-5px);
        box-shadow: 0 8px 20px rgba(31, 119, 180, 0.2) !important;
        border-color: #1f77b4 !important;
    }
    
    /* Scrollbar customizada */
    ::-webkit-scrollbar {
        width: 12px;
        height: 12px;
    }
    
    ::-webkit-scrollbar-track {
        background: #f1f1f1;
        border-radius: 10px;
    }
    
    ::-webkit-scrollbar-thumb {
        background: linear-gradient(180deg, #1f77b4 0%, #1565c0 100%);
        border-radius: 10px;
    }
    
    ::-webkit-scrollbar-thumb:hover {
        background: linear-gradient(180deg, #1565c0 0%, #0d47a1 100%);
    }
    
    /* Animações suaves */
    @keyframes fadeIn {
        from {
            opacity: 0;
            transform: translateY(15px);
        }
        to {
            opacity: 1;
            transform: translateY(0);
        }
    }
    
    [data-testid="stMarkdownContainer"] {
        animation: fadeIn 0.6s ease-in;
    }
    
    /* Melhorar código LaTeX */
    .katex {
        font-size: 1.15em !important;
    }
    
    /* Separadores */
    hr {
        border: none;
        height: 2px;
        background: linear-gradient(90deg, transparent, #1f77b4, transparent);
        margin: 30px 0;
    }
    
    /* Radio buttons melhorados */
    .stRadio > div {
        background-color: #f8f9fa;
        padding: 10px;
        border-radius: 10px;
    }
    
    /* Selectbox melhorado */
    .stSelectbox > div > div {
        border-radius: 8px !important;
    }
</style>
""", unsafe_allow_html=True)

# Frases estoicas e motivacionais
FRASES_ESTOICAS = [
    "A disciplina é a ponte entre objetivos e realizações.",
    "A excelência não é um ato, mas um hábito.",
    "O conhecimento sem aplicação é apenas informação.",
    "A engenharia transforma sonhos em realidade através da matemática e da física.",
    "Cada cálculo é um passo em direção à precisão.",
    "A paciência e a persistência superam a inteligência.",
    "A prática constante é o caminho para a maestria.",
    "A engenharia é a arte de aplicar a ciência para resolver problemas reais.",
]

def home_page():
    """Página inicial com dashboard e citações"""
    st.title("🏗️ ATLAS - Suíte de Engenharia Civil Integrada")
    
    # Citação aleatória com estilo melhorado
    frase = random.choice(FRASES_ESTOICAS)
    st.markdown(f"""
    <div style="background: linear-gradient(135deg, #e3f2fd 0%, #bbdefb 100%); 
                border-left: 5px solid #1f77b4; 
                border-radius: 10px; 
                padding: 1.5rem; 
                margin: 20px 0;
                box-shadow: 0 4px 12px rgba(0,0,0,0.1);">
        <p style="font-size: 1.2rem; color: #1565c0; font-weight: 600; margin: 0;">
            💡 <em>{frase}</em>
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("## 📚 Bem-vindo ao ATLAS")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        <div style="background: linear-gradient(135deg, #ffffff 0%, #f8f9fa 100%); 
                    padding: 1.5rem; 
                    border-radius: 15px; 
                    box-shadow: 0 4px 12px rgba(0,0,0,0.1);
                    border: 1px solid #e0e0e0;">
            <h3 style="color: #1f77b4; margin-top: 0;">🎯 Objetivo</h3>
            <p style="line-height: 1.8;">
                Acompanhar você durante todo o curso de Engenharia Civil,
                fornecendo ferramentas práticas e teóricas para cada disciplina.
            </p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div style="background: linear-gradient(135deg, #ffffff 0%, #f8f9fa 100%); 
                    padding: 1.5rem; 
                    border-radius: 15px; 
                    box-shadow: 0 4px 12px rgba(0,0,0,0.1);
                    border: 1px solid #e0e0e0;">
            <h3 style="color: #1f77b4; margin-top: 0;">🛠️ Funcionalidades</h3>
            <ul style="line-height: 2;">
                <li>Calculadoras interativas</li>
                <li>Visualizações gráficas</li>
                <li>Teoria e fórmulas em LaTeX</li>
                <li>Módulos por domínio</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div style="background: linear-gradient(135deg, #ffffff 0%, #f8f9fa 100%); 
                    padding: 1.5rem; 
                    border-radius: 15px; 
                    box-shadow: 0 4px 12px rgba(0,0,0,0.1);
                    border: 1px solid #e0e0e0;">
            <h3 style="color: #1f77b4; margin-top: 0;">📖 Módulos</h3>
            <ul style="line-height: 2;">
                <li>Fundamentos</li>
                <li>Estruturas</li>
                <li>Fluidos & Hidráulica</li>
                <li>Geotecnia</li>
                <li>Transportes & Topografia</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    st.markdown("""
    <div style="background: linear-gradient(135deg, #f8f9fa 0%, #e9ecef 100%); 
                padding: 2rem; 
                border-radius: 15px; 
                margin: 20px 0;">
        <h3 style="color: #2c3e50; margin-top: 0;">🚀 Como Usar</h3>
        <p style="font-size: 1.1rem; line-height: 1.8;">
            Use a <strong>barra lateral</strong> para navegar entre os módulos. Cada módulo possui:
        </p>
        <ul style="font-size: 1.05rem; line-height: 2;">
            <li><strong>📖 Teoria:</strong> Explicações detalhadas e fórmulas fundamentais em LaTeX</li>
            <li><strong>🧮 Calculadoras:</strong> Ferramentas práticas interativas para resolução de problemas</li>
            <li><strong>🔬 Demonstrações:</strong> Visualizações e exemplos práticos passo a passo</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)
    
    # Estatísticas rápidas
    st.markdown("---")
    st.markdown("### 📊 Estatísticas do ATLAS")
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("Módulos", "5", "Completos")
    with col2:
        st.metric("Calculadoras", "14+", "Funcionais")
    with col3:
        st.metric("Seções de Teoria", "20+", "Detalhadas")
    with col4:
        st.metric("Cálculo", "1-5", "Completo")

def main():
    """Função principal de navegação"""
    
    # Sidebar Navigation
    st.sidebar.title("🧭 Navegação")
    st.sidebar.markdown("---")
    
    # Menu de navegação
    page = st.sidebar.radio(
        "Selecione o Módulo:",
        [
            "🏠 Home",
            "📐 Fundamentos",
            "🏛️ Estruturas",
            "💧 Fluidos & Hidráulica",
            "🌍 Geotecnia",
            "🛣️ Transportes & Topografia"
        ]
    )
    
    st.sidebar.markdown("---")
    st.sidebar.markdown("""
    <div style="background: rgba(255,255,255,0.1); 
                padding: 1rem; 
                border-radius: 10px; 
                margin-top: 20px;">
        <h3 style="color: white; margin-top: 0;">ℹ️ Sobre</h3>
        <p style="color: white; margin-bottom: 0.5rem;">
            <strong>ATLAS v1.0</strong>
        </p>
        <p style="color: rgba(255,255,255,0.9); font-size: 0.9rem; margin: 0;">
            Suíte de Engenharia Civil Integrada<br>
            Desenvolvida para estudantes
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # Roteamento de páginas
    if page == "🏠 Home":
        home_page()
    elif page == "📐 Fundamentos":
        from modules import fundamentos
        fundamentos.show()
    elif page == "🏛️ Estruturas":
        from modules import estruturas
        estruturas.show()
    elif page == "💧 Fluidos & Hidráulica":
        from modules import fluidos
        fluidos.show()
    elif page == "🌍 Geotecnia":
        from modules import geotecnia
        geotecnia.show()
    elif page == "🛣️ Transportes & Topografia":
        from modules import transportes
        transportes.show()

if __name__ == "__main__":
    main()

