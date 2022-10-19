from importlib.machinery import DEBUG_BYTECODE_SUFFIXES
import pandas as pd
import requests
import collections
import sys

#comentei para add o link direto ao executar o script ficando:

##python loteria.py link da url da caixa

#modalidade = 'Lotofacil'
#url = 'https://servicebus2.caixa.gov.br/portaldeloterias/api/resultados?modalidade='+ modalidade
#print(url)

url = sys.argv[1]

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
df = df[df['Bola1'] == df['Bola1']] #para remover os nulos, que são as linhas em branco dos dados originais

####Análise de dados
#Cria a lista da população, pares, impares e primos

np_pop = list(range(1, 26))
n_pares = list(range(2,25,2))
n_impares = list(range(1,26,2))
nr_primos = [2, 3, 5, 7, 11, 13, 17, 19, 23]

n_pares
n_impares
nr_primos

comb = [] #Combinação de pares e impares

#Criando as variáveis
v_01 = 0
v_02 = 0
v_03 = 0
v_04 = 0
v_05 = 0
v_06 = 0
v_07 = 0
v_08 = 0
v_09 = 0
v_10 = 0
v_11 = 0
v_12 = 0
v_13 = 0
v_14 = 0
v_15 = 0
v_16 = 0
v_17 = 0
v_18 = 0
v_19 = 0
v_20 = 0
v_21 = 0
v_22 = 0
v_23 = 0
v_24 = 0
v_25 = 0

#Definindo quais colunas(variáveis) irá interar no df
lst_campos = ['Bola1', 'Bola2', 'Bola3', 'Bola4', 'Bola5', 'Bola6', 'Bola7', 'Bola8', 'Bola9', 'Bola10', 'Bola11', 'Bola12', 'Bola13', 'Bola14', 'Bola15']

#Criando o for que irá salvar a quantidade de vezes que cada números saiu nos resultados

for index, row in df.iterrows():
    v_pares = 0
    v_impares = 0
    v_primos = 0
    for campo in lst_campos:
        if row[campo] in n_pares:
            v_pares += 1
        if row[campo] in n_impares:
            v_impares += 1
        if row[campo] in nr_primos:
            v_primos += 1
        if row[campo] == 1:
                v_01 += 1
        if row[campo] == 2:
                v_02 += 1
        if row[campo] == 3:
                v_03 += 1
        if row[campo] == 4:
                v_04 += 1
        if row[campo] == 5:
                v_05 += 1
        if row[campo] == 6:
                v_06 += 1
        if row[campo] == 7:
                v_07 += 1
        if row[campo] == 8:
                v_08 += 1
        if row[campo] == 9:
                v_09 += 1
        if row[campo] == 10:
                v_10 += 1
        if row[campo] == 11:
                v_11 += 1
        if row[campo] == 12:
                v_12 += 1
        if row[campo] == 13:
                v_13 += 1
        if row[campo] == 14:
                v_14 += 1
        if row[campo] == 15:
                v_15 += 1
        if row[campo] == 16:
                v_16 += 1
        if row[campo] == 17:
                v_17 += 1
        if row[campo] == 18:
                v_18 += 1
        if row[campo] == 19:
                v_19 += 1
        if row[campo] == 20:
                v_20 += 1
        if row[campo] == 21:
                v_21 += 1
        if row[campo] == 22:
                v_22 += 1
        if row[campo] == 23:
                v_23 += 1
        if row[campo] == 24:
                v_24 += 1
        if row[campo] == 25:
                v_25 += 1
    comb.append(str(v_pares) + 'p-' + str(v_impares) + 'i-'+ str (v_primos)+ 'np')

#Criando uma lista com os resultados

freq_nr = [
    [1, v_01],
    [2, v_02],
    [3, v_03],
    [4, v_04],
    [5, v_05],
    [6, v_06],
    [7, v_07],
    [8, v_08],
    [9, v_09],
    [10, v_10],
    [11, v_11],
    [12, v_12],
    [13, v_13],
    [14, v_14],
    [15, v_15],
    [16, v_16],
    [17, v_17],
    [18, v_18],
    [19, v_19],
    [20, v_20],
    [21, v_21],
    [22, v_22],
    [23, v_23],
    [24, v_24],
    [25, v_25]
]

#Organizando os valores do menos frequente para o mais
freq_nr.sort(key=lambda tup: tup[1])
freq_nr
freq_nr[0] # menos frequente
freq_nr[-1] #mais frequente

#Contando as combinações
counter = collections.Counter(comb)
counter

#Salvando os resultados da contagem em um dataframe
resultado = pd.DataFrame(counter.items(), columns=['Combinacao', 'Frequencia'])
resultado

resultado['pct_freq'] = resultado['Frequencia']/resultado['Frequencia'].sum() #calcula a porcetagem
resultado['pct_freq'] = resultado['pct_freq'] * 100 #converte por 100 para deixar de 0 a 100%
resultado['pct_freq'] = resultado['pct_freq'].round(2) #deixa apenas duas casas decimais
resultado = resultado.sort_values(by = 'pct_freq', ascending= False) #Organiza do mais frequente para o menos frequente
resultado

#Exibindo o resultado formatado
print('''
        O número mais frequente é o: {}
        O número menos frequente é o: {}
        A combinação de pares, impares e primos mais frequente é: {} com a frequencia de {}%
        '''.format(freq_nr[-1][0], freq_nr[0][0], resultado['Combinacao'].values[0], resultado['pct_freq'].values[0])
        )

