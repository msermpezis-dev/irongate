CREATE TABLE UserData(
	user_id INT IDENTITY(0,1) NOT NULL,
    email varchar(50) NOT NULL UNIQUE,
	salt varchar(44) NOT NULL,
	iv varchar(24) NOT NULL,
	mcvalue varchar(24) NOT NULL,
	cvalue varchar(24) NOT NULL,
	emk varchar(64) NOT NULL,
    CONSTRAINT PK_userdata PRIMARY KEY (user_id));
	
CREATE TABLE Entity(
	entity_id	INT IDENTITY(0,1) NOT NULL,
	entity_name varchar(50) NOT NULL,
	entity_un	varchar(44) NOT NULL,
	entity_pw	varchar(44) NOT NULL,
	note TEXT,
   CONSTRAINT PK_entity PRIMARY KEY (entity_id));
   
CREATE TABLE User_Entity(
	user_id INT NOT NULL,
	entity_id INT NOT NULL,
	CONSTRAINT PK_user_entity PRIMARY KEY (user_id, entity_id));



ALTER TABLE User_Entity
ADD CONSTRAINT FK_userdata FOREIGN KEY (user_id) REFERENCES UserData(user_id);

ALTER TABLE User_Entity
ADD CONSTRAINT FK_entity FOREIGN KEY (entity_id) REFERENCES Entity(entity_id);