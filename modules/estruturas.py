"""
Módulo de Estruturas
Calculadoras para vigas, propriedades geométricas e dimensionamento de concreto
"""

import streamlit as st
import numpy as np
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

def show_teoria():
    """Aba de teoria do módulo de Estruturas - Versão Expandida e Didática"""
    st.header("📖 Teoria Detalhada - Estruturas")
    
    st.info("""
    💡 **Bem-vindo à seção de teoria!** Aqui você encontrará explicações profundas, demonstrações passo a passo, 
    visualizações interativas e exemplos práticos para dominar os conceitos de estruturas.
    """)
    
    tab1, tab2, tab3, tab4 = st.tabs(["Vigas Isostáticas", "Propriedades Geométricas", "Concreto Armado", "Exemplos Práticos"])
    
    with tab1:
        st.subheader("🏗️ Vigas Isostáticas - Teoria Completa")
        
        st.markdown("""
        ## 🎯 Introdução
        
        Uma **viga isostática** é uma estrutura estaticamente determinada. Isso significa que possui exatamente 
        o número de reações de apoio necessárias para garantir o equilíbrio estático, resultando em uma solução única.
        
        ### Características Fundamentais:
        - ✅ **3 incógnitas** (2 reações verticais + 1 reação horizontal, geralmente nula)
        - ✅ **3 equações de equilíbrio** (ΣFx=0, ΣFy=0, ΣM=0)
        - ✅ **Sistema determinado** - solução única e estável
        """)
        
        st.markdown("---")
        
        st.markdown("""
        ## ⚖️ Equilíbrio Estático - Fundamentos
        
        Para uma viga em equilíbrio, três condições devem ser satisfeitas simultaneamente:
        """)
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.markdown("""
            ### 1️⃣ Equilíbrio Horizontal
            $$
            \\sum F_x = 0
            $$
            
            Para vigas com cargas apenas verticais:
            $$
            H_A = H_B = 0
            $$
            
            **Interpretação:** Sem cargas horizontais, não há reações horizontais.
            """)
        
        with col2:
            st.markdown("""
            ### 2️⃣ Equilíbrio Vertical
            $$
            \\sum F_y = 0
            $$
            
            $$
            V_A + V_B = \\sum P_i + \\sum q_i \\cdot L_i
            $$
            
            **Onde:**
            - $V_A, V_B$: Reações verticais nos apoios (kN)
            - $P_i$: Cargas pontuais (kN)
            - $q_i$: Intensidade de cargas distribuídas (kN/m)
            - $L_i$: Extensão das cargas distribuídas (m)
            
            **Interpretação:** A soma das reações deve igualar a soma de todas as cargas.
            """)
        
        with col3:
            st.markdown("""
            ### 3️⃣ Equilíbrio de Momentos
            $$
            \\sum M = 0
            $$
            
            Tomando momentos em relação ao ponto A:
            $$
            V_B \\cdot L = \\sum P_i \\cdot x_i + \\sum q_i \\cdot L_i \\cdot \\bar{x}_i
            $$
            
            **Onde:**
            - $L$: Comprimento da viga (m)
            - $x_i$: Posição das cargas pontuais (m)
            - $\\bar{x}_i$: Posição do centroide da carga distribuída (m)
            
            **Interpretação:** O momento das reações deve igualar o momento das cargas.
            """)
        
        st.markdown("---")
        
        with st.expander("🔍 Exemplo Resolvido Passo a Passo", expanded=False):
            st.markdown("""
            **Problema:** Viga de 6 m com carga pontual de 30 kN a 2 m do apoio A.
            
            **Solução:**
            
            **Passo 1:** Equilíbrio vertical
            $$
            V_A + V_B = 30 \\text{ kN}
            $$
            
            **Passo 2:** Equilíbrio de momentos (em relação a A)
            $$
            V_B \\cdot 6 = 30 \\cdot 2 = 60
            $$
            $$
            V_B = \\frac{60}{6} = 10 \\text{ kN}
            $$
            
            **Passo 3:** Calcular $V_A$
            $$
            V_A = 30 - 10 = 20 \\text{ kN}
            $$
            
            **✅ Verificação:** $20 + 10 = 30$ ✓
            """)
        
        st.markdown("---")
        
        st.markdown("""
        ## 📊 Esforços Internos - Conceitos Fundamentais
        
        Os **esforços internos** são forças e momentos que atuam no interior da viga. Eles variam ao longo do 
        comprimento e são fundamentais para o dimensionamento estrutural.
        """)
        
        sub_tab1, sub_tab2 = st.tabs(["🔪 Esforço Cortante (V)", "🔄 Momento Fletor (M)"])
        
        with sub_tab1:
            st.markdown("""
            ### Esforço Cortante V(x)
            
            O **esforço cortante** é a força interna que tende a "cortar" a viga em uma seção transversal.
            
            **Convenção de Sinais:**
            - **Positivo (+):** Tende a girar o elemento no sentido horário
            - **Negativo (-):** Tende a girar no sentido anti-horário
            
            **Fórmula Geral:**
            $$
            V(x) = V_A - \\sum_{x_i \\leq x} P_i - \\int_{x_0}^{x} q(\\xi) \\, d\\xi
            $$
            
            **Interpretação Física:**
            - O cortante em uma seção é igual à **soma algébrica de todas as forças verticais** à esquerda da seção
            - Onde $V(x) = 0$, ocorre o **momento máximo ou mínimo**
            - Mudanças bruscas no cortante indicam **cargas pontuais**
            
            **Relação com Carga Distribuída:**
            $$
            \\frac{dV}{dx} = -q(x)
            $$
            
            A **derivada do cortante** é igual à carga distribuída (com sinal negativo).
            
            **Propriedades do Diagrama de Cortante (DEC):**
            1. Cargas pontuais causam **descontinuidades** (saltos) no diagrama
            2. Cargas distribuídas causam **variação linear** no diagrama
            3. Onde $V = 0$, o momento é **máximo ou mínimo**
            """)
        
        with sub_tab2:
            st.markdown("""
            ### Momento Fletor M(x)
            
            O **momento fletor** é o momento interno que causa flexão na viga.
            
            **Convenção de Sinais:**
            - **Positivo (+):** Tração nas fibras inferiores (viga "sorrindo" 😊)
            - **Negativo (-):** Tração nas fibras superiores (viga "triste" 😢)
            
            **Fórmula Geral:**
            $$
            M(x) = V_A \\cdot x - \\sum_{x_i \\leq x} P_i \\cdot (x - x_i) - \\int_{x_0}^{x} q(\\xi) \\cdot (x - \\xi) \\, d\\xi
            $$
            
            **Interpretação Física:**
            - O momento em uma seção é igual à **soma dos momentos** de todas as forças à esquerda da seção
            - O momento máximo ocorre onde **$V(x) = 0$**
            - A área sob o diagrama de cortante entre dois pontos é igual à **variação do momento** entre esses pontos
            
            **Relação com Cortante:**
            $$
            \\frac{dM}{dx} = V(x)
            $$
            
            A **derivada do momento** é igual ao cortante.
            
            **Propriedades do Diagrama de Momento (DMF):**
            1. Cargas pontuais causam **mudança de inclinação** (quebra)
            2. Cargas distribuídas causam **curvatura** (parábola)
            3. O momento máximo ocorre onde **$V = 0$** ou nos **apoios**
            """)
        
        st.markdown("---")
        
        st.markdown("""
        ## 🔗 Relações Fundamentais entre Carga, Cortante e Momento
        
        Existem relações matemáticas importantes que conectam carga distribuída, cortante e momento:
        
        $$
        \\begin{align}
        q(x) &= -\\frac{dV}{dx} \\quad \\text{(Carga → Variação do Cortante)} \\\\
        V(x) &= \\frac{dM}{dx} \\quad \\text{(Cortante → Variação do Momento)} \\\\
        q(x) &= -\\frac{d^2M}{dx^2} \\quad \\text{(Carga → Curvatura do Momento)}
        \\end{align}
        $$
        
        **Aplicação Prática:**
        - Conhecendo a carga, podemos determinar o cortante por integração
        - Conhecendo o cortante, podemos determinar o momento por integração
        - Essas relações são fundamentais para traçar os diagramas manualmente
        """)
    
    with tab2:
        st.subheader("📐 Propriedades Geométricas de Seções - Teoria Completa")
        
        st.markdown("""
        ## 🎯 Introdução
        
        As **propriedades geométricas** de uma seção transversal são fundamentais para o cálculo de tensões, 
        deformações e capacidade resistente de elementos estruturais. As principais propriedades são:
        
        - **Centroide:** Ponto que representa o centro de gravidade da seção
        - **Momento de Inércia:** Medida da resistência à flexão
        - **Módulo de Resistência:** Relacionado à capacidade de resistir a tensões de flexão
        """)
        
        st.markdown("---")
        
        st.markdown("""
        ## 📍 Centroide (Centro de Gravidade)
        
        O **centroide** é o ponto onde se concentra toda a área da seção. Para seções compostas:
        
        $$
        \\bar{y} = \\frac{\\sum A_i \\cdot y_i}{\\sum A_i}
        $$
        
        $$
        \\bar{x} = \\frac{\\sum A_i \\cdot x_i}{\\sum A_i}
        $$
        
        **Onde:**
        - $A_i$: Área de cada parte da seção
        - $y_i, x_i$: Coordenadas do centroide de cada parte em relação a um sistema de referência
        
        **Interpretação Física:**
        - O centroide é o ponto de equilíbrio da seção
        - Para seções simétricas, o centroide está no eixo de simetria
        - É fundamental para calcular o momento de inércia
        """)
        
        st.markdown("---")
        
        st.markdown("""
        ## 🔄 Momento de Inércia
        
        O **momento de inércia** ($I$) mede a resistência da seção à flexão. Quanto maior o momento de inércia, 
        maior a rigidez à flexão.
        
        ### Teorema dos Eixos Paralelos (Steiner)
        
        Para seções compostas, usamos o teorema de Steiner:
        
        $$
        I_x = \\sum \\left( I_{x,i} + A_i \\cdot d_i^2 \\right)
        $$
        
        **Onde:**
        - $I_{x,i}$: Momento de inércia próprio de cada parte em relação ao seu próprio centroide
        - $A_i$: Área de cada parte
        - $d_i$: Distância do centroide da parte ao centroide total da seção
        
        **Interpretação:**
        - O primeiro termo ($I_{x,i}$) é o momento de inércia próprio
        - O segundo termo ($A_i \\cdot d_i^2$) é o "transporte" devido à distância do centroide
        
        ### Fórmulas para Seções Simples
        
        **Seção Retangular:**
        $$
        I_x = \\frac{b \\cdot h^3}{12}
        $$
        
        $$
        I_y = \\frac{h \\cdot b^3}{12}
        $$
        
        **Seção Circular:**
        $$
        I = \\frac{\\pi \\cdot D^4}{64}
        $$
        
        **Seção T ou I:**
        - Dividir em partes (mesa e alma)
        - Calcular o centroide de cada parte
        - Aplicar o teorema de Steiner para cada parte
        - Somar os resultados
        """)
        
        st.markdown("---")
        
        st.markdown("""
        ## 💪 Módulo de Resistência
        
        O **módulo de resistência** ($W$) relaciona o momento de inércia com a distância até a fibra mais distante:
        
        $$
        W = \\frac{I}{y_{max}}
        $$
        
        **Onde:**
        - $I$: Momento de inércia
        - $y_{max}$: Distância do centroide até a fibra mais distante
        
        **Aplicação:**
        - Usado no cálculo de tensões de flexão: $\\sigma = \\frac{M}{W}$
        - Quanto maior o módulo de resistência, maior a capacidade de resistir a momentos fletores
        """)
        
        with st.expander("🔍 Exemplo: Cálculo de Propriedades para Seção T", expanded=False):
            st.markdown("""
            **Dados:**
            - Mesa: $b_f = 0.30$ m, $t_f = 0.10$ m
            - Alma: $h_w = 0.40$ m, $t_w = 0.10$ m
            
            **Solução:**
            
            **1. Áreas:**
            - $A_{mesa} = 0.30 \\times 0.10 = 0.03$ m²
            - $A_{alma} = 0.40 \\times 0.10 = 0.04$ m²
            - $A_{total} = 0.07$ m²
            
            **2. Centroides (em relação à base):**
            - $y_{mesa} = 0.40 + 0.10/2 = 0.45$ m
            - $y_{alma} = 0.40/2 = 0.20$ m
            
            **3. Centroide total:**
            $$
            \\bar{y} = \\frac{0.03 \\times 0.45 + 0.04 \\times 0.20}{0.07} = 0.307 \\text{ m}
            $$
            
            **4. Momentos de inércia:**
            - $I_{mesa} = \\frac{0.30 \\times 0.10^3}{12} + 0.03 \\times (0.45 - 0.307)^2 = 0.000025 + 0.000614 = 0.000639$ m⁴
            - $I_{alma} = \\frac{0.10 \\times 0.40^3}{12} + 0.04 \\times (0.20 - 0.307)^2 = 0.000533 + 0.000458 = 0.000991$ m⁴
            - $I_{total} = 0.00163$ m⁴
            """)
    
    with tab3:
        st.subheader("🏗️ Dimensionamento de Concreto Armado - Teoria Completa")
        
        st.markdown("""
        ## 🎯 Introdução
        
        O **dimensionamento de concreto armado** consiste em determinar a quantidade de armadura necessária 
        para que uma seção resista aos esforços solicitantes. O método baseia-se nas hipóteses da teoria 
        de flexão simples.
        """)
        
        st.markdown("---")
        
        st.markdown("""
        ## 📋 Hipóteses Básicas da Teoria
        
        ### 1. Compatibilidade de Deformações (Hipótese de Bernoulli)
        - As **seções permanecem planas** após a deformação
        - As deformações são proporcionais à distância da linha neutra
        - $\\epsilon = \\frac{y}{x} \\cdot \\epsilon_c$
        
        ### 2. Comportamento dos Materiais
        
        **Concreto:**
        - **Não resiste à tração** (toda tração é absorvida pelo aço)
        - Compressão: Diagrama parábola-retângulo ou retângulo equivalente
        - Deformação última: $\\epsilon_{cu} = 0.35\\%$ (3.5‰)
        
        **Aço:**
        - Comportamento **elástico-perfeitamente plástico**
        - Módulo de elasticidade: $E_s = 210$ GPa
        - Deformação de escoamento: $\\epsilon_{yd} = \\frac{f_{yd}}{E_s}$
        """)
        
        st.markdown("---")
        
        st.markdown("""
        ## 📊 Domínios de Deformação
        
        Os **domínios de deformação** classificam o estado de ruína da seção:
        """)
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.markdown("""
            ### Domínio 2
            $0 < x/d < 0.259$
            
            **Características:**
            - Ruína por **deformação excessiva do aço**
            - Aço em escoamento
            - Concreto pouco solicitado
            
            **Uso:** Não recomendado (seção subdimensionada)
            """)
        
        with col2:
            st.markdown("""
            ### Domínio 3 ⭐
            $0.259 < x/d < 0.628$
            
            **Características:**
            - Ruína por **deformação do aço** (ideal)
            - Aço em escoamento
            - Concreto bem aproveitado
            
            **Uso:** ✅ **Ideal para dimensionamento**
            """)
        
        with col3:
            st.markdown("""
            ### Domínio 4
            $x/d > 0.628$
            
            **Características:**
            - Ruína por **esmagamento do concreto**
            - Aço não escoa
            - Ruína frágil
            
            **Uso:** ❌ **Não permitido** (armadura dupla necessária)
            """)
        
        st.markdown("---")
        
        st.markdown("""
        ## 🔢 Equações de Dimensionamento
        
        ### Passo 1: Momento Adimensional
        
        $$
        m_d = \\frac{M_d}{b_w \\cdot d^2 \\cdot f_{cd}}
        $$
        
        **Onde:**
        - $M_d = \\gamma_f \\cdot M_k$: Momento de cálculo (N.m)
        - $f_{cd} = \\frac{f_{ck}}{\\gamma_c}$: Resistência de cálculo do concreto (Pa)
        - $\\gamma_c = 1.4$: Coeficiente de ponderação do concreto
        - $\\gamma_f = 1.4$: Coeficiente de ponderação das ações
        
        ### Passo 2: Altura da Linha Neutra
        
        $$
        \\frac{x}{d} = 1.25 \\cdot \\left(1 - \\sqrt{1 - \\frac{2 \\cdot m_d}{0.68}}\\right)
        $$
        
        **Verificação:** Se $x/d > 0.628$, é necessário armadura dupla.
        
        ### Passo 3: Área de Aço
        
        $$
        A_s = \\frac{M_d}{f_{yd} \\cdot (d - 0.4 \\cdot x)}
        $$
        
        **Onde:**
        - $f_{yd} = \\frac{f_{yk}}{\\gamma_s}$: Tensão de escoamento de cálculo (Pa)
        - $\\gamma_s = 1.15$: Coeficiente de ponderação do aço
        - $(d - 0.4x)$: Braço de alavanca (distância entre resultantes)
        
        ### Passo 4: Verificação de Domínio
        
        - Calcular $x/d$
        - Verificar em qual domínio está
        - Se Domínio 4, recalcular com armadura dupla
        """)
        
        st.markdown("---")
        
        st.markdown("""
        ## 📐 Propriedades dos Materiais
        
        ### Concreto (NBR 6118)
        
        | Classe | fck (MPa) | fcd (MPa) | εcu (‰) |
        |--------|-----------|-----------|---------|
        | C20    | 20        | 14.3      | 3.5     |
        | C25    | 25        | 17.9      | 3.5     |
        | C30    | 30        | 21.4      | 3.5     |
        | C40    | 40        | 28.6      | 3.5     |
        
        ### Aço (NBR 6118)
        
        | Tipo  | fyk (MPa) | fyd (MPa) | Es (GPa) |
        |-------|-----------|-----------|----------|
        | CA50  | 500       | 435       | 210      |
        | CA60  | 600       | 522       | 210      |
        """)
        
        with st.expander("🔍 Exemplo Completo de Dimensionamento", expanded=False):
            st.markdown("""
            **Dados:**
            - $M_k = 120$ kN.m
            - $f_{ck} = 25$ MPa
            - CA50
            - $b_w = 0.20$ m
            - $d = 0.45$ m
            
            **Solução:**
            
            **1. Propriedades:**
            - $f_{cd} = 25/1.4 = 17.86$ MPa
            - $f_{yd} = 500/1.15 = 435$ MPa
            - $M_d = 1.4 \\times 120 = 168$ kN.m
            
            **2. Momento adimensional:**
            $$
            m_d = \\frac{168 \\times 1000}{0.20 \\times 0.45^2 \\times 17.86 \\times 10^6} = 0.233
            $$
            
            **3. Linha neutra:**
            $$
            x/d = 1.25 \\times (1 - \\sqrt{1 - 2 \\times 0.233/0.68}) = 0.40
            $$
            $$
            x = 0.40 \\times 0.45 = 0.18 \\text{ m}
            $$
            
            **4. Verificação:** $x/d = 0.40$ → Domínio 3 ✅
            
            **5. Área de aço:**
            $$
            A_s = \\frac{168 \\times 1000}{435 \\times 10^6 \\times (0.45 - 0.4 \\times 0.18)} = 10.2 \\text{ cm}^2
            $$
            
            **✅ Resultado:** $A_s = 10.2$ cm² → **13 barras de 10 mm**
            """)
    
    with tab4:
        st.subheader("📚 Exemplos Práticos Resolvidos")
        
        st.markdown("""
        ## 🎓 Exemplos Passo a Passo
        
        Aqui você encontrará exemplos práticos resolvidos detalhadamente, com explicações de cada etapa do cálculo.
        """)
        
        exemplo_escolhido = st.selectbox(
            "Selecione um exemplo:",
            [
                "Exemplo 1: Viga com carga pontual central",
                "Exemplo 2: Viga com carga distribuída uniforme",
                "Exemplo 3: Viga com múltiplas cargas",
                "Exemplo 4: Dimensionamento de concreto"
            ]
        )
        
        if exemplo_escolhido == "Exemplo 1: Viga com carga pontual central":
            st.markdown("""
            ### 📐 Exemplo 1: Viga Simplesmente Apoiada com Carga Pontual Central
            
            **Dados:**
            - Comprimento da viga: $L = 8$ m
            - Carga pontual: $P = 50$ kN
            - Posição da carga: $x = 4$ m (centro)
            
            **Solução:**
            
            **1. Equilíbrio de Forças Verticais:**
            $$
            V_A + V_B = P = 50 \\text{ kN}
            $$
            
            **2. Equilíbrio de Momentos (em relação ao ponto A):**
            $$
            V_B \\cdot 8 = 50 \\cdot 4 = 200
            $$
            $$
            V_B = \\frac{200}{8} = 25 \\text{ kN}
            $$
            
            **3. Calcular $V_A$:**
            $$
            V_A = 50 - 25 = 25 \\text{ kN}
            $$
            
            **✅ Resultado:**
            - $V_A = 25$ kN (↑)
            - $V_B = 25$ kN (↑)
            
            **Observação:** Por simetria, as reações são iguais quando a carga está no centro.
            
            **Esforços Internos:**
            - **Cortante:** $V(x) = 25$ kN para $x < 4$ m, e $V(x) = -25$ kN para $x > 4$ m
            - **Momento máximo:** $M_{max} = 25 \\times 4 = 100$ kN.m (no centro)
            """)
        
        elif exemplo_escolhido == "Exemplo 2: Viga com carga distribuída uniforme":
            st.markdown("""
            ### 📐 Exemplo 2: Viga com Carga Distribuída Uniforme
            
            **Dados:**
            - Comprimento da viga: $L = 6$ m
            - Carga distribuída: $q = 10$ kN/m (em todo o comprimento)
            
            **Solução:**
            
            **1. Carga total:**
            $$
            Q = q \\cdot L = 10 \\times 6 = 60 \\text{ kN}
            $$
            
            **2. Por simetria:**
            $$
            V_A = V_B = \\frac{Q}{2} = \\frac{60}{2} = 30 \\text{ kN}
            $$
            
            **✅ Resultado:**
            - $V_A = 30$ kN (↑)
            - $V_B = 30$ kN (↑)
            
            **Esforços Internos:**
            - **Cortante:** $V(x) = 30 - 10x$ (linear)
            - **Momento:** $M(x) = 30x - 5x^2$ (parábola)
            - **Momento máximo:** $M_{max} = \\frac{qL^2}{8} = \\frac{10 \\times 6^2}{8} = 45$ kN.m (no centro)
            """)
        
        elif exemplo_escolhido == "Exemplo 3: Viga com múltiplas cargas":
            st.markdown("""
            ### 📐 Exemplo 3: Viga com Múltiplas Cargas
            
            **Dados:**
            - Comprimento: $L = 10$ m
            - Carga pontual $P_1 = 20$ kN em $x_1 = 2$ m
            - Carga pontual $P_2 = 30$ kN em $x_2 = 6$ m
            - Carga distribuída $q = 5$ kN/m de $x = 0$ a $x = 10$ m
            
            **Solução:**
            
            **1. Carga total:**
            $$
            Q_{total} = P_1 + P_2 + q \\cdot L = 20 + 30 + 5 \\times 10 = 100 \\text{ kN}
            $$
            
            **2. Equilíbrio de momentos (em relação a A):**
            $$
            V_B \\cdot 10 = 20 \\times 2 + 30 \\times 6 + 5 \\times 10 \\times 5 = 40 + 180 + 250 = 470
            $$
            $$
            V_B = \\frac{470}{10} = 47 \\text{ kN}
            $$
            
            **3. Calcular $V_A$:**
            $$
            V_A = 100 - 47 = 53 \\text{ kN}
            $$
            
            **✅ Resultado:**
            - $V_A = 53$ kN (↑)
            - $V_B = 47$ kN (↑)
            
            **Dica:** Use a calculadora interativa para visualizar os diagramas!
            """)
        
        elif exemplo_escolhido == "Exemplo 4: Dimensionamento de concreto":
            st.markdown("""
            ### 🏗️ Exemplo 4: Dimensionamento de Viga de Concreto Armado
            
            **Dados:**
            - Momento fletor: $M_k = 150$ kN.m
            - Concreto: $f_{ck} = 25$ MPa
            - Aço: CA50
            - Largura: $b_w = 0.20$ m
            - Altura útil: $d = 0.45$ m
            
            **Solução:**
            
            **1. Propriedades dos materiais:**
            $$
            f_{cd} = \\frac{f_{ck}}{\\gamma_c} = \\frac{25}{1.4} = 17.86 \\text{ MPa}
            $$
            $$
            f_{yd} = \\frac{f_{yk}}{\\gamma_s} = \\frac{500}{1.15} = 435 \\text{ MPa}
            $$
            
            **2. Momento adimensional:**
            $$
            m_d = \\frac{M_d}{b_w \\cdot d^2 \\cdot f_{cd}} = \\frac{150 \\times 1000}{0.20 \\times 0.45^2 \\times 17.86 \\times 10^6} = 0.208
            $$
            
            **3. Altura da linha neutra:**
            $$
            \\frac{x}{d} = 1.25 \\times \\left(1 - \\sqrt{1 - \\frac{2 \\times 0.208}{0.68}}\\right) = 0.35
            $$
            $$
            x = 0.35 \\times 0.45 = 0.158 \\text{ m} = 15.8 \\text{ cm}
            $$
            
            **4. Verificação do domínio:**
            - $x/d = 0.35$ → Domínio 3 ✅ (ideal)
            
            **5. Área de aço:**
            $$
            A_s = \\frac{M_d}{f_{yd} \\cdot (d - 0.4x)} = \\frac{150 \\times 1000}{435 \\times 10^6 \\times (0.45 - 0.4 \\times 0.158)} = 11.2 \\text{ cm}^2
            $$
            
            **✅ Resultado:**
            - $A_s = 11.2$ cm²
            - Sugestão: **15 barras de 10 mm** ou **9 barras de 12.5 mm**
            """)

