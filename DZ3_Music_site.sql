create table if not exists Songwriter (
	id serial primary key, 
	name varchar(100) not null unique
);

create table if not exists Alias_Songwriter (
	id serial primary key,
	alias varchar(100) not null,
	id_sa integer references songwriter(id)
);

create table if not exists Genre (
	id serial primary key,
	genre_name varchar(100) not null
);

create table if not exists SW_Genres (
	id serial primary key,
	id_sw integer not null references Songwriter(id),
	id_genre integer not null references Genre(id)
);

create table if not exists Songwriters_Albums (
	id serial primary key,
	name_album varchar(100) not null,
	released integer
);

create table if not exists Joint_Album (
	id serial primary key,
	id_sw integer not null references Songwriter(id),
	id_album integer not null references Songwriters_Albums(id)
);

create table if not exists Tracks (
	id serial primary key,
	id_album integer references Songwriters_Albums(id),
	track_name varchar(100),
	duration integer
		
);

create table if not exists Collection (
	id serial primary key,
	name_collection varchar(100) not null,
	released_collection integer
);

create table if not exists TC_SA (
	id serial primary key,
	tracks_id integer not null references Tracks(id),
	collection_id integer not null references Collection(id)
);