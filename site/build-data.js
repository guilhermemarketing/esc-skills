#!/usr/bin/env node
/**
 * Build script: Reads all SKILL.md files from ../skills/ and generates skills-data.js
 * with extracted metadata for the showcase website.
 */

const fs = require('fs');
const path = require('path');

const SKILLS_DIR = path.join(__dirname, '..', 'skills');
const OUTPUT_FILE = path.join(__dirname, 'skills-data.js');

// Category mapping based on skill name patterns and keywords
const CATEGORY_RULES = [
  { id: 'ads', label: '📣 Ads & PPC', icon: '📣', match: (name, desc) => /(-ads|ad-creative|google-ads|meta-ads)/.test(name) },
  { id: 'analytics', label: '📈 Analytics & Tracking', icon: '📈', match: (name, desc) => /(-gtm-|analytics|tracking)/.test(name) },
  { id: 'cro', label: '🎯 CRO & LPO', icon: '🎯', match: (name, desc) => /(-landing-page|-pricing-page|wireframe-landing)/.test(name) || name === 'pricing-page' },
  { id: 'seo', label: '🔍 SEO', icon: '🔍', match: (name, desc) => name === 'seo' },
  { id: 'design', label: '🎨 Design & UI', icon: '🎨', match: (name, desc) => /^(ui-ux|frontend-|css-|responsive-|interaction-|progressive-)/.test(name) || name === 'figma-implement-design' || name.includes('design-system') },
  { id: 'animation', label: '⚡ Animation', icon: '⚡', match: (name, desc) => /^(gsap|animejs|threejs-|vantajs|matterjs|3d-|animation-)/.test(name) },
  { id: 'architecture', label: '🏗️ Architecture', icon: '🏗️', match: (name, desc) => /^(component-|domain-|decomposition-|technical-|tlc-)/.test(name) },
  { id: 'deploy', label: '🚀 Deploy', icon: '🚀', match: (name, desc) => /(-deploy|^cloudflare-|^netlify-|^render-|^vercel-)/.test(name) },
  { id: 'security', label: '🔒 Security', icon: '🔒', match: (name, desc) => name.startsWith('security-') },
  { id: 'performance', label: '📊 Performance', icon: '📊', match: (name, desc) => /^(perf-|core-web-|web-quality-)/.test(name) },
  { id: 'devops', label: '🛠 DevOps & CI', icon: '🛠', match: (name, desc) => /^(nx-|gh-|run-nx-)/.test(name) || name === 'sentry' },
  { id: 'docs', label: '📝 Docs & Planning', icon: '📝', match: (name, desc) => /^(docs-|skill-creator|subagent-creator|cursor-)/.test(name) },
  { id: 'integrations', label: '🔌 Integrations', icon: '🔌', match: (name, desc) => /^(figma|confluence-|jira-|feedback-|guimkt-make-)/.test(name) },
  { id: 'development', label: '💻 Development', icon: '💻', match: (name, desc) => /^(javascript-|coding-|best-practices|playwright-)/.test(name) },
  { id: 'cloud', label: '☁️ Cloud', icon: '☁️', match: (name, desc) => name.startsWith('aws-') },
];

const FEATURED_SKILLS = [
  'guimkt-classic-ad-creative', 'guimkt-classic-ad-creative-final',
  'guimkt-design-system-extractor', 'guimkt-google-ads',
  'guimkt-gtm-expert', 'guimkt-gtm-expert-template', 'guimkt-landing-page',
  'guimkt-landing-page-optimization', 'guimkt-make-blueprint-expert', 'guimkt-meta-ads',
  'skill-creator', 'ui-ux-pro-max', 'guimkt-wireframe-landing-page'
];

// Extra categories for skills that belong to multiple categories
const EXTRA_CATEGORIES = {
  'guimkt-classic-ad-creative-final': [
    { id: 'copywriting', label: '✍️ Copywriting', icon: '✍️' },
    { id: 'design', label: '🎨 Design', icon: '🎨' }
  ],
  'guimkt-google-ads': [
    { id: 'copywriting', label: '✍️ Copywriting', icon: '✍️' }
  ],
  'guimkt-meta-ads': [
    { id: 'copywriting', label: '✍️ Copywriting', icon: '✍️' },
    { id: 'design', label: '🎨 Design', icon: '🎨' }
  ],
  'guimkt-landing-page': [
    { id: 'design', label: '🎨 Design & UI', icon: '🎨' }
  ],
  'guimkt-wireframe-landing-page': [
    { id: 'design', label: '🎨 Design & UI', icon: '🎨' }
  ]
};

