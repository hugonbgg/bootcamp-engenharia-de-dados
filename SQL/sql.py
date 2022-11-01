#%%
from sqlalchemy import create_engine
import pandas as pd

#%%
#Criando a conexão
engine = create_engine(
    'postgresql+psycopg2://root:root@localhost:54320/test_db'
)
# %%
#salvando a query numa variável
sql = '''
select * from vw_artist;
'''
# %%
sql
# %%
#Transformando em dataframe
df = pd.read_sql_query(sql, engine)
df
# %%
#Query direto no pandas
pd.read_sql_query('select * from vw_song',engine)

#%%
#fazendo inserções
sql = '''insert into tb_artist (
	select t1.artist, 
	t1.song,
	t1."rank", 
	t1."date"
	from "Billboard" as t1
	where artist = 'Nirvana'
	order by t1.artist, t1."date")
;'''

engine.execute(sql)
