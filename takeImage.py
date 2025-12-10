import csv
import os, cv2
import numpy as np
import pandas as pd
import datetime
import time


# take Image of user
def TakeImage(l1, l2, haarcasecade_path, trainimage_path, message, err_screen, text_to_speech):
    if (l1 == "") and (l2 == ""):
        t = 'Please Enter your Enrollment Number and Name.'
        text_to_speech(t)
    elif l1 == '':
        t = 'Please Enter your Enrollment Number.'
        text_to_speech(t)
    elif l2 == "":
        t = 'Please Enter your Name.'
        text_to_speech(t)
    else:
        try:
            cam = cv2.VideoCapture(0)
            detector = cv2.CascadeClassifier(haarcasecade_path)
            Enrollment = l1
            Name = l2
            sampleNum = 0

            directory = Enrollment + "_" + Name
            path = os.path.join(trainimage_path, directory)
            os.mkdir(path)

            while True:
                ret, img = cam.read()
                gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                faces = detector.detectMultiScale(gray, 1.3, 5)

                for (x, y, w, h) in faces:
                    face = gray[y:y+h, x:x+w]

                    # -----------------------------
                    # 🧠 DIP PREPROCESSING STEPS
                    # -----------------------------

                    # 1. Histogram Equalization (Contrast Enhancement)
                    face = cv2.equalizeHist(face)

                    # 2. Gaussian Blur (Noise Reduction)
                    face = cv2.GaussianBlur(face, (3, 3), 0)

                    # 3. Normalization (Pixel Intensity Scaling)
                    face = cv2.normalize(face, None, 0, 255, cv2.NORM_MINMAX)

                    # 4. (Optional) Edge Detection for visualization
                    edges = cv2.Canny(face, 100, 200)

                    # Increment counter and save enhanced image
                    sampleNum += 1
                    filename = os.path.join(path, f"{Name}_{Enrollment}_{sampleNum}.jpg")
                    cv2.imwrite(filename, face)

                    # Draw rectangle and display processed frame
                    cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
                    cv2.imshow("Captured Image", img)
                    # cv2.imshow("Enhanced Face", edges)  # Uncomment if you want to visualize

                if cv2.waitKey(1) & 0xFF == ord("q"):
                    break
                elif sampleNum > 50:
                    break

            cam.release()
            cv2.destroyAllWindows()

            # Save student details in CSV
            row = [Enrollment, Name]
            with open("StudentDetails/studentdetails.csv", "a+", newline='') as csvFile:
                writer = csv.writer(csvFile, delimiter=",")
                writer.writerow(row)

            res = f"Images Saved and Enhanced for ER No: {Enrollment} Name: {Name}"
            message.configure(text=res)
            text_to_speech(res)

        except FileExistsError:
            t = "Student Data already exists."
            text_to_speech(t)
