import pandas as pd


def load_data():
    df = pd.read_csv("E:/2026-2027/ML/Placement_Prediction/Data/placement_predict_50k Dataset (2).csv")
    return df


def summarize(df):
    return {
        "shape": df.shape,
        "columns": df.columns,
    }
