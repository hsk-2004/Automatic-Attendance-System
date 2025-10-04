import tkinter as tk
from tkinter import *
from PIL import ImageTk, Image
import pyttsx3
import os
import takeImage
import trainImage
import automaticAttedance
import show_attendance
import pandas as pd
from tkinter import messagebox

# ---------------- Text to Speech ----------------
def text_to_speech(user_text):
    engine = pyttsx3.init()
    engine.say(user_text)
    engine.runAndWait()

# ---------------- Paths ----------------
haarcasecade_path = "haarcascade_frontalface_default.xml"
trainimagelabel_path = "./TrainingImageLabel/Trainner.yml"
trainimage_path = "./TrainingImage"
studentdetail_path = "./StudentDetails/studentdetails.csv"
attendance_path = "Attendance"

if not os.path.exists(trainimage_path):
    os.makedirs(trainimage_path)

# ---------------- Main Window ----------------
window = Tk()
window.title("Face Recognizer")
window.geometry("800x600")
window.configure(bg="#f8f9fa")
window.resizable(0, 0)

# Center window
window.update_idletasks()
width, height = 800, 600
x = (window.winfo_screenwidth() // 2) - (width // 2)
y = (window.winfo_screenheight() // 2) - (height // 2)
window.geometry(f"{width}x{height}+{x}+{y}")

# ---------------- Error Screen ----------------
def del_sc1():
    sc1.destroy()

def err_screen():
    global sc1
    sc1 = tk.Tk()
    sc1.geometry("400x110")
    sc1.title("Warning!!")
    sc1.configure(bg="#f8f9fa")
    sc1.resizable(0, 0)
    tk.Label(sc1, text="Enrollment & Name required!!!", fg="red",
             bg="#f8f9fa", font=("Helvetica", 14, "bold")).pack(pady=10)
    tk.Button(sc1, text="OK", command=del_sc1, fg="white", bg="#007BFF",
              width=10, font=("Helvetica", 12, "bold"), relief=FLAT).pack(pady=5)

def testVal(inStr, acttyp):
    if acttyp == "1":
        return inStr.isdigit()
    return True

# ---------------- Title & Logo ----------------
logo = Image.open("UI_Image/0001.png").resize((50, 47), Image.LANCZOS)
logo1 = ImageTk.PhotoImage(logo)
l1 = tk.Label(window, image=logo1, bg="#f8f9fa")
l1.place(x=50, y=10)

tk.Label(window, text="CLASS VISION", bg="#f8f9fa", fg="#343a40",
         font=("Helvetica", 28, "bold")).place(x=120, y=10)
tk.Label(window, text="Welcome to CLASS VISION", bg="#f8f9fa", fg="#495057",
         font=("Helvetica", 24, "bold")).place(x=150, y=80)

# ---------------- Images for Buttons ----------------
ri = Image.open("UI_Image/register.png").resize((150, 150))
r_img = ImageTk.PhotoImage(ri)
Label(window, image=r_img, bg="#f8f9fa").place(x=50, y=200)

ai = Image.open("UI_Image/attendance.png").resize((150, 150))
a_img = ImageTk.PhotoImage(ai)
Label(window, image=a_img, bg="#f8f9fa").place(x=600, y=200)

vi = Image.open("UI_Image/verifyy.png").resize((150, 150))
v_img = ImageTk.PhotoImage(vi)
Label(window, image=v_img, bg="#f8f9fa").place(x=325, y=200)

# ---------------- Register / Take Image ----------------
def TakeImageUI():
    ImageUI = Tk()
    ImageUI.title("Register Student")
    ImageUI.geometry("700x400")
    ImageUI.configure(bg="#f8f9fa")
    ImageUI.resizable(0, 0)

    tk.Label(ImageUI, text="Register Your Face", bg="#f8f9fa", fg="#007BFF",
             font=("Helvetica", 22, "bold")).pack(pady=10)
    tk.Label(ImageUI, text="Enter the details", bg="#f8f9fa", fg="#495057",
             font=("Helvetica", 18, "bold")).place(x=230, y=50)

    # Enrollment
    tk.Label(ImageUI, text="Enrollment No", width=12, height=2, bg="#f8f9fa", fg="#343a40",
             font=("Helvetica", 12)).place(x=50, y=120)
    txt1 = tk.Entry(ImageUI, width=18, bd=3, font=("Helvetica", 14))
    txt1.place(x=220, y=120)

    # Name
    tk.Label(ImageUI, text="Name", width=12, height=2, bg="#f8f9fa", fg="#343a40",
             font=("Helvetica", 12)).place(x=50, y=180)
    txt2 = tk.Entry(ImageUI, width=18, bd=3, font=("Helvetica", 14))
    txt2.place(x=220, y=180)

    # Notification Label
    message = tk.Label(ImageUI, text="", bg="#f8f9fa", fg="#007BFF", font=("Helvetica", 12))
    message.place(x=220, y=240)

    # Take Image Button
    def take_image():
        l1_val = txt1.get()
        l2_val = txt2.get()
        takeImage.TakeImage(l1_val, l2_val, haarcasecade_path, trainimage_path,
                            message, err_screen, text_to_speech)
        txt1.delete(0, END)
        txt2.delete(0, END)

    tk.Button(ImageUI, text="Take Image", command=take_image, bg="#007BFF",
              fg="white", font=("Helvetica", 14, "bold"), width=15).place(x=100, y=300)

    # Train Image Button
    def train_image():
        trainImage.TrainImage(haarcasecade_path, trainimage_path, trainimagelabel_path,
                              message, text_to_speech)

    tk.Button(ImageUI, text="Train Image", command=train_image, bg="#28a745",
              fg="white", font=("Helvetica", 14, "bold"), width=15).place(x=350, y=300)

# ---------------- Automatic Attendance ----------------
def automatic_attedance():
    automaticAttedance.subjectChoose(text_to_speech)

# ---------------- View Attendance ----------------
def view_attendance():
    show_attendance.subjectchoose(text_to_speech)

# ---------------- Delete Student ----------------
def delete_student_ui():
    delete_window = tk.Tk()
    delete_window.title("Delete Student")
    delete_window.geometry("500x250")
    delete_window.configure(bg="#f8f9fa")
    delete_window.resizable(0, 0)

    tk.Label(delete_window, text="Delete a Registered Student", bg="#f8f9fa",
             fg="#007BFF", font=("Helvetica", 18, "bold")).pack(pady=20)
    tk.Label(delete_window, text="Enter Enrollment Number:", bg="#f8f9fa",
             fg="#343a40", font=("Helvetica", 14)).place(x=50, y=90)
    er_entry = tk.Entry(delete_window, width=20, bd=3, font=("Helvetica", 14))
    er_entry.place(x=250, y=90)

    def delete_student():
        enrollment_no = er_entry.get()
        if enrollment_no == "":
            text_to_speech("Please enter an enrollment number!")
            messagebox.showwarning("Input Error", "Enrollment number required!")
            return

        # Delete from CSV
        if os.path.exists(studentdetail_path):
            df = pd.read_csv(studentdetail_path)
            if enrollment_no in df['Enrollment'].astype(str).values:
                df = df[df['Enrollment'].astype(str) != enrollment_no]
                df.to_csv(studentdetail_path, index=False)
            else:
                text_to_speech("Student not found!")
                messagebox.showinfo("Not Found", "Enrollment number not found!")
                return

        # Delete student images
        student_images_folder = f"{trainimage_path}/{enrollment_no}"
        if os.path.exists(student_images_folder):
            for file in os.listdir(student_images_folder):
                os.remove(os.path.join(student_images_folder, file))
            os.rmdir(student_images_folder)

        text_to_speech(f"Student {enrollment_no} deleted successfully!")
        messagebox.showinfo("Deleted", f"Student {enrollment_no} deleted successfully!")
        er_entry.delete(0, END)

    tk.Button(delete_window, text="Delete Student", command=delete_student,
              bg="#dc3545", fg="white", font=("Helvetica", 14, "bold"),
              width=18, height=2).place(x=150, y=150)

# ---------------- Buttons on Main UI ----------------
tk.Button(window, text="Register Student", command=TakeImageUI,
          bg="#007BFF", fg="white", font=("Helvetica", 14, "bold"), width=18, height=2).place(x=50, y=400)

tk.Button(window, text="Take Attendance", command=automatic_attedance,
          bg="#28a745", fg="white", font=("Helvetica", 14, "bold"), width=18, height=2).place(x=300, y=400)

tk.Button(window, text="View Attendance", command=view_attendance,
          bg="#17a2b8", fg="white", font=("Helvetica", 14, "bold"), width=18, height=2).place(x=550, y=400)

tk.Button(window, text="Delete Student", command=delete_student_ui,
          bg="#dc3545", fg="white", font=("Helvetica", 14, "bold"), width=18, height=2).place(x=300, y=500)

tk.Button(window, text="EXIT", command=quit,
          bg="#6c757d", fg="white", font=("Helvetica", 14, "bold"), width=18, height=2).place(x=300, y=580)

window.mainloop()
