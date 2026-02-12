"""
Utilitários para plotagem e visualização
"""

import plotly.graph_objects as go
import numpy as np

def plot_diagrama_cortante_momento(x, cortante, momento, reacoes=None, cargas_pontuais=None, cargas_distribuidas=None, comprimento=None):
    """
    Plota os diagramas de cortante e momento fletor com visualização da viga
    
    Parameters:
    -----------
    x : array
        Posições ao longo da viga
    cortante : array
        Valores de cortante
    momento : array
        Valores de momento fletor
    reacoes : dict, optional
        Dicionário com reações de apoio {'Va': float, 'Vb': float}
    cargas_pontuais : list, optional
        Lista de cargas pontuais para visualização
    cargas_distribuidas : list, optional
        Lista de cargas distribuídas para visualização
    comprimento : float, optional
        Comprimento da viga
    """
    fig = go.Figure()
    
    # Preencher área positiva e negativa
    fig.add_trace(go.Scatter(
        x=x,
        y=cortante,
        mode='lines',
        name='Cortante (V)',
        line=dict(color='red', width=3),
        fill='tozeroy',
        fillcolor='rgba(255,0,0,0.1)',
        hovertemplate='x: %{x:.2f} m<br>V: %{y:.2f} kN<extra></extra>'
    ))
    
    # Linha zero para cortante
    fig.add_hline(y=0, line_dash="dash", line_color="gray", opacity=0.5, annotation_text="Linha Zero")
    
    # Marcar pontos de máximo e mínimo
    idx_max = np.argmax(cortante)
    idx_min = np.argmin(cortante)
    fig.add_trace(go.Scatter(
        x=[x[idx_max], x[idx_min]],
        y=[cortante[idx_max], cortante[idx_min]],
        mode='markers',
        name='Extremos',
        marker=dict(size=10, color='darkred', symbol='diamond'),
        hovertemplate='x: %{x:.2f} m<br>V: %{y:.2f} kN<extra></extra>'
    ))
    
    fig.update_layout(
        title="📊 Diagrama de Esforço Cortante (DEC)",
        xaxis_title="Posição ao longo da viga (m)",
        yaxis_title="Esforço Cortante V (kN)",
        hovermode='x unified',
        height=450,
        showlegend=True,
        template='plotly_white'
    )
    
    fig2 = go.Figure()
    
    # Preencher área do momento
    fig2.add_trace(go.Scatter(
        x=x,
        y=momento,
        mode='lines',
        name='Momento (M)',
        line=dict(color='blue', width=3),
        fill='tozeroy',
        fillcolor='rgba(0,0,255,0.1)',
        hovertemplate='x: %{x:.2f} m<br>M: %{y:.2f} kN.m<extra></extra>'
    ))
    
    # Linha zero para momento
    fig2.add_hline(y=0, line_dash="dash", line_color="gray", opacity=0.5, annotation_text="Linha Zero")
    
    # Marcar ponto de máximo momento
    idx_max_m = np.argmax(np.abs(momento))
    fig2.add_trace(go.Scatter(
        x=[x[idx_max_m]],
        y=[momento[idx_max_m]],
        mode='markers',
        name='Momento Máximo',
        marker=dict(size=12, color='darkblue', symbol='star'),
        hovertemplate='x: %{x:.2f} m<br>M: %{y:.2f} kN.m<extra></extra>'
    ))
    
    fig2.update_layout(
        title="📊 Diagrama de Momento Fletor (DMF)",
        xaxis_title="Posição ao longo da viga (m)",
        yaxis_title="Momento Fletor M (kN.m)",
        hovermode='x unified',
        height=450,
        showlegend=True,
        template='plotly_white'
    )
    
    return fig, fig2

