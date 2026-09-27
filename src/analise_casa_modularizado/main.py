from data.carregamento import carregar_dados
from data.limpeza import converter_tipos, traduzir
from visualizacao.analises import colunas_ano_mes, media_anual, media_por_bairro, grafico_top_5_bairros
from features.engenharia import criar_features

df = carregar_dados('Housing.csv')
df = converter_tipos(df)
df = traduzir(df)
df = colunas_ano_mes(df)      # cria 'ano' e 'mes' — necessário para as features
df = criar_features(df)

print(media_anual(df))
fig = grafico_top_5_bairros(media_por_bairro(df))
fig.show()