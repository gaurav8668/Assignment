use world;
show tables;
drop table project;
drop table auth_key;

create table project(
id varchar(36),
username varchar(50),
email varchar(50),
pas varchar(50)
);

create table auth_key(
akey varchar(36),
uid varchar(36)
);

select * from auth_key;
select * from project;