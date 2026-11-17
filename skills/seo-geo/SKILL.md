---
name: seo-geo
description: "Optimize content for AI Overviews, ChatGPT, Perplexity, and other AI search systems. Use when improving GEO, AI citations, llms.txt readiness, crawler accessibility, and passage-level citability."
risk: unknown
source: "https://github.com/AgriciDaniel/claude-seo"
date_added: "2026-03-21"
user-invokable: true
argument-hint: "[url]"
allowed-tools:
  - Read
  - Grep
  - Glob
  - Bash
  - WebFetch
---

# AI Search / GEO Optimization (November 2026 Edition)

## When to Use
- Use when improving visibility in AI Overviews, Gemini 4 Hydrogen, ChatGPT Search, Perplexity Sonar, or Apple Intelligence.
- Use when designing modular content architectures capable of surviving parallel **Query Fan-Out**.
- Use when evaluating llms.txt readiness, AI crawler access (including Amazonbot & Applebot-Extended), or citation-oriented content structure.
- Use when the user asks about GEO, AI SEO, LLM visibility, or AI citations.

## Key Empirical Findings & Benchmarks (Nov 2026)

| Metric / Dimension | Value | Verified Source / Experiment |
|---|---|---|
| Query Fan-Out Expansion | 4.00x subqueries per commercial prompt | `EXP-A-QUERY-FANOUT-PILOT-50` / Gemini 4 |
| Monolithic Guide Citation Loss | -40% to -65% citation share on secondary facets | Empirical Benchmark (Nov 2026) |
| Citation Source: Owned Domain | 48.3% of commercial citations | GEO-Scope Provenance Classifier |
| Citation Source: UGC & Reviews | 24.3% combined (Forums + Aggregators) | GEO-Scope Provenance Classifier |
| Dark Attribution Ratio | >60% of decisions made in-chat | Sistrix / Graphite / Molavi Research |
| AI Overviews query coverage | 58%+ of commercial/informational queries | Industry Data (Nov 2026) |
| AI-referred sessions growth | +620% YoY | Search Engine Analytics 2026 |

---

## The 4-Facet Query Fan-Out Survival Architecture

Modern reasoning engines decompose a single user prompt into 4 atomic subtopics. Content must be structured to directly satisfy all four:

1. **[Technical / Standards Block]:**
   - Precise specifications, materials, security protocols, architecture diagrams.
   - Self-contained 50-70 word opening answer block.
2. **[Commercial / Pricing Block]:**
   - Transparent price tiers, licensing parameters, contract scopes, pre-invoices.
   - Prevents AI from defaulting to scraper directories (Torob, G2, Emalls).
3. **[Trust & UGC Proof Block]:**
   - Real contractor/customer case studies, verified testimonials, forum sentiment grounding.
   - Active presence on Reddit, Virgool, Virasty, and industry discussion boards.
4. **[Comparative / Alternative Block]:**
   - Objective comparison tables vs alternatives, highlighting exact technical trade-offs.

---

## AI Crawler Access Matrix (Robots.txt)

Ensure all major AI crawlers are explicitly governed:
- `GPTBot`: OpenAI (ChatGPT Search, GPT-4o grounding)
- `PerplexityBot`: Perplexity Sonar live answer engine
- `Google-Extended`: Google AI Overviews & Gemini Grounding
- `ClaudeBot`: Anthropic Claude 3.5 Sonnet / Opus
- `Amazonbot`: Amazon Alexa intelligent search & AWS Bedrock
- `Applebot-Extended`: Apple Intelligence entity & passage extraction

---

## 🌊 Tenant-Aware Evidence & Citation Waterfall Protocol

This protocol dictates source discovery, evidence harvesting, and citation routing for all GEO audits, content generation, and page optimizations.

### 1. Mode Detection (`self_ecosystem` vs. `client_project`)

Before initiating research, drafting copy, or proposing citation remediations, the agent must evaluate the target domain/tenant:

