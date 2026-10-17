#!/usr/bin/env python3
"""Refresh a GitHub profile README catalog from public GitHub repositories.

Python standard library only. Run with --seed to use the curated index without
network access, or without it to fetch all repositories from the public API.
"""

from __future__ import annotations

import argparse
import json
import os
import re
import sys
from datetime import datetime, timezone
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen

OWNER = "Masriyan"
START = "<!-- REPOSITORIES:START -->"
END = "<!-- REPOSITORIES:END -->"

# Descriptions are deliberately conservative. A title is not evidence of a
# feature, and a README is not proof that a product is production-ready.
# Categories and descriptions can be edited here without changing README.
CATEGORIES = [
    "AI, agent workflows and automation",
    "Malware analysis, DFIR and detection",
    "Threat intelligence and OSINT",
    "Reconnaissance and authorized testing",
    "Cloud security and secret exposure",
    "Research, learning and utilities",
    "Other public repositories",
]

# repo_name: (category, description)
PROJECTS: dict[str, tuple[str, str]] = {
    "Claude-Code-CyberSecurity-Skill": (
        CATEGORIES[0], "A collection of 22 Claude Code skills for security workflows, from incident response and hunting to AI security, CTI and purple teaming."
    ),
    "gemini-security-skills": (
        CATEGORIES[0], "Structured security and engineering skills for Gemini CLI, including research, threat-intelligence workflows and agent security."
    ),
    "ShortIT": (
        CATEGORIES[0], "Audits Claude Code session token usage and helps compare practical cost reductions against a recorded baseline."
    ),
    "X-n8-Exnate": (
        CATEGORIES[0], "Security automation and SOC workflow examples connecting orchestration approaches such as n8n and XSOAR."
    ),
    "Asu-SOAR": (
        CATEGORIES[0], "An experimental security orchestration and response platform with integrations and a unified operations interface."
    ),
    "semar": (
        CATEGORIES[0], "Research on evaluating security risks in AI agents, configurations, prompts and connected tools."
    ),
    "Octopus-Ai": (
        CATEGORIES[0], "An AI assistant experiment exploring ways to support everyday workflows with automation."
    ),
    "FlatScan": (
        CATEGORIES[1], "A local, static file-analysis engine in Go with IOC extraction, PE intelligence, heuristics and analyst-oriented exports."
    ),
    "MacFIRE": (
        CATEGORIES[1], "macOS forensic collection and incident-response utilities for live triage, artifact review and reporting."
    ),
    "WinFire": (
        CATEGORIES[1], "Windows incident-response tooling for forensic artifact collection and investigation support."
    ),
    "StealerKiller": (
        CATEGORIES[1], "Endpoint-oriented tooling for detecting and responding to signs of infostealer activity."
    ),
    "Ransomeye": (
        CATEGORIES[1], "A ransomware-focused detection and investigation project."
    ),
    "uclsoc_code": (
        CATEGORIES[1], "A CSOC use-case and detection-rule library with MITRE ATT&CK-aligned content."
    ),
    "DevoSIEM_UCL": (
        CATEGORIES[1], "Detection use cases and response workflow material for Devo SIEM environments."
    ),
    "Qradar-SIEM-Auditor": (
        CATEGORIES[1], "Utilities for reviewing and auditing IBM QRadar SIEM deployments."
    ),
    "OpenBOM": (
        CATEGORIES[1], "Software supply-chain visibility and package-risk research, with vulnerability and lifecycle context."
    ),
    "CrotDalam": (
        CATEGORIES[2], "Public TikTok OSINT collection using a browser, with video metadata and risk-oriented heuristics."
    ),
    "IOC_Radar_X": (
        CATEGORIES[2], "Research on extracting and reviewing indicators of compromise from posts on X."
    ),
    "URL_Request_bot": (
        CATEGORIES[2], "A Telegram-based helper for URL requests and supporting log workflows."
    ),
    "Kalitellingence": (
        CATEGORIES[2], "Shell-based setup and additions for using Kali Linux as a threat-intelligence workstation."
    ),
    "CTI-Product-Assesment-Matrix": (
        CATEGORIES[2], "A reference matrix for comparing cyber threat-intelligence products and their capabilities."
    ),
    "Obscura-Threat-Investigation": (
        CATEGORIES[2], "Threat-investigation notes, case material and security research writeups."
    ),
    "phantom-web": (
        CATEGORIES[2], "A browser-based CTI workspace for IOC extraction, local file triage, ATT&CK mapping and reports."
    ),
    "ExpertXSS": (
        CATEGORIES[3], "An XSS and reflection testing utility with context-aware checks for permitted targets."
    ),
    "Makassarscan": (
        CATEGORIES[3], "A reconnaissance toolkit for collecting and reviewing information about authorized targets."
    ),
    "Bucin": (
        CATEGORIES[3], "External reconnaissance and asset discovery experiments."
    ),
    "Aegis": (
        CATEGORIES[3], "A single-file URL reconnaissance and OSINT enrichment application with optional active checks."
    ),
    "Waduh": (
        CATEGORIES[3], "A WordPress assessment toolkit combining enumeration, scanner modules and optional AI-assisted review."
    ),
    "CVE-2026-85097": (
        CATEGORIES[3], "A repository labeled as a Bricksforge vulnerability PoC, including a checker and defensive rule examples; verify advisory status independently."
    ),
    "FuFuFaFa": (
        CATEGORIES[4], "An AWS cloud-auditing framework for reviewing security configuration and possible exposures."
    ),
    "No-Secret-Scan-": (
        CATEGORIES[4], "A scanner aimed at finding potentially sensitive values exposed in web content."
    ),
    "No-Secret-Scan-Github-Gitlab": (
        CATEGORIES[4], "Scans GitHub and GitLab repositories for possible hardcoded credentials, keys and tokens."
    ),
    "FedChecks": (
        CATEGORIES[5], "Fedora post-installation checks and system-health reporting utilities."
    ),
    "samnayiransomware": (
        CATEGORIES[5], "A ransomware-behavior simulation project intended for controlled research environments."
    ),
    "Jomok": (
        CATEGORIES[5], "A research and educational repository containing experimental material."
    ),
    "security-life.Hacktools": (
        CATEGORIES[5], "A collection of smaller security-related tools and utilities."
    ),
    "Threat-Model-Exploration": (
        CATEGORIES[5], "Threat-modeling templates, examples, case studies and learning challenges."
    ),
    "war-dashboard": (
        CATEGORIES[5], "An experimental dashboard for tracking public reporting about an ongoing conflict; sources require independent verification."
    ),
    "Masriyan": (
        CATEGORIES[5], "The repository that maintains this GitHub profile and its documentation."
    ),
}


