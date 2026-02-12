"""
Módulo de Fundamentos (Ciclo Básico) - Versão Expandida e Didática
Geometria Analítica, Física, Cálculo Numérico e Demonstrações de Operações Básicas
"""

import streamlit as st
import numpy as np
import plotly.graph_objects as go
from scipy.optimize import fsolve, brentq
import sys
import os

# Adicionar path para imports
base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, base_dir)

def show_teoria():
    """Aba de teoria expandida do módulo de Fundamentos"""
    st.header("📖 Teoria Detalhada - Fundamentos")
    
    st.info("""
    💡 **Fundamentos da Engenharia Civil:** Esta seção cobre os conceitos matemáticos e físicos essenciais 
    que fundamentam todas as disciplinas da engenharia civil.
    """)
    
    tab1, tab2, tab3, tab4, tab5 = st.tabs([
        "Vetores 3D", 
        "Métodos Numéricos", 
        "Conversão de Unidades", 
        "Cálculo Diferencial e Integral",
        "Operações Básicas"
    ])
    
    with tab1:
        st.subheader("📐 Geometria Analítica - Vetores 3D")
        
        st.markdown("""
        ## 🎯 Introdução
        
        Os **vetores** são fundamentais na engenharia para representar grandezas que possuem magnitude, direção e sentido:
        - Forças
        - Velocidades
        - Acelerações
        - Momentos
        - Deslocamentos
        
        ### Representação de um Vetor
        
        Um vetor no espaço 3D pode ser representado como:
        
        $$
        \\vec{u} = u_x \\hat{i} + u_y \\hat{j} + u_z \\hat{k}
        $$
        
        Onde:
        - $u_x, u_y, u_z$: Componentes do vetor
        - $\\hat{i}, \\hat{j}, \\hat{k}$: Vetores unitários dos eixos x, y, z
        """)
        
        st.markdown("---")
        
        st.markdown("""
        ## ➕ Operações com Vetores
        
        ### 1. Soma de Vetores
        
        $$
        \\vec{u} + \\vec{v} = (u_x + v_x)\\hat{i} + (u_y + v_y)\\hat{j} + (u_z + v_z)\\hat{k}
        $$
        
        **Interpretação Geométrica:** A soma é o vetor que vai do início de $\\vec{u}$ até o fim de $\\vec{v}$.
        
        ### 2. Módulo (Magnitude) de um Vetor
        
        $$
        |\\vec{u}| = \\sqrt{u_x^2 + u_y^2 + u_z^2}
        $$
        
        **Interpretação:** Distância da origem até a ponta do vetor.
        
        ### 3. Produto Escalar (Produto Interno)
        
        $$
        \\vec{u} \\cdot \\vec{v} = u_x v_x + u_y v_y + u_z v_z = |\\vec{u}| \\cdot |\\vec{v}| \\cdot \\cos(\\theta)
        $$
        
        **Onde $\\theta$ é o ângulo entre os vetores.**
        
        **Propriedades:**
        - Resultado é um **escalar** (número)
        - $\\vec{u} \\cdot \\vec{v} = 0$ se os vetores são perpendiculares
        - $\\vec{u} \\cdot \\vec{u} = |\\vec{u}|^2$
        
        **Aplicações:**
        - Calcular trabalho: $W = \\vec{F} \\cdot \\vec{d}$
        - Verificar perpendicularidade
        - Projeção de um vetor sobre outro
        
        ### 4. Produto Vetorial (Produto Externo)
        
        $$
        \\vec{u} \\times \\vec{v} = \\begin{vmatrix}
        \\hat{i} & \\hat{j} & \\hat{k} \\\\
        u_x & u_y & u_z \\\\
        v_x & v_y & v_z
        \\end{vmatrix}
        $$
        
        **Resultado:**
        $$
        \\vec{u} \\times \\vec{v} = (u_y v_z - u_z v_y)\\hat{i} - (u_x v_z - u_z v_x)\\hat{j} + (u_x v_y - u_y v_x)\\hat{k}
        $$
        
        **Propriedades:**
        - Resultado é um **vetor**
        - Direção: Perpendicular ao plano formado por $\\vec{u}$ e $\\vec{v}$
        - Módulo: $|\\vec{u} \\times \\vec{v}| = |\\vec{u}| \\cdot |\\vec{v}| \\cdot \\sin(\\theta)$
        - $\\vec{u} \\times \\vec{v} = -\\vec{v} \\times \\vec{u}$ (anti-comutativo)
        
        **Aplicações:**
        - Calcular momento: $\\vec{M} = \\vec{r} \\times \\vec{F}$
        - Calcular área de paralelogramo
        - Verificar paralelismo: $\\vec{u} \\times \\vec{v} = \\vec{0}$ se paralelos
        """)
        
        with st.expander("🔍 Exemplo: Cálculo de Momento de uma Força", expanded=False):
            st.markdown("""
            **Problema:** Calcular o momento da força $\\vec{F} = 10\\hat{i} + 5\\hat{j}$ N aplicada no ponto 
            $\\vec{r} = 2\\hat{i} + 3\\hat{j}$ m em relação à origem.
            
            **Solução:**
            
            $$
            \\vec{M} = \\vec{r} \\times \\vec{F} = \\begin{vmatrix}
            \\hat{i} & \\hat{j} & \\hat{k} \\\\
            2 & 3 & 0 \\\\
            10 & 5 & 0
            \\end{vmatrix}
            $$
            
            $$
            \\vec{M} = (2 \\times 0 - 0 \\times 5)\\hat{i} - (2 \\times 0 - 0 \\times 10)\\hat{j} + (2 \\times 5 - 3 \\times 10)\\hat{k}
            $$
            
            $$
            \\vec{M} = -20\\hat{k} \\text{ N.m}
            $$
            
            **Interpretação:** Momento de 20 N.m no sentido negativo do eixo z (regra da mão direita).
            """)
    
    with tab2:
        st.subheader("🔢 Métodos Numéricos - Cálculo de Raízes")
        
        st.markdown("""
        ## 🎯 Introdução
        
        Muitos problemas de engenharia requerem encontrar raízes de equações não-lineares. Os métodos numéricos 
        permitem resolver essas equações quando métodos analíticos não são viáveis.
        
        **Exemplos de Aplicação:**
        - Equações de estado em termodinâmica
        - Equações transcendentais
        - Equações polinomiais de alto grau
        - Equações implícitas em projetos
        """)
        
        st.markdown("---")
        
        st.markdown("""
        ## 📊 Método de Newton-Raphson
        
        O método de Newton-Raphson é um método iterativo que converge rapidamente quando a estimativa inicial 
        está próxima da raiz.
        
        ### Algoritmo
        
        $$
        x_{n+1} = x_n - \\frac{f(x_n)}{f'(x_n)}
        $$
        
        **Onde:**
        - $x_n$: Estimativa atual
        - $f(x_n)$: Valor da função na estimativa atual
        - $f'(x_n)$: Derivada da função na estimativa atual
        
        ### Condições de Convergência
        
        1. A função deve ser **diferenciável** na região da raiz
        2. A derivada não deve ser zero: $f'(x) \\neq 0$
        3. A estimativa inicial deve estar **próxima** da raiz
        4. A função deve ter **concavidade adequada**
        
        ### Vantagens
        
        - ✅ Convergência **rápida** (ordem quadrática)
        - ✅ Precisão alta com poucas iterações
        
        ### Desvantagens
        
        - ❌ Requer cálculo da **derivada**
        - ❌ Pode divergir se a estimativa inicial for ruim
        - ❌ Não funciona se $f'(x) = 0$ na raiz
        """)
        
        st.markdown("---")
        
        st.markdown("""
        ## 🔄 Método da Bisseção
        
        O método da bisseção é um método robusto que sempre converge, desde que a função mude de sinal no intervalo.
        
        ### Algoritmo
        
        Dado intervalo $[a, b]$ tal que $f(a) \\cdot f(b) < 0$:
        
        1. Calcular ponto médio: $c = \\frac{a + b}{2}$
        2. Avaliar $f(c)$
        3. Se $f(a) \\cdot f(c) < 0$, então a raiz está em $[a, c]$
        4. Caso contrário, a raiz está em $[c, b]$
        5. Repetir até convergência
        
        ### Condições de Convergência
        
        1. A função deve ser **contínua** no intervalo
        2. Deve haver **mudança de sinal**: $f(a) \\cdot f(b) < 0$
        3. Deve haver **apenas uma raiz** no intervalo
        
        ### Vantagens
        
        - ✅ **Sempre converge** (método robusto)
        - ✅ Não requer derivada
        - ✅ Fácil de implementar
        
        ### Desvantagens
        
        - ❌ Convergência **lenta** (ordem linear)
        - ❌ Requer intervalo inicial com mudança de sinal
        """)
        
        with st.expander("🔍 Exemplo: Encontrar Raiz de $f(x) = x^3 - x - 2$", expanded=False):
            st.markdown("""
            **Usando Método da Bisseção:**
            
            **Passo 1:** Verificar mudança de sinal
            - $f(1) = 1 - 1 - 2 = -2$ (negativo)
            - $f(2) = 8 - 2 - 2 = 4$ (positivo)
            - Intervalo inicial: $[1, 2]$
            
            **Passo 2:** Primeira iteração
            - $c_1 = \\frac{1 + 2}{2} = 1.5$
            - $f(1.5) = 3.375 - 1.5 - 2 = -0.125$ (negativo)
            - Nova raiz: $[1.5, 2]$
            
            **Passo 3:** Segunda iteração
            - $c_2 = \\frac{1.5 + 2}{2} = 1.75$
            - $f(1.75) = 5.359 - 1.75 - 2 = 1.609$ (positivo)
            - Nova raiz: $[1.5, 1.75]$
            
            **Continua até convergência...**
            
            **Raiz aproximada:** $x \\approx 1.521$
            """)
    
    with tab3:
        st.subheader("🔄 Conversão de Unidades de Engenharia")
        
        st.markdown("""
        ## 🎯 Introdução
        
        A conversão de unidades é fundamental na engenharia, especialmente ao trabalhar com sistemas diferentes 
        (SI vs Imperial) ou ao interpretar dados de diferentes fontes.
        """)
        
        st.markdown("---")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("""
            ### 📏 Unidades de Pressão
            
            **Sistema Internacional (SI):**
            - Pascal (Pa) = N/m²
            - 1 kPa = 1.000 Pa
            - 1 MPa = 1.000.000 Pa = 1 N/mm²
            - 1 bar = 100 kPa = 0.1 MPa
            
            **Sistema Imperial:**
            - 1 psi (pound per square inch) = 6.894,76 Pa
            - 1 ksi = 1.000 psi = 6.895 MPa
            - 1 atm = 101.325 Pa = 14.696 psi
            
            **Conversões Úteis:**
            $$
            \\begin{align}
            1 \\text{ MPa} &= 145.038 \\text{ psi} \\\\
            1 \\text{ psi} &= 0.006895 \\text{ MPa} \\\\
            1 \\text{ bar} &= 14.504 \\text{ psi}
            \\end{align}
            $$
            """)
        
        with col2:
            st.markdown("""
            ### 🌊 Unidades de Viscosidade
            
            **Viscosidade Dinâmica ($\\mu$):**
            - 1 Pa.s = 10 poise
            - 1 cP (centipoise) = 0.001 Pa.s
            - 1 N.s/m² = 1 Pa.s
            
            **Viscosidade Cinemática ($\\nu$):**
            - $\\nu = \\frac{\\mu}{\\rho}$
            - 1 m²/s = 10.000 stokes
            - 1 cSt (centistokes) = 10⁻⁶ m²/s
            
            **Valores Típicos:**
            - Água a 20°C: $\\mu = 0.001$ Pa.s
            - Óleo motor: $\\mu \\approx 0.1$ Pa.s
            """)
        
        st.markdown("---")
        
        st.markdown("""
        ### ⚖️ Unidades de Tensão e Força
        
        **Tensão ($\\sigma$):**
        - 1 Pa = 1 N/m²
        - 1 MPa = 1 N/mm²
        - 1 GPa = 1.000 MPa
        - 1 ksi = 6.895 MPa
        
        **Força:**
        - 1 N = 0.2248 lbf (pound-force)
        - 1 kN = 224.8 lbf
        - 1 kgf = 9.80665 N
        
        ### 📐 Unidades de Comprimento
        
        - 1 m = 3.28084 ft (pés)
        - 1 m = 39.3701 in (polegadas)
        - 1 ft = 0.3048 m
        - 1 in = 25.4 mm
        
        ### ⚡ Unidades de Momento e Torque
        
        - 1 N.m = 0.7376 lbf.ft
        - 1 kN.m = 737.6 lbf.ft
        - 1 kgf.m = 9.80665 N.m
        """)
    
    with tab4:
        st.subheader("📈 Cálculo Diferencial e Integral - Cálculo 1 e 2")
        
        st.markdown("""
        ## 🎯 Introdução
        
        O **Cálculo Diferencial e Integral** é fundamental para a engenharia. Esta seção cobre os principais 
        tópicos de Cálculo 1 e 2, baseados no livro de Stewart.
        """)
        
        sub_tab1, sub_tab2, sub_tab3, sub_tab4, sub_tab5, sub_tab6, sub_tab7 = st.tabs([
            "Cálculo 1: Limites e Derivadas",
            "Cálculo 1: Integrais",
            "Cálculo 2: Técnicas de Integração",
            "Cálculo 3: Funções de Várias Variáveis",
            "Cálculo 4: Equações Diferenciais",
            "Cálculo 5: Séries e Transformadas",
            "Aplicações na Engenharia"
        ])
        
        with sub_tab1:
            st.markdown("""
            ## 📚 Cálculo 1: Limites, Continuidade e Derivadas
            
            ### 📊 Limites
            
            O **limite** de uma função quando $x$ se aproxima de $a$ é o valor que a função se aproxima:
            
            $$
            \\lim_{x \\to a} f(x) = L
            $$
            
            **Propriedades dos Limites:**
            
            $$
            \\lim_{x \\to a} [f(x) + g(x)] = \\lim_{x \\to a} f(x) + \\lim_{x \\to a} g(x)
            $$
            
            $$
            \\lim_{x \\to a} [f(x) \\cdot g(x)] = \\lim_{x \\to a} f(x) \\cdot \\lim_{x \\to a} g(x)
            $$
            
            $$
            \\lim_{x \\to a} \\frac{f(x)}{g(x)} = \\frac{\\lim_{x \\to a} f(x)}{\\lim_{x \\to a} g(x)}, \\quad \\text{se } \\lim_{x \\to a} g(x) \\neq 0
            $$
            
            **Limites Importantes:**
            
            $$
            \\lim_{x \\to 0} \\frac{\\sin(x)}{x} = 1
            $$
            
            $$
            \\lim_{x \\to \\infty} \\left(1 + \\frac{1}{x}\\right)^x = e
            $$
            
            $$
            \\lim_{x \\to 0} \\frac{e^x - 1}{x} = 1
            $$
            
            ### 🔄 Continuidade
            
            Uma função $f$ é **contínua** em $x = a$ se:
            
            $$
            \\lim_{x \\to a} f(x) = f(a)
            $$
            
            **Condições:**
            1. $f(a)$ está definida
            2. $\\lim_{x \\to a} f(x)$ existe
            3. $\\lim_{x \\to a} f(x) = f(a)$
            
            **Tipos de Descontinuidade:**
            - **Removível:** Limite existe mas $f(a)$ não está definida ou é diferente
            - **Salto:** Limites laterais existem mas são diferentes
            - **Infinita:** Limite é infinito
            """)
            
            st.markdown("---")
            
            st.markdown("""
            ### 📐 Derivadas - Conceito e Definição
            
            A **derivada** de uma função $f$ em um ponto $x$ é a taxa de variação instantânea:
            
            $$
            f'(x) = \\lim_{h \\to 0} \\frac{f(x+h) - f(x)}{h}
            $$
            
            **Interpretação Geométrica:**
            - A derivada é a **inclinação da reta tangente** ao gráfico no ponto
            - Representa a **taxa de variação** da função
            
            **Interpretação Física:**
            - **Velocidade:** Derivada da posição em relação ao tempo
            - **Aceleração:** Derivada da velocidade em relação ao tempo
            - **Taxa de variação:** Qualquer grandeza que varia com outra
            """)
            
            st.markdown("---")
            
            st.markdown("""
            ### 📋 Regras de Derivação
            
            **Regra da Constante:**
            $$
            \\frac{d}{dx}[c] = 0
            $$
            
            **Regra da Potência:**
            $$
            \\frac{d}{dx}[x^n] = n \\cdot x^{n-1}
            $$
            
            **Regra da Soma:**
            $$
            \\frac{d}{dx}[f(x) + g(x)] = f'(x) + g'(x)
            $$
            
            **Regra do Produto:**
            $$
            \\frac{d}{dx}[f(x) \\cdot g(x)] = f'(x) \\cdot g(x) + f(x) \\cdot g'(x)
            $$
            
            **Regra do Quociente:**
            $$
            \\frac{d}{dx}\\left[\\frac{f(x)}{g(x)}\\right] = \\frac{f'(x) \\cdot g(x) - f(x) \\cdot g'(x)}{[g(x)]^2}
            $$
            
            **Regra da Cadeia:**
            $$
            \\frac{d}{dx}[f(g(x))] = f'(g(x)) \\cdot g'(x)
            $$
            """)
            
            st.markdown("---")
            
            st.markdown("""
            ### 📚 Derivadas de Funções Elementares
            
            **Funções Trigonométricas:**
            $$
            \\frac{d}{dx}[\\sin(x)] = \\cos(x)
            $$
            
            $$
            \\frac{d}{dx}[\\cos(x)] = -\\sin(x)
            $$
            
            $$
            \\frac{d}{dx}[\\tan(x)] = \\sec^2(x)
            $$
            
            $$
            \\frac{d}{dx}[\\sec(x)] = \\sec(x) \\tan(x)
            $$
            
            $$
            \\frac{d}{dx}[\\csc(x)] = -\\csc(x) \\cot(x)
            $$
            
            $$
            \\frac{d}{dx}[\\cot(x)] = -\\csc^2(x)
            $$
            
            **Funções Exponenciais e Logarítmicas:**
            $$
            \\frac{d}{dx}[e^x] = e^x
            $$
            
            $$
            \\frac{d}{dx}[a^x] = a^x \\ln(a)
            $$
            
            $$
            \\frac{d}{dx}[\\ln(x)] = \\frac{1}{x}
            $$
            
            $$
            \\frac{d}{dx}[\\log_a(x)] = \\frac{1}{x \\ln(a)}
            $$
            
            **Funções Inversas:**
            $$
            \\frac{d}{dx}[\\arcsin(x)] = \\frac{1}{\\sqrt{1-x^2}}
            $$
            
            $$
            \\frac{d}{dx}[\\arccos(x)] = -\\frac{1}{\\sqrt{1-x^2}}
            $$
            
            $$
            \\frac{d}{dx}[\\arctan(x)] = \\frac{1}{1+x^2}
            $$
            """)
            
            st.markdown("---")
            
            st.markdown("""
            ### 📈 Aplicações das Derivadas
            
            **Máximos e Mínimos:**
            - Se $f'(c) = 0$ e $f''(c) > 0$, então $f$ tem um **mínimo local** em $c$
            - Se $f'(c) = 0$ e $f''(c) < 0$, então $f$ tem um **máximo local** em $c$
            
            **Concavidade:**
            - Se $f''(x) > 0$ em um intervalo, $f$ é **côncava para cima**
            - Se $f''(x) < 0$ em um intervalo, $f$ é **côncava para baixo**
            
            **Ponto de Inflexão:**
            - Ocorre onde $f''(x) = 0$ e há mudança de concavidade
            
            **Regra de L'Hôpital:**
            Para formas indeterminadas $\\frac{0}{0}$ ou $\\frac{\\infty}{\\infty}$:
            $$
            \\lim_{x \\to a} \\frac{f(x)}{g(x)} = \\lim_{x \\to a} \\frac{f'(x)}{g'(x)}
            $$
            """)
        
        with sub_tab2:
            st.markdown("""
            ### 📐 Derivadas - Conceito e Definição
            
            A **derivada** de uma função $f$ em um ponto $x$ é a taxa de variação instantânea:
            
            $$
            f'(x) = \\lim_{h \\to 0} \\frac{f(x+h) - f(x)}{h}
            $$
            
            **Interpretação Geométrica:**
            - A derivada é a **inclinação da reta tangente** ao gráfico no ponto
            - Representa a **taxa de variação** da função
            
            **Interpretação Física:**
            - **Velocidade:** Derivada da posição em relação ao tempo
            - **Aceleração:** Derivada da velocidade em relação ao tempo
            - **Taxa de variação:** Qualquer grandeza que varia com outra
            """)
            
            st.markdown("---")
            
            st.markdown("""
            ### 📋 Regras de Derivação
            
            **Regra da Constante:**
            $$
            \\frac{d}{dx}[c] = 0
            $$
            
            **Regra da Potência:**
            $$
            \\frac{d}{dx}[x^n] = n \\cdot x^{n-1}
            $$
            
            **Regra da Soma:**
            $$
            \\frac{d}{dx}[f(x) + g(x)] = f'(x) + g'(x)
            $$
            
            **Regra do Produto:**
            $$
            \\frac{d}{dx}[f(x) \\cdot g(x)] = f'(x) \\cdot g(x) + f(x) \\cdot g'(x)
            $$
            
            **Regra do Quociente:**
            $$
            \\frac{d}{dx}\\left[\\frac{f(x)}{g(x)}\\right] = \\frac{f'(x) \\cdot g(x) - f(x) \\cdot g'(x)}{[g(x)]^2}
            $$
            
            **Regra da Cadeia:**
            $$
            \\frac{d}{dx}[f(g(x))] = f'(g(x)) \\cdot g'(x)
            $$
            """)
            
            st.markdown("---")
            
            st.markdown("""
            ### 📚 Derivadas de Funções Elementares
            
            **Funções Trigonométricas:**
            $$
            \\frac{d}{dx}[\\sin(x)] = \\cos(x)
            $$
            
            $$
            \\frac{d}{dx}[\\cos(x)] = -\\sin(x)
            $$
            
            $$
            \\frac{d}{dx}[\\tan(x)] = \\sec^2(x)
            $$
            
            **Funções Exponenciais e Logarítmicas:**
            $$
            \\frac{d}{dx}[e^x] = e^x
            $$
            
            $$
            \\frac{d}{dx}[a^x] = a^x \\ln(a)
            $$
            
            $$
            \\frac{d}{dx}[\\ln(x)] = \\frac{1}{x}
            $$
            
            $$
            \\frac{d}{dx}[\\log_a(x)] = \\frac{1}{x \\ln(a)}
            $$
            """)
            
            st.markdown("---")
            
            st.markdown("""
            ### 📈 Aplicações das Derivadas
            
            **Máximos e Mínimos:**
            - Se $f'(c) = 0$ e $f''(c) > 0$, então $f$ tem um **mínimo local** em $c$
            - Se $f'(c) = 0$ e $f''(c) < 0$, então $f$ tem um **máximo local** em $c$
            
            **Concavidade:**
            - Se $f''(x) > 0$ em um intervalo, $f$ é **côncava para cima**
            - Se $f''(x) < 0$ em um intervalo, $f$ é **côncava para baixo**
            
            **Ponto de Inflexão:**
            - Ocorre onde $f''(x) = 0$ e há mudança de concavidade
            """)
        
        with sub_tab3:
            st.markdown("""
            ### 📊 Integrais - Conceito e Definição
            
            A **integral** é a operação inversa da derivada. Existem dois tipos principais:
            
            **Integral Indefinida (Antiderivada):**
            $$
            \\int f(x) \\, dx = F(x) + C
            $$
            
            Onde $F'(x) = f(x)$ e $C$ é a constante de integração.
            
            **Integral Definida:**
            $$
            \\int_a^b f(x) \\, dx = F(b) - F(a)
            $$
            
            **Interpretação Geométrica:**
            - A integral definida representa a **área sob a curva** entre $a$ e $b$
            - Área acima do eixo x é positiva, abaixo é negativa
            """)
            
            st.markdown("---")
            
            st.markdown("""
            ### 📋 Regras de Integração
            
            **Integral da Constante:**
            $$
            \\int c \\, dx = cx + C
            $$
            
            **Regra da Potência:**
            $$
            \\int x^n \\, dx = \\frac{x^{n+1}}{n+1} + C, \\quad n \\neq -1
            $$
            
            **Integral da Soma:**
            $$
            \\int [f(x) + g(x)] \\, dx = \\int f(x) \\, dx + \\int g(x) \\, dx
            $$
            
            **Integração por Partes:**
            $$
            \\int u \\, dv = uv - \\int v \\, du
            $$
            
            **Substituição:**
            $$
            \\int f(g(x)) \\cdot g'(x) \\, dx = \\int f(u) \\, du, \\quad \\text{onde } u = g(x)
            $$
            """)
            
            st.markdown("---")
            
            st.markdown("""
            ### 📚 Integrais de Funções Elementares
            
            **Funções Trigonométricas:**
            $$
            \\int \\sin(x) \\, dx = -\\cos(x) + C
            $$
            
            $$
            \\int \\cos(x) \\, dx = \\sin(x) + C
            $$
            
            $$
            \\int \\sec^2(x) \\, dx = \\tan(x) + C
            $$
            
            **Funções Exponenciais e Logarítmicas:**
            $$
            \\int e^x \\, dx = e^x + C
            $$
            
            $$
            \\int \\frac{1}{x} \\, dx = \\ln|x| + C
            $$
            
            $$
            \\int a^x \\, dx = \\frac{a^x}{\\ln(a)} + C
            $$
            """)
            
            st.markdown("---")
            
            st.markdown("""
            ### 🎯 Teorema Fundamental do Cálculo
            
            **Parte 1:**
            Se $f$ é contínua em $[a, b]$ e $F(x) = \\int_a^x f(t) \\, dt$, então:
            $$
            F'(x) = f(x)
            $$
            
            **Parte 2:**
            Se $f$ é contínua em $[a, b]$ e $F$ é uma antiderivada de $f$, então:
            $$
            \\int_a^b f(x) \\, dx = F(b) - F(a)
            $$
            
            **Interpretação:**
            - A derivada da integral é a função original
            - A integral da derivada é a função original (mais constante)
            """)
        
        with sub_tab7:
            st.markdown("""
            ## 🎯 Aplicações do Cálculo na Engenharia Civil
            
            ### 📐 Cálculo 1 e 2 - Aplicações
            
            **1. Análise de Movimento:**
            - **Posição:** $s(t)$
            - **Velocidade:** $v(t) = s'(t) = \\frac{ds}{dt}$
            - **Aceleração:** $a(t) = v'(t) = s''(t) = \\frac{d^2s}{dt^2}$
            - **Relação inversa:** $s(t) = \\int v(t) \\, dt$
            
            **2. Análise de Diagramas (Estruturas):**
            - **Carga distribuída:** $q(x)$
            - **Cortante:** $V(x) = \\int q(x) \\, dx$
            - **Momento:** $M(x) = \\int V(x) \\, dx$
            - **Relações:** $q(x) = -\\frac{dV}{dx}$, $V(x) = \\frac{dM}{dx}$
            
            **3. Cálculo de Áreas e Volumes:**
            - **Área sob curva:** $A = \\int_a^b f(x) \\, dx$
            - **Volume de revolução:** $V = \\pi \\int_a^b [f(x)]^2 \\, dx$
            - **Centroide:** $\\bar{x} = \\frac{\\int x f(x) \\, dx}{\\int f(x) \\, dx}$
            
            **4. Otimização:**
            - Encontrar máximos e mínimos de funções
            - Dimensionamento ótimo de estruturas
            - Minimização de custos
            """)
            
            st.markdown("---")
            
            st.markdown("""
            ### 📊 Cálculo 3 - Aplicações
            
            **1. Análise de Tensões:**
            - Tensão varia no espaço: $\\sigma(x, y, z)$
            - Derivadas parciais: Taxa de variação em cada direção
            - Gradiente: Direção de maior variação
            
            **2. Transferência de Calor:**
            - Temperatura: $T(x, y, z, t)$
            - Equação do calor: $\\frac{\\partial T}{\\partial t} = \\alpha \\nabla^2 T$
            
            **3. Fluxo de Fluidos:**
            - Velocidade: $\\vec{v}(x, y, z)$
            - Divergência: $\\nabla \\cdot \\vec{v}$ (fontes/sumidouros)
            - Rotacional: $\\nabla \\times \\vec{v}$ (vórtices)
            
            **4. Cálculo de Volumes e Massas:**
            - Volume de sólidos complexos: Integrais triplas
            - Massa com densidade variável: $m = \\iiint \\rho(x,y,z) \\, dV$
            - Centro de massa: $\\bar{x} = \\frac{\\iiint x \\rho \\, dV}{\\iiint \\rho \\, dV}$
            """)
            
            st.markdown("---")
            
            st.markdown("""
            ### 🔄 Cálculo 4 - Aplicações
            
            **1. Vibrações de Estruturas:**
            $$
            m\\frac{d^2u}{dt^2} + c\\frac{du}{dt} + ku = F(t)
            $$
            - $u(t)$: Deslocamento
            - Solução: Vibração livre e forçada
            
            **2. Fluxo de Calor Transiente:**
            $$
            \\frac{\\partial T}{\\partial t} = \\alpha \\frac{\\partial^2 T}{\\partial x^2}
            $$
            - Temperatura varia com tempo e posição
            - Solução: Séries de Fourier
            
            **3. Propagação de Ondas:**
            $$
            \\frac{\\partial^2 u}{\\partial t^2} = c^2 \\frac{\\partial^2 u}{\\partial x^2}
            $$
            - Ondas em estruturas
            - Solução de D'Alembert
            """)
            
            st.markdown("---")
            
            st.markdown("""
            ### 📈 Cálculo 5 - Aplicações
            
            **1. Análise de Sinais:**
            - Transformada de Fourier: Análise espectral
            - Filtragem de sinais
            - Processamento de dados
            
            **2. Resolução de EDPs:**
            - Método de separação de variáveis
            - Séries de Fourier para condições de contorno
            - Transformada de Laplace para condições iniciais
            
            **3. Análise Numérica:**
            - Aproximação por séries de Taylor
            - Métodos numéricos baseados em séries
            - Convergência de métodos iterativos
            """)
            
            with st.expander("🔍 Exemplo: Aplicação em Estruturas", expanded=False):
                st.markdown("""
                **Problema:** Dada carga distribuída $q(x) = 10x$ kN/m em uma viga de 0 a 5 m, 
                determinar cortante e momento.
                
                **Solução:**
                
                **1. Cortante:**
                $$
                V(x) = \\int q(x) \\, dx = \\int 10x \\, dx = 5x^2 + C
                $$
                
                Com $V(0) = V_A$ (reação em A):
                $$
                V(x) = V_A - 5x^2
                $$
                
                **2. Momento:**
                $$
                M(x) = \\int V(x) \\, dx = \\int (V_A - 5x^2) \\, dx = V_A x - \\frac{5x^3}{3} + C
                $$
                
                Com $M(0) = 0$:
                $$
                M(x) = V_A x - \\frac{5x^3}{3}
                $$
                """)
            
            with st.expander("🔍 Exemplo: Aplicação em Transferência de Calor", expanded=False):
                st.markdown("""
                **Problema:** Temperatura em uma barra unidimensional com extremidades a 0°C.
                
                **EDP:**
                $$
                \\frac{\\partial T}{\\partial t} = \\alpha \\frac{\\partial^2 T}{\\partial x^2}
                $$
                
                **Condições:**
                - $T(0, t) = 0$, $T(L, t) = 0$
                - $T(x, 0) = f(x)$
                
                **Solução por Separação de Variáveis:**
                $$
                T(x,t) = \\sum_{n=1}^{\\infty} B_n \\sin\\left(\\frac{n\\pi x}{L}\\right) e^{-\\alpha(n\\pi/L)^2 t}
                $$
                
                Onde $B_n$ são coeficientes de Fourier.
                """)
    
    with tab5:
        st.subheader("🔬 Operações Básicas - Física e Matemática")
        
        st.markdown("""
        ## 🎯 Fundamentos Matemáticos e Físicos
        
        Esta seção apresenta demonstrações interativas das operações básicas que fundamentam a engenharia civil.
        """)
        
        st.markdown("---")
        
        sub_tab1, sub_tab2, sub_tab3, sub_tab4 = st.tabs([
            "Trigonometria", "Álgebra Linear", "Cálculo Diferencial", "Física Básica"
        ])
        
        with sub_tab1:
            st.markdown("""
            ### 📐 Trigonometria - Fundamentos
            
            **Relações no Triângulo Retângulo:**
            
            $$
            \\sin(\\theta) = \\frac{\\text{cateto oposto}}{\\text{hipotenusa}} = \\frac{a}{c}
            $$
            
            $$
            \\cos(\\theta) = \\frac{\\text{cateto adjacente}}{\\text{hipotenusa}} = \\frac{b}{c}
            $$
            
            $$
            \\tan(\\theta) = \\frac{\\text{cateto oposto}}{\\text{cateto adjacente}} = \\frac{a}{b} = \\frac{\\sin(\\theta)}{\\cos(\\theta)}
            $$
            
            **Teorema de Pitágoras:**
            $$
            a^2 + b^2 = c^2
            $$
            
            **Identidades Fundamentais:**
            $$
            \\sin^2(\\theta) + \\cos^2(\\theta) = 1
            $$
            
            $$
            \\sin(2\\theta) = 2\\sin(\\theta)\\cos(\\theta)
            $$
            
            $$
            \\cos(2\\theta) = \\cos^2(\\theta) - \\sin^2(\\theta)
            $$
            
            **Aplicações na Engenharia:**
            - Cálculo de componentes de forças
            - Análise de estruturas inclinadas
            - Topografia e levantamentos
            - Projeto de rampas e escadas
            """)
        
        with sub_tab2:
            st.markdown("""
            ### 🔢 Álgebra Linear - Sistemas de Equações
            
            **Sistema Linear 2x2:**
            $$
            \\begin{cases}
            a_1 x + b_1 y = c_1 \\\\
            a_2 x + b_2 y = c_2
            \\end{cases}
            $$
            
            **Solução por Regra de Cramer:**
            $$
            x = \\frac{\\begin{vmatrix} c_1 & b_1 \\\\ c_2 & b_2 \\end{vmatrix}}{\\begin{vmatrix} a_1 & b_1 \\\\ a_2 & b_2 \\end{vmatrix}}
            $$
            
            $$
            y = \\frac{\\begin{vmatrix} a_1 & c_1 \\\\ a_2 & c_2 \\end{vmatrix}}{\\begin{vmatrix} a_1 & b_1 \\\\ a_2 & b_2 \\end{vmatrix}}
            $$
            
            **Aplicações:**
            - Análise de estruturas isostáticas
            - Resolução de sistemas de equações de equilíbrio
            - Método dos nós em treliças
            """)
        
        with sub_tab3:
            st.markdown("""
            ### 📈 Cálculo Diferencial - Derivadas
            
            **Definição:**
            $$
            f'(x) = \\lim_{h \\to 0} \\frac{f(x+h) - f(x)}{h}
            $$
            
            **Regras Fundamentais:**
            
            **Regra da Potência:**
            $$
            \\frac{d}{dx}(x^n) = n \\cdot x^{n-1}
            $$
            
            **Regra do Produto:**
            $$
            \\frac{d}{dx}[f(x) \\cdot g(x)] = f'(x) \\cdot g(x) + f(x) \\cdot g'(x)
            $$
            
            **Regra do Quociente:**
            $$
            \\frac{d}{dx}\\left[\\frac{f(x)}{g(x)}\\right] = \\frac{f'(x) \\cdot g(x) - f(x) \\cdot g'(x)}{[g(x)]^2}
            $$
            
            **Regra da Cadeia:**
            $$
            \\frac{d}{dx}[f(g(x))] = f'(g(x)) \\cdot g'(x)
            $$
            
            **Aplicações na Engenharia:**
            - Taxa de variação (velocidade, aceleração)
            - Máximos e mínimos (otimização)
            - Análise de diagramas (cortante, momento)
            """)
        
        with sub_tab4:
            st.markdown("""
            ### ⚛️ Física Básica - Mecânica
            
            **Leis de Newton:**
            
            **1ª Lei (Inércia):**
            > Um corpo em repouso permanece em repouso, e um corpo em movimento permanece em movimento 
            > com velocidade constante, a menos que uma força resultante atue sobre ele.
            
            **2ª Lei (Força e Aceleração):**
            $$
            \\vec{F} = m \\cdot \\vec{a}
            $$
            
            **3ª Lei (Ação e Reação):**
            > Para toda ação, existe uma reação igual e oposta.
            
            **Energia:**
            
            **Energia Cinética:**
            $$
            E_c = \\frac{1}{2} m v^2
            $$
            
            **Energia Potencial Gravitacional:**
            $$
            E_p = m g h
            $$
            
            **Conservação de Energia:**
            $$
            E_{total} = E_c + E_p = \\text{constante}
            $$
            
            **Aplicações:**
            - Análise de estruturas
            - Dinâmica de sistemas
            - Projeto de fundações
            """)

