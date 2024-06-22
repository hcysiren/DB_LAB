-- Active: 1713270980889@@127.0.0.1@3306@db_finallab
Drop Table if exists Student;
Drop Table if exists Teacher;
Drop Table if exists Project;
Drop Table if exists Company;

Drop Table if exists Topic;
Drop Table if exists Design;
Drop Table if exists Consultant;
Drop Table if exists Recruitment;
Drop Table if exists Guidence;

Create Table Student(
student_id char(8),
name varchar(50),
sex varchar(6),
age int,
department varchar(50),
telephone varchar(20),
remark_path varchar(100),
current_status int,
GPA float,
constraint PK primary key (student_id)
);

Create Table Teacher(
teacher_id char(8),
name varchar(50),
sex varchar(6),
age int,
department varchar(50),
telephone varchar(20),
guide_student_num int default 0,
design_project_num int default 0,
constraint PK primary key (teacher_id)
);

Create Table Project(
project_id char(8),
name varchar(50),
department varchar(50),
source varchar(50),
final_score int default 0,
constraint PK primary key (project_id)
)

Create Table Company(
company_id char(8),
name varchar(50),
address varchar(100),
telephone varchar(20),
department varchar(50),
current_consultant_num int default 0,
current_employee_num int default 0,
wanted_consultant_num int default 0,
wanted_employee_num int default 0,
constraint PK primary key (company_id)
)

Create Table Topic(
    student_id char(8),
    project_id char(8),
    constraint PK primary key (student_id, project_id),
    constraint FK_topic_student foreign key (student_id) references Student(student_id),
    constraint FK_topic_project foreign key (project_id) references Project(project_id)
)

/* Create Table Design(
    project_id char(8),
    teacher_id char(8),
    constraint PK primary key (project_id, teacher_id)
) */

Create Table Consultant(
    company_id char(8),
    teacher_id char(8),
    constraint PK primary key (company_id, teacher_id),
    constraint FK_consultant_company foreign key (company_id) references Company(company_id),
    constraint FK_consultant_teacher foreign key (teacher_id) references Teacher(teacher_id)
)

Create Table Recruitment(
    student_id char(8),
    company_id char(8),
    salary int,
    constraint PK primary key (student_id, company_id),
    constraint FK_recruitment_student foreign key (student_id) references Student(student_id),
    constraint FK_recruitment_company foreign key (company_id) references Company(company_id)
)

Create Table Guidence(
    student_id char(8),
    teacher_id char(8),
    constraint PK primary key (student_id, teacher_id),
    constraint FK_guidence_student foreign key (student_id) references Student(student_id),
    constraint FK_guidence_teacher foreign key (teacher_id) references Teacher(teacher_id)
)