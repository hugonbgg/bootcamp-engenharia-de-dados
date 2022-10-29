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














