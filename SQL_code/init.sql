-- Active: 1713270980889@@127.0.0.1@3306@db_finallab
INSERT INTO student(student_id,name,sex,age,department,telephone,remark_path,current_status,GPA)
VALUES
('S0001','A','Male','20','AI','12345','hello','0','4.0'),
('S0002','B','Male','21','AI','12345','hello','0','3.7'),
('S0003','C','Male','20','AI','12345','hello','1','3.1'),
('S0004','D','Male','20','AI','12345','hello','1','2.2'),
('S0005','E','Male','20','CS','12345','hello','0','4.3'),
('S0006','F','Male','20','CS','12345','hello','1','3.9');

INSERT INTO company(company_id,name,address,telephone,department,wanted_consultant_num,wanted_employee_num)
VALUES
('C0001','A_COM','A_PLACE','12345','AI',3,4),
('C0002','B_COM','B_PLACE','12345','AI',3,2),
('C0003','C_COM','C_PLACE','12345','AI',3,5),
('C0004','D_COM','D_PLACE','12345','AI',2,1),
('C0005','E_COM','E_PLACE','12345','CS',2,4),
('C0006','F_COM','F_PLACE','12345','CS',6,0);

INSERT INTO teacher(teacher_id,name,sex,age,department,telephone,guide_student_num,design_project_num)
VALUES
('T0001','TA','Male','30','AI','12345',0,0),
('T0002','TB','Male','30','AI','12345',0,0),
('T0003','TC','Male','30','AI','12345',0,0),
('T0004','TD','Male','30','AI','12345',0,0),
('T0005','TE','Male','30','CS','12345',0,0),
('T0006','TF','Male','30','CS','12345',0,0),
('T0007','TG','Male','30','CS','12345',0,0);

INSERT INTO guidence(teacher_id,student_id)
VALUES
('T0001','S0001'),
('T0001','S0002'),
('T0001','S0003'),
('T0002','S0004'),
('T0002','S0005'),
('T0002','S0006');

UPDATE guidence SET teacher_id = '0003' WHERE teacher_id = '0001' AND student_id = '0001';

INSERT INTO topic(student_id,project_id)
VALUES
('S0001','P0001');

DELETE FROM topic WHERE student_id = 'S0001';

call RecruitStudents('C0001',2)

call `ChangeCompanyWantedNum`('C0001',1,'E')

CALL SetSalary('C0001', 'S0003', 10000)

CALL DeleteEmployee('C0001', 'S0003')

CALL DeleteEmployee('C0001','S0004')