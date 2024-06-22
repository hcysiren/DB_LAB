import customtkinter
from connect import *
import os

customtkinter.set_appearance_mode("dark")

class App(customtkinter.CTk):
    width = 1000
    height = 600

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.title("CustomTkinter example_background_image.py")
        self.geometry(f"{self.width}x{self.height}")
        self.resizable(True, True)
        
        self.grid_columnconfigure((0, 1, 2, 3), weight=1)
        self.grid_rowconfigure((0, 1, 2, 3), weight=1)
        
        # create sidebar frame
        self.sidebar_frame = customtkinter.CTkFrame(self, width=20, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, rowspan=4, sticky="nsw") #rowspan表示占据的行数
        self.sidebar_frame.grid_rowconfigure(4, weight=1)
        self.appearance_mode_label = customtkinter.CTkLabel(self.sidebar_frame, text="Appearance Mode:", anchor="w")
        self.appearance_mode_label.grid(row=5, column=0, padx=20, pady=(10, 0))
        self.appearance_mode_optionemenu = customtkinter.CTkOptionMenu(self.sidebar_frame, values=["Light", "Dark", "System"],
                                                                       command=self.change_appearance_mode_event)
        self.appearance_mode_optionemenu.grid(row=6, column=0, padx=20, pady=(10, 10))
        self.scaling_label = customtkinter.CTkLabel(self.sidebar_frame, text="UI Scaling:", anchor="w")
        self.scaling_label.grid(row=7, column=0, padx=20, pady=(10, 0))
        self.scaling_optionemenu = customtkinter.CTkOptionMenu(self.sidebar_frame, values=["20%","60%","80%", "90%", "100%", "110%", "120%"],
                                                               command=self.change_scaling_event)
        self.scaling_optionemenu.grid(row=8, column=0, padx=20, pady=(10, 20))
        #创建起始目录，有查看，更改，搜索三大区域
        self.start_menu = customtkinter.CTkFrame(self, corner_radius=0, width=900, height=600)
        self.start_menu.grid(row=0, column=1, rowspan=4, columnspan=3)
        self.start_menu_label = customtkinter.CTkLabel(self.start_menu, text="Welcome to graduation system",
                                                  font=customtkinter.CTkFont(size=40, weight="bold"))
        self.start_menu_label.grid(row=0, column=1, padx=50, pady=50)
        self.start_to_look_button = customtkinter.CTkButton(self.start_menu,text = 'look',command = self.start_to_look_event,width = 200,height = 50)
        self.start_to_look_button.grid(row = 1,column = 1,pady = 10)
        self.start_to_search_button = customtkinter.CTkButton(self.start_menu,text = 'search',command = self.start_to_search_event,width = 200,height = 50)
        self.start_to_search_button.grid(row = 2,column = 1,pady = 10)
        self.start_to_operate_button = customtkinter.CTkButton(self.start_menu,text = 'operate',command = self.start_to_operate_event,width = 200,height = 50)
        self.start_to_operate_button.grid(row = 3,column = 1,pady = 10)
        
        self.look_frame = customtkinter.CTkFrame(self, corner_radius=0, width=900, height=600)
        # self.look_frame.grid_columnconfigure(0, weight=1)
        self.look_frame.grid_remove()
        self.look_frame_label = customtkinter.CTkLabel(self.look_frame, text="存在下列可查看的表格", font=customtkinter.CTkFont(size=40, weight="bold",family="STXingkai"))
        self.look_frame_label.grid(row=0, column=0, padx=30, pady=50, columnspan=3)
        self.student_button = customtkinter.CTkButton(self.look_frame, text="student", command=self.student_event, width=200, height=50)
        self.student_button.grid(row=1, column=0, padx=30, pady=30)
        self.teacher_button = customtkinter.CTkButton(self.look_frame, text="teacher", command=self.teacher_event, width=200, height=50)
        self.teacher_button.grid(row=2, column=0, padx=30, pady=30)
        self.company_button = customtkinter.CTkButton(self.look_frame, text="company", command=self.company_event, width=200, height=50)
        self.company_button.grid(row=3, column=0, padx=30, pady=30)
        self.project_button = customtkinter.CTkButton(self.look_frame, text="project", command=self.project_event, width=200, height=50)
        self.project_button.grid(row=4, column=0, padx=30, pady=30)
        self.topic_button = customtkinter.CTkButton(self.look_frame, text="topic", command=self.topic_event, width=200, height=50)
        self.topic_button.grid(row=1, column=1, padx=30, pady=30)
        self.guidance_button = customtkinter.CTkButton(self.look_frame, text="guidance", command=self.guidance_event, width=200, height=50)
        self.guidance_button.grid(row=2, column=1, padx=30, pady=30)
        self.employee_button = customtkinter.CTkButton(self.look_frame, text="employee", command=self.employee_event, width=200, height=50)
        self.employee_button.grid(row=3, column=1, padx=30, pady=30)
        self.consultant_button = customtkinter.CTkButton(self.look_frame, text="consultant", command=self.consultant_event, width=200, height=50)
        self.consultant_button.grid(row=4, column=1, padx=30, pady=30)
        self.back_button = customtkinter.CTkButton(self.look_frame, text="Back", command=self.look_back_to_start_event, width=200, height=50)
        self.back_button.grid(row=1, column=2, padx=30, pady=30)
        
        self.search_frame = customtkinter.CTkFrame(self, corner_radius=0, width=900, height=600)
        self.search_frame.grid_remove()
        self.search_label = customtkinter.CTkLabel(self.search_frame, text="搜索栏", font=customtkinter.CTkFont(size=40, weight="bold",family="STXingkai"))
        self.search_label.grid(row=0, column=0, padx=30, pady=50, columnspan=3)
        self.search_student_id_entry = customtkinter.CTkEntry(self.search_frame,width=100, placeholder_text="search_student_id")
        self.search_student_id_entry.grid(row=1, column=1,pady = 10)
        self.search_student_name_entry = customtkinter.CTkEntry(self.search_frame,width=100, placeholder_text="search_name_id")
        self.search_student_name_entry.grid(row=2, column=1,pady = 10)
        self.search_by_id_button = customtkinter.CTkButton(self.search_frame, text="search_by_id", command=self.search_student_by_id_event, width=200, height=50)
        self.search_by_id_button.grid(row = 3,column = 1,pady = 10)
        self.search_by_name_button = customtkinter.CTkButton(self.search_frame, text="search_by_name", command=self.search_student_by_name_event, width=200, height=50)
        self.search_by_name_button.grid(row = 4,column = 1,pady = 10)
        self.back_button = customtkinter.CTkButton(self.search_frame, text="Back", command=self.search_back_to_start_event, width=200, height=50)
        self.back_button.grid(row=5, column=1,pady = 10)
        
        self.operate_frame = customtkinter.CTkFrame(self, corner_radius=0, width=900, height=600)
        self.operate_frame.grid_remove()
        self.operate_label = customtkinter.CTkLabel(self.operate_frame, text="操作栏", font=customtkinter.CTkFont(size=40, weight="bold",family="STXingkai"))
        self.operate_label.grid(row=0, column=0, padx=30, pady=50, columnspan=3)
        self.operate_back_to_start_button = customtkinter.CTkButton(self.operate_frame, text="Back", command=self.operate_back_to_start_event, width=200, height=50)
        self.operate_back_to_start_button.grid(row=1, column=0, padx=30, pady=30)
        self.recruit_employee_company_id_entry = customtkinter.CTkEntry(self.operate_frame,width=100, placeholder_text="recruit_employee_company_id")
        self.recruit_employee_company_id_entry.grid(row=1, column=1,pady = 10)
        self.recruit_employee_num_entry = customtkinter.CTkEntry(self.operate_frame,width=100, placeholder_text="want_num")
        self.recruit_employee_num_entry.grid(row=2, column=1,pady = 10)
        self.recruit_employee_button = customtkinter.CTkButton(self.operate_frame, text="recruit_employee", command=self.recruit_employee_event, width=200, height=50)
        self.recruit_employee_button.grid(row=3, column=1,pady = 10)
        self.operate_action_result_label = customtkinter.CTkLabel(self.operate_frame, text="操作结果", font=customtkinter.CTkFont(size=40, weight="bold"))
        self.operate_action_result_label.grid(row=5, column=1, padx=30, pady=50, columnspan=3)
        #上面是招募员工的部分
        
        self.recruit_consultant_company_id_entry = customtkinter.CTkEntry(self.operate_frame,width=100, placeholder_text="recruit_consultant_company_id")
        self.recruit_consultant_company_id_entry.grid(row=1, column=2,pady = 10)
        self.recruit_consultant_num_entry = customtkinter.CTkEntry(self.operate_frame,width=100, placeholder_text="want_num")
        self.recruit_consultant_num_entry.grid(row=2, column=2,pady = 10)
        self.recruit_consultant_button = customtkinter.CTkButton(self.operate_frame, text="recruit_consultant", command=self.recruit_consultant_event, width=200, height=50)
        self.recruit_consultant_button.grid(row=3, column=2,pady = 10)
        
        #上面是招募顾问的部分
        
        self.fire_employee_company_id_entry = customtkinter.CTkEntry(self.operate_frame,width=100, placeholder_text="fire_employee_company_id")
        self.fire_employee_company_id_entry.grid(row=1, column=3,pady = 10)
        self.fire_employee_id_entry = customtkinter.CTkEntry(self.operate_frame,width=100, placeholder_text="fire_employee_id")
        self.fire_employee_id_entry.grid(row=2, column=3,pady = 10)
        self.fire_employee_button = customtkinter.CTkButton(self.operate_frame, text="fire_employee", command=self.fire_employee_event, width=200, height=50)
        self.fire_employee_button.grid(row=3, column=3,pady = 10)
        
        #上面是解雇员工的部分
        self.operate_guidance_teacher_id_entry = customtkinter.CTkEntry(self.operate_frame,width=100, placeholder_text="operate_guidance_teacher_id")
        self.operate_guidance_teacher_id_entry.grid(row=1, column=4,pady = 10)
        self.operate_guidance_student_id_entry = customtkinter.CTkEntry(self.operate_frame,width=100, placeholder_text="operate_guidance_student_id")
        self.operate_guidance_student_id_entry.grid(row=2, column=4,pady = 10)
        self.add_guidance_button = customtkinter.CTkButton(self.operate_frame, text="add_guidance", command=self.add_guidance_event, width=200, height=50)
        self.add_guidance_button.grid(row=3, column=4,pady = 10)
        self.delete_guidance_button = customtkinter.CTkButton(self.operate_frame, text="delete_guidance", command=self.delete_guidance_event, width=200, height=50)
        self.delete_guidance_button.grid(row=4, column=4,pady = 10)
        #上面是改变guidance的部分
        
        self.operate_topic_student_id_entry = customtkinter.CTkEntry(self.operate_frame,width=100, placeholder_text="operate_topic_student_id")
        self.operate_topic_student_id_entry.grid(row=1, column=5,pady = 10)
        self.operate_topic_project_id_entry = customtkinter.CTkEntry(self.operate_frame,width=100, placeholder_text="operate_topic_project_id")
        self.operate_topic_project_id_entry.grid(row=2, column=5,pady = 10)
        self.add_topic_button = customtkinter.CTkButton(self.operate_frame, text="add_topic", command=self.add_topic_event, width=200, height=50)
        self.add_topic_button.grid(row=3, column=5,pady = 10)
        self.delete_topic_button = customtkinter.CTkButton(self.operate_frame, text="delete_topic", command=self.delete_topic_event, width=200, height=50)
        self.delete_topic_button.grid(row=4, column=5,pady = 10)
        
        #上面是改变topic的部分
        
        
        self.student_now_frame = customtkinter.CTkFrame(self, corner_radius=0, width=900, height=600)
        self.student_now_frame.grid_remove()
        self.student_info_label = customtkinter.CTkLabel(self.student_now_frame, text="学生信息", font=customtkinter.CTkFont(size=40, weight="bold",family="STXingkai"))
        self.student_info_label.grid(row=0, column=0, padx=30, pady=50, columnspan=3)
        self.insert_student_name_entry = customtkinter.CTkEntry(self.student_now_frame,width=100, placeholder_text="name")
        self.insert_student_name_entry.grid(row=1, column=3)
        self.insert_student_department_entry = customtkinter.CTkEntry(self.student_now_frame,width=100, placeholder_text="department")
        self.insert_student_department_entry.grid(row=2, column=3)
        self.insert_student_remark_entry = customtkinter.CTkEntry(self.student_now_frame,width=100, placeholder_text="remark")
        self.insert_student_remark_entry.grid(row=3, column=3)
        self.insert_student_GPA_entry = customtkinter.CTkEntry(self.student_now_frame,width=100, placeholder_text="GPA")
        self.insert_student_GPA_entry.grid(row=4, column=3)
        self.insert_student_button = customtkinter.CTkButton(self.student_now_frame, text="insert student", command=self.insert_student_event, width=200, height=50)
        self.insert_student_button.grid(row=5, column=3)
        self.back_button = customtkinter.CTkButton(self.student_now_frame, text="Back", command=self.student_back_to_look_event, width=200, height=50)
        self.back_button.grid(row=7, column=3)
        self.student_action_result_label = customtkinter.CTkLabel(self.student_now_frame, text="操作结果", font=customtkinter.CTkFont(size=40, weight="bold"))
        self.student_action_result_label.grid(row=0, column=1, columnspan=3)
        
        self.teacher_now_frame = customtkinter.CTkFrame(self, corner_radius=0, width=900, height=600)
        self.teacher_now_frame.grid_remove()
        self.teacher_info_label = customtkinter.CTkLabel(self.teacher_now_frame, text="教师信息", font=customtkinter.CTkFont(size=40, weight="bold",family="STXingkai"))
        self.teacher_info_label.grid(row=0, column=0, padx=30, pady=50, columnspan=3)
        self.insert_teacher_name_entry = customtkinter.CTkEntry(self.teacher_now_frame,width=100, placeholder_text="name")
        self.insert_teacher_name_entry.grid(row=1, column=3)
        self.insert_teacher_department_entry = customtkinter.CTkEntry(self.teacher_now_frame,width=100, placeholder_text="department")
        self.insert_teacher_department_entry.grid(row=2, column=3)
        self.insert_teacher_button = customtkinter.CTkButton(self.teacher_now_frame, text="insert teacher", command=self.insert_teacher_event, width=200, height=50)
        self.insert_teacher_button.grid(row=3, column=3)
        self.back_button = customtkinter.CTkButton(self.teacher_now_frame, text="Back", command=self.teacher_back_to_look_event, width=200, height=50)
        self.back_button.grid(row=7, column=3)
        self.teacher_action_result_label = customtkinter.CTkLabel(self.teacher_now_frame, text="操作结果", font=customtkinter.CTkFont(size=40, weight="bold"))
        self.teacher_action_result_label.grid(row=0, column=1, columnspan=3)
        
        self.project_now_frame = customtkinter.CTkFrame(self, corner_radius=0, width=900, height=600)
        self.project_now_frame.grid_remove()
        self.project_info_label = customtkinter.CTkLabel(self.project_now_frame, text="项目信息", font=customtkinter.CTkFont(size=40, weight="bold",family="STXingkai"))
        self.project_info_label.grid(row=0, column=0, padx=30, pady=50, columnspan=3)
        self.insert_project_name_entry = customtkinter.CTkEntry(self.project_now_frame,width=100, placeholder_text="name")
        self.insert_project_name_entry.grid(row=1, column=3)
        self.insert_project_department_entry = customtkinter.CTkEntry(self.project_now_frame,width=100, placeholder_text="department")
        self.insert_project_department_entry.grid(row=2, column=3)
        self.insert_project_button = customtkinter.CTkButton(self.project_now_frame, text="insert project", command=self.insert_project_event, width=200, height=50)
        self.insert_project_button.grid(row=3, column=3)
        self.back_button = customtkinter.CTkButton(self.project_now_frame, text="Back", command=self.project_back_to_look_event, width=200, height=50)
        self.back_button.grid(row=7, column=3)
        self.project_action_result_label = customtkinter.CTkLabel(self.project_now_frame, text="操作结果", font=customtkinter.CTkFont(size=40, weight="bold"))
        self.project_action_result_label.grid(row=0, column=1, columnspan=3)
        
        self.company_now_frame = customtkinter.CTkFrame(self, corner_radius=0, width=900, height=600)
        self.company_now_frame.grid_remove()
        self.company_info_label = customtkinter.CTkLabel(self.company_now_frame, text="公司信息", font=customtkinter.CTkFont(size=40, weight="bold",family="STXingkai"))
        self.company_info_label.grid(row=0, column=0, padx=30, pady=50, columnspan=3)
        self.company_action_result_label = customtkinter.CTkLabel(self.company_now_frame, text="操作结果", font=customtkinter.CTkFont(size=40, weight="bold"))
        self.company_action_result_label.grid(row=0, column=1, columnspan=3)
        self.change_want_num_company_id_entry = customtkinter.CTkEntry(self.company_now_frame,width=100, placeholder_text="company_id")
        self.change_want_num_company_id_entry.grid(row=1, column=3)
        self.change_want_num_entry = customtkinter.CTkEntry(self.company_now_frame,width=100, placeholder_text="want_num")
        self.change_want_num_entry.grid(row=2, column=3)
        self.change_type_entry = customtkinter.CTkEntry(self.company_now_frame,width=100, placeholder_text="type")
        self.change_type_entry.grid(row=3, column=3)
        self.change_want_num_button = customtkinter.CTkButton(self.company_now_frame, text="change_want_num_button", command=self.change_want_num_event, width=200, height=50)
        self.change_want_num_button.grid(row=4, column=3)
        self.insert_company_name_entry = customtkinter.CTkEntry(self.company_now_frame,width=100, placeholder_text="name")
        self.insert_company_name_entry.grid(row=5, column=3)
        self.insert_company_department_entry = customtkinter.CTkEntry(self.company_now_frame,width=100, placeholder_text="department")
        self.insert_company_department_entry.grid(row=6, column=3)
        self.insert_company_button = customtkinter.CTkButton(self.company_now_frame, text="insert company", command=self.insert_company_event, width=200, height=50)
        self.insert_company_button.grid(row=7, column=3)
        self.back_button = customtkinter.CTkButton(self.company_now_frame, text="Back", command=self.company_back_to_look_event, width=200, height=50)
        self.back_button.grid(row=8, column=3)
        
        self.guidance_now_frame = customtkinter.CTkFrame(self, corner_radius=0, width=900, height=600)
        self.guidance_now_frame.grid_remove()
        self.guidance_info_label = customtkinter.CTkLabel(self.guidance_now_frame, text="指导关系信息", font=customtkinter.CTkFont(size=40, weight="bold",family="STXingkai"))
        self.guidance_info_label.grid(row=0, column=0, padx=30, pady=50, columnspan=3)
        self.back_button = customtkinter.CTkButton(self.guidance_now_frame, text="Back", command=self.guidance_back_to_look_event, width=200, height=50)
        self.back_button.grid(row=7, column=3)
        
        self.topic_now_frame = customtkinter.CTkFrame(self, corner_radius=0, width=900, height=600)
        self.topic_now_frame.grid_remove()
        self.topic_info_label = customtkinter.CTkLabel(self.topic_now_frame, text="选题信息", font=customtkinter.CTkFont(size=40, weight="bold",family="STXingkai"))
        self.topic_info_label.grid(row=0, column=0, padx=30, pady=50, columnspan=3)
        self.back_button = customtkinter.CTkButton(self.topic_now_frame, text="Back", command=self.topic_back_to_look_event, width=200, height=50)
        self.back_button.grid(row=7, column=3)
        
        self.employee_now_frame = customtkinter.CTkFrame(self, corner_radius=0, width=900, height=600)
        self.employee_now_frame.grid_remove()
        self.employee_info_label = customtkinter.CTkLabel(self.employee_now_frame, text="员工信息", font=customtkinter.CTkFont(size=40, weight="bold",family="STXingkai"))
        self.employee_info_label.grid(row=0, column=0, padx=30, pady=50, columnspan=3)
        self.back_button = customtkinter.CTkButton(self.employee_now_frame, text="Back", command=self.employee_back_to_look_event, width=200, height=50)
        self.back_button.grid(row=7, column=3)
        
        self.consultant_now_frame = customtkinter.CTkFrame(self, corner_radius=0, width=900, height=600)
        self.consultant_now_frame.grid_remove()
        self.consultant_info_label = customtkinter.CTkLabel(self.consultant_now_frame, text="顾问信息", font=customtkinter.CTkFont(size=40, weight="bold",family="STXingkai"))
        self.consultant_info_label.grid(row=0, column=0, padx=30, pady=50, columnspan=3)
        self.back_button = customtkinter.CTkButton(self.consultant_now_frame, text="Back", command=self.consultant_back_to_look_event, width=200, height=50)
        self.back_button.grid(row=7, column=3)
        
        self.read_remark_frame = customtkinter.CTkFrame(self, corner_radius=0, width=900, height=600)
        self.read_remark_frame.grid_remove()
        self.read_remark_label = customtkinter.CTkLabel(self.read_remark_frame, text="学生备注", font=customtkinter.CTkFont(size=40, weight="bold",family="STXingkai"))
        self.read_remark_label.grid(row=0, column=0, padx=30, pady=50, columnspan=3)
        
        
    def change_appearance_mode_event(self, new_appearance_mode: str):
        customtkinter.set_appearance_mode(new_appearance_mode)
    
    def start_to_look_event(self):
        self.start_menu.grid_forget()
        self.look_frame.grid(row = 0, column =1,columnspan = 3,sticky = 'ns')
    
    def start_to_search_event(self):
        self.start_menu.grid_forget()
        self.search_frame.grid_forget()
        self.search_frame.grid(row = 0, column =1,columnspan = 3,sticky = 'ns')
        
    def look_back_to_start_event(self):
        self.look_frame.grid_forget()
        self.start_menu.grid(row=0, column=1, rowspan=4, columnspan=3)
    
    def student_back_to_look_event(self):
        self.student_now_frame.grid_forget()
        self.look_frame.grid(row = 0, column =1,columnspan = 3,sticky = 'ns')
    
    def teacher_back_to_look_event(self):
        self.teacher_now_frame.grid_forget()
        self.look_frame.grid(row = 0, column =1,columnspan = 3,sticky = 'ns')
        
    def project_back_to_look_event(self):
        self.project_now_frame.grid_forget()
        self.look_frame.grid(row = 0, column =1,columnspan = 3,sticky = 'ns')
        
    def company_back_to_look_event(self):
        self.company_now_frame.grid_forget()
        self.look_frame.grid(row = 0, column =1,columnspan = 3,sticky = 'ns')
    
    def guidance_back_to_look_event(self):
        self.guidance_now_frame.grid_forget()
        self.look_frame.grid(row = 0, column =1,columnspan = 3,sticky = 'ns')
        
    def topic_back_to_look_event(self):
        self.topic_now_frame.grid_forget()
        self.look_frame.grid(row = 0, column =1,columnspan = 3,sticky = 'ns')
    
    def employee_back_to_look_event(self):
        self.employee_now_frame.grid_forget()
        self.look_frame.grid(row = 0, column =1,columnspan = 3,sticky = 'ns')
    
    def consultant_back_to_look_event(self):
        self.consultant_now_frame.grid_forget()
        self.look_frame.grid(row = 0, column =1,columnspan = 3,sticky = 'ns')
    
    def start_to_operate_event(self):
        self.start_menu.grid_forget()
        self.operate_frame.grid(row = 0, column =1,columnspan = 3,sticky = 'ns')
        
    def insert_student_event(self):
        new_student_name = self.insert_student_name_entry.get()
        new_student_department = self.insert_student_department_entry.get()
        new_student_remark = self.insert_student_remark_entry.get()
        new_student_GPA = self.insert_student_GPA_entry.get()
        info = insert_student(new_student_name,new_student_department,new_student_remark,new_student_GPA)
        self.student_action_result_label.configure(text=info)
        
    def insert_teacher_event(self):
        new_teacher_name = self.insert_teacher_name_entry.get()
        new_teacher_department = self.insert_teacher_department_entry.get()
        info = insert_teacher(new_teacher_name,new_teacher_department)
        self.teacher_action_result_label.configure(text=info)
        
    def insert_project_event(self):
        new_project_name = self.insert_project_name_entry.get()
        new_project_department = self.insert_project_department_entry.get()
        info = insert_project(new_project_name,new_project_department)
        self.project_action_result_label.configure(text=info)
        
    def insert_company_event(self):
        new_company_name = self.insert_company_name_entry.get()
        new_company_department = self.insert_company_department_entry.get()
        info = insert_company(new_company_name,new_company_department)
        self.company_action_result_label.configure(text=info)
        
    def change_scaling_event(self, new_scaling: str):
        new_scaling_float = int(new_scaling.replace("%", "")) / 100
        customtkinter.set_widget_scaling(new_scaling_float)
        
    def student_event(self):
        self.look_frame.grid_forget()
        self.read_remark_frame.grid_forget()
        self.student_now_frame.grid(row = 0, column = 1,rowspan = 10,sticky = 'ns')
        student_result = get_student_table_all()
        index = 0
        for student in student_result:
            student_label = customtkinter.CTkLabel(self.student_now_frame, text=f"ID: {student.student_id}, 姓名: {student.name}, 专业: {student.department},当前状态: {student.current_status},GPA: {student.GPA}")
            student_label.grid(row=index+2, column=0, padx=5, pady=5)
            read_remark_button = customtkinter.CTkButton(self.student_now_frame, text="阅读备注", command=lambda s=student: self.read_student_remark_event(s))
            read_remark_button.grid(row=index+2, column=1, padx=5, pady=5)
            index += 1
    
    def teacher_event(self):
        self.look_frame.grid_forget()
        self.teacher_now_frame.grid(row = 0, column = 1,rowspan = 10,sticky = 'ns')
        teacher_result = get_teacher_table_all()
        index = 0
        for teacher in teacher_result:
            teacher_label = customtkinter.CTkLabel(self.teacher_now_frame, text=f"ID: {teacher.teacher_id}, 姓名: {teacher.name}, 专业: {teacher.department},指导学生数: {teacher.guide_student_num}")
            teacher_label.grid(row=index+2, column=0, padx=5, pady=5)
            index += 1
            
    def project_event(self):
        self.look_frame.grid_forget()
        self.project_now_frame.grid(row = 0, column = 1,rowspan = 10,sticky = 'ns')
        project_result = get_project_table_all()
        index = 0
        for project in project_result:
            project_label = customtkinter.CTkLabel(self.project_now_frame, text=f"ID: {project.project_id}, 名称: {project.name}, 专业: {project.department},来源: {project.source},最终分数: {project.final_score}")
            project_label.grid(row=index+2, column=0, padx=5, pady=5)
            index += 1
            
    def company_event(self):
        self.look_frame.grid_forget()
        self.company_now_frame.grid(row = 0, column = 1,rowspan = 10,sticky = 'ns')
        company_result = get_company_table_all()
        index = 0
        for company in company_result:
            company_label = customtkinter.CTkLabel(self.company_now_frame, text=f"ID: {company.company_id}, 名称: {company.name}, 地址: {company.address},电话: {company.telephone},部门: {company.department},当前顾问数: {company.current_consultant_num},当前员工数: {company.current_employee_num},期望顾问数: {company.wanted_consultant_num},期望员工数: {company.wanted_employee_num}")
            company_label.grid(row=index+2, column=0, padx=5, pady=5)
            index += 1
            
    def topic_event(self):
        self.look_frame.grid_forget()
        self.topic_now_frame.grid(row = 0, column = 1,rowspan = 10,sticky = 'ns')
        topic_result = get_topic_table_all()
        index = 0
        resultbox = customtkinter.CTkTextbox(self.topic_now_frame, width=300, height=300)
        resultbox.grid(row=2, column=0)
        for topic in topic_result:
            # topic_label = customtkinter.CTkLabel(self.topic_now_frame, text=f"学生ID: {topic.student_id}, 项目ID: {topic.project_id}")
            # topic_label.grid(row=index+2, column=0, padx=5, pady=5)
            resultbox.insert("0.0", f"学生ID: {topic.student_id}, 项目ID: {topic.project_id}\n")
            index += 1
            
    def guidance_event(self):
        self.look_frame.grid_forget()
        self.guidance_now_frame.grid(row = 0, column = 1,rowspan = 10,sticky = 'ns')
        guidance_result = get_guidance_table_all()
        index = 0
        result_box = customtkinter.CTkTextbox(self.guidance_now_frame, width=300, height=300)
        result_box.grid(row=2, column=0)
        for guidance in guidance_result:
            # guidance_label = customtkinter.CTkLabel(self.guidance_now_frame, text=f"学生ID: {guidance.student_id}, 教师ID: {guidance.teacher_id}")
            # guidance_label.grid(row=index+2, column=0, padx=5, pady=5)
            result_box.insert("0.0", f"学生ID: {guidance.student_id},教师ID: {guidance.teacher_id}\n")
            index += 1
    
    def employee_event(self):
        self.look_frame.grid_forget()
        self.employee_now_frame.grid(row = 0, column = 1,rowspan = 10,sticky = 'ns')
        employee_result = get_recruitment_table_all()
        index = 0
        resultbox = customtkinter.CTkTextbox(self.employee_now_frame, width=300, height=300)
        resultbox.grid(row=2, column=0)
        for employee in employee_result:
            # employee_label = customtkinter.CTkLabel(self.employee_now_frame, text=f"公司ID: {employee.company_id}, 员工ID: {employee.student_id}")
            # employee_label.grid(row=index+2, column=0, padx=5, pady=5)
            resultbox.insert("0.0", f"公司ID: {employee.company_id}, 员工ID: {employee.student_id}\n")
            index += 1
        
    def consultant_event(self):
        self.look_frame.grid_forget()
        self.consultant_now_frame.grid(row = 0, column = 1,rowspan = 10,sticky = 'ns')
        consultant_result = get_consultant_table_all()
        index = 0
        resultbox = customtkinter.CTkTextbox(self.consultant_now_frame, width=300, height=300)
        resultbox.grid(row=2, column=0)
        for consultant in consultant_result:
            # consultant_label = customtkinter.CTkLabel(self.consultant_now_frame, text=f"公司ID: {consultant.company_id}, 教师ID: {consultant.teacher_id}")
            # consultant_label.grid(row=index+2, column=0, padx=5, pady=5)
            resultbox.insert("0.0", f"公司ID: {consultant.company_id}, 教师ID: {consultant.teacher_id}\n")
            index += 1
    
    def search_student_by_id_event(self):
        search_student_id = self.search_student_id_entry.get()
        result = get_student_info_by_id(search_student_id)
        # student_label = customtkinter.CTkLabel(self.search_frame, text=f"ID: {result.student_id}, 姓名: {result.name}, 专业: {result.department},当前状态: {result.current_status},GPA: {result.GPA}")
        # student_label.grid(row=6, column=0, padx=5, pady=5)
        result_box = customtkinter.CTkTextbox(self.search_frame, width=300, height=300)
        result_box.grid(row=2, column=0)
        result_box.insert("0.0", f"ID: {result.student_id}, 姓名: {result.name}, 专业: {result.department},当前状态: {result.current_status},GPA: {result.GPA}")
        
    def search_student_by_name_event(self):
        search_student_name = self.search_student_name_entry.get()
        result = get_student_info_by_name(search_student_name)
        index = 0
        result_box = customtkinter.CTkTextbox(self.search_frame, width=300, height=300)
        result_box.grid(row=2, column=0)
        for student in result:
            # student_label = customtkinter.CTkLabel(self.search_frame, text=f"ID: {student.student_id}, 姓名: {student.name}, 专业: {student.department},当前状态: {student.current_status},GPA: {student.GPA}")
            # student_label.grid(row=index+2, column=0, padx=5, pady=5)
            result_box.insert("0.0", f"ID: {student.student_id}, 姓名: {student.name}, 专业: {student.department},当前状态: {student.current_status},GPA: {student.GPA}\n")
            # index += 1
        
    def search_back_to_start_event(self):
        self.search_frame.grid_forget()
        self.start_menu.grid(row=0, column=1, rowspan=4, columnspan=3)
        
    def recruit_employee_event(self):
        recruit_employee_company_id = self.recruit_employee_company_id_entry.get()
        recruit_employee_num = self.recruit_employee_num_entry.get()
        info = insert_employee(recruit_employee_company_id,recruit_employee_num)
        if(type(info) == str):
            self.operate_action_result_label.configure(text = info)
        else:
            real_info = info.fetchone()[0]
            self.operate_action_result_label.configure(text = real_info)
        
    def recruit_consultant_event(self):
        recruit_consultant_company_id = self.recruit_consultant_company_id_entry.get()
        recruit_consultant_num = self.recruit_consultant_num_entry.get()
        info = insert_consultant(recruit_consultant_company_id,recruit_consultant_num)
        if(type(info) == str):
            self.operate_action_result_label.configure(text = info)
        else:
            real_info = info.fetchone()[0]
            self.operate_action_result_label.configure(text = real_info)
        
    def fire_employee_event(self):
        fire_employee_company_id = self.fire_employee_company_id_entry.get()
        fire_employee_id = self.fire_employee_id_entry.get()
        info = delete_employee(fire_employee_company_id,fire_employee_id)
        if(type(info) == str):
            self.operate_action_result_label.configure(text = info)
        elif(info.fetchone()[0] == 'OK'):
            new_text = "解雇成功，雇员学号为" + fire_employee_id,"，公司编号为"+ fire_employee_company_id
            self.operate_action_result_label.configure(text = new_text)
        else:
            real_info = info.fetchone()[0]
            self.operate_action_result_label.configure(text = real_info)
        
    def add_guidance_event(self):
        operate_guidance_teacher_id = self.operate_guidance_teacher_id_entry.get()
        operate_guidance_student_id = self.operate_guidance_student_id_entry.get()
        info = insert_guidance(operate_guidance_teacher_id,operate_guidance_student_id)
        self.operate_action_result_label.configure(text = info)
        
    def delete_guidance_event(self):
        operate_guidance_teacher_id = self.operate_guidance_teacher_id_entry.get()
        operate_guidance_student_id = self.operate_guidance_student_id_entry.get()
        info = delete_guidance(operate_guidance_teacher_id,operate_guidance_student_id)
        self.operate_action_result_label.configure(text = info)
        
    def add_topic_event(self):
        operate_topic_student_id = self.operate_topic_student_id_entry.get()
        operate_topic_project_id = self.operate_topic_project_id_entry.get()
        info = insert_topic(operate_topic_student_id,operate_topic_project_id)
        self.operate_action_result_label.configure(text = info)
        
    def delete_topic_event(self):
        operate_topic_student_id = self.operate_topic_student_id_entry.get()
        operate_topic_project_id = self.operate_topic_project_id_entry.get()
        info = delete_topic(operate_topic_student_id,operate_topic_project_id)
        self.operate_action_result_label.configure(text = info)
        
    def operate_back_to_start_event(self):
        self.operate_frame.grid_forget()
        self.start_menu.grid(row=0, column=1, rowspan=4, columnspan=3)
        
    def change_want_num_event(self):
        change_want_num_company_id = self.change_want_num_company_id_entry.get()
        change_want_num = self.change_want_num_entry.get()
        change_type = self.change_type_entry.get()
        info = change_company_wanted_num(change_want_num_company_id,change_want_num,change_type)
        if(type(info) == str):
            self.company_action_result_label.configure(text = info)
        else:
            real_info = info.fetchone()[0]
            self.company_action_result_label.configure(text = real_info)

    def read_student_remark_event(self, student):
        self.student_now_frame.grid_forget()
        self.read_remark_frame.grid(row=0, column=0, rowspan=4, columnspan=4, sticky="ns")
        # 读取书籍内容
        for widget in self.read_remark_frame.winfo_children():
            widget.destroy()
        remark_content = get_remark_content(student.student_id)
        self.remark_content_label = customtkinter.CTkLabel(self.read_remark_frame, text=remark_content, font=customtkinter.CTkFont(size=20, weight="bold"))
        self.remark_content_label.grid(row=1, column=0, padx=30, pady=50)
        self.back_button = customtkinter.CTkButton(self.read_remark_frame, text="Back", command=self.student_event, width=200)
        self.back_button.grid(row=2, column=0, padx=30, pady=50)
if __name__ == "__main__":
    app = App()
    app.mainloop()