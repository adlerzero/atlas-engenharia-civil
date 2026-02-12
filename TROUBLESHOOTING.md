# 🔧 Troubleshooting - Erro no Streamlit Cloud

## Erro: "connection refused" no Streamlit Cloud

### Diagnóstico

O erro indica que o Streamlit não consegue inicializar a aplicação. Possíveis causas:

1. **Erro de importação** - Algum módulo não encontrado
2. **Erro silencioso** - Exceção não tratada que impede inicialização
3. **Problema com paths** - Caminhos relativos não funcionam no Cloud

### Soluções

#### 1. Verificar Logs Detalhados

No Streamlit Cloud:
- Vá em "Manage app" → "Logs"
- Procure por erros específicos (Traceback, ImportError, etc.)

#### 2. Testar Localmente

```bash
cd /home/jmek/atlas
source venv/bin/activate
streamlit run app.py
```

Se funcionar localmente, o problema é específico do Cloud.

#### 3. Verificar Dependências

Certifique-se de que `requirements.txt` está completo:

```txt
streamlit>=1.28.0
numpy>=1.24.0
scipy>=1.10.0
pandas>=2.0.0
plotly>=5.14.0
matplotlib>=3.7.0
```

#### 4. Simplificar para Debug

Crie um `app_test.py` simples:

```python
import streamlit as st

st.title("Teste")
st.write("Se isso funcionar, o problema está no app principal")
```

Se funcionar, o problema está nos imports ou na lógica do app principal.

#### 5. Verificar Imports

Todos os módulos devem importar corretamente:

```python
# Teste no terminal
python3 -c "from modules import fundamentos, estruturas, fluidos, geotecnia, transportes; print('OK')"
```

### Próximos Passos

1. ✅ Verificar logs no Streamlit Cloud
2. ✅ Testar localmente
3. ✅ Verificar se todas as dependências estão no requirements.txt
4. ✅ Simplificar app para identificar o problema

### Contato

Se o problema persistir, verifique:
- Logs completos no Streamlit Cloud
- Se há algum erro específico nos módulos
- Se todas as dependências estão instaladas

