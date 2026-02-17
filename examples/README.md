# Examples

## MCP Client Configs

Copy-paste these config files into your MCP client:

| Client | Config File | Where to Put It |
|--------|------------|-----------------|
| Claude Desktop | [`claude_desktop_config.json`](claude_desktop_config.json) | `~/Library/Application Support/Claude/claude_desktop_config.json` (macOS) or `%APPDATA%\Claude\claude_desktop_config.json` (Windows) |
| Cursor | [`cursor_mcp.json`](cursor_mcp.json) | `.cursor/mcp.json` in your project root |

## Direct API Usage

- [`python_example.py`](python_example.py) — Call BGPT directly via HTTP (no MCP client needed)

## Sample Prompts

Once BGPT is connected, try asking your AI:

- "Search for recent papers on CRISPR gene editing efficiency"
- "Find studies about mRNA vaccine immune responses published in the last 90 days"
- "What are the latest findings on gut microbiome and depression?"
- "Search for clinical trials on GLP-1 receptor agonists for weight loss"
- "Find papers comparing transformer models for protein structure prediction"
