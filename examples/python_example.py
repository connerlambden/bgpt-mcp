#!/usr/bin/env python3
"""
Example: Search BGPT MCP API directly via HTTP (without an MCP client).

This shows how to call the BGPT search_papers tool using the MCP SSE protocol.
For normal usage, just add the SSE endpoint to your MCP client config — no code needed.
"""

import json
import urllib.request
import ssl

BGPT_SSE_ENDPOINT = "https://bgpt.pro/mcp/sse"


def search_papers(query: str, num_results: int = 5, days_back: int = None, api_key: str = None):
    """
    Search scientific papers via the BGPT MCP API.

    Args:
        query: Search terms (e.g. "CRISPR gene editing efficiency")
        num_results: Number of results to return (1-100, default 5)
        days_back: Only return papers published within the last N days
        api_key: Stripe subscription ID for paid access (optional for free tier)

    Returns:
        List of paper results with methods, results, quality scores, etc.
    """
    params = {"query": query, "num_results": num_results}
    if days_back is not None:
        params["days_back"] = days_back
    if api_key is not None:
        params["api_key"] = api_key

    payload = json.dumps({
        "jsonrpc": "2.0",
        "id": 1,
        "method": "tools/call",
        "params": {
            "name": "search_papers",
            "arguments": params
        }
    }).encode("utf-8")

    req = urllib.request.Request(
        BGPT_SSE_ENDPOINT.replace("/sse", "/message"),
        data=payload,
        method="POST"
    )
    req.add_header("Content-Type", "application/json")

    ctx = ssl.create_default_context()
    with urllib.request.urlopen(req, context=ctx, timeout=30) as resp:
        return json.loads(resp.read().decode("utf-8"))


if __name__ == "__main__":
    print("Searching for papers on 'CAR-T cell therapy response rates'...\n")

    results = search_papers("CAR-T cell therapy response rates", num_results=3)
    print(json.dumps(results, indent=2))