function parseFrontmatter(content) {
  const match = content.match(/^---\n([\s\S]*?)\n---/);
  if (!match) return { name: '', description: '' };
  
  const yamlBlock = match[1];
  const lines = yamlBlock.split('\n');
  
  let name = '';
  let description = '';
  let collectingDesc = false;
  
  for (let i = 0; i < lines.length; i++) {
    const line = lines[i];
    
    // Extract name
    const nameMatch = line.match(/^name:\s*(.+)$/);
    if (nameMatch) {
      name = nameMatch[1].trim().replace(/^["']|["']$/g, '');
      continue;
    }
    
    // Start of description
    const descInlineMatch = line.match(/^description:\s*(.+)$/);
    if (descInlineMatch) {
      const val = descInlineMatch[1].trim();
      if (val === '>' || val === '|') {
        // Multiline folded/literal — collect indented lines
        collectingDesc = true;
        continue;
      }
      // Single-line description
      description = val.replace(/^["']|["']$/g, '');
      continue;
    }
    
    // Collecting multiline description lines
    if (collectingDesc) {
      if (line.match(/^\s+/)) {
        description += (description ? ' ' : '') + line.trim();
      } else {
        collectingDesc = false;
      }
    }
  }
  
  return { name, description };
}

function getCategory(name, description) {
  for (const rule of CATEGORY_RULES) {
    if (rule.match(name, description)) {
      return { id: rule.id, label: rule.label, icon: rule.icon };
    }
  }
  return { id: 'other', label: '📦 Other', icon: '📦' };
}

function getBodyPreview(content, maxLen = 300) {
  // Remove frontmatter
  const body = content.replace(/^---\n[\s\S]*?\n---\n*/, '').trim();
  // Get first meaningful paragraph (skip # headers)
  const lines = body.split('\n');
  let preview = '';
  for (const line of lines) {
    if (line.startsWith('#')) continue;
    if (line.trim() === '') continue;
    if (line.startsWith('```')) break;
    if (line.startsWith('---')) continue;
    preview += line.trim() + ' ';
    if (preview.length > maxLen) break;
  }
  return preview.trim().substring(0, maxLen);
}

function countFiles(skillDir) {
  let count = 0;
  function walk(dir) {
    const entries = fs.readdirSync(dir, { withFileTypes: true });
    for (const entry of entries) {
      if (entry.isFile()) count++;
      else if (entry.isDirectory()) walk(path.join(dir, entry.name));
    }
  }
  walk(skillDir);
  return count;
}

// Load existing translations and EN overrides from previous build
let existingOverrides = {};
try {
  const existingContent = fs.readFileSync(OUTPUT_FILE, 'utf-8');
  const match = existingContent.match(/const SKILLS_DATA = (\[[\s\S]*?\n\]);/);
  if (match) {
    const existingSkills = JSON.parse(match[1]);
    for (const s of existingSkills) {
      existingOverrides[s.slug] = {
        shortDescription: s.shortDescription,
        shortDescriptionPt: s.shortDescriptionPt,
        descriptionPt: s.descriptionPt
      };
    }
    console.log(`📖 Loaded ${Object.keys(existingOverrides).length} existing overrides`);
  }
} catch (e) { /* No existing file — skip */ }

// Build
const skillDirs = fs.readdirSync(SKILLS_DIR, { withFileTypes: true })
  .filter(d => d.isDirectory())
  .map(d => d.name)
  .sort();

const skills = [];

for (const dirName of skillDirs) {
  const skillPath = path.join(SKILLS_DIR, dirName, 'SKILL.md');
  if (!fs.existsSync(skillPath)) continue;
  
  const content = fs.readFileSync(skillPath, 'utf-8');
  const { name, description } = parseFrontmatter(content);
  const category = getCategory(name || dirName, description);
  const preview = getBodyPreview(content);
  const fileCount = countFiles(path.join(SKILLS_DIR, dirName));
  const isFeatured = FEATURED_SKILLS.includes(name || dirName);
  
  // Short description: first sentence or first 120 chars
  let shortDesc = description;
  const firstSentence = description.match(/^[^.!?]+[.!?]/);
  if (firstSentence && firstSentence[0].length < 150) {
    shortDesc = firstSentence[0];
  } else if (description.length > 120) {
    shortDesc = description.substring(0, 120) + '…';
  }
  
  const skillName = name || dirName;
  const extraCats = EXTRA_CATEGORIES[skillName] || [];
  const existing = existingOverrides[dirName] || {};

  // Use existing EN shortDescription if available (preserves manual translations)
  const finalShortDesc = existing.shortDescription || shortDesc;

  skills.push({
    slug: dirName,
    name: skillName,
    description,
    shortDescription: finalShortDesc,
    shortDescriptionPt: existing.shortDescriptionPt || undefined,
    descriptionPt: existing.descriptionPt || undefined,
    preview,
    category,
    extraCategories: extraCats.length > 0 ? extraCats : undefined,
    fileCount,
    isFeatured,
    githubUrl: `https://github.com/guilhermemarketing/esc-skills/tree/main/skills/${dirName}`
  });
}

// Generate categories list (including extra categories)
const categoriesMap = {};
for (const s of skills) {
  // Count primary category
  if (!categoriesMap[s.category.id]) {
    categoriesMap[s.category.id] = { ...s.category, count: 0 };
  }
  categoriesMap[s.category.id].count++;
  // Count extra categories
  if (s.extraCategories) {
    for (const ec of s.extraCategories) {
      if (!categoriesMap[ec.id]) {
        categoriesMap[ec.id] = { ...ec, count: 0 };
      }
      categoriesMap[ec.id].count++;
    }
  }
}
const categories = Object.values(categoriesMap).sort((a, b) => b.count - a.count);

const output = `// Auto-generated by build-data.js — do not edit manually
// Generated: ${new Date().toISOString()}

const SKILLS_DATA = ${JSON.stringify(skills, null, 2)};

const CATEGORIES = ${JSON.stringify(categories, null, 2)};

const TOTAL_SKILLS = ${skills.length};
const FEATURED_COUNT = ${skills.filter(s => s.isFeatured).length};
`;

fs.writeFileSync(OUTPUT_FILE, output, 'utf-8');
console.log(`✅ Generated ${OUTPUT_FILE}`);
console.log(`📦 ${skills.length} skills extracted`);
console.log(`🏆 ${skills.filter(s => s.isFeatured).length} featured`);
console.log(`📂 ${categories.length} categories:`);
categories.forEach(c => console.log(`   ${c.label}: ${c.count} skills`));
