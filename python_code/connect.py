from sqlalchemy import create_engine,Table,Column,Integer,String,MetaData,ForeignKey,text, func, cast, update, and_
from sqlalchemy.orm import scoped_session, sessionmaker
from model import *  # 确保已经定义了相应的模型类

# 数据库引擎
engine = create_engine(
    "mysql+pymysql://root:hcy672672@127.0.0.1:3306/db_finallab",
    echo=True,
    future=True
)

metaData = MetaData()
metaData.bind = engine

# 会话
Session = scoped_session(sessionmaker(bind=engine, autoflush=False))
session = Session()

def init_db():
    metaData.create_all(engine, checkfirst=True)
    
def drop_db():
    metaData.drop_all(engine, checkfirst=True)
    
# def login(username, role):
#     if role == 'student':
#         user = session.query(Student).filter(Student.student_id == username).first()
#     elif role == 'teacher':
#         user = session.query(Teacher).filter(Teacher.teacher_id == username).first()
#     else:
#         user = None
#     return user is not None

def insert_student(name, department,remark_path, GPA):
    student_id = session.query(func.min_available_id('S')).first()[0]
    new_student = Student(
        student_id=student_id,
        name=name,
        department=department,
        remark_path=remark_path,
        current_status=0,
        GPA=GPA
    )
    session.add(new_student)
    session.commit()
    return '学生添加成功，学号为：' + student_id

def insert_teacher(name,department):
    teacher_id = session.query(func.min_available_id('T')).first()[0]
    new_teacher = Teacher(
        teacher_id=teacher_id,
        name=name,
        department=department,
        guide_student_num=0
    )
    session.add(new_teacher)
    session.commit()
    return '教师添加成功，工号为：' + teacher_id

def insert_project(name, department):
    project_id = session.query(func.min_available_id('P')).first()[0]
    new_project = Project(
        project_id=project_id,
        name=name,
        department=department,
        final_score=0
    )
    session.add(new_project)
    session.commit()
    return '项目添加成功，项目编号为：' + project_id

def insert_company(name, department):
    company_id = session.query(func.min_available_id('C')).first()[0]
    new_company = Company(
        company_id=company_id,
        name=name,
        department=department,
        current_consultant_num=0,
        current_employee_num=0,
        wanted_consultant_num=0,
        wanted_employee_num=0
    )
    session.add(new_company)
    session.commit()
    return '公司添加成功，公司编号为：' + company_id

def get_student_info_by_id(student_id):
    student = session.query(Student).filter(Student.student_id == student_id).first()
    return student

def get_student_info_by_name(name):
    student = session.query(Student).filter(Student.name == name).all()
    return student

def get_student_remark(path):
    with open(path, 'r') as f:
        return f.read()
    
def insert_guidance(teacher_id, student_id):
    this_student = session.query(Student).filter(Student.student_id == student_id).first()
    this_teacher = session.query(Teacher).filter(Teacher.teacher_id == teacher_id).first()
    this_pair = session.query(Guidance).filter(and_(Guidance.student_id == student_id,Guidance.teacher_id == teacher_id)).first()
    student_exist = True
    teacher_exist = True
    info = '指导关系添加失败，'
    if this_pair is not None:
        return '指导关系已存在'
    if this_student is None:
        student_exist = False
    if this_teacher is None:
        teacher_exist = False
    if(student_exist == True and teacher_exist == True):
        new_guidance = Guidance(
            teacher_id=teacher_id,
            student_id=student_id
        )
        session.add(new_guidance)
        session.commit()
        return '指导关系添加成功, 学生学号为：' + student_id + '，教师工号为：' + teacher_id
    if(student_exist == False):
        info += '学生不存在'
    if(teacher_exist == False):
        info += '教师不存在'
    return info

def insert_consultant(company_id,wanted_num):
    this_company = session.query(Company).filter(Company.company_id == company_id).first()
    company_exist = True
    info = '招聘失败，'
    if this_company is None:
        company_exist = False
    if(company_exist == True and int(wanted_num) > 0):
        recruitment_info = session.execute(text("call RecruitConsultants(:this_company_id, :this_wanted_num)")
                            , {'this_company_id':company_id, 'this_wanted_num':wanted_num})
        session.commit()
        return recruitment_info
    else:
        if(company_exist == False):
            info += '公司不存在'
        if(int(wanted_num) <= 0):
            info += '招聘人数不合法'
        return info

def insert_employee(company_id,wanted_num):
    this_company = session.query(Company).filter(Company.company_id == company_id).first()
    company_exist = True
    info = '招聘失败，'
    if this_company is None:
        company_exist = False
    if(company_exist == True and int(wanted_num) > 0):
        recruitment_info = session.execute(text("call RecruitStudents(:this_company_id, :this_wanted_num)")
                            , {'this_company_id':company_id, 'this_wanted_num':wanted_num})
        session.commit()
        return recruitment_info
    else:
        if(company_exist == False):
            info += '公司不存在'
        if(int(wanted_num) <= 0):
            info += '招聘人数不合法'
        return info

