import pandas as pd
import plotly.express as px


def dropar_colunas(df):
    df_dropar_colunas = df.copy()
    cols_tirar = ['id_imovel','data','codigo_postal']
    df_dropar_colunas = df_dropar_colunas.drop(columns=(cols_tirar))

    return df_dropar_colunas

def pearson(df):
    df = df.copy()
    corr_pearson = df.corr('pearson')['preco'].drop('preco')
    return corr_pearson

def spearman(df):
    df = df.copy()
    corr_spearman = df.corr('spearman')['preco'].drop('preco')
    return corr_spearman

def comparacao(entrada_pearson,entrada_spearman):
    corr_preco_pearson = entrada_pearson.copy()
    corr_preco_spearman = entrada_spearman.copy()
    comparacao = pd.DataFrame({
    'pearson': corr_preco_pearson,
    'spearman': corr_preco_spearman
        })
    comparacao['diferenca'] = (comparacao['spearman'] - comparacao['pearson']).round(3)
    comparacao['pearson'] = comparacao['pearson'].round(3)
    comparacao['spearman'] = comparacao['spearman'].round(3)

    comparacao = comparacao.reindex(
        comparacao['spearman'].abs().sort_values(ascending=False).index
    )
    return comparacao

def mapa_de_calor(df):
    df = df.copy()
    df_correlacao_pearson = df.corr('pearson')

    fig_heatmap = px.imshow(
    df_correlacao_pearson,
    text_auto='.2f',            # escreve o valor em cada célula
    aspect='auto',
    color_continuous_scale='RdBu_r',   # vermelho = +, azul = -
    zmin=-1, zmax=1,            # fixa a escala de cor de -1 a 1
    title='Mapa de calor — correlação de Pearson entre variáveis'
                        )
    fig_heatmap.update_layout(height=800, width=900)
    return fig_heatmap

def analise_completa(df):
    df_num = dropar_colunas(df)
    corr_p = pearson(df)
    corr_s= spearman(df)
    tabela = comparacao(corr_p,corr_s)
    mapa = mapa_de_calor(df_num)
    return tabela , mapa