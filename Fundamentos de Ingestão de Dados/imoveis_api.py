#%%
from webbrowser import get
import requests
import pandas as pd
from bs4 import BeautifulSoup as bs
import json
import time

# %%
url = '''https://glue-api.vivareal.com/v2/listings?addressCity=Curitiba&addressLocationId=BR%3EParana%3ENULL%3ECuritiba&addressNeighborhood=&addressState=Paran%C3%A1&addressCountry=Brasil&addressStreet=&addressZone=&addressPointLat=-25.437238&addressPointLon=-49.269973&business=SALE&facets=amenities&unitTypes=APARTMENT&unitSubTypes=UnitSubType_NONE,DUPLEX,LOFT,STUDIO,TRIPLEX&unitTypesV3=APARTMENT&usageTypes=RESIDENTIAL&listingType=USED&parentId=null&categoryPage=RESULT&includeFields=search(result(listings(listing(displayAddressType,amenities,usableAreas,constructionStatus,listingType,description,title,unitTypes,nonActivationReason,propertyType,unitSubTypes,id,portal,parkingSpaces,address,suites,publicationType,externalId,bathrooms,usageTypes,totalAreas,advertiserId,bedrooms,pricingInfos,showPrice,status,advertiserContact,videoTourLink,whatsappNumber,stamps),account(id,name,logoUrl,licenseNumber,showAddress,legacyVivarealId,phones),medias,accountLink,link)),totalCount),page,seasonalCampaigns,fullUriFragments,nearby(search(result(listings(listing(displayAddressType,amenities,usableAreas,constructionStatus,listingType,description,title,unitTypes,nonActivationReason,propertyType,unitSubTypes,id,portal,parkingSpaces,address,suites,publicationType,externalId,bathrooms,usageTypes,totalAreas,advertiserId,bedrooms,pricingInfos,showPrice,status,advertiserContact,videoTourLink,whatsappNumber,stamps),account(id,name,logoUrl,licenseNumber,showAddress,legacyVivarealId,phones),medias,accountLink,link)),totalCount)),expansion(search(result(listings(listing(displayAddressType,amenities,usableAreas,constructionStatus,listingType,description,title,unitTypes,nonActivationReason,propertyType,unitSubTypes,id,portal,parkingSpaces,address,suites,publicationType,externalId,bathrooms,usageTypes,totalAreas,advertiserId,bedrooms,pricingInfos,showPrice,status,advertiserContact,videoTourLink,whatsappNumber,stamps),account(id,name,logoUrl,licenseNumber,showAddress,legacyVivarealId,phones),medias,accountLink,link)),totalCount)),account(id,name,logoUrl,licenseNumber,showAddress,legacyVivarealId,phones,phones),developments(search(result(listings(listing(displayAddressType,amenities,usableAreas,constructionStatus,listingType,description,title,unitTypes,nonActivationReason,propertyType,unitSubTypes,id,portal,parkingSpaces,address,suites,publicationType,externalId,bathrooms,usageTypes,totalAreas,advertiserId,bedrooms,pricingInfos,showPrice,status,advertiserContact,videoTourLink,whatsappNumber,stamps),account(id,name,logoUrl,licenseNumber,showAddress,legacyVivarealId,phones),medias,accountLink,link)),totalCount)),owners(search(result(listings(listing(displayAddressType,amenities,usableAreas,constructionStatus,listingType,description,title,unitTypes,nonActivationReason,propertyType,unitSubTypes,id,portal,parkingSpaces,address,suites,publicationType,externalId,bathrooms,usageTypes,totalAreas,advertiserId,bedrooms,pricingInfos,showPrice,status,advertiserContact,videoTourLink,whatsappNumber,stamps),account(id,name,logoUrl,licenseNumber,showAddress,legacyVivarealId,phones),medias,accountLink,link)),totalCount))&size=300&from={}&q=&developmentsSize=5&__vt=&levels=CITY,UNIT_TYPE&ref=&pointRadius=&isPOIQuery='''

#%%
print(url)

# %%
headersList = {
 "Accept": "*/*",
 "User-Agent": "Thunder Client (https://www.thunderclient.com)",
 "x-domain": "www.vivareal.com.br" 
}

payload = ""
# %%
def get_json(url, i, headersList, payload):
    ret = requests.request("GET", url.format(i), data=payload,  headers=headersList)
    soup = bs(ret.text, 'html.parser')
    return json.loads(soup.text)

# %%
get_json(url, 1, headersList, payload)
# %%

df = pd.DataFrame(
    columns=[
        'descricao',
        'endereco',
        'area',
        'quartos',
        'suites',
        'wc',
        'vagas',
        'valor',
        'condominio',
        'lat',
        'lon',
        'weblink'
        ]
)

