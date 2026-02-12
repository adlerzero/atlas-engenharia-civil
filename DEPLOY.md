# 🚀 Guia de Deploy - ATLAS

## ⚠️ IMPORTANTE: GitHub Pages NÃO funciona para Streamlit!

GitHub Pages é apenas para sites **estáticos** (HTML/CSS/JS). 
Aplicações Streamlit precisam de um **servidor Python**, então GitHub Pages **não funciona**.

## ✅ Solução Recomendada: Streamlit Cloud

### Passo a Passo:

1. **Acesse o Streamlit Cloud:**
   - https://share.streamlit.io/
   - Faça login com sua conta GitHub

2. **Conecte seu Repositório:**
   - Clique em "New app"
   - Selecione seu repositório: `atlas-engenharia-civil`
   - Branch: `main`
   - Main file path: `app.py` (já vem preenchido)

3. **Configure (Opcional):**
   - App URL: `atlas-engenharia-civil` (ou outro nome)
   - Python version: 3.10
   - Advanced settings: Deixe padrão

4. **Deploy:**
   - Clique em "Deploy"
   - Aguarde alguns minutos
   - Pronto! Sua app estará online! 🎉

### Vantagens do Streamlit Cloud:

- ✅ **Gratuito** para apps públicos
- ✅ **Deploy automático** a cada push
- ✅ **URL pública** para compartilhar
- ✅ **Fácil de usar** - sem configuração complexa

## 🔧 Desabilitar GitHub Pages (se não precisar)

Se você não precisa de GitHub Pages, desabilite:

1. Vá em **Settings** do seu repositório
2. Clique em **Pages** (no menu lateral)
3. Em **Source**, selecione **None**
4. Salve

Isso vai parar os erros de build do GitHub Pages.

## 📝 Alternativas de Hosting

Se não quiser usar Streamlit Cloud:

- **Heroku** (pago após free tier)
- **Railway** (free tier disponível)
- **Render** (free tier disponível)
- **DigitalOcean App Platform** (pago)
- **AWS/GCP/Azure** (pago)

## 🎯 Resumo

- ❌ **GitHub Pages:** Não funciona para Streamlit
- ✅ **Streamlit Cloud:** Melhor opção, gratuita e fácil
- ✅ **Outros serviços:** Alternativas se necessário