def show_calculadora_vetores():
    """Calculadora de operações com vetores 3D"""
    st.subheader("🔷 Visualizador e Calculadora de Vetores 3D")
    
    st.markdown("""
    ### 🎯 Como Usar
    
    Insira as componentes de dois vetores e visualize as operações vetoriais em 3D.
    """)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("#### Vetor $\\vec{u}$")
        ux = st.number_input("Componente x", value=3.0, key="ux")
        uy = st.number_input("Componente y", value=2.0, key="uy")
        uz = st.number_input("Componente z", value=1.0, key="uz")
        u = np.array([ux, uy, uz])
    
    with col2:
        st.markdown("#### Vetor $\\vec{v}$")
        vx = st.number_input("Componente x", value=1.0, key="vx")
        vy = st.number_input("Componente y", value=2.0, key="vy")
        vz = st.number_input("Componente z", value=3.0, key="vz")
        v = np.array([vx, vy, vz])
    
    st.markdown("---")
    
    # Calcular operações
    modulo_u = np.linalg.norm(u)
    modulo_v = np.linalg.norm(v)
    produto_escalar = np.dot(u, v)
    produto_vetorial = np.cross(u, v)
    soma = u + v
    subtracao = u - v
    
    # Calcular ângulo
    if modulo_u > 0 and modulo_v > 0:
        cos_theta = produto_escalar / (modulo_u * modulo_v)
        theta = np.arccos(np.clip(cos_theta, -1, 1))
        theta_graus = np.degrees(theta)
    else:
        theta_graus = 0
    
    # Exibir resultados
    st.markdown("### 📊 Resultados")
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Módulo de $\\vec{u}$", f"{modulo_u:.3f}")
        st.metric("Módulo de $\\vec{v}$", f"{modulo_v:.3f}")
    with col2:
        st.metric("Produto Escalar", f"{produto_escalar:.3f}")
        st.metric("Ângulo entre vetores", f"{theta_graus:.2f}°")
    with col3:
        st.metric("Módulo do Produto Vetorial", f"{np.linalg.norm(produto_vetorial):.3f}")
    
    st.markdown("---")
    st.markdown("### 🔢 Operações Detalhadas")
    
    col1, col2 = st.columns(2)
    with col1:
        st.markdown(f"""
        **Soma:** $\\vec{u} + \\vec{v}$
        
        $$
        \\vec{{u}} + \\vec{{v}} = ({soma[0]:.2f}, {soma[1]:.2f}, {soma[2]:.2f})
        $$
        
        **Subtração:** $\\vec{u} - \\vec{v}$
        
        $$
        \\vec{{u}} - \\vec{{v}} = ({subtracao[0]:.2f}, {subtracao[1]:.2f}, {subtracao[2]:.2f})
        $$
        """)
    
    with col2:
        st.markdown(f"""
        **Produto Escalar:** $\\vec{{u}} \\cdot \\vec{{v}}$
        
        $$
        \\vec{{u}} \\cdot \\vec{{v}} = {ux} \\times {vx} + {uy} \\times {vy} + {uz} \\times {vz} = {produto_escalar:.3f}
        $$
        
        **Produto Vetorial:** $\\vec{{u}} \\times \\vec{{v}}$
        
        $$
        \\vec{{u}} \\times \\vec{{v}} = ({produto_vetorial[0]:.2f}, {produto_vetorial[1]:.2f}, {produto_vetorial[2]:.2f})
        $$
        """)
    
    # Visualização 3D
    st.markdown("---")
    st.markdown("### 📐 Visualização 3D")
    
    fig = go.Figure()
    
    # Vetor u
    fig.add_trace(go.Scatter3d(
        x=[0, ux], y=[0, uy], z=[0, uz],
        mode='lines+markers+text',
        name='Vetor u',
        line=dict(color='red', width=8),
        marker=dict(size=5),
        text=['', 'u'],
        textposition="top center"
    ))
    
    # Vetor v
    fig.add_trace(go.Scatter3d(
        x=[0, vx], y=[0, vy], z=[0, vz],
        mode='lines+markers+text',
        name='Vetor v',
        line=dict(color='blue', width=8),
        marker=dict(size=5),
        text=['', 'v'],
        textposition="top center"
    ))
    
    # Produto vetorial
    if np.linalg.norm(produto_vetorial) > 0.1:
        fig.add_trace(go.Scatter3d(
            x=[0, produto_vetorial[0]], y=[0, produto_vetorial[1]], z=[0, produto_vetorial[2]],
            mode='lines+markers+text',
            name='u × v',
            line=dict(color='green', width=6, dash='dash'),
            marker=dict(size=5),
            text=['', 'u×v'],
            textposition="top center"
        ))
    
    fig.update_layout(
        title="Visualização 3D dos Vetores",
        scene=dict(
            xaxis_title="X",
            yaxis_title="Y",
            zaxis_title="Z",
            aspectmode='cube'
        ),
        height=600
    )
    
    st.plotly_chart(fig, use_container_width=True)

