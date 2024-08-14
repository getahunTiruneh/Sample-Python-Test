import numpy as np
import pandas as pd
import os
import matplotlib.pyplot as plt
import seaborn as sns

def load_data(path):
        df = pd.read_csv(path)
        print("Data loaded successfully!")
        return df

def check_missing_values(df):
    missing_data = df.isnull().sum()
    return missing_data
#function for bar chart visualization
def bar_chart(df, column):
    # Count the occurrences of each unique value in the column
    counts = column.value_counts()
    
    # Plot a bar chart
    counts.plot(kind='bar')
    plt.title(f"Bar Chart of {column.name}")
    plt.xlabel(column.name)
    plt.ylabel('Count')
    plt.show()
def heatmap_chart(df):
    corr_matrix = df.select_dtypes(exclude="object").corr()
    plt.figure(figsize=(10, 8))
    sns.heatmap(corr_matrix, annot=True, cmap='coolwarm')
    plt.title('Correlation Heatmap')
    plt.show()
def scatter_plot(df,X_column, y_column):
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