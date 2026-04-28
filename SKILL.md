---
name: sentiment-monitor
version: "0.3.0"
license: MIT
description: >
  Public opinion monitoring and structured report generation.
  Collects publicly available web information about celebrities, TV shows, or brands,
  performs sentiment analysis, and generates responsive HTML reports.
  Trigger keywords: sentiment, public opinion, reputation, monitoring report.
  Examples: "monitor reputation of X", "public opinion analysis for X".
---

# Public Opinion Monitoring & Report Generation

This skill provides a structured methodology for monitoring and analyzing public sentiment about public-facing entities (celebrities, entertainment products, brands) using publicly available web information.

## Purpose & Scope

- **Input**: A target entity name and optional time range
- **Output**: A self-contained HTML report with sentiment analysis, event timeline, and actionable recommendations
- **Data sources**: Public web pages, news articles, social media (public content only)
- **Output format**: HTML file with embedded CSS (no external dependencies)

## Prerequisites

This skill is designed for AI assistant platforms that provide the following built-in tools:

| Tool | Role | Required |
|------|------|----------|
| WebSearch | Retrieve public web information | Yes |
| WebFetch | Read detailed web page content | Yes |
| Write | Save the generated HTML report | Yes |
| preview_url | Display the HTML report preview | Optional |
| deliver_attachments | Deliver the report file to the user | Optional |

> This skill has **zero external dependencies**. It does not install packages,
> execute scripts, access system files, or communicate with external servers.

## Privacy & Data Policy

- All data comes from **publicly accessible web sources** only
- No private data, personal information, or non-public content is accessed
- Aggregate statistics (e.g., view counts, play counts) are only collected when publicly displayed
- Missing data is labeled as "Data Unavailable" in reports — **no data is fabricated or estimated**
- Reports are saved to the user's local workspace; no data leaves the local environment

## Trigger Conditions

This skill activates when user requests include keywords related to:
- Public opinion, sentiment, reputation monitoring
- Celebrity or brand image analysis
- Media coverage or buzz tracking

## Supported Monitoring Targets

- **Entertainment figures**: Actors, musicians, influencers
- **Media products**: TV series, films, variety shows
- **Brands and products**: Consumer brands, product launches

## Workflow

### Phase 1: Parameter Identification

Extract from the user request:

| Parameter | Default | Description |
|-----------|---------|-------------|
| Target | User-specified | Name of the entity to monitor |
| Time range | Last 30 days | Customizable by user |
| Output format | HTML | Only HTML format is supported |
| Focus areas | All dimensions | Fan data, reputation events, platform activity, risk alerts |

### Phase 2: Public Information Gathering

The AI assistant gathers information from publicly accessible web sources across these dimensions:

**Basic data** (3-5 searches recommended):
- Recent news coverage
- Trending topics and hot searches
- Public reviews and discussions
- Fan community statistics
- Cross-platform activity metrics

**Event identification**:
- Positive events: product releases, awards, charity work
- Negative events: controversies, criticism, backlash
- For each event: timestamp, platform, sentiment direction

**Platform metrics** (when publicly available):
- Social media trending status and view counts
- Video play counts and engagement
- Discussion volume indicators

> **Important**: Only data obtainable through public web searches should be used.
> If specific numerical data is unavailable, the report should indicate "Data Unavailable".

### Phase 3: Analysis

**3.1 Sentiment Classification**
Categorize the overall public opinion into:
- Positive proportion (favorable coverage, support, enthusiasm)
- Neutral proportion (objective reporting, general discussion)
- Negative proportion (criticism, controversy, backlash)

**3.2 Event Timeline**
Organize major events chronologically (minimum 5 events), including:
- Event name and description
- Timestamp
- Sentiment direction (positive / neutral / negative)
- Impact level (high / medium / low)

**3.3 Risk Assessment**
Identify current or potential reputation risks:
- Active negative sentiment trends
- Sensitive topics that may escalate
- Competitive disadvantages

### Phase 4: Report Generation

Generate a complete HTML report using the template at `references/report_template.html`.

**File naming**: `{target_name}{days}day_sentiment_report_{YYYYMMDD}.html`

**Report sections**:

The report includes these modules:

1. **Header** — Title, monitoring period, generation date
2. **KPI Overview** — Overall sentiment score (0-100), positive/neutral/negative ratios, event count, active platforms
3. **Sentiment Distribution** — Visual bar chart and trend description
4. **Event Timeline** — Chronological list with sentiment and impact tags
5. **Platform Performance** — Cross-platform activity comparison
6. **Risk Assessment Matrix** — Current risks with severity and recommendations
7. **Operational Recommendations** — Short-term (1-2 weeks), mid-term (1 month), long-term (3+ months)
8. **Disclaimer** — Data source clarification

**Style specifications** (matching the template):
- Embedded CSS only, no external stylesheets
- Responsive layout for mobile viewing
- Color scheme: primary #1a1a2e, secondary #16213e, accent #0f3460
- Sentiment colors: positive #27ae60, negative #e74c3c, neutral #f39c12
- System font stack: -apple-system, "PingFang SC", "Microsoft YaHei", sans-serif

### Phase 5: Delivery

1. Save the HTML report using the Write tool
2. Display the report preview using preview_url (if available)
3. Deliver the file using deliver_attachments (if available)
4. If tools are unavailable, provide the file path for manual access

## Guidelines

- All data must originate from public web sources — fabrication is strictly prohibited
- Unavailable data must be clearly marked as "Data Unavailable"
- Time ranges are calculated automatically based on the current date
- Sentiment analysis should be evidence-based, avoiding subjective assumptions
- Reports should maintain objectivity, presenting multiple viewpoints for controversial events
- Sensitive political content should be avoided in reports
