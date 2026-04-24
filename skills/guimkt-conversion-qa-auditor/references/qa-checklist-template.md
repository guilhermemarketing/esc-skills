# Conversion QA Checklist — {{CLIENTE}}

Template de checklist. Copiar e adaptar ao contexto do cliente.

---

## 1. dataLayer

| # | Verificação | Comando/Ferramenta | Esperado | Status |
|---|-------------|-------------------|----------|--------|
| 1.1 | dataLayer existe na página | Console: `dataLayer` | Array presente | ☐ |
| 1.2 | Consent default dispara primeiro | Console: `dataLayer.filter(e => e[0] === 'consent')` | `consent default` antes de qualquer tag | ☐ |
| 1.3 | Evento `generate_lead` dispara no submit | Submeter formulário + verificar dataLayer | Objeto com `event: "generate_lead"` | ☐ |
| 1.4 | `lead_type` presente no evento | Inspecionar objeto do evento | `form_submit`, `whatsapp_click`, etc. | ☐ |
| 1.5 | `attribution_ids` presentes | Inspecionar objeto do evento | `gclid`, `fbclid`, `fbc`, `fbp` quando aplicável | ☐ |
| 1.6 | `user_data` presente (se consent granted) | Inspecionar objeto do evento | `email_address`, `phone_number` hasheados | ☐ |
| 1.7 | `conversion_value` presente | Inspecionar objeto do evento | Valor numérico > 0 | ☐ |
| 1.8 | `consent_state` presente | Inspecionar objeto do evento | Objeto com 4 sinais | ☐ |

### Comandos de Debug (Console)

```javascript
// Ver todo o dataLayer
console.table(dataLayer);

// Filtrar eventos de conversão
dataLayer.filter(function(e) { return e.event === 'generate_lead'; });

// Verificar consent
dataLayer.filter(function(e) { return e[0] === 'consent'; });

// Verificar UTMs capturados
dataLayer.filter(function(e) { return e.event === 'generate_lead'; }).map(function(e) { return { source: e.lead_source, medium: e.lead_medium, campaign: e.lead_campaign }; });
```

---

## 2. GA4

| # | Verificação | Ferramenta | Esperado | Status |
|---|-------------|-----------|----------|--------|
| 2.1 | GA4 Config tag dispara | GA4 DebugView | `page_view` aparece | ☐ |
| 2.2 | Property ID correto | Tag Assistant / Network tab | Corresponde ao property do cliente | ☐ |
| 2.3 | Eventos customizados aparecem | GA4 DebugView | `generate_lead`, `whatsapp_click`, etc. | ☐ |
| 2.4 | Parâmetros customizados recebidos | GA4 DebugView → click no evento | `lead_type`, `lead_source`, `conversion_value` | ☐ |
| 2.5 | Evento marcado como conversão | GA4 Admin → Events → Conversions | Toggle ativado para eventos primários | ☐ |
| 2.6 | Enhanced Measurement ativo | GA4 Admin → Data Streams | Scroll, outbound clicks, file downloads | ☐ |
| 2.7 | Data Stream conectado | GA4 Admin → Data Streams | Stream ativo, Measurement ID correto | ☐ |

### GA4 DebugView

1. Abrir GA4 → Admin → DebugView
2. Ativar debug no navegador:
   - GTM Preview Mode, OU
   - GA4 Debugger extension, OU
   - `gtag('config', 'G-XXXXX', { debug_mode: true })`
3. Navegar na LP e executar conversões
4. Verificar eventos aparecendo em tempo real no DebugView

---

## 3. Google Ads Conversion

| # | Verificação | Ferramenta | Esperado | Status |
|---|-------------|-----------|----------|--------|
| 3.1 | Conversion Linker tag presente | GTM Preview | Tag dispara em All Pages | ☐ |
| 3.2 | Conversion tag dispara no evento | GTM Preview | Dispara em `generate_lead` | ☐ |
| 3.3 | Conversion ID e Label corretos | GTM Preview → tag details | Corresponde ao Google Ads | ☐ |
| 3.4 | Conversion Value enviado | GTM Preview → tag details | Valor numérico presente | ☐ |
| 3.5 | Enhanced Conversions ativo | GTM Preview → tag details | user_data sendo enviado | ☐ |
| 3.6 | gclid sendo capturado | Console: verificar cookie `_gcl_aw` | Cookie presente após click em anúncio | ☐ |

---

## 4. Meta Pixel

| # | Verificação | Ferramenta | Esperado | Status |
|---|-------------|-----------|----------|--------|
| 4.1 | Pixel base dispara (PageView) | Meta Pixel Helper | `PageView` em todas as páginas | ☐ |
| 4.2 | Pixel ID correto | Meta Pixel Helper | Corresponde ao pixel do cliente | ☐ |
| 4.3 | Evento Lead dispara | Meta Pixel Helper | `Lead` no submit do formulário | ☐ |
| 4.4 | Parâmetros customizados | Meta Pixel Helper → detalhes | `value`, `currency`, `content_name` | ☐ |
| 4.5 | Advanced Matching ativo | Meta Pixel Helper | `em`, `ph` sendo enviados | ☐ |
| 4.6 | Sem erros de pixel | Meta Pixel Helper | Nenhum warning/error | ☐ |

