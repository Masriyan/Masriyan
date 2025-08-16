## 🔐 About Me

Cybersecurity professional specializing in SOC leadership, threat hunting, cyber threat intelligence, and attack surface management. I build efficient, intelligence-driven security operations that go beyond alert monitoring to deliver real-world threat mitigation.

> *"Cybersecurity is more than tools — it’s a strategy."*

---

## 🧭 Open-Source Highlights

- **[MacFIRE](https://github.com/Masriyan/MacFIRE)** — macOS DFIR collection & imaging toolkit: timeline, memory, rootkit checks, HTML reporting.
- **[Aegis](https://github.com/Masriyan/Aegis)** — Windows-friendly single-file Python web app for URL recon, OSINT enrichment, subdomain intel, history & exports.
- **[ExpertXSS](https://github.com/Masriyan/ExpertXSS)** — Python XSS scanner that fetches the latest payloads automatically.
- **[ExpertRecon](https://github.com/Masriyan/ExpertRecon)** — Recon & exploitation helper integrating multi-tech discovery and third-party APIs.
- **[No-Secret-Scan](https://github.com/Masriyan/No-Secret-Scan-)** — Find exposed secrets / hard-coded credentials in web pages.
- **[No-Secret-Scan for GitHub/GitLab](https://github.com/Masriyan/No-Secret-Scan-Github-Gitlab)** — Scan repos for API keys and tokens across history.
- **[uclsoc_code](https://github.com/Masriyan/uclsoc_code)** — Curated SIEM detection logic library mapped by domain & framework.
- **[Kalitellingence](https://github.com/Masriyan/Kalitellingence)** — One-shot Kali setup for Threat Intel & dark-web workflows.

---

## 🧑‍💻 Programming Languages

<p align="left">
  <a href="https://www.python.org/" target="_blank" rel="noreferrer">
    <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python"/>
  </a>
  <a href="https://www.php.net/" target="_blank" rel="noreferrer">
    <img src="https://img.shields.io/badge/PHP-777BB4?style=for-the-badge&logo=php&logoColor=white" alt="PHP"/>
  </a>
  <a href="https://developer.mozilla.org/docs/Web/JavaScript" target="_blank" rel="noreferrer">
    <img src="https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black" alt="JavaScript"/>
  </a>
  <a href="https://tailwindcss.com/" target="_blank" rel="noreferrer">
    <img src="https://img.shields.io/badge/Tailwind_CSS-38B2AC?style=for-the-badge&logo=tailwindcss&logoColor=white" alt="Tailwind CSS"/>
  </a>
</p>

## ⚙️ Frameworks & Libraries

<p align="left">
  <a href="https://flask.palletsprojects.com/" target="_blank" rel="noreferrer">
    <img src="https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white" alt="Flask"/>
  </a>
  <a href="https://fastapi.tiangolo.com/" target="_blank" rel="noreferrer">
    <img src="https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white" alt="FastAPI"/>
  </a>
  <a href="https://laravel.com/" target="_blank" rel="noreferrer">
    <img src="https://img.shields.io/badge/Laravel-FF2D20?style=for-the-badge&logo=laravel&logoColor=white" alt="Laravel"/>
  </a>
  <a href="https://expressjs.com/" target="_blank" rel="noreferrer">
    <img src="https://img.shields.io/badge/Express.js-000000?style=for-the-badge&logo=express&logoColor=white" alt="Express.js"/>
  </a>
  <a href="https://alpinejs.dev/" target="_blank" rel="noreferrer">
    <img src="https://img.shields.io/badge/Alpine.js-8BC0D0?style=for-the-badge&logo=alpinedotjs&logoColor=black" alt="Alpine.js"/>
  </a>
  <a href="https://tailwindcss.com/" target="_blank" rel="noreferrer">
    <img src="https://img.shields.io/badge/Tailwind%20CSS-38B2AC?style=for-the-badge&logo=tailwindcss&logoColor=white" alt="Tailwind CSS"/>
  </a>
</p>

---

## 🛡️ Expertise

- **Threat Hunting & Incident Analysis** — Identify hidden threats and attacker behavior *before* incidents escalate.
- **SOC Strategy & Development** — Design efficient SOC frameworks to improve detection, response, and operations.
- **Cyber Threat Intelligence & OSINT** — Turn intelligence into actionable insights for decisions and adversary tracking.
- **Cloud Security & Attack Surface Management** — Secure cloud environments, reduce misconfigurations, minimize exposure.
- **Security Automation & Process Optimization** — Use automation and analytics to boost efficiency and reduce false positives.

---

## 📈 Visuals (Mermaid)

> GitHub tip: use quoted labels like `A["Text"]` to avoid parser errors with special characters.

### Tech Stack at a Glance
```mermaid
pie title Primary Tech Stack
  "Python" : 40
  "PHP" : 25
  "JavaScript" : 25
  "Tailwind CSS" : 10
```

### Threat Hunting Workflow
```mermaid
flowchart TD
  A["Collect Signals"] --> B["Enrich: WHOIS · OSINT · VT · Shodan"]
  B --> C["Detect and Correlate: SIEM rules · UEBA"]
  C --> D{"Suspicious"}
  D -- "Yes" --> E["Hunt Loop: pivot → query → timeline"]
  D -- "No"  --> H["Autoclose and Tune Rules"]
  E --> F["Triage and Contain"]
  F --> G["Incident Response: Mitigate and Eradicate"]
  G --> I["Lessons Learned"]
  I --> J["Automate: SOAR XSOAR · scripts"]
  J --> C
```

### Project Roadmap (Illustrative)
```mermaid
gantt
  title 2025 Roadmap (Illustrative)
  dateFormat  YYYY-MM-DD
  axisFormat  %b %d

  section Aegis
  Subdomain Intelligence      :active, a1, 2025-06-01, 30d
  Tailwind UI Redesign        :a2, after a1, 20d

  section MacFIRE
  Memory Forensics Module     :m1, 2025-07-10, 25d
  HTML Report v2              :m2, after m1, 20d

  section ExpertXSS
  Payload Auto Update         :x1, 2025-05-20, 15d
  CI CD and Tests             :x2, after x1, 20d
```

### Repo Ecosystem Map
```mermaid
flowchart LR
  Me(("Riyan Pratama"))
  Me --> MacFIRE["MacFIRE"]
  Me --> ExpertXSS["ExpertXSS"]
  Me --> ExpertRecon["ExpertRecon"]
  Me --> Aegis["Aegis"]
  Me --> NSS["No Secret Scan"]
  Me --> NSSGL["No Secret Scan GitHub GitLab"]
  Me --> UCLS["uclsoc_code"]

  Me -.-> PY["Python"]
  Me -.-> PHP["PHP"]
  Me -.-> JS["JavaScript"]
  Me -.-> TW["Tailwind CSS"]

  MacFIRE --> PY
  ExpertXSS --> PY
  ExpertRecon --> PY
  Aegis --> PY
  Aegis --> JS
  NSS --> JS
  NSSGL --> JS
  UCLS --> PY
```

---

## 📌 Pinned Repositories

<div align="center">
  <a href="https://github.com/Masriyan/MacFIRE" rel="noreferrer">
    <img align="center" src="https://github-readme-stats.vercel.app/api/pin/?username=Masriyan&repo=MacFIRE&theme=radical" alt="MacFIRE"/>
  </a>
  <a href="https://github.com/Masriyan/Aegis" rel="noreferrer">
    <img align="center" src="https://github-readme-stats.vercel.app/api/pin/?username=Masriyan&repo=Aegis&theme=radical" alt="Aegis"/>
  </a>
  <a href="https://github.com/Masriyan/ExpertXSS" rel="noreferrer">
    <img align="center" src="https://github-readme-stats.vercel.app/api/pin/?username=Masriyan&repo=ExpertXSS&theme=radical" alt="ExpertXSS"/>
  </a>
  <a href="https://github.com/Masriyan/ExpertRecon" rel="noreferrer">
    <img align="center" src="https://github-readme-stats.vercel.app/api/pin/?username=Masriyan&repo=ExpertRecon&theme=radical" alt="ExpertRecon"/>
  </a>
  <a href="https://github.com/Masriyan/No-Secret-Scan-" rel="noreferrer">
    <img align="center" src="https://github-readme-stats.vercel.app/api/pin/?username=Masriyan&repo=No-Secret-Scan-&theme=radical" alt="No-Secret-Scan"/>
  </a>
  <a href="https://github.com/Masriyan/No-Secret-Scan-Github-Gitlab" rel="noreferrer">
    <img align="center" src="https://github-readme-stats.vercel.app/api/pin/?username=Masriyan&repo=No-Secret-Scan-Github-Gitlab&theme=radical" alt="No-Secret-Scan GitHub/GitLab"/>
  </a>
</div>

---

## 📊 GitHub Stats

<div align="center">
  <a href="https://github.com/Masriyan" rel="noreferrer">
    <img height="180em" src="https://github-readme-stats.vercel.app/api?username=Masriyan&show_icons=true&theme=dracula&include_all_commits=true&count_private=true" alt="GitHub stats"/>
    <img height="180em" src="https://github-readme-stats.vercel.app/api/top-langs/?username=Masriyan&layout=compact&langs_count=8&theme=dracula" alt="Top languages"/>
  </a>
</div>

<div align="center">
  <img src="https://github-readme-streak-stats.herokuapp.com/?user=Masriyan&theme=dracula" alt="GitHub streak"/>
</div>

---

## 🔧 Skills & Tools

```text
🔐 Security          ██████████████████████░░   90%
🕵️ Threat Hunting    ██████████████████████░░   90%
🛡️ SIEM              █████████████████████░░░   85%
🔍 OSINT             ████████████████████░░░░   80%
🧪 Incident Response █████████████████████░░░   85%
🖥️ Network Security  ████████████████████░░░░   80%
```

---

## 📫 Connect with Me

<div align="center">
  <a href="https://www.linkedin.com/in/administratorpanel" target="_blank" rel="noreferrer">
    <img src="https://img.shields.io/badge/LinkedIn-administratorpanel-0077B5?style=for-the-badge&logo=linkedin&logoColor=white" alt="LinkedIn: administratorpanel"/>
  </a>
  <a href="https://sudo3rs.medium.com/" target="_blank" rel="noreferrer">
    <img src="https://img.shields.io/badge/Medium-sudo3rs-12100E?style=for-the-badge&logo=medium&logoColor=white" alt="Medium: sudo3rs"/>
  </a>
</div>

---

## 👨‍🌾 Fun Facts

- Owner of **Wedusku Farm** (goat farmer 🐐)
- Expert in *ngarit* (traditional grass cutting for animal feed)
- I build security solutions while nurturing my farm

---

<div align="center">
  <img src="https://komarev.com/ghpvc/?username=Masriyan&label=Profile%20views&color=blueviolet&style=flat" alt="Profile views counter"/>
  <p>Thanks for visiting my profile! Have a nice day! 🙌</p>
</div>
