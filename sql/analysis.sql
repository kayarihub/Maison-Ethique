-- Execute against outputs/maison_ethique.sqlite after python3 src/build.py
-- 1. Internal risk tier distribution (not statutory AI Act classification)
SELECT risk_tier, COUNT(*) AS systems, ROUND(AVG(risk_score),1) AS avg_score
FROM systems GROUP BY risk_tier ORDER BY avg_score DESC;

-- 2. Control implementation rates by governance framework
SELECT framework, COUNT(*) AS assessments,
SUM(CASE WHEN status='Implemented' THEN 1 ELSE 0 END) AS implemented,
ROUND(100.0 * SUM(CASE WHEN status='Implemented' THEN 1 ELSE 0 END)/COUNT(*),1) AS implementation_pct
FROM assessments GROUP BY framework ORDER BY implementation_pct;

-- 3. High-priority systems with unresolved controls
SELECT s.system_id,s.name,s.department,s.risk_score,
SUM(CASE WHEN a.status IN ('Missing','Partial') THEN 1 ELSE 0 END) AS open_findings
FROM systems s JOIN assessments a USING(system_id)
WHERE s.risk_tier='High' GROUP BY s.system_id ORDER BY open_findings DESC,s.risk_score DESC;

-- 4. Synthetic fairness audit: group selection rates
SELECT group_label, COUNT(*) AS sample_size,
SUM(positive_decision) AS positive_decisions,
ROUND(100.0 * AVG(positive_decision),2) AS selection_rate_pct
FROM fairness_audit GROUP BY group_label ORDER BY selection_rate_pct DESC;

-- 5. Conditional selection rate among synthetic eligible cases
SELECT group_label, COUNT(*) AS eligible_cases,
ROUND(100.0 * AVG(positive_decision),2) AS conditional_selection_pct
FROM fairness_audit WHERE eligible_proxy=1 GROUP BY group_label;