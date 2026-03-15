# Bugs e Aprendizados — ESC Skills

## 2026-03-15 — Cloudflare CDN caching de JS files

### Problema
Após atualizar `skills-data.js` e fazer deploy via rsync, o Cloudways/Cloudflare continuava servindo a versão antiga do arquivo. Mesmo com query strings (`?v=timestamp`), o CDN cacheia agressivamente.

### Solução
Renomear o arquivo com sufixo de versão incrementando:
- `skills-data.js` → `skills-data-v4.js` → `skills-data-v5.js`
- Atualizar a referência em `index.html`: `<script src="skills-data-v5.js">`

### Prevenção
- Sempre que fizer alterações no `skills-data.js`, incrementar a versão do arquivo
- Manter o script source com versionamento: `skills-data-vN.js`
- Versão atual: **v5**

---

## 2026-03-15 — Traduções perdidas durante rebuild

### Problema
O `build-data.js` sobrescrevia traduções manuais (`shortDescriptionPt`, `descriptionPt`) e overrides de `shortDescription` (EN) toda vez que era executado.

### Solução
Adicionada lógica no `build-data.js` para:
1. Carregar o `skills-data.js` existente antes do rebuild
2. Extrair traduções e overrides por skill name
3. Mesclar os valores preservados no output novo

### Prevenção
- Nunca editar `skills-data.js` manualmente (sempre via `build-data.js`)
- Se precisar adicionar tradução, adicionar no fluxo de merge do build
