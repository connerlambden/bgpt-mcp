# BGPT MCP API

**Search scientific papers from Claude, Cursor, or any MCP-compatible AI tool.**

BGPT is a remote [Model Context Protocol](https://modelcontextprotocol.io/) (MCP) server that gives AI assistants access to a database of scientific papers built from full-text studies. Unlike typical search tools that return titles and abstracts, BGPT extracts **raw experimental data** — methods, results, conclusions, quality scores, sample sizes, limitations, and 25+ metadata fields per paper.

[![MCP Compatible](https://img.shields.io/badge/MCP-Compatible-blue)](https://modelcontextprotocol.io/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

---

## Quick Start

Add BGPT to your MCP client in **one line** — no install, no API key required for the free tier.

### Claude Desktop

Add to your `claude_desktop_config.json`:

```json
{
  "mcpServers": {
    "bgpt": {
      "url": "https://bgpt.pro/mcp/sse"
    }
  }
}
```

### Cursor

Add to your MCP settings (`.cursor/mcp.json`):

```json
{
  "mcpServers": {
    "bgpt": {
      "url": "https://bgpt.pro/mcp/sse"
    }
  }
}
```

### Any MCP Client

Connect to the SSE endpoint:

```
https://bgpt.pro/mcp/sse
```

That's it. No Docker, no npm, no build step.

---

## What You Get

BGPT provides one tool: **`search_papers`**

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `query` | string | Yes | Search terms (e.g. "CRISPR gene editing efficiency") |
| `num_results` | integer | No | Number of results to return (1–100, default 10) |
| `days_back` | integer | No | Only return papers published within the last N days |
| `api_key` | string | No | Your Stripe subscription ID for paid access |

### What comes back

Each paper result includes **25+ fields**, extracted from the full text:

- **Title & DOI** — standard identifiers
- **Methods** — experimental design, techniques used
- **Results** — raw findings, measurements, statistical outcomes
- **Conclusions** — what the authors determined
- **Quality scores** — methodological rigor assessment
- **Sample sizes** — participant/specimen counts
- **Limitations** — acknowledged weaknesses
- **And more** — funding, conflicts of interest, study type, etc.

### Example

Ask your AI assistant:

> "Search for recent papers on CAR-T cell therapy response rates"

BGPT returns structured experimental data your AI can reason over — not just a list of titles.

---

## Pricing

| Tier | Cost | Details |
|------|------|---------|
| **Free** | $0 | 50 searches, no API key needed |
| **Pay-as-you-go** | $0.01/result | Billed per result returned. Get an API key at [bgpt.pro/mcp](https://bgpt.pro/mcp) |

---

## How It Works

```
Your AI Assistant (Claude, Cursor, etc.)
        │
        │  MCP Protocol (SSE)
        ▼
   BGPT MCP Server
   https://bgpt.pro/mcp/sse
        │
        │  search_papers(query, ...)
        ▼
   BGPT Paper Database
   (full-text extracted data)
        │
        ▼
   Structured Results
   (methods, results, quality scores, 25+ fields)
```

BGPT is a **hosted remote server** — your MCP client connects via Server-Sent Events (SSE). No local installation needed.

---

## Use Cases

- **Literature reviews** — Ask your AI to survey a topic with real experimental data
- **Evidence synthesis** — Ground AI responses in actual study findings
- **Research assistance** — Find papers by methodology, outcome, or recency
- **Fact-checking** — Verify claims against published experimental results
- **Grant writing** — Quickly gather supporting evidence for proposals

---

## Configuration Reference

### Server Details

| Field | Value |
|-------|-------|
| Protocol | MCP (Model Context Protocol) |
| Transport | SSE (Server-Sent Events) |
| Endpoint | `https://bgpt.pro/mcp/sse` |
| Authentication | None required (free tier) / Stripe API key (paid) |

### Full MCP Client Config

```json
{
  "mcpServers": {
    "bgpt": {
      "url": "https://bgpt.pro/mcp/sse"
    }
  }
}
```

---

## Documentation

Full documentation, FAQ, and setup guides: **[bgpt.pro/mcp](https://bgpt.pro/mcp/)**

---

## Support

- **Email:** [contact@bgpt.pro](mailto:contact@bgpt.pro)
- **Issues:** [GitHub Issues](../../issues)
- **API Key / Billing:** [bgpt.pro/mcp](https://bgpt.pro/mcp)

---

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines on reporting bugs, requesting features, and contributing.

---

## License

This repository (documentation, examples, and configuration files) is licensed under the [MIT License](LICENSE).

The BGPT MCP API service itself is operated by BGPT and subject to its own [terms of service](https://bgpt.pro/mcp/).
