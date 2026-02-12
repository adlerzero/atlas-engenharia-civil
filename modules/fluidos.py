"""
Módulo de Fluidos & Hidráulica
Calculadoras para Reynolds, Darcy-Weisbach e Manning
"""

import streamlit as st
import numpy as np
import sys
import os

# Adicionar path para imports
base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, base_dir)

from utils.calculations import (
    calcular_reynolds,
    calcular_fator_atrito_colebrook,
    calcular_perda_carga_darcy_weisbach,
    calcular_manning_canal
)

def show_teoria():
    """Aba de teoria expandida do módulo de Fluidos"""
    st.header("📖 Teoria Detalhada - Fluidos & Hidráulica")
    
    st.info("""
    💡 **Hidráulica e Fenômenos de Transporte:** Esta seção cobre os fundamentos do escoamento de fluidos, 
    perdas de carga e dimensionamento de sistemas hidráulicos.
    """)
    
    tab1, tab2, tab3, tab4 = st.tabs(["Reynolds & Regime", "Darcy-Weisbach", "Manning", "Exemplos Práticos"])
    
    with tab1:
        st.subheader("🌊 Número de Reynolds e Classificação de Regime")
        
        st.markdown("""
        ## 🎯 Introdução
        
        O **número de Reynolds** é um dos parâmetros adimensionais mais importantes da mecânica dos fluidos. 
        Ele relaciona as forças de inércia com as forças viscosas, determinando o regime de escoamento.
        
        ### Definição
        
        $$
        Re = \\frac{\\rho \\cdot V \\cdot D}{\\mu} = \\frac{V \\cdot D}{\\nu}
        $$
        
        **Onde:**
        - $\\rho$: Densidade do fluido (kg/m³)
        - $V$: Velocidade média do escoamento (m/s)
        - $D$: Diâmetro característico ou comprimento característico (m)
        - $\\mu$: Viscosidade dinâmica (Pa.s)
        - $\\nu = \\mu/\\rho$: Viscosidade cinemática (m²/s)
        
        **Interpretação Física:**
        - Numerador ($\\rho V D$): Representa as **forças de inércia**
        - Denominador ($\\mu$): Representa as **forças viscosas**
        - Re alto: Inércia domina (turbulento)
        - Re baixo: Viscosidade domina (laminar)
        """)
        
        st.markdown("---")
        
        st.markdown("""
        ## 📊 Classificação do Regime de Escoamento
        
        ### Regime Laminar ($Re < 2300$)
        
        **Características:**
        - Escoamento **ordenado**, com camadas paralelas
        - Sem mistura entre camadas
        - Perfil de velocidade parabólico (Hagen-Poiseuille)
        - Baixas perdas de energia
        
        **Aplicações:**
        - Escoamento em tubos muito finos
        - Escoamento de fluidos muito viscosos
        - Microfluídica
        
        **Fator de Atrito:**
        $$
        f = \\frac{64}{Re}
        $$
        
        ### Regime de Transição ($2300 < Re < 4000$)
        
        **Características:**
        - Regime **instável** e imprevisível
        - Alternância entre laminar e turbulento
        - **Evitar** em projetos (usar limites conservadores)
        
        ### Regime Turbulento ($Re > 4000$)
        
        **Características:**
        - Escoamento **desordenado**, com vórtices e turbulência
        - Mistura intensa entre camadas
        - Perfil de velocidade mais uniforme
        - Maiores perdas de energia
        
        **Aplicações:**
        - Maioria dos escoamentos em engenharia
        - Sistemas de abastecimento de água
        - Sistemas de drenagem
        
        **Fator de Atrito:**
        Depende de Re e rugosidade (Colebrook-White)
        """)
        
        st.markdown("---")
        
        st.markdown("""
        ## 🔬 Origem e Significado Físico
        
        O número de Reynolds foi introduzido por **Osborne Reynolds** em 1883 através de experimentos com 
        escoamento em tubos. Ele observou que a transição entre regimes dependia de uma combinação específica 
        de parâmetros.
        
        **Análise Dimensional:**
        
        Aplicando análise dimensional às equações de Navier-Stokes, obtemos:
        
        $$
        Re = \\frac{\\text{Forças de Inércia}}{\\text{Forças Viscosas}} = \\frac{\\rho V^2 L^2}{\\mu V L} = \\frac{\\rho V L}{\\mu}
        $$
        
        **Valores Típicos:**
        - Água em tubo de 10 cm a 1 m/s: $Re \\approx 100.000$ (turbulento)
        - Óleo em tubo fino: $Re < 2300$ (laminar)
        - Escoamento em canais: $Re > 10.000$ (turbulento)
        """)
        
        with st.expander("🔍 Exemplo: Determinar Regime de Escoamento", expanded=False):
            st.markdown("""
            **Problema:** Água a 20°C escoa em um tubo de 0.15 m de diâmetro a 2 m/s.
            
            **Dados:**
            - $\\rho = 1000$ kg/m³
            - $\\mu = 0.001$ Pa.s
            - $D = 0.15$ m
            - $V = 2$ m/s
            
            **Solução:**
            
            $$
            Re = \\frac{\\rho V D}{\\mu} = \\frac{1000 \\times 2 \\times 0.15}{0.001} = 300.000
            $$
            
            **Resultado:** $Re = 300.000 > 4000$ → **Regime Turbulento** ✅
            
            **Interpretação:** O escoamento é turbulento, com vórtices e mistura intensa.
            """)
    
    with tab2:
        st.subheader("Perda de Carga - Darcy-Weisbach")
        st.markdown("""
        ### Equação de Darcy-Weisbach
        
        A perda de carga distribuída em uma tubulação é calculada por:
        
        $$
        h_f = f \\cdot \\frac{L}{D} \\cdot \\frac{V^2}{2g}
        $$
        
        Onde:
        - $h_f$: Perda de carga (m)
        - $f$: Fator de atrito (adimensional)
        - $L$: Comprimento do trecho (m)
        - $D$: Diâmetro da tubulação (m)
        - $V$: Velocidade média (m/s)
        - $g$: Aceleração da gravidade (m/s²)
        
        ### Fator de Atrito
        
        **Regime Laminar ($Re < 2300$):**
        $$
        f = \\frac{64}{Re}
        $$
        
        **Regime Turbulento ($Re > 4000$):**
        
        Usando a equação de Colebrook-White:
        $$
        \\frac{1}{\\sqrt{f}} = -2 \\log_{10}\\left(\\frac{\\epsilon/D}{3.7} + \\frac{2.51}{Re \\sqrt{f}}\\right)
        $$
        
        Onde $\\epsilon/D$ é a rugosidade relativa.
        
        **Aproximação de Haaland (explícita):**
        $$
        \\frac{1}{\\sqrt{f}} = -1.8 \\log_{10}\\left[\\left(\\frac{\\epsilon/D}{3.7}\\right)^{1.11} + \\frac{6.9}{Re}\\right]
        $$
        
        ### Rugosidade Absoluta Típica
        
        - Aço comercial: $\\epsilon = 0.045$ mm
        - Ferro fundido: $\\epsilon = 0.26$ mm
        - Concreto: $\\epsilon = 0.3-3.0$ mm
        - PVC: $\\epsilon = 0.0015$ mm
        """)
    
    with tab3:
        st.subheader("Dimensionamento de Canais - Equação de Manning")
        st.markdown("""
        ### Equação de Manning
        
        Para escoamento em canais abertos, a vazão é calculada por:
        
        $$
        Q = \\frac{1}{n} \\cdot A \\cdot R_h^{2/3} \\cdot S^{1/2}
        $$
        
        Onde:
        - $Q$: Vazão (m³/s)
        - $n$: Coeficiente de Manning (adimensional)
        - $A$: Área da seção molhada (m²)
        - $R_h = A/P$: Raio hidráulico (m)
        - $P$: Perímetro molhado (m)
        - $S$: Declividade do canal (m/m)
        
        ### Para Canal Retangular
        
        $$
        A = b \\cdot y
        $$
        
        $$
        P = b + 2y
        $$
        
        $$
        R_h = \\frac{b \\cdot y}{b + 2y}
        $$
        
        Onde:
        - $b$: Largura do canal (m)
        - $y$: Altura da lâmina d'água (m)
        
        ### Coeficiente de Manning Típico
        
        - Concreto liso: $n = 0.012-0.014$
        - Concreto áspero: $n = 0.016-0.020$
        - Terra: $n = 0.020-0.030$
        - Grama: $n = 0.030-0.040$
        - Pedra: $n = 0.025-0.035$
        
        ### Aplicações
        
        - Dimensionamento de canais de drenagem
        - Projeto de sistemas de irrigação
        - Análise de escoamento em rios e córregos
        """)
    
    with tab4:
        st.subheader("📚 Exemplos Práticos Resolvidos")
        
        exemplo = st.selectbox("Selecione um exemplo:", [
            "Exemplo 1: Determinar regime de escoamento",
            "Exemplo 2: Cálculo de perda de carga em tubulação",
            "Exemplo 3: Dimensionamento de canal de drenagem"
        ])
        
        if exemplo == "Exemplo 1: Determinar regime de escoamento":
            st.markdown("""
            **Problema:** Água a 20°C escoa em um tubo de 0.20 m de diâmetro a 1.5 m/s.
            
            **Dados:**
            - $\\rho = 1000$ kg/m³
            - $\\mu = 0.001$ Pa.s
            - $D = 0.20$ m
            - $V = 1.5$ m/s
            
            **Solução:**
            
            $$
            Re = \\frac{\\rho V D}{\\mu} = \\frac{1000 \\times 1.5 \\times 0.20}{0.001} = 300.000
            $$
            
            **Resultado:** $Re = 300.000 > 4000$ → **Regime Turbulento**
            
            **Fator de atrito (assumindo rugosidade relativa $\\epsilon/D = 0.0002$):**
            $$
            f \\approx 0.014
            $$
            """)
        
        elif exemplo == "Exemplo 2: Cálculo de perda de carga em tubulação":
            st.markdown("""
            **Problema:** Calcular a perda de carga em uma tubulação de aço comercial de 100 m de comprimento, 
            0.15 m de diâmetro, com água escoando a 2 m/s.
            
            **Dados:**
            - $L = 100$ m
            - $D = 0.15$ m
            - $V = 2$ m/s
            - $\\rho = 1000$ kg/m³
            - $\\mu = 0.001$ Pa.s
            - $\\epsilon = 0.045$ mm (aço comercial)
            
            **Solução:**
            
            **1. Calcular Reynolds:**
            $$
            Re = \\frac{1000 \\times 2 \\times 0.15}{0.001} = 300.000
            $$
            
            **2. Rugosidade relativa:**
            $$
            \\frac{\\epsilon}{D} = \\frac{0.045}{150} = 0.0003
            $$
            
            **3. Fator de atrito (Colebrook-White):**
            $$
            f \\approx 0.0145
            $$
            
            **4. Perda de carga:**
            $$
            h_f = 0.0145 \\times \\frac{100}{0.15} \\times \\frac{2^2}{2 \\times 9.81} = 1.97 \\text{ m}
            $$
            
            **✅ Resultado:** Perda de carga de 1.97 m
            """)
        
        elif exemplo == "Exemplo 3: Dimensionamento de canal de drenagem":
            st.markdown("""
            **Problema:** Dimensionar um canal retangular de concreto para escoar 5 m³/s com declividade de 0.001.
            
            **Dados:**
            - $Q = 5$ m³/s
            - $S = 0.001$ m/m
            - $n = 0.014$ (concreto liso)
            - Largura: $b = 2$ m
            
            **Solução:**
            
            **1. Equação de Manning:**
            $$
            Q = \\frac{1}{n} A R_h^{2/3} S^{1/2}
            $$
            
            **2. Para canal retangular:**
            - $A = b \\cdot y = 2y$
            - $P = b + 2y = 2 + 2y$
            - $R_h = \\frac{A}{P} = \\frac{2y}{2 + 2y} = \\frac{y}{1 + y}$
            
            **3. Substituindo:**
            $$
            5 = \\frac{1}{0.014} \\times 2y \\times \\left(\\frac{y}{1+y}\\right)^{2/3} \\times 0.001^{1/2}
            $$
            
            **4. Resolvendo (método iterativo):**
            $$
            y \\approx 1.85 \\text{ m}
            $$
            
            **✅ Resultado:** Altura da lâmina d'água = 1.85 m
            """)

