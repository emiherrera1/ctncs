# CTNCS Changelog

## v2.0 — October 2026

First edition of the CTNCS Manual, the normative text for this release (definitions, assignment rules, worked examples, governance, and the full codebook). v1.0 was released as a codebook only.

### Structure
- Level 4 is the Sub-Niche (called Content Style in v1.0): a narrower subject within its Niche. A Sub-Niche never names a format and never repeats its Niche's label.
- Each Sub-Niche lists 3 to 6 common formats, and only those, plus six universal formats that wrap any subject (08 Commentary, 10 Compilation, 22 Highlight, 62 Mashups, 66 Reaction, 67 Parody), are valid in its IDs. v1.0 listed one or two per node (275 pairings); v2.0 lists 1,620. If a release's structure is not listed, the ID uses the closest listed format and the actual structure is recorded in `unlisted_format` (Rule 6.10).
- Level 6 is the Example Concept: one illustrative release idea per common format of each Sub-Niche, published in the codebook. Example concepts are not codes.
- Niche and Sub-Niche codes widened to three digits. New ID shape: `SS.CC.NNN.SSS.FF(.RRR)`. The optional last segment is a Release Number assigned by the dataset owner; it is not part of the published codebook.
- New validation regex: `^\d{2}\.\d{2}\.\d{3}\.\d{3}\.\d{2}(\.\d{3})?$`

### Tree
- 17 Sectors, 68 Categories, 169 Niches, 347 Sub-Niches (601 nodes; 2 Sectors, 15 Categories, 65 Niches, and 151 Sub-Niches new in v2.0).
- Sectors 13 Science, 14 Travel, and 15 Automotive fully placed. Sector 16 Religion & Spirituality and Sector 17 Sensitive Topics added. Sector 17 is recorded only in the `sensitive_topics` metadata field.
- New Categories: Religious Life & Culture, Brand-Safety Restricted Topics, Car Care & Modding, EVs & Future Mobility, Language Learning, Game Genres, Relationships & Dating, Real Estate, Sports Media & Fandom, Combat Sports, Motorsport, Action & Outdoor Sports, Kids & Family, Competitions & Spectacle, Hobbies & Collecting.
- Fitness consolidated into Lifestyle: Exercise Routines moved from Physical Health. Physical Health gained Sleep & Recovery.
- Category and Niche labels renamed from format names to subject names, with codes unchanged: Film Reviews to Film; TV Recaps to Television; Skits to Sketch & Improv Comedy; Music Videos to Music Releases; Live Performances to Concerts & Stage Performance; Coding Tutorials to Coding & Programming; Crafting Guides to Handcrafts; Recipes to Dishes & Meals; Makeup Tutorials to Makeup; Gadget Reviews to Personal Gadgets; Daily Updates to General News; Debates to Political Discourse; Gameplay & Streams to Gameplay & Guides; Live Streams to Gameplay; Walkthroughs to Game Guides; Game Reviews to Game Releases & Classics; Exercise Routines to Cardio & Conditioning; Vlogs & Daily Life to Personal & Family Life; Personal Vlogs to Personal Life; Family Vlogs to Family Life; Fitness Training to Athletic Conditioning; Pet Vlogs to Pet Daily Life.
- Other Category and Niche renames: Smart Home Devices to Household Appliances; Astrology to Astrology & Divination; Vehicles & Car Culture to Cars & Car Culture.
- Labels that repeated their Sector's name, codes unchanged: Category 16.51 Religion & Spirituality to Faith & Practice and Category 17.52 Sensitive Topics to Crisis, Trauma & Loss.
- Punctuation-only label changes, codes unchanged: Arts and Crafts to Arts & Crafts (06.45); Comics and Graphic Novels to Comics & Graphic Novels (06.48.099); War and Conflicts to Wars & Conflicts (05.15.104).
- Every Sub-Niche label and definition was audited against the Sub-Niche rule. Codes are unchanged, so no IDs change. Of the 146 Sub-Niches placed in v1.0, 69 have new labels; a re-scoped node also has a new definition naming the subject it covers: Blockbuster Critiques to Blockbuster Films; Indie Film Analysis to Independent Film; Episode Summaries to Currently Airing Series (re-scoped); Season Highlights to Season Arcs & Finales; Short-Form Sketches to Scripted Sketches; Live Routines to Club & Open Mic Sets; Indie Clips to Indie & Experimental Music; Concert Footage to Concerts & Festivals; Algebra Basics to Algebra; Calculus Concepts to Calculus; Modern Events to Modern History; Sewing Projects to Sewing; Planetary Studies to Planets & Moons; Ecosystem Analysis to Ecosystems & Habitats; Beginner Flows to Beginner Yoga; Advanced Poses to Advanced Yoga; Baking Skills to Baking; Grilling Tips to Grilling & BBQ; Daily Looks to Everyday Makeup; Special Effects to SFX & Fantasy Makeup; Mobile Apps to iOS & Android Development (re-scoped); Desktop Software to Desktop App Development (re-scoped); Best Practices to Clean Code & Conventions; Video Content to Video Creation; Podcasts to Podcasting; Cryptocurrencies to Crypto Protocols & Technology; Live Updates to Developing Stories; Event Recaps to Aftermath & Follow-Ups; News Briefs to Top Headlines; Morning Reports to Local & Regional News; Live Discussions to Current Politics (re-scoped); Opinion Clashes to Contested Issues; Legislation Reviews to Legislation & Bills; Election Insights to Elections & Campaigns; Justice Topics to Criminal Justice & Civil Rights; Community Stories to Underrepresented Communities (re-scoped); Tech Impacts to Technology & Society; Casual Sessions to Casual Play; Story Guides to Story Progression & Endings (re-scoped); Puzzle Solutions to Puzzles & Secrets; Player Profiles to Pro Players; Funding Strategies to Startup Fundraising; Marketing Tactics to Growth Marketing; Leadership Training to Leadership; E-Commerce to Online Store Operations; Soccer Highlights to Soccer; Lifestyle Posts to Influencer Life (re-scoped); TikTok Tips to TikTok Growth; Group Events to Meetups & Conventions; Basketball Plays to Basketball; Forum Chats to Online Forums & Threads; Cosplay Creations to Cosplay; Equality Drives to Representation & Inclusion (re-scoped); Parenting Moments to Everyday Parenting; Tennis Matches to Tennis; Endurance Runs to Distance Running; Trick Shows to Pet Tricks; Funny Moments to Pet Antics; Golf Techniques to Golf; Daily Routines to Pet Habits & Personalities; Vet Tips to Preventive Care & Vet Visits; Diet Advice to Pet Nutrition; Dribbling Drills to Ball Handling; Power Lifting to Powerlifting; Life Updates to Life Milestones (re-scoped); Astrology Insights to Zodiac Signs & Planets (re-scoped); Travel Diaries to Personal Travel; Counseling Tips to Coping Skills; Cardio Workouts to Endurance Cardio (re-scoped).
- Scope notes added to 69 nodes.
- Sensitive Topics separated from subject classification. Sector 17 nodes are recorded in the new `sensitive_topics` field (any number per release) and never as a primary or secondary path, so `secondary_path` stays free for a second subject. New subject homes for content that previously had none: Drinks & Cocktails (03.08.169), Cannabis Culture (03.54.170), Casino Games & Poker (07.21.168), and Hunting & Shooting Sports (11.66.167). Each Sector 17 Niche names the subject path that usually applies.
- Kids & Family (01.67) holds only genres that exist only for children: kids' songs, toy play, and kids' animation. Children's versions of other subjects take that subject's path with `made_for_kids = TRUE`. Preschool Learning is placed under Education > Academic (02.04.160). Kid-Hosted Shows was dropped before release because it classified by the host's age rather than the subject; its codes (Niche 163, Sub-Niches 332 and 333) are reserved.

