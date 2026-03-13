# Landing Page Premium — Template HTML

Template de referência para o HTML da Fase 2 (Landing Page Premium). O arquivo deve ser auto-contido: todo CSS e JS inline.

## Estrutura Completa

```html
<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>[MARCA] — [PROPOSTA DE VALOR CURTA]</title>
    <meta name="description" content="[Meta description com proposta de valor e CTA]">

    <!-- FONTS -->
    <link href="https://fonts.googleapis.com/css2?family=[DISPLAY_FONT]:wght@600;700;800&family=[BODY_FONT]:wght@400;500;600&display=swap" rel="stylesheet">

    <!-- ICONS -->
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css">

    <!-- CSS inline (ver seção completa) -->
</head>
<body>
    <!-- FLOATING NAVBAR -->
    <nav class="navbar">
        <div class="navbar-inner">
            <span class="navbar-logo">[MARCA]</span>
            <a href="#form" class="navbar-cta">[CTA curto] →</a>
        </div>
    </nav>

    <!-- HERO -->
    <section class="hero">
        <div class="orb orb-1"></div>
        <div class="orb orb-2"></div>
        <div class="container">
            <div data-animate="fade-up">
                <span class="badge">[Badge de contexto]</span>
                <h1>[Headline com <span class="gradient-text">destaque gradiente</span>]</h1>
                <p class="hero-sub">[Subheadline de proposta de valor]</p>
                <a href="#form" class="cta-premium">[CTA] →</a>
            </div>
            <!-- Trust bar -->
            <div class="trust-bar" data-animate="fade-up">
                <div class="trust-item"><i class="fas fa-shield-alt"></i> [Trust 1]</div>
                <div class="trust-item"><i class="fas fa-check-circle"></i> [Trust 2]</div>
                <div class="trust-item"><i class="fas fa-star"></i> [Trust 3]</div>
            </div>
        </div>
    </section>

    <!-- SEÇÕES DO FRAMEWORK (repetir conforme wireframe-tabela) -->
    <section class="section-alt">
        <div class="container">
            <h2 data-animate="fade-up">[Headline da seção]</h2>
            <p class="section-sub" data-animate="fade-up">[Subheadline]</p>
            <div class="cards-grid" data-animate="fade-up" data-stagger>
                <div class="glass-card">
                    <i class="fas fa-icon icon"></i>
                    <h3>[Título]</h3>
                    <p>[Descrição]</p>
                </div>
                <!-- mais cards -->
            </div>
        </div>
    </section>

    <!-- FORMULÁRIO -->
    <section id="form" class="section-form">
        <div class="orb orb-3"></div>
        <div class="container">
            <h2 class="text-center" data-animate="fade-up">[Headline do form]</h2>
            <p class="section-sub text-center" data-animate="fade-up">[Reforço de valor]</p>
            <div class="form-card glass-card" data-animate="fade-scale">
                <input type="text" placeholder="Seu nome completo">
                <input type="email" placeholder="Seu melhor e-mail">
                <input type="tel" placeholder="WhatsApp com DDD">
                <input type="text" placeholder="Nome da empresa">
                <select><option value="">Seu cargo</option><!-- opções --></select>
                <select><option value="">Segmento da empresa</option></select>
                <select><option value="">Principal desafio</option></select>
                <button class="cta-premium full-width">[CTA do form] →</button>
                <p class="form-trust">🔒 Seus dados são confidenciais. Respondemos em até 24h.</p>
            </div>
        </div>
    </section>

    <!-- FOOTER -->
    <footer class="footer">
        <div class="container">
            <p class="footer-logo">[MARCA]</p>
            <p class="footer-copy">© 2026 [MARCA] — Todos os direitos reservados</p>
        </div>
    </footer>

    <!-- SCROLL ANIMATIONS -->
    <script>
        document.addEventListener('DOMContentLoaded', () => {
            const els = document.querySelectorAll('[data-animate], [data-stagger]');
            if (window.matchMedia('(prefers-reduced-motion: reduce)').matches) {
                els.forEach(el => { el.style.opacity = '1'; });
                return;
            }
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

        // Navbar scroll effect
        window.addEventListener('scroll', () => {
            const navbar = document.querySelector('.navbar');
            if (window.scrollY > 50) {
                navbar.classList.add('scrolled');
            } else {
                navbar.classList.remove('scrolled');
            }
        });
    </script>
</body>
</html>
```

## CSS Design System Completo

