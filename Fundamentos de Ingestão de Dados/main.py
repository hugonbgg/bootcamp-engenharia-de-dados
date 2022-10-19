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

# %%

