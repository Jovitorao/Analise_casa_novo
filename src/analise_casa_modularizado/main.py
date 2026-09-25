from data.carregamento import carregar_dados
from data.limpeza import converter_tipos, traduzir
from features.engenharia import criar_features   # ajuste ao nome real
from visualizacao.analises import media_anual, media_por_bairro, grafico_top_5_bairros

df = carregar_dados('Housing.csv')      # ajuste o caminho do CSV
df = converter_tipos(df)
df = traduzir(df)
df = criar_features(df)

print(media_anual(df))
fig = grafico_top_5_bairros(media_por_bairro(df))
fig.show()