```css
/* ══════════════════════════════════════════ */
/* CSS VARIABLES (design system tokens)      */
/* Adaptar às cores da marca do cliente      */
/* ══════════════════════════════════════════ */
:root {
    --primary: #6366f1;
    --primary-rgb: 99, 102, 241;
    --accent: #a855f7;
    --accent-rgb: 168, 85, 247;

    --bg: #0a0a0f;
    --bg-surface: rgba(255, 255, 255, 0.03);
    --bg-alt: #0f0f18;

    --text: #f1f5f9;
    --text-secondary: #94a3b8;
    --text-muted: #64748b;

    --glass-bg: rgba(255, 255, 255, 0.05);
    --glass-border: rgba(255, 255, 255, 0.08);
    --glass-blur: 20px;

    --font-display: 'Inter Tight', sans-serif;
    --font-body: 'Inter', sans-serif;

    --radius-sm: 8px;
    --radius-md: 16px;
    --radius-lg: 24px;
    --radius-xl: 32px;

    --shadow-sm: 0 2px 8px rgba(0,0,0,0.2);
    --shadow-md: 0 8px 32px rgba(0,0,0,0.2);
    --shadow-lg: 0 16px 48px rgba(0,0,0,0.3);
    --shadow-glow: 0 4px 24px rgba(var(--primary-rgb), 0.3);
}

/* ═══ Light mode override ═══ */
/* Descomentar se o briefing pedir light mode */
/*
:root {
    --bg: #fafafa;
    --bg-surface: rgba(0, 0, 0, 0.02);
    --bg-alt: #f1f5f9;
    --text: #0f172a;
    --text-secondary: #475569;
    --text-muted: #64748b;
    --glass-bg: rgba(255, 255, 255, 0.7);
    --glass-border: rgba(0, 0, 0, 0.06);
}
*/

/* ═══ RESET ═══ */
* { margin: 0; padding: 0; box-sizing: border-box; }

body {
    font-family: var(--font-body);
    background: var(--bg);
    color: var(--text);
    line-height: 1.7;
    overflow-x: hidden;
}

h1, h2, h3, h4 {
    font-family: var(--font-display);
    font-weight: 700;
    line-height: 1.2;
    color: var(--text);
}
h1 { font-size: clamp(2.2rem, 5vw, 3.5rem); letter-spacing: -0.02em; }
h2 { font-size: clamp(1.6rem, 3.5vw, 2.5rem); letter-spacing: -0.01em; }
h3 { font-size: 1.25rem; }

.container { max-width: 1100px; margin: 0 auto; padding: 0 24px; }

/* ═══ GRADIENT TEXT ═══ */
.gradient-text {
    background: linear-gradient(135deg, var(--primary), var(--accent));
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
}

/* ═══ GLASSMORPHISM ═══ */
.glass-card {
    background: var(--glass-bg);
    backdrop-filter: blur(var(--glass-blur));
    -webkit-backdrop-filter: blur(var(--glass-blur));
    border: 1px solid var(--glass-border);
    border-radius: var(--radius-lg);
    padding: 32px;
    box-shadow: var(--shadow-md);
    transition: all 0.3s ease;
}
.glass-card:hover {
    border-color: rgba(var(--primary-rgb), 0.2);
    box-shadow: var(--shadow-lg), 0 0 40px rgba(var(--primary-rgb), 0.05);
}

/* ═══ GRADIENT ORBS ═══ */
.orb {
    position: absolute;
    border-radius: 50%;
    filter: blur(80px);
    opacity: 0.25;
    pointer-events: none;
    will-change: transform;
}
.orb-1 { width: 400px; height: 400px; background: var(--primary); top: -100px; right: -100px; }
.orb-2 { width: 300px; height: 300px; background: var(--accent); bottom: -50px; left: -80px; }
.orb-3 { width: 350px; height: 350px; background: var(--primary); top: 50%; left: -120px; }

/* ═══ FLOATING NAVBAR ═══ */
.navbar {
    position: fixed;
    top: 16px; left: 16px; right: 16px;
    background: var(--glass-bg);
    backdrop-filter: blur(var(--glass-blur));
    -webkit-backdrop-filter: blur(var(--glass-blur));
    border: 1px solid var(--glass-border);
    border-radius: var(--radius-md);
    z-index: 100;
    padding: 12px 24px;
    transition: all 0.3s ease;
}
.navbar.scrolled {
    background: rgba(10, 10, 15, 0.9);
    box-shadow: var(--shadow-md);
}
.navbar-inner {
    display: flex; align-items: center; justify-content: space-between;
    max-width: 1100px; margin: 0 auto;
}
.navbar-logo {
    font-family: var(--font-display); font-weight: 800;
    font-size: 1.1rem; color: var(--text);
}
.navbar-cta {
    background: linear-gradient(135deg, var(--primary), var(--accent));
    color: #fff; padding: 8px 20px; border-radius: var(--radius-sm);
    text-decoration: none; font-weight: 600; font-size: 0.85rem;
    transition: all 0.3s;
}
.navbar-cta:hover { transform: translateY(-1px); box-shadow: var(--shadow-glow); }

/* ═══ HERO ═══ */
.hero {
    position: relative; padding: 140px 0 80px; overflow: hidden;
}
.hero-sub {
    font-size: 1.15rem; color: var(--text-secondary);
    max-width: 560px; margin-bottom: 32px; line-height: 1.8;
}

/* ═══ BADGE ═══ */
.badge {
    display: inline-block; padding: 6px 16px; border-radius: 50px;
    background: rgba(var(--primary-rgb), 0.1);
    border: 1px solid rgba(var(--primary-rgb), 0.2);
    color: var(--primary); font-size: 0.8rem; font-weight: 600;
    margin-bottom: 20px; letter-spacing: 0.5px;
}

/* ═══ CTA BUTTON ═══ */
.cta-premium {
    display: inline-block;
    background: linear-gradient(135deg, var(--primary), var(--accent));
    color: #fff; border: none; border-radius: var(--radius-sm);
    padding: 16px 40px; font-size: 1rem; font-weight: 700;
    cursor: pointer; text-decoration: none;
    transition: all 0.3s ease;
    box-shadow: 0 4px 24px rgba(var(--primary-rgb), 0.4);
    font-family: var(--font-body);
}
.cta-premium:hover {
    transform: translateY(-2px);
    box-shadow: 0 8px 32px rgba(var(--primary-rgb), 0.5);
}
.cta-premium.full-width { width: 100%; text-align: center; }

/* ═══ TRUST BAR ═══ */
.trust-bar {
    display: flex; gap: 24px; margin-top: 48px; flex-wrap: wrap;
}
.trust-item {
    display: flex; align-items: center; gap: 8px;
    color: var(--text-muted); font-size: 0.85rem;
}
.trust-item i { color: var(--primary); }

/* ═══ SECTIONS ═══ */
section { padding: 100px 0; position: relative; overflow: hidden; }
.section-alt { background: var(--bg-alt); }
.section-sub {
    color: var(--text-secondary); font-size: 1.05rem;
    max-width: 600px; margin-bottom: 48px; line-height: 1.8;
}

/* ═══ CARDS GRID ═══ */
.cards-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
    gap: 24px;
}

.icon {
    font-size: 28px; color: var(--primary); margin-bottom: 16px;
    display: inline-block;
}

/* ═══ FORM ═══ */
.section-form { background: var(--bg-alt); }
.form-card { max-width: 520px; margin: 0 auto; }

input, textarea, select {
    font-family: var(--font-body);
    width: 100%; padding: 14px 18px; margin-bottom: 16px;
    background: var(--bg-surface);
    border: 1px solid var(--glass-border);
    border-radius: var(--radius-sm);
    color: var(--text); font-size: 0.95rem;
    outline: none; transition: all 0.3s;
}
input::placeholder, textarea::placeholder { color: var(--text-muted); }
input:focus, textarea:focus, select:focus {
    border-color: var(--primary);
    box-shadow: 0 0 0 3px rgba(var(--primary-rgb), 0.15);
}

select {
    appearance: none;
    background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='12' height='12' viewBox='0 0 24 24' fill='none' stroke='%2394a3b8' stroke-width='2'%3E%3Cpath d='M6 9l6 6 6-6'/%3E%3C/svg%3E");
    background-repeat: no-repeat;
    background-position: right 16px center;
    padding-right: 40px;
}

.form-trust {
    text-align: center; font-size: 0.8rem;
    color: var(--text-muted); margin-top: 16px;
}

/* ═══ FOOTER ═══ */
.footer {
    padding: 40px 0; text-align: center;
    border-top: 1px solid var(--glass-border);
}
.footer-logo {
    font-family: var(--font-display); font-weight: 800;
    font-size: 1.2rem; margin-bottom: 8px; color: var(--text);
}
.footer-copy { font-size: 0.8rem; color: var(--text-muted); }

/* ═══ UTILITIES ═══ */
.text-center { text-align: center; }

/* ═══ SCROLL ANIMATIONS ═══ */
@keyframes fadeInUp {
    from { opacity: 0; transform: translateY(40px); }
    to { opacity: 1; transform: translateY(0); }
}
@keyframes fadeInScale {
    from { opacity: 0; transform: scale(0.92); }
    to { opacity: 1; transform: scale(1); }
}
@keyframes slideInLeft {
    from { opacity: 0; transform: translateX(-40px); }
    to { opacity: 1; transform: translateX(0); }
}
@keyframes slideInRight {
    from { opacity: 0; transform: translateX(40px); }
    to { opacity: 1; transform: translateX(0); }
}

[data-animate] { opacity: 0; }
[data-animate].is-visible {
    animation-fill-mode: both;
    animation-duration: 0.8s;
    animation-timing-function: cubic-bezier(0.22, 1, 0.36, 1);
}
[data-animate="fade-up"].is-visible    { animation-name: fadeInUp; }
[data-animate="fade-scale"].is-visible { animation-name: fadeInScale; }
[data-animate="slide-left"].is-visible { animation-name: slideInLeft; }
[data-animate="slide-right"].is-visible{ animation-name: slideInRight; }

/* Stagger */
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

/* ═══ REDUCED MOTION ═══ */
@media (prefers-reduced-motion: reduce) {
    *, *::before, *::after {
        animation-duration: 0.01ms !important;
        transition-duration: 0.01ms !important;
    }
    [data-animate] { opacity: 1 !important; }
    [data-stagger]>* { opacity: 1 !important; }
}

/* ═══ RESPONSIVE ═══ */
@media (max-width: 768px) {
    section { padding: 64px 0; }
    .hero { padding: 120px 0 60px; }
    .cards-grid { grid-template-columns: 1fr; }
    .trust-bar { flex-direction: column; gap: 12px; }
    .cta-premium { width: 100%; text-align: center; }
    .navbar { top: 8px; left: 8px; right: 8px; padding: 10px 16px; }
    .orb { display: none; }  /* Hide orbs on mobile for performance */
}

@media (max-width: 480px) {
    h1 { font-size: 1.8rem; }
    .glass-card { padding: 20px; }
}
```

