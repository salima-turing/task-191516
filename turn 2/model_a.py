import unittest
from parameterized import parameterized
import pandas as pd

class TestDataProcessing(unittest.TestCase):

	@parameterized.expand([
		("data_v1", pd.DataFrame({'feature1': [1, 2], 'feature2': [10, 20]}), [10, 40]),
		("data_v2", pd.DataFrame({'feature1': [1, 2], 'feature2': [10, 20], 'feature3': [3, 4]}), [13, 20]),
	])
	def test_data_processing(self, name, data, expected_result):
		def process_data(data):
			result = data['feature1'] * data['feature2']
			if 'feature3' in data:
				result += data['feature3']
			return result

		processed_data = process_data(data)
		self.assertTrue(processed_data.equals(pd.Series(expected_result)))

if __name__ == '__main__':
	unittest.main()
