# CTNCS Changelog

## v2.0 — October 2026

### Corrections (13 October 2026)
- Content Style labels that named a format (Vlogs, Tips, Reviews, Playthroughs, Recaps and similar) or were broader than their Niche were renamed to the subject or angle. Codes and meanings are unchanged, so no IDs change. 36 labels: Season Highlights to Season Arcs & Finales; Indie Clips to Indie & Experimental Music; Immersion & Polyglot Vlogs to Immersion & Polyglot Life; Grilling Tips to Grilling & BBQ; Cryptocurrencies to Crypto Protocols & Technology; Legislation Reviews to Legislation & Bills; Conflict Explainers to Conflict Background & History; Conflict Updates to Active Conflicts; Casual Sessions to Casual Play; Competitive Shooter Gameplay to Competitive Shooters; RPG Playthroughs to Story-Driven RPGs; Strategy Gameplay to Real-Time & Turn-Based Strategy; Horror Playthroughs to Horror Games; E-Commerce to Online Store Operations; Resume Tips to Resumes & Applications; Counseling Tips to Coping Skills; Travel Diaries to Personal Travel; TikTok Tips to TikTok Growth; Game Day Vlogs to Game Day & Tailgating; Wrestling Recaps to Matches & Events; Race Recaps to Races & Results; Riding & Sessions to Board Riding; Vet Tips to Preventive Care & Vet Visits; Research Updates to New Research; Breakthrough Reports to Breakthroughs; Camping Guides to Camping; Destination Guides to Destinations; Ownership Diaries to Long-Term Ownership; EV Reviews to EV Models; Theology Explainers to Theology & Doctrine; Faith Journey Vlogs to Faith Journeys; Fasting & Observance Logs to Fasting & Observance; Casino & Gambling Streams to Casino & Slots; Cannabis Culture to Cannabis Content; Firearms Reviews to Firearms & Accessories; Hunting & Shooting Sports to Hunting & Shooting Content.
- New rule in the manual: a Content Style names an angle or community within its Niche; it never names a format and is never broader than its Niche. `tools/check_labels.py` checks every Content Style label against this rule.

First edition of the CTNCS Manual, the normative text for this release (definitions, assignment rules, worked examples, governance, and the full codebook). v1.0 was released as a codebook only.

### Structure
- Format became an independent facet. Any Content Style may take any of the 73 active Format codes. The v1.0 pairings of Content Style and Format are kept as `typical_formats` (guidance, not a constraint).
- Niche and Content Style codes widened to three digits. New ID shape: `SS.CC.NNN.SSS.FF(.III)`.
- New validation regex: `^\d{2}\.\d{2}\.\d{3}\.\d{3}\.\d{2}(\.\d{3})?$`
- Level 6 is now an optional Content Instance code (`III`) assigned by the dataset owner. It is not part of the published codebook.

### Tree
- 17 Sectors, 68 Categories, 169 Niches, 347 Content Styles (601 nodes; 2 Sectors, 15 Categories, 65 Niches, and 151 Content Styles new in v2.0).
- Sectors 13 Science, 14 Travel, and 15 Automotive fully placed. Sector 16 Religion & Spirituality and Sector 17 Sensitive Topics added. Sector 17 is recorded only in the `sensitive_topics` metadata field.
- New Categories: Religious Life & Culture, Brand-Safety Restricted Topics, Car Care & Modding, EVs & Future Mobility, Language Learning, Game Genres, Relationships & Dating, Real Estate, Sports Media & Fandom, Combat Sports, Motorsport, Action & Outdoor Sports, Kids & Family, Competitions & Spectacle, Hobbies & Collecting.
- Fitness consolidated into Lifestyle: Exercise Routines moved from Physical Health. Physical Health gained Sleep & Recovery.
- Labels renamed from format names to subject names, with codes unchanged: Film Reviews to Film; TV Recaps to Television; Skits to Sketch & Improv Comedy; Music Videos to Music Releases; Live Performances to Concerts & Stage Performance; Recipes to Dishes & Meals; Makeup Tutorials to Makeup; Gadget Reviews to Personal Gadgets; Daily Updates to General News; Debates to Political Discourse; Live Streams to Gameplay; Walkthroughs to Game Guides; Game Reviews to Game Releases & Classics; Personal Vlogs to Personal Life; Family Vlogs to Family Life; Pet Vlogs to Pet Daily Life; Documentaries to Natural History; Gameplay & Streams to Gameplay & Guides; Vlogs & Daily Life to Personal & Family Life; Video Content to Video Creation; Podcasts (Content Style) to Podcasting; Live Updates to Developing Stories; News Briefs to Top Headlines; Live Discussions to Political Talk; Opinion Clashes to Contested Issues; Nature Films to Nature & Landscapes; Space Docs to Space & Cosmos; Morning Reports to Local & Regional News (re-scoped); Coding Tutorials to Coding & Programming; Crafting Guides to Handcrafts; Behavior Tips to Pet Behavior; Classic Car Reviews to Classic Cars; Soccer Highlights to Soccer; Basketball Plays to Basketball; Event Recaps to Aftermath & Follow-Ups (re-scoped to follow-up news coverage); Season Highlights to Season Arcs & Finales; Indie Clips to Indie & Experimental Music; Grilling Tips to Grilling & BBQ; Cryptocurrencies to Crypto Protocols & Technology; Legislation Reviews to Legislation & Bills; Casual Sessions to Casual Play; E-Commerce to Online Store Operations; Resume Tips to Resumes & Applications; Counseling Tips to Coping Skills; Travel Diaries to Personal Travel; TikTok Tips to TikTok Growth; Vet Tips to Preventive Care & Vet Visits; Research Updates to New Research; Breakthrough Reports to Breakthroughs; Camping Guides to Camping; Destination Guides to Destinations.
- Other renames: Smart Home Devices to Household Appliances; Fitness Training to Athletic Conditioning; Exercise Routines to Cardio & Conditioning; Astrology to Astrology & Divination; Astrology Insights to Astrology Education; Vehicles & Car Culture to Cars & Car Culture.
- Scope notes added to 68 nodes.
- Sensitive Topics separated from subject classification. Sector 17 nodes are recorded in the new `sensitive_topics` field (any number per release) and never as a primary or secondary path, so `secondary_path` stays free for a second subject. New subject homes for content that previously had none: Drinks & Cocktails (03.08.169), Cannabis Culture (03.54.170), Casino Games & Poker (07.21.168), and Hunting & Shooting Sports (11.66.167). Each Sector 17 Niche names the subject path that usually applies.
- Kids & Family (01.67) holds only genres that exist only for children: kids' songs, toy play, and kids' animation. Children's versions of other subjects take that subject's path with `made_for_kids = TRUE`. Preschool Learning is placed under Education > Academic (02.04.160). Kid-Hosted Shows was dropped before release because it classified by the host's age rather than the subject; its codes (Niche 163, Content Styles 332 and 333) are reserved.

