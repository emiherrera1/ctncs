# CTNCS: Content Terminal Niche Classification Standard

A classification standard for digital content.

**Version:** v2.0
**Author:** Emily Herrera
**License:** Creative Commons Attribution 4.0 International (CC BY 4.0)
**Last updated:** October 2026

## What is CTNCS?

CTNCS classifies a single content release (a video, post, episode, or article) by subject and by structure. It gives researchers, creators, platforms, investors, and institutions a shared, stable code for what a piece of content is about and how it is made.

> If GICS is for industries and Dewey is for libraries, CTNCS is for content.

## Structure

The subject tree has four levels: Sector, Category, Niche, and Sub-Niche. Each Sub-Niche lists the formats common to it, and the Format must be one of those. A Release Number is optional.

| Segment | Level | Digits | Count (v2.0) |
|---|---|---|---|
| SS | Sector | 2 | 17 |
| CC | Category | 2 | 68 |
| NNN | Niche | 3 | 169 |
| SSS | Sub-Niche | 3 | 347 |
| FF | Format | 2 | 73 active (74 codes); 3 to 6 per Sub-Niche |
| RRR | Release Number (optional) | 3 | assigned by the dataset owner |

A Sub-Niche is a narrower subject within its Niche. It never names a format.

Each Sub-Niche lists 3 to 6 `common_formats`, and only those, plus six universal formats, are valid in its IDs. The universal formats wrap any subject: 08 Commentary, 10 Compilation, 22 Highlight, 62 Mashups, 66 Reaction, and 67 Parody (`universal = TRUE` in the Formats file). If a release's structure is not listed, use the closest listed format and record the actual structure in the `unlisted_format` metadata field, so the list can be reviewed at the next revision. Format 25 (Live) is retired; whether a release is live is recorded in the `release_mode` metadata field.

Each Sub-Niche also gives one example concept per common format, such as "Action Movie Review" under Blockbuster Films. Example concepts illustrate the codebook. They are not codes.

Sector 17 (Sensitive Topics) is recorded only in the `sensitive_topics` metadata field. It is never a primary or secondary path.

## ID format

```
SS.CC.NNN.SSS.FF(.RRR)
```

Validation regex:

```
^\d{2}\.\d{2}\.\d{3}\.\d{3}\.\d{2}(\.\d{3})?$
```

### Example

`03.08.127.253.07`

| Segment | Code | Meaning |
|---|---|---|
| Sector | 03 | Lifestyle |
| Category | 08 | Food & Cooking |
| Niche | 127 | Ready-Made Food |
| Sub-Niche | 253 | Fast Food |
| Format | 07 | Challenge |

## Files

| File | Contents |
|---|---|
| `CTNCS_Codebook_v2.0.csv` / `.tsv` | All 601 tree nodes (Levels 1 to 4), flat, with `code` and `parent_code` |
| `CTNCS_Codebook_v2.0_hier.json` | The same tree, nested |
| `CTNCS_Formats_v2.0.csv` | The 74 Format codes and definitions, with `status` (73 active, 1 retired) and `universal` (valid under every Sub-Niche) |
| `CTNCS_Metadata_v2.0.csv` | Release metadata fields (platform, made_for_kids, release_mode, secondary_path, sensitive_topics, unlisted_format, and others) |
| `v1.0/` | The September 2025 release, kept for reference |

### Codebook columns

| Column | Description |
|---|---|
| `taxonomy_version` | Release the row belongs to |
| `code` | Full dot-path code for the node |
| `parent_code` | Code of the immediate parent, formed by removing the last segment; blank for Sectors |
| `level` / `level_name` | 1 Sector, 2 Category, 3 Niche, 4 Sub-Niche |
| `label` / `definition` | Node name and definition |
| `common_formats` / `common_format_labels` | Sub-Niches only; the semicolon-separated Format codes and names valid for that Sub-Niche |
| `example_concepts` | Sub-Niches only; one example concept per common format, in the same order |
| `scope_note` | Inclusions, exclusions, and where neighboring content belongs |
| `sensitive_topics_only` | TRUE for Sector 17 nodes, which are recorded only in the `sensitive_topics` field |
| `added_in` | Release in which the node was first defined. `v1.0` includes nodes listed in the v1.0 codebook but first placed in the tree in v2.0 |

The flat files preserve the hierarchy through `parent_code`, so they can be loaded into any table or database.

## How to use CTNCS

1. Work top-down: choose the Sector, then the Category, Niche, and Sub-Niche that best describe the release's main subject.
2. Add one primary Format for how most of the runtime is structured, chosen from that Sub-Niche's common formats or the six universal formats. If the structure is not listed, use the closest listed format and record the actual one in `unlisted_format`.
3. Record `platform`, `made_for_kids`, and `release_mode` (1 live, 2 standing, 3 derivative).
4. If the release substantially engages with a Sensitive Topic, add the Sector 17 node to `sensitive_topics`.
5. Optionally record a secondary path, a secondary format, and other metadata fields. Metadata is stored next to the ID, never inside it.

To check the codebook or an ID, run `python3 tools/check_labels.py` or `python3 tools/check_labels.py --id 03.08.127.253.07`.

The full rules, decision chart, and worked examples are in the CTNCS Manual. An interactive explorer is at [classify.cvaccelerator.com](https://classify.cvaccelerator.com).

## Changes and requests

See [CHANGELOG.md](CHANGELOG.md). To propose a new node or report a problem, open an issue in this repository or email emily@cvaccelerator.com.

## How to cite CTNCS

Herrera, Emily. CTNCS: Content Terminal Niche Classification Standard, v2.0 (2026).
