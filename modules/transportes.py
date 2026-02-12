"""
Módulo de Transportes & Topografia - Versão Expandida
Estradas e Topografia
"""

import streamlit as st
import numpy as np
import plotly.graph_objects as go
import pandas as pd

def show_teoria():
    """Aba de teoria expandida do módulo de Transportes"""
    st.header("📖 Teoria Detalhada - Transportes & Topografia")
    
    st.info("""
    💡 **Projeto de Estradas e Topografia:** Esta seção cobre os fundamentos do projeto geométrico de estradas 
    e cálculos topográficos essenciais.
    """)
    
    tab1, tab2, tab3 = st.tabs(["Curvas Horizontais", "Poligonal Topográfica", "Exemplos Práticos"])
    
    with tab1:
        st.subheader("🛣️ Curvas Horizontais Circulares - Teoria Completa")
        
        st.markdown("""
        ## 🎯 Introdução
        
        As **curvas horizontais** são elementos fundamentais no projeto geométrico de estradas. Permitem mudanças 
        suaves de direção, garantindo segurança e conforto aos usuários.
        
        ### Elementos de uma Curva Circular
        
        Uma curva circular é definida pelos seguintes elementos:
        """)
        
        st.markdown("---")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("""
            ### 📐 Elementos Geométricos
            
            **Raio (R):**
            - Distância do centro da curva até qualquer ponto do arco
            - Unidade: metros (m)
            - Valores típicos: 50 m a 2000 m
            
            **Ângulo Central (Δ):**
            - Ângulo formado pelos raios que unem o centro aos pontos de tangência
            - Unidade: graus (°)
            - Determina a "curvatura" da estrada
            
            **Tangente (T):**
            $$
            T = R \\cdot \\tan\\left(\\frac{\\Delta}{2}\\right)
            $$
            
            - Distância do ponto de tangência (PT) ao ponto de interseção (PI)
            - Usada para locar a curva no terreno
            """)
        
        with col2:
            st.markdown("""
            ### 🔄 Elementos de Desenvolvimento
            
            **Desenvolvimento (D):**
            $$
            D = R \\cdot \\Delta \\cdot \\frac{\\pi}{180}
            $$
            
            - Comprimento do arco da curva
            - Distância ao longo da estrada entre PT e PC
            
            **Grau da Curva (G):**
            $$
            G = \\frac{180}{\\pi \\cdot R}
            $$
            
            - Ângulo central correspondente a um arco de 20 m
            - Usado para locação da curva
            - Unidade: graus por 20 m
            """)
        
        st.markdown("---")
        
        st.markdown("""
        ## 📍 Pontos Característicos
        
        **PC (Ponto de Curvatura):**
        - Ponto onde a tangente termina e a curva começa
        - Também chamado de **PT** (Ponto de Tangência) em alguns sistemas
        
        **PT (Ponto de Tangência):**
        - Ponto onde a curva termina e a tangente recomeça
        - Também chamado de **PC** em alguns sistemas
        
        **PI (Ponto de Interseção):**
        - Ponto de interseção das duas tangentes
        - Não pertence à curva, mas é usado para cálculo
        
        **Centro (O):**
        - Centro do círculo que define a curva
        - Localizado a uma distância R do arco
        """)
        
        st.markdown("---")
        
        st.markdown("""
        ## 🔢 Relações entre Elementos
        
        **Cálculo do Raio a partir do Desenvolvimento:**
        $$
        R = \\frac{180 \\cdot D}{\\pi \\cdot \\Delta}
        $$
        
        **Cálculo do Raio a partir do Grau:**
        $$
        R = \\frac{180}{\\pi \\cdot G}
        $$
        
        **Flecha (F):**
        $$
        F = R \\cdot \\left(1 - \\cos\\frac{\\Delta}{2}\\right)
        $$
        
        - Distância do ponto médio do arco até a corda
        - Usada para verificação e locação
        
        **Corda (C):**
        $$
        C = 2R \\cdot \\sin\\frac{\\Delta}{2}
        $$
        
        - Distância em linha reta entre PC e PT
        """)
        
        st.markdown("---")
        
        st.markdown("""
        ## 🎯 Aplicações no Projeto de Estradas
        
        **Critérios de Projeto:**
        - **Raio mínimo:** Função da velocidade de projeto e superelevação
        - **Transição:** Curvas de transição (espirais) para mudanças suaves
        - **Sobrelevação:** Inclinação transversal para compensar força centrífuga
        
        **Velocidade de Projeto:**
        $$
        R_{min} = \\frac{V^2}{127(e + f)}
        $$
        
        Onde:
        - $V$: Velocidade (km/h)
        - $e$: Superelevação máxima (decimal)
        - $f$: Coeficiente de atrito lateral
        """)
        
        with st.expander("🔍 Exemplo: Dimensionamento de Curva", expanded=False):
            st.markdown("""
            **Problema:** Projetar uma curva circular com $\\Delta = 45°$ e $R = 200$ m.
            
            **Solução:**
            
            **1. Tangente:**
            $$
            T = 200 \\times \\tan(22.5°) = 82.84 \\text{ m}
            $$
            
            **2. Desenvolvimento:**
            $$
            D = 200 \\times 45 \\times \\frac{\\pi}{180} = 157.08 \\text{ m}
            $$
            
            **3. Grau da curva:**
            $$
            G = \\frac{180}{\\pi \\times 200} = 0.286° \\text{ por 20 m}
            $$
            
            **✅ Resultado:** Curva com desenvolvimento de 157.08 m
            """)
    
    with tab2:
        st.subheader("📐 Poligonal Topográfica - Teoria Completa")
        
        st.markdown("""
        ## 🎯 Introdução
        
        Uma **poligonal topográfica** é uma sequência de pontos conectados por linhas retas, formando um 
        polígono fechado ou aberto. É fundamental para levantamentos topográficos e projetos de engenharia.
        
        ### Tipos de Poligonais
        
        **Poligonal Fechada:**
        - Inicia e termina no mesmo ponto
        - Permite verificação de fechamento
        - Usada em levantamentos de áreas
        
        **Poligonal Aberta:**
        - Inicia e termina em pontos diferentes
        - Usada em alinhamentos (estradas, linhas de transmissão)
        - Requer pontos de controle conhecidos
        """)
        
        st.markdown("---")
        
        st.markdown("""
        ## 📊 Sistema de Coordenadas
        
        **Azimute (Az):**
        - Ângulo horizontal medido no sentido horário a partir do Norte
        - Varia de 0° a 360°
        - Convenção: Norte = 0°, Leste = 90°, Sul = 180°, Oeste = 270°
        
        **Rumo:**
        - Ângulo agudo entre a direção e o eixo Norte-Sul
        - Sempre menor que 90°
        - Inclui quadrante (NE, SE, SW, NW)
        """)
        
        st.markdown("---")
        
        st.markdown("""
        ## 🔢 Cálculo de Coordenadas
        
        ### Coordenadas Parciais (Incrementos)
        
        As coordenadas parciais representam o deslocamento em X e Y entre dois pontos consecutivos:
        
        $$
        \\Delta X = D \\cdot \\sin(Az)
        $$
        
        $$
        \\Delta Y = D \\cdot \\cos(Az)
        $$
        
        **Onde:**
        - $D$: Distância horizontal entre os pontos (m)
        - $Az$: Azimute da direção (graus)
        - $\\Delta X$: Incremento em X (Este-Oeste)
        - $\\Delta Y$: Incremento em Y (Norte-Sul)
        
        **Convenção de Sinais:**
        - $\\Delta X > 0$: Leste
        - $\\Delta X < 0$: Oeste
        - $\\Delta Y > 0$: Norte
        - $\\Delta Y < 0$: Sul
        """)
        
        st.markdown("---")
        
        st.markdown("""
        ### Coordenadas Absolutas
        
        As coordenadas absolutas são calculadas acumulando os incrementos:
        
        $$
        X_i = X_{i-1} + \\Delta X_i
        $$
        
        $$
        Y_i = Y_{i-1} + \\Delta Y_i
        $$
        
        **Onde:**
        - $X_i, Y_i$: Coordenadas do ponto atual
        - $X_{i-1}, Y_{i-1}$: Coordenadas do ponto anterior
        - $\\Delta X_i, \\Delta Y_i$: Incrementos calculados
        """)
        
        st.markdown("---")
        
        st.markdown("""
        ## ✅ Verificação de Fechamento
        
        Para poligonais fechadas, a soma dos incrementos deve ser zero:
        
        $$
        \\sum \\Delta X = 0
        $$
        
        $$
        \\sum \\Delta Y = 0
        $$
        
        **Erros de Fechamento:**
        
        $$
        E_x = \\sum \\Delta X
        $$
        
        $$
        E_y = \\sum \\Delta Y
        $$
        
        $$
        E_{linear} = \\sqrt{E_x^2 + E_y^2}
        $$
        
        **Precisão:**
        $$
        P = \\frac{1}{\\frac{E_{linear}}{\\sum D}}
        $$
        
        **Onde:**
        - $E_x, E_y$: Erros em X e Y (m)
        - $E_{linear}$: Erro linear total (m)
        - $\\sum D$: Perímetro da poligonal (m)
        - $P$: Precisão (adimensional)
        
        **Critérios de Aceitação:**
        - Poligonais de 1ª ordem: $P \\geq 1:10.000$
        - Poligonais de 2ª ordem: $P \\geq 1:5.000$
        - Poligonais de 3ª ordem: $P \\geq 1:2.000$
        """)
        
        st.markdown("---")
        
        st.markdown("""
        ## 🔧 Compensação de Erros
        
        Quando o erro está dentro da tolerância, pode-se compensar distribuindo o erro:
        
        **Compensação Proporcional:**
        $$
        \\Delta X_{comp} = \\Delta X - \\frac{E_x}{\\sum D} \\cdot D
        $$
        
        $$
        \\Delta Y_{comp} = \\Delta Y - \\frac{E_y}{\\sum D} \\cdot D
        $$
        
        **Método:** Distribuir o erro proporcionalmente ao comprimento de cada lado.
        """)
        
        with st.expander("🔍 Exemplo: Cálculo de Poligonal", expanded=False):
            st.markdown("""
            **Problema:** Calcular coordenadas de uma poligonal com:
            - Ponto inicial: (100, 200)
            - Lado 1: $D = 50$ m, $Az = 45°$
            - Lado 2: $D = 30$ m, $Az = 135°$
            
            **Solução:**
            
            **Lado 1:**
            $$
            \\Delta X_1 = 50 \\times \\sin(45°) = 35.35 \\text{ m}
            $$
            $$
            \\Delta Y_1 = 50 \\times \\cos(45°) = 35.35 \\text{ m}
            $$
            $$
            P_1 = (100 + 35.35, 200 + 35.35) = (135.35, 235.35)
            $$
            
            **Lado 2:**
            $$
            \\Delta X_2 = 30 \\times \\sin(135°) = 21.21 \\text{ m}
            $$
            $$
            \\Delta Y_2 = 30 \\times \\cos(135°) = -21.21 \\text{ m}
            $$
            $$
            P_2 = (135.35 + 21.21, 235.35 - 21.21) = (156.56, 214.14)
            $$
            """)
    
    with tab3:
        st.subheader("📚 Exemplos Práticos Resolvidos")
        
        exemplo = st.selectbox("Selecione um exemplo:", [
            "Exemplo 1: Dimensionamento de Curva Horizontal",
            "Exemplo 2: Cálculo de Poligonal Fechada"
        ])
        
        if exemplo == "Exemplo 1: Dimensionamento de Curva Horizontal":
            st.markdown("""
            **Problema:** Projetar curva com $\\Delta = 60°$ e velocidade de projeto de 60 km/h.
            
            **Solução:**
            
            **1. Raio mínimo (assumindo $e=0.08$, $f=0.15$):**
            $$
            R_{min} = \\frac{60^2}{127(0.08 + 0.15)} = 123.4 \\text{ m}
            $$
            
            **Adotar:** $R = 150$ m (arredondamento)
            
            **2. Tangente:**
            $$
            T = 150 \\times \\tan(30°) = 86.60 \\text{ m}
            $$
            
            **3. Desenvolvimento:**
            $$
            D = 150 \\times 60 \\times \\frac{\\pi}{180} = 157.08 \\text{ m}
            $$
            """)
        
        elif exemplo == "Exemplo 2: Cálculo de Poligonal Fechada":
            st.markdown("""
            **Problema:** Calcular e verificar fechamento de poligonal com 4 lados.
            
            **Dados:**
            - Lado 1: $D=100$ m, $Az=0°$
            - Lado 2: $D=80$ m, $Az=90°$
            - Lado 3: $D=100$ m, $Az=180°$
            - Lado 4: $D=80$ m, $Az=270°$
            
            **Solução:**
            
            **Incrementos:**
            - $\\Delta X_1 = 0$, $\\Delta Y_1 = 100$
            - $\\Delta X_2 = 80$, $\\Delta Y_2 = 0$
            - $\\Delta X_3 = 0$, $\\Delta Y_3 = -100$
            - $\\Delta X_4 = -80$, $\\Delta Y_4 = 0$
            
            **Erros:**
            $$
            E_x = 0 + 80 + 0 - 80 = 0
            $$
            $$
            E_y = 100 + 0 - 100 + 0 = 0
            $$
            
            **✅ Poligonal fechada perfeitamente!**
            """)

