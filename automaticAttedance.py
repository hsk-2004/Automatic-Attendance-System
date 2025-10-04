import tkinter as tk
from tkinter import *
import os, cv2, pandas as pd, datetime, time, csv

haarcasecade_path = "haarcascade_frontalface_default.xml"
trainimagelabel_path = "TrainingImageLabel\\Trainner.yml"
studentdetail_path = "StudentDetails\\studentdetails.csv"
attendance_path = "Attendance"

def subjectChoose(text_to_speech):
    def FillAttendance():
        sub = tx.get()
        if sub == "":
            text_to_speech("Please enter the subject name!")
            return
        try:
            recognizer = cv2.face.LBPHFaceRecognizer_create()
            recognizer.read(trainimagelabel_path)
            faceCascade = cv2.CascadeClassifier(haarcasecade_path)
            
            # Load all students
            df_students = pd.read_csv(studentdetail_path)
            df_students["Present"] = 0  # 0 = absent initially

            cam = cv2.VideoCapture(0)
            font = cv2.FONT_HERSHEY_SIMPLEX
            detected_ids = set()
            start_time = time.time()
            duration = 20  # seconds

            while True:
                ret, im = cam.read()
                gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
                faces = faceCascade.detectMultiScale(gray, 1.2, 5)

                for (x, y, w, h) in faces:
                    Id, conf = recognizer.predict(gray[y:y+h, x:x+w])
                    if conf < 70:
                        name = df_students.loc[df_students["Enrollment"]==Id,"Name"].values[0]
                        df_students.loc[df_students["Enrollment"]==Id,"Present"] = 1
                        detected_ids.add(Id)
                        cv2.rectangle(im, (x,y), (x+w,y+h), (0,255,0), 4)
                        cv2.putText(im, f"{Id}-{name}", (x,y), font, 1, (255,255,0), 2)
                    else:
                        cv2.rectangle(im, (x,y), (x+w,y+h), (0,0,255), 4)
                        cv2.putText(im, "Unknown", (x,y), font,1,(0,0,255),2)

                cv2.imshow("Taking Attendance...", im)
                if cv2.waitKey(30) & 0xFF == 27 or (time.time() - start_time) > duration:
                    break

            cam.release()
            cv2.destroyAllWindows()

            # Save attendance CSV
            date = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
            path = os.path.join(attendance_path, sub)
            if not os.path.exists(path):
                os.makedirs(path)

            fileName = os.path.join(path, f"{sub}_{date}.csv")
            df_students.to_csv(fileName, index=False)

            text_to_speech(f"Attendance Filled Successfully for {sub}")

            # Show attendance table
            root = tk.Tk()
            root.title(f"Attendance of {sub}")
            root.geometry("600x400")
            root.configure(bg="#f8f9fa")
            root.resizable(0,0)

            with open(fileName) as file:
                reader = csv.reader(file)
                for r,row in enumerate(reader):
                    for c,val in enumerate(row):
                        tk.Label(root, text=val, bg="#ffffff", fg="#343a40",
                                 font=("Arial",12), relief=RIDGE, width=12, height=1).grid(row=r,column=c,padx=1,pady=1)
            root.mainloop()

        except Exception as e:
            text_to_speech("Error: "+str(e))
            cv2.destroyAllWindows()

    # Subject input window
    subject_window = tk.Tk()
    subject_window.title("Enter Subject")
    subject_window.geometry("580x320")
    subject_window.configure(bg="#f8f9fa")
    subject_window.resizable(0,0)

    tk.Label(subject_window, text="Enter Subject Name", bg="#f8f9fa", fg="#007BFF",
             font=("Arial",20,"bold")).place(x=150,y=20)
    tk.Label(subject_window, text="Subject", bg="#f8f9fa", fg="#343a40", font=("Arial",15)).place(x=50,y=100)
    tx = tk.Entry(subject_window, bg="white", fg="#343a40", font=("Arial",20), width=15)
    tx.place(x=150,y=100)

    tk.Button(subject_window, text="Fill Attendance", command=FillAttendance, bg="#28a745", fg="white",
              font=("Arial",15), width=15, height=2).place(x=150,y=170)

    subject_window.mainloop()