def show_calculadora_reynolds():
    """Calculadora de Reynolds"""
    st.subheader("🌊 Calculadora de Reynolds & Regime")
    
    col1, col2 = st.columns(2)
    with col1:
        densidade = st.number_input("Densidade ρ (kg/m³)", min_value=1.0, value=1000.0, step=10.0, help="Água: 1000 kg/m³")
    with col2:
        velocidade = st.number_input("Velocidade V (m/s)", min_value=0.01, value=1.0, step=0.1)
    
    col1, col2 = st.columns(2)
    with col1:
        diametro = st.number_input("Diâmetro D (m)", min_value=0.001, value=0.1, step=0.01)
    with col2:
        viscosidade = st.number_input("Viscosidade Dinâmica μ (Pa.s)", min_value=1e-6, value=0.001, step=0.0001, format="%.6f", help="Água a 20°C: 0.001 Pa.s")
    
    if st.button("Calcular Reynolds", type="primary"):
        resultado = calcular_reynolds(densidade, velocidade, diametro, viscosidade)
        
        st.markdown("### Resultados")
        col1, col2 = st.columns(2)
        with col1:
            st.metric("Número de Reynolds", f"{resultado['Re']:.2f}")
        with col2:
            st.metric("Regime", resultado['regime'])
        
        # Classificação visual
        if resultado['regime'] == "Laminar":
            st.success(f"✅ Regime **{resultado['regime']}** - Escoamento ordenado")
        elif resultado['regime'] == "Transição":
            st.warning(f"⚠️ Regime **{resultado['regime']}** - Instável, cuidado na análise")
        else:
            st.info(f"ℹ️ Regime **{resultado['regime']}** - Escoamento desordenado")
        
        # Informações adicionais
        st.markdown("### Informações Adicionais")
        viscosidade_cinematica = viscosidade / densidade
        st.write(f"**Viscosidade Cinemática:** $\\nu = {viscosidade_cinematica:.6f}$ m²/s")
        st.write(f"**Reynolds:** $Re = \\frac{{{densidade:.1f} \\times {velocidade:.2f} \\times {diametro:.3f}}}{{{viscosidade:.6f}}} = {resultado['Re']:.2f}$")

