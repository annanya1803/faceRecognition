from tkinter import*
from tkinter import ttk
from turtle import bgcolor, width
from unittest import result
from PIL import Image,ImageTk
from tkinter import messagebox
from cv2 import DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS
import cv2
import os
import numpy as np




class Train:
    def __init__(self,root):
        self.root=root
        self.root.geometry("15600x800+0+0")
        self.root.title("Train data")

        title_lbl= Label(self.root,text="TRAINING DATA SET",font=("times new roman",35,"bold"),bg="white",fg="red")
        title_lbl.place(x=0,y=0,width=1530,height=45)

        #image1
        img4=Image.open(r"C:\Users\ANNANYA\OneDrive\Desktop\face_recog\images\course_4826_image.jpg")
        img4=img4.resize((770,325),Image.ANTIALIAS)
        self.photoimg4=ImageTk.PhotoImage(img4)
        f_lbl = Label(self.root,image=self.photoimg4)
        f_lbl.place(x=0,y=45,width=770,height=345)

        #image2
        img5=Image.open(r"C:\Users\ANNANYA\OneDrive\Desktop\face_recog\images\images.jpg")
        img5=img5.resize((770,325),Image.ANTIALIAS)
        self.photoimg5=ImageTk.PhotoImage(img5)
        f_lbl = Label(self.root,image=self.photoimg5)
        f_lbl.place(x=770,y=45,width=770,height=345)

        #button
        bt1_lbl=Button(self.root,text="Train data",command=self.train_classifier,cursor="hand2",font=("times new roman",40,"bold"),bg="white",fg="red")
        bt1_lbl.place(x=0,y=350,width=1530,height=100)

        #background/bottom image
        imgbg=Image.open(r"C:\Users\ANNANYA\OneDrive\Desktop\face_recog\images\imagesss.jpg")
        imgbg=imgbg.resize((1530,325),Image.ANTIALIAS)
        self.photoimgbg=ImageTk.PhotoImage(imgbg)
        f_lbl = Label(self.root,image=self.photoimgbg)
        f_lbl.place(x=0,y=440,width=1530,height=370)

        ## use LOCAL BINARY PATTERN HISTOGRAMS algorithm to train the data
        #function to train
    def train_classifier(self):
        datadir=("data")
        path= [os.path.join(datadir,file) for file in os.listdir(datadir)]


        faces=[]
        ids=[]

        for image in path:
            img=Image.open(image).convert('L') # gray scale image
            imgnp=np.array(img,'uint8')
            id=int(os.path.split(image)[1].split('.')[1])

            faces.append(imgnp)
            ids.append(id)
            cv2.imshow("Training",imgnp)
            cv2.waitKey(1)==13
        ids=np.array(ids)

        ## train the classifier and will then save it
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces,ids)
        #to write in a file
        clf.write("classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Result","Training datsets completed",parent=self.root)


if __name__ == "__main__":
    root=Tk()
    obj=Train(root)
    root.mainloop()