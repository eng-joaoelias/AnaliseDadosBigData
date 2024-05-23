# -*- coding: utf-8 -*-
"""TRABALHO_A3.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1L3WMRJseAc52mkCwtjGaGEWM_sc5Bcpd
"""

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

'''
from google.colab import drive
drive.mount('/content/drive')
'''

"""# Sobre Obesidade

## Abrindo o DataSet Obesidade
"""

df_obesidade = pd.read_csv('https://raw.githubusercontent.com/eng-joaoelias/AnaliseDadosBigData/main/DataSetADBD/obesidade-limpo.csv', sep = ',', index_col='Unnamed: 0')

"""## Filtre as informações corretas para apresentar os resultados de obesidade."""

df_obesidade

"""## Os dados entre homens mulheres são parecidos? Informe com números."""

# Extrair os três primeiros caracteres da coluna 'Obesity (%)' e converter para float
df_obesidade['Obesity no interval'] = pd.to_numeric(df_obesidade['Obesity (%)'].str.extract(r'(\d+\.\d+|\d+)')[0], errors='coerce')
'''
Regex para extração: A expressão regular r'(\d+\.\d+|\d+)' captura qualquer sequência de dígitos que pode ter ou não um ponto decimal. Ela funciona assim:

\d+: captura um ou mais dígitos.
\.: captura um ponto literal.
(\d+\.\d+|\d+): captura uma sequência de dígitos que pode ou não ter um ponto decimal.
'''
df_obesidade

df_obesidade[pd.isna(df_obesidade['Obesity no interval'])]

# Remover registros com NaN em 'Obesity no interval'
df_obesidade = df_obesidade.dropna(subset=['Obesity no interval'])

# Filtrar o DataFrame para incluir apenas as linhas onde a coluna "Sex" é igual a "Male"
male_df = df_obesidade[df_obesidade['Sex'] == 'Male']

# Calcular a média da coluna "Obesity no interval" para os valores filtrados
media_porc_obesidade_homem = male_df['Obesity no interval'].mean()
print("Media de obesidade de homens: {}".format(media_porc_obesidade_homem))

# Filtrar o DataFrame para incluir apenas as linhas onde a coluna "Sex" é igual a "Male"
female_df = df_obesidade[df_obesidade['Sex'] == 'Female']

# Calcular a média da coluna "Obesity no interval" para os valores filtrados
media_porc_obesidade_mulher = female_df['Obesity no interval'].mean()
print("Media de obesidade de mulheres: {}".format(media_porc_obesidade_mulher))

df_obesidade[df_obesidade['Sex'] == 'Male'].describe()['Obesity no interval']

df_obesidade[df_obesidade['Sex'] == 'Female'].describe()['Obesity no interval']

# Vamos criar DataFrames para os dados de homens e mulheres
male_df = pd.DataFrame({
    'Sex': 'Male',
    'Obesity': male_df['Obesity no interval']
})
female_df = pd.DataFrame({
    'Sex': 'Female',
    'Obesity': female_df['Obesity no interval']
})

# Concatenar os DataFrames de homens e mulheres
combined_df = pd.concat([male_df, female_df])

# Plotar o boxplot usando Seaborn
plt.figure(figsize=(10, 6))
sns.boxplot(x='Sex', y='Obesity', data=combined_df)
plt.title('Distribuição de Obesidade entre Homens e Mulheres')
plt.xlabel('Sexo')
plt.ylabel('Obesidade (%)')
plt.show()

"""R: Percebe-se que os dados entre homens e mulhereres são diferentes. Há um maior percentual geral de mulheres obesas do que homens.

## Qual o percentual médio de obesidade por sexo na américa do norte no ano de 2010?
"""

df_obesidade['Country'].unique() #lista de países

exp_logica_america_norte = (df_obesidade['Country'] == 'United States of America') | \
                            (df_obesidade['Country'] == 'Canada') | \
                            (df_obesidade['Country'] == 'Mexico')
df_america_norte = df_obesidade[exp_logica_america_norte]
df_america_norte

df_america_norte_2010 = df_america_norte[df_america_norte['Year'] == 2010]
df_america_norte_2010

df_america_norte_2010_homens = df_america_norte_2010[df_america_norte_2010['Sex'] == 'Male']
df_america_norte_2010_homens

df_america_norte_2010_mulheres = df_america_norte_2010[df_america_norte_2010['Sex'] == 'Female']
df_america_norte_2010_mulheres

print('O percentual médio de homens obesos na América do Norte, em 2010, é {:.2f}%\n'.format(df_america_norte_2010_homens['Obesity no interval'].mean()))
print('O percentual médio de mulheres obesas na América do Norte, em 2010, é {:.2f}%'.format(df_america_norte_2010_mulheres['Obesity no interval'].mean()))

