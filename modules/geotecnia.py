"""
Módulo de Geotecnia
Mecânica dos Solos e Fundações
"""

import streamlit as st
import numpy as np
import sys
import os

# Adicionar path para imports
base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, base_dir)

from utils.plotting import plot_circulo_mohr

def show_teoria():
    """Aba de teoria expandida do módulo de Geotecnia"""
    st.header("📖 Teoria Detalhada - Geotecnia")
    
    st.info("""
    💡 **Mecânica dos Solos e Fundações:** Esta seção cobre os fundamentos da geotecnia, incluindo 
    classificação de solos, análise de tensões e dimensionamento de fundações.
    """)
    
    tab1, tab2, tab3, tab4 = st.tabs(["Classificação de Solos", "Círculo de Mohr", "Capacidade de Carga", "Exemplos Práticos"])
    
    with tab1:
        st.subheader("🏔️ Classificação de Solos - Teoria Completa")
        
        st.markdown("""
        ## 🎯 Introdução
        
        A **classificação de solos** é fundamental para entender o comportamento geotécnico e selecionar 
        métodos de projeto adequados. Os sistemas de classificação agrupam solos com características similares.
        
        ### Propriedades Índices dos Solos
        
        **Limite de Liquidez (LL):**
        - Teor de umidade que separa o comportamento **líquido** do **plástico**
        - Determinado pelo ensaio do aparelho de Casagrande
        - Representa a umidade na qual o solo flui como líquido
        
        **Limite de Plasticidade (LP):**
        - Teor de umidade mínimo para o solo apresentar comportamento **plástico**
        - Determinado pelo ensaio de rolagem em cilindros
        - Representa a transição entre estados plástico e semi-sólido
        
        **Índice de Plasticidade (IP):**
        $$
        IP = LL - LP
        $$
        
        - Mede a **faixa de umidade** na qual o solo é plástico
        - Quanto maior o IP, mais plástico é o solo
        - Solos com IP = 0 são **não-plásticos**
        """)
        
        st.markdown("---")
        
        st.markdown("""
        ## 📊 Sistema Unificado de Classificação de Solos (SUCS)
        
        O sistema SUCS (Unified Soil Classification System) é amplamente utilizado na engenharia geotécnica.
        
        ### Classificação de Solos Grossos (Granulares)
        
        **Símbolos:**
        - **G** (Gravel): Pedregulho/Areia grossa
        - **S** (Sand): Areia
        
        **Modificadores:**
        - **W** (Well-graded): Bem graduado
        - **P** (Poorly-graded): Mal graduado
        - **M** (Silty): Com finos siltosos
        - **C** (Clayey): Com finos argilosos
        
        **Exemplos:**
        - **GW:** Pedregulho bem graduado
        - **SP:** Areia mal graduada
        - **GM:** Pedregulho com finos siltosos
        
        ### Classificação de Solos Finos (Coesivos)
        
        **Símbolos:**
        - **M** (Silt): Silte
        - **C** (Clay): Argila
        - **O** (Organic): Orgânico
        
        **Modificadores baseados no IP:**
        - **L** (Low plasticity): Baixa plasticidade (IP < 7)
        - **H** (High plasticity): Alta plasticidade (IP > 7)
        
        **Exemplos:**
        - **CL:** Argila de baixa plasticidade
        - **CH:** Argila de alta plasticidade
        - **ML:** Silte de baixa plasticidade
        
        ### Carta de Plasticidade
        
        A classificação de solos finos utiliza a **Carta de Plasticidade de Casagrande:**
        
        - **Linha A:** $IP = 0.73(LL - 20)$ - Separa argilas de siltes
        - **Linha U:** $IP = 0.9(LL - 8)$ - Limite superior de plasticidade
        
        **Regras:**
        - Se o ponto está **acima da linha A:** Argila (C)
        - Se o ponto está **abaixo da linha A:** Silte (M)
        - Se $LL < 50$: Baixa plasticidade (L)
        - Se $LL > 50$: Alta plasticidade (H)
        """)
        
        st.markdown("---")
        
        st.markdown("""
        ## 🛣️ Sistema HRB (Highway Research Board)
        
        Sistema alternativo usado principalmente em **estradas e pavimentação**.
        
        **Grupos:**
        - **A-1 a A-3:** Solos granulares (excelentes a bons)
        - **A-4 a A-7:** Solos finos (marginais a pobres)
        
        **Características:**
        - Focado no comportamento como material de subleito
        - Considera características de compactação
        - Usado para seleção de materiais de pavimentação
        """)
        
        with st.expander("🔍 Exemplo: Classificar um Solo", expanded=False):
            st.markdown("""
            **Dados:**
            - LL = 45%
            - LP = 25%
            - Granulometria: 60% passando na peneira #200 (fino)
            - 40% retido na peneira #200 (grosso)
            
            **Solução:**
            
            **1. Calcular IP:**
            $$
            IP = LL - LP = 45 - 25 = 20\\%
            $$
            
            **2. Verificar na Carta de Plasticidade:**
            - Ponto (LL=45, IP=20)
            - Linha A: $IP = 0.73(45-20) = 18.25$
            - Como $IP = 20 > 18.25$, está **acima da linha A** → Argila
            
            **3. Verificar plasticidade:**
            - Como $LL = 45 < 50$ → Baixa plasticidade (L)
            
            **✅ Classificação SUCS: CL** (Argila de baixa plasticidade)
            """)
    
    with tab2:
        st.subheader("⭕ Círculo de Mohr - Análise de Tensões")
        
        st.markdown("""
        ## 🎯 Introdução
        
        O **Círculo de Mohr** é uma representação gráfica do estado de tensões em um ponto do solo. 
        Permite visualizar e calcular tensões principais, tensões de cisalhamento máximas e tensões 
        em qualquer plano.
        
        ### Estado de Tensão Plana
        
        Para um elemento sob **tensões planas**, temos:
        - Tensão normal em x: $\\sigma_x$
        - Tensão normal em y: $\\sigma_y$
        - Tensão de cisalhamento: $\\tau_{xy} = \\tau_{yx}$
        """)
        
        st.markdown("---")
        
        st.markdown("""
        ## 📐 Tensões Principais
        
        As **tensões principais** são as tensões normais nos planos onde a tensão de cisalhamento é zero.
        
        **Cálculo das Tensões Principais:**
        
        $$
        \\sigma_{1,2} = \\frac{\\sigma_x + \\sigma_y}{2} \\pm \\sqrt{\\left(\\frac{\\sigma_x - \\sigma_y}{2}\\right)^2 + \\tau_{xy}^2}
        $$
        
        **Onde:**
        - $\\sigma_1$: Tensão principal **máxima** (sempre maior)
        - $\\sigma_2$: Tensão principal **mínima** (sempre menor)
        
        **Interpretação:**
        - $\\sigma_1$ e $\\sigma_2$ são as tensões normais **máxima e mínima** possíveis
        - Nos planos principais, $\\tau = 0$
        - Os planos principais são **perpendiculares** entre si
        """)
        
        st.markdown("---")
        
        st.markdown("""
        ## 🔄 Construção do Círculo de Mohr
        
        ### Centro do Círculo
        
        $$
        \\sigma_{centro} = \\frac{\\sigma_x + \\sigma_y}{2}
        $$
        
        ### Raio do Círculo
        
        $$
        R = \\sqrt{\\left(\\frac{\\sigma_x - \\sigma_y}{2}\\right)^2 + \\tau_{xy}^2}
        $$
        
        ### Tensões Principais
        
        $$
        \\sigma_1 = \\sigma_{centro} + R
        $$
        
        $$
        \\sigma_2 = \\sigma_{centro} - R
        $$
        
        ### Tensão de Cisalhamento Máxima
        
        $$
        \\tau_{max} = R = \\frac{\\sigma_1 - \\sigma_2}{2}
        $$
        
        **Ocorre em planos a 45° dos planos principais.**
        """)
        
        st.markdown("---")
        
        st.markdown("""
        ## 📐 Ângulo do Plano Principal
        
        O ângulo que o plano principal forma com o eixo x é:
        
        $$
        \\theta_p = \\frac{1}{2} \\arctan\\left(\\frac{2\\tau_{xy}}{\\sigma_x - \\sigma_y}\\right)
        $$
        
        **Interpretação:**
        - $\\theta_p$: Ângulo do plano onde atua $\\sigma_1$
        - O outro plano principal está a $\\theta_p + 90°$
        - Convenção: Rotação no sentido anti-horário é positiva
        """)
        
        st.markdown("---")
        
        st.markdown("""
        ## 🎯 Aplicações na Geotecnia
        
        **1. Análise de Estabilidade de Taludes:**
        - Determinar tensões de cisalhamento críticas
        - Verificar condições de ruptura
        
        **2. Dimensionamento de Fundações:**
        - Calcular tensões transmitidas ao solo
        - Verificar capacidade de carga
        
        **3. Análise de Empuxos:**
        - Determinar tensões em estruturas de contenção
        - Calcular empuxos ativo e passivo
        
        **4. Ensaios de Laboratório:**
        - Interpretar resultados de ensaios triaxiais
        - Determinar parâmetros de resistência do solo
        """)
        
        with st.expander("🔍 Exemplo: Análise de Tensões", expanded=False):
            st.markdown("""
            **Dados:**
            - $\\sigma_x = 100$ kPa
            - $\\sigma_y = 50$ kPa
            - $\\tau_{xy} = 30$ kPa
            
            **Solução:**
            
            **1. Centro do círculo:**
            $$
            \\sigma_{centro} = \\frac{100 + 50}{2} = 75 \\text{ kPa}
            $$
            
            **2. Raio:**
            $$
            R = \\sqrt{\\left(\\frac{100-50}{2}\\right)^2 + 30^2} = \\sqrt{625 + 900} = 39.05 \\text{ kPa}
            $$
            
            **3. Tensões principais:**
            $$
            \\sigma_1 = 75 + 39.05 = 114.05 \\text{ kPa}
            $$
            $$
            \\sigma_2 = 75 - 39.05 = 35.95 \\text{ kPa}
            $$
            
            **4. Tensão de cisalhamento máxima:**
            $$
            \\tau_{max} = 39.05 \\text{ kPa}
            $$
            """)
    
    with tab3:
        st.subheader("🏗️ Capacidade de Carga - Teoria de Terzaghi")
        
        st.markdown("""
        ## 🎯 Introdução
        
        A **capacidade de carga** é a tensão máxima que o solo pode suportar sem sofrer ruptura por cisalhamento. 
        A teoria de Terzaghi (1943) é uma das mais utilizadas para dimensionamento de fundações superficiais.
        
        ### Hipóteses da Teoria de Terzaghi
        
        1. Solo é **homogêneo** e **isotrópico**
        2. Fundação é **rígida** e **corrida** (comprimento muito maior que largura)
        3. Superfície do terreno é **horizontal**
        4. Ruptura ocorre por **cisalhamento geral**
        5. Solo acima da base da fundação atua como **sobrecarga**
        """)
        
        st.markdown("---")
        
        st.markdown("""
        ## 📐 Fórmula de Terzaghi para Sapatas Corridas
        
        $$
        q_{ult} = c \\cdot N_c + \\gamma \\cdot D \\cdot N_q + \\frac{1}{2} \\gamma \\cdot B \\cdot N_\\gamma
        $$
        
        **Onde:**
        - $q_{ult}$: Capacidade de carga **última** (kPa)
        - $c$: **Coesão** do solo (kPa)
        - $\\gamma$: **Peso específico** do solo (kN/m³)
        - $D$: **Profundidade** da fundação (m)
        - $B$: **Largura** da fundação (m)
        - $N_c, N_q, N_\\gamma$: **Fatores de capacidade de carga** (função de $\\phi$)
        
        **Interpretação dos Termos:**
        
        1. **$c \\cdot N_c$:** Contribuição da **coesão** do solo
        2. **$\\gamma \\cdot D \\cdot N_q$:** Contribuição da **sobrecarga** (peso do solo acima)
        3. **$\\frac{1}{2} \\gamma \\cdot B \\cdot N_\\gamma$:** Contribuição do **peso próprio** do solo
        """)
        
        st.markdown("---")
        
        st.markdown("""
        ## 📊 Fatores de Capacidade de Carga
        
        Os fatores $N_c$, $N_q$ e $N_\\gamma$ dependem do **ângulo de atrito interno** $\\phi$ do solo:
        
        $$
        N_q = e^{\\pi \\tan \\phi} \\cdot \\tan^2\\left(45° + \\frac{\\phi}{2}\\right)
        $$
        
        $$
        N_c = (N_q - 1) \\cot \\phi
        $$
        
        $$
        N_\\gamma = \\frac{1}{2}(N_q - 1) \\tan(1.4 \\phi)
        $$
        
        **Valores Típicos:**
        
        | $\\phi$ (°) | $N_c$ | $N_q$ | $N_\\gamma$ |
        |-------------|-------|-------|-------------|
        | 0           | 5.7   | 1.0   | 0.0         |
        | 20          | 14.8  | 6.4   | 3.9         |
        | 30          | 30.1  | 18.4  | 22.4        |
        | 40          | 75.3  | 64.2  | 109.4       |
        """)
        
        st.markdown("---")
        
        st.markdown("""
        ## ✅ Capacidade de Carga Admissível
        
        A capacidade de carga **admissível** considera um **fator de segurança**:
        
        $$
        q_{adm} = \\frac{q_{ult}}{FS}
        $$
        
        **Onde:**
        - $FS$: Fator de segurança (geralmente **2.5 a 3.0**)
        - Para edifícios: $FS = 3.0$
        - Para estruturas temporárias: $FS = 2.0$
        
        **Verificação:**
        $$
        \\sigma_{aplicada} \\leq q_{adm}
        $$
        
        Onde $\\sigma_{aplicada} = \\frac{P}{A}$ é a tensão aplicada pela fundação.
        """)
        
        st.markdown("---")
        
        st.markdown("""
        ## 🔧 Modificações para Outros Tipos de Fundação
        
        **Sapatas Quadradas:**
        $$
        q_{ult} = 1.3cN_c + \\gamma D N_q + 0.4\\gamma B N_\\gamma
        $$
        
        **Sapatas Circulares:**
        $$
        q_{ult} = 1.3cN_c + \\gamma D N_q + 0.3\\gamma B N_\\gamma
        $$
        
        **Fatores de Forma:**
        - Sapatas retangulares: Aplicar fatores de forma
        - Fundações em grupo: Considerar efeito de grupo
        """)
        
        with st.expander("🔍 Exemplo: Dimensionamento de Sapata", expanded=False):
            st.markdown("""
            **Dados:**
            - Solo: $c = 20$ kPa, $\\phi = 25°$, $\\gamma = 18$ kN/m³
            - Sapata: $B = 2$ m, $D = 1.5$ m
            - $FS = 3.0$
            
            **Solução:**
            
            **1. Fatores de capacidade (para $\\phi = 25°$):**
            - $N_c \\approx 20.7$
            - $N_q \\approx 10.7$
            - $N_\\gamma \\approx 10.9$
            
            **2. Capacidade última:**
            $$
            q_{ult} = 20 \\times 20.7 + 18 \\times 1.5 \\times 10.7 + \\frac{1}{2} \\times 18 \\times 2 \\times 10.9
            $$
            $$
            q_{ult} = 414 + 288.9 + 196.2 = 899.1 \\text{ kPa}
            $$
            
            **3. Capacidade admissível:**
            $$
            q_{adm} = \\frac{899.1}{3} = 299.7 \\text{ kPa}
            $$
            
            **✅ Resultado:** A sapata pode suportar até 299.7 kPa
            """)
    
    with tab4:
        st.subheader("📚 Exemplos Práticos Resolvidos")
        
        exemplo = st.selectbox("Selecione um exemplo:", [
            "Exemplo 1: Classificação de Solo",
            "Exemplo 2: Análise de Círculo de Mohr",
            "Exemplo 3: Dimensionamento de Fundação"
        ])
        
        if exemplo == "Exemplo 1: Classificação de Solo":
            st.markdown("""
            **Problema:** Classificar um solo com LL=40%, LP=20%, 55% passando na peneira #200.
            
            **Solução:**
            
            **1. Calcular IP:**
            $$
            IP = LL - LP = 40 - 20 = 20\\%
            $$
            
            **2. Verificar na Carta de Plasticidade:**
            - Linha A: $IP = 0.73(40-20) = 14.6$
            - Como $IP = 20 > 14.6$ → Acima da linha A → **Argila**
            
            **3. Verificar plasticidade:**
            - Como $LL = 40 < 50$ → **Baixa plasticidade**
            
            **✅ Classificação SUCS: CL** (Argila de baixa plasticidade)
            """)
        
        elif exemplo == "Exemplo 2: Análise de Círculo de Mohr":
            st.markdown("""
            **Problema:** Determinar tensões principais para $\\sigma_x=120$ kPa, $\\sigma_y=60$ kPa, $\\tau_{xy}=40$ kPa.
            
            **Solução:**
            
            **1. Centro:**
            $$
            \\sigma_{centro} = \\frac{120+60}{2} = 90 \\text{ kPa}
            $$
            
            **2. Raio:**
            $$
            R = \\sqrt{\\left(\\frac{120-60}{2}\\right)^2 + 40^2} = 50 \\text{ kPa}
            $$
            
            **3. Tensões principais:**
            $$
            \\sigma_1 = 90 + 50 = 140 \\text{ kPa}
            $$
            $$
            \\sigma_2 = 90 - 50 = 40 \\text{ kPa}
            $$
            """)
        
        elif exemplo == "Exemplo 3: Dimensionamento de Fundação":
            st.markdown("""
            **Problema:** Calcular capacidade admissível de sapata corrida.
            
            **Dados:** $c=15$ kPa, $\\phi=30°$, $\\gamma=19$ kN/m³, $B=1.5$ m, $D=1.0$ m, $FS=3.0$
            
            **Solução:**
            
            **Fatores:** $N_c=30.1$, $N_q=18.4$, $N_\\gamma=22.4$
            
            $$
            q_{ult} = 15 \\times 30.1 + 19 \\times 1.0 \\times 18.4 + \\frac{1}{2} \\times 19 \\times 1.5 \\times 22.4
            $$
            
            $$
            q_{ult} = 451.5 + 349.6 + 319.2 = 1120.3 \\text{ kPa}
            $$
            
            $$
            q_{adm} = \\frac{1120.3}{3} = 373.4 \\text{ kPa}
            $$
            """)

