# Wireframe-Sketch — Template HTML

Template de referência para o HTML da Fase 2 (Wireframe-Sketch). O sketch é auto-contido: todo CSS e JS são inline.

## Estrutura Completa

```html
<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Wireframe - [MARCA]</title>
    <link href="https://fonts.googleapis.com/css2?family=Architects+Daughter&family=Comic+Neue:wght@400;700&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css">
    <!-- CSS inline abaixo -->
</head>
<body>
    <!-- Sketch Badge -->
    <div class="sketch-badge">📐 Wireframe Sketch — Baixa Fidelidade</div>

    <!-- SEÇÕES DA LP (usar backgrounds alternados) -->
    <section class="hero bg-cream">
        <div class="container">
            <span class="section-label">Hero</span>
            <div data-animate="fade-up">
                <h1>[Headline principal]</h1>
                <p>[Subheadline com proposta de valor]</p>
                <a href="#form" class="cta-button primary">[Call to Action] →</a>
            </div>
        </div>
    </section>

    <!-- Repetir seções conforme framework -->

    <!-- FORMULÁRIO -->
    <section id="form" class="bg-peach">
        <div class="container">
            <span class="section-label">Conversão</span>
            <h2 class="text-center" data-animate="fade-up">[CTA de fechamento]</h2>
            <div style="max-width: 500px; margin: 0 auto;" data-animate="fade-up">
                <input type="text" placeholder="Seu nome">
                <input type="email" placeholder="Seu melhor e-mail">
                <input type="tel" placeholder="WhatsApp com DDD">
                <input type="text" placeholder="Nome da empresa">
                <select><option>Seu cargo</option></select>
                <select><option>Segmento da empresa</option></select>
                <select><option>Principal desafio</option></select>
                <button class="cta-button primary" style="width: 100%;">[Texto do CTA] →</button>
                <p class="trust-text">🔒 Dados confidenciais. Respondemos em até 24h.</p>
            </div>
        </div>
    </section>

    <!-- SCROLL ANIMATIONS (IntersectionObserver) -->
    <script>
        document.addEventListener('DOMContentLoaded', () => {
            const els = document.querySelectorAll('[data-animate], [data-stagger]');
            const observer = new IntersectionObserver((entries) => {
                entries.forEach(entry => {
                    if (entry.isIntersecting) {
                        entry.target.classList.add('is-visible');
                        observer.unobserve(entry.target);
                    }
                });
            }, { threshold: 0.15, rootMargin: '0px 0px -40px 0px' });
            els.forEach(el => observer.observe(el));
        });

        // Smooth scroll
        document.querySelectorAll('a[href^="#"]').forEach(anchor => {
            anchor.addEventListener('click', function(e) {
                e.preventDefault();
                const target = document.querySelector(this.getAttribute('href'));
                if (target) target.scrollIntoView({ behavior: 'smooth', block: 'start' });
            });
        });
    </script>
</body>
</html>
```

## CSS Completo (inline no `<head>`)

