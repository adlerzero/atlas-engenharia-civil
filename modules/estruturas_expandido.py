"""
Módulo de Estruturas - Versão Expandida e Didática
Calculadoras para vigas, propriedades geométricas e dimensionamento de concreto
Com explicações profundas, demonstrações e visualizações interativas
"""

import streamlit as st
import numpy as np
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import sys
import os

# Adicionar path para imports
base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, base_dir)

from utils.calculations import (
    calcular_reacoes_viga_simples,
    calcular_esforcos_viga,
    calcular_propriedades_geometricas,
    dimensionar_concreto_armado_simples
)
from utils.plotting import plot_diagrama_cortante_momento, plot_viga_esquema

def show_teoria_vigas_detalhada():
    """Teoria detalhada sobre vigas isostáticas"""
    st.header("📚 Teoria Detalhada: Vigas Isostáticas")
    
    st.markdown("""
    ## 🎯 Introdução
    
    Uma **viga isostática** é uma estrutura estaticamente determinada, ou seja, possui exatamente o número 
    de reações de apoio necessárias para garantir o equilíbrio estático. As vigas simplesmente apoiadas 
    são o caso mais comum de vigas isostáticas.
    
    ### Características Fundamentais:
    - ✅ **3 incógnitas** (2 reações verticais + 1 reação horizontal, geralmente nula)
    - ✅ **3 equações de equilíbrio** (ΣFx=0, ΣFy=0, ΣM=0)
    - ✅ **Sistema determinado** - solução única
    """)
    
    st.markdown("---")
    
    st.markdown("""
    ## ⚖️ Equilíbrio Estático
    
    Para uma viga em equilíbrio, três condições devem ser satisfeitas simultaneamente:
    """)
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        ### 1. Equilíbrio de Forças Horizontais
        $$
        \\sum F_x = 0
        $$
        
        Para vigas com cargas apenas verticais:
        $$
        H_A = H_B = 0
        $$
        """)
    
    with col2:
        st.markdown("""
        ### 2. Equilíbrio de Forças Verticais
        $$
        \\sum F_y = 0
        $$
        
        $$
        V_A + V_B = \\sum P_i + \\sum q_i \\cdot L_i
        $$
        
        Onde:
        - $V_A, V_B$: Reações verticais nos apoios
        - $P_i$: Cargas pontuais
        - $q_i$: Intensidade de cargas distribuídas
        - $L_i$: Extensão das cargas distribuídas
        """)
    
    with col3:
        st.markdown("""
        ### 3. Equilíbrio de Momentos
        $$
        \\sum M = 0
        $$
        
        Tomando momentos em relação ao ponto A:
        $$
        V_B \\cdot L = \\sum P_i \\cdot x_i + \\sum q_i \\cdot L_i \\cdot \\bar{x}_i
        $$
        
        Onde $\\bar{x}_i$ é a posição do centroide da carga distribuída.
        """)
    
    st.markdown("---")
    
    st.markdown("""
    ## 📐 Demonstração Passo a Passo
    
    Vamos resolver um exemplo prático para entender o processo:
    """)
    
    with st.expander("🔍 Exemplo Resolvido: Viga com Carga Pontual", expanded=True):
        st.markdown("""
        **Dados do Problema:**
        - Viga de comprimento $L = 6$ m
        - Carga pontual $P = 30$ kN na posição $x = 2$ m
        
        **Passo 1: Equilíbrio de Forças Verticais**
        $$
        V_A + V_B = P = 30 \\text{ kN}
        $$
        
        **Passo 2: Equilíbrio de Momentos (em relação ao ponto A)**
        $$
        V_B \\cdot 6 = P \\cdot 2 = 30 \\cdot 2 = 60
        $$
        
        $$
        V_B = \\frac{60}{6} = 10 \\text{ kN}
        $$
        
        **Passo 3: Calcular $V_A$**
        $$
        V_A = 30 - 10 = 20 \\text{ kN}
        $$
        
        **✅ Resultado:**
        - $V_A = 20$ kN (↑)
        - $V_B = 10$ kN (↑)
        """)
    
    st.markdown("---")
    
    st.markdown("""
    ## 📊 Esforços Internos
    
    Os **esforços internos** são forças e momentos que atuam no interior da viga. Eles variam ao longo do 
    comprimento e são fundamentais para o dimensionamento.
    """)
    
    tab1, tab2 = st.tabs(["Esforço Cortante", "Momento Fletor"])
    
    with tab1:
        st.markdown("""
        ### 🔪 Esforço Cortante (V)
        
        O **esforço cortante** é a força interna que tende a "cortar" a viga em uma seção transversal.
        
        **Convenção de Sinais:**
        - **Positivo (+):** Quando tende a girar o elemento no sentido horário
        - **Negativo (-):** Quando tende a girar no sentido anti-horário
        
        **Cálculo:**
        $$
        V(x) = V_A - \\sum_{x_i \\leq x} P_i - \\int_{x_0}^{x} q(\\xi) \\, d\\xi
        $$
        
        **Interpretação Física:**
        - O cortante em uma seção é igual à **soma algébrica de todas as forças verticais** à esquerda (ou direita) da seção
        - Onde $V(x) = 0$, ocorre o **momento máximo**
        - Mudanças bruscas no cortante indicam **cargas pontuais**
        
        **Relação com Carga Distribuída:**
        $$
        \\frac{dV}{dx} = -q(x)
        $$
        
        Ou seja, a **derivada do cortante** é igual à carga distribuída (com sinal negativo).
        """)
        
        # Gráfico explicativo do cortante
        x_exemplo = np.linspace(0, 6, 100)
        V_exemplo = 20 - 30 * (x_exemplo >= 2)
        
        fig_v = go.Figure()
        fig_v.add_trace(go.Scatter(
            x=x_exemplo,
            y=V_exemplo,
            mode='lines',
            name='Cortante V(x)',
            line=dict(color='red', width=3),
            fill='tozeroy',
            fillcolor='rgba(255,0,0,0.2)'
        ))
        fig_v.add_vline(x=2, line_dash="dash", line_color="gray", annotation_text="Carga P")
        fig_v.add_hline(y=0, line_dash="dash", line_color="black")
        fig_v.update_layout(
            title="Exemplo: Diagrama de Esforço Cortante",
            xaxis_title="Posição x (m)",
            yaxis_title="Cortante V (kN)",
            height=350,
            template='plotly_white'
        )
        st.plotly_chart(fig_v, use_container_width=True)
    
    with tab2:
        st.markdown("""
        ### 🔄 Momento Fletor (M)
        
        O **momento fletor** é o momento interno que causa flexão na viga.
        
        **Convenção de Sinais:**
        - **Positivo (+):** Tração nas fibras inferiores (viga "sorrindo" 😊)
        - **Negativo (-):** Tração nas fibras superiores (viga "triste" 😢)
        
        **Cálculo:**
        $$
        M(x) = V_A \\cdot x - \\sum_{x_i \\leq x} P_i \\cdot (x - x_i) - \\int_{x_0}^{x} q(\\xi) \\cdot (x - \\xi) \\, d\\xi
        $$
        
        **Interpretação Física:**
        - O momento em uma seção é igual à **soma dos momentos** de todas as forças à esquerda (ou direita) da seção
        - O momento máximo ocorre onde **$V(x) = 0$**
        - A área sob o diagrama de cortante entre dois pontos é igual à **variação do momento** entre esses pontos
        
        **Relação com Cortante:**
        $$
        \\frac{dM}{dx} = V(x)
        $$
        
        Ou seja, a **derivada do momento** é igual ao cortante.
        """)
        
        # Gráfico explicativo do momento
        x_exemplo = np.linspace(0, 6, 100)
        M_exemplo = 20 * x_exemplo - 30 * np.maximum(0, x_exemplo - 2)
        
        fig_m = go.Figure()
        fig_m.add_trace(go.Scatter(
            x=x_exemplo,
            y=M_exemplo,
            mode='lines',
            name='Momento M(x)',
            line=dict(color='blue', width=3),
            fill='tozeroy',
            fillcolor='rgba(0,0,255,0.2)'
        ))
        fig_m.add_vline(x=2, line_dash="dash", line_color="gray", annotation_text="Carga P")
        fig_m.add_hline(y=0, line_dash="dash", line_color="black")
        fig_m.update_layout(
            title="Exemplo: Diagrama de Momento Fletor",
            xaxis_title="Posição x (m)",
            yaxis_title="Momento M (kN.m)",
            height=350,
            template='plotly_white'
        )
        st.plotly_chart(fig_m, use_container_width=True)
    
    st.markdown("---")
    
    st.markdown("""
    ## 🔗 Relações Fundamentais
    
    Existem relações importantes entre carga, cortante e momento:
    
    $$
    \\begin{align}
    q(x) &= -\\frac{dV}{dx} \\\\
    V(x) &= \\frac{dM}{dx} \\\\
    q(x) &= -\\frac{d^2M}{dx^2}
    \\end{align}
    $$
    
    **Interpretação:**
    - Carga distribuída → Variação do cortante
    - Cortante → Variação do momento
    - Carga distribuída → Curvatura do momento (segunda derivada)
    """)
    
    st.markdown("---")
    
    st.markdown("""
    ## 📈 Propriedades dos Diagramas
    
    ### Diagrama de Cortante (DEC):
    1. **Cargas pontuais** causam **descontinuidades** (saltos) no diagrama
    2. **Cargas distribuídas** causam **variação linear** no diagrama
    3. Onde $V = 0$, o momento é **máximo ou mínimo**
    
    ### Diagrama de Momento (DMF):
    1. **Cargas pontuais** causam **mudança de inclinação** (quebra)
    2. **Cargas distribuídas** causam **curvatura** (parábola)
    3. O momento máximo ocorre onde **$V = 0$** ou nos **apoios**
    """)

def show_exemplo_interativo_vigas():
    """Exemplo interativo de cálculo de vigas"""
    st.header("🎓 Exemplo Interativo: Análise de Viga")
    
    st.markdown("""
    Vamos resolver um exemplo passo a passo. Você pode modificar os valores e ver como isso afeta os resultados!
    """)
    
    col1, col2 = st.columns(2)
    
    with col1:
        L = st.slider("Comprimento da Viga L (m)", 2.0, 10.0, 6.0, 0.5)
        P = st.slider("Carga Pontual P (kN)", 10.0, 100.0, 30.0, 5.0)
        x_p = st.slider("Posição da Carga x (m)", 0.5, float(L-0.5), 2.0, 0.5)
    
    with col2:
        q = st.slider("Carga Distribuída q (kN/m)", 0.0, 20.0, 5.0, 1.0)
        x_q_inicio = st.slider("Início Carga Distribuída (m)", 0.0, float(L), 0.0, 0.5)
        x_q_fim = st.slider("Fim Carga Distribuída (m)", 0.0, float(L), L, 0.5)
    
    # Calcular
    cargas_pontuais = [{'posicao': x_p, 'valor': P}]
    cargas_distribuidas = [{'inicio': x_q_inicio, 'fim': x_q_fim, 'valor': q}]
    
    reacoes = calcular_reacoes_viga_simples(L, cargas_pontuais, cargas_distribuidas)
    
    st.markdown("---")
    st.markdown("### 📊 Solução Passo a Passo")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown(f"""
        **Passo 1: Somar todas as forças**
        
        Carga pontual: $P = {P:.1f}$ kN
        
        Carga distribuída: $q \\cdot L_q = {q:.1f} \\times {x_q_fim - x_q_inicio:.1f} = {q * (x_q_fim - x_q_inicio):.1f}$ kN
        
        **Total:** $\\sum F = {P + q * (x_q_fim - x_q_inicio):.1f}$ kN
        """)
    
    with col2:
        st.markdown(f"""
        **Passo 2: Equilíbrio de forças verticais**
        
        $V_A + V_B = {P + q * (x_q_fim - x_q_inicio):.1f}$ kN
        """)
    
    # Calcular momento em relação a A
    momento_P = P * x_p
    centro_q = (x_q_inicio + x_q_fim) / 2
    momento_q = q * (x_q_fim - x_q_inicio) * centro_q
    momento_total = momento_P + momento_q
    
    st.markdown(f"""
    **Passo 3: Equilíbrio de momentos (em relação ao ponto A)**
    
    Momento da carga pontual: $M_P = P \\cdot x = {P:.1f} \\times {x_p:.1f} = {momento_P:.1f}$ kN.m
    
    Momento da carga distribuída: $M_q = q \\cdot L_q \\cdot \\bar{{x}} = {q:.1f} \\times {x_q_fim - x_q_inicio:.1f} \\times {centro_q:.1f} = {momento_q:.1f}$ kN.m
    
    **Total:** $\\sum M_A = {momento_total:.1f}$ kN.m
    
    $$
    V_B = \\frac{{\\sum M_A}}{{L}} = \\frac{{{momento_total:.1f}}}{{{L:.1f}}} = {reacoes['Vb']:.2f} \\text{{ kN}}
    $$
    
    $$
    V_A = {P + q * (x_q_fim - x_q_inicio):.1f} - {reacoes['Vb']:.2f} = {reacoes['Va']:.2f} \\text{{ kN}}
    $$
    """)
    
    st.markdown("---")
    st.markdown("### ✅ Resultados")
    
    col1, col2 = st.columns(2)
    with col1:
        st.metric("Reação em A (Va)", f"{reacoes['Va']:.2f} kN", delta=f"{reacoes['Va']/(P + q*(x_q_fim-x_q_inicio))*100:.1f}% do total")
    with col2:
        st.metric("Reação em B (Vb)", f"{reacoes['Vb']:.2f} kN", delta=f"{reacoes['Vb']/(P + q*(x_q_fim-x_q_inicio))*100:.1f}% do total")
    
    # Verificar equilíbrio
    soma_reacoes = reacoes['Va'] + reacoes['Vb']
    soma_cargas = P + q * (x_q_fim - x_q_inicio)
    erro = abs(soma_reacoes - soma_cargas)
    
    if erro < 0.01:
        st.success(f"✅ Equilíbrio verificado! ΣFy = {soma_reacoes:.2f} kN")
    else:
        st.warning(f"⚠️ Erro no equilíbrio: {erro:.2f} kN")
    
    # Visualizações
    st.markdown("---")
    st.markdown("### 📐 Visualizações")
    
    # Esquema da viga
    fig_esquema = plot_viga_esquema(L, cargas_pontuais, cargas_distribuidas, reacoes)
    st.plotly_chart(fig_esquema, use_container_width=True)
    
    # Diagramas
    x = np.linspace(0, L, 200)
    cortante, momento = calcular_esforcos_viga(x, L, cargas_pontuais, cargas_distribuidas, reacoes)
    
    fig_v, fig_m = plot_diagrama_cortante_momento(x, cortante, momento, reacoes, cargas_pontuais, cargas_distribuidas, L)
    st.plotly_chart(fig_v, use_container_width=True)
    st.plotly_chart(fig_m, use_container_width=True)
    
    # Análise dos resultados
    st.markdown("---")
    st.markdown("### 🔍 Análise dos Resultados")
    
    idx_max_v = np.argmax(np.abs(cortante))
    idx_max_m = np.argmax(np.abs(momento))
    idx_zero_v = np.where(np.abs(cortante) < 0.1)[0]
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Cortante Máximo", f"{np.max(np.abs(cortante)):.2f} kN", f"em x = {x[idx_max_v]:.2f} m")
    with col2:
        st.metric("Momento Máximo", f"{np.max(np.abs(momento)):.2f} kN.m", f"em x = {x[idx_max_m]:.2f} m")
    with col3:
        if len(idx_zero_v) > 0:
            st.metric("Onde V = 0", f"x = {x[idx_zero_v[0]]:.2f} m", "Momento máximo")
        else:
            st.metric("Onde V = 0", "Não encontrado", "Verifique o diagrama")

# Continuar com o resto do arquivo...

