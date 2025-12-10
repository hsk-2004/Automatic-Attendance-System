import tkinter as tk
from tkinter import *
from PIL import ImageTk, Image
import pyttsx3
import shutil
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
window.geometry("600x400")
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
l1.place(relx=0.5, y=10, anchor="n")

tk.Label(window, text="BML MUNJAL UNIVERSITY", bg="#f8f9fa", fg="#343a40",
         font=("Helvetica", 28, "bold")).place(relx=0.5, y=70, anchor="n")

tk.Label(window, text="Welcome to BML Attendance System", bg="#f8f9fa", fg="#495057",
         font=("Helvetica", 24, "bold")).place(relx=0.5, y=120, anchor="n")

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

    tk.Label(ImageUI, text="Enrollment No", width=12, height=2, bg="#f8f9fa", fg="#343a40",
             font=("Helvetica", 12)).place(x=50, y=120)
    txt1 = tk.Entry(ImageUI, width=18, bd=3, font=("Helvetica", 14))
    txt1.place(x=220, y=120)

    tk.Label(ImageUI, text="Name", width=12, height=2, bg="#f8f9fa", fg="#343a40",
             font=("Helvetica", 12)).place(x=50, y=180)
    txt2 = tk.Entry(ImageUI, width=18, bd=3, font=("Helvetica", 14))
    txt2.place(x=220, y=180)

    message = tk.Label(ImageUI, text="", bg="#f8f9fa", fg="#007BFF", font=("Helvetica", 12))
    message.place(x=220, y=240)

    def take_image():
        l1_val = txt1.get()
        l2_val = txt2.get()
        takeImage.TakeImage(l1_val, l2_val, haarcasecade_path, trainimage_path,
                            message, err_screen, text_to_speech)
        txt1.delete(0, END)
        txt2.delete(0, END)

    tk.Button(ImageUI, text="Take Image", command=take_image, bg="#007BFF",
              fg="white", font=("Helvetica", 14, "bold"), width=15).place(x=100, y=300)

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
                text_to_speech("Student not found!")
                messagebox.showinfo("Not Found", "Enrollment number not found!")
                return

        if os.path.exists(trainimage_path):
            import shutil
            found = False
            for folder_name in os.listdir(trainimage_path):
                if folder_name.startswith(enrollment_no):
                    folder_path = os.path.join(trainimage_path, folder_name)
                    shutil.rmtree(folder_path)
                    found = True
                    break

        text_to_speech(f"Student {enrollment_no} deleted successfully!")
        messagebox.showinfo("Deleted", f"Student {enrollment_no} deleted successfully!")
        er_entry.delete(0, END)

    tk.Button(delete_window, text="Delete Student", command=delete_student,
              bg="#dc3545", fg="white", font=("Helvetica", 14, "bold"),
              width=18, height=2).place(x=150, y=150)