#%%
#Raspando todas as paginas enquanto a quantidade não for igual a quantidade exibida na pagina

i = 0
imovel_id = 0
json_data = get_json(url, imovel_id, headersList, payload)

while len(json_data['search']['result']['listings']) > 0:
    qtd = len(json_data['search']['result']['listings'])
    print(f'Quantidade de Imóveis: {qtd} | total{imovel_id}')
    for i in range(0, qtd):
        try: 
            descricao = json_data['search']['result']['listings'][i]['listing']['description']
        except:
            descricao = '-'
        try: 
            endereco = json_data['search']['result']['listings'][i]['listing']['address']['street']
        except:
            endereco = '-'
        try: 
            area = json_data['search']['result']['listings'][i]['listing']['totalAreas'][0]
        except:
            area = '-'
        try: 
            quartos = json_data['search']['result']['listings'][i]['listing']['bedrooms'][0]
        except:
            quartos = '-'
        try: 
            suites = json_data['search']['result']['listings'][i]['listing']['suites'][0]
        except:
            suites = '-'
        try: 
            wc = json_data['search']['result']['listings'][i]['listing']['bathrooms'][0]
        except:
            wc = '-'       
        try: 
            valor = json_data['search']['result']['listings'][i]['listing']['pricingInfos'][0]['price']
        except:
            valor = '-'        
        try: 
            vagas = json_data['search']['result']['listings'][i]['listing']['parkingSpaces'][0]
        except:
            vagas = '-' 
        try: 
            condominio = json_data['search']['result']['listings'][i]['listing']['pricingInfos'][0]['monthlyCondoFee']
        except:
            condominio = '-'     
        try: 
            lat = str(json_data['search']['result']['listings'][i]['listing']['address']['point']['lat'])
        except:
            lat = '-'  
        try: 
            lon = str(json_data['search']['result']['listings'][i]['listing']['address']['point']['lon'])
        except:
            lon = '-'     
        try: 
            weblink = 'https://www.vivareal.com.br' + json_data['search']['result']['listings'][i]['link']['href']
        except:
            weblink = '-'      

        df.loc[df.shape[0]] = [        
            descricao,
            endereco,
            area,
            quartos,
            suites,
            wc,
            vagas,
            valor,
            condominio,
            lat,
            lon,
            weblink        
        ]                                                              
    
    imovel_id = imovel_id + qtd
    if imovel_id > 10000:
        break
    time.sleep(2)
    json_data = get_json(url, imovel_id, headersList, payload)

#%%
df.to_csv('banco_de_imoveis.csv', sep = ";", index = False, )
# %%
####################
############Estudos sobre json
#####Entendendo o aninhamento
i = 0
ret = requests.request("GET", url.format(i), data=payload,  headers=headersList)
ret.text# %%
soup = bs(ret.text, 'html.parser')
soup.prettify()
soup.text
# %%
json.loads(soup.text)
# %%
json_data = json.loads(soup.text)
# %%
json_data
# %%
type(json_data)
#%%
type(json_data['search']['result']['listings'])
#%%
json_data['search']['result']['listings'][0]['listing']['description']

# %%
json_data['search']['result']['listings'][0]
# %%
len(json_data['search']['result']['listings'])
#%%
i = 0
while i < 5:
    print(json_data['search']['result']['listings'][i]['listing']['description'])
    i += 1
i = 0

#%%
#Exibindo a descrição dos imoveis
i = 0
while i < len(json_data['search']['result']['listings']):
    print(f"Imóvel {i}:\n{json_data['search']['result']['listings'][i]['listing']['description']}")
    i += 1

# %%
#Exibindo o preço dos imoveis já formatados
i = 0
while i < len(json_data['search']['result']['listings']):
    print(f"O valor do imóvel é: R${int(json_data['search']['result']['listings'][i]['listing']['pricingInfos'][0]['price']):n}")
    i += 1

#%%
### Usando o locale para formatar os numeros

import locale
locale.setlocale(locale.LC_ALL, '')
#%%
num = 10000000
print(f"{num:n}")
# %%

json_data['search']['result']['listings'][i]['link']['href']
# %%
json_data['search']['result']['listings'][i]['listing']['totalAreas'][0]
# %%
json_data
# %%
json_data['search']['result']['listings'][0]['listing']['address']['point']['lat']
# %%
type(json_data['search']['result']['listings'][0]['listing']['address']['point']['lon'])
# %%
str(json_data['search']['result']['listings'][0]['listing']['address']['point']['lat'])

#%%