def show_calculadora_vigas():
    """Calculadora de vigas isostáticas com visualizações melhoradas"""
    st.subheader("📊 Calculadora de Vigas Isostáticas")
    
    st.markdown("""
    ### 🎯 Como Usar
    
    Esta calculadora permite analisar vigas isostáticas com múltiplas cargas pontuais e distribuídas.
    Preencha os dados abaixo e clique em "Calcular" para obter:
    - ✅ Reações de apoio
    - ✅ Diagrama de Esforço Cortante (DEC)
    - ✅ Diagrama de Momento Fletor (DMF)
    - ✅ Valores máximos e suas posições
    - ✅ Esquema visual da viga
    
    **Dica:** Comece com um exemplo simples e vá adicionando complexidade!
    """)
    
    st.markdown("---")
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        comprimento = st.number_input("Comprimento da viga (m)", min_value=0.1, value=5.0, step=0.1)
    
    with col2:
        num_pontos = st.number_input("Número de pontos para cálculo", min_value=50, max_value=1000, value=200, step=50)
    
    st.markdown("---")
    st.markdown("### Cargas Pontuais")
    
    num_cargas_pontuais = st.number_input("Número de cargas pontuais", min_value=0, max_value=10, value=1, step=1)
    
    cargas_pontuais = []
    for i in range(num_cargas_pontuais):
        col1, col2 = st.columns(2)
        with col1:
            posicao = st.number_input(f"Posição carga {i+1} (m)", min_value=0.0, max_value=float(comprimento), value=comprimento/2, key=f"pos_p_{i}")
        with col2:
            valor = st.number_input(f"Valor carga {i+1} (kN)", value=10.0, key=f"val_p_{i}")
        cargas_pontuais.append({'posicao': posicao, 'valor': valor})
    
    st.markdown("---")
    st.markdown("### Cargas Distribuídas")
    
    num_cargas_dist = st.number_input("Número de cargas distribuídas", min_value=0, max_value=10, value=0, step=1)
    
    cargas_distribuidas = []
    for i in range(num_cargas_dist):
        col1, col2, col3 = st.columns(3)
        with col1:
            inicio = st.number_input(f"Início carga {i+1} (m)", min_value=0.0, max_value=float(comprimento), value=0.0, key=f"ini_d_{i}")
        with col2:
            fim = st.number_input(f"Fim carga {i+1} (m)", min_value=0.0, max_value=float(comprimento), value=comprimento, key=f"fim_d_{i}")
        with col3:
            valor = st.number_input(f"Valor carga {i+1} (kN/m)", value=5.0, key=f"val_d_{i}")
        cargas_distribuidas.append({'inicio': inicio, 'fim': fim, 'valor': valor})
    
    if st.button("Calcular", type="primary"):
        # Calcular reações
        reacoes = calcular_reacoes_viga_simples(comprimento, cargas_pontuais, cargas_distribuidas)
        
        # Calcular esforços
        x = np.linspace(0, comprimento, num_pontos)
        cortante, momento = calcular_esforcos_viga(x, comprimento, cargas_pontuais, cargas_distribuidas, reacoes)
        
        # Exibir resultados
        col1, col2 = st.columns(2)
        with col1:
            st.metric("Reação em A (Va)", f"{reacoes['Va']:.2f} kN")
        with col2:
            st.metric("Reação em B (Vb)", f"{reacoes['Vb']:.2f} kN")
        
        # Esquema da viga
        st.markdown("### 📐 Esquema da Viga")
        fig_esquema = plot_viga_esquema(comprimento, cargas_pontuais, cargas_distribuidas, reacoes)
        st.plotly_chart(fig_esquema, use_container_width=True)
        
        st.markdown("---")
        st.markdown("### 📊 Diagramas de Esforços")
        
        # Plotar diagramas
        fig_v, fig_m = plot_diagrama_cortante_momento(x, cortante, momento, reacoes, cargas_pontuais, cargas_distribuidas, comprimento)
        st.plotly_chart(fig_v, use_container_width=True)
        st.plotly_chart(fig_m, use_container_width=True)
        
        # Análise detalhada
        st.markdown("---")
        st.markdown("### 🔍 Análise Detalhada")
        
        # Onde o cortante é zero
        idx_zero_v = np.where(np.abs(cortante) < np.max(np.abs(cortante)) * 0.01)[0]
        if len(idx_zero_v) > 0:
            st.info(f"📍 **Pontos onde V = 0:** {', '.join([f'x = {x[i]:.2f} m' for i in idx_zero_v[:3]])} - Nestes pontos, o momento é máximo ou mínimo.")
        
        # Verificação de equilíbrio
        soma_reacoes = reacoes['Va'] + reacoes['Vb']
        soma_cargas = sum([c['valor'] for c in cargas_pontuais]) + sum([c['valor'] * (c['fim'] - c['inicio']) for c in cargas_distribuidas])
        erro = abs(soma_reacoes - soma_cargas)
        
        if erro < 0.01:
            st.success(f"✅ **Equilíbrio verificado:** ΣFy = {soma_reacoes:.2f} kN")
        else:
            st.warning(f"⚠️ **Erro no equilíbrio:** {erro:.2f} kN")
        
        # Valores máximos
        st.markdown("### Valores Máximos")
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            st.metric("Cortante Máximo", f"{np.max(np.abs(cortante)):.2f} kN")
        with col2:
            st.metric("Momento Máximo", f"{np.max(np.abs(momento)):.2f} kN.m")
        with col3:
            idx_max_v = np.argmax(np.abs(cortante))
            st.metric("Posição Max Cortante", f"{x[idx_max_v]:.2f} m")
        with col4:
            idx_max_m = np.argmax(np.abs(momento))
            st.metric("Posição Max Momento", f"{x[idx_max_m]:.2f} m")