def delete_employee(company_id, student_id):
    this_pair = session.query(Recruitment).filter(and_(Recruitment.student_id == student_id,Recruitment.company_id == company_id)).first()
    pair_exist = True
    info = '删除失败，雇佣关系中'
    if this_pair is None:
        pair_exist = False
    if(this_pair is not None):
        delete_info = session.execute(text("call DeleteEmployee(:this_company_id, :this_student_id)")
                                ,{'this_company_id':company_id, 'this_student_id':student_id})
        session.commit()
        return delete_info
    if(pair_exist == False):
        info += '雇佣关系不存在'  
    return info

def delete_guidance(teacher_id, student_id):
    this_pair = session.query(Guidance).filter(and_(Guidance.student_id == student_id,Guidance.teacher_id == teacher_id)).first()
    pair_exist = True
    info = '删除失败，指导关系中'
    if this_pair is None:
        pair_exist = False

    if(pair_exist == True):
        session.query(Guidance).filter(and_(Guidance.teacher_id == teacher_id, Guidance.student_id == student_id)).delete()
        session.commit()
        return '指导关系删除成功, 学生学号为：' + student_id + '，教师工号为：' + teacher_id
    else:
        if (pair_exist == False):
            info += '指导关系不存在'
        return info

def insert_topic(student_id, project_id):
    this_student = session.query(Student).filter(Student.student_id == student_id).first()
    this_project = session.query(Project).filter(Project.project_id == project_id).first()
    this_pair = session.query(Topic).filter(and_(Topic.student_id == student_id,Topic.project_id == project_id)).first()
    
    student_exist = True
    project_exist = True
    info = '选题失败，'
    if(this_pair is not None):
        return '选题关系已存在'
    if this_student is None:
        student_exist = False
    if this_project is None:
        project_exist = False
    if(student_exist == True and project_exist == True):
        new_topic = Topic(
            student_id=student_id,
            project_id=project_id
        )
        session.add(new_topic)
        session.commit()
        return '选题成功, 学生学号为：' + student_id + '，项目编号为：' + project_id
    if(student_exist == False):
        info += '学生不存在'
    if(project_exist == False):
        info += '项目不存在'
    return info

def delete_topic(student_id, project_id):
    this_pair = session.query(Topic).filter(and_(Topic.student_id == student_id,Topic.project_id == project_id)).first()
    this_student = session.query(Student).filter(Student.student_id == student_id).first()
    pair_exist = True
    not_have_job = True
    info = '退选失败，选题关系中'
    if this_pair is None:
        pair_exist = False
    if this_student.current_status == 2:
        not_have_job = False
    if(pair_exist == True and not_have_job == True):
        session.query(Topic).filter(and_(Topic.student_id == student_id, Topic.project_id == project_id)).delete()
        session.commit()
        return '退选成功, 学生学号为：' + student_id + '，项目编号为：' + project_id
    else:
        if(pair_exist == False):
            info += '选题关系不存在'
        if(not_have_job == False):
            info += '学生已经有工作'
        return info
#下面展开测试

def change_company_wanted_num(company_id,wanted_num,type):
    this_company = session.query(Company).filter(Company.company_id == company_id).first()
    company_exist = True
    info = '更改人数失败，'
    if this_company is None:
        company_exist = False
    if(company_exist):
        change_info = session.execute(text("call ChangeCompanyWantedNum(:this_company_id, :wanted_num, :type)")
                                ,{'this_company_id':company_id, 'wanted_num':wanted_num, 'type':type})
        return change_info
    else:
        if(company_exist == False):
            info += '公司不存在'
        return info

# def set_salary(company_id,employee_id,salary):
#         session.execute(text("call SetSalary(:this_company_id, :this_employee_id, :new_salary)")
#                                 ,{'this_company_id':company_id, 'this_employee_id':employee_id, 'new_salary':salary})
        
def get_student_table_all():
    student_all = session.query(Student).all()
    return student_all

def get_teacher_table_all():
    teacher_all = session.query(Teacher).all()
    return teacher_all

def get_project_table_all():
    project_all = session.query(Project).all()
    return project_all

def get_company_table_all():
    company_all = session.query(Company).all()
    return company_all

def get_guidance_table_all():
    guidance_all = session.query(Guidance).all()
    return guidance_all

def get_topic_table_all():
    topic_all = session.query(Topic).all()
    return topic_all

def get_recruitment_table_all():
    recruitment_all = session.query(Recruitment).all()
    return recruitment_all

def get_consultant_table_all():
    consultant_all = session.query(Consultant).all()
    return consultant_all

def get_remark_content(student_id):
    student = session.query(Student).filter(Student.student_id == student_id).first()
    with open(student.remark_path, 'r') as f:
        return f.read()
if __name__ == '__main__':
    change_info = change_company_wanted_num('C0001', 1, 'E')
    print(change_info.fetchone())