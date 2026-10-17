<div align="center">

# Hey, I'm Riyan.

**Cybersecurity practitioner and open-source tinkerer from Indonesia.**

Threat hunting · Digital forensics · Detection engineering · OSINT · Security automation

<a href="https://github.com/Masriyan">GitHub</a> · <a href="https://www.security-life.org">Website</a> · <a href="https://sudo3rs.medium.com/">Writing</a> · <a href="https://www.linkedin.com/in/sudo3rs/">LinkedIn</a>

</div>

---

### A little about me

Most of my work sits somewhere between incident response, threat intelligence, detection engineering, and building small security tools.

I like understanding how things work, especially when the documentation is incomplete or the answer is buried in logs. Many repositories here began as something I needed for an investigation, a routine task I wanted to simplify, or an idea worth testing in a lab.

Not everything here is a finished product. Some projects are maintained utilities, others are research notes, prototypes, or earlier experiments. I keep them public because sharing the process, including what still needs improvement, can be useful too.

I am usually interested in practical problems, readable code, reproducible findings, and feedback from people who see things differently.

### What I usually work on

| Area | What interests me |
| --- | --- |
| **Threat hunting and CTI** | Turning scattered indicators, behaviors, and open-source evidence into useful leads. |
| **DFIR and malware triage** | Collecting artifacts, understanding suspicious files, and documenting what the evidence actually supports. |
| **Detection engineering** | Writing and improving SIEM use cases, analytics, and incident-response workflows. |
| **Security tooling** | Building focused utilities that reduce repetitive work without hiding important context. |
| **AI-assisted security** | Exploring where agents and automation help analysts, and where their behavior still needs oversight. |

### A few projects to start with

These are useful starting points if you are new to my repositories. The full public catalog is further down.

