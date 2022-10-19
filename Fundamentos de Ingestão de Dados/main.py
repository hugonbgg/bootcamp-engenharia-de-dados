#%%
#imports
import requests
import json


#%%
url = 'https://economia.awesomeapi.com.br/json/last/USD-BRL'
ret = requests.get(url)

# %%
print(ret)
print(ret.text)

# %%
if ret:
    print(ret.text)
else:
    print('Falhou')

# %%
json.loads(ret.text)
json.loads(ret.text)['USDBRL']
dolar = json.loads(ret.text)['USDBRL']
type(dolar)
dolar# %%

# %%
print(f"20 doláres hoje ({dolar['create_date'][:10]}) custam {round(float(dolar['bid']) * 20, 2)} reais")

# %%