---

## 5. Meta CAPI (Server-Side)

| # | Verificação | Ferramenta | Esperado | Status |
|---|-------------|-----------|----------|--------|
| 5.1 | Evento CAPI disparando | Stape GTM Helper / sGTM logs | Request para graph.facebook.com | ☐ |
| 5.2 | Event name correto | sGTM Debug / Stape logs | `Lead`, `CompleteRegistration` | ☐ |
| 5.3 | `event_id` deduplicado | Comparar client vs. server | Mesmo `event_id` em ambos | ☐ |
| 5.4 | `action_source` correto | sGTM tag config | `website` para eventos web | ☐ |
| 5.5 | User data presente | sGTM logs | `em`, `ph`, `fbc`, `fbp`, `fbclid` | ☐ |
| 5.6 | Test events recebidos | Meta Events Manager → Test Events | Eventos aparecendo com match quality | ☐ |

---

## 6. Hidden Fields (Formulário)

| # | Verificação | Ferramenta | Esperado | Status |
|---|-------------|-----------|----------|--------|
| 6.1 | Hidden fields existem no HTML | DevTools → Elements | Todos os campos do measurement plan | ☐ |
| 6.2 | UTMs preenchidos na chegada | DevTools → Elements após load | Valores preenchidos via script | ☐ |
| 6.3 | gclid/fbclid preenchidos | DevTools → Elements | Valor do cookie/URL param | ☐ |
| 6.4 | `form_url` preenchido | DevTools → Elements | URL da página atual | ☐ |
| 6.5 | `landing_page` preenchido | DevTools → Elements | URL de primeira entrada | ☐ |
| 6.6 | Dados enviados ao CRM | CRM → registro do lead | Todos os campos de atribuição presentes | ☐ |
| 6.7 | Persistência cross-page | Navegar entre páginas | UTMs mantidos via cookie | ☐ |

### Teste de Preenchimento

```
1. Abrir LP com UTMs de teste:
   ?utm_source=linkedin&utm_medium=cpc&utm_campaign=aw_leads_junho_teste&utm_content=ad_b_teste&utm_placement=feed_linkedin_teste&utm_adname=guimarketing_ad_teste&utm_adgroup=guimarketing_group_teste&utm_adset=guimarketing_set_teste&utm_term=termo_generico_teste&utm_source_platform=youtube_teste&form_url=landing_teste&matchtype=phrase&keyword=palavra_chave_teste&term=busca_teste&position=1&location=teste&device=mobile&gclid=TESTE-gclid-123&fbclid=TESTE-fbclid-123&fbc=fb.1.1111111111111.2222222222222&fbp=1111111111111.2222222222222&parceiro=guimarketing


2. Inspecionar hidden fields (DevTools → Elements → buscar "hidden")

3. Submeter formulário

4. Verificar no CRM se todos os campos chegaram
```

---

## 7. Consent Mode v2

| # | Verificação | Ferramenta | Esperado | Status |
|---|-------------|-----------|----------|--------|
| 7.1 | Default deny ativo | Console: verificar consent state | Todos negados antes do CMP | ☐ |
| 7.2 | CMP carrega corretamente | Visual: banner aparece | Banner de cookies visível | ☐ |
| 7.3 | Aceitar atualiza consent | Console: verificar consent update | `ad_storage: granted` etc. | ☐ |
| 7.4 | GA4 dispara pre-consent (pings) | Network tab: filtrar `collect` | Requests sem cookies | ☐ |
| 7.5 | GA4 tracking completo pós-consent | Network tab | Requests com cookies | ☐ |
| 7.6 | Meta Pixel respeita consent | Meta Pixel Helper | Não dispara pre-consent | ☐ |
| 7.7 | Tags condicionais no GTM | GTM Preview | Tags com consent check | ☐ |
| 7.8 | `wait_for_update` configurado | Console: primeiro consent push | `wait_for_update: 500` | ☐ |

### Comandos de Consent Debug

```javascript
// Verificar estado atual do consent
// (após CMP carregar)
document.cookie.split(';').filter(function(c) {
  return c.indexOf('consent') > -1 || c.indexOf('CookieConsent') > -1;
});

// Verificar consent no dataLayer
dataLayer.filter(function(e) { return e[0] === 'consent'; });
```

---

## 8. Server-Side Tags (sGTM)

