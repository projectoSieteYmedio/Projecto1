alter table PLAYER modify id_player varchar(45) primary key not null unique;

alter table PLAYER modify name varchar(45) not null;

alter table PLAYER modify player_risk int;

alter table PLAYER modify human boolean;

alter table GAME modify players int;

alter table GAME modify id_game int primary key auto_increment not null unique;

alter table GAME modify number_rounds int;

alter table GAME modify start_hour datetime;

alter table GAME modify end_hour datetime;

alter table GAME modify id_deck char(3) not null;

alter table DECK modify id_deck char(3) primary key not null unique;

alter table DECK modify name_deck varchar(45) not null unique;

alter table CARD modify id_card char(3) not null unique;

alter table CARD modify card_name varchar(45) not null unique;

alter table CARD modify card_value int;

alter table CARD modify card_priority int;

alter table CARD modify card_real_value decimal(3,1);

alter table ROUNDS modify round_number int not null;

alter table ROUNDS modify bank boolean;

alter table ROUNDS modify bet tinyint;

alter table ROUNDS modify cards_value decimal(4,1);

alter table ROUNDS modify starting_round_points int;

alter table ROUNDS modify ending_round_points int;

alter table ROUNDS modify id_player varchar(45) not null;

alter table PLAYER_GAME modify id_game int not null;

alter table PLAYER_GAME modify id_player varchar(45) not null;

alter table PLAYER_GAME modify initial_card char(3);

alter table PLAYER_GAME add constraint PK_PLAYER_GAME primary key (id_game,id_player);

alter table ROUNDS add constraint PK_ROUNDS primary key (id_game,round_number,id_player);

alter table CARD add constraint PK_CARD primary key (id_card,id_deck);

alter table GAME add constraint FK_DECK_GAME
foreign key(id_deck)
	references DECK(id_deck);
    
alter table CARD add constraint FK_PK_DECK_CARD
foreign key(id_deck)
	references DECK(id_deck);
    
alter table PLAYER_GAME add constraint FK_PK_PLAYER_PLAYER_GAME
foreign key(id_player)
	references PLAYER(id_player);
    
alter table PLAYER_GAME add constraint FK_PK_GAME_PLAYER_GAME
foreign key(id_game)
	references GAME(id_game);

alter table ROUNDS add constraint FK_PK_PLAYER_GAME_ROUNDS
foreign key(id_game,id_player)
	references PLAYER_GAME(id_game,id_player);
    
alter table PLAYER_GAME add constraint FK_CARD_PLAYER_GAME
foreign key(initial_card)
	references CARD(id_card);


