import unittest
import pandas as pd


class TestDataVersioning(unittest.TestCase):
    def setUp(self):
        # Dummy data for different versions of a dataset
        self.data_v1 = pd.DataFrame({
            'feature1': [1, 2, 3, 4, 5],
            'feature2': [10, 20, 30, 40, 50],
        })

        self.data_v2 = pd.DataFrame({
            'feature1': [1, 2, 3, 4, 5],
            'feature2': [10, 20, 30, 40, 50],
            'feature3': [6, 7, 8, 9, 10]
        })

    def test_data_processing_v1(self):
        # Function to process data for version 1
        def process_data_v1(data):
            result = data['feature1'] * data['feature2']
            return result

        # Test the data processing function with version 1 data
        processed_data_v1 = process_data_v1(self.data_v1)
        expected_result_v1 = self.data_v1['feature1'] * self.data_v1['feature2']
        self.assertTrue(processed_data_v1.equals(expected_result_v1))

    def test_data_processing_v2(self):
        # Function to process data for version 2 (includes feature3)
        def process_data_v2(data):
            result = data['feature1'] * data['feature2'] + data['feature3']
            return result

        # Test the data processing function with version 2 data
        processed_data_v2 = process_data_v2(self.data_v2)
        expected_result_v2 = self.data_v2['feature1'] * self.data_v2['feature2'] + self.data_v2['feature3']
        self.assertTrue(processed_data_v2.equals(expected_result_v2))


if __name__ == '__main__':
    unittest.main()