### Formats
- ASMR recoded 61, Mashups 62, Fancam 63 to resolve code collisions.
- Definitions of Debate, Deep Dive, Demo, DIY, and FAQ corrected (they were shifted one row in v1.0).
- Definitions of Experiment (16), Guide (19), Performance (30), Recital (40), Test (50), Tour (53), Walkthrough (60), and Fancam (63) sharpened to separate them from neighboring formats.
- Added: Skit (64), Documentary (65), Reaction (66), Parody (67), Routine (68), Essay (69), Transformation (70), Follow-Along (71), Playthrough (72), Announcement (73), Report (74).
- Retired: Live (25). Live is a way of reaching an audience, not a structure; it is now recorded in `release_mode`. The code is reserved and will not be reused. Seventeen Sub-Niches that listed Live were given structural formats instead.
- Roasts (42) is a common format of Club & Open Mic Sets, Comedy Specials, and Meme Culture.
- Added rules 6.11 (deciding between similar formats) and 6.12 (definition of substantial treatment: at least 25 percent of runtime or a recurring segment).

### Metadata
- Release metadata specification added (`CTNCS_Metadata_v2.0.csv`), including `made_for_kids`, YouTube Kids as a platform value, `sensitive_topics`, and `release_mode` (1 live, 2 standing, 3 derivative): the attention market a release competes in.
- Added `unlisted_format`: the structure a release actually uses when it is not one of its Sub-Niche's common formats (Rule 6.10).

### Files
- `CTNCS_Codebook_v2.0.csv`, `.tsv`, and `_hier.json` replace the v1.0 codebook files. New columns: `level_name`, `common_formats`, `common_format_labels`, `example_concepts`, `scope_note`, `sensitive_topics_only`, `added_in`.
- `CTNCS_Formats_v2.0.csv` and `CTNCS_Metadata_v2.0.csv` added.
- v1.0 files moved to `v1.0/`.
- `tools/check_labels.py` checks the codebook against the Sub-Niche rule and the common-format lists, and validates IDs (`--id`).

### Compatibility
- 101 nodes were defined in the v1.0 codebook without a place in the tree, so they had no v1.0 ID. v2.0 places them under their v1.0 codes; no conversion is needed. Only four nodes moved (03.07.053, 03.07.053.105, 03.07.014.106, 09.28.093.114); see Section 13.1 of the manual.
- Every v1.0 pairing of a Sub-Niche and a Format is still a common format of that Sub-Niche, except pairings with retired Format 25 (Live), so converted v1.0 IDs remain valid.
- v1.0 IDs do not validate against the v2.0 regex. Convert Niche and Sub-Niche segments to three digits and re-check Format codes 16, 58, and 59, which were each shared by two formats in v1.0 (Fancam is now 63, ASMR 61, Mashups 62).

## v1.0 — September 2025
- Initial public release of the CTNCS codebook (no manual).
- Codebook defined 15 Sectors, 53 Categories, 104 Niches, and 196 Content Styles. The published tree file placed 12 Sectors, 36 Categories, 73 Niches, and 146 Content Styles; the other 101 nodes were placed in v2.0 under their v1.0 codes.
- Level 5 paired each Content Style with one or two of 60 Format codes (275 pairings). Codes 16, 58, and 59 were each shared by two formats.
- Published as CSV (`CTNCS_Codebook_v1.0_github.csv`), TSV (`CTNCS_Codebook_v1.0_github.tsv`), and JSON (`CTNCS_Codebook_v1.0_hier.json`), now in `v1.0/`.
- Licensed under Creative Commons Attribution 4.0 (CC BY 4.0).
