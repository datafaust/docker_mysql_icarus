
-- inserts data from staging to production
DROP PROCEDURE IF EXISTS icarus.insertPrdData;
DELIMITER $$
CREATE PROCEDURE icarus.insertPrdData()
	
    BEGIN
    -- Declare variables to hold diagnostics area information
    -- DECLARE errorCode CHAR(5) DEFAULT '00000';
    -- DECLARE errorMessage TEXT DEFAULT '';

    -- Declare exception handler for failed insert
    -- DECLARE CONTINUE HANDLER FOR SQLEXCEPTION 
    
    
INSERT IGNORE INTO flights_prd
SELECT
CONCAT(icao24,REPLACE(REPLACE(REPLACE(time_stamp,'-',''),' ',''),':','')) AS unique_id,
icao24,               
callsign,            
last_position,               
CAST(time_stamp AS DATETIME) as time_stamp,          
CAST(longitude AS FLOAT) as longitude,            
CAST(latitude AS FLOAT) as latitude,                     
CAST(altitude AS FLOAT) as altitude,
IF(onground='1', TRUE, FALSE) as onground,                          
CAST(groundspeed as FLOAT) AS groundspeed,                    
CAST(track AS FLOAT) AS track,                         
CAST(vertical_rate AS FLOAT) AS vertical_rate,                  
CAST(geoaltitude AS FLOAT) AS geoaltitude,                 
CONVERT(squawk, UNSIGNED INTEGER) AS squawk,                       
CONVERT(position_source, UNSIGNED INTEGER) AS position_source 
FROM
flights_stg;
-- Check whether the insert was successful
    -- IF errorCode != '00000' THEN
     --   INSERT INTO `errors` (code, message, query_type, record_id, on_db, on_table) VALUES (errorCode, errorMessage, 'insert', NEW.id, 'test_db2', 'users');
    -- END IF;
	END$$
DELIMITER ;


-- deletes data from staging
DROP PROCEDURE IF EXISTS icarus.deleteStgData;
DELIMITER $$
CREATE PROCEDURE deleteStgData()
BEGIN
	DELETE FROM flights_stg;
END$$
DELIMITER ;

-- CALL deleteStgData();
-- CALL insertPrdData();
-- SELECT COUNT(*) from flights_prd;
-- SELECT * from errors;