def show_calculadora_propriedades():
    """Calculadora de propriedades geométricas"""
    st.subheader("📐 Calculadora de Propriedades Geométricas")
    
    tipo_secao = st.selectbox("Tipo de Seção", ["retangulo", "t", "i"])
    
    dimensoes = {}
    
    if tipo_secao == "retangulo":
        col1, col2 = st.columns(2)
        with col1:
            dimensoes['largura'] = st.number_input("Largura b (m)", min_value=0.01, value=0.2, step=0.01)
        with col2:
            dimensoes['altura'] = st.number_input("Altura h (m)", min_value=0.01, value=0.5, step=0.01)
    
    elif tipo_secao == "t":
        st.markdown("**Dimensões da Mesa:**")
        col1, col2 = st.columns(2)
        with col1:
            dimensoes['largura_mesa'] = st.number_input("Largura da mesa bf (m)", min_value=0.01, value=0.3, step=0.01)
        with col2:
            dimensoes['espessura_mesa'] = st.number_input("Espessura da mesa tf (m)", min_value=0.01, value=0.1, step=0.01)
        
        st.markdown("**Dimensões da Alma:**")
        col1, col2 = st.columns(2)
        with col1:
            dimensoes['altura_alma'] = st.number_input("Altura da alma hw (m)", min_value=0.01, value=0.4, step=0.01)
        with col2:
            dimensoes['espessura_alma'] = st.number_input("Espessura da alma tw (m)", min_value=0.01, value=0.1, step=0.01)
    
    elif tipo_secao == "i":
        st.markdown("**Dimensões da Mesa:**")
        col1, col2 = st.columns(2)
        with col1:
            dimensoes['largura_mesa'] = st.number_input("Largura da mesa bf (m)", min_value=0.01, value=0.3, step=0.01)
        with col2:
            dimensoes['espessura_mesa'] = st.number_input("Espessura da mesa tf (m)", min_value=0.01, value=0.1, step=0.01)
        
        st.markdown("**Dimensões da Alma:**")
        col1, col2 = st.columns(2)
        with col1:
            dimensoes['altura_alma'] = st.number_input("Altura da alma hw (m)", min_value=0.01, value=0.4, step=0.01)
        with col2:
            dimensoes['espessura_alma'] = st.number_input("Espessura da alma tw (m)", min_value=0.01, value=0.1, step=0.01)
    
    if st.button("Calcular Propriedades", type="primary"):
        try:
            props = calcular_propriedades_geometricas(tipo_secao, dimensoes)
            
            st.markdown("### Resultados")
            col1, col2, col3, col4 = st.columns(4)
            with col1:
                st.metric("Área", f"{props['area']*1e4:.2f} cm²")
            with col2:
                st.metric("Centroide y", f"{props['centroide_y']*100:.2f} cm")
            with col3:
                st.metric("Ix", f"{props['Ix']*1e8:.2f} cm⁴")
            with col4:
                st.metric("Iy", f"{props['Iy']*1e8:.2f} cm⁴")
            
            # Módulo de resistência
            Wx = props['Ix'] / max(props['centroide_y'], dimensoes.get('altura', dimensoes.get('altura_alma', 0) + dimensoes.get('espessura_mesa', 0)) - props['centroide_y'])
            st.metric("Módulo de Resistência Wx", f"{Wx*1e6:.2f} cm³")
            
        except Exception as e:
            st.error(f"Erro no cálculo: {str(e)}")