def show_calculadora_curvas():
    """Calculadora de curvas horizontais"""
    st.subheader("🛣️ Calculadora de Curvas Horizontais")
    
    st.markdown("""
    ### 🎯 Como Usar
    
    Calcule os elementos de uma curva circular horizontal.
    """)
    
    modo = st.radio("Modo de Cálculo", ["Dado Raio e Ângulo", "Dado Desenvolvimento e Ângulo"], horizontal=True)
    
    if modo == "Dado Raio e Ângulo":
        R = st.number_input("Raio R (m)", min_value=10.0, value=200.0, step=10.0)
        Delta = st.number_input("Ângulo Central Δ (graus)", min_value=1.0, max_value=180.0, value=45.0, step=1.0)
    else:
        D = st.number_input("Desenvolvimento D (m)", min_value=1.0, value=157.08, step=1.0)
        Delta = st.number_input("Ângulo Central Δ (graus)", min_value=1.0, max_value=180.0, value=45.0, step=1.0)
        R = (D * 180) / (np.pi * Delta)
    
    if st.button("Calcular", type="primary"):
        Delta_rad = np.radians(Delta)
        
        # Calcular elementos
        T = R * np.tan(Delta_rad / 2)
        D_calc = R * Delta_rad
        G = (180 / (np.pi * R)) if R > 0 else 0
        F = R * (1 - np.cos(Delta_rad / 2))
        C = 2 * R * np.sin(Delta_rad / 2)
        
        st.markdown("### ✅ Resultados")
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            st.metric("Raio R", f"{R:.2f} m")
        with col2:
            st.metric("Tangente T", f"{T:.2f} m")
        with col3:
            st.metric("Desenvolvimento D", f"{D_calc:.2f} m")
        with col4:
            st.metric("Grau da Curva G", f"{G:.4f}°")
        
        col1, col2 = st.columns(2)
        with col1:
            st.metric("Flecha F", f"{F:.2f} m")
        with col2:
            st.metric("Corda C", f"{C:.2f} m")
        
        # Visualização
        st.markdown("---")
        st.markdown("### 📐 Visualização da Curva")
        
        # Gerar pontos da curva
        theta = np.linspace(-Delta_rad/2, Delta_rad/2, 100)
        x_curva = R * np.sin(theta)
        y_curva = R * (1 - np.cos(theta))
        
        fig = go.Figure()
        
        # Curva
        fig.add_trace(go.Scatter(
            x=x_curva, y=y_curva,
            mode='lines',
            name='Curva',
            line=dict(color='blue', width=3)
        ))
        
        # Tangentes
        fig.add_trace(go.Scatter(
            x=[-T, 0], y=[0, 0],
            mode='lines',
            name='Tangente',
            line=dict(color='red', width=2, dash='dash')
        ))
        fig.add_trace(go.Scatter(
            x=[0, T*np.cos(Delta_rad)], y=[0, T*np.sin(Delta_rad)],
            mode='lines',
            name='Tangente',
            line=dict(color='red', width=2, dash='dash'),
            showlegend=False
        ))
        
        # PC e PT
        fig.add_trace(go.Scatter(
            x=[0, R*np.sin(Delta_rad/2)], y=[0, R*(1-np.cos(Delta_rad/2))],
            mode='markers+text',
            name='PC/PT',
            marker=dict(size=10, color='green'),
            text=['PC', 'PT'],
            textposition="top center"
        ))
        
        fig.update_layout(
            title="Esquema da Curva Circular",
            xaxis_title="X (m)",
            yaxis_title="Y (m)",
            height=500,
            xaxis=dict(scaleanchor="y", scaleratio=1)
        )
        
        st.plotly_chart(fig, use_container_width=True)

