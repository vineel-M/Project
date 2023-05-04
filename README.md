# Airport-Management-GUI
I am facing problem creating a gui for airport management system, i am not able to link the two tables : CREATE TABLE Airports
(
  flight_number VARCHAR2(10) PRIMARY KEY,
  flight_name VARCHAR2(50),
  gate_number VARCHAR2(50),
  terminal_number VARCHAR2(50)
);

CREATE TABLE FlightPassengers
(
  passenger_id NUMBER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
  passenger_name VARCHAR2(50),
  seat_number VARCHAR2(10),
  flight_number VARCHAR2(10),
  FOREIGN KEY (flight_number) REFERENCES Airports(flight_number)
);
also if anyone can suggest changes to the layout of the gui as well it is much appreciated