def show_calculadora_concreto():
    """Calculadora de dimensionamento de concreto"""
    st.subheader("🏗️ Dimensionamento de Concreto Armado")
    
    col1, col2 = st.columns(2)
    with col1:
        Mk = st.number_input("Momento Fletor de Cálculo Mk (kN.m)", min_value=0.1, value=100.0, step=1.0)
    with col2:
        fck = st.number_input("Resistência do Concreto fck (MPa)", min_value=20, max_value=90, value=25, step=5)
    
    col1, col2 = st.columns(2)
    with col1:
        aco_tipo = st.selectbox("Tipo de Aço", ["CA50", "CA60"])
    with col2:
        bw = st.number_input("Largura da Seção bw (m)", min_value=0.1, value=0.2, step=0.05)
    
    col1, col2 = st.columns(2)
    with col1:
        usar_h = st.checkbox("Usar altura total h")
        if usar_h:
            h = st.number_input("Altura total h (m)", min_value=0.2, value=0.5, step=0.05)
            d = None
        else:
            h = None
            d = st.number_input("Altura útil d (m)", min_value=0.2, value=0.45, step=0.05)
    with col2:
        pass
    
    if st.button("Dimensionar", type="primary"):
        try:
            resultado = dimensionar_concreto_armado_simples(Mk, fck, aco_tipo, bw, d, h)
            
            st.markdown("### Resultados do Dimensionamento")
            col1, col2, col3, col4 = st.columns(4)
            with col1:
                st.metric("Área de Aço As", f"{resultado['As']:.2f} cm²")
            with col2:
                st.metric("Domínio", resultado['dominio'])
            with col3:
                st.metric("Altura da LN x", f"{resultado['x']:.2f} cm")
            with col4:
                st.metric("Altura útil d", f"{resultado['d']:.2f} cm")
            
            # Verificação
            if "Domínio 4" in resultado['dominio']:
                st.warning("⚠️ Atenção: Dimensionamento no Domínio 4. É necessário usar armadura dupla!")
            elif "Domínio 2" in resultado['dominio']:
                st.info("ℹ️ Dimensionamento no Domínio 2. A seção está subdimensionada.")
            else:
                st.success("✅ Dimensionamento adequado no Domínio 3.")
            
            # Sugestão de bitola
            bitolas = [6.3, 8.0, 10.0, 12.5, 16.0, 20.0, 25.0]
            area_bitola = {6.3: 0.312, 8.0: 0.503, 10.0: 0.785, 12.5: 1.227, 16.0: 2.011, 20.0: 3.142, 25.0: 4.909}
            
            st.markdown("### Sugestão de Armadura")
            for bitola in bitolas:
                num_barras = int(np.ceil(resultado['As'] / area_bitola[bitola]))
                if num_barras <= 20:  # Limite razoável
                    st.write(f"**{num_barras} barras de {bitola:.1f} mm** (As = {num_barras * area_bitola[bitola]:.2f} cm²)")
                    break
            
        except Exception as e:
            st.error(f"Erro no dimensionamento: {str(e)}")

def show():
    """Função principal do módulo de Estruturas"""
    st.title("🏛️ Módulo de Estruturas")
    st.markdown("---")
    
    tab_teoria, tab_calc = st.tabs(["📖 Teoria", "🧮 Calculadoras"])
    
    with tab_teoria:
        show_teoria()
    
    with tab_calc:
        calc_tab = st.radio(
            "Selecione a Calculadora:",
            ["Vigas Isostáticas", "Propriedades Geométricas", "Dimensionamento de Concreto"],
            horizontal=True
        )
        
        st.markdown("---")
        
        if calc_tab == "Vigas Isostáticas":
            show_calculadora_vigas()
        elif calc_tab == "Propriedades Geométricas":
            show_calculadora_propriedades()
        elif calc_tab == "Dimensionamento de Concreto":
            show_calculadora_concreto()

