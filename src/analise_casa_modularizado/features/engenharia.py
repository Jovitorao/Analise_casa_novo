import pandas as pd


def criar_features(df):
    df = df.copy()
    df['habitavel_por_terreno'] = df['m2_area_habitavel'] / df['m2_terreno']
    df['idade_imovel'] = df['ano'] - df['ano_construcao']
    df['idade_efetiva'] = df['ano'] - df[['ano_construcao', 'ano_renovacao']].max(axis=1)
    df['total_comodos'] = df['quartos'] + df['banheiros']
    df['foi_renovado'] = (df['ano_renovacao'] > 0).astype(int)

    df['idade_imovel'] = df['idade_imovel'].clip(lower=0)
    df['idade_efetiva'] = df['idade_efetiva'].clip(lower=0)
    return df