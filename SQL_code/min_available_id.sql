-- Active: 1713270980889@@127.0.0.1@3306@db_finallab

DROP FUNCTION IF EXISTS min_available_id;
DELIMITER //

CREATE FUNCTION min_available_id(TABLE_NAME CHAR(1))
RETURNS CHAR(8)
DETERMINISTIC
READS SQL DATA
BEGIN
    DECLARE min_id CHAR(8);
    DECLARE i INT DEFAULT 1;

    IF TABLE_NAME = 'S' THEN
        WHILE i <= 1000 DO
            SET min_id = CONCAT('S', LPAD(i, 4, '0'));
            IF NOT EXISTS (SELECT * FROM student WHERE student_id = min_id) THEN
                RETURN min_id;
            END IF;
            SET i = i + 1;
        END WHILE;
    ELSEIF TABLE_NAME = 'T' THEN
        WHILE i <= 1000 DO
            SET min_id = CONCAT('T', LPAD(i, 4, '0'));
            IF NOT EXISTS (SELECT * FROM teacher WHERE teacher_id = min_id) THEN
                RETURN min_id;
            END IF;
            SET i = i + 1;
        END WHILE;
    ELSEIF TABLE_NAME = 'C' THEN
        WHILE i <= 1000 DO
            SET min_id = CONCAT('C', LPAD(i, 4, '0'));
            IF NOT EXISTS (SELECT * FROM company WHERE company_id = min_id) THEN
                RETURN min_id;
            END IF;
            SET i = i + 1;
        END WHILE;
    ELSEIF TABLE_NAME = 'P' THEN
        WHILE i <= 1000 DO
            SET min_id = CONCAT('P', LPAD(i, 4, '0'));
            IF NOT EXISTS (SELECT * FROM project WHERE project_id = min_id) THEN
                RETURN min_id;
            END IF;
            SET i = i + 1;
        END WHILE; 
    ELSE
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Invalid table name.';
    END IF;

    RETURN NULL;
END //

DELIMITER ;
