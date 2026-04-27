---
name: bgpt-mcp
author: "BGPT"
description: "How to use BGPT MCP to search scientific papers and retrieve structured experimental data including methods, results, sample sizes, conflicts of interest, limitations, reproducibility scores, and falsifiability criteria. Use this skill when the user asks to find scientific evidence, search the literature, evaluate research quality, check reproducibility, surface study limitations or conflicts of interest, retrieve raw experimental data, or build evidence-grounded AI workflows. Also trigger when the user references PubMed, arXiv, biorxiv, medrxiv, systematic reviews, evidence-based medicine, GRADE, or critical appraisal."
---

# BGPT MCP — Scientific Paper Search with Structured Critical Appraisal

BGPT is a remote [Model Context Protocol](https://modelcontextprotocol.io/) (MCP) server that searches a database of scientific papers built from full-text studies. Unlike typical search tools that return titles and abstracts, BGPT extracts **raw experimental data** along with 25+ structured fields per paper.

## When to Use

Use BGPT whenever the user asks to:

- Find scientific papers on a topic
- Evaluate research quality, reproducibility, or COI
- Surface limitations, blindspots, or falsifiability criteria of studies
- Retrieve methods, sample sizes, populations, or experimental techniques
- Build an evidence-grounded answer that requires citing primary literature
- Compare evidence across multiple studies with quality signals

## Setup

Add BGPT to the MCP client config — no API key needed for the free tier (50 free results, then $0.02/result).

**Claude Desktop / Cursor / any MCP client (SSE):**

```json
{
  "mcpServers": {
    "bgpt": {
      "url": "https://bgpt.pro/mcp/sse"
    }
  }
}
```

**Streamable HTTP** (alternative): `https://bgpt.pro/mcp/stream`

## Tool: `search_papers`

The single tool exposed by BGPT.

**Input:**
- `query` (string, required) — natural-language description of what to search for. Examples: `"CRISPR base editing in vivo delivery 2024"`, `"semaglutide cardiovascular outcomes"`, `"transformer attention sparse activations"`.

**Output (per paper):**

Each result is a paper with these structured fields:

- `title`, `authors`, `journal`, `year`, `doi`, `url`
- `abstract`
- `methods_and_experimental_techniques`
- `results_and_conclusions`
- `sample_size_and_population`
- `study_context`
- `paper_limitations_and_biases`
- `study_blindspots` — confounders the authors did not examine
- `how_to_falsify` — what evidence would disprove the paper's claims
- `conflict_of_interest`
- `funding_json`
- `data_availability_statements`
- `code_and_data_links`
- `quality_scores` — calibrated 0-10 scores for: scientific rigor, novelty, generality, usefulness, reproducibility, depth

## Best Practices

1. **Cite the structured fields, not just the abstract.** When summarizing a paper, surface the `paper_limitations_and_biases`, `study_blindspots`, and `conflict_of_interest` fields in the response so the user gets calibrated context.
2. **Use `quality_scores.reproducibility` to triage.** When multiple papers conflict, prefer the higher reproducibility score and note the difference.
3. **For systematic reviews and clinical questions**, leverage `sample_size_and_population` to filter underpowered studies.
4. **For methods-heavy questions** (replication, technique comparison), focus on `methods_and_experimental_techniques`.
5. **Always show `how_to_falsify` when the user asks "is X true?"** — the falsification criterion is the test the claim should pass.
6. **Always disclose `conflict_of_interest`** when summarizing pharma, nutrition, or industry-funded research.

## Example Workflows

### Evidence-graded literature search

User: *"What's the evidence for time-restricted eating on cardiovascular outcomes?"*

Use `search_papers("time-restricted eating cardiovascular outcomes RCT")`. From results, return a comparative table that includes for each paper: sample size, primary outcome, reproducibility score, and disclosed COI/funding.

### Critical appraisal

User: *"Is paper X reliable?"*

Search for the paper title. Surface `paper_limitations_and_biases`, `study_blindspots`, `how_to_falsify`, and `quality_scores`. State the falsification criterion explicitly.

### Replicability check

User: *"Has this finding replicated?"*

Search the original finding, then search for follow-up replications. Compare `quality_scores.reproducibility` across studies and surface methodological differences from `methods_and_experimental_techniques`.

## Pricing

- 50 free searches per network (no API key needed)
- $0.02 per result thereafter (API key from https://bgpt.pro/mcp)

## Links

- Site: https://bgpt.pro/mcp
- npm: https://www.npmjs.com/package/bgpt-mcp
- Source: https://github.com/connerlambden/bgpt-mcp
