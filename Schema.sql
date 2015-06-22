CREATE TABLE Person
(SSN CHAR(5) NOT NULL,
age INTEGER,
gender VARCHAR(20),
firstName VARCHAR(20),
lastName VARCHAR(20),
GId CHAR(5)
);

CREATE TABLE Company
(cName VARCHAR(20) NOT NULL,
cAdress VARCHAR(20),
GId CHAR(5)
);

CREATE TABLE Guest
(GId CHAR(5) NOT NULL,
guestType VARCHAR(20),
VId CHAR(5)
);

CREATE TABLE VIP
(VId CHAR(5) NOT NULL,
status VARCHAR(20)
);

CREATE TABLE Gym
(FacilityId CHAR(5) NOT NULL,
type VARCHAR(20)
);

CREATE TABLE ChessRoom
(FacilityId CHAR(5) NOT NULL,
size VARCHAR(20) 
);

CREATE TABLE Facility
(FacilityId CHAR(5) NOT NULL,
ServiceId CHAR(5) NOT NULL,
duration VARCHAR(20) 
);

CREATE TABLE Food
(FoodId CHAR(5) NOT NULL,
ServiceId CHAR(5) NOT NULL,
deliveredTime VARCHAR(20) 
);

CREATE TABLE Service
(ServiceId CHAR(5) NOT NULL,
cost INTEGER,
RoomId CHAR(5)
);

CREATE TABLE Room
(RoomId CHAR(5) NOT NULL,
available BOOLEAN,
price INTEGER,
BigFlag BOOLEAN,
DoubleFlag BOOLEAN,
SingleFlag BOOLEAN
);

CREATE TABLE Administrator
(UserId CHAR(5),
password VARCHAR(20)
);

CREATE TABLE Employee
(UserId CHAR(5),
password VARCHAR(20)
);

CREATE TABLE Bill
(ResId CHAR(5) NOT NULL,
total INTEGER
);

CREATE TABLE Contact
(GId CHAR(5),
telNo VARCHAR(20)
);

CREATE TABLE Reserve
(EmpId CHAR(5),
GId CHAR(5),
RoomId CHAR(5),
ResId CHAR(5) NOT NULL,
startDate DATE,
endDate DATE
);

ALTER TABLE Person
ADD PRIMARY KEY(SSN);


ALTER TABLE Company
ADD PRIMARY KEY(cName);

ALTER TABLE Guest
ADD PRIMARY KEY(GId);

ALTER TABLE VIP
ADD PRIMARY KEY(VId);

ALTER TABLE Gym
ADD PRIMARY KEY(FacilityId);

ALTER TABLE ChessRoom
ADD PRIMARY KEY(FacilityId);

ALTER TABLE Facility
ADD PRIMARY KEY(FacilityId, ServiceId);

ALTER TABLE Food
ADD PRIMARY KEY(FoodId, ServiceId);

ALTER TABLE Service
ADD PRIMARY KEY(ServiceId);

ALTER TABLE Room
ADD PRIMARY KEY(RoomId);

ALTER TABLE Administrator
ADD PRIMARY KEY(UserId);

ALTER TABLE Employee
ADD PRIMARY KEY(UserId);

ALTER TABLE Bill
ADD PRIMARY KEY(ResId);

ALTER TABLE Contact
ADD PRIMARY KEY(GId, telNo)
ADD FOREIGN KEY(GId) REFERENCES Guest(GId)
ON DELETE SET NULL ON UPDATE CASCADE;

ALTER TABLE Reserve
ADD PRIMARY KEY(ResId);

ALTER TABLE Person
ADD FOREIGN KEY(GId) REFERENCES Guest(GId)
ON DELETE SET NULL ON UPDATE CASCADE;

ALTER TABLE Company
ADD FOREIGN KEY(GId) REFERENCES Guest(GId)
ON DELETE SET NULL ON UPDATE CASCADE;

ALTER TABLE Service
ADD FOREIGN KEY(RoomId) REFERENCES Room(RoomId)
ON DELETE SET NULL ON UPDATE CASCADE;


ALTER TABLE Reserve
ADD FOREIGN KEY(EmpId) REFERENCES Employee(UserId)
ON DELETE CASCADE ON UPDATE CASCADE,
ADD FOREIGN KEY(GId) REFERENCES Guest(GId)
ON DELETE CASCADE ON UPDATE CASCADE,
ADD FOREIGN KEY(RoomId) REFERENCES Room (RoomId)
ON DELETE CASCADE ON UPDATE CASCADE;

ALTER TABLE Contact
ADD FOREIGN KEY(GId) REFERENCES Guest(GId)
ON DELETE CASCADE ON UPDATE CASCADE;

ALTER TABLE Gym
ADD FOREIGN KEY(FacilityId) REFERENCES Facility(FacilityId)
ON DELETE CASCADE ON UPDATE CASCADE;

ALTER TABLE ChessRoom
ADD FOREIGN KEY(FacilityId) REFERENCES Facility(FacilityId)
ON DELETE CASCADE ON UPDATE CASCADE;

ALTER TABLE Facility
ADD FOREIGN KEY(ServiceId) REFERENCES Service(ServiceId)
ON DELETE CASCADE ON UPDATE CASCADE;

ALTER TABLE Food
ADD FOREIGN KEY(ServiceId) REFERENCES Service(ServiceId)
ON DELETE CASCADE ON UPDATE CASCADE;

ALTER TABLE Bill
ADD FOREIGN KEY(ResId) REFERENCES Reserve(ResId) 
ON DELETE CASCADE ON UPDATE CASCADE;


CREATE TABLE Global (
	UserId INTEGER,
    RoomId INTEGER,
    GId INTEGER,
    ResId INTEGER
);

INSERT INTO Global values(0, 0, 0, 0);