def show_calculadora_raizes():
    """Calculadora de raízes usando métodos numéricos"""
    st.subheader("🔢 Calculadora de Raízes - Métodos Numéricos")
    
    st.markdown("""
    ### 🎯 Como Usar
    
    Insira uma função e encontre suas raízes usando métodos numéricos.
    """)
    
    metodo = st.selectbox("Método", ["Newton-Raphson", "Bisseção"])
    
    # Input da função
    st.markdown("### 📝 Função")
    st.markdown("""
    **Nota:** Use 'x' como variável. Exemplos:
    - `x**2 - 4` para $x^2 - 4$
    - `x**3 - x - 2` para $x^3 - x - 2$
    - `np.sin(x) - x/2` para $\\sin(x) - x/2$
    """)
    
    funcao_str = st.text_input("f(x) =", value="x**2 - 4")
    
    try:
        # Criar função
        def f(x):
            return eval(funcao_str.replace('x', 'x'))
        
        if metodo == "Newton-Raphson":
            st.markdown("### Método de Newton-Raphson")
            
            x0 = st.number_input("Estimativa inicial x₀", value=2.0)
            tol = st.number_input("Tolerância", value=1e-6, format="%.0e")
            max_iter = st.number_input("Máximo de iterações", value=100, min_value=1)
            
            if st.button("Calcular", type="primary"):
                # Derivada numérica
                h = 1e-8
                def df(x):
                    return (f(x + h) - f(x)) / h
                
                x = x0
                iteracoes = []
                
                for i in range(max_iter):
                    fx = f(x)
                    dfx = df(x)
                    
                    if abs(dfx) < 1e-10:
                        st.error("Derivada muito próxima de zero!")
                        break
                    
                    x_novo = x - fx / dfx
                    erro = abs(x_novo - x)
                    iteracoes.append({'iteracao': i+1, 'x': x, 'f(x)': fx, 'erro': erro})
                    
                    if erro < tol:
                        break
                    x = x_novo
                
                if len(iteracoes) > 0:
                    st.success(f"✅ Raiz encontrada: x = {x:.8f}")
                    st.metric("Número de iterações", len(iteracoes))
                    st.metric("f(x) na raiz", f"{f(x):.2e}")
                    
                    # Tabela de iterações
                    st.markdown("### 📊 Histórico de Iterações")
                    import pandas as pd
                    df_iter = pd.DataFrame(iteracoes)
                    st.dataframe(df_iter, use_container_width=True)
        
        else:  # Bisseção
            st.markdown("### Método da Bisseção")
            
            col1, col2 = st.columns(2)
            with col1:
                a = st.number_input("Limite inferior a", value=0.0)
            with col2:
                b = st.number_input("Limite superior b", value=5.0)
            
            tol = st.number_input("Tolerância", value=1e-6, format="%.0e")
            max_iter = st.number_input("Máximo de iterações", value=100, min_value=1)
            
            if st.button("Calcular", type="primary"):
                if f(a) * f(b) > 0:
                    st.error("❌ Não há mudança de sinal no intervalo! Escolha outro intervalo.")
                else:
                    iteracoes = []
                    for i in range(max_iter):
                        c = (a + b) / 2
                        fc = f(c)
                        erro = (b - a) / 2
                        iteracoes.append({'iteracao': i+1, 'a': a, 'b': b, 'c': c, 'f(c)': fc, 'erro': erro})
                        
                        if abs(fc) < tol or erro < tol:
                            break
                        
                        if f(a) * fc < 0:
                            b = c
                        else:
                            a = c
                    
                    st.success(f"✅ Raiz encontrada: x = {c:.8f}")
                    st.metric("Número de iterações", len(iteracoes))
                    st.metric("f(x) na raiz", f"{f(c):.2e}")
                    
                    # Tabela de iterações
                    st.markdown("### 📊 Histórico de Iterações")
                    import pandas as pd
                    df_iter = pd.DataFrame(iteracoes)
                    st.dataframe(df_iter, use_container_width=True)
                    
                    # Gráfico
                    x_plot = np.linspace(a-1, b+1, 100)
                    y_plot = [f(x) for x in x_plot]
                    
                    fig = go.Figure()
                    fig.add_trace(go.Scatter(x=x_plot, y=y_plot, mode='lines', name='f(x)'))
                    fig.add_hline(y=0, line_dash="dash", line_color="gray")
                    fig.add_vline(x=c, line_dash="dash", line_color="red", annotation_text=f"Raiz: {c:.4f}")
                    fig.update_layout(title="Gráfico da Função", xaxis_title="x", yaxis_title="f(x)", height=400)
                    st.plotly_chart(fig, use_container_width=True)
    
    except Exception as e:
        st.error(f"Erro ao processar função: {str(e)}")
        st.info("Certifique-se de usar a sintaxe correta. Exemplo: 'x**2 - 4'")

