<div align="center">

# Hi, I'm Utkarsh Singh Chauhan.
### Cybersecurity Student | SOC Analyst Aspirant

**Gujarat, India** • Security Monitoring • Threat Detection • Digital Forensics & Incident Response (DFIR)

[![GitHub](https://img.shields.io/badge/GitHub-utkarshchauhaniitk--star-00B4D8?style=flat-square&logo=github&logoColor=white)](https://github.com/utkarshchauhaniitk-star)
[![Email](https://img.shields.io/badge/Email-utkarshchauhaniitk%40gmail.com-EA4335?style=flat-square&logo=gmail&logoColor=white)](mailto:utkarshchauhaniitk@gmail.com)
[![ThreatForge Live Demo](https://img.shields.io/badge/Live_Project-ThreatForge_SIEM-10B981?style=flat-square&logo=vercel&logoColor=white)](https://threatforge.vercel.app)

</div>

---

## 🛡️ Professional Introduction

I am a final-year cybersecurity student based in Gujarat, India, preparing for cybersecurity internships and entry-level security operations roles. My core interests center on **Security Operations Center (SOC) workflows**, **security monitoring**, **threat detection engineering**, and **digital forensics and incident response (DFIR)**.

Rather than focusing solely on theoretical concepts, I build practical, defensive security tools to understand how security telemetry is ingested, how attack patterns map to real-world adversary tactics, and how analysts can triage and investigate incidents efficiently.

---

## 🎯 Career Focus

- **Security Operations Center (SOC)**: Alert triage, security event monitoring, shift handoffs, and escalation procedures.
- **Security Monitoring & Log Analysis**: Telemetry ingestion from syslogs, authentication records, and firewall connection logs.
- **Threat Detection Engineering**: Designing explainable, correlation-based detection logic mapped to adversary behaviors.
- **Digital Forensics & Incident Response (DFIR)**: Case investigation lifecycles, forensic note-taking, timeline analysis, and root-cause identification.
- **Threat Intelligence**: Monitoring emerging vulnerabilities (CVEs), threat advisories, and indicators of compromise (IoCs).
- **Security Automation**: Writing Python utilities to normalize telemetry, automate repetitive triage tasks, and compile audit summaries.

---

## 🧰 Technical Skills

Skills and tools I work with across my practical projects and academic studies:

| Category | Tools & Technologies |
| :--- | :--- |
| **Programming & Scripting** | Python, JavaScript, SQL (SQLite, PostgreSQL), Bash |
| **Cybersecurity Concepts** | Security Monitoring, Log Telemetry Analysis, Threat Detection, MITRE ATT&CK® Mapping, Digital Forensics, Incident Triage |
| **Security Tools** | Splunk (SIEM), Kali Linux, FTK (Forensic Toolkit), DUMP IT (Memory Acquisition) |
| **Development** | FastAPI, React, Node.js, Vite, Tailwind CSS, REST APIs |
| **Infrastructure & Systems** | Linux / Unix CLI, Docker, Git, GitHub, GitHub Actions CI/CD |

---

## 🚀 Existing Projects

### 1. 🛡️ ThreatForge — Security Monitoring & Threat Detection Platform (Primary Project)
**Repository**: [github.com/utkarshchauhaniitk-star/threatforge](https://github.com/utkarshchauhaniitk-star/threatforge) &nbsp;|&nbsp; **Live Application**: [threatforge.vercel.app](https://threatforge.vercel.app) &nbsp;|&nbsp; **License**: MIT

ThreatForge is a full-stack security monitoring and threat detection platform built to simulate real-world SOC workflows. It addresses the challenge security analysts face when ingesting raw, heterogeneous telemetry from authentication services, firewalls, and servers by normalizing logs into a standardized schema and executing deterministic correlation rules.

<p align="center">
  <a href="https://threatforge.vercel.app">
    <img src="https://raw.githubusercontent.com/utkarshchauhaniitk-star/threatforge/main/docs/screenshots/dashboard.png" width="95%" alt="ThreatForge Security Monitoring Dashboard" />
  </a>
</p>

- **Purpose**: Bridge the gap between raw log collection and explainable incident response for defensive security learners and junior analysts.
- **Technology Stack**: Python 3.12, FastAPI, SQLAlchemy 2.0, SQLite / PostgreSQL, React 18, TypeScript 5.7, Vite, Tailwind CSS, Recharts.
- **Key Implemented Features**:
  - **Telemetry Ingestion & Schema Normalization**: Ingests JSON and CSV logs (auth logs, firewall drops, web access records) with automatic field mapping.
  - **Rule-Based Threat Correlation**: Implements detection logic mapped directly to the **MITRE ATT&CK®** framework:
    - `T1110.001` — Brute Force (Password Guessing) via sliding-window failed attempt thresholds.
    - `T1110.003` — Password Spraying across multiple usernames from a single origin.
    - `T1078.001` — Unusual Privileged Activity and sensitive account elevation attempts.
    - `T1046` — Network Service Discovery and denied connection bursts.
  - **SOC Case Management**: Full investigation workspace with severity assignment, status lifecycle tracking (`Open`, `In Progress`, `Closed`), and timestamped analyst forensic notes.
  - **Executive Audit Reports**: Automated generation of incident summaries and exportable compliance briefs.
  - **Automated Verification**: Comprehensive test coverage with 15 Pytest backend test suites and 6 Vitest frontend test suites running via GitHub Actions CI.

---

### 2. 📡 CyberNewsAI-Pro — Cybersecurity Threat Intelligence Platform
**Repository**: [github.com/utkarshchauhaniitk-star/CyberNewsAI-Pro](https://github.com/utkarshchauhaniitk-star/CyberNewsAI-Pro) &nbsp;|&nbsp; **License**: MIT

CyberNewsAI-Pro is an automated threat intelligence aggregator that continuously collects, categorizes, and analyzes emerging security advisories, vulnerability disclosures, and CVEs across authoritative global research feeds.

<p align="center">
  <a href="https://github.com/utkarshchauhaniitk-star/CyberNewsAI-Pro">
    <img src="https://raw.githubusercontent.com/utkarshchauhaniitk-star/CyberNewsAI-Pro/main/docs/screenshots/radar-feed.png" width="95%" alt="CyberNewsAI Threat Intelligence Radar Feed" />
  </a>
</p>

- **Purpose**: Accelerate vulnerability research and situational awareness by consolidating disparate threat feeds into a unified dashboard with automated risk classification.
- **Technology Stack**: Python 3.12, FastAPI, SQLite (WAL mode), React 19, Vite, Tailwind CSS, Google Gemini API (with deterministic heuristic fallback).
- **Key Implemented Features**:
  - **Multi-Feed Concurrent Ingestion**: Ingests live threat advisories from 5 authoritative research feeds: BleepingComputer, The Hacker News, SecurityWeek, CISA Advisories, and KrebsOnSecurity.
  - **Deterministic CVE Extraction**: Regex-based detection of Common Vulnerabilities and Exposures (`CVE-YYYY-NNNN+`) with automated severity calculation.
  - **AI & Heuristic Briefings**: Synthesizes concise executive summaries using the Google Gemini API with fallback to deterministic keyword-based heuristics when API keys are not supplied.
  - **Analyst HUD**: Interactive interface featuring dynamic category filtering, severity badges, CVE search, and Pin-to-Vault bookmarking.
  - **Automated Testing**: 8 backend API verification tests and GitHub Actions CI workflow.

---

## 📖 Current Learning & Skill Development

I am actively dedicating time every week to deepen my defensive security capabilities through hands-on labs and technical study:

- **SOC Operations & Incident Handling**: Deepening hands-on practice with triage playbooks, event timeline reconstruction, and false-positive reduction.
- **SIEM & Query Languages**: Building deeper proficiency in Splunk search processing language (SPL) for correlation and log searching.
- **Detection Engineering**: Studying Sigma rules and transforming threat intelligence indicators into robust detection signatures.
- **Digital Forensics & Artifact Analysis**: Practicing disk and memory forensics analysis using FTK, DUMP IT, and Volatility in isolated lab environments.
- **Python for Security**: Expanding Python automation scripts for log parsing, API integration, and automated evidence collection.

---

## 📬 Contact & Links

- **GitHub**: [github.com/utkarshchauhaniitk-star](https://github.com/utkarshchauhaniitk-star)
- **Email**: [utkarshchauhaniitk@gmail.com](mailto:utkarshchauhaniitk@gmail.com)
- **LinkedIn**: [Connect on LinkedIn](https://www.linkedin.com) *(Add your personal profile link)*
- **Location**: Gujarat, India
- **Status**: Open to Cybersecurity Internships & Entry-Level SOC Analyst Opportunities
