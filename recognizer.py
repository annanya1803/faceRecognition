from tkinter import*
from tkinter import ttk
from turtle import bgcolor, width
from unittest import result
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
from time import strftime
from datetime import datetime
import cv2
import os
import numpy as np




class Recognizer:
    def __init__(self,root):
        self.root=root
        self.root.geometry("15600x800+0+0")
        self.root.title("Face Recognization System")

        title_lbl= Label(self.root,text="FACE RECOGNIZATION SYSTEM",font=("times new roman",35,"bold"),bg="white",fg="red")
        title_lbl.place(x=0,y=0,width=1530,height=55)

        #image1
        img4=Image.open(r"C:\Users\ANNANYA\OneDrive\Desktop\face_recog\images\face.jpg")
        img4=img4.resize((650,700),Image.ANTIALIAS)
        self.photoimg4=ImageTk.PhotoImage(img4)
        f_lbl = Label(self.root,image=self.photoimg4)
        f_lbl.place(x=0,y=55,width=650,height=700)

        #image2
        img5=Image.open(r"C:\Users\ANNANYA\OneDrive\Desktop\face_recog\images\face2.webp")
        img5=img5.resize((950,700),Image.ANTIALIAS)
        self.photoimg5=ImageTk.PhotoImage(img5)
        f_lbl = Label(self.root,image=self.photoimg5)
        f_lbl.place(x=650,y=55,width=950,height=700)

        #button
        bt1_lbl=Button(f_lbl,text="Face Recognization",command=self.facerecog,cursor="hand2",font=("times new roman",18,"bold"),bg="black",fg="red")
        bt1_lbl.place(x=365,y=620,width=200,height=40)


    ## attendance function
    def attendance(self,i,s,r,d):
        with open("data1.csv","r+",newline="\n") as f:
            mydata=f.readlines()
            name=[]
            for p in mydata:
                entry=p.split((","))
                name.append(entry[0])
            if((i not in name) and (s not in name) and (r not in name) and (d not in name)):
                now=datetime.now()
                d1=now.strftime("%d/%m/%Y")
                dt=now.strftime("%H:%M:%S")
                f.writelines(f"\n{i},{s},{r},{d},{dt},{d1},Present")


    ## face recognization function
    def facerecog(self):
        def draw_boundary(img,classifier,scalefactor,minNeighbour,color,text,clf):
            gray_image=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            features=classifier.detectMultiScale(gray_image,scalefactor,minNeighbour)

            coordinates=[]

            for(x,y,w,h) in features:
                cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
                #image predict
                id,predict=clf.predict(gray_image[y:y+h,x:x+w])
                confidence=int((100*(1-predict/300)))

                #we have to take the data from the database
                conn=mysql.connector.connect(host="localhost",username="root",password="a1234",database="face_recog")
                mycursor=conn.cursor()

                mycursor.execute("select name from student where student_id="+str(id))
                r=mycursor.fetchone()
                r="+".join(r)

                mycursor.execute("select roll from student where student_id="+str(id))
                s=mycursor.fetchone()
                s="+".join(s)

                mycursor.execute("select Dept from student where student_id="+str(id))
                d=mycursor.fetchone()
                d="+".join(d)

                mycursor.execute("select student_id from student where student_id="+str(id))
                i=mycursor.fetchone()
                i="+".join(i)

                if confidence>77:
                    cv2.putText(img,f"StudentID:{i}",(x,y-75),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"Roll No:{s}",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"Name:{r}",(x,y-30),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"Dept:{d}",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    self.attendance(i,s,r,d)
                else:
                    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),3)
                    cv2.putText(img,"Unknown person",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                coordinates=[x,y,w,h]

            return coordinates

        def recognize(img,clf,faceCascade):
            coordinates=draw_boundary(img,faceCascade,1.1,10,(255,25,255),"face",clf)
            return img
        
        faceCascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")

        video=cv2.VideoCapture(0)

        while True:
            ret,img=video.read()
            img=recognize(img,clf,faceCascade)
            cv2.imshow("Welcome to face recognization system",img)

            if cv2.waitKey(0):
                break

            video.release()
            cv2.destroyAllWindows()




if __name__ == "__main__":
    root=Tk()
    obj=Recognizer(root)
    root.mainloop()