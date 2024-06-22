-- Active: 1713270980889@@127.0.0.1@3306@db_finallab
DROP TRIGGER IF EXISTS teacher_guide_trigger_insert;
DROP TRIGGER IF EXISTS teacher_guide_trigger_delete;
DELIMITER //
CREATE TRIGGER teacher_guide_trigger_insert AFTER INSERT ON guidence FOR EACH ROW
BEGIN
    UPDATE teacher
    SET guide_student_num = guide_student_num + 1
    WHERE teacher_id = NEW.teacher_id;
END//
DELIMITER ;

/* DELIMITER //
CREATE TRIGGER teacher_guide_trigger_update AFTER UPDATE ON guidence FOR EACH ROW
BEGIN
    UPDATE teacher
    SET guide_student_num = guide_student_num - 1
    WHERE teacher_id = OLD.teacher_id;
    UPDATE teacher
    SET guide_student_num = guide_student_num + 1
    WHERE teacher_id = NEW.teacher_id;
END//
DELIMITER ; */

DELIMITER //
CREATE TRIGGER teacher_guide_trigger_delete AFTER DELETE ON guidence FOR EACH ROW
BEGIN
    UPDATE teacher
    SET guide_student_num = guide_student_num - 1
    WHERE teacher_id = OLD.teacher_id;
END
DELIMITER ;