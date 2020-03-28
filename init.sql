CREATE DATABASE icarus;
USE icarus;
SET SQL_SAFE_UPDATES = 0;
CREATE TABLE flights_stg(
     icao24 VARCHAR(100),               
     callsign VARCHAR(100),            
     last_position VARCHAR(100),               
     time_stamp VARCHAR(100),          
     longitude VARCHAR(100),            
     latitude VARCHAR(100),                     
     altitude VARCHAR(100),                     
     onground VARCHAR(100),                          
     groundspeed VARCHAR(100),                    
     track VARCHAR(100),                         
     vertical_rate VARCHAR(100),                  
     geoaltitude VARCHAR(100),                 
     squawk VARCHAR(100),                       
     position_source VARCHAR(100)                
     );

CREATE TABLE flights_prd(
     unique_id VARCHAR(100) PRIMARY KEY,
     icao24 VARCHAR(100),               
     callsign VARCHAR(100),            
     last_position VARCHAR(100),               
     time_stamp DATETIME,          
     longitude FLOAT,            
     latitude FLOAT,                     
     altitude FLOAT,                     
     onground BOOLEAN,                          
     groundspeed FLOAT,                    
     track FLOAT,                         
     vertical_rate FLOAT,                  
     geoaltitude FLOAT,                 
     squawk INT,                       
     position_source INT  
     );

CREATE TABLE IF NOT EXISTS errors (
  id int(11) AUTO_INCREMENT NOT NULL,
  code varchar(30) NOT NULL,
  message TEXT NOT NULL,
  query_type varchar(50) NOT NULL,
  record_id int(11) NOT NULL,
  on_db varchar(50) NOT NULL,
  on_table varchar(50) NOT NULL,
  emailed TINYINT DEFAULT 0,
  created_at timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (id)
);