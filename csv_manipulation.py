import pandas as pd

def load_csv():
    df_input = pd.DataFrame()
    df_input = pd.read_csv(input, sep=None, engine='python', encoding='utf-8',
                           parse_dates=True,
                           infer_datetime_format=True)
    return df_input

