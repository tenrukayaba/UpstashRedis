# test_upstashredis.py
"""
Tests for UpstashRedis module.
"""

import unittest
from upstashredis import UpstashRedis

class TestUpstashRedis(unittest.TestCase):
    """Test cases for UpstashRedis class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = UpstashRedis()
        self.assertIsInstance(instance, UpstashRedis)
        
    def test_run_method(self):
        """Test the run method."""
        instance = UpstashRedis()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
