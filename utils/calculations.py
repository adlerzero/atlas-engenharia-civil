"""
Funções de cálculo compartilhadas
"""

import numpy as np
from scipy.optimize import fsolve, brentq

def calcular_reacoes_viga_simples(comprimento, cargas_pontuais, cargas_distribuidas):
    """
    Calcula reações de apoio para viga simplesmente apoiada
    
    Parameters:
    -----------
    comprimento : float
        Comprimento da viga (m)
    cargas_pontuais : list of dict
        [{'posicao': float, 'valor': float}, ...]
    cargas_distribuidas : list of dict
        [{'inicio': float, 'fim': float, 'valor': float}, ...]
    
    Returns:
    --------
    dict : {'Va': float, 'Vb': float}
    """
    # Somatório de forças verticais
    soma_forcas = 0
    
    # Forças pontuais
    for carga in cargas_pontuais:
        soma_forcas += carga['valor']
    
    # Forças distribuídas
    for carga in cargas_distribuidas:
        intensidade = carga['valor'] * (carga['fim'] - carga['inicio'])
        soma_forcas += intensidade
    
    # Somatório de momentos em relação ao ponto A
    soma_momentos = 0
    
    # Momentos das cargas pontuais
    for carga in cargas_pontuais:
        soma_momentos += carga['valor'] * carga['posicao']
    
    # Momentos das cargas distribuídas
    for carga in cargas_distribuidas:
        centro = (carga['inicio'] + carga['fim']) / 2
        intensidade = carga['valor'] * (carga['fim'] - carga['inicio'])
        soma_momentos += intensidade * centro
    
    # Reação em B
    Vb = soma_momentos / comprimento
    
    # Reação em A
    Va = soma_forcas - Vb
    
    return {'Va': Va, 'Vb': Vb}

def calcular_esforcos_viga(x, comprimento, cargas_pontuais, cargas_distribuidas, reacoes):
    """
    Calcula esforços cortantes e momentos fletores ao longo da viga
    
    Parameters:
    -----------
    x : array
        Posições para calcular
    comprimento : float
        Comprimento da viga
    cargas_pontuais : list of dict
    cargas_distribuidas : list of dict
    reacoes : dict
        {'Va': float, 'Vb': float}
    
    Returns:
    --------
    cortante : array
    momento : array
    """
    cortante = np.zeros_like(x)
    momento = np.zeros_like(x)
    
    # Contribuição da reação em A
    cortante += reacoes['Va']
    momento += reacoes['Va'] * x
    
    # Contribuição das cargas pontuais
    for carga in cargas_pontuais:
        mask = x >= carga['posicao']
        cortante[mask] -= carga['valor']
        momento[mask] -= carga['valor'] * (x[mask] - carga['posicao'])
    
    # Contribuição das cargas distribuídas
    for carga in cargas_distribuidas:
        mask_inicio = x >= carga['inicio']
        mask_fim = x >= carga['fim']
        
        # Entre início e fim
        mask_meio = mask_inicio & ~mask_fim
        cortante[mask_meio] -= carga['valor'] * (x[mask_meio] - carga['inicio'])
        momento[mask_meio] -= carga['valor'] * (x[mask_meio] - carga['inicio'])**2 / 2
        
        # Após o fim
        intensidade = carga['valor'] * (carga['fim'] - carga['inicio'])
        cortante[mask_fim] -= intensidade
        momento[mask_fim] -= intensidade * (x[mask_fim] - carga['fim']) + \
                            carga['valor'] * (carga['fim'] - carga['inicio'])**2 / 2
    
    return cortante, momento

