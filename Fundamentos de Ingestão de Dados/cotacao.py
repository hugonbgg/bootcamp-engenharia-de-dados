#%%
#imports
import requests
import json


#%%
#Request da cotação do dólar em reais
url = 'https://economia.awesomeapi.com.br/json/last/USD-BRL'
ret = requests.get(url)

# %%
print(ret) #exibe a resposta
print(ret.text) #exibe o retorno em formato texto

# %%
#If para exibir o retorno ou o falhou
if ret:
    print(ret.text)
else:
    print('Falhou')

# %%
#transformando o retorno em json
json.loads(ret.text)
json.loads(ret.text)['USDBRL'] #como é um json dentro do outro, captura apenas o usdbrl
dolar = json.loads(ret.text)['USDBRL']
type(dolar)
dolar# %%

# %%
#printa a data de hoje e o valor da cotação
print(f"20 doláres hoje ({dolar['create_date'][:10]}) custam {round(float(dolar['bid']) * 20, 2)} reais")

#%%
#Salvando o codigo em uma função
def cotacao(qtd, moeda):
    url = f'https://economia.awesomeapi.com.br/json/last/{moeda}'
    
    ret = requests.get(url)
    moeda_cotacao = json.loads(ret.text)[moeda.replace('-','')]
    print(f'''
        {qtd} {moeda[:3]} custam hoje {round(float(moeda_cotacao['bid']) * 20)} {moeda[4:]}. 
        A cotação máxima do dia foi {float(moeda_cotacao['high']).__round__(2)} {moeda[4:]} e a minima {float(moeda_cotacao['low']).__round__(2)} {moeda[4:]}.
        ''')
    print(moeda_cotacao)
 
#%%
cotacao(20,'USD-BRL')


# %%


# %%
