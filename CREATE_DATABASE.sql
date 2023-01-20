drop database if exists EMA;
create database EMA character set utf8;
use EMA;

create table if not exists PLAYER(
id_player varchar(45),
name varchar(45),
player_risk int,
human boolean);


create table if not exists GAME(
id_game int,
id_deck char(3),
number_rounds int,
players int,
start_hour datetime,
end_hour datetime);

create table if not exists DECK(
id_deck char(3),
name_deck varchar(45));

create table if not exists CARD(
id_card char(3),
id_deck char(3),
card_name varchar(45),
card_value int,
card_priority int,
card_real_value dec(3,1));

create table if not exists ROUNDS(
round_number int,
id_game int,
id_player varchar(45),
bet int,
bank boolean,
cards_value decimal(4,1),
starting_round_points int,
ending_round_points int);

create table if not exists PLAYER_GAME(
id_game int,
id_player varchar(45),
initial_card varchar(10),
starting_points int,
ending_points int);


    
    






