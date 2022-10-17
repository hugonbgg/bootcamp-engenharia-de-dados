from importlib.machinery import DEBUG_BYTECODE_SUFFIXES
import pandas as pd
import requests

modalidade = 'Lotofacil'
url = 'https://servicebus2.caixa.gov.br/portaldeloterias/api/resultados?modalidade='+ modalidade
print(url)

r = requests.get(url, verify = False)
r.text
r_text = r.text

r_text = r_text.replace('\\n','').replace('\\r','') #remove os finais das linhas, os enters e os espaços
r_text = r_text.replace('"\r\n}','') #remove os ultimos caracteres da tabela que não foram removidos anteriormente
r_text = r_text.replace('{\r\n  "html": "','') #limpa as primeiras linhas da tabela
r_text[:100]
r_text

df = pd.read_html(r_text)
type(df)
type(df[0])
df = df[0].copy()
df
df[df['Bola1'] == df['Bola1']]