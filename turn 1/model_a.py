import unittest
import pandas as pd

class TestDataVersioning(unittest.TestCase):

	def setUp(self):
		# Dummy data for different versions
		self.data_v1 = pd.DataFrame({
			'feature1': [1, 2, 3],
			'feature2': [4.0, 5.0, 6.0]
		})

		self.data_v2 = pd.DataFrame({
			'feature1': [1, 2, 3, 4],
			'feature2': [4.0, 5.0, 6.0, 7.0],
			'feature3': ['a', 'b', 'c', 'd']
		})

		self.data_v3 = self.data_v2.copy()
		self.data_v3.loc[2, 'feature2'] = 10.0

	def test_load_data_v1(self):
		loaded_data = load_data('v1')
		pd.testing.assert_frame_equal(loaded_data, self.data_v1, check_dtype=False)

	def test_load_data_v2(self):
		loaded_data = load_data('v2')
		pd.testing.assert_frame_equal(loaded_data, self.data_v2, check_dtype=False)

	def test_load_data_v3(self):
		loaded_data = load_data('v3')
		pd.testing.assert_frame_equal(loaded_data, self.data_v3, check_dtype=False)

	def test_data_version_not_found(self):
		with self.assertRaises(KeyError):
			load_data('v4')

if __name__ == '__main__':
	unittest.main()

# Function to load data based on version
def load_data(version):
	data_versions = {
		'v1': TestDataVersioning().data_v1,
		'v2': TestDataVersioning().data_v2,
		'v3': TestDataVersioning().data_v3
	}

	if version not in data_versions:
		raise KeyError(f"Data version '{version}' not found.")

	return data_versions[version]
