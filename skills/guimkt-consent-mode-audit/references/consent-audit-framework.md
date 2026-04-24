# Consent Audit Framework

Especificações técnicas para auditoria de Consent Mode v2, CMP e LGPD.

## Consent Mode v2 — Sinais e Estados

### Os 7 Sinais de Consent

| Sinal | Controla | Default Recomendado |
|-------|---------|:-------------------:|
| `ad_storage` | Cookies de publicidade (_gcl_aw, _gac) | `denied` |
| `ad_user_data` | Envio de dados do usuário para ads | `denied` |
| `ad_personalization` | Remarketing e personalização | `denied` |
| `analytics_storage` | Cookies de analytics (_ga, _gid) | `denied` |
| `functionality_storage` | Cookies funcionais (idioma, chat) | `granted` |
| `personalization_storage` | Cookies de personalização (recomendações) | `denied` |
| `security_storage` | Cookies de segurança (CSRF, auth) | `granted` |

### Consent Mode: Básico vs Avançado

| Aspecto | Básico | Avançado |
|---------|--------|---------|
| Tags bloqueadas sem consent | ✅ Sim | ✅ Sim |
| Pings cookieless enviados | ❌ Não | ✅ Sim |
| Modelagem de conversões | ❌ Não | ✅ Sim |
| Modelagem de comportamento | ❌ Não | ✅ Sim |
| Requer CMP Partner certificada | ❌ Não | ✅ Sim |
| Perda de dados estimada | ~60-80% | ~20-30% |

### Implementação Técnica

#### Consent Default (deve ser PRIMEIRO no GTM)

```javascript
// Via gtag (inline no <head>, ANTES do GTM)
gtag('consent', 'default', {
  'ad_storage': 'denied',
  'ad_user_data': 'denied',
  'ad_personalization': 'denied',
  'analytics_storage': 'denied',
  'functionality_storage': 'granted',
  'personalization_storage': 'denied',
  'security_storage': 'granted',
  'wait_for_update': 500,
  'regions': ['BR']
});

// Via GTM: Tag tipo "Consent Initialization - All Pages"
// Tipo: Google Tag > Consent Initialization
```

#### Consent Update (enviado pela CMP)

```javascript
// Exemplo após usuário aceitar analytics + marketing:
gtag('consent', 'update', {
  'ad_storage': 'granted',
  'ad_user_data': 'granted',
  'ad_personalization': 'granted',
  'analytics_storage': 'granted'
});
```

---

## Tags: Comportamento por Estado de Consent

### Google Tags

| Tag | Consent Necessário | Com Denied | Com Granted |
|-----|:------------------:|------------|-------------|
| GA4 Config | `analytics_storage` | Pings sem cookie, consent_mode pings | Tracking completo |
| Google Ads Conversion | `ad_storage` + `ad_user_data` | Conversion modeling (avançado) | Conversion tracking completo |
| Google Ads Remarketing | `ad_storage` + `ad_personalization` | NÃO dispara | Remarketing ativo |
| Conversion Linker | `ad_storage` | NÃO grava cookie | Grava _gcl_aw, _gac |
| Floodlight | `ad_storage` | Modeling (avançado) | Tracking completo |

### Non-Google Tags

| Tag | Consent Necessário | Com Denied | Com Granted |
|-----|:------------------:|------------|-------------|
| Meta Pixel | `ad_storage` | **DEVE NÃO disparar** | Dispara normalmente |
| Meta CAPI (server) | `ad_storage` (parcial) | Dispara SEM user_data | Dispara COM user_data hashed |
| LinkedIn Insight | `ad_storage` | **DEVE NÃO disparar** | Dispara normalmente |
| TikTok Pixel | `ad_storage` | **DEVE NÃO disparar** | Dispara normalmente |
| Pinterest Tag | `ad_storage` | **DEVE NÃO disparar** | Dispara normalmente |
| Hotjar/Clarity | `analytics_storage` | **DEVE NÃO disparar** | Dispara normalmente |
| Google Optimize | `analytics_storage` | Não personaliza | Personaliza |

> **⚠️ IMPORTANTE:** Tags non-Google NÃO têm Consent Mode nativo. A proteção depende de:
> 1. **Consent-aware triggers** no GTM (trigger com condição de consent), ou
> 2. **Built-in consent settings** do GTM (configuração de consent por tag)

---

## CMP: Requisitos e Certificação

### Requisitos Mínimos

