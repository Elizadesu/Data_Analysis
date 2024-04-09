import pandas as pd
import requests

# Specify the file path
df = pd.read_csv('integracao\\Dataset .csv')

#Media de todas as ratings
rating=df["Aggregate rating"]
media_coluna = rating.mean()
# ou media_coluna=df["Aggregate rating"].mean()
print("A média da coluna médias é:", media_coluna)


#Média de rating para um Restaurante especifico por ID
ID=6314605
id_restaurant=df[df["Restaurant ID"] == ID]
rating_restaurant=id_restaurant['Aggregate rating'].mean()
restaurant_name = str(id_restaurant.loc[id_restaurant.index[0], 'Restaurant Name'])

print("A avaliação média do restaurante", restaurant_name,"é:", rating_restaurant)

#Média de rating para uma cidade
Cidade='Rio de Janeiro'
city_restaurant=df[df["City"] == Cidade]
rating_city=city_restaurant['Aggregate rating'].mean()

print('A avaliação média de restaurantes da cidade',Cidade,'é:',rating_city)

#O restaurante com o menor preço medio para dois
#Convertendo tudo a dolar
#currencies=df['Currency']
#print(currencies.drop_duplicates())

df_dolar=df.copy()
url = 'https://api.exchangerate-api.com/v4/latest/usd'
response = requests.get(url)
data = response.json()

for indice, linha in df_dolar.iterrows():
    if linha['Currency'] == 'Botswana Pula(P)':
       df_dolar.at[indice,'ACF2Dolar'] = float(linha['Average Cost for two'])/data['rates']['BWP']
    
    elif linha['Currency'] == 'Brazilian Real(R$)':
        df_dolar.at[indice,'ACF2Dolar'] = float(linha['Average Cost for two'])/data['rates']['BRL']

    elif linha['Currency'] == 'Dollar($)':
        df_dolar.at[indice,'ACF2Dolar'] = float(linha['Average Cost for two'])/data['rates']['USD']

    elif linha['Currency'] == 'Emirati Diram(AED)':
        df_dolar.at[indice,'ACF2Dolar'] = float(linha['Average Cost for two'])/data['rates']['AED']

    elif linha['Currency'] == 'Indian Rupees(Rs.)':
        df_dolar.at[indice,'ACF2Dolar'] = float(linha['Average Cost for two'])/data['rates']['INR']

    elif linha['Currency'] == 'Indonesian Rupiah(IDR)':
        df_dolar.at[indice,'ACF2Dolar'] = float(linha['Average Cost for two'])/data['rates']['IDR']

    elif linha['Currency'] == 'NewZealand($)':
        df_dolar.at[indice,'ACF2Dolar'] = float(linha['Average Cost for two'])/data['rates']['NZD']

    elif linha['Currency'] == 'Pounds(��)':
        df_dolar.at[indice,'ACF2Dolar'] = float(linha['Average Cost for two'])/data['rates']['GBP']

    elif linha['Currency'] == 'Qatari Rial(QR)':
        df_dolar.at[indice,'ACF2Dolar'] = float(linha['Average Cost for two'])/data['rates']['QAR']

    elif linha['Currency'] == 'Rand(R)':
        df_dolar.at[indice,'ACF2Dolar'] = float(linha['Average Cost for two'])/data['rates']['ZAR']

    elif linha['Currency'] == 'Sri Lankan Rupee(LKR)':
        df_dolar.at[indice,'ACF2Dolar'] =float(linha['Average Cost for two'])/data['rates']['LKR']

    elif linha['Currency'] == 'Turkish Lira(TL)':
        df_dolar.at[indice,'ACF2Dolar'] = float(linha['Average Cost for two'])/data['rates']['TRY']

#Encontrando o restaurante com o menor preço medio para dois
preco=df_dolar[df_dolar['ACF2Dolar'] != 0]['ACF2Dolar']
menor_preco = preco.min()
linha_menor_preco = df_dolar[df_dolar['ACF2Dolar'] == menor_preco]
quantidade_linhas = linha_menor_preco.shape[0]

print("Menor preço médio:", menor_preco)
print("Os restaurantes com os menores preços são:")
i=0
while i < quantidade_linhas:
    print(linha_menor_preco.iloc[i]['Restaurant Name'])
    i += 1


#O Restaurante com a maior quantidade de votos
votos=df['Votes']
max_rating=votos.max()
linha_mais_votos = df[df['Votes'] == max_rating]
rest_max_rat=linha_mais_votos.iloc[0]['Restaurant Name']
city_max_rat=linha_mais_votos.iloc[0]['City']
print('O Restaurante que recebeu mais votos é',rest_max_rat,'na cidade de',city_max_rat,'com',max_rating,'votos')