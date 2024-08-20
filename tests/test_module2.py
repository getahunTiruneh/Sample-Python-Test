import unittest
from unittest.mock import patch
import pandas as pd
import numpy as np
import sys
sys.path.insert(0, '/CBE_Doc/AI Training/Sample-Python-Test/scripts')  

from scripts.module2 import data_analysis

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
        self.da = data_analysis(pd.DataFrame()) 
    def test_check_missing_values_with_missing(self):
        # Arrange
        expected_output = pd.Series([1, 1, 1], index=['A', 'B', 'C'])

        # Act
        result = self.da.check_missing_values(self.df_with_missing)

        # Assert
        pd.testing.assert_series_equal(result, expected_output)

    def test_check_missing_values_without_missing(self):
        # Arrange
        expected_output = pd.Series([0, 0, 0], index=['A', 'B', 'C'])

        # Act
        result = self.da.check_missing_values(self.df_without_missing)

        # Assert
        pd.testing.assert_series_equal(result, expected_output)
    @patch('scripts.module2.sns.heatmap')
    @patch('scripts.module2.plt.figure')
    @patch('scripts.module2.plt.title')
    @patch('scripts.module2.plt.show')
    def test_heatmap_chart(self, mock_show, mock_title, mock_figure, mock_heatmap):
        # Create a sample DataFrame
        data = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
        df = pd.DataFrame(data, columns=['A', 'B', 'C'])      
        
        # Call the function
        self.da.heatmap_chart(df)

        # Check if the functions were called with the correct arguments
        mock_figure.assert_called_once_with(figsize=(10, 8))
        
        # Extract the DataFrame that was passed to heatmap
        args, kwargs = mock_heatmap.call_args
        
        # Compare the DataFrame values
        pd.testing.assert_frame_equal(args[0], df.select_dtypes(exclude="object").corr())
        self.assertEqual(kwargs['annot'], True)
        self.assertEqual(kwargs['cmap'], 'coolwarm')
        
        mock_title.assert_called_once_with('Correlation Heatmap')
        mock_show.assert_called_once()


if __name__ == '__main__':
    unittest.main()

if __name__ == '__main__':
    unittest.main()
  