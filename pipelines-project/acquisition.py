import pandas as pd


def load_data(data):
    df = pd.read_csv(data, encoding="ISO-8859-1")
    return df