if abs(df_america_norte_2010_homens['Obesity no interval'].mean() - df_america_norte_2010_mulheres['Obesity no interval'].mean()) < 5:
  print('\nOs percentuais são próximos')
else:
  print('\nOs percentuais são distantes')

"""## Qual os top 3 com maior e menor taxa de aumento de índices de obesidade nesse período de 2010? E em 2016?

Passos executados

1. **Filtrar os dados para incluir apenas os anos 2010 e 2016 e para o sexo "Both sexes".**
2. **Pivotar os dados para ter as taxas de obesidade de 2010 e 2016 lado a lado.**
3. **Calcular a diferença na taxa de obesidade entre 2010 e 2016 para cada país.**
4. **Identificar os top 3 países com maiores e menores aumentos na taxa de obesidade.**
"""

#Vizualização das colunas
df_obesidade.columns

# Filtrar os dados para os anos de interesse e para "Both sexes"
df_filtered = df_obesidade[(df_obesidade['Year'].isin([2010, 2016])) & (df_obesidade['Sex'] == 'Both sexes')]

# Pivotar os dados para ter as taxas de obesidade de 2010 e 2016 lado a lado
df_pivot = df_filtered.pivot_table(index=['Country', 'Sex'], columns='Year', values='Obesity no interval').reset_index()
df_pivot = df_pivot.drop('Sex', axis = 1)
df_pivot

# Remover possíveis linhas com dados faltantes para os anos 2010 ou 2016
df_pivot.dropna(subset=[2010, 2016], inplace=True)

# Calcular a diferença na taxa de obesidade
df_pivot['Diff'] = df_pivot[2016] - df_pivot[2010]

df_pivot

# Identificar os top 3 países com maior aumento na taxa de obesidade
top_3_increase = df_pivot.nlargest(3, 'Diff')

# Identificar os top 3 países com maior redução na taxa de obesidade
top_3_decrease = df_pivot.nsmallest(3, 'Diff')

# Exibir os resultados
print("Top 3 países com maior aumento na taxa de obesidade entre 2010 e 2016:")
print(top_3_increase)

print("\nTop 3 países com maior redução na taxa de obesidade entre 2010 e 2016:")
print(top_3_decrease)

"""## E os top 3 com maior e menor taxa de aumento de índices de obesidade no período completo, até o último registro ?

Passos executados:

1. **Filtrar os dados para incluir apenas registros onde `Sex` é "Both Sexes"**.
2. **Calcular a diferença na obesidade (%) entre o primeiro e o último ano disponível para cada país**.
3. **Classificar os países com base nessa diferença**.
4. **Selecionar os top 3 países com o maior e menor aumento na obesidade (%)**.
"""

# Filtrar os dados para incluir apenas registros onde 'Sex' é "Both Sexes"
df_obesidade_both_sexes = df_obesidade[df_obesidade['Sex'] == 'Both sexes'].copy()

# Verificar se há dados após filtragem e limpeza
print(f"Total de registros após filtragem: {len(df_obesidade_both_sexes)}")

# Remover registros com NaN em 'Obesity no interval'
df_obesidade_both_sexes = df_obesidade_both_sexes.dropna(subset=['Obesity no interval'])

# Obter o primeiro e o último ano para cada país
first_last_years = df_obesidade_both_sexes.groupby('Country')['Year'].agg(['min', 'max']).reset_index()

# Mesclar com o dataframe original para obter as taxas de obesidade nos primeiros e últimos anos
first_year_data = pd.merge(df_obesidade_both_sexes, first_last_years[['Country', 'min']], left_on=['Country', 'Year'], right_on=['Country', 'min'])
last_year_data = pd.merge(df_obesidade_both_sexes, first_last_years[['Country', 'max']], left_on=['Country', 'Year'], right_on=['Country', 'max'])

# Renomear colunas para facilitar a manipulação
first_year_data = first_year_data.rename(columns={'Obesity no interval': 'Obesity First Year', 'min': 'First Year'})
last_year_data = last_year_data.rename(columns={'Obesity no interval': 'Obesity Last Year', 'max': 'Last Year'})

# Mesclar os dados de primeiro e último ano
combined_data = pd.merge(first_year_data[['Country', 'First Year', 'Obesity First Year']],
                         last_year_data[['Country', 'Last Year', 'Obesity Last Year']],
                         on='Country')

# Calcular a diferença na obesidade
combined_data['Obesity Increase'] = combined_data['Obesity Last Year'] - combined_data['Obesity First Year']

# Verificar os dados combinados
print(combined_data.head())

# Classificar os países com base no aumento da obesidade
combined_data = combined_data.sort_values(by='Obesity Increase', ascending=False)

# Top 3 países com maior aumento
top_3_increase = combined_data.head(3)

# Top 3 países com menor aumento (ou maior diminuição)
top_3_decrease = combined_data.tail(3)

