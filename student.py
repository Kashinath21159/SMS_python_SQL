from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk   #pip install pillow
import mysql.connector
from tkinter import messagebox



class Student:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1365x760+0+0")
        self.root.title("STUDENT MANAGEMENT SYSTEM")

        # variable
        self.var_dep=StringVar()
        self.var_course=StringVar()  
        self.var_year=StringVar()
        self.var_sem=StringVar()
        self.var_ID=StringVar()
        self.var_name=StringVar()
        self.var_div=StringVar()
        self.var_rollno=StringVar()
        self.var_gender=StringVar()
        self.var_dob=StringVar()
        self.var_email=StringVar()
        self.var_mobileno=StringVar()
        self.var_address=StringVar()

        
        # 1st  image             
        img=Image.open(r"college_images/university.jpg")
        img=img.resize((1365,160),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)

        img_lbl=Label(self.root,image=self.photoimg,bd=2,relief=RIDGE)
        img_lbl.place(x=0,y=0,width=1365,height=160)

        

       
        # bg image
        img_2=Image.open(r"college_images\university.jpg")
        img_2=img_2.resize((1365,790),Image.ANTIALIAS)
        self.photoimg_2=ImageTk.PhotoImage(img_2)

        bg_lbl=Label(self.root,image=self.photoimg_2,bd=2,relief=RIDGE)
        bg_lbl.place(x=0,y=160,width=1365,height=710)


        lbl_title=Label(bg_lbl,text="STUDENT MANAGEMENT SYSTEM",font=("times new roman",37,"bold"),fg="red",bg="white")
        lbl_title.place(x=0,y=0,width=1365,height=50)


        # manage_Frame
        Manage_frame=Frame(bg_lbl,bd=2,relief=RIDGE,bg="white")
        Manage_frame.place(x=15,y=55,width=1325,height=470)


        # left Frame
        DataFrameLeft=LabelFrame(Manage_frame,bd=4,padx=2,relief=RIDGE,fg="crimson",bg="white",font=("arial",12,"bold"),text="Student Information")
        DataFrameLeft.place(x=10,y=5,width=580,height=460)

        
        # Currentt course details frame
        std_label_info_frame=LabelFrame(DataFrameLeft,bd=4,padx=2,relief=RIDGE,fg="crimson",bg="white",font=("arial",12,"bold"),text="Current course details")
        std_label_info_frame.place(x=0,y=0,width=560,height=120)

        # labels and combobox
        # Department
        lbl_dep=Label(std_label_info_frame,text="Department",font=("times new roman",12,"bold"),bg="white")
        lbl_dep.grid(row=0,column=0,padx=2,sticky=W) 
        
        combo_dep=ttk.Combobox(std_label_info_frame,textvariable=self.var_dep,font=("times new roman",12,"bold"),width=17,state="readonly")
        combo_dep["value"]=("Select Department","Computer science","IT","BMS")
        combo_dep.current(0)
        combo_dep.grid(row=0,column=1,padx=2,pady=10,sticky=W)

         # course
        course_std=Label(std_label_info_frame,font=("times new roman",12,"bold"),text="Courses:",bg="white")
        course_std.grid(row=0,column=2,sticky=W,padx=2,pady=10)

        com_textcourse_std=ttk.Combobox(std_label_info_frame,textvariable=self.var_course,state="readonly",font=("times new roman",12,"bold"),width=17)

        com_textcourse_std['value']=("Select Course Year","FY","SY","TY")
        com_textcourse_std.current(0)
        com_textcourse_std.grid(row=0,column=3,sticky=W,padx=2,pady=10)

        # Academic year
        academic_year=Label(std_label_info_frame,font=("times new roman",12,"bold"),text="Academic year:",bg="white")
        academic_year.grid(row=1,column=0,sticky=W,padx=2,pady=10)

        com_text_academic_year=ttk.Combobox(std_label_info_frame,textvariable=self.var_year,state="readonly",font=("times new roman",12,"bold"),width=17)

        com_text_academic_year['value']=("Select academic Year","2020-2021")
        com_text_academic_year.current(0)
        com_text_academic_year.grid(row=1,column=1,sticky=W,padx=2,)

        # semester
        Label_Semester=Label(std_label_info_frame,font=("times new roman",12,"bold"),text="Semester:",bg="white")
        Label_Semester.grid(row=1,column=2,sticky=W,padx=2,pady=10)

        comsemester=ttk.Combobox(std_label_info_frame,textvariable=self.var_sem,state="readonly",font=("times new roman",12,"bold"),width=17)

        comsemester['value']=("Select Semester","SEM 1","SEM 2","SEM 3","SEM 4","SEM 5","SEM 6")
        comsemester.current(0)
        comsemester.grid(row=1,column=3,sticky=W,padx=2,pady=10)

        # student personal info
        std_personalinfo=LabelFrame(DataFrameLeft,bd=4,padx=2,relief=RIDGE,fg="crimson",bg="white",font=("arial",12,"bold"),text="Student Personal Info")
        std_personalinfo.place(x=0,y=130,width=560,height=230)
        
        #student id
        Label_Stdid=Label(std_personalinfo,font=("times new roman",12,"bold"),text="Student ID:",bg="white")
        Label_Stdid.grid(row=0,column=0,sticky=W,padx=2,pady=7)
        
        
        id_entry=ttk.Entry(std_personalinfo,textvariable=self.var_ID,font=("times new roman",12,"bold"),width=15)
        id_entry.grid(row=0,column=1,sticky=W,padx=2,pady=7)

        # Name
        Lbl_Name=Label(std_personalinfo,font=("times new roman",12,"bold"),text="Student Name:",bg="white")
        Lbl_Name.grid(row=0,column=2,sticky=W,padx=2,pady=7)
        
        
        txt_name=ttk.Entry(std_personalinfo,textvariable=self.var_name,font=("times new roman",12,"bold"),width=22)
        txt_name.grid(row=0,column=3,padx=2,pady=7)

        # Division
        lbl_div=Label(std_personalinfo,font=("times new roman",12,"bold"),text="Division:",bg="white")
        lbl_div.grid(row=1,column=0,sticky=W,padx=2,pady=7)

        com_txt_div=ttk.Combobox(std_personalinfo,textvariable=self.var_div,state="readonly",font=("times new roman",12,"bold"),width=15)

        com_txt_div['value']=("Select Division","A","B","C")
        com_txt_div.current(0)
        com_txt_div.grid(row=1,column=1,sticky=W,padx=2,pady=7)



        # Roll no
        Lbl_rollno=Label(std_personalinfo,font=("times new roman",12,"bold"),text="Roll no:",bg="white")
        Lbl_rollno.grid(row=1,column=2,sticky=W,padx=2,pady=7)

        txt_rollno=ttk.Entry(std_personalinfo,textvariable=self.var_rollno,font=("times new roman",12,"bold"),width=10)
        txt_rollno.grid(row=1,column=3,padx=2,pady=7)

        # gender
        lbl_gender=Label(std_personalinfo,font=("times new roman",12,"bold"),text="Gender:",bg="white")
        lbl_gender.grid(row=2,column=0,sticky=W,padx=2,pady=7)

        com_text_gender=ttk.Combobox(std_personalinfo,textvariable=self.var_gender,state="readonly",font=("times new roman",12,"bold"),width=10)

        com_text_gender['value']=("GENDER","MALE","FEMALE","OTHER")
        com_text_gender.current(0)
        com_text_gender.grid(row=2,column=1,sticky=W,padx=2,pady=7)

        # DOB
        lbl_dob=Label(std_personalinfo,font=("times new roman",12,"bold"),text="DOB:",bg="white")
        lbl_dob.grid(row=2,column=2,sticky=W,padx=2,pady=7)

        txt_dob=ttk.Entry(std_personalinfo,textvariable=self.var_dob,font=("times new roman",12,"bold"),width=22)
        txt_dob.grid(row=2,column=3,padx=2,pady=7)

        # Email
        lbl_email=Label(std_personalinfo,font=("times new roman",12,"bold"),text="Email ID:",bg="white")
        lbl_email.grid(row=3,column=0,sticky=W,padx=2,pady=7)

        txt_email=ttk.Entry(std_personalinfo,textvariable=self.var_email,font=("times new roman",12,"bold"),width=15)
        txt_email.grid(row=3,column=1,padx=2,pady=7)

        # phone no
        lbl_mobno=Label(std_personalinfo,font=("times new roman",12,"bold"),text="MOBILE NO:",bg="white")
        lbl_mobno.grid(row=3,column=2,sticky=W,padx=2,pady=7)

        txt_mobno=ttk.Entry(std_personalinfo,textvariable=self.var_mobileno,font=("times new roman",12,"bold"),width=22)
        txt_mobno.grid(row=3,column=3,padx=2,pady=7)

        # address
        lbl_add=Label(std_personalinfo,font=("times new roman",12,"bold"),text="ADDRESS",bg="white")
        lbl_add.grid(row=4,column=0,sticky=W,padx=2,pady=7)

        txt_add=ttk.Entry(std_personalinfo,textvariable=self.var_address,font=("times new roman",12,"bold"),width=20)
        txt_add.grid(row=4,column=1,padx=2,pady=7)

        # buttoButton_
        Button_frame=Frame(DataFrameLeft,bd=2,relief=RIDGE,bg="white")
        Button_frame.place(x=0,y=365,width=560,height=60)

        btn_Add=Button(Button_frame,text="Save",command=self.add_data,font=("arial",11,"bold"),width=19,bg="yellow",fg="red")
        btn_Add.grid(row=0,column=0,padx=1)


        btn_delete=Button(Button_frame,text="Delete",command=self.delete_data,font=("arial",11,"bold"),width=19,bg="yellow",fg="red")
        btn_delete.grid(row=0,column=2,padx=1)

        btn_resrt=Button(Button_frame,text="Reset",command=self.reset_data,font=("arial",11,"bold"),width=19,bg="yellow",fg="red")
        btn_resrt.grid(row=0,column=3,padx=1)

        # right frame 
        DataFrameRight=LabelFrame(Manage_frame,bd=4,padx=2,relief=RIDGE,fg="crimson",bg="white",font=("arial",12,"bold"),text="Student Information")
        DataFrameRight.place(x=600,y=5,width=720,height=480)

       

    

        # ============== student table=================

        table_frame=Frame(DataFrameRight,bd=4,relief=RIDGE)
        table_frame.place(x=0,y=0,width=700,height=450)

        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)
        self.student_table=ttk.Treeview(table_frame,column=("dep","course","year","sem","ID","name","div","rollno","gender","dob","email","mobileno","address"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("dep",text="Department")
        self.student_table.heading("course",text="Course")   
        self.student_table.heading("year",text="Academic year")
        self.student_table.heading("sem",text="Semester")
        self.student_table.heading("ID",text="Student Id")
        self.student_table.heading("name",text="Student Nmae")
        self.student_table.heading("div",text="Division")
        self.student_table.heading("rollno",text="Roll_no")
        self.student_table.heading("gender",text="Gender")
        self.student_table.heading("dob",text="DOB")
        self.student_table.heading("email",text="Email ID")
        self.student_table.heading("mobileno",text="MOBILE NO")
        self.student_table.heading("address",text="Address")

        self.student_table["show"]="headings"

        self.student_table.column("dep",width=100)
        self.student_table.column("course",width=100)
        self.student_table.column("year",width=100)
        self.student_table.column("sem",width=100)
        self.student_table.column("ID",width=100)
        self.student_table.column("name",width=100)
        self.student_table.column("div",width=100)
        self.student_table.column("rollno",width=100)
        self.student_table.column("gender",width=100)
        self.student_table.column("dob",width=100)
        self.student_table.column("email",width=100)
        self.student_table.column("mobileno",width=100)
        self.student_table.column("address",width=100)
        
        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()
       


    def add_data(self):
        if (self.var_dep.get()=="" or self.var_email.get=="" or self.var_ID.get()==""):
            messagebox.showerror("Error","All Fields Are Required")    
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="Tanmaycr7$",database="studentmns")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                                                          self.var_dep.get(),
                                                                                                          self.var_course.get(),
                                                                                                          self.var_year.get(),
                                                                                                          self.var_sem.get(),
                                                                                                          self.var_ID.get(),
                                                                                                          self.var_name.get(),
                                                                                                          self.var_div.get(),
                                                                                                          self.var_rollno.get(),
                                                                                                          self.var_gender.get(),
                                                                                                          self.var_dob.get(),
                                                                                                          self.var_email.get(),
                                                                                                          self.var_mobileno.get(),
                                                                                                          self.var_address.get()
                                                                                                        
                                                                                                          

                                                                                                         ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","Student added Succesfully!",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root) 

    #fetch data
    def fetch_data(self): 
        conn=mysql.connector.connect(host="localhost",username="root",password="Tanmaycr7$",database="studentmns")
        my_cursor=conn.cursor() 
        my_cursor.execute("select * from student")
        data=my_cursor.fetchall()
        if len(data)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("",END,values=i)
            conn.commit()
        conn.close() 

    #Get cursor
    def get_cursor(self,event=""):
        cursor_row=self.student_table.focus()
        content=self.student_table.item(cursor_row)
        data=content["values"]

        self.var_dep.set(data[0])
        self.var_course.set(data[1])
        self.var_year.set(data[2])
        self.var_sem.set(data[3])
        self.var_ID.set(data[4])
        self.var_name.set(data[5])
        self.var_div.set(data[6])
        self.var_rollno.set(data[7])
        self.var_gender.set(data[8])
        self.var_dob.set(data[9])
        self.var_email.set(data[10])
        self.var_mobileno.set(data[11])
        self.var_address.set(data[12])

    
           
    #delete
    def delete_data(self):
        if self.var_ID.get()=="":
             messagebox.showerror("Error","All Fields Are Required",parent=self.root)
        else:
            try:
                Delete=messagebox.askyesno("Delete","Are you sure you want to delete",parent=self.root)
                if Delete>0:
                    conn=mysql.connector.connect(host="localhost",username="root",password="Tanmaycr7$",database="studentmns")
                    my_cursor=conn.cursor()
                    sql="delete from student where ID=%s"
                    value=(self.var_ID.get(),)
                    my_cursor.execute(sql,value)
                else:
                    if not Delete:
                        return
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Delete","your data is deleted",parent=self.root) 
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)  

    #reset
    def reset_data(self):
        self.var_dep.set("Select Department")
        self.var_course.set("Select Course")
        self.var_year.set("Select Year")
        self.var_sem.set("Select Semester")
        self.var_ID.set("")
        self.var_name.set("")
        self.var_div.set("Select Divison")
        self.var_rollno.set("")  
        self.var_gender.set("")
        self.var_dob.set("")
        self.var_email.set("")
        self.var_mobileno.set("")
        self.var_address.set("")

   







           








       


        
 
        
       
       

        
        
      
        
        

        




if __name__ == "__main__":
    root=Tk()
    obj=Student(root)
    root.mainloop()