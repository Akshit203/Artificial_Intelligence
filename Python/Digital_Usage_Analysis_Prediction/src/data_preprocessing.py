# src/data_preprocessing.py
import pandas as pd
import numpy as np
import re

def normalize_column(col_name):
    col = col_name.strip().lower()               # lowercase & strip spaces
    col = re.sub(r'[^0-9a-zA-Z]+', '_', col)    # replace non-alphanumeric chars with underscore
    col = re.sub(r'_+', '_', col)               # replace multiple underscores with single
    col = col.strip('_')                         # remove leading/trailing underscores
    return col

def load_data(file_path):
    df = pd.read_csv(file_path)
    df.columns = [normalize_column(col) for col in df.columns]
    
    
    
    return df

def clean_data(df):
    numeric_cols = df.select_dtypes(include=np.number).columns
    df[numeric_cols] = df[numeric_cols].fillna(df[numeric_cols].median())
    
    cat_cols = df.select_dtypes(include='object').columns
    for col in cat_cols:
        df[col] = df[col].fillna(df[col].mode()[0])
    
    # Ensure target column is string
    df['user_behavior_class'] = df['user_behavior_class'].astype(str)
    
    return df

def preprocess(file_path):
    df = load_data(file_path)
    df = clean_data(df)
    return df