print("Top 3 países com maior aumento de obesidade:")
print(top_3_increase[['Country', 'First Year', 'Last Year', 'Obesity First Year', 'Obesity Last Year', 'Obesity Increase']])

print("\nTop 3 países com menor aumento (ou maior diminuição) de obesidade:")
print(top_3_decrease[['Country', 'First Year', 'Last Year', 'Obesity First Year', 'Obesity Last Year', 'Obesity Increase']])

"""O aumento significativo da obesidade nesses países pode ser atribuído à transição nutricional, onde houve uma mudança para uma dieta mais ocidentalizada, rica em alimentos processados, açúcares adicionados e gorduras saturadas.

## Extraia o máximo de informação possível sobre o Brasil. (O que julga ser importante sobre esse dataset? Use gráficos e apresente.)
"""

df_brasil = df_obesidade[df_obesidade['Country'] == 'Brazil']
print('Dados sobre o Brasil:\n\n{}'.format(df_brasil))

df_brasil_male = df_obesidade[(df_obesidade['Country'] == 'Brazil') & (df_obesidade['Sex'] == 'Male')] #Dados dos homens
df_brasil_female = df_obesidade[(df_obesidade['Country'] == 'Brazil') & (df_obesidade['Sex'] == 'Female')] #Dados das mulheres

## Plotando um gráfico sobre o crescimento da obesidade masculina no Brasil

# Ordenar os dados pelo ano
df_brasil_male = df_brasil_male.sort_values('Year')

# Plotar o gráfico
plt.figure(figsize=(10, 6))
plt.plot(df_brasil_male['Year'], df_brasil_male['Obesity no interval'], marker='o', color='b')
plt.title('Crescimento da obesidade masculina no Brasil')
plt.xlabel('Ano')
plt.ylabel('Taxa de obesidade (%)')
plt.grid(True)
plt.show()

## Plotando um gráfico sobre o crescimento da obesidade masculina no Brasil

# Ordenar os dados pelo ano
df_brasil_female = df_brasil_female.sort_values('Year')

# Plotar o gráfico
plt.figure(figsize=(10, 6))
plt.plot(df_brasil_female['Year'], df_brasil_female['Obesity no interval'], marker='o', color='b')
plt.title('Crescimento da obesidade feminina no Brasil')
plt.xlabel('Ano')
plt.ylabel('Taxa de obesidade (%)')
plt.grid(True)
plt.show()

print('Alguns cálculos estatísticos sobre obesidade no Brasil:\n\n{}'.format(df_brasil['Obesity no interval'].describe()))

"""### Comparar a obesidade no Brasil com o restante do mundo

Este código plota um gráfico comparativo das médias de obesidade ao longo do tempo para o Brasil em azul e para os outros países (excluindo o Brasil) em vermelho.
"""

# Calcular a média da obesidade para cada ano no Brasil
media_obesidade_brasil = df_brasil.groupby('Year')['Obesity no interval'].mean()

# Filtrar os dados para incluir apenas os registros de outros países (excluindo o Brasil)
df_outros_paises = df_obesidade[df_obesidade['Country'] != 'Brazil']

# Calcular a média da obesidade para cada ano nos outros países
media_obesidade_outros_paises = df_outros_paises.groupby('Year')['Obesity no interval'].mean()

# Plotar os gráficos comparativos das médias de obesidade ao longo do tempo
plt.figure(figsize=(10, 6))
plt.plot(media_obesidade_brasil.index, media_obesidade_brasil, label='Brasil', color='blue')
plt.plot(media_obesidade_outros_paises.index, media_obesidade_outros_paises, label='Outros países', color='red')
plt.title('Comparação da obesidade: Brasil vs. Outros países')
plt.xlabel('Ano')
plt.ylabel('Média de obesidade (%)')
plt.legend()
plt.grid(True)
plt.show()

"""Agora, há um interesse em saber quando o Brasil esteve abaixo da média mundial e acima da média mundial. O código a seguir visa resolver esse problema."""

# 1. Calcule a média mundial de obesidade para cada ano
media_obesidade_mundial = df_obesidade.groupby('Year')['Obesity no interval'].mean()

# 2. Calcule a média de obesidade para o Brasil para cada ano
media_obesidade_brasil = df_brasil.groupby('Year')['Obesity no interval'].mean()

# 3. Compare a média de obesidade do Brasil com a média mundial para cada ano
diferenca_obesidade = media_obesidade_brasil - media_obesidade_mundial

# 4. Identifique os anos em que a média de obesidade do Brasil está acima e abaixo da média mundial
anos_acima_media = diferenca_obesidade[diferenca_obesidade > 0].index
anos_abaixo_media = diferenca_obesidade[diferenca_obesidade < 0].index

