import pandas as pd


def converter_tipos(df):
    df_convertido = df.copy()
    df_convertido['date'] = pd.to_datetime(df_convertido['date'])
    df_convertido['zipcode'] = df_convertido['zipcode'].astype(str)

    converter = ['sqft_living', 'sqft_lot', 'sqft_above',
                 'sqft_basement', 'sqft_living15', 'sqft_lot15']
    for i in converter:
        df_convertido[i] = df_convertido[i] * 0.092903
    return df_convertido


def traduzir(df):
    df_traduzido = df.copy()
    traducao_colunas = {
        'id': 'id_imovel',
        'date': 'data',
        'price': 'preco',
        'bedrooms': 'quartos',
        'bathrooms': 'banheiros',
        'sqft_living': 'm2_area_habitavel',
        'sqft_lot': 'm2_terreno',
        'floors': 'andares',
        'waterfront': 'vista_mar_rio',
        'view': 'nota_vista',
        'condition': 'condicao_imovel',
        'grade': 'nota_design',
        'sqft_above': 'm2_acima_solo',
        'sqft_basement': 'm2_porao',
        'yr_built': 'ano_construcao',
        'yr_renovated': 'ano_renovacao',
        'zipcode': 'codigo_postal',
        'lat': 'latitude',
        'long': 'longitude',
        'sqft_living15': 'm2_area_vizinhos_15',
        'sqft_lot15': 'm2_terreno_vizinhos_15'
    }
    df_traduzido = df_traduzido.rename(columns=traducao_colunas)
    return df_traduzido