# %%
import pandas as pd

# %%
df = pd.read_excel("/home/leonardo/ufpr-2025/periodo_6/marketing_analytics/atividade_3/data/Pesquisa-chocolate.xlsx")
df.info()

# %%
df.describe()

# %%
condicao_agrupado = df.groupby(by='Condição')[['Avaliacao_geral_Mais','Avaliacao_geral_Bis']].sum()
condicao_agrupado
# %%
genero_agrupado = df.groupby(by='Gênero')[['Avaliacao_geral_Mais','Avaliacao_geral_Bis']].sum()
genero_agrupado

# %%
print(df['Compraria_Bis'].value_counts())
print(df['Compraria_Mais'].value_counts())
