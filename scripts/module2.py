import numpy as np
import pandas as pd
import os

def load_data(path):
        df = pd.read_csv(path)
        print("Data loaded successfully!")
        return df

def check_missing_values(df):
    missing_data = df.isnull().sum()
    return missing_data

# Main function for testing (optional)
if __name__ == "__main__":
    # Load the data into the DataFrame
    # df = load_data('../data/heart.csv')
    print(os.getcwd())