def show_calculadora_poligonal():
    """Calculadora de poligonal topográfica"""
    st.subheader("📐 Calculadora de Poligonal Topográfica")
    
    st.markdown("""
    ### 🎯 Como Usar
    
    Insira os dados da poligonal (distâncias e azimutes) para calcular coordenadas e verificar fechamento.
    """)
    
    num_lados = st.number_input("Número de Lados", min_value=2, max_value=20, value=4, step=1)
    
    # Coordenadas iniciais
    col1, col2 = st.columns(2)
    with col1:
        X0 = st.number_input("Coordenada X Inicial", value=100.0)
    with col2:
        Y0 = st.number_input("Coordenada Y Inicial", value=200.0)
    
    st.markdown("### Dados dos Lados")
    
    dados = []
    for i in range(num_lados):
        st.markdown(f"**Lado {i+1}**")
        col1, col2 = st.columns(2)
        with col1:
            D = st.number_input(f"Distância (m)", min_value=0.1, value=50.0, key=f"D_{i}")
        with col2:
            Az = st.number_input(f"Azimute (graus)", min_value=0.0, max_value=360.0, value=90.0*i, key=f"Az_{i}")
        dados.append({'D': D, 'Az': Az})
    
    if st.button("Calcular Poligonal", type="primary"):
        # Calcular incrementos
        delta_X = []
        delta_Y = []
        for dado in dados:
            Az_rad = np.radians(dado['Az'])
            dX = dado['D'] * np.sin(Az_rad)
            dY = dado['D'] * np.cos(Az_rad)
            delta_X.append(dX)
            delta_Y.append(dY)
        
        # Calcular coordenadas
        X = [X0]
        Y = [Y0]
        for i in range(num_lados):
            X.append(X[-1] + delta_X[i])
            Y.append(Y[-1] + delta_Y[i])
        
        # Erros
        E_x = sum(delta_X)
        E_y = sum(delta_Y)
        E_linear = np.sqrt(E_x**2 + E_y**2)
        soma_D = sum([d['D'] for d in dados])
        precisao = 1 / (E_linear / soma_D) if E_linear > 0 else float('inf')
        
        st.markdown("### ✅ Resultados")
        
        # Tabela
        df = pd.DataFrame({
            'Lado': range(1, num_lados + 1),
            'Distância (m)': [d['D'] for d in dados],
            'Azimute (°)': [d['Az'] for d in dados],
            'ΔX (m)': [f"{dx:.3f}" for dx in delta_X],
            'ΔY (m)': [f"{dy:.3f}" for dy in delta_Y],
            'X (m)': [f"{x:.3f}" for x in X[1:]],
            'Y (m)': [f"{y:.3f}" for y in Y[1:]]
        })
        st.dataframe(df, use_container_width=True)
        
        st.markdown("---")
        st.markdown("### 📊 Verificação de Fechamento")
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            st.metric("Erro em X", f"{E_x:.4f} m")
        with col2:
            st.metric("Erro em Y", f"{E_y:.4f} m")
        with col3:
            st.metric("Erro Linear", f"{E_linear:.4f} m")
        with col4:
            if precisao != float('inf'):
                st.metric("Precisão", f"1:{precisao:.0f}")
            else:
                st.metric("Precisão", "Perfeita")
        
        if E_linear < 0.01:
            st.success("✅ Poligonal fechada perfeitamente!")
        elif E_linear < 0.1:
            st.warning(f"⚠️ Erro pequeno: {E_linear:.4f} m")
        else:
            st.error(f"❌ Erro significativo: {E_linear:.4f} m")
        
        # Visualização
        st.markdown("---")
        st.markdown("### 📐 Visualização da Poligonal")
        
        fig = go.Figure()
        fig.add_trace(go.Scatter(
            x=X, y=Y,
            mode='lines+markers+text',
            name='Poligonal',
            line=dict(color='blue', width=2),
            marker=dict(size=8, color='red'),
            text=[f"P{i}" for i in range(len(X))],
            textposition="top center"
        ))
        fig.update_layout(
            title="Poligonal Topográfica",
            xaxis_title="X (m)",
            yaxis_title="Y (m)",
            height=500,
            xaxis=dict(scaleanchor="y", scaleratio=1)
        )
        st.plotly_chart(fig, use_container_width=True)

def show():
    """Função principal do módulo de Transportes"""
    st.title("🛣️ Módulo de Transportes & Topografia")
    st.markdown("---")
    
    st.info("""
    💡 **Módulo Completo:** Este módulo inclui teoria detalhada, calculadoras interativas e exemplos práticos 
    para projeto geométrico de estradas e cálculos topográficos.
    """)
    
    tab_teoria, tab_calc = st.tabs(["📖 Teoria", "🧮 Calculadoras"])
    
    with tab_teoria:
        show_teoria()
    
    with tab_calc:
        calc_tab = st.radio(
            "Selecione a Calculadora:",
            ["Curvas Horizontais", "Poligonal Topográfica"],
            horizontal=True
        )
        
        st.markdown("---")
        
        if calc_tab == "Curvas Horizontais":
            show_calculadora_curvas()
        elif calc_tab == "Poligonal Topográfica":
            show_calculadora_poligonal()

