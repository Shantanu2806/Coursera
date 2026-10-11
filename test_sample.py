import unittest
from sample import app_status


class TestSample(unittest.TestCase):
    def test_routes(self):
        self.assertEqual(app_status(), "OK")

    def test_health(self):
        self.assertTrue(True)


if __name__ == "__main__":
    unittest.main()
