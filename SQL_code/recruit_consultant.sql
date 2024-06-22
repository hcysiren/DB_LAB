DROP PROCEDURE IF EXISTS RecruitTeachers;
DELIMITER //

CREATE PROCEDURE RecruitTeachers (
    IN this_company_id CHAR(8),
    IN this_wanted_num INT
)
BEGIN
    DECLARE available_positions INT;
    DECLARE valid_teacher_num INT;
    DECLARE this_total_wanted_consultant_num INT;
    DECLARE this_current_consultant_num INT;
    DECLARE teacher_total_num INT;

    SELECT current_consultant_num, wanted_consultant_num INTO this_current_consultant_num, this_total_wanted_consultant_num FROM company WHERE company_id = this_company_id;
    SET available_positions = LEAST(this_wanted_num, this_total_wanted_consultant_num - this_current_consultant_num);

    DROP TEMPORARY TABLE IF EXISTS temp_teacher;

    -- 检查公司的最大招募人数是否满足招募要求
    IF available_positions = 0 THEN
        SELECT 'Failure: No available positions.' AS message;
    ELSE
        START TRANSACTION;

        -- 创建临时表存储符合条件的教师
        CREATE TEMPORARY TABLE temp_teacher AS
            SELECT teacher_id FROM Teacher
            WHERE department = (SELECT department FROM Company WHERE company_id = this_company_id);

        SELECT COUNT(*) INTO teacher_total_num FROM temp_teacher;

        IF teacher_total_num = 0 THEN
            SELECT 'Failure: No relevant consultant available.' AS message;
            DROP TEMPORARY TABLE IF EXISTS temp_teacher;
            ROLLBACK;
        ELSEIF available_positions < teacher_total_num THEN
            SELECT 'Failure: Cannot recruit all the consultants.' AS message;
            DROP TEMPORARY TABLE IF EXISTS temp_teacher;
            ROLLBACK;
        ELSE
            INSERT INTO consultant(company_id, teacher_id)
            SELECT this_company_id, teacher_id FROM temp_teacher;

            UPDATE Company
            SET current_consultant_num = this_current_consultant_num + teacher_total_num
            WHERE company_id = this_company_id;

            SELECT CONCAT('Success: ', teacher_total_num, ' teacher recruited.') AS message;
            DROP TEMPORARY TABLE IF EXISTS temp_teacher;
            COMMIT;
        END IF;
    END IF;
END //

DELIMITER ;
