import unittest
from app.data_processor import process_data


class TestProcessor(unittest.TestCase):
    def test_process_data(self):
        data = {"age": [20, 25, 30, 16]}
        result = process_data(data)
        self.assertEqual(result.loc["mean", "age"], 22.75)

if __name__ == '__main__':
    unittest.main()