# 5. Encontre o intervalo de anos em que o Brasil está acima e abaixo da média mundial
intervalo_acima_media = (anos_acima_media.min(), anos_acima_media.max())
intervalo_abaixo_media = (anos_abaixo_media.min(), anos_abaixo_media.max())

print("Intervalo em que o Brasil está acima da média mundial de obesidade:", intervalo_acima_media)
print("Intervalo em que o Brasil está abaixo da média mundial de obesidade:", intervalo_abaixo_media)

"""### Um aspecto adicional: previsão para obesos em 2023 usando regressão linear."""

import numpy as np
from sklearn.linear_model import LinearRegression

# Dados históricos de obesidade no Brasil
anos_hist = np.array(df_brasil['Year']).reshape(-1, 1)  # Anos como matriz de uma coluna
obesidade_hist = np.array(df_brasil['Obesity no interval'])  # Taxa de obesidade

# Ajustar um modelo de regressão linear aos dados históricos
modelo = LinearRegression()
modelo.fit(anos_hist, obesidade_hist)

# Prever a taxa de obesidade em 2024
obesidade_2023 = modelo.predict([[2023]])

print("Estimativa de % obesidade no Brasil em 2023:", obesidade_2023[0])

"""Gráfico tirado do Ministério da saúde com os dados

![Obesidade no Brasil](https://raw.githubusercontent.com/eng-joaoelias/AnaliseDadosBigData/main/DataSetADBD/obesos_brasil_grafico.jpeg)
"""

#Calculando o erro absoluto da previsão

err_abs = round(abs(obesidade_2023[0] - 24.3), 2)
print('Erro absoluto na previsão do modelo: {}%'.format(err_abs))

"""### Comparação entre a obesidade masculina e feminina
Nesta secção, será revelado o quanto a obesidade média masculina representa, no Brasil, em relação a feminina
"""

media_obesidade_geral_masc_br = df_brasil_male['Obesity no interval'].mean()
media_obesidade_geral_fem_br = df_brasil_female['Obesity no interval'].mean()
media_relativa_masc_fem = media_obesidade_geral_masc_br / media_obesidade_geral_fem_br
if media_relativa_masc_fem < 1:
  print('No geral, os homens são menos obesos que as mulheres. Representam {}% da média de mulheres.'.format(100*round(media_relativa_masc_fem, 4)))
else:
  print('No geral, os homens são mais obesos que as mulheres. Representam {}% da média de homens.'.format(100*round(media_relativa_masc_fem, 4)))

"""### Diferenças de Gênero
Aqui, será mostrada a prevalência da obesidade entre homens e mulheres ao longo dos anos. Isso pode revelar se há diferenças significativas na tendência de obesidade entre os gêneros.
"""

# Plotar gráficos de obesidade por gênero
plt.figure(figsize=(10, 6))
plt.plot(df_brasil_male['Year'], df_brasil_male['Obesity no interval'], marker='o', color='blue', label='Homens')
plt.plot(df_brasil_female['Year'], df_brasil_female['Obesity no interval'], marker='o', color='red', label='Mulheres')
plt.title('Prevalência da Obesidade por Gênero no Brasil')
plt.xlabel('Ano')
plt.ylabel('Obesidade (%)')
plt.legend()
plt.grid(True)
plt.show()

# Calcular a diferença de obesidade entre homens e mulheres para cada ano
df_diferencas = pd.DataFrame()
df_diferencas['Year'] = df_brasil_male['Year']  # Definir os anos como a primeira coluna

# Calcular a diferença de obesidade masculina e feminina para cada ano
df_diferencas['Diferenca_obesidade'] = df_brasil_female['Obesity no interval'].values - df_brasil_male['Obesity no interval'].values

# Contar os casos onde o percentual de obesidade feminina ultrapassa a masculina
casos_positivos = (df_diferencas['Diferenca_obesidade'] > 0).sum()

porcentagem_a_comparar = 50

if 100*(casos_positivos / len(df_diferencas.index)) > porcentagem_a_comparar:
  print('Há mais mulheres obesas do que homens.')
else:
  print('Há mais homens obesos do que mulheres.')

"""#### Prever a tendência de comportamento para os próximos 10 anos
Para isso, podemos usar redes neurais
"""

import tensorflow as tf

# Dados históricos de obesidade feminina
anos = np.array(df_brasil_female['Year']).reshape(-1, 1)  # Anos como matriz de uma coluna
obesidade = np.array(df_brasil_female['Obesity no interval'])  # Taxa de obesidade feminina

# Normalizar os dados
anos_norm = (anos - anos.min()) / (anos.max() - anos.min())
obesidade_norm = (obesidade - obesidade.min()) / (obesidade.max() - obesidade.min())