def show_conversor_unidades():
    """Conversor de unidades de engenharia"""
    st.subheader("🔄 Conversor de Unidades de Engenharia")
    
    tipo = st.selectbox("Tipo de Grandeza", [
        "Pressão",
        "Viscosidade",
        "Tensão",
        "Força",
        "Comprimento",
        "Momento/Torque"
    ])
    
    col1, col2, col3 = st.columns(3)
    
    conversoes = {
        "Pressão": {
            "Pa": 1,
            "kPa": 1000,
            "MPa": 1e6,
            "bar": 100000,
            "psi": 6894.76,
            "ksi": 6894760
        },
        "Viscosidade": {
            "Pa.s": 1,
            "cP": 0.001,
            "poise": 0.1
        },
        "Tensão": {
            "Pa": 1,
            "MPa": 1e6,
            "GPa": 1e9,
            "psi": 6894.76,
            "ksi": 6894760
        },
        "Força": {
            "N": 1,
            "kN": 1000,
            "lbf": 4.44822,
            "kgf": 9.80665
        },
        "Comprimento": {
            "m": 1,
            "mm": 0.001,
            "cm": 0.01,
            "ft": 0.3048,
            "in": 0.0254
        },
        "Momento/Torque": {
            "N.m": 1,
            "kN.m": 1000,
            "lbf.ft": 1.35582,
            "kgf.m": 9.80665
        }
    }
    
    unidades = list(conversoes[tipo].keys())
    
    with col1:
        valor = st.number_input("Valor", value=1.0)
        unidade_origem = st.selectbox("De", unidades, key="origem")
    
    with col2:
        st.markdown("<br>", unsafe_allow_html=True)
        st.markdown("### →")
    
    with col3:
        unidade_destino = st.selectbox("Para", unidades, key="destino")
        
        # Converter
        valor_si = valor * conversoes[tipo][unidade_origem]
        valor_convertido = valor_si / conversoes[tipo][unidade_destino]
        
        st.metric("Resultado", f"{valor_convertido:.6f} {unidade_destino}")
    
    # Tabela de conversões
    st.markdown("---")
    st.markdown("### 📊 Tabela de Conversões")
    
    import pandas as pd
    tabela = []
    for unid in unidades:
        fator = conversoes[tipo][unid]
        tabela.append({
            "Unidade": unid,
            f"Fator para {unidades[0]}": f"{fator:.6e}" if fator < 1 else f"{fator:.6f}"
        })
    
    df = pd.DataFrame(tabela)
    st.dataframe(df, use_container_width=True)

