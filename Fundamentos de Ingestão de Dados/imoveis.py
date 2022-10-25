#%%
import requests
import pandas as pd
from bs4 import BeautifulSoup as bs


# %%
url = 'https://www.vivareal.com.br/venda/parana/curitiba/apartamento_residencial/?pagina={}'
i = 1
ret = requests.get(url.format(i))
ret.text
# %%
soup = bs(ret.text, 'html.parser')
# %%
soup.prettify()
# %%
soup.find('a', attrs={'class':'property-card__content-link js-card-title'})
soup.find('a', attrs={'class':'property-card__content-link js-card-title'}).text

# %%
imoveis = soup.find_all('a', attrs={'class':'property-card__content-link js-card-title'})
imoveis
# %%
for imovel in imoveis:
    print (imovel.text)
# %%
len(imoveis)
# %%
qtd_imoveis = int(soup.find('strong', attrs= {'class':'results-summary__count js-total-records'}).text.replace('.',''))
qtd_imoveis# %%

# %%
imovel = imoveis[0]
# %%
imovel
# %%
descricao = imovel.find('span', attrs = {'class':'property-card__title'}).text.strip()
endereco = imovel.find('span', attrs = {'class':'property-card__address'}).text.strip()
area = imovel.find('span', attrs = {'class':'property-card__detail-area'}).text.strip()
quartos = imovel.find('li', attrs = {'class':'property-card__detail-room'}).span.text.strip()
wc = imovel.find('li', attrs = {'class':'property-card__detail-bathroom'}).span.text.strip()
vagas = imovel.find('li', attrs = {'class':'property-card__detail-garage'}).span.text.strip()
valor = imovel.find('div', attrs = {'class':'property-card__price'}).p.text.strip()
condominio = imovel.find('strong', attrs = {'class':'js-condo-price'}).text.strip()
weblink = 'https://www.vivareal.com.br' + imovel['href']


print(descricao)
print(endereco)
print(area)
print(quartos)
print(wc)
print(vagas)
print(valor)
print(condominio)
print(weblink)

#%%

# %%
df = pd.DataFrame(
    columns=[
        'descricao',
        'endereco',
        'area',
        'quartos',
        'wc',
        'vagas',
        'valor',
        'condominio',
        'weblink'
        ]
)

i = 0
# %%
while qtd_imoveis > df.shape[0]:
    i += 1
    print(f"Valor i: {i} \t\t quantidade de imóveis: {df.shape[0]}")
    ret = requests.get(url.format(i))
    soup = bs(ret.text)
    imoveis = soup.find_all('a', attrs={'class':'property-card__content-link js-card-title'})

for imovel in imoveis:
    try: 
        descricao = imovel.find('span', attrs = {'class':'property-card__title'}).text.strip()
    except:
        descricao = None
    try: 
        endereco = imovel.find('span', attrs = {'class':'property-card__address'}).text.strip()
    except:
        endereco = None
    try: 
        area = imovel.find('span', attrs = {'class':'property-card__detail-area'}).text.strip()
    except:
        area = None
    try: 
        quartos = imovel.find('li', attrs = {'class':'property-card__detail-room'}).span.text.strip()
    except:
        quartos = None
    try: 
        wc = imovel.find('li', attrs = {'class':'property-card__detail-bathroom'}).span.text.strip()
    except:
        wc = None
    try: 
        vagas = imovel.find('li', attrs = {'class':'property-card__detail-garage'}).span.text.strip()
    except:
        vagas = None
    try: 
        valor = imovel.find('div', attrs = {'class':'property-card__price'}).p.text.strip()
    except:
        valor = None
    try: 
        condominio = imovel.find('strong', attrs = {'class':'js-condo-price'}).text.strip()
    except:
        condominio = None
    try: 
        weblink = 'https://www.vivareal.com.br' + imovel['href']
    except:
        weblink = None

    df.loc[df.shape[0]] = [
        descricao,
        endereco,
        area,
        quartos,
        wc,
        vagas,
        valor,
        condominio,
        weblink
    ]
# %%
df
# %%
