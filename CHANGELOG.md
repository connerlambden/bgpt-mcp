# Changelog

All notable changes to the BGPT MCP API will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).

## [1.0.0] - 2026-02-17

### Added
- Initial public release of BGPT MCP API
- `search_papers` tool with query, num_results, days_back, and api_key parameters
- SSE transport at `https://bgpt.pro/mcp/sse`
- Free tier: 50 searches with no API key required
- Pay-as-you-go: $0.01 per result with Stripe API key
- 25+ metadata fields per paper result (methods, results, conclusions, quality scores, etc.)
- Compatible with Claude Desktop, Cursor, Claude Code, and any MCP client