def calcular_propriedades_geometricas(tipo_secao, dimensoes):
    """
    Calcula centroide e momento de inércia para seções comuns
    
    Parameters:
    -----------
    tipo_secao : str
        'retangulo', 't', 'i'
    dimensoes : dict
        Depende do tipo de seção
    
    Returns:
    --------
    dict : {'centroide_y': float, 'Ix': float, 'Iy': float, 'area': float}
    """
    if tipo_secao == 'retangulo':
        b = dimensoes['largura']
        h = dimensoes['altura']
        area = b * h
        centroide_y = h / 2
        Ix = b * h**3 / 12
        Iy = h * b**3 / 12
        
    elif tipo_secao == 't':
        bf = dimensoes['largura_mesa']
        tf = dimensoes['espessura_mesa']
        hw = dimensoes['altura_alma']
        tw = dimensoes['espessura_alma']
        
        # Áreas
        area_mesa = bf * tf
        area_alma = hw * tw
        area = area_mesa + area_alma
        
        # Centroide
        y_mesa = hw + tf / 2
        y_alma = hw / 2
        centroide_y = (area_mesa * y_mesa + area_alma * y_alma) / area
        
        # Momentos de inércia
        Ix_mesa = bf * tf**3 / 12 + area_mesa * (y_mesa - centroide_y)**2
        Ix_alma = tw * hw**3 / 12 + area_alma * (y_alma - centroide_y)**2
        Ix = Ix_mesa + Ix_alma
        
        Iy = tf * bf**3 / 12 + hw * tw**3 / 12
        
    elif tipo_secao == 'i':
        bf = dimensoes['largura_mesa']
        tf = dimensoes['espessura_mesa']
        hw = dimensoes['altura_alma']
        tw = dimensoes['espessura_alma']
        
        # Similar ao T, mas com duas mesas
        area_mesa = 2 * bf * tf
        area_alma = hw * tw
        area = area_mesa + area_alma
        
        centroide_y = (hw + 2 * tf) / 2  # Simétrico
        
        Ix_mesa = 2 * (bf * tf**3 / 12 + bf * tf * ((hw + tf) / 2)**2)
        Ix_alma = tw * hw**3 / 12
        Ix = Ix_mesa + Ix_alma
        
        Iy = 2 * tf * bf**3 / 12 + hw * tw**3 / 12
    
    else:
        raise ValueError(f"Tipo de seção '{tipo_secao}' não suportado")
    
    return {
        'centroide_y': centroide_y,
        'Ix': Ix,
        'Iy': Iy,
        'area': area
    }

def dimensionar_concreto_armado_simples(Mk, fck, aco_tipo='CA50', bw=0.2, d=None, h=None):
    """
    Dimensionamento básico de concreto armado (armadura simples)
    
    Parameters:
    -----------
    Mk : float
        Momento fletor de cálculo (kN.m)
    fck : float
        Resistência característica do concreto (MPa)
    aco_tipo : str
        Tipo de aço ('CA50' ou 'CA60')
    bw : float
        Largura da seção (m)
    d : float, optional
        Altura útil (m). Se None, calcula a partir de h
    h : float, optional
        Altura total (m). Usado se d não for fornecido
    
    Returns:
    --------
    dict : {'As': float, 'dominio': str, 'x': float, 'd': float}
    """
    # Propriedades do aço
    if aco_tipo == 'CA50':
        fyd = 435e6  # Pa
        Es = 210e9  # Pa
    else:  # CA60
        fyd = 522e6  # Pa
        Es = 210e9  # Pa
    
    # Propriedades do concreto
    fcd = fck * 1e6 / 1.4  # Pa (considerando γc = 1.4)
    epsilon_cu = 0.0035  # Deformação última do concreto
    
    # Altura útil
    if d is None:
        if h is None:
            # Estimativa inicial
            d = 0.9 * 0.5  # 50 cm de altura, 90% útil
        else:
            d = 0.9 * h  # Estimativa conservadora
    else:
        d = d
    
    # Cálculo do momento adimensional
    Md = Mk * 1000  # Converter para N.m
    md = Md / (bw * d**2 * fcd)
    
    # Verificação do domínio
    # Domínio 2: 0 < x/d < 0.259
    # Domínio 3: 0.259 < x/d < 0.628 (para CA50)
    # Domínio 4: x/d > 0.628 (não permitido)
    
    # Resolver para x/d
    # md = 0.68 * (x/d) * (1 - 0.4 * (x/d))
    # Simplificado: assumindo domínio 3
    x_d = 1.25 * (1 - np.sqrt(1 - 2 * md / 0.68))
    
    if x_d < 0.259:
        dominio = "Domínio 2"
    elif x_d < 0.628:
        dominio = "Domínio 3"
    else:
        dominio = "Domínio 4 (não permitido - armadura dupla necessária)"
        x_d = 0.628  # Limite
    
    x = x_d * d
    
    # Área de aço
    As = Md / (fyd * (d - 0.4 * x))
    
    return {
        'As': As * 1e4,  # Converter para cm²
        'dominio': dominio,
        'x': x * 100,  # Converter para cm
        'd': d * 100,  # Converter para cm
        'x_d': x_d
    }

