--create table

create table "Billboard" (
"date" date null,
"rank" int4 null,
song varchar(300) null,
artist varchar(300) null,
"last-week" int4 null,
"peak-rank" int4 null,
"weeks-on-board" int4 null
);

--import csv
COPY "Billboard"
FROM '/home/charts.csv'
DELIMITER ','
CSV HEADER
;

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

---criando uma view a partir da tabela criada anteriormente,tb_artist.
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
);

------Adicionando U2 a tabela tb_artist usando o insert
insert into tb_artist (
	select t1.artist, 
	t1.song,
	t1."rank", 
	t1."date"
	from "Billboard" as t1
	where artist = 'U2'
	order by t1.artist, t1."date")
;
	
------Adicionando os Elvis a tabela tb_artist usando o insert
insert into tb_artist (
	select t1.artist, 
	t1.song,
	t1."rank", 
	t1."date"
	from "Billboard" as t1
	where artist like 'Elvis%'
	order by t1.artist, t1."date")
;
	
--- criando uma view dos songs
create view vw_song as (
	with cte_dedupli_artist as (
		select t1.song,
			t1."rank",
			t1."date",
			row_number() over (
				partition by song
				order by 
				song,
				"date"					
				) as "artist_row"
		from tb_artist as t1
		order by t1.artist,t1."date", 
		t1.song			
		) select 
				song,
				"rank",
				"date"
	from cte_dedupli_artist where artist_row = 1
);

---Fazendo novo insert (Adele) na tabela base tb_artist
insert into tb_artist (
	select t1.artist, 
	t1.song,
	t1."rank", 
	t1."date"
	from "Billboard" as t1
	where artist like 'Adele%'
	order by t1.artist, t1."date")
;