# Construir o modelo
model = tf.keras.Sequential([
    tf.keras.layers.Dense(10, activation='relu', input_shape=(1,)),
    tf.keras.layers.Dense(1)
])

# Compilar o modelo
model.compile(optimizer='adam', loss='mean_squared_error')

# Treinar o modelo
model.fit(anos_norm, obesidade_norm, epochs=1000, verbose=0)

# Prever a obesidade feminina para os próximos 10 anos
proximos_anos = np.arange(2017, 2027).reshape(-1, 1)  # Próximos 10 anos
proximos_anos_norm = (proximos_anos - anos.min()) / (anos.max() - anos.min())  # Normalizar os próximos anos
previsao_obesidade_norm = model.predict(proximos_anos_norm).flatten()  # Previsão da obesidade normalizada
previsao_obesidade = previsao_obesidade_norm * (obesidade.max() - obesidade.min()) + obesidade.min()  # Desnormalizar a previsão

# Exibir as previsões
print("Previsão da obesidade feminina para os próximos 10 anos:")
for ano, previsao in zip(proximos_anos.flatten(), previsao_obesidade):
    print("Ano:", ano, "Previsão:", previsao)

# Plotar o gráfico das previsões
plt.figure(figsize=(10, 6))
plt.plot(anos, obesidade, marker='o', linestyle='-', color='blue', label='Dados históricos')
plt.plot(proximos_anos, previsao_obesidade, marker='o', linestyle='--', color='red', label='Previsões')
plt.title('Previsão da obesidade feminina para os próximos 10 anos')
plt.xlabel('Ano')
plt.ylabel('Taxa de obesidade (%)')
plt.legend()
plt.grid(True)
plt.show()

"""#Sobre PIB Per Capita

## Abrindo o DataSet PIB Per Capita
"""

#df_pib_per_capita = pd.read_csv('/content/drive/MyDrive/DataSetADBD/PIB-Per-Capita.csv', sep = ',')
df_pib_per_capita = pd.read_csv('https://raw.githubusercontent.com/eng-joaoelias/AnaliseDadosBigData/main/DataSetADBD/PIB-Per-Capita.csv', sep = ',')
df_pib_per_capita

"""## Limpeza de dados"""

df_pib_per_capita['Year'].dtype

# Extrair apenas o ano da coluna 'Year' e converter para int
df_pib_per_capita['Year'] = df_pib_per_capita['Year'].str.extract('(\d{4})').astype(int)

df_pib_per_capita

#Remover os registros anteriores a 1975
df_pib_per_capita = df_pib_per_capita.query('Year >= 1975')

df_pib_per_capita

"""## Os dados estão separados de 5 em 5 anos. Adapte preenchendo os anos vazios.
>Dica: faça uma média entre um valor e outro, dívida por 5, e interpole esses valores.
"""

print(df_pib_per_capita.columns) #Inicialmente, ver quais sao as colunas

df_pib_per_capita[' GDP_pp '].dtype #Precisamos converter a coluna do valor do PIB per capita em float

# Garantir que a coluna ' GDP_pp ' esteja no formato float
df_pib_per_capita[' GDP_pp '] = df_pib_per_capita[' GDP_pp '].str.replace(',', '').astype(float)

# Função para interpolar valores de PIB per capita e preencher anos ausentes
def interpolate_gdp(group):
    # Criar um DataFrame com todos os anos no intervalo desejado
    all_years = pd.DataFrame({'Year': range(group['Year'].min(), 2017)})
    # Fazer o merge com os dados do grupo para garantir todos os anos
    group = pd.merge(all_years, group, how='left', on='Year')
    # Preencher colunas 'Country' e 'Region' com valores corretos
    group['Country'] = group['Country'].fillna(method='ffill').fillna(method='bfill')
    group['Region'] = group['Region'].fillna(method='ffill').fillna(method='bfill')
    # Preencher os valores ausentes usando interpolação linear
    group[' GDP_pp '] = group[' GDP_pp '].interpolate(method='linear')
    return group

# Aplicar a interpolação para cada país
df_pib_per_capita = df_pib_per_capita.groupby('Country').apply(interpolate_gdp).reset_index(drop=True)

df_pib_per_capita

#Se os dados de entrada não tiverem valores diferentes para interpolar, a interpolação linear não poderá produzir novos valores.
df_pib_per_capita[(df_pib_per_capita['Country'] == 'Brazil') & (df_pib_per_capita['Year'] >= 2010)]

"""### Plot um gráfico"""

# Calcular a média do PIB per capita para cada país
mean_gdp_per_capita = df_pib_per_capita.groupby('Country')[' GDP_pp '].mean()

# Resetar o índice para transformar 'Country' em uma coluna
mean_gdp_per_capita = mean_gdp_per_capita.reset_index()