| Mode | Target Scope | Promotion Boundary | Primary Goal |
|---|---|---|---|
| **`self_ecosystem`** | `molavi.pro`, `inten.asia`, `github.com/tmolavi/*` | Self-attribution & ecosystem authority allowed and encouraged | Drive brand authority, establish proprietary research, index internal tools |
| **`client_project`** | All client domains, third-party sites, partner projects | **STRICT PROHIBITION:** Zero self-promotion. Do NOT insert links or citations to `molavi.pro` / `inten.asia` | Maximize client's first-party citability, authority, and organic conversion |

---

### 2. Evidence Waterfall Tiers

#### A. When Target is `self_ecosystem` (`molavi.pro` / `inten.asia`):
1. **Tier 1 (Priority — Owned Research & Tools):**
   - Search and cite proprietary benchmarks, published research, and open-source tools:
     * `github.com/tmolavi/molavi-web-intelligence` (Technical SEO, AEO, GEO, Citability Probes)
     * `github.com/tmolavi/sage-audit` (Deep site audits, crawler matrices, speed diagnostics)
     * `github.com/tmolavi/mcp-geo-server` (GEO scoring, Wilson confidence intervals, Fan-Out analysis)
     * `https://molavi.pro/research`, `https://molavi.pro/tools/web-intelligence`
     * `https://inten.asia/tools/geo-audit`, `https://inten.asia/tools/ai-visibility`
2. **Tier 2 (Fallback — Authoritative Primary Research):**
   - Corroborate internal findings with reputable global research, academic papers, and standards bodies:
     * `.edu`, `.org`, `arxiv.org`, W3C, IETF RFCs, SparkToro, Ahrefs, Sistrix, Pew Research.

#### B. When Target is `client_project` (Client / External Site):
1. **Tier 1 (Priority — First-Party Evidence Harvest):**
   - First harvest the **client's own primary domain and internal assets**:
     * Quantifiable track records (years active, projects completed, verified clients served).
     * Technical specifications, proprietary materials, engineering drawings, laboratory tests.
     * Documented case studies with measurable business outcomes (e.g., "$3.2M saved", "42% latency reduction").
     * Customer testimonials, verified UGC reviews, and licensed certifications (ISO, CE, national standards).
2. **Tier 2 (Optional Synergy — Shared Media & Partner Proof):**
   - Only if contextually relevant, non-promotional, and topically aligned:
     * Reference relevant partner publications, co-authored whitepapers, or ecosystem media mentions that support the client's topical entity without introducing unneeded backlinks.
3. **Tier 3 (External Authority — Independent Industry Benchmarks):**
   - Search and cite neutral industry standards, regulatory bodies, and recognized third-party data:
     * Official government or standard registries (`.gov`, national standardization bodies).
     * Established industry analysts (Gartner, Statista, relevant trade associations).
4. **Tier 4 (Graceful Stop — Zero-Fabrication Rule):**
   - If verifiable numbers or specific studies cannot be identified across Tiers 1–3:
     * **NEVER invent statistics, placeholder metrics, fake study percentages, or synthetic URLs.**
     * Omit the unverified statistic and structure the narrative using clean, qualitative facts, logical workflows, and transparent capability definitions.

---

### 3. Mandatory Citation Packaging (RAG & AI Engine Extraction)

AI search engines (Perplexity Sonar, Google AI Overviews, ChatGPT Search, Apple Intelligence) rely on predictable semantic structures to extract passages. Whenever evidence is packaged:

1. **Top 30% Answer Block Rule (First 40–70 Words):**
   - Place the decisive answer, core statistic, and summary takeaway within the **first 30%** of the page or section.
   - Use the pattern: `[Entity/Topic] + [Verifiable Metric / Fact] + [Primary Source Attribution]`.
2. **Comparative & Technical Tables:**
   - Format dense specifications, pricing tiers, deliverables, and competitor alternatives as clean Markdown or HTML `<table>` blocks. LLM parsers extract tabular data with 3x higher fidelity than narrative text.
