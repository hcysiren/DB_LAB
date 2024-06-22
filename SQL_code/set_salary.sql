-- Active: 1713270980889@@127.0.0.1@3306@db_finallab
DROP PROCEDURE IF EXISTS SetSalary;
CREATE PROCEDURE SetSalary(IN this_company_id CHAR(8), IN this_employee_id CHAR(8), IN new_salary INT)
BEGIN
    UPDATE recruitment SET salary = new_salary WHERE company_id = this_company_id AND student_id = this_employee_id;
END