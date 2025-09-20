import pandas as pd

def save_to_csv(df: pd.DataFrame, path: str) -> None:
    df.to_csv(path, index=False)