def show_demonstracoes_operacoes():
    """Seção de demonstrações interativas de operações básicas"""
    st.subheader("🔬 Demonstrações Interativas - Operações Básicas")
    
    st.markdown("""
    ## 🎯 Demonstrações Práticas
    
    Esta seção apresenta demonstrações interativas das operações matemáticas e físicas fundamentais.
    """)
    
    demo_tipo = st.selectbox("Selecione a Demonstração:", [
        "Trigonometria - Componentes de Força",
        "Álgebra - Sistema de Equações",
        "Cálculo - Derivadas e Integrais",
        "Física - Equilíbrio de Forças",
        "Geometria - Áreas e Volumes"
    ])
    
    if demo_tipo == "Trigonometria - Componentes de Força":
        st.markdown("### 📐 Decomposição de Força em Componentes")
        
        F = st.slider("Magnitude da Força F (N)", 10.0, 100.0, 50.0)
        theta = st.slider("Ângulo θ (graus)", 0.0, 90.0, 45.0)
        theta_rad = np.radians(theta)
        
        Fx = F * np.cos(theta_rad)
        Fy = F * np.sin(theta_rad)
        
        col1, col2 = st.columns(2)
        with col1:
            st.metric("Componente Horizontal Fx", f"{Fx:.2f} N")
            st.latex(f"F_x = F \\cos(\\theta) = {F:.1f} \\times \\cos({theta:.1f}°) = {Fx:.2f} \\text{{ N}}")
        with col2:
            st.metric("Componente Vertical Fy", f"{Fy:.2f} N")
            st.latex(f"F_y = F \\sin(\\theta) = {F:.1f} \\times \\sin({theta:.1f}°) = {Fy:.2f} \\text{{ N}}")
        
        # Verificação
        F_calc = np.sqrt(Fx**2 + Fy**2)
        st.info(f"✅ Verificação: $F = \\sqrt{{F_x^2 + F_y^2}} = \\sqrt{{{Fx:.2f}^2 + {Fy:.2f}^2}} = {F_calc:.2f}$ N")
        
        # Gráfico
        fig = go.Figure()
        fig.add_trace(go.Scatter(
            x=[0, Fx], y=[0, Fy],
            mode='lines+markers+text',
            name='Força F',
            line=dict(color='red', width=4),
            marker=dict(size=10),
            text=['', f'F = {F:.1f} N'],
            textposition="top center"
        ))
        fig.add_trace(go.Scatter(
            x=[0, Fx], y=[0, 0],
            mode='lines+markers',
            name='Fx',
            line=dict(color='blue', width=2, dash='dash'),
            marker=dict(size=5)
        ))
        fig.add_trace(go.Scatter(
            x=[Fx, Fx], y=[0, Fy],
            mode='lines+markers',
            name='Fy',
            line=dict(color='green', width=2, dash='dash'),
            marker=dict(size=5)
        ))
        fig.update_layout(
            title="Decomposição de Força",
            xaxis_title="Fx (N)",
            yaxis_title="Fy (N)",
            height=500,
            xaxis=dict(scaleanchor="y", scaleratio=1)
        )
        st.plotly_chart(fig, use_container_width=True)
    
    elif demo_tipo == "Álgebra - Sistema de Equações":
        st.markdown("### 🔢 Resolução de Sistema Linear 2x2")
        
        st.markdown("""
        Resolva o sistema:
        $$
        \\begin{cases}
        a_1 x + b_1 y = c_1 \\\\
        a_2 x + b_2 y = c_2
        \\end{cases}
        $$
        """)
        
        col1, col2 = st.columns(2)
        with col1:
            a1 = st.number_input("a₁", value=2.0, key="a1")
            b1 = st.number_input("b₁", value=3.0, key="b1")
            c1 = st.number_input("c₁", value=8.0, key="c1")
        with col2:
            a2 = st.number_input("a₂", value=1.0, key="a2")
            b2 = st.number_input("b₂", value=-1.0, key="b2")
            c2 = st.number_input("c₂", value=1.0, key="c2")
        
        if st.button("Resolver", type="primary"):
            # Regra de Cramer
            det = a1 * b2 - a2 * b1
            
            if abs(det) < 1e-10:
                st.error("❌ Sistema indeterminado ou impossível! Determinante = 0")
            else:
                det_x = c1 * b2 - c2 * b1
                det_y = a1 * c2 - a2 * c1
                
                x = det_x / det
                y = det_y / det
                
                st.success(f"✅ Solução: x = {x:.4f}, y = {y:.4f}")
                
                st.markdown(f"""
                **Cálculo:**
                
                Determinante: $\\Delta = {a1} \\times {b2} - {a2} \\times {b1} = {det}$
                
                $$
                x = \\frac{{\\Delta_x}}{{\\Delta}} = \\frac{{{det_x}}}{{{det}}} = {x:.4f}
                $$
                
                $$
                y = \\frac{{\\Delta_y}}{{\\Delta}} = \\frac{{{det_y}}}{{{det}}} = {y:.4f}
                $$
                
                **Verificação:**
                - Equação 1: ${a1} \\times {x:.4f} + {b1} \\times {y:.4f} = {a1*x + b1*y:.4f}$ ✓
                - Equação 2: ${a2} \\times {x:.4f} + {b2} \\times {y:.4f} = {a2*x + b2*y:.4f}$ ✓
                """)
    
    elif demo_tipo == "Cálculo - Derivadas e Integrais":
        st.markdown("### 📈 Cálculo Diferencial e Integral")
        
        funcao_tipo = st.selectbox("Função", [
            "Polinômio: f(x) = x²",
            "Polinômio: f(x) = x³ - 2x",
            "Trigonométrica: f(x) = sin(x)",
            "Exponencial: f(x) = e^x"
        ])
        
        funcoes = {
            "Polinômio: f(x) = x²": (lambda x: x**2, lambda x: 2*x, lambda x: x**3/3),
            "Polinômio: f(x) = x³ - 2x": (lambda x: x**3 - 2*x, lambda x: 3*x**2 - 2, lambda x: x**4/4 - x**2),
            "Trigonométrica: f(x) = sin(x)": (lambda x: np.sin(x), lambda x: np.cos(x), lambda x: -np.cos(x)),
            "Exponencial: f(x) = e^x": (lambda x: np.exp(x), lambda x: np.exp(x), lambda x: np.exp(x))
        }
        
        f, df, F = funcoes[funcao_tipo]
        
        x_range = st.slider("Range de x", -5.0, 5.0, (-3.0, 3.0))
        x_plot = np.linspace(x_range[0], x_range[1], 100)
        
        fig = make_subplots(rows=3, cols=1, subplot_titles=("Função f(x)", "Derivada f'(x)", "Integral F(x)"))
        
        fig.add_trace(go.Scatter(x=x_plot, y=[f(x) for x in x_plot], name='f(x)', line=dict(color='blue')), row=1, col=1)
        fig.add_trace(go.Scatter(x=x_plot, y=[df(x) for x in x_plot], name="f'(x)", line=dict(color='red')), row=2, col=1)
        fig.add_trace(go.Scatter(x=x_plot, y=[F(x) for x in x_plot], name='F(x)', line=dict(color='green')), row=3, col=1)
        
        fig.update_layout(height=800, title_text="Função, Derivada e Integral")
        st.plotly_chart(fig, use_container_width=True)
        
        st.markdown("""
        **Relações:**
        - A **derivada** mostra a taxa de variação da função
        - A **integral** mostra a área sob a curva
        - $\\frac{d}{dx}[F(x)] = f(x)$ (Teorema Fundamental do Cálculo)
        """)
    
    elif demo_tipo == "Física - Equilíbrio de Forças":
        st.markdown("### ⚖️ Equilíbrio de Forças no Plano")
        
        st.markdown("""
        Demonstração do equilíbrio de forças em um ponto:
        $$
        \\sum F_x = 0 \\quad \\text{e} \\quad \\sum F_y = 0
        $$
        """)
        
        col1, col2, col3 = st.columns(3)
        with col1:
            st.markdown("**Força F₁**")
            F1 = st.number_input("Magnitude (N)", value=50.0, key="F1")
            theta1 = st.number_input("Ângulo (graus)", value=0.0, key="theta1")
        with col2:
            st.markdown("**Força F₂**")
            F2 = st.number_input("Magnitude (N)", value=50.0, key="F2")
            theta2 = st.number_input("Ângulo (graus)", value=120.0, key="theta2")
        with col3:
            st.markdown("**Força F₃**")
            F3 = st.number_input("Magnitude (N)", value=50.0, key="F3")
            theta3 = st.number_input("Ângulo (graus)", value=240.0, key="theta3")
        
        if st.button("Calcular Equilíbrio", type="primary"):
            # Componentes
            F1x = F1 * np.cos(np.radians(theta1))
            F1y = F1 * np.sin(np.radians(theta1))
            F2x = F2 * np.cos(np.radians(theta2))
            F2y = F2 * np.sin(np.radians(theta2))
            F3x = F3 * np.cos(np.radians(theta3))
            F3y = F3 * np.sin(np.radians(theta3))
            
            soma_x = F1x + F2x + F3x
            soma_y = F1y + F2y + F3y
            resultante = np.sqrt(soma_x**2 + soma_y**2)
            
            col1, col2 = st.columns(2)
            with col1:
                st.metric("ΣFx", f"{soma_x:.2f} N")
            with col2:
                st.metric("ΣFy", f"{soma_y:.2f} N")
            
            if resultante < 0.01:
                st.success("✅ Sistema em EQUILÍBRIO!")
            else:
                st.warning(f"⚠️ Sistema NÃO está em equilíbrio. Resultante = {resultante:.2f} N")
    
    elif demo_tipo == "Geometria - Áreas e Volumes":
        st.markdown("### 📐 Cálculo de Áreas e Volumes")
        
        forma = st.selectbox("Forma Geométrica", [
            "Retângulo",
            "Círculo",
            "Triângulo",
            "Cilindro",
            "Esfera"
        ])
        
        if forma == "Retângulo":
            b = st.number_input("Base (m)", value=5.0)
            h = st.number_input("Altura (m)", value=3.0)
            area = b * h
            st.metric("Área", f"{area:.2f} m²")
            st.latex(f"A = b \\times h = {b} \\times {h} = {area} \\text{{ m}}^2")
        
        elif forma == "Círculo":
            r = st.number_input("Raio (m)", value=2.0)
            area = np.pi * r**2
            st.metric("Área", f"{area:.2f} m²")
            st.latex(f"A = \\pi r^2 = \\pi \\times {r}^2 = {area:.2f} \\text{{ m}}^2")
        
        elif forma == "Triângulo":
            b = st.number_input("Base (m)", value=4.0)
            h = st.number_input("Altura (m)", value=3.0)
            area = 0.5 * b * h
            st.metric("Área", f"{area:.2f} m²")
            st.latex(f"A = \\frac{{1}}{{2}} b h = \\frac{{1}}{{2}} \\times {b} \\times {h} = {area} \\text{{ m}}^2")
        
        elif forma == "Cilindro":
            r = st.number_input("Raio (m)", value=1.0)
            h = st.number_input("Altura (m)", value=5.0)
            volume = np.pi * r**2 * h
            area_lateral = 2 * np.pi * r * h
            area_total = 2 * np.pi * r**2 + area_lateral
            st.metric("Volume", f"{volume:.2f} m³")
            st.metric("Área Total", f"{area_total:.2f} m²")
        
        elif forma == "Esfera":
            r = st.number_input("Raio (m)", value=2.0)
            volume = (4/3) * np.pi * r**3
            area = 4 * np.pi * r**2
            st.metric("Volume", f"{volume:.2f} m³")
            st.metric("Área", f"{area:.2f} m²")

def show():
    """Função principal do módulo de Fundamentos"""
    st.title("📐 Módulo de Fundamentos")
    st.markdown("---")
    
    tab_teoria, tab_calc, tab_demo = st.tabs(["📖 Teoria", "🧮 Calculadoras", "🔬 Demonstrações"])
    
    with tab_teoria:
        show_teoria()
    
    with tab_calc:
        calc_tab = st.radio(
            "Selecione a Calculadora:",
            ["Vetores 3D", "Raízes (Métodos Numéricos)", "Conversor de Unidades"],
            horizontal=True
        )
        
        st.markdown("---")
        
        if calc_tab == "Vetores 3D":
            show_calculadora_vetores()
        elif calc_tab == "Raízes (Métodos Numéricos)":
            show_calculadora_raizes()
        elif calc_tab == "Conversor de Unidades":
            show_conversor_unidades()
    
    with tab_demo:
        show_demonstracoes_operacoes()
