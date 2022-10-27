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

select * from "Billboard" limit 100;
select count (*) as quantidade from "Billboard";
select artist, song, "weeks-on-board"  from "Billboard" b where "weeks-on-board" > 50;


SELECT t1."date"
	,t1."rank"
	,t1.song
	,t1.artist
	,t1."last-week"
	,t1."peak-rank"
	,t1."weeks-on-board"
FROM "Billboard" AS t1

	

SELECT t1.song
	,t1.artist
FROM "Billboard" AS t1
where t1.artist = 'Chuck Berry'


select distinct t1.artist
	, t1.song
	, count(*) as "#song"
from "Billboard" as t1
where t1.artist = 'Chuck Berry'
group by t1.artist, t1.song 
order by "#song" desc
	
select distinct t1.artist
	, t1.song
	, count(*) as "#song"
from "Billboard" as t1
-- where t1.artist = 'Chuck Berry' or t1.artist = 'Frankie Vaughan'
where t1.artist in ('Chuck Berry', 'Frankie Vaughan')
group by t1.artist, t1.song 
order by "#song" desc

--CTE
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