def show_calculadora_mohr():
    """Calculadora de Círculo de Mohr"""
    st.subheader("⭕ Círculo de Mohr de Tensões")
    
    col1, col2, col3 = st.columns(3)
    with col1:
        sigma_x = st.number_input("Tensão Normal σx (kPa)", value=100.0, step=10.0)
    with col2:
        sigma_y = st.number_input("Tensão Normal σy (kPa)", value=50.0, step=10.0)
    with col3:
        tau_xy = st.number_input("Tensão de Cisalhamento τxy (kPa)", value=30.0, step=5.0)
    
    if st.button("Calcular", type="primary"):
        fig, sigma_1, sigma_2, theta_p = plot_circulo_mohr(sigma_x, sigma_y, tau_xy)
        
        st.plotly_chart(fig, use_container_width=True)
        
        st.markdown("### Resultados")
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("Tensão Principal σ₁", f"{sigma_1:.2f} kPa")
        with col2:
            st.metric("Tensão Principal σ₂", f"{sigma_2:.2f} kPa")
        with col3:
            st.metric("Ângulo Principal θp", f"{np.degrees(theta_p):.2f}°")
        
        # Tau máximo
        tau_max = (sigma_1 - sigma_2) / 2
        st.metric("Tensão de Cisalhamento Máxima τmax", f"{tau_max:.2f} kPa")
        
        # Análise detalhada
        st.markdown("---")
        st.markdown("### 🔍 Análise Detalhada")
        st.markdown(f"""
        **Centro do círculo:** $\\sigma_{{centro}} = \\frac{{{sigma_x} + {sigma_y}}}{{2}} = {(sigma_x + sigma_y)/2:.2f}$ kPa
        
        **Raio:** $R = \\sqrt{{\\left(\\frac{{{sigma_x} - {sigma_y}}}{{2}}\\right)^2 + {tau_xy}^2}} = {np.sqrt(((sigma_x - sigma_y)/2)**2 + tau_xy**2):.2f}$ kPa
        """)

