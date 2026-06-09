import pandas as pd
import numpy as np

def clean_and_explore_data():
    print("Pandas Preprocessing & EDA")
    
    try:
        df = pd.read_csv("raw_snus_sales.csv")
        print(f"Successfully loaded data. Initial Shape: {df.shape[0]} rows, {df.shape[1]} columns")
    except FileNotFoundError:
        print("Error: 'raw_snus_sales.csv' not found. Please run data_acquisition.py first.")
        return

    # Exploratory Data Analysis (Initial Check)
    print("\n[EDA] Missing values per column before cleaning:")
    print(df.isnull().sum())
    
    # Handle Duplicates
    duplicate_count = df.duplicated(subset=['Order_ID']).sum()
    print(f"\n[Cleaning] Found {duplicate_count} duplicate orders based on Order_ID. Dropping them...")
    df.drop_duplicates(subset=['Order_ID'], keep='first', inplace=True)
    
    # Fix Data Type 
    print("[Cleaning] Standardizing 'Price_Per_Can' data type...")
    df['Price_Per_Can'] = df['Price_Per_Can'].astype(str).str.replace(' SEK', '', case=False).str.strip()
    df['Price_Per_Can'] = pd.to_numeric(df['Price_Per_Can'], errors='coerce')
    
    # Handle Missing Values
    print("[Cleaning] Handling missing values...")
    median_age = df['Customer_Age'].median()
    df['Customer_Age'] = df['Customer_Age'].fillna(median_age)
    df['Customer_Age'] = df['Customer_Age'].astype(int) 
    df['Region'] = df['Region'].fillna('Unknown')
    
    # Post-Cleaning Verification & EDA Summary
    print("\n[EDA] Final Cleaned Dataset Summary:")
    print(f"Final Shape: {df.shape[0]} rows, {df.shape[1]} columns")
    print(f"Missing values remaining: {df.isnull().sum().sum()}")
    print("\n[EDA] Basic Descriptive Statistics for Numeric Data:")
    print(df[['Strength_mg', 'Quantity', 'Price_Per_Can', 'Customer_Age']].describe())
    
    # Export Cleaned Dataset for PySpark
    cleaned_filename = "cleaned_snus_sales.csv"
    df.to_csv(cleaned_filename, index=False)
    print(f"\nSuccessfully saved cleaned structured pipeline data to '{cleaned_filename}'")

if __name__ == "__main__":
    clean_and_explore_data()