```
□ Banner aparece no primeiro acesso
□ Botão "Aceitar" e "Rejeitar" igualmente visíveis
□ Opção de granularidade (analytics vs marketing)
□ Link para gerenciar preferências (footer ou ícone fixo)
□ Integração com GTM Consent Mode (envia consent update)
□ Cookie scan atualizado (todos os cookies classificados)
□ Política de privacidade linkada no banner
□ Funciona em mobile (banner não quebra)
□ Persiste escolha (não re-pergunta a cada visita)
□ Permite revogação a qualquer momento
```

### CMPs Certificadas pelo Google (Consent Mode v2 Avançado)

| CMP | Certificada | Notas |
|-----|:----------:|-------|
| Cookiebot (Cybot) | ✅ | Popular no BR, boa integração GTM |
| OneTrust | ✅ | Enterprise, mais complexa |
| Usercentrics | ✅ | Boa UX, popular na EU |
| CookieYes | ✅ | Acessível, boa para PMEs |
| Iubenda | ✅ | LGPD-friendly, popular no BR |
| Didomi | ✅ | Enterprise, multi-regulação |
| Quantcast | ✅ | Foco EU/GDPR |
| TrustArc | ✅ | Enterprise |
| Complianz | ⚠️ | WordPress plugin, verificar versão |
| LGPD Framework (custom) | ❌ | Sem certificação, modo básico only |

---

## LGPD: Requisitos Aplicáveis a Sites de Marketing

### Base Legal para Cookies

| Tipo de Cookie | Base Legal LGPD | Nota |
|----------------|:---------------:|------|
| Necessários (session, CSRF) | Legítimo interesse (Art. 7, IX) | Não precisa consent |
| Analytics (GA4) | Consentimento (Art. 7, I) | Precisa opt-in |
| Marketing (Pixel, Ads) | Consentimento (Art. 7, I) | Precisa opt-in |
| Funcionais (idioma) | Legítimo interesse ou consentimento | Depende do uso |

### Checklist LGPD para Sites

```
□ Política de Privacidade atualizada (Art. 9)
  - Lista de cookies com finalidade e duração
  - Base legal para cada tratamento
  - Direitos do titular (acesso, correção, exclusão)
  - Contato do Encarregado/DPO
  - Compartilhamento com terceiros documentado

□ Consentimento válido (Art. 8)
  - Livre (sem coerção ou cookie wall)
  - Informado (usuário sabe o que aceita)
  - Inequívoco (ação afirmativa, não inação)
  - Finalidade específica (não genérico)
  - Granular (pode aceitar uns e rejeitar outros)

□ Revogação (Art. 8, §5)
  - Mecanismo simples para retirar consentimento
  - Igualmente fácil quanto dar consentimento
  - Efetivo (cookies realmente removidos)

□ Registro de Consentimento (Art. 8, §2)
  - CMP registra data/hora do consentimento
  - Logs disponíveis para auditoria
  - Retenção do registro adequada
```

---

## Critérios de Scoring

### Consent Mode v2 (25 pontos)

| Critério | Pontos |
|----------|:------:|
| Default denied configurado para todos os sinais | 8 |
| Wait_for_update configurado (500-2000ms) | 2 |
| Consent update disparando após CMP choice | 8 |
| Modo avançado ativo (cookieless pings) | 5 |
| Regions configurado (BR e/ou EU) | 2 |

### CMP (25 pontos)

| Critério | Pontos |
|----------|:------:|
| CMP presente e funcional | 8 |
| Google CMP Partner certificada | 5 |
| Botões Aceitar/Rejeitar equilibrados | 4 |
| Granularidade de categorias | 3 |
| Cookie scan atualizado | 3 |
| Link de gerenciamento no footer | 2 |

### Tags & Disparos (25 pontos)

| Critério | Pontos |
|----------|:------:|
| GA4 comportamento correto com denied | 5 |
| Google Ads comportamento correto com denied | 5 |
| Meta Pixel NÃO dispara com denied | 5 |
| Outros pixels NÃO disparam com denied | 5 |
| Consent granted restaura tracking completo | 5 |

### LGPD Compliance (25 pontos)

| Critério | Pontos |
|----------|:------:|
| Política de Privacidade presente e atualizada | 5 |
| Consentimento livre e informado | 5 |
| Sem dark patterns | 5 |
| Revogação simples e funcional | 5 |
| Registro de consentimento (logs) | 5 |
