# sentiment-monitor

> AI-powered public opinion monitoring and structured report generation skill for AI assistant platforms.

AI 驱动的舆情监控与结构化报告生成技能，适用于 AI 助手平台。

## Overview

This skill enables AI assistants to perform automated public opinion (sentiment) monitoring for celebrities, TV shows, brands, and other public-facing entities. It collects publicly available information from web searches, analyzes sentiment distribution, identifies key events, and generates a polished HTML report.

## Features

- **Multi-source data collection** — Gathers data from public web sources (news, social media, search engines)
- **Sentiment analysis** — Classifies public opinion into positive, neutral, and negative categories
- **Event timeline** — Identifies and chronologically orders major public opinion events
- **Platform analysis** — Evaluates presence and performance across major social platforms
- **Risk assessment** — Flags potential reputation risks with severity levels
- **Actionable recommendations** — Provides short, medium, and long-term operational advice
- **Professional HTML report** — Outputs a responsive, styled HTML report with embedded CSS

## How It Works

1. **Parameter extraction** — Identifies the monitoring target and time range from user input
2. **Data collection** — Uses web search tools to gather public information across multiple dimensions
3. **Analysis** — Performs sentiment classification, event identification, and risk evaluation
4. **Report generation** — Produces a structured HTML report using the bundled template

## File Structure

```
sentiment-monitor/
├── SKILL.md                          # Skill definition and instructions
├── README.md                         # This file
├── LICENSE                           # MIT License
├── SECURITY.md                       # Security and privacy documentation
├── .gitignore                        # Git ignore rules
├── assets/                           # Static assets directory (reserved)
│   └── .gitkeep
└── references/
    └── report_template.html          # HTML report template with inline CSS
```

## Requirements

This skill requires the AI assistant platform to provide the following built-in tools:

| Tool | Purpose | Required |
|------|---------|----------|
| WebSearch | Search public web for sentiment data | Yes |
| WebFetch | Fetch detailed content from web pages | Yes |
| Write | Write HTML report file | Yes |
| preview_url | Preview the generated HTML report | Recommended |
| deliver_attachments | Send report file to user | Recommended |

## Security & Privacy

- **Public data only** — All data is collected from publicly available web sources
- **No personal data** — Does not access, collect, or use any private or personal information
- **No external dependencies** — Zero third-party packages or libraries required
- **No network exfiltration** — Data is only written to the user's local workspace
- **No credentials required** — Does not request or store any API keys or secrets

See [SECURITY.md](SECURITY.md) for detailed security documentation.

## Installation

Install via ClawHub:

```bash
npx clawhub@latest install sentiment-monitor
```

Or manually place this directory in your AI assistant's skills folder.

## Usage Examples

```
"帮我跑一下张凌赫的舆情监测"
"肖战口碑怎么样"
"这个月XX的舆论分析"
"生成XX品牌30天舆情报告"
```

## Version History

- **v0.3.0** — Security hardening, added README/LICENSE/SECURITY.md, reduced scan false positives
- **v0.2.0** — Added prerequisites section, privacy statement, removed PDF dependency
- **v0.1.0** — Initial release

## License

This project is licensed under the MIT License. See [LICENSE](LICENSE) for details.
