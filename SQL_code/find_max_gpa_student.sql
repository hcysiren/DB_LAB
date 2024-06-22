-- Active: 1713270980889@@127.0.0.1@3306@db_finallab
DROP FUNCTION IF EXISTS find_max_gpa_student;
delimiter //
create function find_max_gpa_student(status int)
returns char(8)
DETERMINISTIC
READS SQL DATA
BEGIN
    DECLARE king_id char(8);
    SELECT student_id INTO king_id FROM (SELECT * FROM student WHERE student.current_status = status ORDER BY GPA DESC LIMIT 1) as KING ;
    RETURN king_id;
END//
delimiter ;