def show_calculadora_classificacao():
    """Calculadora de classificação de solos"""
    st.subheader("🏔️ Classificação de Solos (SUCS)")
    
    st.markdown("""
    ### 🎯 Como Usar
    
    Insira os dados do solo para obter a classificação segundo o Sistema Unificado de Classificação de Solos (SUCS).
    """)
    
    col1, col2 = st.columns(2)
    
    with col1:
        LL = st.number_input("Limite de Liquidez LL (%)", min_value=0.0, value=40.0, step=1.0)
        LP = st.number_input("Limite de Plasticidade LP (%)", min_value=0.0, value=20.0, step=1.0)
    
    with col2:
        p200 = st.number_input("Percentual passando na peneira #200 (%)", min_value=0.0, max_value=100.0, value=55.0, step=1.0)
        p4 = st.number_input("Percentual passando na peneira #4 (%)", min_value=0.0, max_value=100.0, value=80.0, step=1.0)
    
    if st.button("Classificar Solo", type="primary"):
        IP = LL - LP
        
        # Determinar se é grosso ou fino
        if p200 < 50:
            # Solo grosso
            if p4 < 50:
                simbolo_base = "G"  # Gravel
            else:
                simbolo_base = "S"  # Sand
            
            # Determinar modificador
            if p200 < 5:
                if p4 < 50:
                    # Gravel bem ou mal graduado
                    Cu = st.number_input("Coeficiente de Uniformidade Cu", value=5.0, key="Cu")
                    Cc = st.number_input("Coeficiente de Curvatura Cc", value=1.0, key="Cc")
                    if Cu > 4 and 1 <= Cc <= 3:
                        modificador = "W"  # Well-graded
                    else:
                        modificador = "P"  # Poorly-graded
                else:
                    # Sand bem ou mal graduado
                    if p200 < 5:
                        modificador = "W" if p4 > 50 else "P"
                    else:
                        modificador = "P"
            else:
                # Com finos
                if LL < 50 and IP < 4:
                    modificador = "M"  # Silty
                elif LL >= 50 or IP >= 7:
                    modificador = "C"  # Clayey
                else:
                    modificador = "M"
            
            classificacao = f"{simbolo_base}{modificador}"
        else:
            # Solo fino
            # Verificar na carta de plasticidade
            linha_A = 0.73 * (LL - 20)
            
            if IP > linha_A:
                simbolo_base = "C"  # Clay
            else:
                simbolo_base = "M"  # Silt
            
            if LL < 50:
                modificador = "L"  # Low plasticity
            else:
                modificador = "H"  # High plasticity
            
            classificacao = f"{simbolo_base}{modificador}"
        
        st.markdown("### ✅ Resultado da Classificação")
        st.success(f"**Classificação SUCS: {classificacao}**")
        
        st.markdown("---")
        st.markdown("### 📊 Dados Calculados")
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("Índice de Plasticidade IP", f"{IP:.1f}%")
        with col2:
            st.metric("Percentual Fino", f"{p200:.1f}%")
        with col3:
            if p200 >= 50:
                linha_A = 0.73 * (LL - 20)
                st.metric("Linha A (IP)", f"{linha_A:.1f}%")
        
        # Descrição
        descricoes = {
            "GW": "Pedregulho bem graduado",
            "GP": "Pedregulho mal graduado",
            "GM": "Pedregulho com finos siltosos",
            "GC": "Pedregulho com finos argilosos",
            "SW": "Areia bem graduada",
            "SP": "Areia mal graduada",
            "SM": "Areia com finos siltosos",
            "SC": "Areia com finos argilosos",
            "ML": "Silte de baixa plasticidade",
            "MH": "Silte de alta plasticidade",
            "CL": "Argila de baixa plasticidade",
            "CH": "Argila de alta plasticidade",
            "OL": "Solo orgânico de baixa plasticidade",
            "OH": "Solo orgânico de alta plasticidade"
        }
        
        if classificacao in descricoes:
            st.info(f"**Descrição:** {descricoes[classificacao]}")

