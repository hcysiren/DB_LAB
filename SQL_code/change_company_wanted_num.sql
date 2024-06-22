-- Active: 1713270980889@@127.0.0.1@3306@db_finallab
DROP Procedure IF EXISTS ChangeCompanyWantedNum;
DELIMITER //
CREATE PROCEDURE ChangeCompanyWantedNum(IN this_company_id CHAR(8), IN wanted_num INT,IN type CHAR(1))
BEGIN
    DECLARE current_num INT;
    DECLARE current_want_num INT;
    START TRANSACTION;
    IF type = 'C' THEN              #说明是调整想要的顾问数目
        SELECT current_consultant_num INTO current_num FROM company WHERE this_company_id = company_id;
        IF wanted_num < current_num THEN
            SELECT 'Failure: Wanted consultant number cannot be less than current consultant number.' AS message;
            ROLLBACK;
        ELSE
            SELECT wanted_consultant_num INTO current_want_num FROM company WHERE company_id = this_company_id;
            UPDATE company SET wanted_consultant_num = wanted_num WHERE company_id = this_company_id;
            SELECT CONCAT('Success: Wanted consultant number changed from ', current_want_num, ' to ', wanted_num, '.') AS message;
            COMMIT;
        END IF;
    ELSEIF type = 'E' THEN          #说明是调整想要的员工数目
        SELECT current_employee_num INTO current_num FROM company WHERE this_company_id = company_id;
        IF wanted_num < current_num THEN
            SELECT 'Failure: Wanted employee number cannot be less than current employee number.' AS message;
            ROLLBACK;
        ELSE
            SELECT wanted_employee_num INTO current_want_num FROM company WHERE company_id = this_company_id;
            UPDATE company SET wanted_employee_num = wanted_num WHERE company_id = this_company_id;
            SELECT CONCAT('Success: Wanted employee number changed from ', current_want_num, ' to ', wanted_num, '.') AS message;
            COMMIT;
        END IF;
    ELSE
        SELECT 'Failure: Invalid type.' AS message;
        ROLLBACK;
    END IF;
END//
DELIMITER ;