def show_calculadora_darcy_weisbach():
    """Calculadora de perda de carga Darcy-Weisbach"""
    st.subheader("💧 Perda de Carga - Darcy-Weisbach")
    
    col1, col2 = st.columns(2)
    with col1:
        comprimento = st.number_input("Comprimento L (m)", min_value=0.1, value=100.0, step=1.0)
    with col2:
        diametro = st.number_input("Diâmetro D (m)", min_value=0.001, value=0.1, step=0.01)
    
    col1, col2 = st.columns(2)
    with col1:
        velocidade = st.number_input("Velocidade V (m/s)", min_value=0.01, value=2.0, step=0.1)
    with col2:
        densidade = st.number_input("Densidade ρ (kg/m³)", min_value=1.0, value=1000.0, step=10.0)
    
    col1, col2 = st.columns(2)
    with col1:
        viscosidade = st.number_input("Viscosidade μ (Pa.s)", min_value=1e-6, value=0.001, step=0.0001, format="%.6f")
    with col2:
        rugosidade_abs = st.number_input("Rugosidade Absoluta ε (mm)", min_value=0.001, value=0.045, step=0.01, help="Aço comercial: 0.045 mm")
    
    metodo = st.selectbox("Método para fator de atrito", ["Colebrook-White", "Haaland"])
    
    if st.button("Calcular Perda de Carga", type="primary"):
        # Calcular Reynolds
        Re_result = calcular_reynolds(densidade, velocidade, diametro, viscosidade)
        Re = Re_result['Re']
        
        # Calcular fator de atrito
        rugosidade_relativa = (rugosidade_abs / 1000) / diametro
        
        if metodo == "Colebrook-White":
            f = calcular_fator_atrito_colebrook(Re, rugosidade_relativa)
        else:  # Haaland
            if Re < 2300:
                f = 64 / Re
            else:
                f = 0.25 / (np.log10((rugosidade_relativa / 3.7)**1.11 + 6.9 / Re))**2
        
        # Calcular perda de carga
        hf = calcular_perda_carga_darcy_weisbach(f, comprimento, diametro, velocidade)
        
        st.markdown("### Resultados")
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            st.metric("Reynolds", f"{Re:.2f}")
        with col2:
            st.metric("Regime", Re_result['regime'])
        with col3:
            st.metric("Fator de Atrito f", f"{f:.4f}")
        with col4:
            st.metric("Perda de Carga hf", f"{hf:.3f} m")
        
        # Perda de carga em pressão
        g = 9.81
        delta_p = densidade * g * hf / 1000  # kPa
        st.metric("Perda de Pressão Δp", f"{delta_p:.2f} kPa")
        
        # Informações
        st.markdown("### Detalhes do Cálculo")
        st.write(f"**Rugosidade Relativa:** $\\epsilon/D = {rugosidade_relativa:.6f}$")
        st.write(f"**Fator de Atrito:** $f = {f:.4f}$")
        st.write(f"**Perda de Carga:** $h_f = {f:.4f} \\times \\frac{{{comprimento:.1f}}}{{{diametro:.3f}}} \\times \\frac{{{velocidade:.2f}^2}}{{2 \\times 9.81}} = {hf:.3f}$ m")