# Plotar o gráfico de barras
plt.figure(figsize=(12, 8))
bars = plt.bar(mean_gdp_per_capita['Country'], mean_gdp_per_capita[' GDP_pp '], color='skyblue')

plt.xlabel('Country')
plt.ylabel('Average GDP per Capita')
plt.title('Average GDP per Capita by Country')

plt.xticks(rotation=90)  # Rotacionar os rótulos dos países para melhor visualização
plt.tight_layout()  # Ajustar o layout para evitar cortes nos nomes dos países

# Ajustar os rótulos dos países de forma escalonada
plt.gca().set_xticks(mean_gdp_per_capita['Country'][::10])
plt.gca().set_xticklabels(mean_gdp_per_capita['Country'][::10], rotation=45, ha='right')

plt.show()

"""Exibição dos rótulos dos países de forma escalonada, exibindo apenas cada décimo país. Isso ajuda a evitar a sobreposição de rótulos e melhora a legibilidade do gráfico.

### Informe as regiões de maiores crescimentos de PIB. Use gráficos para finalizar a resposta.
"""

df_pib_per_capita['Region'].value_counts() #Exibindo quais são as regiões do PIB per capita.

"""1. **Calcular a variação do PIB per capita por região ao longo do tempo**: Para isso, precisamos agrupar os dados por região e ano, calcular a média do PIB per capita por ano para cada região e, em seguida, calcular a variação do PIB per capita ao longo do tempo.
2. **Identificar as regiões com maiores crescimentos**: Com a variação calculada, podemos identificar as regiões com os maiores crescimentos.
"""

# Calcular a média do PIB per capita por ano para cada região
df_mean_gdp = df_pib_per_capita.groupby(['Region', 'Year'])[' GDP_pp '].mean().reset_index()

# Pivotar os dados para ter os anos como colunas e as regiões como linhas
df_pivot = df_mean_gdp.pivot(index='Region', columns='Year', values=' GDP_pp ')

# Calcular a variação percentual do PIB per capita
growth = df_pivot.pct_change(axis='columns') * 100

# Calcular a média da variação percentual ao longo dos anos para cada região
average_growth = growth.mean(axis=1)

# Identificar as regiões com maiores crescimentos
top_regions = average_growth.sort_values(ascending=False)

print("Crescimento médio anual de cada região\n", top_regions)

# Encontrar o primeiro e o último ano do DataFrame
first_year = df_pib_per_capita['Year'].min()
last_year = df_pib_per_capita['Year'].max()

# Filtrar os dados para o primeiro e o último ano
df_first_year = df_pib_per_capita[df_pib_per_capita['Year'] == first_year]
df_last_year = df_pib_per_capita[df_pib_per_capita['Year'] == last_year]

# Calcular a média do PIB per capita no primeiro e no último ano para cada região
gdp_first_year = df_first_year.groupby('Region')[' GDP_pp '].mean()
gdp_last_year = df_last_year.groupby('Region')[' GDP_pp '].mean()

# Calcular o crescimento percentual geral
growth_general = ((gdp_last_year - gdp_first_year) / gdp_first_year) * 100

# Ordenar as regiões pelo crescimento percentual geral
growth_general_sorted = growth_general.sort_values(ascending=False)

print("Crescimento geral das regiões:\n", growth_general_sorted)

"""#### Gráfico para mostrar o crescimento/descrescimento do PIB *per capita* de cada região"""

# Plotar o gráfico
plt.figure(figsize=(12, 8))
for region in df_mean_gdp['Region'].unique():
    region_data = df_mean_gdp[df_mean_gdp['Region'] == region]
    plt.plot(region_data['Year'], region_data[' GDP_pp '], label=region)

plt.title('Crescimento do PIB per capita por região ao longo do tempo')
plt.xlabel('Ano')
plt.ylabel('PIB per capita')
plt.legend()
plt.grid(True)
plt.show()

"""## Quanto mais rico, mais obeso?

Primeiramente, os países estão com grafias distintas
"""

df_obesidade['Country'].unique()

df_pib_per_capita['Country'].unique()

"""Devemos criar um dicionário de mapeamento para mapear as grafias dos países de um dataset para o outro.

"""

# Dicionário de mapeamento
country_mapping = {
    'Bolivia (Plurinational State of)': 'Bolivia',
    'Cape Verde': 'Cabo Verde',
    'Czechia': 'Czech Rep.',
    "Democratic People's Republic of Korea": 'Korea, Dem. Rep.',
    'Republic of Korea': 'Korea, Rep.',
    "Côte d'Ivoire": "Cote d'Ivoire",
    'United Kingdom of Great Britain and Northern Ireland': 'United Kingdom',
    'United States of America': 'United States',
    'Venezuela (Bolivarian Republic of)': 'Venezuela',
    'Viet Nam': 'Vietnam',
    'Syrian Arab Republic': 'Syria',
    'Iran (Islamic Republic of)': 'Iran'
}