def fetch_public_repositories(owner: str) -> list[dict]:
    """Fetch every page. GitHub limits each page to 100 repositories."""
    token = os.environ.get("GITHUB_TOKEN", "")
    results: list[dict] = []
    page = 1
    while True:
        url = f"https://api.github.com/users/{owner}/repos?type=owner&per_page=100&page={page}"
        headers = {
            "Accept": "application/vnd.github+json",
            "User-Agent": "profile-readme-catalog-updater",
            "X-GitHub-Api-Version": "2022-11-28",
        }
        if token:
            headers["Authorization"] = f"Bearer {token}"
        request = Request(url, headers=headers)
        with urlopen(request, timeout=25) as response:
            page_data = json.load(response)
        if not isinstance(page_data, list):
            raise ValueError("Unexpected GitHub response. Expected a list of repositories.")
        results.extend(repo for repo in page_data if repo.get("private") is False)
        if len(page_data) < 100:
            break
        page += 1
    if not results:
        raise ValueError("No public repositories returned. Keeping README unchanged.")
    return results


def markdown_cell(value: str) -> str:
    return re.sub(r"\s+", " ", str(value)).replace("|", "\\|").replace("\r", "").strip()


def fallback_description(repo: dict) -> str:
    raw = (repo.get("description") or "").strip()
    if not raw:
        return "Code and project notes. See the repository for its current scope."
    raw = re.sub(r"\s+", " ", raw)
    return raw[:197] + "..." if len(raw) > 200 else raw


def render_catalog(repos: list[dict], *, origin: str) -> str:
    rows: dict[str, list[tuple[str, str]]] = {cat: [] for cat in CATEGORIES}
    for repo in repos:
        name = repo["name"]
        category, description = PROJECTS.get(name, (CATEGORIES[-1], fallback_description(repo)))
        note = []
        if repo.get("archived"):
            note.append("archived")
        if repo.get("fork"):
            note.append("fork")
        suffix = f" <sub>({', '.join(note)})</sub>" if note else ""
        url = repo.get("html_url") or f"https://github.com/{OWNER}/{name}"
        # Only GitHub repo URLs belong in the catalog (avoid injecting third-party links).
        if not url.startswith(f"https://github.com/{OWNER}/"):
            url = f"https://github.com/{OWNER}/{name}"
        first = f"[**{markdown_cell(name)}**]({url}){suffix}"
        rows[category].append((name.casefold(), f"| {first} | {markdown_cell(description)} |"))

    total = sum(len(group) for group in rows.values())
    out = [f"<sub>{total} public repositories in this index. "]
    if origin == "github":
        out[0] += "Automatically synchronized with the GitHub public repository API.</sub>"
    else:
        out[0] += "Initial curated snapshot. Run the catalog workflow to include all currently public repositories.</sub>"
    out += [""]
    for category, group in rows.items():
        if not group:
            continue
        out += [f"### {category}", "", "| Repository | Scope |", "| --- | --- |"]
        out += [row for _, row in sorted(group)]
        out += [""]
    return "\n".join(out).rstrip() + "\n"


def build_seed() -> list[dict]:
    return [
        {"name": name, "html_url": f"https://github.com/{OWNER}/{name}",
         "private": False, "fork": False, "archived": name == "Aegis"}
        for name in PROJECTS
    ]


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--readme", default="README.md", help="Path to profile README")
    parser.add_argument("--owner", default=OWNER, help="GitHub username")
    parser.add_argument("--seed", action="store_true", help="Use the offline curated snapshot")
    args = parser.parse_args()
    readme = Path(args.readme)
    original = readme.read_text(encoding="utf-8")
    if original.count(START) != 1 or original.count(END) != 1:
        raise ValueError("README must contain exactly one pair of repository section markers.")
    repos = build_seed() if args.seed else fetch_public_repositories(args.owner)
    catalog = render_catalog(repos, origin="seed" if args.seed else "github")
    updated = original.split(START, 1)[0] + START + "\n" + catalog + END + original.split(END, 1)[1]
    if updated != original:
        readme.write_text(updated, encoding="utf-8")
    print(f"Indexed {len(repos)} public repositories; changed={updated != original}.")
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except (HTTPError, URLError, OSError, ValueError) as error:
        print(f"Catalog update failed, README not replaced: {error}", file=sys.stderr)
        sys.exit(1)