def show_calculadora_capacidade_carga():
    """Calculadora de capacidade de carga (Terzaghi)"""
    st.subheader("🏗️ Capacidade de Carga - Terzaghi")
    
    st.markdown("""
    ### 🎯 Como Usar
    
    Calcule a capacidade de carga de fundações superficiais usando a teoria de Terzaghi.
    """)
    
    tipo_fundacao = st.selectbox("Tipo de Fundação", ["Sapata Corrida", "Sapata Quadrada", "Sapata Circular"])
    
    st.markdown("### Propriedades do Solo")
    col1, col2, col3 = st.columns(3)
    with col1:
        c = st.number_input("Coesão c (kPa)", min_value=0.0, value=20.0, step=1.0)
    with col2:
        phi = st.number_input("Ângulo de Atrito φ (graus)", min_value=0.0, max_value=45.0, value=25.0, step=1.0)
    with col3:
        gamma = st.number_input("Peso Específico γ (kN/m³)", min_value=10.0, value=18.0, step=1.0)
    
    st.markdown("### Dimensões da Fundação")
    col1, col2 = st.columns(2)
    with col1:
        B = st.number_input("Largura B (m)", min_value=0.5, value=2.0, step=0.1)
    with col2:
        D = st.number_input("Profundidade D (m)", min_value=0.0, value=1.5, step=0.1)
    
    FS = st.number_input("Fator de Segurança FS", min_value=1.5, max_value=5.0, value=3.0, step=0.5)
    
    if st.button("Calcular Capacidade de Carga", type="primary"):
        # Calcular fatores de capacidade
        phi_rad = np.radians(phi)
        Nq = np.exp(np.pi * np.tan(phi_rad)) * (np.tan(np.radians(45 + phi/2)))**2
        Nc = (Nq - 1) / np.tan(phi_rad) if phi > 0 else 5.7
        Ngamma = 0.5 * (Nq - 1) * np.tan(np.radians(1.4 * phi)) if phi > 0 else 0
        
        # Calcular capacidade última
        if tipo_fundacao == "Sapata Corrida":
            q_ult = c * Nc + gamma * D * Nq + 0.5 * gamma * B * Ngamma
        elif tipo_fundacao == "Sapata Quadrada":
            q_ult = 1.3 * c * Nc + gamma * D * Nq + 0.4 * gamma * B * Ngamma
        else:  # Circular
            q_ult = 1.3 * c * Nc + gamma * D * Nq + 0.3 * gamma * B * Ngamma
        
        q_adm = q_ult / FS
        
        st.markdown("### ✅ Resultados")
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("Capacidade Última q_ult", f"{q_ult:.2f} kPa")
        with col2:
            st.metric("Capacidade Admissível q_adm", f"{q_adm:.2f} kPa")
        with col3:
            st.metric("Fator de Segurança", f"{FS:.1f}")
        
        st.markdown("---")
        st.markdown("### 📊 Fatores de Capacidade")
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("Nc", f"{Nc:.2f}")
        with col2:
            st.metric("Nq", f"{Nq:.2f}")
        with col3:
            st.metric("Nγ", f"{Ngamma:.2f}")
        
        st.markdown("---")
        st.markdown("### 📐 Detalhamento do Cálculo")
        st.markdown(f"""
        **Contribuição da coesão:**
        $$
        c \\cdot N_c = {c} \\times {Nc:.2f} = {c * Nc:.2f} \\text{{ kPa}}
        $$
        
        **Contribuição da sobrecarga:**
        $$
        \\gamma \\cdot D \\cdot N_q = {gamma} \\times {D} \\times {Nq:.2f} = {gamma * D * Nq:.2f} \\text{{ kPa}}
        $$
        
        **Contribuição do peso próprio:**
        $$
        \\frac{{1}}{{2}} \\gamma \\cdot B \\cdot N_\\gamma = \\frac{{1}}{{2}} \\times {gamma} \\times {B} \\times {Ngamma:.2f} = {0.5 * gamma * B * Ngamma:.2f} \\text{{ kPa}}
        $$
        
        **Capacidade última:**
        $$
        q_{{ult}} = {c * Nc:.2f} + {gamma * D * Nq:.2f} + {0.5 * gamma * B * Ngamma:.2f} = {q_ult:.2f} \\text{{ kPa}}
        $$
        """)

def show():
    """Função principal do módulo de Geotecnia"""
    st.title("🌍 Módulo de Geotecnia")
    st.markdown("---")
    
    tab_teoria, tab_calc = st.tabs(["📖 Teoria", "🧮 Calculadoras"])
    
    with tab_teoria:
        show_teoria()
    
    with tab_calc:
        calc_tab = st.radio(
            "Selecione a Calculadora:",
            ["Círculo de Mohr", "Classificação de Solos", "Capacidade de Carga"],
            horizontal=True
        )
        
        st.markdown("---")
        
        if calc_tab == "Círculo de Mohr":
            show_calculadora_mohr()
        elif calc_tab == "Classificação de Solos":
            show_calculadora_classificacao()
        elif calc_tab == "Capacidade de Carga":
            show_calculadora_capacidade_carga()

