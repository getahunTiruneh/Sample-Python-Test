import numpy as np
import pandas as pd
import os
import matplotlib.pyplot as plt
import seaborn as sns

class data_analysis:
    def __init__(self, df):
        self.df = df
    def load_data(self,file_path):
        """Loads data from a CSV file into a DataFrame.

        Args:
            file_path (str): The path to the CSV file to load.

        Returns:
            DataFrame: The loaded DataFrame containing the data.
        """
        self.df = pd.read_csv(file_path)
        print("Data loaded successfully!")
        return self.df

    def check_missing_values(self,df):
        self.missing_data = df.isnull().sum()
        return self.missing_data
    #function for bar chart visualization
    def bar_chart(self,df, column):
        # Count the occurrences of each unique value in the column
        counts = column.value_counts()
        
        # Plot a bar chart
        counts.plot(kind='bar')
        plt.title(f"Bar Chart of {column.name}")
        plt.xlabel(column.name)
        plt.ylabel('Count')
        plt.show()
    def heatmap_chart(self,df):
        corr_matrix = df.select_dtypes(exclude="object").corr()
        plt.figure(figsize=(10, 8))
        sns.heatmap(corr_matrix, annot=True, cmap='coolwarm')
        plt.title('Correlation Heatmap')
        plt.show()
    def scatter_plot(self,df,X_column, y_column):
        plt.scatter(df[X_column], df[y_column])
        plt.xlabel(X_column)
        plt.ylabel(y_column)
        plt.title(f"Scatter Plot of {X_column} vs {y_column}")
        plt.show()
# Main function for testing (optional)
if __name__ == "__main__":
    # Load the data into the DataFrame
    # df = load_data('../data/heart.csv')
    print(os.getcwd())