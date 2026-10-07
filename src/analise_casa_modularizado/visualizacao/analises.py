import pandas as pd
import plotly.express as px


def colunas_ano_mes(df):
    df_temporal = df.copy()
    df_temporal['ano'] = df_temporal['data'].dt.year
    df_temporal['mes'] = df_temporal['data'].dt.month
    return df_temporal


def media_anual(df):
    df = df.copy()
    df_media_anual = df.groupby('ano')['preco'].mean().reset_index().round(2)
    return df_media_anual


def media_mensal(df):
    df = df.copy()
    df_media_mensal = df.groupby(['ano', 'mes'])['preco'].mean().reset_index().round(2)
    return df_media_mensal


def preco_cep(df):
    df = df.copy()
    df_preco_cep = df.groupby('codigo_postal')['preco'].mean().reset_index().round(2)
    return df_preco_cep


def preco_cep_especifico(df, cep):
    df = df.copy()
    df_bairro = df[df['codigo_postal'] == cep]
    media = df_bairro['preco'].mean()
    maximo = df_bairro['preco'].max()
    minimo = df_bairro['preco'].min()
    return media, maximo, minimo


def media_por_bairro(df):
    df = df.copy()
    media_preco_bairro = (
        df.groupby('codigo_postal')['preco'].mean()
        .sort_values(ascending=False)
        .reset_index()
        .rename(columns={'preco': 'Media_preco', 'codigo_postal': 'Bairro'})
        .round(2)
    )
    return media_preco_bairro


def grafico_top_5_bairros(media_preco_bairro):
    top5 = media_preco_bairro.copy().head(5)
    fig_top5 = px.bar(
        top5,
        x='Media_preco',
        y='Bairro',
        orientation='h',
        text_auto='.3s',
        color='Media_preco',
        title='Top 5 bairros com maiores preços médios'
    )
    fig_top5.update_yaxes(type='category')
    return fig_top5


def outlier(df):
    df_outlier = df.copy()
    fig_outlier = px.box(df_outlier, y='preco',
                         title='Distribuição de Preços com Outliers',
                         points='outliers')
    return fig_outlier


def histograma(df):
    df_hist = df.copy()
    fig_hist = px.histogram(df_hist, x='preco', nbins=100,
                            title='Distribuição de Preços')
    return fig_hist


def area_e_preco(df):
    df_area_preco = df.copy()
    fig_area_preco = px.scatter(df_area_preco, x='m2_area_habitavel', y='preco',
                                title='Relação preço por área')
    return fig_area_preco


def evolucao_temporal(df_media_mensal):
    """Recebe o resultado de media_mensal(df), não o df cru."""
    df_temporal = df_media_mensal.copy()
    df_temporal['data_formatada'] = (df_temporal['ano'].astype(str) + '-'
                                     + df_temporal['mes'].astype(str))
    fig_preco = px.line(
        df_temporal,
        x='data_formatada',
        y='preco',
        title='Evolução do Preço ao Longo do Tempo',
        labels={'data_formatada': 'Período (Ano-Mês)', 'preco': 'Preço ($)'}
    )
    fig_preco.update_xaxes(type='category')
    return fig_preco