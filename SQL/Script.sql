--create billboard table

create table public."Billboard" (
"date" date null,
"rank" int4 null,
song varchar(300) null,
artist varchar(300) null,
"last-week" int4 null,
"peak-rank" int4 null,
"weeks-on-board" int4 null
);

select * from "Billboard" b 

-CTE
--Tabelas distintas
select distinct t1.artist
	,t1.song
from "Billboard" as t1
order by t1.artist
	,t1.song

select t1.artist
	,count(*) as qtd_artist
from "Billboard" as t1
group by t1.artist
order by t1.artist

select t1.song
	,count(*) as qtd_song
from "Billboard" as t1
group by t1.song
order by t1.song

-- Com left join
select distinct t1.artist
	,t2.qtd_artist
	,t1.song
	,t3.qtd_song
from "Billboard" as t1
left join (
	select t1.artist
		,count(*) as qtd_artist
	from "Billboard" as t1
	group by t1.artist
	order by t1.artist
	) as t2 on (t1.artist = t2.artist)
left join (
	select t1.song
		,count(*) as qtd_song
	from "Billboard" as t1
	group by t1.song
	order by t1.song
	) as t3 on (t1.song = t3.song)
order by t1.artist
	,t1.song
	--Criando os CTE 

with cte_artist
as (
	select t1.artist, count(*) as qtd_artist
	from public."Billboard" as t1
	group by t1.artist
	order by t1.artist
	), 	
	cte_song
as (
	select t1.song, count(*) as qtd_song
	from public."Billboard" as t1
	group by t1.song
	order by t1.song
	)
select distinct t1.artist, t2.qtd_artist, t1.song, t3.qtd_song
from "Billboard" as t1
left join cte_artist as t2 on (t1.artist = t2.artist)
left join cte_song as t3 on (t1.song = t3.song)
order by t1.artist, t1.song

----Window function 

with cte_billboard 
as (
	select distinct 
	t1.artist,
	t1.song
from "Billboard" as t1
order by t1.artist, t1.song
)
select *,
row_number () over(order by artist, song) as "row_number",
row_number () over(partition by artist order by artist, song) as "row_number_by_artist"
from cte_billboard;

----
with cte_billboard 
as (
select distinct 
	t1.artist,
	t1.song,
	row_number () over(
	order by artist,
	song) 
	as "row_number",
	row_number () over(partition by artist
order by
	artist,	song) 
	as "row_number_by_artist"
from
	"Billboard" as t1
order by
	t1.artist, t1.song
)
select
	*
from
	cte_billboard
	where "row_number_by_artist" = 1
--------------
	
WITH cte_billboard
AS (
	SELECT DISTINCT t1.artist,
		t1.song
		FROM "Billboard" AS t1
	ORDER BY t1.artist,
		t1.song
	)
select *, 
--row_number() OVER (ORDER BY artist,song) AS "row",
--row_number() OVER (PARTITION BY artist ORDER BY artist,	song) AS "row_by_artist",
rank() over(partition by artist order by artist, song) as "rank",
--lag(song, 1) over(partition by artist order by artist, song) as "lag_song",
--lead(song, 1) over(partition by artist order by artist, song) as "lead_song",
first_value (song) over(partition by artist order by artist, song) as "first_song",
last_value (song) over(partition by artist order by artist, song range between unbounded preceding and unbounded following) as "last_song"
FROM cte_billboard

------------------------
---primeira vez na billboard
with cte_dedupli_artist 
as (
select t1.artist, t1."rank", t1."date",
row_number () over (partition by artist order by artist, date) as "artist_row"
from "Billboard" as t1
order by t1.artist, t1."date")
SELECT * FROM cte_dedupli_artist
WHERE artist_row = 1

---primeira vez na billboard e com qual musica
with cte_dedup_artist 
as (
select t1.artist, t1.song, t1."rank", t1."date",
row_number () over (partition by artist, song order by artist, date) as "artist_row"
from "Billboard" as t1
order by t1.artist, t1."date")
select * from cte_dedup_artist
where artist_row = 1

---Criando tabela com o resultado da query
create table website as (
	with cte_dedupli_artist 
	as (
	select t1.artist, 
	t1.song, 
	t1."rank", 
	t1."date",
	row_number () over (partition by artist, song order by artist, date) as "artist_row"
	from "Billboard" as t1
	order by t1.artist, t1."date")
	select artist, song, "rank", "date" from cte_dedupli_artist
	where artist_row = 1
);

drop table website;
select * from website 

---criando uma tabela intermediaria para os exemplos a frente. Selecionado apenas o AC/DC
create table tb_artist as (
	select t1.artist, 
	t1.song,
	t1."rank", 
	t1."date"
	from "Billboard" as t1
	where artist = 'AC/DC'
	order by t1.artist, t1."date")
;
	
select * from tb_artist;
drop table tb_artist

---criando uma view a partir da tabela criada anteriormente,tb_artist. Substitiu a billboard pela tb_artist, o resto ficou tudo igual.
---View dos artistas selecionados

create view vw_artist as (
	with cte_dedupli_artist as (
		select t1.artist,
			t1."rank",
			t1."date",
			row_number() over (
				partition by artist
				order by artist,
					"date"
				) as "artist_row"
		from tb_artist as t1
		order by t1.artist,
			t1."date"
		) select artist,
	"rank",
	"date"
	from cte_dedupli_artist where artist_row = 1
)
	
-- para dropar: drop view vw_artist; 
drop view vw_artist;
select * from vw_artist;

------Adicionando U2 a tabela tb_artist usando o insert
insert into tb_artist (
	select t1.artist, 
	t1.song,
	t1."rank", 
	t1."date"
	from "Billboard" as t1
	where artist = 'U2'
	order by t1.artist, t1."date")
	
------Adicionando os Elvis a tabela tb_artist usando o insert
insert into tb_artist (
	select t1.artist, 
	t1.song,
	t1."rank", 
	t1."date"
	from "Billboard" as t1
	where artist like 'Elvis%'
	order by t1.artist, t1."date")
	
	select * from tb_artist ta 
	
-----Verificando a view da tabela tb_artist
select * from vw_artist va 

---criando a tabela songs

--- criando uma view dos songs
create view vw_song as (
	with cte_dedupli_artist as (
		select t1.artist,
			t1.song,
			t1."rank",
			t1."date",
			row_number() over (
				partition by artist, song
				order by artist,
				song,
				"date"					
				) as "artist_row"
		from tb_artist as t1
		order by t1.artist,t1."date", 
		t1.song			
		) select artist,
				song,
				"rank",
				"date"
	from cte_dedupli_artist where artist_row = 1
)

drop view vw_song;
select * from vw_song vs 

---Fazendo novo insert na tabela base tb_artist
insert into tb_artist (
	select t1.artist, 
	t1.song,
	t1."rank", 
	t1."date"
	from "Billboard" as t1
	where artist like 'Adele%'
	order by t1.artist, t1."date")
	
	select * from tb_artist

select * from vw_song;
select * from vw_artist va 

---Alterando a view, retirando os artistas
drop view vw_song;

create view vw_song as (
	with cte_dedupli_artist as (
		select 
			t1.song,
			t1."rank",
			t1."date",
			row_number() over (
				partition by song
				order by 
				song,
				"date"					
				) as "artist_row"
		from tb_artist as t1
		order by t1.song,	
		t1."date"
		) select 
				song,
				"rank",
				"date"
	from cte_dedupli_artist 
	where artist_row = 1
)

select * from vw_song; 