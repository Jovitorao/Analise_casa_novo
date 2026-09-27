import pandas as pd


def carregar_dados(caminho):
    df = pd.read_csv(caminho)
    return df


def salvar_dados(df, caminho):
    df.to_csv(caminho, index=False)