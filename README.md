# faceRecognition
This is a face recognition web based application project. It detects the students face and mark their attendance using python and it's libraries.
I have used tkinter for the GUI application , used ttk for more themed and stylish features.
I have created the main web page having 6 buttons i.e student details,train data,photos,face detect,attendance and exit.
From the student details buttons one can jump to the page where we can insert student data in the database using mysql library. I have used mysql workbench for creating the databse and the tables.
All the data types of the columns are varchar in the table.
In the students details system page one can update , delete and reset students data.
For taking photo sample for a student one has to click on the update button and then the take photo sample button , the webcam will automatically open and will take 100 photos of the person.
I have imported cv2 and used haarcascade_frontalface_default.xml for face detection where we have to crop our images , we will crop the images to a rectangle.
I have converted the images to gray scale and have used detectmultisacle function to return boundary rectangles around the face for the face detection and will store all the image samples to a file (here my file of all the images is named as data) and whenever 100 samples is been completly taken then the camera will be released and the cv2 will destroy the window.
Now we have to train the data for training the data. I have used the LOCAL BINARY PATTERN HISTOGRAMS(LBPH) algorithm where histograms are created , will open the file having the images and convert it to gray scale image and store it in a numpy array , stored the faces and the ids in different list and now will train the faces and the ids using train function under the cv2 method LBPHFaceRecognizer_create() and stored all the trained data into an xml file.
After the data is been trained we should recognize it. I have used various approaches to compare the histograms. I have created rectanges around the gray image and have predicted the image and calculated the confidence and if the confidence is more then 77 then the student ID ,roll no ,name and department will be displayed upon the face It will recognize the image using LBPH algorithm by reading the data from the xml file and after doing that cv2 will destroy the window.
For the attendance from the face recognition a csv file is created where the student ID,roll no,name,department,time ,date and whether the student is present or absent is stored. The csv file works afetr the face is been recognized.
In the attendance button one has to import the csv of the data and the attendance details section shows the status of the student with all the information. We can reset the attendance details with the help of reset button in the attendance page.
From the exit button either you can exit the application or remain on the same page.
