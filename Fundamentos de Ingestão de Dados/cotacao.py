#%%
#imports
from logging import exception
from numpy import inner
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
    'RPL-BRL' 
] #RPL-BRL Essa moeda não existe

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
#Criando uma função multi moeda
def multi_moeda(valor):
    lst_moedas = [
        'USD-BRL',
        'EUR-BRL',
        'BTC-BRL',
        'JPY-BRL',
        'RPL-BRL' 
    ]

    for moeda in lst_moedas:
        cotacao(valor, moeda)

# %%
multi_moeda(20)
# %%
#usando decoretors para checar as funções

def error_check(func):
    def inner_func(*args, **kargs):
        try:
            func(*args, **kargs)
        except:
            print(f"{func.__name__} {moeda} falhou!")
    return inner_func

# %%
@error_check
def multi_moeda(valor):
    lst_moedas = [
        'USD-BRL',
        'EUR-BRL',
        'BTC-BRL',
        'JPY-BRL',
        'RPL-BRL' 
    ]

    for moeda in lst_moedas:
        cotacao(valor, moeda)
multi_moeda(1)# %%

# %%
#simulando uma api
import backoff
import random

def test_func(*args, **kargs):
    rnd = random.randint(100, 1000)
    print(f"""
            RND: {rnd}
            args: {args if args else 'sem args'}
            kargs: {kargs if kargs else 'sem kargs'}
        """)
    if rnd < 200:
        raise ConnectionAbortedError('Conexão foi finalizada')
    elif rnd < 400:
        raise ConnectionRefusedError('Conexão foi recusada')
    elif rnd < 600:
        raise TimeoutError('Tempo de espera excedido')
    else:
        return "OK!"

# %%
test_func()
# %%
#Simulando a API e usando o backoff
@backoff.on_exception(backoff.expo, (ConnectionAbortedError, ConnectionRefusedError, TimeoutError), max_tries=10)
def test_func(*args, **kargs):
    rnd = random.randint(100, 1000)
    print(f"""
            RND: {rnd}
            args: {args if args else 'sem args'}
            kargs: {kargs if kargs else 'sem kargs'}
        """)
    if rnd < 200:
        raise ConnectionAbortedError('Conexão foi finalizada')
    elif rnd < 400:
        raise ConnectionRefusedError('Conexão foi recusada')
    elif rnd < 600:
        raise TimeoutError('Tempo de espera excedido')
    else:
        return "OK!"

test_func()# %%

# %%
