"""Unit tests for the synthetic risk triage model."""
import sys
import unittest
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/"src"))
from build import WEIGHTS, risk_score, risk_tier

class RiskScoringTests(unittest.TestCase):
    def test_weights_sum_to_one(self):
        self.assertAlmostEqual(sum(WEIGHTS.values()),1.0)
    def test_score_range(self):
        self.assertEqual(risk_score({key:1 for key in WEIGHTS}),20)
        self.assertEqual(risk_score({key:5 for key in WEIGHTS}),100)
    def test_tier_thresholds(self):
        self.assertEqual(risk_tier(44),"Low")
        self.assertEqual(risk_tier(45),"Medium")
        self.assertEqual(risk_tier(69),"Medium")
        self.assertEqual(risk_tier(70),"High")
if __name__=="__main__":
    unittest.main()
