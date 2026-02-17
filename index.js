#!/usr/bin/env node

/**
 * BGPT MCP Server — Search scientific papers from any AI tool.
 *
 * This is a thin wrapper that connects to the remote BGPT MCP server
 * via mcp-remote. It enables installation via npx/npm for any MCP client.
 *
 * Usage:
 *   npx bgpt-mcp
 *
 * Or add to your MCP client config:
 *   { "command": "npx", "args": ["-y", "bgpt-mcp"] }
 *
 * Learn more: https://bgpt.pro/mcp/
 */

const { spawn } = require("child_process");
const path = require("path");

const BGPT_SSE_URL = "https://bgpt.pro/mcp/sse";

const mcpRemoteBin = path.join(
  __dirname,
  "node_modules",
  ".bin",
  "mcp-remote"
);

const child = spawn(mcpRemoteBin, [BGPT_SSE_URL], {
  stdio: "inherit",
  env: process.env,
});

child.on("error", (err) => {
  if (err.code === "ENOENT") {
    console.error(
      "mcp-remote not found. Install dependencies: npm install"
    );
    process.exit(1);
  }
  console.error("Failed to start BGPT MCP:", err.message);
  process.exit(1);
});

child.on("exit", (code) => {
  process.exit(code ?? 0);
});

process.on("SIGINT", () => child.kill("SIGINT"));
process.on("SIGTERM", () => child.kill("SIGTERM"));