| # | Verificação | Ferramenta | Esperado | Status |
|---|-------------|-----------|----------|--------|
| 8.1 | Container sGTM respondendo | Browser: `https://data.dominio.com/healthy` | Response 200 | ☐ |
| 8.2 | GA4 Client recebendo | Stape GTM Helper / sGTM Preview | Requests recebidos do client | ☐ |
| 8.3 | GA4 Server tag disparando | sGTM Preview Mode | Tag fired com sucesso | ☐ |
| 8.4 | Cookie Keeper ativo (Stape) | DevTools → Cookies | 1st party cookies com domínio correto | ☐ |
| 8.5 | Subdomínio first-party | DNS check | CNAME/A record apontando para sGTM | ☐ |
| 8.6 | SSL válido | Browser: verificar cadeado | Certificado válido no subdomínio | ☐ |
| 8.7 | GEO Headers ativos | Stape GTM Helper / sGTM Preview | Headers `X-GEO-Country`, `X-GEO-Region`, `X-GEO-City`, `X-GEO-PostalCode`, `X-GEO-Ipaddress` presentes nos requests | ☐ |
| 8.8 | GEO data populando Enhanced Conversions | sGTM tag config | Campos `city`, `region`, `postal_code`, `country` sendo preenchidos via GEO Headers para Google Ads e Meta CAPI | ☐ |
| 8.9 | Region-specific tags configuradas | GTM / sGTM | Tags com comportamento condicional por região geográfica (ex: consent rules LGPD vs. GDPR, pixel por país) | ☐ |

> **💡 GEO Headers (Stape):** O servidor sGTM (Stape ou equivalente) pode enriquecer requests com headers de geolocalização (`X-GEO-*`), permitindo preencher campos de localização para Enhanced Conversions sem depender do usuário. Docs: https://stape.io/solutions/geo-headers
>
> **💡 Region-Specific Tags:** GA4 e Google Ads Enhanced Conversions podem ter comportamento condicional por região (ex: consent rules diferentes por país, tags específicas por mercado). Docs: https://stape.io/blog/region-specific-tags-behaviour-in-google-tag-manager

---

## 9. UTM Preservation

| # | Verificação | Ferramenta | Esperado | Status |
|---|-------------|-----------|----------|--------|
| 9.1 | UTMs capturados na landing | Console: verificar cookies | Cookies com valores UTM | ☐ |
| 9.2 | UTMs persistem cross-page | Navegar para outra página | Cookies mantidos | ☐ |
| 9.3 | UTMs chegam no formulário | Submeter form em página interna | Hidden fields preenchidos | ☐ |
| 9.4 | UTMs no CRM | CRM → detalhes do lead | Campos de atribuição preenchidos | ☐ |
| 9.5 | WhatsApp redirect preserva | Clicar botão WA | dataLayer event antes do redirect | ☐ |

---

## 10. Offline Conversions Pipeline

| # | Verificação | Ferramenta | Esperado | Status |
|---|-------------|-----------|----------|--------|
| 10.1 | CRM registra attribution IDs | CRM → lead recente | gclid, fbclid, fbc, fbp presentes | ☐ |
| 10.2 | Status de lead rastreável | CRM → pipeline | Lead → MQL → SQL → Proposta → Venda | ☐ |
| 10.3 | Upload Google Ads funcionando | Google Ads → Conversions → Uploads | Import sem erros | ☐ |
| 10.4 | Upload Meta Offline Events | Meta Events Manager → Offline Events | Eventos recebidos com match quality | ☐ |
| 10.5 | Frequência de upload adequada | Verificar timestamps | Diária ou a cada 6h | ☐ |
| 10.6 | Valores de conversão corretos | Comparar CRM vs. plataforma | Valores correspondentes | ☐ |

---

## 11. Cross-Device & Mobile

| # | Verificação | Ferramenta | Esperado | Status |
|---|-------------|-----------|----------|--------|
| 11.1 | LP responsiva | DevTools → Device Mode | Layout correto em mobile | ☐ |
| 11.2 | Formulário funcional mobile | Testar submit em mobile | Submit com sucesso | ☐ |
| 11.3 | Hidden fields em mobile | DevTools mobile | Campos preenchidos | ☐ |
| 11.4 | WhatsApp link funcional | Clicar em mobile | Abre WhatsApp app | ☐ |
| 11.5 | CMP funcional em mobile | Visual | Banner usável, botão clicável | ☐ |
| 11.6 | Page speed mobile | Lighthouse mobile | Score > 70 | ☐ |

---

## Resultado do QA

### Score

```
Total de checks: [X]
Aprovados: [X] ✅
Reprovados: [X] ❌
Não aplicável: [X] ➖

Score: [X]% ([aprovados] / [total - não_aplicável])
```

### Classificação

| Score | Veredicto | Ação |
|-------|-----------|------|
| **90-100%** | ✅ **Pronto para launch** | Publicar com confiança |
| **70-89%** | ⚠️ **Launch com ressalvas** | Documentar gaps + timeline de correção |
| **0-69%** | 🚨 **Não lançar** | Corrigir itens críticos antes de publicar |

### Itens Críticos (bloqueantes)
```
Os seguintes itens reprovados IMPEDEM o lançamento:
- 1.3 (dataLayer generate_lead não dispara)
- 2.3 (GA4 não recebe eventos de conversão)
- 3.2 (Google Ads conversion tag não dispara)
- 4.3 (Meta Pixel Lead não dispara)
- 6.6 (CRM não recebe campos de atribuição)
- 7.1 (Consent default não está ativo)
```
