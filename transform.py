import pandas as pd

def add_total_column(df: pd.DataFrame) -> pd.DataFrame:
    df["total"] = df.sum(axis=1, numeric_only=True)
    return df
