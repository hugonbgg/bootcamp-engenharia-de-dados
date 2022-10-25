#%%
import requests
import pandas as pd
from bs4 import BeautifulSoup as bs

# %%
url = 'https://www.vivareal.com.br/venda/parana/curitiba/apartamento_residencial/?pagina={}'
ret = requests.get(url)
ret.text
# %%
soup = bs(ret.text, 'html.parser')
# %%
soup.prettify()
# %%
soup.find('a', attrs={'class':'property-card__content-link js-card-title'})
soup.find('a', attrs={'class':'property-card__content-link js-card-title'}).text

# %%
soup.find_all('a', attrs={'class':'property-card__content-link js-card-title'})
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
