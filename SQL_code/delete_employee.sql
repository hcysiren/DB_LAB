-- Active: 1713270980889@@127.0.0.1@3306@db_finallab
DROP PROCEDURE IF EXISTS DeleteEmployee;
DELIMITER //
CREATE Procedure DeleteEmployee(IN this_company_id char(8),IN employee_id CHAR(8))
BEGIN
    DECLARE exist INT;
    DECLARE still_have_topic INT;
    SELECT COUNT(*) INTO exist FROM recruitment WHERE company_id = this_company_id AND employee_id = employee_id;
    IF exist = 0 THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'The employee does not exist in the company';
    ELSE
    DELETE FROM recruitment WHERE company_id = this_company_id AND employee_id = student_id;
    UPDATE company SET current_employee_num = current_employee_num - 1 WHERE this_company_id = company_id;
    SELECT 'OK';
    SELECT COUNT(*) INTO still_have_topic FROM topic WHERE topic.student_id = employee_id;
    IF still_have_topic = 0 THEN
    UPDATE student SET current_status = 0 WHERE student_id = employee_id;
    ELSE
    UPDATE student SET current_status = 1 WHERE student_id = employee_id;
    END IF;
    END IF;
END//
DELIMITER ;