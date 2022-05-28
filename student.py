from tkinter import*
from tkinter import ttk
from turtle import bgcolor, width
from unittest import result
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2




class Student:
    def __init__(self,root):
        self.root=root
        self.root.geometry("15600x800+0+0")
        self.root.title("Student details")

        ## variables of the column name
        self.vdept=StringVar()
        self.vcourse=StringVar()
        self.vyear=StringVar()
        self.vsem=StringVar()
        self.vstuid=StringVar()
        self.vstuname=StringVar()
        self.vdiv=StringVar()
        self.vroll=StringVar()
        self.vgender=StringVar()
        self.vdob=StringVar()
        self.vemail=StringVar()
        self.vphone=StringVar()
        self.vaddress=StringVar()
        self.vfaculty=StringVar()
        ## For photo we have radio buttons so we will add variables there only self.vphoto=StringVar()



        #image1
        img=Image.open(r"C:\Users\ANNANYA\OneDrive\Desktop\face_recog\images\student.jpg")
        img=img.resize((500,150),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)

    #to put label in the window
        f_lbl = Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=500,height=130)

        #image2
        img1=Image.open(r"C:\Users\ANNANYA\OneDrive\Desktop\face_recog\images\student1.jpg")
        img1=img1.resize((500,150),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)
        f_lbl = Label(self.root,image=self.photoimg1)
        f_lbl.place(x=500,y=0,width=500,height=130)

        #image3
        img2=Image.open(r"C:\Users\ANNANYA\OneDrive\Desktop\face_recog\images\student2.jpg")
        img2=img2.resize((550,150),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)
        f_lbl = Label(self.root,image=self.photoimg2)
        f_lbl.place(x=1000,y=0,width=550,height=130)

        #bg image
        img3=Image.open(r"C:\Users\ANNANYA\OneDrive\Desktop\face_recog\images\imagesss.jpg")
        img3=img3.resize((1530,700),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)
        b_lbl = Label(self.root,image=self.photoimg3)
        b_lbl.place(x=0,y=130,width=1530,height=700)

        title_lbl= Label(b_lbl,text="STUDENT DETAILS SYSTEM",font=("times new roman",35,"bold"),bg="white",fg="red")
        title_lbl.place(x=0,y=0,width=1530,height=40)

        #will make frame
        main_frame=Frame(b_lbl,bd=2,bg="white")
        main_frame.place(x=10,y=55,width=1500,height=650)

        #left label frame
        left_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student details",font=("times new roman",12,"bold"))
        left_frame.place(x=10,y=10,width=780,height=580)

        img4=Image.open(r"C:\Users\ANNANYA\OneDrive\Desktop\face_recog\images\student1.jpg")
        img4=img4.resize((770,130),Image.ANTIALIAS)
        self.photoimg4=ImageTk.PhotoImage(img4)
        f_lbl = Label(left_frame,image=self.photoimg4)
        f_lbl.place(x=5,y=0,width=770,height=100)

        #course frame
        cc_frame=LabelFrame(left_frame,bd=2,bg="white",relief=RIDGE,text="Current Course Information",font=("times new roman",12,"bold"))
        cc_frame.place(x=5,y=100,width=770,height=120)


        #department
        dept_lbl=Label(cc_frame,text="Department",font=("times new roman",12,"bold"),bg="white")
        dept_lbl.grid(row=0,column=0,padx=2,sticky=W)
        #combo box for department
        dept_combo=ttk.Combobox(cc_frame,textvariable=self.vdept,font=("times new roman",12,"bold"),state="readonly",width=20)
        #combo box values for department
        dept_combo["values"]=("Select your Department","Computer Science","Maths","IT","Civil","Mechanical","Social Studies")
        dept_combo.current(0)
        dept_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)


        #course
        course_lbl=Label(cc_frame,text="Course",font=("times new roman",12,"bold"),bg="white")
        course_lbl.grid(row=0,column=2,padx=2,sticky=W)
        course_combo=ttk.Combobox(cc_frame,textvariable=self.vcourse,font=("times new roman",12,"bold"),state="readonly",width=20)
        course_combo["values"]=("Select your Course","BTECH","BSC","BBA","BCom","MBA")
        course_combo.current(0)
        course_combo.grid(row=0,column=3,padx=2,pady=10,sticky=W)


        #year
        year_lbl=Label(cc_frame,text="Year",font=("times new roman",12,"bold"),bg="white")
        year_lbl.grid(row=1,column=0,padx=2,sticky=W)
        year_combo=ttk.Combobox(cc_frame,textvariable=self.vyear,font=("times new roman",12,"bold"),state="readonly",width=20)
        year_combo["values"]=("Select your Year","2020-2022","2020-2023","2020-2024","2020-2025")
        year_combo.current(0)
        year_combo.grid(row=1,column=1,padx=2,pady=10,sticky=W)

        #semester
        sem_lbl=Label(cc_frame,text="Semester",font=("times new roman",12,"bold"),bg="white")
        sem_lbl.grid(row=1,column=2,padx=2,sticky=W)
        sem_combo=ttk.Combobox(cc_frame,textvariable=self.vsem,font=("times new roman",12,"bold"),state="readonly",width=20)
        sem_combo["values"]=("Select your Semester","1","2","3","4","5","6","7","8","9","10")
        sem_combo.current(0)
        sem_combo.grid(row=1,column=3,padx=2,pady=10,sticky=W)




        #Class student information frame
        cs_frame=LabelFrame(left_frame,bd=2,bg="white",relief=RIDGE,text="Class Student Information",font=("times new roman",12,"bold"))
        cs_frame.place(x=5,y=220,width=770,height=330)

        #student id
        studentID_lbl=Label(cs_frame,text="Student Id",font=("times new roman",12,"bold"),bg="white")
        studentID_lbl.grid(row=0,column=0,padx=2,sticky=W)
        studentIDEntry=ttk.Entry(cs_frame,textvariable=self.vstuid,width=20,font=("times new roman",15,"bold"))
        studentIDEntry.grid(row=0,column=1,padx=2,sticky=W)

        #student name
        studentName_lbl=Label(cs_frame,text="Student Name",font=("times new roman",12,"bold"),bg="white")
        studentName_lbl.grid(row=0,column=2,padx=2,sticky=W)
        studentNameEntry=ttk.Entry(cs_frame,textvariable=self.vstuname,width=20,font=("times new roman",15,"bold"))
        studentNameEntry.grid(row=0,column=3,padx=2,sticky=W)

        #student Division
        studentDivision_lbl=Label(cs_frame,text="Student Division",font=("times new roman",12,"bold"),bg="white")
        studentDivision_lbl.grid(row=1,column=0,padx=2,pady=10,sticky=W)
        studentDivisionEntry=ttk.Entry(cs_frame,textvariable=self.vdiv,width=20,font=("times new roman",15,"bold"))
        studentDivisionEntry.grid(row=1,column=1,padx=2,sticky=W)

        #student roll no
        studentRoll_lbl=Label(cs_frame,text="Student Roll no",font=("times new roman",12,"bold"),bg="white")
        studentRoll_lbl.grid(row=1,column=2,padx=2,pady=10,sticky=W)
        studentRollEntry=ttk.Entry(cs_frame,textvariable=self.vroll,width=20,font=("times new roman",15,"bold"))
        studentRollEntry.grid(row=1,column=3,padx=2,sticky=W)

        #student gender
        studentGender_lbl=Label(cs_frame,text="Student Gender",font=("times new roman",12,"bold"),bg="white")
        studentGender_lbl.grid(row=2,column=0,padx=2,pady=10,sticky=W)
        studentGenderEntry=ttk.Entry(cs_frame,width=20,textvariable=self.vgender,font=("times new roman",15,"bold"))
        studentGenderEntry.grid(row=2,column=1,padx=2,sticky=W)

        #student dob
        studentDOB_lbl=Label(cs_frame,text="Student DOB",font=("times new roman",12,"bold"),bg="white")
        studentDOB_lbl.grid(row=2,column=2,padx=2,pady=10,sticky=W)
        studentDOBEntry=ttk.Entry(cs_frame,textvariable=self.vdob,width=20,font=("times new roman",15,"bold"))
        studentDOBEntry.grid(row=2,column=3,padx=2,sticky=W)

        #student email
        studentEmail_lbl=Label(cs_frame,text="Student Email",font=("times new roman",12,"bold"),bg="white")
        studentEmail_lbl.grid(row=3,column=0,padx=2,pady=10,sticky=W)
        studentEmailEntry=ttk.Entry(cs_frame,textvariable=self.vemail,width=20,font=("times new roman",15,"bold"))
        studentEmailEntry.grid(row=3,column=1,padx=2,sticky=W)

        #student phone
        studentPhone_lbl=Label(cs_frame,text="Student phone number",font=("times new roman",12,"bold"),bg="white")
        studentPhone_lbl.grid(row=3,column=2,padx=2,pady=10,sticky=W)
        studentPhoneEntry=ttk.Entry(cs_frame,textvariable=self.vphone,width=20,font=("times new roman",15,"bold"))
        studentPhoneEntry.grid(row=3,column=3,padx=2,sticky=W)

        #student address
        studentAddress_lbl=Label(cs_frame,text="Student Address",font=("times new roman",12,"bold"),bg="white")
        studentAddress_lbl.grid(row=4,column=0,padx=2,pady=10,sticky=W)
        studentAddressEntry=ttk.Entry(cs_frame,textvariable=self.vaddress,width=20,font=("times new roman",15,"bold"))
        studentAddressEntry.grid(row=4,column=1,padx=2,sticky=W)

        #student faculty
        studentFaculty_lbl=Label(cs_frame,text="Student Faculty",font=("times new roman",12,"bold"),bg="white")
        studentFaculty_lbl.grid(row=4,column=2,padx=2,pady=10,sticky=W)
        studentFacultyEntry=ttk.Entry(cs_frame,textvariable=self.vfaculty,width=20,font=("times new roman",15,"bold"))
        studentFacultyEntry.grid(row=4,column=3,padx=2,sticky=W)

        #radio buttons for photo samples
        self.vradio1=StringVar()
        radiobt1 = ttk.Radiobutton(cs_frame,variable=self.vradio1,text="Take a photo sample",value="Yes")
        radiobt1.grid(row=5,column=0)

        radiobt2 = ttk.Radiobutton(cs_frame,variable=self.vradio1,text="No photo sample",value="No")
        radiobt2.grid(row=5,column=1)



        #buttons frame
        bt_frame=Frame(cs_frame,bd=2,bg="white",relief=RIDGE)
        bt_frame.place(x=5,y=240,width=700,height=28)

        #button to save data
        save_bt=Button(bt_frame,text="Save",command=self.add,width=16,font=("times new roman",13,"bold"),bg="red",fg="white")
        save_bt.grid(row=0,column=0)

         #button to update data
        update_bt=Button(bt_frame,text="Update",command=self.update,width=16,font=("times new roman",13,"bold"),bg="red",fg="white")
        update_bt.grid(row=0,column=1)

         #button to delete data
        del_bt=Button(bt_frame,text="Delete",command=self.delete,width=16,font=("times new roman",13,"bold"),bg="red",fg="white")
        del_bt.grid(row=0,column=2)

         #button to reset data
        re_bt=Button(bt_frame,text="Reset",command=self.reset,width=18,font=("times new roman",13,"bold"),bg="red",fg="white")
        re_bt.grid(row=0,column=3)

        bt_frame1=Frame(cs_frame,bd=2,bg="white",relief=RIDGE)
        bt_frame1.place(x=5,y=275,width=700,height=25)

        #button for taking photo data
        tp_bt=Button(bt_frame1,text="Take photo sample",command=self.generate_dataset,width=69,font=("times new roman",13,"bold"),bg="red",fg="white")
        tp_bt.grid(row=1,column=0)


         #button to update photo data
        #up_bt=Button(bt_frame1,text="Update photo",width=35,font=("times new roman",13,"bold"),bg="red",fg="white")
        #up_bt.grid(row=1,column=1)


        #right label frame
        right_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student updated details",font=("times new roman",12,"bold"))
        right_frame.place(x=800,y=10,width=660,height=580)

        img5=Image.open(r"C:\Users\ANNANYA\OneDrive\Desktop\face_recog\images\student.jpg")
        img5=img5.resize((600,100),Image.ANTIALIAS)
        self.photoimg5=ImageTk.PhotoImage(img5)
        f_lbl = Label(right_frame,image=self.photoimg5)
        f_lbl.place(x=5,y=0,width=600,height=100)


        #### Table frame #####
        #table frame
        table_frame=Frame(right_frame,bd=2,bg="white",relief=RIDGE)
        table_frame.place(x=5,y=120,width=640,height=420)

        #scroll bar
        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.student_table=ttk.Treeview(table_frame,column=("dept","course","year","sem","id","name","div","roll","gender","dob","email","phone","address","faculty","photo"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("dept",text="Departmnet")
        self.student_table.heading("course",text="Course")
        self.student_table.heading("year",text="Year")
        self.student_table.heading("sem",text="Semester")
        self.student_table.heading("id",text="StudentID")
        self.student_table.heading("name",text="Name")
        self.student_table.heading("div",text="Division")
        self.student_table.heading("roll",text="Roll No")
        self.student_table.heading("gender",text="Gender")
        self.student_table.heading("dob",text="DOB")
        self.student_table.heading("email",text="Email")
        self.student_table.heading("phone",text="Phone")
        self.student_table.heading("address",text="Address")
        self.student_table.heading("faculty",text="Faculty")
        self.student_table.heading("photo",text="PhotoSample")
        self.student_table["show"]="headings"

        self.student_table.column("dept",width=100)
        self.student_table.column("course",width=100)
        self.student_table.column("year",width=100)
        self.student_table.column("sem",width=100)
        self.student_table.column("id",width=100)
        self.student_table.column("name",width=100)
        self.student_table.column("div",width=100)
        self.student_table.column("roll",width=100)
        self.student_table.column("gender",width=100)
        self.student_table.column("dob",width=100)
        self.student_table.column("email",width=100)
        self.student_table.column("phone",width=100)
        self.student_table.column("address",width=100)
        self.student_table.column("faculty",width=100)
        self.student_table.column("photo",width=100)

        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease>",self.getcursor)
        self.fetch()
        

    # for inserting data in the database
    
    # function to add the data
    def add(self):
        if self.vdept.get()=="" or self.vaddress.get()=="" or self.vcourse.get()=="" or self.vdept.get()=="" or self.vdiv.get()=="" or self.vdob.get()=="" or self.vemail.get()=="" or self.vfaculty.get()=="" or self.vgender.get()=="" or self.vphone.get()=="" or self.vradio1.get()=="" or self.vroll.get()=="" or self.vstuname.get()=="" or self.vstuid.get()=="":
            messagebox.showerror("Error","All the fields are required to be filled",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="a1234",database="face_recog")
                mycursor=conn.cursor()
                mycursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(

                            self.vdept.get(),self.vcourse.get(),self.vyear.get(),self.vsem.get(),
                            self.vstuid.get(),self.vstuname.get(),self.vdiv.get(),self.vroll.get(),
                            self.vgender.get(),self.vdob.get(),self.vemail.get(),self.vphone.get(),
                            self.vaddress.get(),self.vfaculty.get(),self.vradio1.get()
                                                    ))
                conn.commit()
                self.fetch()
                conn.close()
                messagebox.showinfo("Success","Student details have been added",parent=self.root)
            except Exception as e:
                messagebox.showerror("Error",f"Reason for exception:{str(e)}",parent=self.root)

    # to fetch the data
    def fetch(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="a1234",database="face_recog")
        mycursor=conn.cursor()
        mycursor.execute("select * from student")
        result=mycursor.fetchall()
        if len(result)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for i in result:
                self.student_table.insert("",END,values=i)
            conn.commit()
        conn.close()


    # to get the cursor
    def getcursor(self,event=""):
        focus_courser=self.student_table.focus()
        content=self.student_table.item(focus_courser)
        result=content["values"]

        self.vdept.set(result[0]),
        self.vcourse.set(result[1]),
        self.vyear.set(result[2]),
        self.vsem.set(result[3]),
        self.vstuid.set(result[4]),
        self.vstuname.set(result[5]),
        self.vdiv.set(result[6]),
        self.vroll.set(result[7]),
        self.vgender.set(result[8]),
        self.vdob.set(result[9]),
        self.vemail.set(result[10]),
        self.vphone.set(result[11]),
        self.vaddress.set(result[12]),
        self.vfaculty.set(result[13]),
        self.vradio1.set(result[14]),
        

    # to update the data
    def update(self):
        if self.vdept.get()=="" or self.vaddress.get()=="" or self.vcourse.get()=="" or self.vdept.get()=="" or self.vdiv.get()=="" or self.vdob.get()=="" or self.vemail.get()=="" or self.vfaculty.get()=="" or self.vgender.get()=="" or self.vphone.get()=="" or self.vradio1.get()=="" or self.vroll.get()=="" or self.vstuname.get()=="" or self.vstuid.get()=="":
            messagebox.showerror("Error","All the fields are required to be filled",parent=self.root)
        else:
            try:
                Updatee=messagebox.askyesno("Update","do you want to update",parent=self.root)
                if Updatee>0:
                    conn=mysql.connector.connect(host="localhost",username="root",password="a1234",database="face_recog")
                    mycursor=conn.cursor()
                    mycursor.execute("update student set Dept=%s,course=%s,year=%s,semester=%s,name=%s,division=%s,roll=%s,gender=%s,dob=%s,email=%s,phone=%s,address=%s,faculty=%s,photosample=%s where student_id=%s",(
                                                                                                                                                                                            self.vdept.get(),
                                                                                                                                                                                            self.vcourse.get(),
                                                                                                                                                                                            self.vyear.get(),
                                                                                                                                                                                            self.vsem.get(),
                                                                                                                                                                                            self.vstuname.get(),
                                                                                                                                                                                            self.vdiv.get(),
                                                                                                                                                                                            self.vroll.get(),
                                                                                                                                                                                            self.vgender.get(),
                                                                                                                                                                                            self.vdob.get(),
                                                                                                                                                                                            self.vemail.get(),
                                                                                                                                                                                            self.vphone.get(),
                                                                                                                                                                                            self.vaddress.get(),
                                                                                                                                                                                            self.vfaculty.get(),
                                                                                                                                                                                            self.vradio1.get(),
                                                                                                                                                                                            self.vstuid.get()
                                                                                                                                                                                        ))
                else:
                   if not Updatee:
                       return
                messagebox.showinfo("Success","Student details updated",parent=self.root)
                conn.commit()
                self.fetch()
                conn.close()
            except Exception as e:
                messagebox.showerror("Error",f"Reason for exception:{str(e)}",parent=self.root)


    #delete data
    def delete(self):
        if self.vstuid.get()=="":
            messagebox.showerror("Error","Student id is required to delete any record",parent=self.root)
        else:
            try:
                delete=messagebox.askyesno("Delete","do you want to delete",parent=self.root)
                if delete>0:
                    conn=mysql.connector.connect(host="localhost",username="root",password="a1234",database="face_recog")
                    mycursor=conn.cursor()
                    sql="delete from student where student_id=%s"
                    val=(self.vstuid.get(),)
                    mycursor.execute(sql,val)
                else:
                    if not delete:
                        return
                conn.commit()
                self.fetch()
                conn.close()
                messagebox.showinfo("Success","Student details deleted",parent=self.root)
            except Exception as e:
                messagebox.showerror("Error",f"Reason for exception:{str(e)}",parent=self.root)

    #reset the data
    def reset(self):
        self.vdept.set("Select Your Department")
        self.vcourse.set("Select Your Course")
        self.vyear.set("Select Your Year")
        self.vsem.set("Select Your Semester")
        self.vstuid.set("")
        self.vstuname.set("")
        self.vdiv.set("")
        self.vroll.set("")
        self.vgender.set("")
        self.vdob.set("")
        self.vemail.set("")
        self.vphone.set("")
        self.vaddress.set("")
        self.vfaculty.set("")
        self.vradio1.set("")

    # to generate the data set and to take the photo sample
    # we have to match the photo with the data of the database 
    # will update the photo of the people in the database

    def generate_dataset(self):
        if self.vdept.get()=="" or self.vaddress.get()=="" or self.vcourse.get()=="" or self.vdept.get()=="" or self.vdiv.get()=="" or self.vdob.get()=="" or self.vemail.get()=="" or self.vfaculty.get()=="" or self.vgender.get()=="" or self.vphone.get()=="" or self.vradio1.get()=="" or self.vroll.get()=="" or self.vstuname.get()=="" or self.vstuid.get()=="":
            messagebox.showerror("Error","All the fields are required to be filled",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="a1234",database="face_recog")
                mycursor=conn.cursor()
                mycursor.execute("select * from student")
                #will store all the data in a variable
                myresult=mycursor.fetchall()
                #we have to match the student id 
                id=0
                for i in myresult:
                    id+=1
                mycursor.execute("update student set Dept=%s,course=%s,year=%s,semester=%s,name=%s,division=%s,roll=%s,gender=%s,dob=%s,email=%s,phone=%s,address=%s,faculty=%s,photosample=%s where student_id=%s",(
                                                                                                                                                                                            self.vdept.get(),
                                                                                                                                                                                            self.vcourse.get(),
                                                                                                                                                                                            self.vyear.get(),
                                                                                                                                                                                            self.vsem.get(),
                                                                                                                                                                                            self.vstuname.get(),
                                                                                                                                                                                            self.vdiv.get(),
                                                                                                                                                                                            self.vroll.get(),
                                                                                                                                                                                            self.vgender.get(),
                                                                                                                                                                                            self.vdob.get(),
                                                                                                                                                                                            self.vemail.get(),
                                                                                                                                                                                            self.vphone.get(),
                                                                                                                                                                                            self.vaddress.get(),
                                                                                                                                                                                            self.vfaculty.get(),
                                                                                                                                                                                            self.vradio1.get(),
                                                                                                                                                                                            self.vstuid.get()==id+1
                                                                                                                                                                                        ))
                conn.commit()
                self.fetch()
                self.reset()
                conn.close()  

                ## we will use haarcascade algorithm
                # loading predefined data on face frontals from opencv 
                faceClassifier=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
                # we have to crop the images
                def crop(img):
                    #we have to convert the images into gray scale
                    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                    #detectMultiScale is used to return boundary rectangles for the face detected
                    faces=faceClassifier.detectMultiScale(gray,1.3,5) # by default scaling factor=1.3 and minimum neighbour =5
                    for(x,y,w,h) in faces:
                        crop=img[y:y+h,x:x+w] # the size of y will be y+h and for x is x+w
                        return crop
                # open the camera               
                cam=cv2.VideoCapture(0)  
                img_id=0
                while True:
                    ret,myframe=cam.read()
                    if crop(myframe) is not None:
                        img_id+=1
                        face=cv2.resize(crop(myframe),(450,450))
                        face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                        #to write the name of the files having different images
                        filename="data/user."+str(id)+"."+str(img_id)+".jpg"
                        cv2.imwrite(filename,face)
                        cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)
                        cv2.imshow("Cropped face is",face)

                    if cv2.waitKey(1)==13 or int(img_id)==100:
                        break
                cam.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Final","Generated Data set",parent=self.root)
            except Exception as e:
                messagebox.showerror("Error",f"Reason for exception:{str(e)}",parent=self.root)






if __name__ == "__main__":
    root=Tk()
    obj=Student(root)
    root.mainloop()