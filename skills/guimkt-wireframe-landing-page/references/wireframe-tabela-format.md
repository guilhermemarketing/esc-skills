# Wireframe-Tabela — Formato HTML

Template de referência para o HTML da Fase 1 (Wireframe-Tabela).

## Estrutura do HTML

```html
<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Wireframe LP — [MARCA]</title>
    <link href="https://fonts.googleapis.com/css2?family=Inter+Tight:wght@700&family=Inter:wght@400;500;600&display=swap" rel="stylesheet">
    <!-- CSS inline (ver seção Estilos) -->
</head>
<body>
    <header class="page-header">
        <h1>Wireframe Landing Page — [MARCA]</h1>
        <p class="subtitle">
            Wireframe em formato de tabela para landing page de geração de SQLs.
            Framework <strong>[FRAMEWORK]</strong> — [PRODUTO].
        </p>
    </header>

    <div class="container">
        <span class="brand-badge">[MARCA] · [PRODUTO]</span>

        <!-- TABELA WIREFRAME -->
        <div class="wireframe-wrap">
            <table class="wireframe-table" id="wireframe-[slug]">
                <thead>
                    <tr>
                        <th>Seção</th>
                        <th>Framework</th>
                        <th>Elemento</th>
                        <th>Conteúdo</th>
                        <th>Notas para Designer</th>
                    </tr>
                </thead>
                <tbody>
                    <!-- Separador de etapa do framework -->
                    <tr class="section-separator">
                        <td colspan="5">[ETAPA] ([DESCRIÇÃO])</td>
                    </tr>
                    <!-- Linhas da seção -->
                    <tr>
                        <td>[Nome seção]</td>
                        <td>[Etapa]</td>
                        <td>[Elemento UI]</td>
                        <td>[Conteúdo real]</td>
                        <td>[Notas de design]</td>
                    </tr>
                    <!-- Repetir para cada linha/seção -->
                </tbody>
            </table>
        </div>

        <!-- DEFESA DO WIREFRAME -->
        <div class="defesa-card">
            <span class="tag-framework">[FRAMEWORK]</span>
            <h2>Defesa do Wireframe: Framework [FRAMEWORK]</h2>

            <h3>1. Justificativa da Escolha</h3>
            <p>[Explicação + pontos fortes em lista]</p>

            <h3>2. Adequação ao Contexto</h3>
            <ul>
                <li><strong>Nível de consciência:</strong> [...]</li>
                <li><strong>Natureza do produto:</strong> [...]</li>
                <li><strong>Objetivo (SQL):</strong> [...]</li>
                <li><strong>Canal:</strong> [...]</li>
            </ul>

            <h3>3. Frameworks Descartados</h3>
            <ul>
                <li><strong>[Framework A]</strong> — [Motivo]</li>
                <li><strong>[Framework B]</strong> — [Motivo]</li>
                <li><strong>[Framework C]</strong> — [Motivo]</li>
            </ul>

            <h3>4. Resultado Esperado</h3>
            <ul>
                <li><strong>Tempo médio na página:</strong> [...]</li>
                <li><strong>Taxa de conversão estimada:</strong> [...]</li>
                <li><strong>Qualidade dos leads:</strong> [...]</li>
            </ul>
        </div>
    </div>
</body>
</html>
```

## Estilos CSS

