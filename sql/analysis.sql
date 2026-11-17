-- Maison Éthique: run after python3 src/build.py
-- Adjust column names if adapting the data model.
SELECT * FROM sqlite_master WHERE type='table' ORDER BY name;
-- Explore internal risk distribution
SELECT risk_tier, COUNT(*) AS system_count FROM systems GROUP BY risk_tier;
-- Note: Internal risk tier is not a legal EU AI Act classification.
