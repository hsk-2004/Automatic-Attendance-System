import tkinter as tk
from tkinter import *
from PIL import ImageTk, Image
import pyttsx3
import shutil
import os
import sys
import takeImage
import trainImage
import automaticAttedance
import show_attendance
import pandas as pd
from tkinter import messagebox

# ==================================================
# PYINSTALLER SAFE PATH FUNCTION
# ==================================================
def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS  # PyInstaller temp folder
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

# ---------------- Text to Speech ----------------
def text_to_speech(user_text):
    engine = pyttsx3.init()
    engine.say(user_text)
    engine.runAndWait()

# ---------------- Paths (DEPLOYMENT SAFE) ----------------
haarcasecade_path = resource_path("haarcascade_frontalface_default.xml")

trainimagelabel_path = os.path.join("TrainingImageLabel", "Trainner.yml")
trainimage_path = "TrainingImage"
studentdetail_path = os.path.join("StudentDetails", "studentdetails.csv")
attendance_path = "Attendance"

os.makedirs(trainimage_path, exist_ok=True)
os.makedirs(attendance_path, exist_ok=True)
os.makedirs(os.path.dirname(studentdetail_path), exist_ok=True)

# ---------------- Main Window ----------------
window = Tk()
window.title("Face Recognizer")
window.configure(bg="#f8f9fa")
window.resizable(0, 0)

