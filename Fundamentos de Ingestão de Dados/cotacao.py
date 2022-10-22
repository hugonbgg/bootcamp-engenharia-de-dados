#%%
#imports
from logging import exception
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
        {qtd} {moeda[:3]} custam hoje {float(moeda_cotacao['bid']).__round__(3) * qtd} {moeda[4:]}. 
        A cotação máxima do dia foi {float(moeda_cotacao['high']).__round__(2)} {moeda[4:]} e a minima {float(moeda_cotacao['low']).__round__(2)} {moeda[4:]}.
        ''')
    #print(moeda_cotacao)
 
#%%
cotacao(1,'USD-BRL')


# %%
cotacao(1, 'JPY-BRL')

# %%
#Simulando um erro
#a moeda hugo não existe
cotacao(20, 'Hugo')

# %%
#exemplo para imprimir apenas o erro
try:
    10/0
except Exception as e:
    print(e)
else:
    print("Ok")
# %%
try:
    10/2
except Exception as e:
    print(e)
else:
    print("Ok")

# %%
try:
    cotacao(20, 'Hugo')
except Exception as e:
    print(e)
else:
    print("Ok")
# %%
try:
    cotacao(20, 'JPY-BRL')
except Exception as e:
    print(e)
else:
    print("Ok")

# %%
#Rodando uma lista de moedas
lst_moedas = [
    'USD-BRL',
    'EUR-BRL',
    'BTC-BRL',
    'JPY-BRL',
    'RPL-BRL' #Essa moeda não existe
]

# %%
for moeda in lst_moedas:
    cotacao(1, moeda)
    

# %%
#desse modo ignora a moeda com erro
for moeda in lst_moedas:
    try:
        cotacao(1, moeda)
    except:
        pass
# %%
for moeda in lst_moedas:
    try:
        cotacao(1, moeda)
    except:
        print(f" Falha na moeda {moeda}")


# %%
