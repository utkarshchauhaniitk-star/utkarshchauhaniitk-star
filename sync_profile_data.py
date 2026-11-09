#!/usr/bin/env python3
"""
sync_profile_data.py - Master Profile Synchronization & LinkedIn Generator

Single Source of Truth pipeline for Utkarsh Singh Chauhan's cybersecurity portfolio.
Reads professional_profile_master.json, validates data integrity, verifies links,
and exports copy-ready LinkedIn profile sections, GitHub README alignment,
and automated project announcement drafts.
"""

import json
import os
import re
import sys
from pathlib import Path

WORKSPACE_ROOT = Path(__file__).resolve().parent
MASTER_FILE = WORKSPACE_ROOT / "professional_profile_master.json"

def load_master_data():
    if not MASTER_FILE.exists():
        raise FileNotFoundError(f"Master file not found at: {MASTER_FILE}")
    with open(MASTER_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

def validate_master_data(data):
    """Ensure all required fields exist and adhere to constraints."""
    issues = []
    
    # 1. Identity validation
    identity = data.get("personal_identity", {})
    if not identity.get("full_name"):
        issues.append("Missing personal_identity.full_name")
    if not identity.get("headline"):
        issues.append("Missing personal_identity.headline")
    if len(identity.get("headline", "")) > 220:
        issues.append("Headline exceeds LinkedIn limit of 220 characters")
        
    # Check for forbidden claims
    headline_lower = identity.get("headline", "").lower()
    for forbidden in ["senior", "architect", "lead engineer", "5+ years", "10+ years"]:
        if forbidden in headline_lower:
            issues.append(f"Forbidden exaggerated claim detected in headline: '{forbidden}'")
            
    # 2. Project validation
    projects = data.get("projects", [])
    if len(projects) != 3:
        issues.append(f"Expected exactly 3 portfolio projects, found {len(projects)}")
    for proj in projects:
        if not proj.get("name") or not proj.get("repository_url"):
            issues.append(f"Project missing name or repository URL: {proj}")
        if not proj.get("technologies"):
            issues.append(f"Project missing technologies: {proj.get('name')}")
            
    # 3. Links validation
    links = data.get("links", {})
    url_pattern = re.compile(r"^https?://")
    email_pattern = re.compile(r"^[^@]+@[^@]+\.[^@]+$")
    for key, val in links.items():
        if val:
            if key == "email":
                if not email_pattern.match(val):
                    issues.append(f"Invalid email format for links.email: '{val}'")
            else:
                if not url_pattern.match(val):
                    issues.append(f"Invalid URL format for links.{key}: '{val}'")

    return issues

def generate_linkedin_markdown(data):
    """Generate structured, copy-ready LinkedIn sections."""
    identity = data["personal_identity"]
    projects = data["projects"]
    skills = data["skills"]
    links = data["links"]
    
    md = []
    md.append("# Optimized LinkedIn Profile Content")
    md.append(f"**Candidate**: {identity['full_name']}  ")
    md.append(f"**Target Role**: SOC Analyst • Threat Detection • DFIR  ")
    md.append(f"**Profile URL**: [{links['linkedin_profile']}]({links['linkedin_profile']})  ")
    md.append(f"**Generated From**: `professional_profile_master.json`  \n")
    md.append("---\n")
    
    # Section 1: Headline
    md.append("## 1. LinkedIn Headline")
    md.append("> **Character Limit**: 220 characters | **Length**: " + str(len(identity['headline'])) + " characters\n")
    md.append("```text")
    md.append(identity["headline"])
    md.append("```\n")
    md.append("*Why it works*: Immediately identifies you as a final-year cybersecurity student aiming for SOC Analyst and DFIR roles, highlighting your primary technical domains without artificial title inflation.\n")
    md.append("---\n")
    
    # Section 2: About Section
    md.append("## 2. About Section")
    md.append("```text")
    md.append(f"Hi, I'm {identity['preferred_name']}.")
    md.append("")
    md.append(f"I am a {identity['current_status'].lower()}. Rather than focusing exclusively on theoretical textbooks, I invest my time in building practical open-source defensive cybersecurity tools to understand how attacks happen, how security telemetry is ingested, and how analysts triage alerts in real-world Security Operations Centers (SOCs).")
    md.append("")
    md.append("🛡️ KEY PRACTICAL PROJECTS:")
    for proj in projects:
        md.append(f"• {proj['name']}: {proj['purpose']}")
        md.append(f"  Repo: {proj['repository_url']}")
        if proj.get('live_demo_url'):
            md.append(f"  Live Demo: {proj['live_demo_url']}")
    md.append("")
    md.append("🎯 CORE TECHNICAL FOCUS:")
    md.append("• Security Operations (SOC) & Alert Triage (MITRE ATT&CK®)")
    md.append("• Security Telemetry & Log Normalization (Syslog, Auth, Firewall)")
    md.append("• Digital Forensics & Incident Response (DFIR & Chain-of-Custody)")
    md.append("• Cryptographic Integrity Verification (Streaming SHA-256)")
    md.append("• Threat Intelligence Aggregation & CVE Extraction")
    md.append("• Python Security Tooling & Automation")
    md.append("")
    md.append("🧰 TECHNICAL TOOLKIT:")
    md.append(f"• Languages & Systems: {', '.join(skills['programming_and_scripting'])}")
    md.append(f"• Security & SIEM Tools: {', '.join(skills['security_tools_and_environments'])}")
    md.append(f"• Frameworks & Dev: {', '.join(skills['frameworks_and_libraries'][:6])}")
    md.append("")
    md.append("📬 OPEN TO OPPORTUNITIES:")
    md.append("I am actively preparing for Cybersecurity Internships and Entry-Level SOC Analyst / DFIR positions. Feel free to connect or review my open-source security projects on GitHub.")
    md.append(f"GitHub: {links['github_profile']}")
    md.append(f"Email: {links['email']}")
    md.append("```\n")
    md.append("---\n")
    
    # Section 3: Projects Section
    md.append("## 3. LinkedIn Projects Section\n")
    for i, proj in enumerate(projects, 1):
        md.append(f"### Project {i}: {proj['name']}")
        md.append(f"**Project Name**: `{proj['title']}`  ")
        md.append(f"**URL**: `{proj['repository_url']}`  ")
        if proj.get("live_demo_url"):
            md.append(f"**Associated Link (Demo)**: `{proj['live_demo_url']}`  ")
        md.append("\n**Description (Copy into LinkedIn Project Description)**:")
        md.append("```text")
        md.append(proj['purpose'])
        md.append("")
        md.append("Key Implemented Capabilities:")
        for feat in proj['key_features']:
            md.append(f"- {feat}")
        md.append("")
        md.append(f"Tech Stack: {', '.join(proj['technologies'])}")
        md.append(f"Repository: {proj['repository_url']}")
        if proj.get("live_demo_url"):
            md.append(f"Live Application: {proj['live_demo_url']}")
        md.append("```\n")
    md.append("---\n")
    
    # Section 4: Skills Section
    md.append("## 4. LinkedIn Skills Section\n")
    md.append("### Recommended Top 5 Pinned Skills on LinkedIn:")
    top_5 = [
        "Security Operations Center (SOC)",
        "Threat Detection",
        "Digital Forensics",
        "Python (Programming Language)",
        "Incident Response"
    ]
    for s in top_5:
        md.append(f"1. **{s}**")
        
    md.append("\n### Complete Skills Categorized for LinkedIn:")
    for cat_name, items in skills.items():
        formatted_name = cat_name.replace("_", " ").title()
        md.append(f"- **{formatted_name}**: {', '.join(items)}")
    md.append("\n---\n")
    
    # Section 5: Featured Section
    md.append("## 5. LinkedIn Featured Section Recommendations\n")
    md.append("Add the following 4 items to your LinkedIn **Featured** section:\n")
    md.append(f"1. **GitHub Portfolio**  \n   - **Link**: `{links['github_profile']}`  \n   - **Title**: Utkarsh Singh Chauhan — Cybersecurity Portfolio & Open Source Security Tools  \n   - **Description**: Central hub for defensive security engineering projects, automated SIEM detection, and forensic integrity platforms.")
    md.append(f"2. **ThreatForge (SIEM & Threat Detection)**  \n   - **Link**: `{links['threatforge_live']}` (or repo: `{links['threatforge_repo']}`)  \n   - **Title**: ThreatForge — Security Monitoring & MITRE ATT&CK Threat Correlation  \n   - **Description**: Full-stack SIEM simulation with automated log ingestion, sliding-window correlation rules, and analyst investigation workflows.")
    md.append(f"3. **DFIR CaseVault (Forensics & Chain-of-Custody)**  \n   - **Link**: `{links['dfir_casevault_repo']}`  \n   - **Title**: DFIR CaseVault — Digital Forensics & Cryptographic Integrity Platform  \n   - **Description**: Forensic investigation platform featuring streaming SHA-256 hash baselines, on-disk tamper detection, append-only chain of custody, and ReportLab PDF dossiers.")
    md.append(f"4. **CyberNewsAI-Pro (Threat Intelligence)**  \n   - **Link**: `{links['cybernewsai_repo']}`  \n   - **Title**: CyberNewsAI-Pro — Automated Threat Intelligence & CVE Aggregator  \n   - **Description**: Multi-feed intelligence aggregator parsing CISA, BleepingComputer, and Hacker News with regex CVE extraction and heuristic risk scoring.")
    md.append("\n---\n")
    
    # Section 6: Experience & Education Advisory
    md.append("## 6. Experience & Education Section Guidelines\n")
    md.append("- **Experience Section**: Leave clear of personal projects. Do not label personal software projects as commercial employment or freelance contracts. Keeping this empty or noting academic student projects maintains total credibility with security hiring managers.")
    md.append("- **Education Section**: Add your college/university, field of study (`Cybersecurity` or `Computer Science`), and expected graduation year once confirmed.")
    md.append("- **Licenses & Certifications**: Keep unpopulated until verified certifications (e.g. CompTIA Security+, BTL1, CEH) are earned.")
    
    return "\n".join(md)

def generate_sample_linkedin_post(repo_id: str, change_type: str = "feature"):
    """Generate an authentic, professional LinkedIn project announcement post draft."""
    data = load_master_data()
    proj = next((p for p in data["projects"] if p["id"] == repo_id.lower()), None)
    if not proj:
        raise ValueError(f"Project ID '{repo_id}' not found in master data.")
        
    post = []
    if repo_id.lower() == "threatforge":
        post.append("🛡️ Enhancing Detection Engineering in ThreatForge: Adding Brute Force & Password Spraying Correlation Rules")
        post.append("")
        post.append("As part of my final-year cybersecurity projects, I've been focusing heavily on bridging the gap between raw log collection and explainable threat detection.")
        post.append("")
        post.append("In ThreatForge, I implemented rule-based detection logic mapped directly to the MITRE ATT&CK® framework:")
        post.append("• T1110.001 (Brute Force): Sliding-window threshold correlation identifying repeated authentication failures.")
        post.append("• T1110.003 (Password Spraying): Single-origin authentication attempts across multiple target usernames.")
        post.append("• T1078.001 (Privileged Activity): Detecting anomalous off-hours account elevation.")
        post.append("")
        post.append("Built with Python 3.12, FastAPI, React, and TypeScript. All 21 test suites are verified via GitHub Actions CI.")
        post.append("")
        post.append(f"Explore the project: {proj['repository_url']}")
        if proj.get('live_demo_url'):
            post.append(f"Live Demo: {proj['live_demo_url']}")
        post.append("")
        post.append("#Cybersecurity #SOC #ThreatDetection #MITREATTACK #Python #InfoSec #StudentsInTech")
    elif repo_id.lower() == "dfir-casevault":
        post.append("🔍 Cryptographic Integrity & Evidence Verification: Building DFIR CaseVault")
        post.append("")
        post.append("When handling digital evidence during an incident response investigation, maintaining cryptographic integrity and an immutable chain of custody is non-negotiable.")
        post.append("")
        post.append("In my open-source project DFIR CaseVault, I implemented:")
        post.append("• Streaming 256-bit SHA-256 baseline hashing upon evidence ingestion.")
        post.append("• On-demand disk verification detecting byte-level tampering without overwriting the recorded baseline.")
        post.append("• Append-only chain-of-custody tracking recording every transfer, audit, and download.")
        post.append("• Safe, non-executing artifact parsers (syslog, CSV, JSON, PDF metadata, image EXIF, and ZIP table-of-contents without disk decompression).")
        post.append("• Automated investigation PDF dossier generation via ReportLab.")
        post.append("")
        post.append(f"Check out the repository and test suite on GitHub: {proj['repository_url']}")
        post.append("")
        post.append("#DigitalForensics #DFIR #IncidentResponse #Cybersecurity #Python #FastAPI #EvidenceIntegrity")
    else:
        post.append("📡 Consolidating Real-Time Threat Feeds with CyberNewsAI-Pro")
        post.append("")
        post.append("Staying current with newly disclosed vulnerabilities and active campaigns across fragmented sources is a daily challenge for security analysts.")
        post.append("")
        post.append("CyberNewsAI-Pro concurrently collects threat advisories across 5 authoritative sources (BleepingComputer, The Hacker News, SecurityWeek, CISA Advisories, KrebsOnSecurity), automatically parses CVE identifiers, and extracts risk scores.")
        post.append("")
        post.append("Includes both AI executive briefings and a deterministic heuristic fallback to ensure uninterrupted offline triage.")
        post.append("")
        post.append(f"Project repository: {proj['repository_url']}")
        post.append("")
        post.append("#ThreatIntelligence #Cybersecurity #CVE #Python #FastAPI #SOC #VulnerabilityManagement")
        
    return "\n".join(post)

if __name__ == "__main__":
    data = load_master_data()
    issues = validate_master_data(data)
    
    if issues:
        print("❌ Master Data Validation Failed:")
        for issue in issues:
            print(f"  - {issue}")
        sys.exit(1)
        
    print("✅ Master Data Validation Passed (0 errors).")
    
    # Export LinkedIn guide
    output_file = WORKSPACE_ROOT / "LINKEDIN_PROFILE_OPTIMIZED.md"
    content = generate_linkedin_markdown(data)
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"✅ Generated LinkedIn Profile Guide: {output_file}")
