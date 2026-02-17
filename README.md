<div align="center">

![BGPT Logo](https://bgpt.pro/static/logo_t.png)

# BGPT — Scientific Paper Search for AI

**Give your AI assistant access to real experimental data from thousands of scientific papers.**

[![MCP Compatible](https://img.shields.io/badge/MCP-Compatible-blue?style=for-the-badge)](https://modelcontextprotocol.io/)
[![Remote Server](https://img.shields.io/badge/Remote_Server-No_Install-brightgreen?style=for-the-badge)](#quick-start)
[![License: MIT](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)](LICENSE)
[![50 Free Searches](https://img.shields.io/badge/Free_Tier-50_Searches-orange?style=for-the-badge)](https://bgpt.pro/mcp)

[Live Page](https://bgpt.pro/mcp/) · [Get API Key](https://bgpt.pro/mcp) · [Report Issue](../../issues)

</div>

---

BGPT is a **remote MCP server** that gives AI assistants access to a curated database of scientific papers built from **full-text studies**. Unlike typical search tools that return titles and abstracts, BGPT extracts **raw experimental data** — methods, results, conclusions, quality scores, sample sizes, limitations, and **25+ metadata fields** per paper.

No install. No Docker. No build step. Just add one config block and start searching.

---

## Quick Start

Add BGPT to your MCP client — no installation, no API key needed for the free tier.

### Cursor

Add to your MCP settings (`.cursor/mcp.json` in your project root, or global settings):

```json
{
  "mcpServers": {
    "bgpt": {
      "url": "https://bgpt.pro/mcp/sse"
    }
  }
}
```

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

### Cline / Roo Code

Add to your Cline MCP settings:

```json
{
  "mcpServers": {
    "bgpt": {
      "url": "https://bgpt.pro/mcp/sse"
    }
  }
}
```

### Windsurf

Add to your `~/.codeium/windsurf/mcp_config.json`:

```json
{
  "mcpServers": {
    "bgpt": {
      "serverUrl": "https://bgpt.pro/mcp/sse"
    }
  }
}
```

### Any MCP Client

Connect to the SSE endpoint:

```
https://bgpt.pro/mcp/sse
```

**That's it.** Your AI assistant can now search scientific papers.

---

## What You Get

BGPT provides one powerful tool: **`search_papers`**

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `query` | string | Yes | Search terms (e.g. "CRISPR gene editing efficiency") |
| `num_results` | integer | No | Number of results (1–100, default 10) |
| `days_back` | integer | No | Only papers published within the last N days |
| `api_key` | string | No | Stripe subscription ID for paid tier |

### Returned Data

Each paper includes **25+ structured fields** extracted from the full text:

| Category | Fields |
|----------|--------|
| **Identifiers** | Title, DOI, authors, journal |
| **Core Data** | Methods, results, conclusions |
| **Quality** | Methodological rigor scores, limitations |
| **Metadata** | Sample sizes, study type, funding, conflicts of interest |

### Example Usage

Ask your AI assistant:

> "Search for recent papers on CAR-T cell therapy response rates"

BGPT returns structured experimental data your AI can reason over — not just a list of titles.

> "Find studies comparing mRNA vaccine efficacy published in the last 90 days"

> "Search for papers on gut microbiome and depression with large sample sizes"

---

## How It Works

```
Your AI (Cursor, Claude, Cline, etc.)
        │
        │  MCP Protocol (SSE)
        ▼
   ┌─────────────────────┐
   │  BGPT MCP Server    │
   │  bgpt.pro/mcp/sse   │
   └─────────┬───────────┘
             │
             ▼
   ┌─────────────────────┐
   │  BGPT Paper Database │
   │  Full-text extracted  │
   │  experimental data    │
   └─────────┬───────────┘
             │
             ▼
   Structured Results
   (methods, results, quality scores, 25+ fields)
```

BGPT is **fully hosted** — your MCP client connects via Server-Sent Events (SSE). No local processes, no dependencies.

---

## Use Cases

| Use Case | Description |
|----------|-------------|
| **Literature Reviews** | Survey a topic with real experimental data, not just abstracts |
| **Evidence Synthesis** | Ground AI responses in actual published findings |
| **Research Assistance** | Find papers by methodology, outcome, or recency |
| **Fact-Checking** | Verify claims against published experimental results |
| **Grant Writing** | Quickly gather supporting evidence for proposals |
| **Systematic Reviews** | Search with structured queries across the full corpus |

---

## Pricing

| Tier | Cost | Details |
|------|------|---------|
| **Free** | $0 | 50 searches per network — no API key needed |
| **Pay-as-you-go** | $0.01/result | Billed per result returned |

Get an API key at **[bgpt.pro/mcp](https://bgpt.pro/mcp)** to unlock unlimited searches.

---

## Configuration Reference

| Field | Value |
|-------|-------|
| **Protocol** | MCP (Model Context Protocol) |
| **Transport** | SSE (Server-Sent Events) |
| **Endpoint** | `https://bgpt.pro/mcp/sse` |
| **Auth** | None (free tier) / Stripe API key (paid) |
| **Tool** | `search_papers` |

---

## Documentation & Links

- **Live page & docs:** [bgpt.pro/mcp](https://bgpt.pro/mcp/)
- **API Key & billing:** [bgpt.pro/mcp](https://bgpt.pro/mcp)
- **MCP Protocol:** [modelcontextprotocol.io](https://modelcontextprotocol.io/)

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
