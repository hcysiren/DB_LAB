DROP PROCEDURE IF EXISTS RecruitStudents;
DELIMITER //

CREATE PROCEDURE RecruitStudents (
    IN this_company_id CHAR(8),
    IN this_wanted_num INT
)
BEGIN

    DECLARE available_positions INT;
    DECLARE valid_student_num INT;
    DECLARE this_total_wanted_employee_num INT;
    DECLARE this_current_employee_num INT;

    SELECT current_employee_num, wanted_employee_num INTO this_current_employee_num, this_total_wanted_employee_num FROM company WHERE company_id = this_company_id;
    SET available_positions = LEAST(this_wanted_num, this_total_wanted_employee_num - this_current_employee_num);

    DROP TEMPORARY TABLE IF EXISTS temp_student;
    -- 检查公司的最大招募人数是否满足招募要求
    IF available_positions = 0 THEN
        SELECT 'Failure: No available positions.' AS message;
    ELSE
    -- 创建临时表存储符合条件的学生
    CREATE TEMPORARY TABLE temp_student AS
        SELECT student_id FROM Student
        WHERE department = (SELECT department FROM Company WHERE company_id = this_company_id)
          AND current_status = 1
        ORDER BY GPA DESC
        LIMIT available_positions;

    SELECT COUNT(*) INTO valid_student_num FROM temp_student;

    IF valid_student_num = 0 THEN
        SELECT 'Failure: No student available.' AS message;
        DROP TEMPORARY TABLE temp_student;
    ELSE
    -- 选择符合条件的学生并更新状态
    UPDATE Student
    SET current_status = 2
    WHERE student_id IN (SELECT student_id FROM temp_student);

    -- 插入招募记录
    INSERT INTO Recruitment(company_id, student_id)
    SELECT this_company_id, student_id FROM temp_student;

    -- 更新公司的当前雇员数
    UPDATE Company
    SET current_employee_num = this_current_employee_num + valid_student_num
    WHERE company_id = this_company_id;

    -- 输出成功信息
    SELECT CONCAT('Success: ', valid_student_num, ' students recruited.') AS message;
    DROP TEMPORARY TABLE temp_student;
    END IF;
    END IF;
END //

DELIMITER ;
