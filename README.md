🎓 Attendance Management System Using Face Recognition

A desktop-based attendance management system that uses face recognition to automatically mark attendance.
Built with Python, OpenCV, and Tkinter, this project eliminates manual attendance, reduces proxy attendance, and improves accuracy.

📌 About the Project

This project automates the traditional attendance process by recognizing faces in real time using a webcam.
Students are registered by capturing facial images, which are then trained using the LBPH (Local Binary Pattern Histogram) algorithm.
During attendance, faces are detected and matched with trained data, and attendance is recorded automatically.

The system is fully offline, easy to use, and deployed as a Windows desktop application (.exe).

✨ Features

✅ Real-time face detection and recognition

✅ Student registration with face image capture

✅ Automatic attendance marking

✅ Attendance stored securely in CSV files

✅ View attendance records from the app

✅ Delete registered students

✅ Voice feedback using text-to-speech

✅ Simple and user-friendly GUI

✅ Desktop executable deployment

🛠️ Technology Stack

Programming Language: Python

Computer Vision: OpenCV

GUI: Tkinter

Face Detection: Haar Cascade Classifier

Face Recognition Algorithm: LBPH

Text-to-Speech: pyttsx3

Data Storage: CSV files

Deployment Tool: PyInstaller

⚙️ How It Works

Register Student-

Enter enrollment number and name

Capture face images using webcam

Train Model-

Images are processed and trained using LBPH

Take Attendance-

System detects and recognizes faces in real time

Attendance is marked automatically

View Attendance-

Attendance records can be viewed subject-wise

Delete Student-

Removes student details and associated images

