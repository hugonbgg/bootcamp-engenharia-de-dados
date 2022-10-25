#%%
import requests
import pandas as pd
from bs4 import BeautifulSoup as bs
import json
import time

# %%
url = '''https://glue-api.vivareal.com/v2/listings?addressCity=Curitiba&addressLocationId=BR%3EParana%3ENULL%3ECuritiba&addressNeighborhood=&addressState=Paran%C3%A1&addressCountry=Brasil&addressStreet=&addressZone=&addressPointLat=-25.437238&addressPointLon=-49.269973&business=SALE&facets=amenities&unitTypes=APARTMENT&unitSubTypes=UnitSubType_NONE,DUPLEX,LOFT,STUDIO,TRIPLEX&unitTypesV3=APARTMENT&usageTypes=RESIDENTIAL&listingType=USED&parentId=null&categoryPage=RESULT&includeFields=search(result(listings(listing(displayAddressType,amenities,usableAreas,constructionStatus,listingType,description,title,unitTypes,nonActivationReason,propertyType,unitSubTypes,id,portal,parkingSpaces,address,suites,publicationType,externalId,bathrooms,usageTypes,totalAreas,advertiserId,bedrooms,pricingInfos,showPrice,status,advertiserContact,videoTourLink,whatsappNumber,stamps),account(id,name,logoUrl,licenseNumber,showAddress,legacyVivarealId,phones),medias,accountLink,link)),totalCount),page,seasonalCampaigns,fullUriFragments,nearby(search(result(listings(listing(displayAddressType,amenities,usableAreas,constructionStatus,listingType,description,title,unitTypes,nonActivationReason,propertyType,unitSubTypes,id,portal,parkingSpaces,address,suites,publicationType,externalId,bathrooms,usageTypes,totalAreas,advertiserId,bedrooms,pricingInfos,showPrice,status,advertiserContact,videoTourLink,whatsappNumber,stamps),account(id,name,logoUrl,licenseNumber,showAddress,legacyVivarealId,phones),medias,accountLink,link)),totalCount)),expansion(search(result(listings(listing(displayAddressType,amenities,usableAreas,constructionStatus,listingType,description,title,unitTypes,nonActivationReason,propertyType,unitSubTypes,id,portal,parkingSpaces,address,suites,publicationType,externalId,bathrooms,usageTypes,totalAreas,advertiserId,bedrooms,pricingInfos,showPrice,status,advertiserContact,videoTourLink,whatsappNumber,stamps),account(id,name,logoUrl,licenseNumber,showAddress,legacyVivarealId,phones),medias,accountLink,link)),totalCount)),account(id,name,logoUrl,licenseNumber,showAddress,legacyVivarealId,phones,phones),developments(search(result(listings(listing(displayAddressType,amenities,usableAreas,constructionStatus,listingType,description,title,unitTypes,nonActivationReason,propertyType,unitSubTypes,id,portal,parkingSpaces,address,suites,publicationType,externalId,bathrooms,usageTypes,totalAreas,advertiserId,bedrooms,pricingInfos,showPrice,status,advertiserContact,videoTourLink,whatsappNumber,stamps),account(id,name,logoUrl,licenseNumber,showAddress,legacyVivarealId,phones),medias,accountLink,link)),totalCount)),owners(search(result(listings(listing(displayAddressType,amenities,usableAreas,constructionStatus,listingType,description,title,unitTypes,nonActivationReason,propertyType,unitSubTypes,id,portal,parkingSpaces,address,suites,publicationType,externalId,bathrooms,usageTypes,totalAreas,advertiserId,bedrooms,pricingInfos,showPrice,status,advertiserContact,videoTourLink,whatsappNumber,stamps),account(id,name,logoUrl,licenseNumber,showAddress,legacyVivarealId,phones),medias,accountLink,link)),totalCount))&size=10&from={}&q=&developmentsSize=5&__vt=&levels=CITY,UNIT_TYPE&ref=&pointRadius=&isPOIQuery='''

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
        'wc',
        'vagas',
        'valor',
        'condominio',
        'weblink'
        ]
)
# %%
####################
i = 1
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
i = 0
while i < len(json_data['search']['result']['listings']):
    print(f"Imóvel {i}:\n{json_data['search']['result']['listings'][i]['listing']['description']}")
    i += 1


# %%
