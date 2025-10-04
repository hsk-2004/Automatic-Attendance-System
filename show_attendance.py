import tkinter as tk
from tkinter import messagebox
import pandas as pd
from glob import glob
import csv

def subjectchoose(text_to_speech):
    def calculate_attendance():
        Subject = tx.get()
        if Subject == "":
            text_to_speech("Please enter the subject name!")
            return

        filenames = glob(f"Attendance\\{Subject}\\{Subject}*.csv")
        if not filenames:
            text_to_speech(f"No attendance files found for {Subject}")
            messagebox.showwarning("No Files", f"No attendance files found for {Subject}")
            return

        # Merge all CSVs
        df_list = [pd.read_csv(f) for f in filenames]
        merged_df = df_list[0]
        for i in range(1, len(df_list)):
            merged_df = merged_df.merge(df_list[i], on=["Enrollment","Name"], how="outer")
        merged_df.fillna(0, inplace=True)

        # Count number of times student was present (sum of all session columns)
        merged_df["Attendance Count"] = merged_df.iloc[:, 2:].sum(axis=1).astype(int)

        # Only keep Enrollment, Name, Attendance Count for display
        summary_df = merged_df[["Enrollment","Name","Attendance Count"]]

        # Save summary CSV
        save_path = f"Attendance\\{Subject}\\attendance_count.csv"
        summary_df.to_csv(save_path, index=False)

        # Display summary in modern white window
        root = tk.Tk()
        root.title(f"Attendance of {Subject}")
        root.geometry("500x400")
        root.configure(bg="#f8f9fa")
        root.resizable(0,0)

        with open(save_path, newline="") as file:
            reader = csv.reader(file)
            for r,row in enumerate(reader):
                for c,val in enumerate(row):
                    tk.Label(root, text=val, bg="#ffffff", fg="#343a40",
                             font=("Arial",12), relief=tk.RIDGE, width=15, height=1).grid(row=r,column=c,padx=1,pady=1)

        root.mainloop()

    # Subject input window
    subject_window = tk.Tk()
    subject_window.title("View Attendance")
    subject_window.geometry("500x250")
    subject_window.configure(bg="#f8f9fa")
    subject_window.resizable(0,0)

    tk.Label(subject_window, text="Which Subject's Attendance?", bg="#f8f9fa",
             fg="#007BFF", font=("Arial",18,"bold")).pack(pady=20)

    tk.Label(subject_window, text="Enter Subject Name:", bg="#f8f9fa",
             fg="#343a40", font=("Arial",14)).place(x=50,y=90)
    tx = tk.Entry(subject_window, width=20, bd=3, font=("Arial",14))
    tx.place(x=220,y=90)

    tk.Button(subject_window, text="View Attendance", command=calculate_attendance,
              bg="#007BFF", fg="white", font=("Arial",14,"bold"),
              width=18, height=2).place(x=150, y=150)

    subject_window.mainloop()
