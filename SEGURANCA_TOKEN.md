# ⚠️ ALERTA DE SEGURANÇA - Token GitHub Exposto

## 🔴 AÇÃO NECESSÁRIA

O token GitHub foi compartilhado e está exposto. Você **DEVE** revogá-lo imediatamente após o push.

## 🛡️ Como Revogar o Token

1. **Acesse GitHub:**
   - https://github.com/settings/tokens
   - Ou: Settings → Developer settings → Personal access tokens → Tokens (classic)

2. **Encontre o token:**
   - Procure por tokens criados recentemente
   - Ou procure pelo nome/descrição que você deu

3. **Revogue:**
   - Clique no token
   - Clique em "Delete" ou "Revoke"
   - Confirme

4. **Crie um novo token (se necessário):**
   - Generate new token (classic)
   - Dê permissões necessárias (repo, workflow, etc.)
   - **NUNCA compartilhe o novo token!**

## 🔐 Boas Práticas

- ✅ Use tokens apenas localmente
- ✅ Nunca commite tokens no código
- ✅ Use variáveis de ambiente
- ✅ Revogue tokens expostos imediatamente
- ✅ Use tokens com escopo mínimo necessário

## 📝 Alternativa Segura

Para evitar expor tokens, você pode:

1. **Usar SSH:**
   ```bash
   git remote set-url origin git@github.com:USUARIO/repo.git
   ```

2. **Usar GitHub CLI:**
   ```bash
   gh auth login
   ```

3. **Usar credenciais do sistema:**
   - Git Credential Manager
   - Keychain (macOS)
   - Credential Manager (Windows)

