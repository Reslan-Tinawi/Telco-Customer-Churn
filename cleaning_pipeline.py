def start_pipeline(dataframe):
    return dataframe.copy()


def drop_noisy_columns(datafram, cols):
    return datafram.drop(columns=cols)


def convert_column_dtypes(datafram, dtypes_mapping):
    return datafram.astype(dtypes_mapping)