## Componentes de Referência

### Glass Card com Ícone

```html
<div class="glass-card">
    <i class="fas fa-shield-alt icon"></i>
    <h3>[Título]</h3>
    <p>[Descrição com copy real do wireframe-tabela]</p>
</div>
```

### Gradient Text em Headline

```html
<h1>Pare de perder leads com <span class="gradient-text">páginas genéricas</span></h1>
```

### Badge de Contexto

```html
<span class="badge">🚀 [Marca] · [Produto/Serviço]</span>
```

### Seção com Orbs

```html
<section class="section-alt">
    <div class="orb orb-2"></div>
    <div class="container">
        <h2 data-animate="fade-up">[Headline]</h2>
        <!-- conteúdo -->
    </div>
</section>
```

### Grid com Stagger

```html
<div class="cards-grid" data-animate="fade-up" data-stagger>
    <div class="glass-card">...</div>
    <div class="glass-card">...</div>
    <div class="glass-card">...</div>
</div>
```

## Design System — Paletas de Referência

Usar quando o cliente não fornecer paleta de cores:

### Dark Mode (Default)

| Setor | Primary | Accent | Background |
|-------|---------|--------|------------|
| **Tech/SaaS** | `#6366f1` (indigo) | `#a855f7` (purple) | `#0a0a0f` |
| **Fintech** | `#06b6d4` (cyan) | `#3b82f6` (blue) | `#0a0f1a` |
| **Saúde** | `#10b981` (emerald) | `#6ee7b7` (mint) | `#0a0f12` |
| **Educação** | `#f59e0b` (amber) | `#f97316` (orange) | `#0f0a05` |
| **Arquitetura** | `#f1f5f9` (slate) | `#d4a853` (gold) | `#0a0a0a` |
| **Jurídico** | `#1e40af` (blue) | `#3b82f6` (blue) | `#050a15` |
| **Varejo** | `#ef4444` (red) | `#f97316` (orange) | `#0f0505` |

### Light Mode

| Setor | Primary | Accent | Background |
|-------|---------|--------|------------|
| **Tech/SaaS** | `#4f46e5` (indigo) | `#7c3aed` (violet) | `#fafafa` |
| **Beleza/Spa** | `#ec4899` (pink) | `#d946ef` (fuchsia) | `#fdf2f8` |
| **Saúde** | `#059669` (emerald) | `#10b981` (green) | `#f0fdf4` |
| **Consultoria** | `#1e40af` (blue) | `#6366f1` (indigo) | `#f8fafc` |

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
| Crescimento | `fa-rocket`, `fa-chart-bar`, `fa-arrow-up` |
