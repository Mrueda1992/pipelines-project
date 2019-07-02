import pandas as pd

def drop_nulls(df, cols):
    df = df[df[cols].notnull()]
    return df

def rename (df, col, new_col):
    df.rename (columns= {col: new_col}, inplace=True)
    return df