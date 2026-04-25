---
description: Push seguro para GitHub com validação de manifest, sync de diretórios e boas práticas de commit. Use SEMPRE que precisar fazer git commit + push no repositório esc-skills — nunca faça push direto sem passar por este workflow.
---

# GitHub Deploy — Push Seguro

Pipeline obrigatório para qualquer push no repositório `esc-skills`. Garante que o CI (`Verify Skill Versions`) não quebre.

> **Lição-chave (2026-04-25):** Push de SKILL.md sem atualizar `manifest.json` causou 8 falhas no CI.
> Este workflow existe para que isso nunca mais aconteça.

---

## Etapa 0 — Verificar o que mudou

// turbo

```bash
git status --short
```

**Decisão:**
- Se **nenhum SKILL.md** foi alterado → pular para Etapa 3
- Se **algum SKILL.md em `.agent/skills/`** foi alterado → ir para Etapa 1
- Se **algum SKILL.md em `skills/`** foi alterado → ir para Etapa 2

---

## Etapa 1 — Sync `.agent/skills/` → `skills/` (público)

O git só tracka `skills/`. Edições feitas em `.agent/skills/` precisam ser copiadas.

// turbo

```bash
# Para cada skill modificada:
cp -R ".agent/skills/<SKILL_NAME>/" "skills/<SKILL_NAME>/"
```

> ⚠️ Copiar a **pasta inteira** (não só o SKILL.md) para incluir references/, scripts/, etc.

---

## Etapa 2 — Atualizar manifest

### 2.1 Adicionar version headers (se necessário)

// turbo

```bash
python3 scripts/update_manifest.py --add-headers
```

### 2.2 Bumpar versão de cada skill modificada

```bash
# MINOR para mudanças funcionais (novo comportamento, novas regras)
python3 scripts/update_manifest.py --bump <SKILL_NAME> MINOR

# PATCH para correções e ajustes menores (typos, formatting)
python3 scripts/update_manifest.py --bump <SKILL_NAME> PATCH
```

> **Quando usar cada tipo:**
> - `MAJOR` → breaking change (reestruturação completa da skill)
> - `MINOR` → nova funcionalidade, nova regra, novo intake (o que fizemos hoje)
> - `PATCH` → fix de typo, ajuste cosmético, adição de header

### 2.3 Verificar integridade

// turbo

```bash
python3 scripts/update_manifest.py --verify
```

**Resultado esperado:** `✅ All NN skills verified — hashes match, headers present`

**Se falhar:** Repetir 2.1 e 2.2 para as skills apontadas no erro.

### 2.4 Sync reverso `skills/` → `.agent/skills/`

Os bumps e headers alteraram `skills/`. Sincronizar de volta:

// turbo

```bash
# Para cada skill bumpada:
cp "skills/<SKILL_NAME>/SKILL.md" ".agent/skills/<SKILL_NAME>/SKILL.md"
```

---

## Etapa 3 — Commit

### Convenções de commit

| Prefixo | Quando usar | Exemplo |
|---------|-------------|---------|
| `feat(scope):` | Nova funcionalidade ou regra | `feat(gtm-suite): enforce template-first` |
| `fix(scope):` | Correção de bug | `fix(qa-auditor): add missing etapa 1.5` |
| `chore:` | Manutenção (manifest, headers) | `chore: update manifest hashes` |
| `docs:` | Documentação (se tracked) | `docs: update README skill count` |
| `refactor(scope):` | Reestruturação sem mudar comportamento | `refactor(gtm-expert): simplify intake` |

### Regras de commit

1. **Separar mudanças funcionais de chore:** Se editou skills E atualizou manifest, pode ser 1 ou 2 commits — mas o manifest DEVE estar no push
2. **Não incluir `.DS_Store`** — verificar com `git status` antes de `git add`
3. **Mensagem em inglês** — padrão do repo

```bash
# Stage apenas o necessário (nunca git add -A sem revisar)
git add skills/<SKILL_1>/SKILL.md skills/<SKILL_2>/SKILL.md manifest.json

git commit -m "feat(scope): descrição concisa

- Detalhe 1
- Detalhe 2"
```

---

## Etapa 4 — Push

// turbo

```bash
git push origin main
```

---

## Etapa 5 — Verificar CI

Após o push, o GitHub Actions roda `Verify Skill Versions` automaticamente.

- ✅ Verde → deploy concluído
- ❌ Vermelho → voltar para Etapa 2

> 💡 Se o CI falhar após seguir este workflow completo, é provável que outro arquivo tenha mudado entre o `--verify` local e o push. Rodar `--verify` novamente e commitar a correção.

---

## Checklist Rápido

```
- [ ] git status revisado (sem .DS_Store, sem arquivos indesejados)
- [ ] .agent/skills/ → skills/ sincronizado (se aplicável)
- [ ] --add-headers executado
- [ ] --bump executado para cada skill modificada
- [ ] --verify retorna ✅
- [ ] skills/ → .agent/skills/ sync reverso (se aplicável)
- [ ] Commit com mensagem convencional
- [ ] git push origin main
- [ ] CI verde no GitHub
```

---

## Anti-patterns

```
❌ git add -A && git push — nunca sem revisar o que está sendo staged
❌ Push de SKILL.md sem rodar --verify — CI VAI quebrar
❌ Editar skills/ direto sem copiar para .agent/skills/ — agente local fica desatualizado
❌ Usar git add . em vez de listar arquivos explícitos — risco de incluir .DS_Store, keys/, etc.
❌ Reusar versão sem bump — manifest hash diverge do conteúdo
```
