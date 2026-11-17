# Methodology and limitations

## Internal triage scoring
Weighted score = 100 × (0.30 impact + 0.25 data sensitivity + 0.20 autonomy + 0.15 scale + 0.10 opacity) / 5. Scores are based on integer dimensions 1–5. Thresholds: Low below 45; Medium 45–69; High 70+. These are illustrative internal triage scores, **not EU AI Act legal classifications**.

## Control assessments
Eleven governance prompts are mapped to voluntary NIST AI RMF guidance and considerations under GDPR and the EU AI Act. These are educational mappings only; the script assigns fictional status using a seeded pseudorandom generator. A status does not certify legal compliance, and applicability requires assessment of context, actor role, purpose, and jurisdiction.

## Fairness signals
2,400 entirely fictional offer decisions, across three arbitrarily named synthetic groups. Selection rate = positive decisions / cases within a group. Conditional rate (true-positive-rate **proxy**) = positive decisions in rows with synthetic eligible_proxy=1 / eligible rows. Maximum selection-rate gap and minimum/maximum rate ratio are descriptive screening indicators. They do not prove causation, discrimination or compliance. The simulator intentionally introduces probability differences by group.

## Regulatory sources
- NIST AI RMF (voluntary): https://www.nist.gov/itl/ai-risk-management-framework
- GDPR official text: https://eur-lex.europa.eu/eli/reg/2016/679/oj
- EU AI Act official text: https://eur-lex.europa.eu/eli/reg/2024/1689/oj

Always consult current official consolidated texts and implementation guidance when analyzing real AI systems. The EU AI Act involves different obligations and staged application dates.

## Reproducibility
Use Python 3.9+ and run `python3 src/build.py` from the repository root. The script generates synthetic CSV data, a SQLite database, a JSON summary, fairness metrics, and `dashboard/index.html` from `dashboard/template.html`. Run `python3 -m unittest discover -s tests` to check scoring invariants.

## Limitations
No real luxury brand, person, customer data, deployed model, documented legal determination, causal fairness finding, regulatory assessment, or production control framework is represented. For portfolio demonstration and learning only.