# ---------------- DIP PARAMETERS WINDOW ----------------
def show_dip_parameters():
    dip_window = tk.Tk()
    dip_window.title("Digital Image Processing Parameters & Results")
    dip_window.geometry("650x550")
    dip_window.configure(bg="#f8f9fa")
    dip_window.resizable(0, 0)

    tk.Label(
        dip_window,
        text="DIGITAL IMAGE PROCESSING - SYSTEM ANALYSIS & LIVE RESULTS",
        bg="#f8f9fa",
        fg="#007BFF",
        font=("Helvetica", 16, "bold"),
        wraplength=600,
        justify="center"
    ).pack(pady=10)

    container = tk.Frame(dip_window)
    container.pack(fill="both", expand=True)

    canvas = tk.Canvas(container, bg="#f8f9fa", highlightthickness=0)
    scrollbar = tk.Scrollbar(container, orient="vertical", command=canvas.yview)
    scroll_frame = tk.Frame(canvas, bg="#f8f9fa")

    scroll_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
    canvas.create_window((0, 0), window=scroll_frame, anchor="nw")
    canvas.configure(yscrollcommand=scrollbar.set)

    canvas.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")

    def _on_mousewheel(event):
        canvas.yview_scroll(int(-1*(event.delta/120)), "units")
    canvas.bind_all("<MouseWheel>", _on_mousewheel)

    try:
        student_df = pd.read_csv(studentdetail_path)
        total_students = len(student_df)
    except:
        total_students = 0

    total_images = 0
    if os.path.exists(trainimage_path):
        for folder in os.listdir(trainimage_path):
            folder_path = os.path.join(trainimage_path, folder)
            if os.path.isdir(folder_path):
                total_images += len(os.listdir(folder_path))

    total_attendance_files = 0
    if os.path.exists(attendance_path):
        total_attendance_files = len([f for f in os.listdir(attendance_path) if f.endswith('.csv')])

    sections = [
        ("LIVE SYSTEM STATS",
         f"• Total Registered Students: {total_students}\n"
         f"• Total Captured Images: {total_images}\n"
         f"• Total Attendance Records: {total_attendance_files}"),
        ("PROCESSING STEPS",
         "• Images are captured via webcam.\n"
         "• Preprocessed (grayscale, histogram equalization).\n"
         "• Features extracted using LBPH.\n"
         "• Model trained and saved as 'Trainner.yml'.\n"
         "• Recognition done in real-time during attendance."),
    ]

    for title, content in sections:
        tk.Label(scroll_frame, text=title, bg="#f8f9fa",
                 fg="#343a40", font=("Helvetica", 14, "bold"), anchor="w").pack(fill="x", pady=8)
        tk.Label(scroll_frame, text=content, bg="#f8f9fa",
                 fg="#495057", font=("Helvetica", 12), wraplength=600, justify="left").pack(fill="x")

    # ---------------- MODEL PERFORMANCE SECTION ----------------
    from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
    tk.Label(scroll_frame, text="MODEL PERFORMANCE (Live Evaluation)", bg="#f8f9fa",
             fg="#343a40", font=("Helvetica", 14, "bold"), anchor="w").pack(fill="x", pady=8)

    predictions_file = "./TrainingImageLabel/predictions.csv"
    if os.path.exists(predictions_file):
        try:
            pred_df = pd.read_csv(predictions_file)
            y_true = pred_df["Actual"]
            y_pred = pred_df["Predicted"]

            acc = accuracy_score(y_true, y_pred)
            prec = precision_score(y_true, y_pred, average="weighted", zero_division=0)
            rec = recall_score(y_true, y_pred, average="weighted", zero_division=0)
            f1 = f1_score(y_true, y_pred, average="weighted", zero_division=0)

            metrics_text = (
                f"• Accuracy  : {acc:.4f}\n"
                f"• Precision : {prec:.4f}\n"
                f"• Recall    : {rec:.4f}\n"
                f"• F1 Score  : {f1:.4f}"
            )
        except:
            metrics_text = "⚠ Error calculating metrics. Check predictions.csv format."
    else:
        metrics_text = "⚠ No evaluation file found — run recognition to generate predictions.csv."

    tk.Label(scroll_frame, text=metrics_text, bg="#f8f9fa",
             fg="#495057", font=("Helvetica", 12), wraplength=600, justify="left").pack(fill="x")

    tk.Button(dip_window, text="Close", command=dip_window.destroy,
              bg="#6c757d", fg="white", font=("Helvetica", 14, "bold"),
              width=15).pack(pady=10)

# ---------------- Buttons on Main UI ----------------
tk.Button(window, text="Register Student", command=TakeImageUI,
          bg="#007BFF", fg="white", font=("Helvetica", 14, "bold"), width=18, height=2).place(x=50, y=400)

tk.Button(window, text="Take Attendance", command=automatic_attedance,
          bg="#28a745", fg="white", font=("Helvetica", 14, "bold"), width=18, height=2).place(x=300, y=400)

tk.Button(window, text="View Attendance", command=view_attendance,
          bg="#17a2b8", fg="white", font=("Helvetica", 14, "bold"), width=18, height=2).place(x=550, y=400)

tk.Button(window, text="Delete Student", command=delete_student_ui,
          bg="#dc3545", fg="white", font=("Helvetica", 14, "bold"), width=18, height=2).place(x=300, y=500)

tk.Button(window, text="DIP Parameters", command=show_dip_parameters,
          bg="#ffc107", fg="black", font=("Helvetica", 14, "bold"),
          width=18, height=2).place(x=50, y=500)

tk.Button(window, text="EXIT", command=quit,
          bg="#6c757d", fg="white", font=("Helvetica", 14, "bold"),
          width=18, height=2).place(x=550, y=500)

window.mainloop()
