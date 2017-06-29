DROP TABLE IF EXISTS aircrafts;

CREATE TABLE aircrafts (
    hex varchar(6) not null,
    flight varchar(7),
    timestamp TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (hex,flight),
    UNIQUE(hex,flight)
    
);
