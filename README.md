**CTNCS: Content Terminal Niche Classification Standard**
A content classification standard.

**Version:** v1.0  
**Author:** Emily Herrera  
**License:** Creative Commons Attribution 4.0 International (CC BY 4.0)  
**Last Updated:** September 2025


**What Is CTNCS?**

CTNCS is a six-level hierarchical taxonomy built to classify digital content units across platforms, styles, and formats. It is designed for use by researchers, Creators, platforms, investors, and institutions to bring clarity, rigor, and interoperability to the content ecosystem.

> If GICS is for industries and Dewey is for libraries, CTNCS is for content.



**What It Includes**

- **CTNCS Manual (v1.0)** – full standard: theory, methodology, classification guide, and implementation notes  
- **CTNCS Codebook** – complete listings for Levels 1–5, with numeric codes and definitions  
- **CTNCS ID Format Spec** – composite identifier rules (dot-notation), regex, and schema  
- **Quick Reference Guide** – visual onboarding for new users  
- **License (CC BY 4.0)** – open for use, adaptation, and extension with attribution  


**How to Use CTNCS**

- Classify a single unit of content using the 6-level CTNCS ID.  
- Use the codebook to assign sector, category, niche, style, and format.  
- Optionally tag with metadata like platform, language, or region.  
- Apply CTNCS to research datasets, platform taxonomies, tagging pipelines, or content audits.  



**Example CTNCS ID**

03.09.06.04.02
Segment	Meaning
03	Lifestyle (Sector)
09	Food & Cooking
06	Taste Tests
04	Fast Food Challenge
02	Compilation



**Code vs. Parent Code**
In the published CSV/TSV files, each row has both a code and a parent_code.

code is the full dot-path identifier shown above.

parent_code is the immediate ancestor’s code, created by truncating the last segment.

This design allows CTNCS to be distributed as a flat file while preserving its hierarchy.



**How to Cite CTNCS**
Herrera, Emily. CTNCS: Content Terminal Niche Classification Standard. v1.0 (2025).
Creative Commons Attribution 4.0. [contentterminal.co](https://contentterminal.co)



**License**
This project is licensed under the Creative Commons Attribution 4.0 International License (CC BY 4.0).
You may use, share, adapt, and fork this system — as long as credit is given to the original source.

Full license text →

**Forks & Extensions**
You are encouraged to fork CTNCS for internal use (e.g., platform-specific formats, subcultures, experimental labels).
Please tag your version clearly, e.g. CTNCS v1.2 (Shorts Fork) and retain attribution to the base standard.

## Contact
Have questions, feedback, or want to contribute?

Emily Herrera
em@pre-founder.com