```css
/* RESET */
* { margin: 0; padding: 0; box-sizing: border-box; }

body {
    font-family: 'Comic Neue', cursive;
    background: #FFFFFF;
    color: #666666;
    line-height: 1.7;
}

/* TIPOGRAFIA SKETCH */
h1, h2, h3, h4, h5, h6 {
    font-family: 'Architects Daughter', cursive;
    color: #000000;
    line-height: 1.3;
}
h1 { font-size: 42px; margin-bottom: 16px; }
h2 { font-size: 32px; margin-bottom: 14px; }
h3 { font-size: 24px; margin-bottom: 12px; }

/* CONTAINER */
.container { max-width: 960px; margin: 0 auto; padding: 0 24px; }

/* SECTION LABEL */
.section-label {
    font-family: 'Architects Daughter', cursive;
    font-size: 12px;
    color: #999;
    text-transform: uppercase;
    letter-spacing: 2px;
    margin-bottom: 8px;
    padding: 4px 12px;
    border-left: 3px solid #CCCCCC;
    display: inline-block;
}

/* SECTIONS */
section { padding: 64px 0; }

/* BACKGROUNDS ALTERNADOS */
.bg-cream    { background: #FFFDF7; }
.bg-rose     { background: #FFF5F3; }
.bg-white    { background: #FFFFFF; }
.bg-mint     { background: #F2FAF6; }
.bg-ice      { background: #EDF4FF; }
.bg-lavender { background: #F5F0FF; }
.bg-peach    { background: #FFF8F0; }
.bg-gray     { background: #F5F5F5; }

/* CARDS */
.card {
    border: 3px solid #000000;
    border-radius: 12px;
    padding: 24px;
    background: #FFFFFF;
}
.cards-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
    gap: 20px;
}

/* BOTÕES CTA */
.cta-button {
    font-family: 'Comic Neue', cursive;
    font-weight: 700;
    background: #E0E0E0;
    border: 2px solid #000000;
    border-radius: 20px;
    box-shadow: 4px 4px 0px #000000;
    padding: 14px 32px;
    cursor: pointer;
    font-size: 16px;
    color: #000000;
    display: inline-block;
    text-decoration: none;
    transition: all 0.15s ease;
}
.cta-button:hover {
    transform: translate(2px, 2px);
    box-shadow: 2px 2px 0px #000000;
}
.cta-button.primary { background: #F0F4F8; }

/* PLACEHOLDER DE IMAGEM */
.image-placeholder {
    background: #F0F4F8;
    border: 3px dashed #CCCCCC;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    min-height: 240px;
    border-radius: 8px;
    gap: 12px;
}
.image-placeholder .x-mark {
    font-size: 48px;
    color: #CCCCCC;
    font-weight: 700;
}
.image-placeholder .direction {
    background: #FFF9C4;
    padding: 6px 14px;
    font-size: 13px;
    color: #555;
    border-radius: 6px;
    text-align: center;
    max-width: 80%;
    font-style: italic;
}

/* FORMULÁRIOS */
input, textarea, select {
    font-family: 'Comic Neue', cursive;
    border: 2px solid #CCCCCC;
    border-radius: 8px;
    padding: 14px 16px;
    width: 100%;
    font-size: 14px;
    color: #555;
    background: #fff;
    outline: none;
    transition: border-color 0.2s;
    margin-bottom: 16px;
}
input::placeholder, textarea::placeholder { color: #BBBBBB; }
input:focus, textarea:focus, select:focus { border-color: #000; }

/* TRUST TEXT */
.trust-text {
    text-align: center;
    font-size: 12px;
    color: #999;
    margin-top: 12px;
}

/* ÍCONES */
.icon { font-size: 32px; margin-bottom: 12px; color: #000000; }
.icon-alert { color: #D90429; }

/* HERO */
.hero { padding: 80px 0 60px; }
.hero h1 { font-size: 36px; max-width: 800px; }
.hero p { font-size: 17px; color: #666; max-width: 600px; margin-bottom: 28px; line-height: 1.8; }

/* SKETCH BADGE */
.sketch-badge {
    position: fixed;
    top: 16px;
    right: 16px;
    background: #FFF9C4;
    border: 2px solid #000;
    border-radius: 8px;
    padding: 8px 16px;
    font-family: 'Architects Daughter', cursive;
    font-size: 12px;
    color: #000;
    box-shadow: 3px 3px 0 #000;
    z-index: 999;
}

/* UTILITIES */
.text-center { text-align: center; }
.mt-20 { margin-top: 20px; }
.mb-20 { margin-bottom: 20px; }

/* SCROLL ANIMATIONS */
@keyframes fadeInUp {
    from { opacity: 0; transform: translateY(40px); }
    to { opacity: 1; transform: translateY(0); }
}
@keyframes fadeInScale {
    from { opacity: 0; transform: scale(0.92); }
    to { opacity: 1; transform: scale(1); }
}
@keyframes slideInLeft {
    from { opacity: 0; transform: translateX(-30px); }
    to { opacity: 1; transform: translateX(0); }
}
@keyframes slideInRight {
    from { opacity: 0; transform: translateX(30px); }
    to { opacity: 1; transform: translateX(0); }
}

[data-animate] { opacity: 0; }
[data-animate].is-visible {
    animation-fill-mode: both;
    animation-duration: 0.7s;
    animation-timing-function: cubic-bezier(0.22, 1, 0.36, 1);
}
[data-animate="fade-up"].is-visible    { animation-name: fadeInUp; }
[data-animate="fade-scale"].is-visible { animation-name: fadeInScale; }
[data-animate="slide-left"].is-visible { animation-name: slideInLeft; }
[data-animate="slide-right"].is-visible{ animation-name: slideInRight; }

/* STAGGER */
[data-stagger]>*:nth-child(1) { --delay: 0s; }
[data-stagger]>*:nth-child(2) { --delay: 0.12s; }
[data-stagger]>*:nth-child(3) { --delay: 0.24s; }
[data-stagger]>*:nth-child(4) { --delay: 0.36s; }
[data-stagger]>*:nth-child(5) { --delay: 0.48s; }
[data-stagger]>*:nth-child(6) { --delay: 0.6s; }
[data-stagger].is-visible>* {
    animation: fadeInUp 0.6s cubic-bezier(0.22, 1, 0.36, 1) both;
    animation-delay: var(--delay, 0s);
}
[data-stagger]>* { opacity: 0; }

/* RESPONSIVE */
@media (max-width: 768px) {
    section { padding: 40px 0; }
    h1 { font-size: 28px; }
    h2 { font-size: 24px; }
    .hero { padding: 48px 0 40px; }
    .hero h1 { font-size: 28px; }
    .cards-grid { grid-template-columns: 1fr; }
    .cta-button { width: 100%; text-align: center; }
}
```

## Componentes de Referência

### Card com Ícone

```html
<div class="card">
    <i class="fas fa-exclamation-triangle icon"></i>
    <h3>[Título do card]</h3>
    <p>[Descrição]</p>
</div>
```

### Grid com Stagger

```html
<div class="cards-grid mt-20" data-animate="fade-up" data-stagger>
    <div class="card">...</div>
    <div class="card">...</div>
    <div class="card">...</div>
</div>
```

### Placeholder de Imagem

```html
<div class="image-placeholder" data-animate="fade-scale">
    <span class="direction">[Direcionamento: foto de equipe em reunião]</span>
    <span class="x-mark">✕</span>
</div>
```

### Seção com Background e Animation

```html
<section class="bg-rose">
    <div class="container">
        <span class="section-label">Problema</span>
        <h2 data-animate="fade-up">[Headline da seção]</h2>
        <p>[Conteúdo]</p>
    </div>
</section>
```

## Ícones Sugeridos (Font Awesome)

| Contexto | Ícone |
|----------|-------|
| Dor/problema | `fa-exclamation-triangle`, `fa-times-circle` |
| Benefício | `fa-check-circle`, `fa-chart-line`, `fa-shield-alt` |
| Dinheiro | `fa-dollar-sign`, `fa-coins` |
| Tempo | `fa-clock`, `fa-hourglass` |
| Segurança | `fa-lock`, `fa-shield-alt` |
| Pessoas | `fa-users`, `fa-user-tie` |
| Processo | `fa-cogs`, `fa-sitemap`, `fa-project-diagram` |
| Suporte | `fa-headset`, `fa-life-ring` |

Usar `class="icon"` no `<i>` para tamanho padronizado. Usar `class="icon icon-alert"` para ícones de alerta em vermelho.