def plot_viga_esquema(comprimento, cargas_pontuais=None, cargas_distribuidas=None, reacoes=None):
    """
    Plota um esquema visual da viga com cargas e reações
    """
    fig = go.Figure()
    
    # Desenhar a viga (linha horizontal)
    fig.add_trace(go.Scatter(
        x=[0, comprimento],
        y=[0, 0],
        mode='lines',
        name='Viga',
        line=dict(color='black', width=4)
    ))
    
    # Apoios
    fig.add_trace(go.Scatter(
        x=[0, comprimento],
        y=[0, 0],
        mode='markers',
        name='Apoios',
        marker=dict(size=15, color='gray', symbol='square'),
        hovertemplate='Apoio<extra></extra>'
    ))
    
    # Cargas pontuais
    if cargas_pontuais:
        for carga in cargas_pontuais:
            fig.add_trace(go.Scatter(
                x=[carga['posicao'], carga['posicao']],
                y=[0, -0.3],
                mode='lines+markers',
                name=f"Carga {carga['valor']} kN",
                line=dict(color='red', width=3),
                marker=dict(size=10, color='red', symbol='arrow-down'),
                hovertemplate=f"P = {carga['valor']:.1f} kN<br>x = {carga['posicao']:.2f} m<extra></extra>"
            ))
    
    # Cargas distribuídas
    if cargas_distribuidas:
        for carga in cargas_distribuidas:
            x_carga = np.linspace(carga['inicio'], carga['fim'], 20)
            y_carga = -0.1 * (x_carga - carga['inicio']) / (carga['fim'] - carga['inicio'] + 1e-6)
            fig.add_trace(go.Scatter(
                x=x_carga,
                y=y_carga,
                mode='lines',
                name=f"q = {carga['valor']} kN/m",
                line=dict(color='orange', width=2),
                fill='tozeroy',
                fillcolor='rgba(255,165,0,0.2)',
                hovertemplate=f"q = {carga['valor']:.1f} kN/m<extra></extra>"
            ))
    
    # Reações
    if reacoes:
        fig.add_trace(go.Scatter(
            x=[0],
            y=[0.3],
            mode='markers+text',
            name='Va',
            marker=dict(size=12, color='green', symbol='triangle-up'),
            text=[f"Va = {reacoes['Va']:.1f} kN"],
            textposition="top center",
            hovertemplate=f"Va = {reacoes['Va']:.2f} kN<extra></extra>"
        ))
        fig.add_trace(go.Scatter(
            x=[comprimento],
            y=[0.3],
            mode='markers+text',
            name='Vb',
            marker=dict(size=12, color='green', symbol='triangle-up'),
            text=[f"Vb = {reacoes['Vb']:.1f} kN"],
            textposition="top center",
            hovertemplate=f"Vb = {reacoes['Vb']:.2f} kN<extra></extra>"
        ))
    
    fig.update_layout(
        title="📐 Esquema da Viga",
        xaxis_title="Posição (m)",
        yaxis_title="",
        height=300,
        showlegend=True,
        yaxis=dict(range=[-0.5, 0.5], showgrid=False, zeroline=False, showticklabels=False),
        xaxis=dict(range=[-0.5, comprimento + 0.5]),
        template='plotly_white'
    )
    
    return fig

def plot_circulo_mohr(sigma_x, sigma_y, tau_xy):
    """
    Plota o círculo de Mohr para tensões
    
    Parameters:
    -----------
    sigma_x : float
        Tensão normal em x
    sigma_y : float
        Tensão normal em y
    tau_xy : float
        Tensão de cisalhamento
    """
    # Centro e raio do círculo
    centro = (sigma_x + sigma_y) / 2
    raio = np.sqrt(((sigma_x - sigma_y) / 2)**2 + tau_xy**2)
    
    # Tensões principais
    sigma_1 = centro + raio
    sigma_2 = centro - raio
    
    # Ângulo do plano principal
    theta_p = 0.5 * np.arctan2(2 * tau_xy, sigma_x - sigma_y)
    
    # Gerar pontos do círculo
    theta = np.linspace(0, 2 * np.pi, 100)
    sigma_circle = centro + raio * np.cos(theta)
    tau_circle = raio * np.sin(theta)
    
    fig = go.Figure()
    
    # Círculo de Mohr
    fig.add_trace(go.Scatter(
        x=sigma_circle,
        y=tau_circle,
        mode='lines',
        name='Círculo de Mohr',
        line=dict(color='blue', width=2),
        fill='toself',
        fillcolor='rgba(0,0,255,0.1)'
    ))
    
    # Tensões principais
    fig.add_trace(go.Scatter(
        x=[sigma_1, sigma_2],
        y=[0, 0],
        mode='markers',
        name='Tensões Principais',
        marker=dict(size=12, color='red', symbol='diamond'),
        hovertemplate='σ: %{x:.2f} kPa<br>τ: %{y:.2f} kPa<extra></extra>'
    ))
    
    # Estado de tensão inicial
    fig.add_trace(go.Scatter(
        x=[sigma_x],
        y=[tau_xy],
        mode='markers',
        name='Estado de Tensão',
        marker=dict(size=10, color='green', symbol='circle'),
        hovertemplate='σ: %{x:.2f} kPa<br>τ: %{y:.2f} kPa<extra></extra>'
    ))
    
    # Centro do círculo
    fig.add_trace(go.Scatter(
        x=[centro],
        y=[0],
        mode='markers',
        name='Centro',
        marker=dict(size=8, color='orange', symbol='x'),
        hovertemplate='Centro: %{x:.2f} kPa<extra></extra>'
    ))
    
    fig.update_layout(
        title="Círculo de Mohr",
        xaxis_title="Tensão Normal σ (kPa)",
        yaxis_title="Tensão de Cisalhamento τ (kPa)",
        hovermode='closest',
        height=500,
        xaxis=dict(scaleanchor="y", scaleratio=1)
    )
    
    return fig, sigma_1, sigma_2, theta_p

