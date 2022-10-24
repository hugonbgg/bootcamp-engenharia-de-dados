#%%
import requests
from bs4 import BeautifulSoup as bs
import logging
import pandas as pd

# %%
url= 'https://portalcafebrasil.com.br/todos/podcasts/'

# %%
ret = requests.get(url)
# %%
ret.text
# %%
# %
#lê utilizando o parser html
soup = bs(ret.text, 'html.parser')
# %%
soup
# %%
soup.prettify()
# %%
soup.find('h5') #encontrar as tags h5

# %%
soup.find('h5').text #retorna a parte de texto
# %%
soup.find('h5').a #retorna a parte que é a tag a
# %%
soup.find('h5').a['href'] #retorna o link
# %%
lst_episodios = soup.find_all('h5') #salva todas tags em uma lista
lst_episodios
# %%
#imprime os eps e seus links
for item in lst_episodios:
    print(f"EP: {item.text} - Link: {item.a['href']}")
# %%
######################
####Definindo o logger
log = logging.getLogger()
log.setLevel(logging.DEBUG)
formatter = logging.Formatter(
    '%(asctime)s - %(name)s - %(levelname)s - %(message)s')
ch = logging.StreamHandler()
ch.setFormatter(formatter)
log.addHandler(ch)

#Raspando todo o site
#definindo a url para receber o numero da pagina
url = 'https://portalcafebrasil.com.br/todos/podcasts/page/{}/?ajax=true'
# %%
url.format(5)
#%%
#função para obter os dados sobre os podcasts, o que foi feito acima agora em uma função
def get_podcast(url):
    ret = requests.get(url)
    soup = bs(ret.text, 'html.parser')
    return soup.find_all('h5')

# %%
get_podcast(url.format(5))
# %%
pagina = 1
lst_podcast = []
lst_get = get_podcast(url.format(pagina))
# %%
#log.debug(f"Coletado {len(lst_get)} episódios do link {url.format(pagina)}")
while len(lst_get) > 0:
    lst_podcast = lst_podcast + lst_get
    pagina += 1
    lst_get = get_podcast(url.format(pagina))
    log.debug(f"Coletado {len(lst_get)} episódios do link {url.format(pagina)}")


# %%
len(lst_podcast)
# %%
#Criando o dataframe
df = pd.DataFrame(columns=('nome', 'link'))

# %%
for item in lst_podcast:
    df.loc[df.shape[0]] = [item.text, item.a['href']]
# %%
df.shape
#%%
print(df.shape) #exibe a dimensão
print(df.shape[0]) #linhas
print(df.shape[1]) #Colunas
# %%
df.to_csv('banco_de_podcast.csv', sep = ";", index = False)
# %%