def show_calculadora_manning():
    """Calculadora de Manning para canais"""
    st.subheader("🏞️ Dimensionamento de Canais - Manning")
    
    modo = st.radio("Modo de Cálculo", ["Calcular Altura (dado Q)", "Calcular Vazão (dado y)"], horizontal=True)
    
    col1, col2 = st.columns(2)
    with col1:
        largura = st.number_input("Largura do Canal b (m)", min_value=0.1, value=2.0, step=0.1)
    with col2:
        declividade = st.number_input("Declividade S (m/m)", min_value=0.0001, value=0.001, step=0.0001, format="%.4f")
    
    col1, col2 = st.columns(2)
    with col1:
        n_manning = st.number_input("Coeficiente de Manning n", min_value=0.001, value=0.014, step=0.001, format="%.3f", help="Concreto liso: 0.012-0.014")
    with col2:
        if modo == "Calcular Altura (dado Q)":
            vazao = st.number_input("Vazão Q (m³/s)", min_value=0.01, value=5.0, step=0.1)
            altura = None
        else:
            altura = st.number_input("Altura da Lâmina d'água y (m)", min_value=0.01, value=1.0, step=0.1)
            vazao = None
    
    if st.button("Calcular", type="primary"):
        if modo == "Calcular Altura (dado Q)":
            resultado = calcular_manning_canal(vazao, declividade, largura, n_manning, altura=None)
            
            if resultado.get('erro'):
                st.error(f"Erro: {resultado['erro']}")
            else:
                st.markdown("### Resultados")
                col1, col2, col3, col4 = st.columns(4)
                with col1:
                    st.metric("Altura y", f"{resultado['altura']:.3f} m")
                with col2:
                    st.metric("Velocidade V", f"{resultado['velocidade']:.2f} m/s")
                with col3:
                    st.metric("Área A", f"{resultado['area']:.2f} m²")
                with col4:
                    st.metric("Raio Hidráulico Rh", f"{resultado['raio_hidraulico']:.3f} m")
                
                st.metric("Perímetro Molhado P", f"{resultado['perimetro']:.2f} m")
        else:
            resultado = calcular_manning_canal(vazao=None, declividade=declividade, largura=largura, n_manning=n_manning, altura=altura)
            
            st.markdown("### Resultados")
            col1, col2, col3, col4 = st.columns(4)
            with col1:
                vazao_calc = (1 / n_manning) * resultado['area'] * resultado['raio_hidraulico']**(2/3) * declividade**0.5
                st.metric("Vazão Q", f"{vazao_calc:.3f} m³/s")
            with col2:
                st.metric("Velocidade V", f"{resultado['velocidade']:.2f} m/s")
            with col3:
                st.metric("Área A", f"{resultado['area']:.2f} m²")
            with col4:
                st.metric("Raio Hidráulico Rh", f"{resultado['raio_hidraulico']:.3f} m")
            
            st.metric("Perímetro Molhado P", f"{resultado['perimetro']:.2f} m")
        
        # Verificação de velocidade
        if 'velocidade' in resultado:
            if resultado['velocidade'] > 5.0:
                st.warning("⚠️ Velocidade muito alta! Risco de erosão.")
            elif resultado['velocidade'] < 0.3:
                st.info("ℹ️ Velocidade baixa. Risco de assoreamento.")

def show():
    """Função principal do módulo de Fluidos"""
    st.title("💧 Módulo de Fluidos & Hidráulica")
    st.markdown("---")
    
    st.info("""
    💡 **Módulo Completo:** Este módulo inclui teoria detalhada, calculadoras interativas e exemplos práticos 
    para análise de escoamentos, perdas de carga e dimensionamento de sistemas hidráulicos.
    """)
    
    tab_teoria, tab_calc = st.tabs(["📖 Teoria", "🧮 Calculadoras"])
    
    with tab_teoria:
        show_teoria()
    
    with tab_calc:
        calc_tab = st.radio(
            "Selecione a Calculadora:",
            ["Reynolds & Regime", "Darcy-Weisbach", "Manning"],
            horizontal=True
        )
        
        st.markdown("---")
        
        if calc_tab == "Reynolds & Regime":
            show_calculadora_reynolds()
        elif calc_tab == "Darcy-Weisbach":
            show_calculadora_darcy_weisbach()
        elif calc_tab == "Manning":
            show_calculadora_manning()

