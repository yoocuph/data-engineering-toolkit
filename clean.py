import pandas as pd 

def clean_dataframe(df: pd.DataFrame) -> pd.DataFrame:
    df = df.dropna()             # remove nulls
    df = df.drop_duplicates()    # remove duplicates
    return df