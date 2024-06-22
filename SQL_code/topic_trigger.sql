-- Active: 1713270980889@@127.0.0.1@3306@db_finallab
-- Active: 1713270980889@@127.0.0.1@3306@db_finallab
DROP TRIGGER IF EXISTS topic_trigger_insert;
DROP TRIGGER IF EXISTS topic_trigger_delete;
DELIMITER //
CREATE TRIGGER topic_trigger_insert AFTER INSERT ON topic FOR EACH ROW
BEGIN
    DECLARE student_now_status INT;
    SELECT current_status INTO student_now_status WHERE student_id = NEW.student_id;
    IF student_now_status = 0 THEN
        UPDATE student
        SET current_status = 1
        WHERE student_id = NEW.student_id;
    END IF;
END//
DELIMITER ;

DELIMITER //
CREATE TRIGGER topic_trigger_delete AFTER DELETE ON topic FOR EACH ROW
BEGIN
DECLARE this_student_total_project INT;
    SELECT COUNT(*) INTO this_student_total_project WHERE student_id = OLD.student_id;
    IF this_student_total_project = 0 THEN
        UPDATE student
        SET current_status = 0
        WHERE student_id = OLD.student_id;
    END IF;
END//
DELIMITER ;