### Formats
- ASMR recoded 61, Mashups 62, Fancam 63 to resolve code collisions.
- Definitions of Debate, Deep Dive, Demo, DIY, and FAQ corrected (they were shifted one row in v1.0).
- Added: Skit (64), Documentary (65), Reaction (66), Parody (67), Routine (68), Essay (69), Transformation (70), Follow-Along (71), Playthrough (72), Announcement (73), Report (74).
- Retired: Live (25). Live is a way of reaching an audience, not a structure; it is now recorded in `release_mode`. The code is reserved and will not be reused. Seventeen Content Styles that listed Live as a typical format were given structural formats instead.
- Added rules 6.11 (deciding between similar formats) and 6.12 (definition of substantial treatment: at least 25 percent of runtime or a recurring segment).

### Metadata
- Release metadata specification added (`CTNCS_Metadata_v2.0.csv`), including `made_for_kids`, YouTube Kids as a platform value, `sensitive_topics`, and `release_mode` (1 live, 2 standing, 3 derivative): the attention market a release competes in.

### Files
- `CTNCS_Codebook_v2.0.csv`, `.tsv`, and `_hier.json` replace the v1.0 codebook files. New columns: `level_name`, `typical_formats`, `typical_format_labels`, `scope_note`, `sensitive_topics_only`, `added_in`.
- `CTNCS_Formats_v2.0.csv` and `CTNCS_Metadata_v2.0.csv` added.
- v1.0 files moved to `v1.0/`.

### Compatibility
- 101 nodes were defined in the v1.0 codebook without a place in the tree, so they had no v1.0 ID. v2.0 places them under their v1.0 codes; no conversion is needed. Only four nodes moved (03.07.053, 03.07.053.105, 03.07.014.106, 09.28.093.114); see Section 13.1 of the manual.
- v1.0 IDs do not validate against the v2.0 regex. Convert Niche and Content Style segments to three digits and re-check Format codes 16, 58, and 59, which were each shared by two formats in v1.0 (Fancam is now 63, ASMR 61, Mashups 62).

## v1.0 — September 2025
- Initial public release of the CTNCS codebook (no manual).
- Codebook defined 15 Sectors, 53 Categories, 104 Niches, and 196 Content Styles. The published tree file placed 12 Sectors, 36 Categories, 73 Niches, and 146 Content Styles; the other 101 nodes were placed in v2.0 under their v1.0 codes.
- Level 5 paired each Content Style with one or two of 60 Format codes (275 pairings). Codes 16, 58, and 59 were each shared by two formats.
- Published as CSV (`CTNCS_Codebook_v1.0_github.csv`), TSV (`CTNCS_Codebook_v1.0_github.tsv`), and JSON (`CTNCS_Codebook_v1.0_hier.json`), now in `v1.0/`.
- Licensed under Creative Commons Attribution 4.0 (CC BY 4.0).
