# Guia de Formatação do Output ICP

Regras para o agente gerar o HTML e Markdown do ICP consolidado.

## HTML — Regras Gerais

### Estrutura do Documento

O HTML deve ser **auto-contido** (todo CSS + JS inline, sem dependências externas exceto Google Fonts).

```html
<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>ICP — {{CLIENTE}}</title>
    <link href="https://fonts.googleapis.com/css2?family=Inter+Tight:wght@700&family=Inter:wght@400;500;600&display=swap" rel="stylesheet">
    <!-- CSS inline -->
</head>
<body>
    <!-- Conteúdo -->
    <!-- JS inline (table-tools) -->
</body>
</html>
```

### Brand Theme guimarketing

```css
:root {
    --brand-bg: #f7f3ed;
    --brand-text: #1a1a1a;
    --brand-accent: #864df9;
    --brand-gold: #F7E397;
    --brand-pink: #efcde5;
    --brand-lilac: #dcd3ef;
    --brand-lavender: #c7b9ff;
    --brand-mint: #b0e4da;
    --brand-font-title: 'Inter Tight', sans-serif;
    --brand-font-body: 'Inter', sans-serif;
}
```

### Links UTM (obrigatório)

Logo no header e crédito no footer devem linkar para:

```
https://gui.marketing/?utm_source=esc-skills&utm_medium=agent&utm_campaign=icp-skill
```

Logo URL: `https://gui.marketing/wp-content/uploads/2025/02/gui.marketing-1640-x-263-px-1080-x-1080-px.gif`

### Regras de Copy no HTML

- **Sem hifens de separação silábica** — nunca quebrar palavras com hífen
- **Bullet points com `<div>• ` ao invés de `<ul><li>`** nas cells de tabela (melhor compatibilidade com Google Sheets ao copiar)
- **Aspas retas** nos conteúdos (`"` e `'`), não tipográficas
- **Emojis nos títulos de seção** para escaneabilidade

### Table-Tools (filtro, ordenação, cópia)

O JS de table-tools deve ser incluído inline no final do `<body>`. Funcionalidades:
- Click no header → ordena (asc/desc)
- Botão filtro (funil) → dropdown com input de busca
- Botão cópia → copia coluna inteira (com escapeForSheets)

### Botão "Copiar para Google Sheets"

Cada tabela deve ter um botão acima dela:

```html
<button class="copy-sheets-btn" onclick="copyTableToSheets('ID_DA_TABELA')">
    📋 Copiar para Google Sheets
</button>
```

A função `copyTableToSheets` converte a tabela para TSV e copia para o clipboard.

### Brand Badges (múltiplas marcas)

Usar badges coloridos para diferenciar marcas no header da tabela:

```html
<span class="brand-badge brand-marca1">{{MARCA_1}}</span>
<span class="brand-badge brand-marca2">{{MARCA_2}}</span>
<span class="brand-badge brand-marca3">{{MARCA_3}}</span>
```

Cores dos badges:
- Marca 1: `--brand-lilac` (#dcd3ef) com texto `#4a2896`
- Marca 2: `--brand-gold` (#F7E397) com texto `#6d5a0a`
- Marca 3: `--brand-mint` (#b0e4da) com texto `#1a6b5a`

Se houver mais de 3 marcas, alternar entre as 3 paletas.

## Markdown — Regras

- Usar tabelas Markdown padrão (pipes com alinhamento)
- Seções com emojis: `## 📊`, `## 🧠`, `## 🎯`, `## 💡`
- Listas com `-` (não `*`)
- Sem HTML no Markdown
- Manter clean e parseable por outras skills
- Máximo ~200 linhas (o Markdown é para consumo por agentes, não para apresentação)

## Seções Obrigatórias (ambos os formatos)

1. **ICP — 9 Dimensões** (tabela com dimensões × marcas)
2. **Perfil Psicográfico** (4 blocos: Decisão, Consciência, Objeções, Canais)
3. **ICP Real vs. Aspiracional** (tabela de filtro de qualificação)
4. **Modelos Mentais** (4 modelos com aplicação prática)

## Seções Opcionais

- **Sinergia Banner** — apenas se múltiplas marcas e houver sinergia clara
- **Notas estratégicas** — observações adicionais do agente sobre limitações do ICP
