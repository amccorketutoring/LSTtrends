"""
Unit tests for summer_trend.py module.
"""

import sys
from pathlib import Path
import unittest

# Add the project root (LSTtrends/) to sys.path for local imports
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

import pandas as pd

# Import the module you want to test
import lsttrends.summer_trend as summer_trend


class TestSummerTrend(unittest.TestCase):
    def test_compute_summer_lst_trend(self):
        """
        Test whether compute_summer_lst_trend returns a positive float
        when given increasing LST values.
        """
        # Simulated LST trend data
        df = pd.DataFrame(
            {
                "year": [2000, 2005, 2010, 2015, 2020],
                "lst": [30.2, 31.0, 32.1, 32.8, 34.0],
            }
        )

        trend = summer_trend.compute_summer_lst_trend(df)

        # Assertions
        self.assertIsInstance(trend, float)
        self.assertGreater(round(trend, 1), 0)  # Expect increasing trend

    def test_zero_or_negative_trend(self):
        df = pd.DataFrame(
            {
                "year": [2000, 2005, 2010, 2015, 2020],
                "lst": [34.0, 33.8, 33.0, 32.8, 32.0],
            }
        )
        trend = summer_trend.compute_summer_lst_trend(df)
        self.assertIsInstance(trend, float)
        self.assertLessEqual(round(trend, 1), 0)  # Expect decreasing or flat trend


if __name__ == "__main__":
    unittest.main()
