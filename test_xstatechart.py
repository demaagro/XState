# test_xstatechart.py
"""
Tests for XStateChart module.
"""

import unittest
from xstatechart import XStateChart

class TestXStateChart(unittest.TestCase):
    """Test cases for XStateChart class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = XStateChart()
        self.assertIsInstance(instance, XStateChart)
        
    def test_run_method(self):
        """Test the run method."""
        instance = XStateChart()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