"""2. Substituição dos Nomes dos Países"""

# Substituir os nomes dos países no dataset de obesidade
df_obesidade['Country'] = df_obesidade['Country'].replace(country_mapping)

# Substituir os nomes dos países no dataset de PIB per capita (se necessário)
df_pib_per_capita['Country'] = df_pib_per_capita['Country'].replace(country_mapping)

"""3. Filtragem e Mesclagem dos Dados"""

# Filtrar o dataframe de obesidade para incluir apenas 'Both Sexes'
df_obesidade_both_sexes = df_obesidade[df_obesidade['Sex'] == 'Both sexes']

# Selecionar as colunas desejadas dos dataframes
df_obesidade_filtered = df_obesidade_both_sexes[['Country', 'Year', 'Obesity no interval']]
df_pib_filtered = df_pib_per_capita[['Country', 'Year', 'Region', ' GDP_pp ']]

# Mesclar os dataframes com base nas colunas 'Country' e 'Year'
df_combined = pd.merge(df_obesidade_filtered, df_pib_filtered, on=['Country', 'Year'], how='inner')

df_combined

# Calcular a média do PIB per capita e obesidade por região ou país
mean_data = df_combined.groupby(['Region', 'Country']).mean()

# Plotar um gráfico de dispersão
plt.figure(figsize=(10, 6))
sns.scatterplot(data=mean_data, x=' GDP_pp ', y='Obesity no interval', hue='Region', palette='Set2')
plt.xlabel('PIB per capita')
plt.ylabel('Obesidade')
plt.title('Relação entre PIB per capita e Obesidade por Região')
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
plt.show()

# Calcular a correlação entre PIB per capita e obesidade
correlation = mean_data[' GDP_pp '].corr(mean_data['Obesity no interval'])
print("Correlação entre PIB per capita e obesidade:", correlation)

"""Uma correlação de 0.388 sugere uma correlação positiva moderada entre o PIB per capita e a obesidade. Isso significa que há uma tendência de que países com um PIB per capita mais alto também tenham níveis mais altos de obesidade. No entanto, a correlação não é muito forte, o que significa que outros fatores também podem influenciar os níveis de obesidade em um país. Portanto, podemos dizer que a afirmação "Quanto mais rico, mais obeso" tem algum suporte com base nos dados, mas a relação não é tão forte e outros fatores também devem ser considerados."""

# Gráfico de calor com a correlação entre PIB per capita e obesidade
plt.figure(figsize=(10, 8))
sns.heatmap(df_combined[[' GDP_pp ', 'Obesity no interval']].corr(), annot=True, cmap='coolwarm', fmt=".2f")
plt.title('Correlação entre PIB per capita e Obesidade')
plt.show()

"""## O resultado em 1 é o mesmo no Brasil? Qual a diferença entre Brasil, USA e Portugal?"""

# Filtrar os dados para Brasil, USA e Portugal
countries_of_interest = ['Brazil', 'United States', 'Portugal']
df_filtered = df_combined[df_combined['Country'].isin(countries_of_interest)]

# Função para calcular a correlação entre PIB per capita e obesidade para um país específico
def calculate_correlation(df, country):
    df_country = df[df['Country'] == country]
    correlation = df_country[' GDP_pp '].corr(df_country['Obesity no interval'])
    return correlation

# Calcular a correlação para Brasil, EUA e Portugal
correlation_brazil = calculate_correlation(df_filtered, 'Brazil')
correlation_usa = calculate_correlation(df_filtered, 'United States')
correlation_portugal = calculate_correlation(df_filtered, 'Portugal')

# Exibir os resultados
print(f"Correlação entre PIB per capita e obesidade no Brasil: {correlation_brazil}")
print(f"Correlação entre PIB per capita e obesidade nos EUA: {correlation_usa}")
print(f"Correlação entre PIB per capita e obesidade em Portugal: {correlation_portugal}")

# Analisar os resultados
differences = {
    "Brasil vs EUA": correlation_brazil - correlation_usa,
    "Brasil vs Portugal": correlation_brazil - correlation_portugal,
    "EUA vs Portugal": correlation_usa - correlation_portugal
}

print("Diferenças de correlação:")
for comparison, difference in differences.items():
    print(f"{comparison}: {difference}")

"""1.   A relação entre PIB per capita e obesidade é ligeiramente mais forte nos EUA do que no Brasil.
2.   A relação entre PIB per capita e obesidade é ligeiramente mais forte no Brasil do que em Portugal, mas a diferença é muito pequena.
3.   A relação entre PIB per capita e obesidade é um pouco mais forte nos EUA do que em Portugal.




"""

# Configurar o estilo dos gráficos
sns.set(style="whitegrid")

