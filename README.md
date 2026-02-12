# 🏗️ ATLAS - Suíte de Engenharia Civil Integrada

Aplicação web (Single Page Application) desenvolvida em Streamlit para acompanhar estudantes durante todo o curso de Engenharia Civil, com módulos para cada grande disciplina técnica.

## 📋 Características

- **Interface Moderna:** Navegação lateral intuitiva com Streamlit
- **Módulos por Domínio:** Organização por áreas de conhecimento, não apenas períodos
- **Teoria + Prática:** Cada módulo possui abas de teoria (com fórmulas LaTeX) e calculadoras
- **Visualizações Interativas:** Gráficos Plotly para análise de resultados
- **Arquitetura Modular:** Estrutura de pastas preparada para escalabilidade

## 🚀 Instalação

### Pré-requisitos

- Python 3.10 ou superior
- pip (gerenciador de pacotes Python)

### Passos

#### Opção 1: Script Automático (Recomendado)

1. Navegue até o diretório do projeto:
   ```bash
   cd atlas
   ```

2. Execute o script de setup:
   ```bash
   ./setup.sh
   ```

3. Ative o ambiente virtual e execute:
   ```bash
   source venv/bin/activate
   streamlit run app.py
   ```

#### Opção 2: Manual

1. Navegue até o diretório do projeto:
   ```bash
   cd atlas
   ```

2. **Crie e ative um ambiente virtual** (recomendado para evitar conflitos):
   ```bash
   # Criar ambiente virtual
   python3 -m venv venv
   
   # Ativar ambiente virtual
   # No Linux/Mac:
   source venv/bin/activate
   # No Windows:
   # venv\Scripts\activate
   ```

4. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

5. Execute a aplicação:
   ```bash
   streamlit run app.py
   ```

6. A aplicação abrirá automaticamente no navegador em `http://localhost:8501`

### ⚠️ Nota sobre Ambientes Gerenciados

Se você encontrar o erro `externally-managed-environment`, isso significa que seu sistema Python está protegido. **Sempre use um ambiente virtual** para este projeto. O ambiente virtual já foi criado na pasta `venv/`.

**Para usar o ambiente virtual:**
```bash
# Ativar (Linux/Mac)
source venv/bin/activate

# Ativar (Windows)
venv\Scripts\activate

# Desativar (quando terminar)
deactivate
```

## 📚 Módulos Disponíveis

### ✅ Implementados

#### 🏛️ Estruturas
- **Calculadora de Vigas Isostáticas:** Cálculo de reações de apoio e diagramas de esforço cortante (DEC) e momento fletor (DMF)
- **Propriedades Geométricas:** Cálculo de centroide e momento de inércia para seções retangulares, T e I
- **Dimensionamento de Concreto:** Dimensionamento básico de concreto armado (armadura simples) com verificação de domínio

#### 💧 Fluidos & Hidráulica
- **Reynolds & Regime:** Cálculo do número de Reynolds e classificação do regime de escoamento
- **Darcy-Weisbach:** Cálculo de perda de carga distribuída com fator de atrito (Colebrook-White ou Haaland)
- **Manning:** Dimensionamento de canais abertos usando a equação de Manning

### 🚧 Em Desenvolvimento

#### 📐 Fundamentos (Ciclo Básico)
- Visualizador Vetorial 3D
- Calculadora de Raízes (Newton-Raphson e Bisseção)
- Conversor de Unidades de Engenharia

#### 🌍 Geotecnia
- Círculo de Mohr de Tensões ✅ (implementado)
- Classificação de Solos (SUCS/HRB)
- Capacidade de Carga (Terzaghi)

#### 🛣️ Transportes & Topografia
- Curvas Horizontais
- Poligonal Topográfica

## 📁 Estrutura do Projeto

```
atlas/
├── app.py                 # Aplicação principal
├── requirements.txt       # Dependências Python
├── README.md             # Este arquivo
├── setup.sh              # Script de instalação automática
├── .gitignore           # Arquivos a ignorar no Git
├── venv/                # Ambiente virtual (criado automaticamente)
├── modules/             # Módulos da aplicação
│   ├── __init__.py
│   ├── fundamentos.py   # Módulo de Fundamentos
│   ├── estruturas.py    # Módulo de Estruturas (completo)
│   ├── fluidos.py       # Módulo de Fluidos (completo)
│   ├── geotecnia.py     # Módulo de Geotecnia
│   └── transportes.py   # Módulo de Transportes
└── utils/               # Utilitários compartilhados
    ├── __init__.py
    ├── calculations.py  # Funções de cálculo
    └── plotting.py      # Funções de plotagem
```

## 🛠️ Tech Stack

- **Core:** Python 3.10+
- **Frontend:** Streamlit (multipage apps pattern)
- **Math:** NumPy, SciPy, Pandas
- **Visualização:** Plotly (interativo), Matplotlib
- **Fórmulas:** LaTeX (renderizado pelo Streamlit)

## 📖 Como Usar

1. **Navegação:** Use a barra lateral para selecionar o módulo desejado
2. **Teoria:** Cada módulo possui uma aba "Teoria" com explicações e fórmulas em LaTeX
3. **Calculadoras:** Na aba "Calculadoras", selecione a ferramenta desejada e preencha os dados
4. **Resultados:** Os resultados são exibidos com métricas e gráficos interativos

## 🎯 Exemplos de Uso

### Exemplo 1: Análise de Viga
1. Navegue até **Estruturas** → **Calculadoras** → **Vigas Isostáticas**
2. Defina o comprimento da viga
3. Adicione cargas pontuais e/ou distribuídas
4. Clique em "Calcular" para ver reações, diagramas DEC/DMF e valores máximos

### Exemplo 2: Dimensionamento de Canal
1. Navegue até **Fluidos & Hidráulica** → **Calculadoras** → **Manning**
2. Defina largura, declividade e coeficiente de Manning
3. Informe a vazão desejada
4. O sistema calcula a altura da lâmina d'água necessária

## 🔧 Desenvolvimento

Para adicionar novos módulos ou funcionalidades:

1. Crie um novo arquivo em `modules/` seguindo o padrão dos existentes
2. Implemente a função `show()` que será chamada pelo `app.py`
3. Adicione o roteamento no `app.py` se necessário
4. Use as funções em `utils/` para cálculos e plotagens compartilhadas

## 📝 Licença

Este projeto é desenvolvido para fins educacionais.

## 👨‍💻 Autor

Desenvolvido para estudantes de Engenharia Civil.

---

**Versão:** 1.0  
**Última Atualização:** 2024