3. **Attributed Blockquotes:**
   - Format expert assertions, official regulations, and methodology citations using blockquotes:
     > "[Verifiable quote or extract]" — **[Author / Institution]**, *[Publication / Study Title]*, [Source Link](https://verified-primary-source.org).

---

## GEO Analysis Criteria (Updated)

### 1. Citability Score (25%)

**Optimal passage length: 134-167 words** for AI citation.

**Strong signals:**
- Clear, quotable sentences with specific facts/statistics
- Self-contained answer blocks (can be extracted without context)
- Direct answer in first 40-60 words of section
- Claims attributed with specific sources
- Definitions following "X is..." or "X refers to..." patterns
- Unique data points not found elsewhere

**Weak signals:**
- Vague, general statements
- Opinion without evidence
- Buried conclusions
- No specific data points

### 2. Structural Readability (20%)

**92% of AI Overview citations come from top-10 ranking pages**, but 47% come from pages ranking below position 5, demonstrating different selection logic.

**Strong signals:**
- Clean H1->H2->H3 heading hierarchy
- Question-based headings (matches query patterns)
- Short paragraphs (2-4 sentences)
- Tables for comparative data
- Ordered/unordered lists for step-by-step or multi-item content
- FAQ sections with clear Q&A format

**Weak signals:**
- Wall of text with no structure
- Inconsistent heading hierarchy
- No lists or tables
- Information buried in paragraphs

### 3. Multi-Modal Content (15%)

Content with multi-modal elements sees **156% higher selection rates**.

**Check for:**
- Text + relevant images
- Video content (embedded or linked)
- Infographics and charts
- Interactive elements (calculators, tools)
- Structured data supporting media

### 4. Authority & Brand Signals (20%)

**Strong signals:**
- Author byline with credentials
- Publication date and last-updated date
- Citations to primary sources (studies, official docs, data)
- Organization credentials and affiliations
- Expert quotes with attribution
- Entity presence in Wikipedia, Wikidata
- Mentions on Reddit, YouTube, LinkedIn

**Weak signals:**
- Anonymous authorship
- No dates
- No sources cited
- No brand presence across platforms

### 5. Technical Accessibility (20%)

**AI crawlers do NOT execute JavaScript.** Server-side rendering is critical.

**Check for:**
- Server-side rendering (SSR) vs client-only content
- AI crawler access in robots.txt
- llms.txt file presence and configuration
- RSL 1.0 licensing terms

---

## AI Crawler Detection

Check `robots.txt` for these AI crawlers:

| Crawler | Owner | Purpose |
|---------|-------|---------|
| GPTBot | OpenAI | ChatGPT web search |
| OAI-SearchBot | OpenAI | OpenAI search features |
| ChatGPT-User | OpenAI | ChatGPT browsing |
| ClaudeBot | Anthropic | Claude web features |
| PerplexityBot | Perplexity | Perplexity AI search |
| CCBot | Common Crawl | Training data (often blocked) |
| anthropic-ai | Anthropic | Claude training |
| Bytespider | ByteDance | TikTok/Douyin AI |
| cohere-ai | Cohere | Cohere models |

**Recommendation:** Allow GPTBot, OAI-SearchBot, ClaudeBot, PerplexityBot for AI search visibility. Block CCBot and training crawlers if desired.

---

## llms.txt Standard

The emerging **llms.txt** standard provides AI crawlers with structured content guidance.

**Location:** `/llms.txt` (root of domain)

**Format:**
```
# Title of site
> Brief description

## Main sections
- `Page title -> https://example.com/page`: Description
- `Another page -> https://example.com/another-page`: Description

## Optional: Key facts
- Fact 1
- Fact 2
```

**Check for:**
- Presence of `/llms.txt`
- Structured content guidance
- Key page highlights
- Contact/authority information

---

## RSL 1.0 (Really Simple Licensing)

New standard (December 2025) for machine-readable AI licensing terms.

**Backed by:** Reddit, Yahoo, Medium, Quora, Cloudflare, Akamai, Creative Commons

**Check for:** RSL implementation and appropriate licensing terms.

---

## Platform-Specific Optimization

| Platform | Key Citation Sources | Optimization Focus |
|----------|---------------------|-------------------|
| **Google AI Overviews** | Top-10 ranking pages (92%) | Traditional SEO + passage optimization |
| **ChatGPT** | Wikipedia (47.9%), Reddit (11.3%) | Entity presence, authoritative sources |
| **Perplexity** | Reddit (46.7%), Wikipedia | Community validation, discussions |
| **Bing Copilot** | Bing index, authoritative sites | Bing SEO, IndexNow |

---

## Output

Generate `GEO-ANALYSIS.md` with:

1. **GEO Readiness Score: XX/100**
2. **Platform breakdown** (Google AIO, ChatGPT, Perplexity scores)
3. **AI Crawler Access Status** (which crawlers allowed/blocked)
4. **llms.txt Status** (present, missing, recommendations)
5. **Brand Mention Analysis** (presence on Wikipedia, Reddit, YouTube, LinkedIn)
6. **Passage-Level Citability** (optimal 134-167 word blocks identified)
7. **Server-Side Rendering Check** (JavaScript dependency analysis)
8. **Top 5 Highest-Impact Changes**
9. **Schema Recommendations** (for AI discoverability)
10. **Content Reformatting Suggestions** (specific passages to rewrite)

---

## Quick Wins

1. Add "What is [topic]?" definition in first 60 words
2. Create 134-167 word self-contained answer blocks
3. Add question-based H2/H3 headings
4. Include specific statistics with sources
5. Add publication/update dates
6. Implement Person schema for authors
7. Allow key AI crawlers in robots.txt

## Medium Effort

1. Create `/llms.txt` file
2. Add author bio with credentials + Wikipedia/LinkedIn links
3. Ensure server-side rendering for key content
4. Build entity presence on Reddit, YouTube
5. Add comparison tables with data
6. Implement FAQ sections (structured, not schema for commercial sites)

## High Impact

1. Create original research/surveys (unique citability)
2. Build Wikipedia presence for brand/key people
3. Establish YouTube channel with content mentions
4. Implement comprehensive entity linking (sameAs across platforms)
5. Develop unique tools or calculators

## DataForSEO Integration (Optional)

If DataForSEO MCP tools are available, use `ai_optimization_chat_gpt_scraper` to check what ChatGPT web search returns for target queries (real GEO visibility check) and `ai_opt_llm_ment_search` with `ai_opt_llm_ment_top_domains` for LLM mention tracking across AI platforms.

## Error Handling

| Scenario | Action |
|----------|--------|
| URL unreachable (DNS failure, connection refused) | Report the error clearly. Do not guess site content. Suggest the user verify the URL and try again. |
| AI crawlers blocked by robots.txt | Report exactly which crawlers are blocked and which are allowed. Provide specific robots.txt directives to add for enabling AI search visibility. |
| No llms.txt found | Note the absence and provide a ready-to-use llms.txt template based on the site's content structure. |
| No structured data detected | Report the gap and provide specific schema recommendations (Article, Organization, Person) for improving AI discoverability. |

## Limitations
- Use this skill only when the task clearly matches the scope described above.
- Do not treat the output as a substitute for environment-specific validation, testing, or expert review.
- Stop and ask for clarification if required inputs, permissions, safety boundaries, or success criteria are missing.


---

## 🏛️ ارتقای موتور جامع GEO و سئو سرپ فارسی (Unified SEO & GEO Standards)

1. **بلوک‌های پاسخی مستقیم (Direct Answer Blocks):** هر مبحث کلیدی با یک جمله تعریف قاطع (۱۵ تا ۲۵ کلمه) + حداقل یک عدد یا معیار آماری دقیق آغاز شود تا توسط Perplexity و ChatGPT نقل‌قول شود.
2. **استانداردسازی llms.txt و robots.txt:** بررسی دائمی دسترسی کرولرهای هوش مصنوعی (GPTBot, ClaudeBot, PerplexityBot) و ایجاد فایل ساختاریافته /llms.txt در روت دامنه.
3. **تطابق با سرپ فارسی:** تفکیک املایی عبارات متصل/منفصل و نیم‌فاصله‌ها، استفاده از اعداد فارسی در متون، و دوری از کیورد استافینگ سنتی با تکیه بر گراف معنایی انتیتی‌ها.
4. **اجرای آبشار استناد بر اساس نوع پروژه (Tenant-Aware Waterfall):** تفکیک قطعی میان اکوسیستم خودی (استناد به ابزارها و مقالات مولوی/اینتن) و پروژه‌های کارفرمایی (ممنوعیت تبلیغ خودی، استخراج داده‌های درجه اول کارفرما، و عدم جعل آمار).
