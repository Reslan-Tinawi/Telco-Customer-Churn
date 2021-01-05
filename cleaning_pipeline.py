from typing import Any, Dict, List
import numpy as np

import pandas as pd


def start_pipeline(df: pd.DataFrame) -> pd.DataFrame:
    return df.copy()


def drop_noisy_columns(df: pd.DataFrame, cols: List[str]) -> pd.DataFrame:
    return df.drop(columns=cols)


def replace_empty_strings_with_nan(df: pd.DataFrame) -> pd.DataFrame:
    empty_string_pattern: str = r"^\s*$"
    return df.replace(to_replace=empty_string_pattern, value=np.nan, regex=True)


def drop_missing_values(df: pd.DataFrame) -> pd.DataFrame:
    return df.dropna()


def map_column_values(
    df: pd.DataFrame, col: str, mapping_dict: Dict[Any, Any]
) -> pd.DataFrame:
    df[col] = df[col].map(mapping_dict)
    return df


def convert_column_dtypes(
    df: pd.DataFrame, dtypes_mapping: Dict[str, str]
) -> pd.DataFrame:
    return df.astype(dtypes_mapping)
