import unittest
import os
from modules.base_agent import BaseAgent


class TestAgent(BaseAgent):
    def execute(self):
        pass


class TestBaseAgent(unittest.TestCase):
    def setUp(self):
        """Set up test environment."""
        self.agent = TestAgent("test_project")

    def test_logging_setup(self):
        """Ensure logging is initialized."""
        self.assertIsNotNone(self.agent.logger)

    def test_write_to_csv(self):
        """Test writing data to a CSV file."""
        test_data = [{'name': 'Product1', 'price': '$20'}, {'name': 'Product2', 'price': '$30'}]
        self.agent.write_to_csv("test.csv", test_data)
        self.assertTrue(os.path.exists("test_project/test.csv"))

    def tearDown(self):
        """Clean up test files."""
        if os.path.exists("test_project/test.csv"):
            os.remove("test_project/test.csv")


if __name__ == "__main__":
    unittest.main()
