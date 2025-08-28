# %%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# %%
# Leitura do Arquivo:
df = pd.read_excel("/home/leonardo/ufpr-2025/periodo_6/marketing_analytics/atividade_3/data/Pesquisa-chocolate.xlsx")
df.info()

# %%
# Filtro entre pessoas que viram a marca e os que não viram (1 e 0, respectivamente):

filtro_c_marca = df['Condição'] == 1
filtro_s_marca = df['Condição'] == 0  
#%%
# Testando a divisão dos datasets
print(df[filtro_c_marca].info())
print(df[filtro_s_marca].info())

# %%
# Iniciando as estatísticas descritivas:
print(df[filtro_s_marca].describe())
print(df[filtro_c_marca].describe())

# %%
# Agrupando o dataframe original por Condição para conseguir trazer um resumo geral
df_condicao_agg = df.groupby(by="Condição")[['Cor_Bis',
                           'Cor_Mais',	
                           'Aroma_Bis',	
                           'Aroma_Mais',
                            'Sabor_Bis',
                            'Sabor_Mais',	
                            'Crocância_Bis',	
                            'Crocância_Mais',
                            'Consitência_Bis',
                            'Consistência_Mais',
                            'Residual_Bis',	
                            'Residual_Mais',
                            'Avaliacao_geral_Bis',	
                            'Avaliacao_geral_Mais',
                            'Compraria_Bis',
                            'Compraria_Mais',	
                            'Gênero']].mean()
df_condicao_agg = pd.DataFrame(df_condicao_agg, index=[0, 1])
df_condicao_agg
# %%
# Validação cruzada com os dataframes individuais
print(df[filtro_c_marca].mean().sort_values(ascending=False))
print(df[filtro_s_marca].mean().sort_values(ascending=False))

# %%
# Plotando visualmente a diferença entre as médias em relação a :
# Sabor, Avaliação Geral, Intenção de Compra e Outros Atributos.
plt.figure(figsize=(10, 6))
df_condicao_agg[['Sabor_Bis', 'Sabor_Mais']].T.plot(kind='bar', figsize=(10, 6), color=['#A52A2A', '#8B4513'])
plt.title('Média de Sabor por Condição')
plt.xlabel('Marca')
plt.ylabel('Nota Média')
plt.xticks(ticks=[0, 1], labels=['Bis', 'Hershey\'s (Mais)'], rotation=0, fontsize='large')
plt.legend(title='Condição', labels=['Sem Marca', 'Com Marca'])
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()
# %%
plt.figure(figsize=(10, 6))
df_condicao_agg[['Avaliacao_geral_Bis', 'Avaliacao_geral_Bis']].T.plot(kind='bar', figsize=(10, 6), color=['#A52A2A', '#8B4513'])
plt.title('Média de Avaliação por Condição')
plt.xlabel('Marca')
plt.ylabel('Nota Média')
plt.xticks(ticks=[0, 1], labels=['Bis', 'Hershey\'s (Mais)'], rotation=0, fontsize='large')
plt.legend(title='Condição', labels=['Sem Marca', 'Com Marca'])
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()

# %%
plt.figure(figsize=(10, 6))
df_condicao_agg[['Compraria_Bis', 'Compraria_Mais']].T.plot(kind='bar', figsize=(10, 6), color=['#A52A2A', '#8B4513'])
plt.title('Média de Intenção de Compra por Condição')
plt.xlabel('Marca')
plt.ylabel('Nota Média')
plt.xticks(ticks=[0, 1], labels=['Bis', 'Hershey\'s (Mais)'], rotation=0, fontsize='large')
plt.legend(title='Condição', labels=['Sem Marca', 'Com Marca'])
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()

# %%
plt.figure(figsize=(10, 6))
df_condicao_agg[['Consitência_Bis', 'Consistência_Mais']].T.plot(kind='bar', figsize=(10, 6), color=['#A52A2A', '#8B4513'])
plt.title('Média de Consistência por Condição')
plt.xlabel('Marca')
plt.ylabel('Nota Média')
plt.xticks(ticks=[0, 1], labels=['Bis', 'Hershey\'s (Mais)'], rotation=0, fontsize='large')
plt.legend(title='Condição', labels=['Sem Marca', 'Com Marca'])
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()

# %%
# Agrupando o dataframe original por Condição para conseguir trazer um resumo geral
df_genero_agg = df[filtro_s_marca].groupby(by="Gênero")[['Cor_Bis',
                           'Cor_Mais',	
                           'Aroma_Bis',	
                           'Aroma_Mais',
                            'Sabor_Bis',
                            'Sabor_Mais',	
                            'Crocância_Bis',	
                            'Crocância_Mais',
                            'Consitência_Bis',
                            'Consistência_Mais',
                            'Residual_Bis',	
                            'Residual_Mais',
                            'Avaliacao_geral_Bis',	
                            'Avaliacao_geral_Mais',
                            'Compraria_Bis',
                            'Compraria_Mais',	
                            'Condição']].mean()
