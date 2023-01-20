 /*8*/select id_game,round(avg(bet),2) from ROUNDS group by id_game;

 /*9*/select id_game,round(avg(bet),2) from ROUNDS  where round_number=1
group by id_game;

/*10*/select id_game,round(avg(bet),2) from ROUNDS  where round_number=(select number_rounds from GAME where round_number=number_rounds)
group by id_game;

 /*2*/select id_game,any_value(id_player),min(bet) from ROUNDS group by id_game;
 /*3*/select id_game,any_value(id_player),max(bet) from ROUNDS group by id_game;

 /*5*/select r.id_player,p.id_game,p.ending_points-p.starting_points from PLAYER_GAME p
inner join PLAYER r on p.id_player=r.id_player
where r.human=0 and (p.ending_points-p.starting_points)=(select max(pg.ending_points-pg.starting_points)
from PLAYER_GAME pg where pg.id_game=p.id_game)
order by id_game;

 /*7*/select id_game,count(distinct id_player)from ROUNDS where bank=TRUE group by id_game;



