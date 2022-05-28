from tkinter import*
from tkinter import ttk
import tkinter
from turtle import width
from PIL import Image,ImageTk
from student import Student
import os
from train import Train
from recognizer import Recognizer
from attendance import Attendance

class Face_recog:
    def __init__(self,root):
        self.root=root
        self.root.geometry("15600x800+0+0")
        self.root.title("Face Recognition")
    
    #to put image
        #image1
        img=Image.open(r"C:\Users\ANNANYA\OneDrive\Desktop\face_recog\images\face-recognition-using-opencv.jpg")
        img=img.resize((500,150),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)

    #to put label in the window
        f_lbl = Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=500,height=150)

        #image2
        img1=Image.open(r"C:\Users\ANNANYA\OneDrive\Desktop\face_recog\images\course_4826_image.jpg")
        img1=img1.resize((500,150),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)
        f_lbl = Label(self.root,image=self.photoimg1)
        f_lbl.place(x=500,y=0,width=500,height=150)

        #image3
        img2=Image.open(r"C:\Users\ANNANYA\OneDrive\Desktop\face_recog\images\shutterstock_680761540-1.jpg")
        img2=img2.resize((550,150),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)
        f_lbl = Label(self.root,image=self.photoimg2)
        f_lbl.place(x=1000,y=0,width=550,height=150)


        #bg image
        img3=Image.open(r"C:\Users\ANNANYA\OneDrive\Desktop\face_recog\images\imagesss.jpg")
        img3=img3.resize((1530,700),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)
        b_lbl = Label(self.root,image=self.photoimg3)
        b_lbl.place(x=0,y=150,width=1530,height=700)

        title_lbl= Label(b_lbl,text="FACE RECOGNITION ATTENDANCE SYSTEM",font=("times new roman",35,"bold"),bg="white",fg="red")
        title_lbl.place(x=0,y=0,width=1530,height=45)


        #student button
        img4=Image.open(r"C:\Users\ANNANYA\OneDrive\Desktop\face_recog\images\student.jpg")
        img4=img4.resize((220,220),Image.ANTIALIAS)
        self.photoimg4=ImageTk.PhotoImage(img4)

        bt1=Button(b_lbl,image=self.photoimg4,command=self.student_details,cursor="hand2")
        bt1.place(x=300,y=100,width=220,height=220)
        bt1_lbl=Button(b_lbl,text="Student Details",command=self.student_details,cursor="hand2",font=("times new roman",15,"bold"),bg="white",fg="red")
        bt1_lbl.place(x=300,y=300,width=220,height=40)


        #face detection button
        img5=Image.open(r"C:\Users\ANNANYA\OneDrive\Desktop\face_recog\images\images.jpg")
        img5=img5.resize((220,220),Image.ANTIALIAS)
        self.photoimg5=ImageTk.PhotoImage(img5)

        bt2=Button(b_lbl,image=self.photoimg5,command=self.face_data,cursor="hand2")
        bt2.place(x=600,y=100,width=220,height=220)
        bt2_lbl=Button(b_lbl,text="Face Detect",command=self.face_data,cursor="hand2",font=("times new roman",15,"bold"),bg="white",fg="red")
        bt2_lbl.place(x=600,y=300,width=220,height=40)


        #attendance button
        img6=Image.open(r"C:\Users\ANNANYA\OneDrive\Desktop\face_recog\images\attendance.jpg")
        img6=img6.resize((220,220),Image.ANTIALIAS)
        self.photoimg6=ImageTk.PhotoImage(img6)

        bt3=Button(b_lbl,image=self.photoimg6,command=self.attend,cursor="hand2")
        bt3.place(x=900,y=100,width=220,height=220)
        bt3_lbl=Button(b_lbl,text="Attendance",command=self.attend,cursor="hand2",font=("times new roman",15,"bold"),bg="white",fg="red")
        bt3_lbl.place(x=900,y=300,width=220,height=40)


        #training data button
        img7=Image.open(r"C:\Users\ANNANYA\OneDrive\Desktop\face_recog\images\data1.jpg")
        img7=img7.resize((220,220),Image.ANTIALIAS)
        self.photoimg7=ImageTk.PhotoImage(img7)

        bt4=Button(b_lbl,image=self.photoimg7,command=self.train,cursor="hand2")
        bt4.place(x=300,y=400,width=220,height=220)
        bt4_lbl=Button(b_lbl,text="Train data",command=self.train,cursor="hand2",font=("times new roman",15,"bold"),bg="white",fg="red")
        bt4_lbl.place(x=300,y=600,width=220,height=40)

        #photos button
        img8=Image.open(r"C:\Users\ANNANYA\OneDrive\Desktop\face_recog\images\photos.jpg")
        img8=img8.resize((220,220),Image.ANTIALIAS)
        self.photoimg8=ImageTk.PhotoImage(img8)

        bt5=Button(b_lbl,image=self.photoimg8,cursor="hand2",command=self.open)
        bt5.place(x=600,y=400,width=220,height=220)
        bt5_lbl=Button(b_lbl,text="Photos",cursor="hand2",command=self.open,font=("times new roman",15,"bold"),bg="white",fg="red")
        bt5_lbl.place(x=600,y=600,width=220,height=40)


        #exit button
        img9=Image.open(r"C:\Users\ANNANYA\OneDrive\Desktop\face_recog\images\exit.jpg")
        img9=img9.resize((220,220),Image.ANTIALIAS)
        self.photoimg9=ImageTk.PhotoImage(img9)

        bt6=Button(b_lbl,image=self.photoimg9,command=self.exit,cursor="hand2")
        bt6.place(x=900,y=400,width=220,height=220)
        bt6_lbl=Button(b_lbl,text="Exit",cursor="hand2",command=self.exit,font=("times new roman",15,"bold"),bg="white",fg="red")
        bt6_lbl.place(x=900,y=600,width=220,height=40)


    # function to open images
    def open(self):
        os.startfile("data")

    # to exit
    def exit(self):
        self.exit=tkinter.messagebox.askyesno("Exit","Are you sure you want to exit",parent=self.root)
        if self.exit >0:
            self.root.destroy()
        else:
            return


    ## Functions for the buttons made

    # for student button will open the student details information window
    def student_details(self):
        self.new_window=Toplevel(self.root)
        self.st=Student(self.new_window)

    
    # for train button will open the training dataset window
    def train(self):
        self.new_window=Toplevel(self.root)
        self.st=Train(self.new_window)

    
    # for face recognizer button will open the recognizer window
    def face_data(self):
        self.new_window=Toplevel(self.root)
        self.st=Recognizer(self.new_window)

    # for attendance button will open the attendance details window
    def attend(self):
        self.new_window=Toplevel(self.root)
        self.st=Attendance(self.new_window)

    


if __name__ == "__main__":
    root=Tk()
    obj=Face_recog(root)
    root.mainloop()
