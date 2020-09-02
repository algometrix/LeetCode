create table movies(id integer,title varchar(40));
create table movie_ratings(movie_id integer,user_id integer, rating integer, created_at timestamp);
create table users(id integer,name varchar(40));

insert into movies values (1, 'Avengers Endgame');
insert into movies values (2, 'Alladin');
insert into movies values (3, 'Aquaman');

insert into movie_ratings values(1,1,3,now());
insert into movie_ratings values(1,2,4,now());
insert into movie_ratings values(1,3,5,now());
insert into movie_ratings values(1,4,4,now());
insert into movie_ratings values(2,1,1,now());
insert into movie_ratings values(2,2,3,now());
insert into movie_ratings values(2,3,3,now());
insert into movie_ratings values(2,4,3,now());
insert into movie_ratings values(3,1,1,now());
insert into movie_ratings values(3,2,2,now());
insert into movie_ratings values(3,3,3,now());
insert into movie_ratings values(3,4,5,now());

insert into users values(1, 'Ben');
insert into users values(2, 'Nicole');
insert into users values(3, 'James');


select title from (select mr.movie_id, ms.title, mr.rating from movie_ratings mr, movies ms where mr.movie_id = ms.id and mr.created_at < now() group by mr.movie_id order by avg(mr.rating) desc) B limit 1;

select title from movies where id in (select movie_id from movie_ratings where created_at < now() group by movie_id order by avg(rating)) limit 1;

select movie_id, avg(rating) from movie_ratings where created_at < now() group by movie_id order by avg(rating) desc;

select movie_id, avg(rating) from movie_ratings where created_at < '2020-09-01' group by movie_id order by avg(rating) desc limit 1;

select title from (select mr.movie_id, ms.title, mr.rating from movie_ratings mr, movies ms where mr.movie_id = ms.id and mr.created_at < now() group by mr.movie_id order by avg(mr.rating) desc) B limit 1;