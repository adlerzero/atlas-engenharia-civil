# 🚀 Guia Rápido - Como Acessar as Calculadoras

## 📍 Onde estão as Calculadoras?

As calculadoras estão dentro de cada módulo. Siga estes passos:

### 1. **Navegue até um Módulo**
   - Use a barra lateral (sidebar) à esquerda
   - Selecione um módulo, por exemplo: **🏛️ Estruturas**

### 2. **Acesse a Aba "Calculadoras"**
   - No topo da página, você verá duas abas:
     - **📖 Teoria** - Explicações e fórmulas
     - **🧮 Calculadoras** - Ferramentas práticas
   - **Clique na aba "🧮 Calculadoras"**

### 3. **Selecione a Calculadora Desejada**
   - Dentro da aba Calculadoras, há botões de seleção horizontal
   - Por exemplo, no módulo Estruturas:
     - Vigas Isostáticas
     - Propriedades Geométricas
     - Dimensionamento de Concreto

## ✅ Módulos com Calculadoras Funcionais

### 🏛️ Estruturas (COMPLETO)
- ✅ **Vigas Isostáticas**: Cálculo de reações, DEC e DMF
- ✅ **Propriedades Geométricas**: Centroide e momento de inércia
- ✅ **Dimensionamento de Concreto**: Armadura simples

### 💧 Fluidos & Hidráulica (COMPLETO)
- ✅ **Reynolds & Regime**: Classificação do escoamento
- ✅ **Darcy-Weisbach**: Perda de carga
- ✅ **Manning**: Dimensionamento de canais

### 🌍 Geotecnia (PARCIAL)
- ✅ **Círculo de Mohr**: Tensões principais
- 🚧 Classificação de Solos (em desenvolvimento)
- 🚧 Capacidade de Carga (em desenvolvimento)

## 🔧 Se as Páginas Estão Vazias

1. **Limpe o cache do Streamlit:**
   ```bash
   streamlit cache clear
   ```

2. **Reinicie a aplicação:**
   - Pare o servidor (Ctrl+C)
   - Execute novamente: `streamlit run app.py`

3. **Verifique se está usando o ambiente virtual:**
   ```bash
   source venv/bin/activate
   streamlit run app.py
   ```

## 📝 Exemplo de Uso

1. Clique em **🏛️ Estruturas** na sidebar
2. Clique na aba **🧮 Calculadoras** (não em "Teoria")
3. Selecione **Vigas Isostáticas**
4. Preencha os dados (comprimento, cargas, etc.)
5. Clique em **Calcular**
6. Veja os resultados: reações, diagramas DEC/DMF e valores máximos

---

**Dica:** Se você não vê as calculadoras, certifique-se de estar na aba "🧮 Calculadoras" e não na aba "📖 Teoria"!