| Project | Why you might open it |
| --- | --- |
| [**FlatScan**](https://github.com/Masriyan/FlatScan) | Static malware triage in Go. Inspect a file without executing it, collect indicators, review PE metadata, and export findings for further analysis. |
| [**Claude Code CyberSecurity Skills**](https://github.com/Masriyan/Claude-Code-CyberSecurity-Skill) | 22 structured Claude Code skills spanning defensive and authorized offensive workflows, CTI, malware analysis, IR, AI security, and more. |
| [**MacFIRE**](https://github.com/Masriyan/MacFIRE) | macOS-oriented forensic collection and investigation, with artifact review and reporting features. |
| [**CrotDalam**](https://github.com/Masriyan/CrotDalam) | Public TikTok OSINT collection and analysis using a browser rather than a paid API. |
| [**PHANTOM Web**](https://github.com/Masriyan/phantom-web) | A lightweight, browser-based workspace for IOC extraction, ATT&CK mapping, local triage and notes. |
| [**ShortIT**](https://github.com/Masriyan/ShortIT) | Measure where Claude Code tokens are spent and compare optimizations against a real baseline. |
| [**FuFuFaFa**](https://github.com/Masriyan/FuFuFaFa) | AWS security auditing experiments and configuration review. |
| [**OpenBOM**](https://github.com/Masriyan/OpenBOM) | Software supply-chain risk research and dependency visibility. |

<sub>Each repository has its own scope, setup instructions, limitations and license. Please read those before using the code.</sub>

---

## Repository directory

I group my public work by its main purpose rather than by stars or popularity. Some repositories overlap across disciplines, so each one appears once in the catalog below. Archived projects remain listed because they may still be useful as references.

<!-- REPOSITORIES:START -->
<sub>39 public repositories in this index. Initial curated snapshot. Run the catalog workflow to include all currently public repositories.</sub>

### AI, agent workflows and automation

| Repository | Scope |
| --- | --- |
| [**Asu-SOAR**](https://github.com/Masriyan/Asu-SOAR) | An experimental security orchestration and response platform with integrations and a unified operations interface. |
| [**Claude-Code-CyberSecurity-Skill**](https://github.com/Masriyan/Claude-Code-CyberSecurity-Skill) | A collection of 22 Claude Code skills for security workflows, from incident response and hunting to AI security, CTI and purple teaming. |
| [**gemini-security-skills**](https://github.com/Masriyan/gemini-security-skills) | Structured security and engineering skills for Gemini CLI, including research, threat-intelligence workflows and agent security. |
| [**Octopus-Ai**](https://github.com/Masriyan/Octopus-Ai) | An AI assistant experiment exploring ways to support everyday workflows with automation. |
| [**semar**](https://github.com/Masriyan/semar) | Research on evaluating security risks in AI agents, configurations, prompts and connected tools. |
| [**ShortIT**](https://github.com/Masriyan/ShortIT) | Audits Claude Code session token usage and helps compare practical cost reductions against a recorded baseline. |
| [**X-n8-Exnate**](https://github.com/Masriyan/X-n8-Exnate) | Security automation and SOC workflow examples connecting orchestration approaches such as n8n and XSOAR. |

### Malware analysis, DFIR and detection

| Repository | Scope |
| --- | --- |
| [**DevoSIEM_UCL**](https://github.com/Masriyan/DevoSIEM_UCL) | Detection use cases and response workflow material for Devo SIEM environments. |
| [**FlatScan**](https://github.com/Masriyan/FlatScan) | A local, static file-analysis engine in Go with IOC extraction, PE intelligence, heuristics and analyst-oriented exports. |
| [**MacFIRE**](https://github.com/Masriyan/MacFIRE) | macOS forensic collection and incident-response utilities for live triage, artifact review and reporting. |
| [**OpenBOM**](https://github.com/Masriyan/OpenBOM) | Software supply-chain visibility and package-risk research, with vulnerability and lifecycle context. |
| [**Qradar-SIEM-Auditor**](https://github.com/Masriyan/Qradar-SIEM-Auditor) | Utilities for reviewing and auditing IBM QRadar SIEM deployments. |
| [**Ransomeye**](https://github.com/Masriyan/Ransomeye) | A ransomware-focused detection and investigation project. |
| [**StealerKiller**](https://github.com/Masriyan/StealerKiller) | Endpoint-oriented tooling for detecting and responding to signs of infostealer activity. |
| [**uclsoc_code**](https://github.com/Masriyan/uclsoc_code) | A CSOC use-case and detection-rule library with MITRE ATT&CK-aligned content. |
| [**WinFire**](https://github.com/Masriyan/WinFire) | Windows incident-response tooling for forensic artifact collection and investigation support. |

### Threat intelligence and OSINT

| Repository | Scope |
| --- | --- |
| [**CrotDalam**](https://github.com/Masriyan/CrotDalam) | Public TikTok OSINT collection using a browser, with video metadata and risk-oriented heuristics. |
| [**CTI-Product-Assesment-Matrix**](https://github.com/Masriyan/CTI-Product-Assesment-Matrix) | A reference matrix for comparing cyber threat-intelligence products and their capabilities. |
| [**IOC_Radar_X**](https://github.com/Masriyan/IOC_Radar_X) | Research on extracting and reviewing indicators of compromise from posts on X. |
| [**Kalitellingence**](https://github.com/Masriyan/Kalitellingence) | Shell-based setup and additions for using Kali Linux as a threat-intelligence workstation. |
| [**Obscura-Threat-Investigation**](https://github.com/Masriyan/Obscura-Threat-Investigation) | Threat-investigation notes, case material and security research writeups. |
| [**phantom-web**](https://github.com/Masriyan/phantom-web) | A browser-based CTI workspace for IOC extraction, local file triage, ATT&CK mapping and reports. |
| [**URL_Request_bot**](https://github.com/Masriyan/URL_Request_bot) | A Telegram-based helper for URL requests and supporting log workflows. |

### Reconnaissance and authorized testing

| Repository | Scope |
| --- | --- |
| [**Aegis**](https://github.com/Masriyan/Aegis) <sub>(archived)</sub> | A single-file URL reconnaissance and OSINT enrichment application with optional active checks. |
| [**Bucin**](https://github.com/Masriyan/Bucin) | External reconnaissance and asset discovery experiments. |
| [**CVE-2026-85097**](https://github.com/Masriyan/CVE-2026-85097) | A repository labeled as a Bricksforge vulnerability PoC, including a checker and defensive rule examples; verify advisory status independently. |
| [**ExpertXSS**](https://github.com/Masriyan/ExpertXSS) | An XSS and reflection testing utility with context-aware checks for permitted targets. |
| [**Makassarscan**](https://github.com/Masriyan/Makassarscan) | A reconnaissance toolkit for collecting and reviewing information about authorized targets. |
| [**Waduh**](https://github.com/Masriyan/Waduh) | A WordPress assessment toolkit combining enumeration, scanner modules and optional AI-assisted review. |

### Cloud security and secret exposure

| Repository | Scope |
| --- | --- |
| [**FuFuFaFa**](https://github.com/Masriyan/FuFuFaFa) | An AWS cloud-auditing framework for reviewing security configuration and possible exposures. |
| [**No-Secret-Scan-**](https://github.com/Masriyan/No-Secret-Scan-) | A scanner aimed at finding potentially sensitive values exposed in web content. |
| [**No-Secret-Scan-Github-Gitlab**](https://github.com/Masriyan/No-Secret-Scan-Github-Gitlab) | Scans GitHub and GitLab repositories for possible hardcoded credentials, keys and tokens. |

### Research, learning and utilities

| Repository | Scope |
| --- | --- |
| [**FedChecks**](https://github.com/Masriyan/FedChecks) | Fedora post-installation checks and system-health reporting utilities. |
| [**Jomok**](https://github.com/Masriyan/Jomok) | A research and educational repository containing experimental material. |
| [**Masriyan**](https://github.com/Masriyan/Masriyan) | The repository that maintains this GitHub profile and its documentation. |
| [**samnayiransomware**](https://github.com/Masriyan/samnayiransomware) | A ransomware-behavior simulation project intended for controlled research environments. |
| [**security-life.Hacktools**](https://github.com/Masriyan/security-life.Hacktools) | A collection of smaller security-related tools and utilities. |
| [**Threat-Model-Exploration**](https://github.com/Masriyan/Threat-Model-Exploration) | Threat-modeling templates, examples, case studies and learning challenges. |
| [**war-dashboard**](https://github.com/Masriyan/war-dashboard) | An experimental dashboard for tracking public reporting about an ongoing conflict; sources require independent verification. |
<!-- REPOSITORIES:END -->

<sub>The accompanying GitHub Actions workflow can refresh this directory from all of my public GitHub repositories. Repository metadata and project scopes can change, so each project's own README is the primary source for its current capabilities.</sub>

---

## How I approach open-source security work

**Evidence before assumptions.** I try to distinguish confirmed observations from heuristics, especially in threat intelligence and malware triage.

**Small tools are allowed to stay small.** A single-purpose script is sometimes more helpful than a complicated platform.

**Know the limitations.** A suspicious pattern is not always malicious, and a scan result is not a substitute for investigation.

**Use the tools responsibly.** Anything involving scanning, exploitation, or adversary simulation belongs on systems you own or are explicitly authorized to assess.

**Keep learning in public.** Bug reports, corrections, ideas, and contributions are welcome. A thoughtful issue can be as helpful as a pull request.

## Notes, writing and contact

When I have something worth documenting, I usually put it in a repository or write about it here:

- [security-life.org](https://www.security-life.org) for articles and experiments
- [Medium](https://sudo3rs.medium.com/) and [Blogger](https://ibliz-muda.blogspot.com/) for longer notes
- [LinkedIn](https://www.linkedin.com/in/sudo3rs/) and [X](https://x.com/sudo3rs) for occasional updates
- [Security Life GitHub community](https://github.com/secuity-life-org) for related open-source work

For a project-specific problem, please use that repository's **Issues** or **Discussions**, when enabled. For other conversations, you can contact me at [this email address](mailto:decisive.smelt.akjy@shieldedpost.net).

If something here saved you a little time, I'm glad it did. If you want to [buy me a coffee](https://paypal.me/riyansuryapratama), thank you, but there is absolutely no obligation.

<div align="center">

---

<sub>Built with curiosity, revised with feedback, and shared for people who are still figuring things out too.</sub>

</div>