width, height = 800, 600
x = (window.winfo_screenwidth() // 2) - (width // 2)
y = (window.winfo_screenheight() // 2) - (height // 2)
window.geometry(f"{width}x{height}+{x}+{y}")

# ---------------- Error Screen ----------------
def del_sc1():
    sc1.destroy()

def err_screen():
    global sc1
    sc1 = tk.Toplevel()
    sc1.geometry("400x110")
    sc1.title("Warning!!")
    sc1.configure(bg="#f8f9fa")
    sc1.resizable(0, 0)
    tk.Label(
        sc1,
        text="Enrollment & Name required!!!",
        fg="red",
        bg="#f8f9fa",
        font=("Helvetica", 14, "bold")
    ).pack(pady=10)
    tk.Button(
        sc1,
        text="OK",
        command=del_sc1,
        fg="white",
        bg="#007BFF",
        width=10,
        font=("Helvetica", 12, "bold")
    ).pack(pady=5)

def testVal(inStr, acttyp):
    if acttyp == "1":
        return inStr.isdigit()
    return True

# ---------------- Title & Logo ----------------
logo = Image.open(resource_path("UI_Image/0001.png")).resize((50, 47), Image.LANCZOS)
logo1 = ImageTk.PhotoImage(logo)
tk.Label(window, image=logo1, bg="#f8f9fa").place(relx=0.5, y=10, anchor="n")

tk.Label(
    window,
    text="BML MUNJAL UNIVERSITY",
    bg="#f8f9fa",
    fg="#343a40",
    font=("Helvetica", 28, "bold")
).place(relx=0.5, y=70, anchor="n")

tk.Label(
    window,
    text="Welcome to BML Attendance System",
    bg="#f8f9fa",
    fg="#495057",
    font=("Helvetica", 24, "bold")
).place(relx=0.5, y=120, anchor="n")

# ---------------- Images for Buttons ----------------
r_img = ImageTk.PhotoImage(
    Image.open(resource_path("UI_Image/register.png")).resize((150, 150))
)
a_img = ImageTk.PhotoImage(
    Image.open(resource_path("UI_Image/attendance.png")).resize((150, 150))
)
v_img = ImageTk.PhotoImage(
    Image.open(resource_path("UI_Image/verifyy.png")).resize((150, 150))
)

Label(window, image=r_img, bg="#f8f9fa").place(x=50, y=200)
Label(window, image=a_img, bg="#f8f9fa").place(x=600, y=200)
Label(window, image=v_img, bg="#f8f9fa").place(x=325, y=200)

# ---------------- Register / Take Image ----------------
def TakeImageUI():
    ImageUI = Tk()
    ImageUI.title("Register Student")
    ImageUI.geometry("700x400")
    ImageUI.configure(bg="#f8f9fa")
    ImageUI.resizable(0, 0)

    tk.Label(
        ImageUI,
        text="Register Your Face",
        bg="#f8f9fa",
        fg="#007BFF",
        font=("Helvetica", 22, "bold")
    ).pack(pady=10)

    tk.Label(
        ImageUI,
        text="Enter the details",
        bg="#f8f9fa",
        fg="#495057",
        font=("Helvetica", 18, "bold")
    ).place(x=230, y=50)

    tk.Label(ImageUI, text="Enrollment No", bg="#f8f9fa").place(x=50, y=120)
    txt1 = tk.Entry(ImageUI, width=18, bd=3, font=("Helvetica", 14))
    txt1.place(x=220, y=120)

    tk.Label(ImageUI, text="Name", bg="#f8f9fa").place(x=50, y=180)
    txt2 = tk.Entry(ImageUI, width=18, bd=3, font=("Helvetica", 14))
    txt2.place(x=220, y=180)

    message = tk.Label(ImageUI, text="", bg="#f8f9fa", fg="#007BFF")
    message.place(x=220, y=240)

    def take_image():
        takeImage.TakeImage(
            txt1.get(),
            txt2.get(),
            haarcasecade_path,
            trainimage_path,
            message,
            err_screen,
            text_to_speech
        )
        txt1.delete(0, END)
        txt2.delete(0, END)

    def train_image():
        trainImage.TrainImage(
            haarcasecade_path,
            trainimage_path,
            trainimagelabel_path,
            message,
            text_to_speech
        )

    tk.Button(ImageUI, text="Take Image", command=take_image,
              bg="#007BFF", fg="white",
              font=("Helvetica", 14, "bold"), width=15).place(x=100, y=300)

    tk.Button(ImageUI, text="Train Image", command=train_image,
              bg="#28a745", fg="white",
              font=("Helvetica", 14, "bold"), width=15).place(x=350, y=300)

# ---------------- Automatic Attendance ----------------
def automatic_attedance():
    automaticAttedance.subjectChoose(text_to_speech)

# ---------------- View Attendance ----------------
def view_attendance():
    show_attendance.subjectchoose(text_to_speech)

# ---------------- Delete Student ----------------
def delete_student_ui():
    delete_window = tk.Toplevel()
    delete_window.title("Delete Student")
    delete_window.geometry("500x250")
    delete_window.configure(bg="#f8f9fa")
    delete_window.resizable(0, 0)

    tk.Label(delete_window, text="Delete a Registered Student",
             bg="#f8f9fa", fg="#007BFF",
             font=("Helvetica", 18, "bold")).pack(pady=20)

    tk.Label(delete_window, text="Enter Enrollment Number:",
             bg="#f8f9fa", fg="#343a40",
             font=("Helvetica", 14)).place(x=50, y=90)

    er_entry = tk.Entry(delete_window, width=20, bd=3, font=("Helvetica", 14))
    er_entry.place(x=250, y=90)

    def delete_student():
        enrollment_no = er_entry.get().strip()
        if enrollment_no == "":
            text_to_speech("Please enter an enrollment number!")
            messagebox.showwarning("Input Error", "Enrollment number required!")
            return

        if os.path.exists(studentdetail_path):
            df = pd.read_csv(studentdetail_path)
            if enrollment_no in df['Enrollment'].astype(str).values:
                df = df[df['Enrollment'].astype(str) != enrollment_no]
                df.to_csv(studentdetail_path, index=False)
            else:
                messagebox.showinfo("Not Found", "Enrollment number not found!")
                return

        if os.path.exists(trainimage_path):
            for folder_name in os.listdir(trainimage_path):
                if folder_name.startswith(enrollment_no):
                    shutil.rmtree(os.path.join(trainimage_path, folder_name))
                    break

        messagebox.showinfo("Deleted", f"Student {enrollment_no} deleted successfully!")
        er_entry.delete(0, END)

    tk.Button(delete_window, text="Delete Student",
              command=delete_student,
              bg="#dc3545", fg="white",
              font=("Helvetica", 14, "bold"),
              width=18, height=2).place(x=150, y=150)

# ---------------- Buttons on Main UI ----------------
tk.Button(window, text="Register Student", command=TakeImageUI,
          bg="#007BFF", fg="white",
          font=("Helvetica", 14, "bold"),
          width=18, height=2).place(x=50, y=400)

tk.Button(window, text="Take Attendance", command=automatic_attedance,
          bg="#28a745", fg="white",
          font=("Helvetica", 14, "bold"),
          width=18, height=2).place(x=300, y=400)

tk.Button(window, text="View Attendance", command=view_attendance,
          bg="#17a2b8", fg="white",
          font=("Helvetica", 14, "bold"),
          width=18, height=2).place(x=550, y=400)

tk.Button(window, text="Delete Student", command=delete_student_ui,
          bg="#dc3545", fg="white",
          font=("Helvetica", 14, "bold"),
          width=18, height=2).place(x=300, y=500)

tk.Button(window, text="EXIT", command=window.destroy,
          bg="#6c757d", fg="white",
          font=("Helvetica", 14, "bold"),
          width=18, height=2).place(x=550, y=500)

window.mainloop()
