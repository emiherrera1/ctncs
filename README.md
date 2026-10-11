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

The subject tree has four levels. Format is an independent facet. Content Instance is optional.

| Segment | Level | Digits | Count (v2.0) |
|---|---|---|---|
| SS | Sector | 2 | 17 |
| CC | Category | 2 | 68 |
| NNN | Niche | 3 | 169 |
| SSS | Content Style | 3 | 347 |
| FF | Format | 2 | 73 active (74 codes) |
| III | Content Instance (optional) | 3 | assigned by the dataset owner |

Any Content Style may take any active Format. Format 25 (Live) is retired; whether a release is live is recorded in the `release_mode` metadata field. Each Content Style lists `typical_formats` as guidance, not as a constraint.

Sector 17 (Sensitive Topics) is recorded only in the `sensitive_topics` metadata field. It is never a primary or secondary path.

## ID format

```
SS.CC.NNN.SSS.FF(.III)
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
| Niche | 127 | Taste Tests |
| Content Style | 253 | Fast Food Challenges |
| Format | 07 | Challenge |

## Files

| File | Contents |
|---|---|
| `CTNCS_Codebook_v2.0.csv` / `.tsv` | All 601 tree nodes (Levels 1 to 4), flat, with `code` and `parent_code` |
| `CTNCS_Codebook_v2.0_hier.json` | The same tree, nested |
| `CTNCS_Formats_v2.0.csv` | The 74 Format codes and definitions, with `status` (73 active, 1 retired) |
| `CTNCS_Metadata_v2.0.csv` | Release metadata fields (platform, made_for_kids, release_mode, secondary_path, sensitive_topics, and others) |
| `v1.0/` | The September 2025 release, kept for reference |

### Codebook columns

| Column | Description |
|---|---|
| `taxonomy_version` | Release the row belongs to |
| `code` | Full dot-path code for the node |
| `parent_code` | Code of the immediate parent, formed by removing the last segment; blank for Sectors |
| `level` / `level_name` | 1 Sector, 2 Category, 3 Niche, 4 Content Style |
| `label` / `definition` | Node name and definition |
| `typical_formats` / `typical_format_labels` | Content Styles only; semicolon-separated Format codes and names |
| `scope_note` | Inclusions, exclusions, and where neighboring content belongs |
| `sensitive_topics_only` | TRUE for Sector 17 nodes, which are recorded only in the `sensitive_topics` field |
| `added_in` | Release in which the node was first defined. `v1.0` includes nodes listed in the v1.0 codebook but first placed in the tree in v2.0 |

The flat files preserve the hierarchy through `parent_code`, so they can be loaded into any table or database.

## How to use CTNCS

1. Work top-down: choose the Sector, then the Category, Niche, and Content Style that best describe the release's main subject.
2. Add one primary Format for how most of the runtime is structured.
3. Record `platform`, `made_for_kids`, and `release_mode` (1 live, 2 standing, 3 derivative).
4. If the release substantially engages with a Sensitive Topic, add the Sector 17 node to `sensitive_topics`.
5. Optionally record a secondary path, a secondary format, and other metadata fields. Metadata is stored next to the ID, never inside it.

The full rules, decision chart, and worked examples are in the CTNCS Manual. An interactive explorer is at [classify.cvaccelerator.com](https://classify.cvaccelerator.com).

## Changes and requests

See [CHANGELOG.md](CHANGELOG.md). To propose a new node or report a problem, open an issue in this repository or email emily@cvaccelerator.com.

## How to cite CTNCS

Herrera, Emily. CTNCS: Content Terminal Niche Classification Standard, v2.0 (2026).
