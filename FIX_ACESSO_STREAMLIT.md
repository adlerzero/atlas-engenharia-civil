# 🔐 Fix: Problema de Acesso no Streamlit Cloud

## Erro: "You do not have access to this app or it does not exist"

### Diagnóstico

O erro indica que há um problema de **permissões** ou **configuração de conta** no Streamlit Cloud.

**Situação atual:**
- Email: rodrigobrunow.eng.ti@gmail.com
- GitHub: github.com/adlerzero
- Repositório: atlas-engenharia-civil

### Soluções

#### Opção 1: Recriar o App (Recomendado)

1. **Delete o app atual:**
   - Vá em "My apps" no Streamlit Cloud
   - Encontre o app `atlas-engenharia-civil`
   - Clique em "⋮" (três pontos) → "Delete app"
   - Confirme a exclusão

2. **Criar novo app:**
   - Clique em "Create app" (canto superior direito)
   - Preencha:
     - **Repository:** `adlerzero/atlas-engenharia-civil`
     - **Branch:** `main`
     - **Main file path:** `app.py`
     - **App URL:** `atlas-engenharia-civil` (ou outro nome)
   - Clique em "Deploy"

3. **Verificar permissões:**
   - Certifique-se de que está logado com a conta correta do GitHub
   - O repositório deve ser público ou você deve ter acesso

#### Opção 2: Verificar Permissões do Repositório

1. **No GitHub:**
   - Vá para: https://github.com/adlerzero/atlas-engenharia-civil/settings
   - Verifique se o repositório está **público** ou você tem acesso

2. **No Streamlit Cloud:**
   - Vá em "Settings" → "Source control"
   - Verifique se a conta GitHub está conectada corretamente
   - Se necessário, desconecte e reconecte

#### Opção 3: Conectar Conta Correta

1. **Desconectar e reconectar:**
   - No Streamlit Cloud, vá em "Settings"
   - Clique em "Disconnect" na seção GitHub
   - Clique em "Connect" e autorize novamente

2. **Verificar conta:**
   - Certifique-se de estar logado com a conta que tem acesso ao repositório
   - Se o repositório é privado, você precisa ter acesso no GitHub

### Verificações

✅ **Repositório existe?**
- https://github.com/adlerzero/atlas-engenharia-civil

✅ **Repositório é público ou você tem acesso?**
- Settings → Change repository visibility

✅ **Conta GitHub conectada corretamente?**
- Streamlit Cloud → Settings → Source control

### Passo a Passo Rápido

1. Delete o app atual no Streamlit Cloud
2. Certifique-se de que o repositório está público (ou você tem acesso)
3. Crie um novo app conectando ao mesmo repositório
4. Deploy automático deve funcionar

### Se o Problema Persistir

- Verifique se o repositório realmente existe
- Verifique se você tem permissões de leitura no repositório
- Tente criar o app com um nome diferente
- Entre em contato com o suporte do Streamlit Cloud

