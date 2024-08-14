import unittest
from scripts.module2 import load_data, check_missing_values
import pandas as pd

class Testmodule2(unittest.TestCase):
    def setUp(self):
        self.df_with_missing = pd.DataFrame({
            'A': [1, 2, None, 4],
            'B': [5, None, 7, 8],
            'C': [9, 10, 11, None]
        })
        self.df_without_missing = pd.DataFrame({
            'A': [1, 2, 3, 4],
            'B': [5, 6, 7, 8],
            'C': [9, 10, 11, 12]
        })

    def test_check_missing_values_with_missing(self):
        # Arrange
        expected_output = pd.Series([1, 1, 1], index=['A', 'B', 'C'])

        # Act
        result = check_missing_values(self.df_with_missing)

        # Assert
        pd.testing.assert_series_equal(result, expected_output)

    def test_check_missing_values_without_missing(self):
        # Arrange
        expected_output = pd.Series([0, 0, 0], index=['A', 'B', 'C'])

        # Act
        result = check_missing_values(self.df_without_missing)

        # Assert
        pd.testing.assert_series_equal(result, expected_output)

if __name__ == '__main__':
    unittest.main()
  