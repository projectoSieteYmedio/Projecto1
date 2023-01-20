insert into CARD values ('O01','ESP','As de oros',1,4,1);
insert into CARD values ('O02','ESP','Dos de oros',2,4,2);
insert into CARD values ('O03','ESP','Tres de oros',3,4,3);
insert into CARD values ('O04','ESP','Cuatro de oros',4,4,4);
insert into CARD values ('O05','ESP','Cinco de oros',5,4,5);
insert into CARD values ('O06','ESP','Seis de oros',6,4,6);
insert into CARD values ('O07','ESP','Siete de oros',7,4,7);
insert into CARD values ('O10','ESP','Sota de oros',8,4,0.5);
insert into CARD values ('O11','ESP','Caballo de oros',9,4,0.5);
insert into CARD values ('O12','ESP','Rey de oros',10,4,0.5);
/*---------------------------------------------------------------*/
insert into CARD values ('C01','ESP','As de copas',1,3,1);
insert into CARD values ('C02','ESP','Dos de copas',2,3,2);
insert into CARD values ('C03','ESP','Tres de copas',3,3,3);
insert into CARD values ('C04','ESP','Cuatro de copas',4,3,4);
insert into CARD values ('C05','ESP','Cinco de copas',5,3,5);
insert into CARD values ('C06','ESP','Seis de copas',6,3,6);
insert into CARD values ('C07','ESP','Siete de copas',7,3,7);
insert into CARD values ('C10','ESP','Sota de copas',8,3,0.5);
insert into CARD values ('C11','ESP','Caballo de copas',9,3,0.5);
insert into CARD values ('C12','ESP','Rey de copas',10,3,0.5);
/*-------------------------------------------*/
insert into CARD values ('E01','ESP','As de espadas',1,2,1);
insert into CARD values ('E02','ESP','Dos de espadas',2,2,2);
insert into CARD values ('E03','ESP','Tres de espadas',3,2,3);
insert into CARD values ('E04','ESP','Cuatro de espadas',4,2,4);
insert into CARD values ('E05','ESP','Cinco de espadas',5,2,5);
insert into CARD values ('E06','ESP','Seis de espadas',6,2,6);
insert into CARD values ('E07','ESP','Siete de espadas',7,2,7);
insert into CARD values ('E10','ESP','Sota de espadas',8,2,0.5);
insert into CARD values ('E11','ESP','Caballo de espadas',9,2,0.5);
insert into CARD values ('E12','ESP','Rey de espadas',10,2,0.5);
/*-----------------------------------------------*/
insert into CARD values ('B01','ESP','As de bastos',1,1,1);
insert into CARD values ('B02','ESP','Dos de bastos',2,1,2);
insert into CARD values ('B03','ESP','Tres de bastos',3,1,3);
insert into CARD values ('B04','ESP','Cuatro de bastos',4,1,4);
insert into CARD values ('B05','ESP','Cinco de bastos',5,1,5);
insert into CARD values ('B06','ESP','Seis de bastos',6,1,6);
insert into CARD values ('B07','ESP','Siete de bastos',7,1,7);
insert into CARD values ('B10','ESP','Sota de bastos',8,1,0.5);
insert into CARD values ('B11','ESP','Caballo de bastos',9,1,0.5);
insert into CARD values ('B12','ESP','Rey de bastos',10,1,0.5);
/*-----------------------------------------------*/
insert into PLAYER values ('48073176W','Alex',50,1);
insert into PLAYER values ('12345677Q','Marc',40,0);
insert into PLAYER values ('12345676A','Marc',30,0);
select * from PLAYER;
delete from PLAYER;
/*-----------------------------------------------*/
insert into PLAYER_GAME values (2,'48073176W','E01',20,85);
insert into PLAYER_GAME values (2,'12345677Q','O01',20,30);
insert into PLAYER_GAME values (2,'12345676A','E11',20,250);
select * from PLAYER_GAME;
delete FROM PLAYER_GAME;
use EMA;
/*-----------------------------------------------*/
select * from ROUNDS;
select * from GAME;
delete FROM ROUNDS;
insert into ROUNDS values (1,1,'48073176W',10,TRUE,2,20,25); 
insert into ROUNDS values (1,1,'12345677Q',5,FALSE,2,20,25);
insert into ROUNDS values (2,1,'48073176W',20,TRUE,2,20,25);
insert into ROUNDS values (2,1,'12345677Q',24,FALSE,2,20,25);
insert into ROUNDS values (3,1,'48073176W',31,TRUE,2,20,25);
insert into ROUNDS values (3,1,'12345677Q',10,FALSE,2,20,25);

insert into ROUNDS values (1,2,'48073176W',50,TRUE,2,20,25);
insert into ROUNDS values (1,2,'12345677Q',20,FALSE,2,20,25);
insert into ROUNDS values (1,2,'12345676A',10,FALSE,2,20,25); 
insert into ROUNDS values (2,2,'12345677Q',30,TRUE,2,20,25);
insert into ROUNDS values (2,2,'48073176W',20,FALSE,2,20,25);
insert into ROUNDS values (2,2,'12345676A',15,FALSE,2,20,25);
insert into ROUNDS values (3,2,'12345677Q',15,TRUE,2,20,25);
insert into ROUNDS values (3,2,'48073176W',9,FALSE,2,20,25);
insert into ROUNDS values (3,2,'12345676A',15,FALSE,2,20,25);
insert into ROUNDS values (4,2,'12345677Q',15,TRUE,2,20,25);
insert into ROUNDS values (4,2,'48073176W',7,FALSE,2,20,25);
insert into ROUNDS values (4,2,'12345676A',15,FALSE,2,20,25);