df_genero_agg = pd.DataFrame(df_genero_agg, index=[0, 1])
df_genero_agg

# %%
plt.figure(figsize=(10, 6))
df_genero_agg[['Sabor_Bis', 'Sabor_Mais']].T.plot(kind='bar', figsize=(10, 6), color=['#A52A2A', '#8B4513'])
plt.title('Média de Sabor por Genêro')
plt.xlabel('Marca')
plt.ylabel('Nota Média')
plt.xticks(ticks=[0, 1], labels=['Bis', 'Hershey\'s (Mais)'], rotation=0, fontsize='large')
plt.legend(title='Genêro', labels=['Masculino', 'Feminino'])
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()

# %%
plt.figure(figsize=(10, 6))
df_genero_agg[['Avaliacao_geral_Bis', 'Avaliacao_geral_Mais']].T.plot(kind='bar', figsize=(10, 6), color=['#A52A2A', '#8B4513'])
plt.title('Média de Avaliação por Genêro')
plt.xlabel('Marca')
plt.ylabel('Nota Média')
plt.xticks(ticks=[0, 1], labels=['Bis', 'Hershey\'s (Mais)'], rotation=0, fontsize='large')
plt.legend(title='Genêro', labels=['Masculino', 'Feminino'])
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()
# %%
plt.figure(figsize=(10, 6))
df_genero_agg[['Compraria_Bis', 'Compraria_Mais']].T.plot(kind='bar', figsize=(10, 6), color=['#A52A2A', '#8B4513'])
plt.title('Média de Inteção de Compra por Genêro')
plt.xlabel('Marca')
plt.ylabel('Nota Média')
plt.xticks(ticks=[0, 1], labels=['Bis', 'Hershey\'s (Mais)'], rotation=0, fontsize='large')
plt.legend(title='Genêro', labels=['Masculino', 'Feminino'])
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()
# %%
df_genero_agg_1 = df[filtro_c_marca].groupby(by="Gênero")[['Cor_Bis',
                           'Cor_Mais',	
                           'Aroma_Bis',	
                           'Aroma_Mais',
                            'Sabor_Bis',
                            'Sabor_Mais',	
                            'Crocância_Bis',	
                            'Crocância_Mais',
                            'Consitência_Bis',
                            'Consistência_Mais',
                            'Residual_Bis',	
                            'Residual_Mais',
                            'Avaliacao_geral_Bis',	
                            'Avaliacao_geral_Mais',
                            'Compraria_Bis',
                            'Compraria_Mais',	
                            'Condição']].mean()
df_genero_agg_1 = pd.DataFrame(df_genero_agg_1, index=[0, 1])
df_genero_agg_1

# %%
plt.figure(figsize=(10, 6))
df_genero_agg_1[['Sabor_Bis', 'Sabor_Mais']].T.plot(kind='bar', figsize=(10, 6), color=['#A52A2A', '#8B4513'])
plt.title('Média de Sabor por Genêro')
plt.xlabel('Marca')
plt.ylabel('Nota Média')
plt.xticks(ticks=[0, 1], labels=['Bis', 'Hershey\'s (Mais)'], rotation=0, fontsize='large')
plt.legend(title='Genêro', labels=['Masculino', 'Feminino'])
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()
# %%
plt.figure(figsize=(10, 6))
df_genero_agg_1[['Avaliacao_geral_Bis', 'Avaliacao_geral_Mais']].T.plot(kind='bar', figsize=(10, 6), color=['#A52A2A', '#8B4513'])
plt.title('Média de Avaliação por Genêro')
plt.xlabel('Marca')
plt.ylabel('Nota Média')
plt.xticks(ticks=[0, 1], labels=['Bis', 'Hershey\'s (Mais)'], rotation=0, fontsize='large')
plt.legend(title='Genêro', labels=['Masculino', 'Feminino'])
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()

# %%
plt.figure(figsize=(10, 6))
df_genero_agg_1[['Compraria_Bis', 'Compraria_Mais']].T.plot(kind='bar', figsize=(10, 6), color=['#A52A2A', '#8B4513'])
plt.title('Média de Inteção de Compra por Genêro')
plt.xlabel('Marca')
plt.ylabel('Nota Média')
plt.xticks(ticks=[0, 1], labels=['Bis', 'Hershey\'s (Mais)'], rotation=0, fontsize='large')
plt.legend(title='Genêro', labels=['Masculino', 'Feminino'])
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()