# Criar o gráfico de dispersão com linhas de regressão
plt.figure(figsize=(10, 6))
scatter_plot = sns.lmplot(
    data=df_filtered,
    x=' GDP_pp ',
    y='Obesity no interval',
    hue='Country',
    ci=None,  # Remove o intervalo de confiança para as linhas de regressão
    height=6,
    aspect=1.5,
    markers=['o', 's', 'D'],  # Diferentes marcadores para cada país
    palette='Set1'  # Paleta de cores para diferenciar os países
)

# Ajustar o título e os rótulos dos eixos
plt.title('Relação entre PIB per capita e Obesidade por País', fontsize=15)
plt.xlabel('PIB per capita', fontsize=12)
plt.ylabel('Obesidade (%)', fontsize=12)

# Mostrar o gráfico
plt.show()

"""Ao analisar as diferenças entre Brasil, Estados Unidos e Portugal em relação à correlação entre PIB per capita e obesidade, podemos destacar algumas possíveis razões para as discrepâncias nos resultados:

1. **Contexto Socioeconômico**:
   - Cada país possui um contexto socioeconômico único, com diferentes níveis de desenvolvimento econômico, distribuição de renda, acesso a serviços de saúde e políticas públicas relacionadas à alimentação e estilo de vida. Essas diferenças podem influenciar a relação entre PIB per capita e obesidade.

2. **Hábitos Alimentares e Estilo de Vida**:
   - Os hábitos alimentares e o estilo de vida variam entre os países. Por exemplo, o padrão alimentar tradicional pode diferir significativamente entre o Brasil, os Estados Unidos e Portugal, afetando os índices de obesidade em cada país.

3. **Políticas de Saúde Pública e Prevenção**:
   - As políticas de saúde pública e prevenção da obesidade também podem ser diferentes em cada país. Isso inclui iniciativas governamentais relacionadas à educação nutricional, acesso a alimentos saudáveis, restrições à publicidade de alimentos não saudáveis, promoção da atividade física, entre outros.

4. **Cultura e Percepções Sociais**:
   - A cultura e as percepções sociais em relação à alimentação, imagem corporal e saúde podem variar entre os países. Por exemplo, atitudes em relação ao peso corporal, dietas da moda e estigma associado à obesidade podem influenciar os padrões de obesidade em cada país.

5. **Estrutura Demográfica**:
   - As características demográficas de cada país, como idade, gênero, etnia e composição populacional, podem influenciar os padrões de obesidade e sua relação com o PIB per capita.

### Análise de Dados Temporais
A análise de correlação atual considera apenas os dados agregados. No entanto, ao analisar dados ao longo do tempo, pode-se obter insights mais profundos.

- **Analisar Tendências Temporais**: Verificar se a correlação entre obesidade e PIB per capita muda ao longo do tempo. Isso pode ser feito calculando correlações em diferentes períodos (por exemplo, décadas).
"""

# Calcular correlações em diferentes períodos
periods = [(1980, 1990), (1990, 2000), (2000, 2010), (2010, 2016)]
correlations = {}

for start, end in periods:
    df_period = df_combined[(df_combined['Year'] >= start) & (df_combined['Year'] <= end)]
    correlation = df_period[' GDP_pp '].corr(df_period['Obesity no interval'])
    correlations[f"{start}-{end}"] = correlation

#print(correlations)

print("Correlação por período:\n")
for period, correlation in correlations.items():
    print(f"{period}: {correlation}")

"""Correlação dentro de diferentes regiões para verificar se a relação entre obesidade e PIB per capita varia entre regiões."""

# Calcular correlação por região
regions = df_combined['Region'].unique()
regional_correlations = {}

for region in regions:
    df_region = df_combined[df_combined['Region'] == region]
    correlation = df_region[' GDP_pp '].corr(df_region['Obesity no interval'])
    regional_correlations[region] = correlation

for region, correlation in regional_correlations.items():
    print(f"{region}: {correlation}")

"""Hipóteses possíveis para explicar a alta correlação na América do Sul:

* **Mudança na dieta:** Com o crescimento econômico, pode haver uma mudança na alimentação da população, indo de uma dieta baseada em alimentos frescos para outra mais industrializada e processada, geralmente rica em açúcares e gorduras. Isso poderia contribuir para o aumento da obesidade.
* **Urbanização:** O desenvolvimento econômico muitas vezes está associado à urbanização. Nas cidades, as pessoas tendem a ter menos atividade física diária e o acesso a fast food e alimentos processados pode ser maior.
* **Menos acesso a alimentos saudáveis:** Em alguns casos, o crescimento econômico pode não ser uniforme, beneficiando apenas uma parcela da população. Isso poderia levar a uma situação onde as pessoas com menor poder aquisitivo teriam menos acesso a alimentos saudáveis, como frutas, verduras e legumes frescos.
"""
