#%%
import requests
import pandas as pd
from bs4 import BeautifulSoup as bs


# %%
#define a url para raspagem
url = 'https://www.vivareal.com.br/venda/parana/curitiba/apartamento_residencial/?pagina={}'
i = 1
ret = requests.get(url.format(i))
ret.text
# %%
#parseia o request
soup = bs(ret.text, 'html.parser')
# %%
#exibe o resultado
soup.prettify()
# %%
#define o conteudo que contem as infos sobre os imoveis
soup.find('a', attrs={'class':'property-card__content-link js-card-title'})
soup.find('a', attrs={'class':'property-card__content-link js-card-title'}).text

# %%
#salve em uma lista os imoveis da pagina
imoveis = soup.find_all('a', attrs={'class':'property-card__content-link js-card-title'})
imoveis
# %%
#intera e exibe os imoveis 
for imovel in imoveis:
    print (imovel.text)
# %%
#exibe a qtd de imoveis capturados
len(imoveis)
# %%
#captura o valor de imoveis exibidos na pagina
qtd_imoveis = int(soup.find('strong', attrs= {'class':'results-summary__count js-total-records'}).text.replace('.',''))
qtd_imoveis# %%

# %%
#seleciona um imovel para os testes a seguir
imovel = imoveis[0]
# %%
#exibe o imovel selecionado
imovel
# %%
#salva em variáveis as informações de interesse
descricao = imovel.find('span', attrs = {'class':'property-card__title'}).text.strip()
endereco = imovel.find('span', attrs = {'class':'property-card__address'}).text.strip()
area = imovel.find('span', attrs = {'class':'property-card__detail-area'}).text.strip()
quartos = imovel.find('li', attrs = {'class':'property-card__detail-room'}).span.text.strip()
wc = imovel.find('li', attrs = {'class':'property-card__detail-bathroom'}).span.text.strip()
vagas = imovel.find('li', attrs = {'class':'property-card__detail-garage'}).span.text.strip()
valor = imovel.find('div', attrs = {'class':'property-card__price'}).p.text.strip()
condominio = imovel.find('strong', attrs = {'class':'js-condo-price'}).text.strip()
weblink = 'https://www.vivareal.com.br' + imovel['href']

#printa as infos dos imoveis
print(descricao)
print(endereco)
print(area)
print(quartos)
print(wc)
print(vagas)
print(valor)
print(condominio)
print(weblink)


# %%
#cria um df com as colunas definidas para salvar os registros
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
#zera o contador
i = 0
# %%
#intera sobre as paginas para capturar os registros enquanto o numero de registros for menor que o exibido na pagina do viva real(qtd_imoveis)
#try e except para os campos que não existem em alguns registros, como o condominio.
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
#Salvando as variaveis no df
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