def calcular_reynolds(densidade, velocidade, diametro, viscosidade):
    """
    Calcula número de Reynolds e classifica o regime
    
    Parameters:
    -----------
    densidade : float
        Densidade do fluido (kg/m³)
    velocidade : float
        Velocidade média (m/s)
    diametro : float
        Diâmetro característico (m)
    viscosidade : float
        Viscosidade dinâmica (Pa.s)
    
    Returns:
    --------
    dict : {'Re': float, 'regime': str}
    """
    Re = (densidade * velocidade * diametro) / viscosidade
    
    if Re < 2300:
        regime = "Laminar"
    elif Re < 4000:
        regime = "Transição"
    else:
        regime = "Turbulento"
    
    return {'Re': Re, 'regime': regime}

def calcular_fator_atrito_colebrook(Re, rugosidade_relativa, tol=1e-6, max_iter=100):
    """
    Calcula fator de atrito usando equação de Colebrook-White
    
    Parameters:
    -----------
    Re : float
        Número de Reynolds
    rugosidade_relativa : float
        ε/D (rugosidade absoluta / diâmetro)
    tol : float
        Tolerância para convergência
    max_iter : int
        Número máximo de iterações
    
    Returns:
    --------
    float : Fator de atrito f
    """
    if Re < 2300:
        # Regime laminar
        return 64 / Re
    
    # Estimativa inicial (Swamee-Jain)
    f = 0.25 / (np.log10(rugosidade_relativa / 3.7 + 5.74 / Re**0.9))**2
    
    # Iteração de Colebrook-White
    for _ in range(max_iter):
        f_old = f
        f = 0.25 / (np.log10(rugosidade_relativa / 3.7 + 2.51 / (Re * np.sqrt(f_old))))**2
        
        if abs(f - f_old) < tol:
            break
    
    return f

def calcular_perda_carga_darcy_weisbach(f, comprimento, diametro, velocidade, g=9.81):
    """
    Calcula perda de carga distribuída usando Darcy-Weisbach
    
    Parameters:
    -----------
    f : float
        Fator de atrito
    comprimento : float
        Comprimento do trecho (m)
    diametro : float
        Diâmetro da tubulação (m)
    velocidade : float
        Velocidade média (m/s)
    g : float
        Aceleração da gravidade (m/s²)
    
    Returns:
    --------
    float : Perda de carga (m)
    """
    hf = f * (comprimento / diametro) * (velocidade**2 / (2 * g))
    return hf

def calcular_manning_canal(vazao, declividade, largura, n_manning, altura=None):
    """
    Resolve equação de Manning para canais abertos
    
    Parameters:
    -----------
    vazao : float
        Vazão (m³/s)
    declividade : float
        Declividade do canal (m/m)
    largura : float
        Largura do canal (m)
    n_manning : float
        Coeficiente de Manning
    altura : float, optional
        Se fornecido, calcula vazão. Se None, resolve para altura.
    
    Returns:
    --------
    dict : {'altura': float, 'velocidade': float, 'area': float, 'perimetro': float}
    """
    if altura is None:
        # Resolver para altura
        def equacao_manning(y):
            area = largura * y
            perimetro = largura + 2 * y
            raio_hidraulico = area / perimetro
            vazao_calc = (1 / n_manning) * area * raio_hidraulico**(2/3) * declividade**0.5
            return vazao_calc - vazao
        
        # Método de bisseção
        try:
            altura = brentq(equacao_manning, 0.01, 10.0)
        except:
            altura = None
            return {'altura': None, 'erro': 'Não foi possível resolver'}
    
    area = largura * altura
    perimetro = largura + 2 * altura
    raio_hidraulico = area / perimetro
    velocidade = (1 / n_manning) * raio_hidraulico**(2/3) * declividade**0.5
    
    return {
        'altura': altura,
        'velocidade': velocidade,
        'area': area,
        'perimetro': perimetro,
        'raio_hidraulico': raio_hidraulico
    }

