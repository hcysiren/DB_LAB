from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship

Base = declarative_base()

class Student(Base):
    __tablename__ = 'Student'
    student_id = Column(String(8), primary_key=True)
    name = Column(String(50))
    sex = Column(String(6))
    age = Column(Integer)
    department = Column(String(50))
    telephone = Column(String(20))
    remark_path = Column(String(100))
    current_status = Column(Integer)
    GPA = Column(Float)

class Teacher(Base):
    __tablename__ = 'Teacher'
    teacher_id = Column(String(8), primary_key=True)
    name = Column(String(50))
    sex = Column(String(6))
    age = Column(Integer)
    department = Column(String(50))
    telephone = Column(String(20))
    guide_student_num = Column(Integer, default=0)
    design_project_num = Column(Integer, default=0)

class Project(Base):
    __tablename__ = 'Project'
    project_id = Column(String(8), primary_key=True)
    name = Column(String(50))
    department = Column(String(50))
    source = Column(String(50))
    final_score = Column(Integer, default=0)

class Company(Base):
    __tablename__ = 'Company'
    company_id = Column(String(8), primary_key=True)
    name = Column(String(50))
    address = Column(String(100))
    telephone = Column(String(20))
    department = Column(String(50))
    current_consultant_num = Column(Integer, default=0)
    current_employee_num = Column(Integer, default=0)
    wanted_consultant_num = Column(Integer, default=0)
    wanted_employee_num = Column(Integer, default=0)

class Topic(Base):
    __tablename__ = 'Topic'
    student_id = Column(String(8), ForeignKey('Student.student_id'), primary_key=True)
    project_id = Column(String(8), ForeignKey('Project.project_id'), primary_key=True)
    student = relationship("Student", back_populates="topics")
    project = relationship("Project", back_populates="topics")

class Consultant(Base):
    __tablename__ = 'Consultant'
    company_id = Column(String(8), ForeignKey('Company.company_id'), primary_key=True)
    teacher_id = Column(String(8), ForeignKey('Teacher.teacher_id'), primary_key=True)
    company = relationship("Company", back_populates="consultants")
    teacher = relationship("Teacher", back_populates="consultants")

class Recruitment(Base):
    __tablename__ = 'Recruitment'
    student_id = Column(String(8), ForeignKey('Student.student_id'), primary_key=True)
    company_id = Column(String(8), ForeignKey('Company.company_id'), primary_key=True)
    salary = Column(Integer)
    student = relationship("Student", back_populates="recruitments")
    company = relationship("Company", back_populates="recruitments")

class Guidance(Base):
    __tablename__ = 'Guidance'
    student_id = Column(String(8), ForeignKey('Student.student_id'), primary_key=True)
    teacher_id = Column(String(8), ForeignKey('Teacher.teacher_id'), primary_key=True)
    student = relationship("Student", back_populates="guidances")
    teacher = relationship("Teacher", back_populates="guidances")

# Setting up relationships
Student.topics = relationship("Topic", back_populates="student")
Student.recruitments = relationship("Recruitment", back_populates="student")
Student.guidances = relationship("Guidance", back_populates="student")
Teacher.consultants = relationship("Consultant", back_populates="teacher")
Teacher.guidances = relationship("Guidance", back_populates="teacher")
Project.topics = relationship("Topic", back_populates="project")
Company.consultants = relationship("Consultant", back_populates="company")
Company.recruitments = relationship("Recruitment", back_populates="company")
