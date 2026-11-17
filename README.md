<div align="center">

![Maison Éthique pink banner](assets/maison-ethique-banner.svg)

# 💗 Maison Éthique 💗
### 🎀 The AI Risk Atelier 🎀

*Where luxury meets responsible intelligence.* ✨

![Python](https://img.shields.io/badge/Python-Analytics-F8BBD0?style=for-the-badge)
![SQL](https://img.shields.io/badge/SQLite-Governance%20Queries-F2B6D0?style=for-the-badge)
![Dashboard](https://img.shields.io/badge/Dashboard-Pink%20%26%20Interactive-FFE0ED?style=for-the-badge)
![Data](https://img.shields.io/badge/Data-100%25%20Synthetic-E9B2CA?style=for-the-badge)

</div>

## 🎀 Explore the Google Data Studio report

<div align="center">

### 💗 [Open the Maison Éthique Interactive Dashboard](https://datastudio.google.com/reporting/82b07e34-b80e-4511-baea-e2e5079fccf8)

*Executive risk KPIs · AI risk distribution · Department-level analysis · Governance control status*

</div>

The report uses synthetic datasets and includes four visualizations in this first release. Additional charts and fairness-audit views are planned for future versions. **Viewer access depends on the report's Google Data Studio sharing settings.** If a visitor sees a permission prompt, the owner needs to enable link-based viewing and ensure that data-source credentials allow report viewers to load the charts.

## 💗 Portfolio case study — first release (v1.0)

**The first dashboard iteration is complete.** Additional charts are reserved for v1.1.

**Built in Google Data Studio:**
- 🎀 Executive scorecards: **24 AI systems**, **134 open findings**, **56.42 average internal risk**
- 🌸 Risk-tier donut: 11 Medium (45.8%), 7 High (29.2%), 6 Low (25%)
- 🩷 Department-risk bars: Payments (78), Clienteling (72), People (71) have the highest synthetic average scores
- 🪞 Governance-control stacked bars: Implemented / Partial / Missing / Not assessed across NIST AI RMF, EU AI Act and GDPR considerations

**Underlying synthetic study:** 24 systems · 264 assessments · 104 implemented · 134 Partial/Missing · 2,400 fairness cases. **These are simulated governance signals, not legal compliance findings.**

📓 [Read the v1.0 release notes and future dashboard roadmap](docs/release-notes-v1.md).

**Publishing status:** This repository currently holds the project documentation, banner and SQL starter. The separate downloadable v1.0 project archive contains the complete tested Python source, synthetic datasets, SQLite outputs, dashboard, and four report screenshots. The Google Data Studio report URL is now linked above; public viewer access has not been independently verified.

## 🩰 Bonjour, governance girlies!

**Maison Éthique** is a luxury-inspired AI governance and compliance portfolio simulation. Imagine a fictional luxury group using AI in personal shopping, marketing, beauty, authentication, recruitment, and supply chain. The goal is to prioritize risks, assess governance controls, explore fairness signals, and document regulatory considerations in a polished pink dashboard. 💕

> 💌 **Transparency first:** All AI systems, assessments, customer-like cases, scores, and outcomes are **synthetic**. Internal risk tiers are **not EU AI Act legal classifications**, and this project is neither legal advice nor a compliance certification.

## 🎀 What's in the atelier?

- 🌸 **AI system register:** 24 fictional luxury-industry use cases
- 💗 **Risk scoring:** Weighted internal prioritization across five dimensions
- 🧁 **Fairness audit:** 2,400 simulated decisions with group-level selection rates
- 🪞 **Governance mapping:** NIST AI RMF, GDPR, and EU AI Act considerations
- 🩷 **Interactive dashboard:** Department, risk-tier, and framework filters
- ✨ **SQL analytics:** Risk concentration, control status, and fairness metrics

## 💻 Let's get glam

Python 3.9+ is sufficient; no third-party packages needed.

```bash
python3 src/build.py
python3 -m unittest discover -s tests
open dashboard/index.html
```

The fixed-seed generator writes synthetic CSVs to `data/`, a SQLite database and fairness metrics to `outputs/`, and a standalone pink dashboard to `dashboard/index.html`.

## 🌷 How the risk score works

| 💕 Dimension | 🎀 Weight |
|---|---:|
| Potential impact | 30% |
| Data sensitivity | 25% |
| Autonomy | 20% |
| Scale | 15% |
| Opacity | 10% |

Each dimension scores 1–5; the weighted result is scaled to 0–100 style (minimum possible score 20). **Low below 45 · Medium 45–69 · High 70+.** This is an illustrative *internal* rubric, not a legal classification.

## ⚖️ A little legal sparkle

- 💗 **NIST AI RMF:** Voluntary guidance structured around Govern, Map, Measure, and Manage.
- 🌸 **GDPR:** Binding where applicable; assess legal basis, data rights, and possible DPIA obligations.
- 🎀 **EU AI Act:** Requirements depend on the system's purpose, provider/deployer role, legal classification, and applicable dates. **Internal “High” does not mean legally “high-risk AI.”**

See [methodology](docs/methodology.md) for assumptions and limitations.

## 🗂️ What's in my beauty bag?

```text
maison-ethique/
├── README.md
├── assets/maison-ethique-banner.svg
├── src/build.py
├── sql/analysis.sql
├── dashboard/template.html
├── dashboard/index.html
├── data/*.csv
├── outputs/
├── docs/methodology.md
└── tests/test_build.py
```

## 💼 Skills, but make them chic

**Python ETL** · **SQL** · **AI risk assessment** · **Fairness auditing** · **Governance controls** · **Regulatory mapping** · **Data visualization** · **Executive storytelling**

## 📚 Official references

- [NIST AI Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework)
- [EU AI Act (EUR-Lex)](https://eur-lex.europa.eu/eli/reg/2024/1689/oj)
- [GDPR (EUR-Lex)](https://eur-lex.europa.eu/eli/reg/2016/679/oj)

---

<div align="center">

### 💕 Thank you for visiting the atelier!

*Ethics is always in style.* 🎀 🌸 ✨

</div>