```css
:root {
    --font-title: 'Inter Tight', sans-serif;
    --font-body: 'Inter', sans-serif;
}

* { margin: 0; padding: 0; box-sizing: border-box; }

body {
    font-family: var(--font-body);
    background: #f7f3ed;
    color: #1a1a1a;
    line-height: 1.65;
}

/* HEADER */
.page-header {
    text-align: center;
    padding: 48px 24px 32px;
}
.page-header h1 {
    font-family: var(--font-title);
    font-size: 2rem;
    color: #000;
}
.page-header .subtitle {
    font-size: .95rem;
    color: #666;
    max-width: 560px;
    margin: 8px auto 0;
}

/* CONTAINER */
.container {
    max-width: 1200px;
    margin: 0 auto;
    padding: 0 24px 64px;
}

/* BADGE */
.brand-badge {
    display: inline-block;
    padding: 3px 12px;
    border-radius: 20px;
    font-weight: 600;
    font-size: .75rem;
    background: #dcd3ef;
    color: #4a2896;
    margin-bottom: 24px;
}

/* TABLE */
.wireframe-wrap {
    overflow-x: auto;
    border-radius: 16px;
    box-shadow: 0 2px 16px rgba(0,0,0,.06);
    background: #fff;
    margin-bottom: 40px;
}

table.wireframe-table {
    width: 100%;
    border-collapse: collapse;
    font-size: .86rem;
}

table.wireframe-table thead th {
    font-family: var(--font-title);
    font-weight: 700;
    font-size: .8rem;
    text-transform: uppercase;
    padding: 14px 16px;
    background: #555;       /* cor neutra — adaptar à marca */
    color: #fff;
    text-align: left;
    position: sticky;
    top: 0;
    z-index: 2;
}

table.wireframe-table thead th:first-child { border-radius: 16px 0 0 0; }
table.wireframe-table thead th:last-child { border-radius: 0 16px 0 0; }

table.wireframe-table tbody td {
    padding: 14px 16px;
    border-bottom: 1px solid #eee;
    vertical-align: top;
}

table.wireframe-table tbody tr:hover { background: #faf8f5; }

table.wireframe-table tbody td:first-child {
    font-weight: 600;
    font-family: var(--font-title);
    color: #555;
    white-space: nowrap;
    min-width: 140px;
}

.section-separator td {
    background: #dcd3ef !important;
    font-family: var(--font-title) !important;
    font-weight: 700 !important;
    color: #4a2896 !important;
    font-size: .82rem !important;
    text-transform: uppercase !important;
    letter-spacing: .5px !important;
    padding: 10px 16px !important;
}

/* DEFESA CARD */
.defesa-card {
    background: #fff;
    border-radius: 16px;
    padding: 32px;
    box-shadow: 0 2px 16px rgba(0,0,0,.06);
    border-top: 4px solid #555;
    margin-bottom: 40px;
}

.defesa-card h2 { font-family: var(--font-title); font-size: 1.2rem; margin-bottom: 20px; }
.defesa-card h3 { font-family: var(--font-title); font-size: .95rem; margin: 20px 0 8px; }
.defesa-card p, .defesa-card li { font-size: .88rem; line-height: 1.7; }
.defesa-card ul { padding-left: 18px; }
.defesa-card ul li { margin-bottom: 6px; }

.tag-framework {
    display: inline-block;
    padding: 4px 14px;
    border-radius: 12px;
    font-size: .72rem;
    font-weight: 700;
    background: #555;
    color: #fff;
    margin-bottom: 16px;
}

/* RESPONSIVE */
@media (max-width: 768px) {
    .page-header h1 { font-size: 1.5rem; }
    table.wireframe-table { font-size: .8rem; }
}
```

## Seções Obrigatórias da Tabela

Estrutura mínima da tabela para qualquer framework:

1. **Hero Section**
   - Headline (H1) — máx. 2 linhas, impacto emocional
   - Subheadline — máx. 3 linhas, proposta de valor
   - CTA Primário — texto real do botão
   - Trust Bar — 3-4 badges ou credenciais

2. **Seções do Framework** (1 separador por etapa)
   - Headline (H2) por seção
   - Componentes UI relevantes (cards, listas, depoimentos, etc.)
   - Conteúdo real baseado no briefing

3. **Formulário**
   - Headline do form + promessa de resposta
   - Campos com lead scoring (nome, e-mail, telefone, empresa + dropdowns: cargo, segmento, desafio)
   - CTA do form — texto real
   - Garantia/trust: confidencialidade, prazo de resposta

4. **Footer**
   - Logo, redes sociais, telefone/WhatsApp, copyright

## Notas de Personalização

- **Cores:** Adaptar `background` do `thead th`, `.tag-framework`, `.defesa-card border-top` e `td:first-child color` para cores da marca do cliente quando disponíveis
- **Logo:** Se o cliente fornecer logo, incluir no header
- **Fontes:** Inter Tight + Inter são defaults neutros e profissionais. Adaptar se a marca tiver tipografia própria
