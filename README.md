# 🎓 Face Recognition Attendance Management System

> A desktop-based automated attendance system using real-time face detection and recognition, built with Python, OpenCV, and Tkinter.

---

## 📌 Overview

This project automates the process of marking student attendance using **face recognition technology**. It detects and identifies student faces via webcam in real time, matches them against a trained dataset, and logs attendance with timestamps into CSV files — eliminating the need for manual roll calls.

The system features a full-featured **Tkinter GUI**, a **MySQL database** for student records, and a **LBPH (Local Binary Patterns Histograms)** face recognizer trained using OpenCV.

---

## ✨ Features

- 👤 **Student Registration** — Add student details (name, ID, course, etc.) and capture face samples from webcam
- 🧠 **Model Training** — Train the LBPH face recognizer on collected face data with one click
- 📷 **Real-Time Face Detection** — Detect and recognize faces live using Haar Cascade classifier
- 📋 **Automated Attendance Logging** — Mark attendance automatically with date and time, saved to CSV
- 📊 **Attendance Viewer** — View, filter, and manage attendance records through the GUI
- 🗄️ **MySQL Integration** — Store and retrieve student records from a MySQL database
- 🖥️ **Desktop GUI** — Clean, image-rich Tkinter interface with navigation buttons

---

## 🛠️ Tech Stack

| Component | Technology |
|---|---|
| Language | Python 3 |
| GUI | Tkinter, ttk |
| Computer Vision | OpenCV (`cv2`) |
| Face Recognition | OpenCV LBPH Face Recognizer |
| Face Detection | Haar Cascade (`haarcascade_frontalface_default.xml`) |
| Database | MySQL via `pymysql` |
| Image Processing | Pillow (PIL) |
| Data Storage | CSV files (`Attendance.csv`) |
| Numerical Computing | NumPy |

---

## 📁 Project Structure

```
Face-Recognition-Attendence-System/
│
├── main.py                             # App entry point — main dashboard GUI
├── student.py                          # Student registration module (form + face capture)
├── train.py                            # Model training using LBPH recognizer
├── face_recognition.py                 # Real-time face detection & recognition
├── Attendance.py                       # Attendance viewer and logging module
├── extra.py                            # Utility/helper functions
│
├── haarcascade_frontalface_default.xml # OpenCV pre-trained face detection model
├── classifier.xml                      # Generated after training (LBPH model)
│
├── Attendance.csv                      # Main attendance log (auto-updated)
├── 12_07.csv                           # Sample dated attendance file
│
├── data/                               # Captured face images for training
├── images/                             # UI background and button images
├── Presentation/                       # Project presentation files
├── drawio/                             # System architecture/flow diagrams
└── ps/                                 # Additional project assets
```

---

## 🔄 How It Works

```
1. REGISTER STUDENT
   └─► Enter student details → Capture 50+ face samples via webcam → Save to /data/

2. TRAIN MODEL
   └─► Load all images from /data/ → Convert to grayscale → Train LBPH recognizer
       └─► Save model as classifier.xml

3. RECOGNIZE & MARK ATTENDANCE
   └─► Open webcam → Detect face (Haar Cascade) → Recognize face (LBPH)
       └─► Match with student DB → Log Name + ID + Date + Time → Save to CSV

4. VIEW ATTENDANCE
   └─► Load CSV → Display in table → Filter by date/student
```

---

## 🚀 Getting Started

### Prerequisites

- Python 3.8+
- MySQL Server (running locally)
- A webcam

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/rohitch2710/Face-Recognition-Attendence-System.git
   cd Face-Recognition-Attendence-System
   ```

2. **Install dependencies**
   ```bash
   pip install opencv-contrib-python pillow pymysql numpy
   ```

   > ⚠️ Use `opencv-contrib-python` (not just `opencv-python`) — it includes the LBPH face recognizer.

3. **Set up MySQL database**

   Open MySQL and create a database and table for student records:
   ```sql
   CREATE DATABASE face_attendance;
   USE face_attendance;

   CREATE TABLE students (
       id INT AUTO_INCREMENT PRIMARY KEY,
       student_id VARCHAR(20),
       name VARCHAR(100),
       course VARCHAR(100),
       year VARCHAR(10),
       division VARCHAR(10),
       gender VARCHAR(10),
       dob VARCHAR(20),
       email VARCHAR(100),
       phone VARCHAR(15),
       address TEXT,
       teacher VARCHAR(100)
   );
   ```

4. **Configure database credentials** in `student.py` and `Attendance.py`:
   ```python
   conn = pymysql.connect(
       host="localhost",
       user="your_mysql_user",       # ← update
       password="your_password",     # ← update
       database="face_attendance"
   )
   ```

5. **Create required directories**
   ```bash
   mkdir data
   ```

6. **Run the application**
   ```bash
   python main.py
   ```

---

## 📸 Usage Guide

### Step 1 — Register a Student
- Click **Student Details** on the dashboard
- Fill in the student's information (ID, name, course, etc.)
- Click **Take Photo Sample** to capture 50 face images via webcam
- Click **Save** to store the record in MySQL

### Step 2 — Train the Model
- Click **Train Data** on the dashboard
- Click the **Train Data** button in the training window
- Wait for the LBPH model to train on all captured faces
- A `classifier.xml` file will be saved automatically

### Step 3 — Mark Attendance
- Click **Face Detector** on the dashboard
- The webcam opens and begins detecting faces in real time
- Recognized students are automatically logged with timestamp into `Attendance.csv`

### Step 4 — View Attendance
- Click **Attendance** on the dashboard
- View attendance records, filter by date or student

---

## 📋 Attendance CSV Format

Each attendance log entry follows this structure:

| Field | Example |
|---|---|
| Student ID | `2021001` |
| Name | `Rohit Chaudhari` |
| Date | `12/07/2024` |
| Time | `09:32:15` |

Daily attendance files are also saved separately (e.g., `12_07.csv`).

---

## ⚙️ Key Parameters

| Parameter | File | Description |
|---|---|---|
| Face samples to capture | `student.py` | Number of face images captured per student (default: ~50) |
| Confidence threshold | `face_recognition.py` | LBPH confidence cutoff for recognizing a face |
| Database credentials | `student.py`, `Attendance.py` | MySQL host, user, password, database name |
| Image save path | `student.py` | Folder where face images are stored (default: `data/`) |
| Classifier path | `train.py` | Path to save/load `classifier.xml` |

---

## 🖥️ Dashboard Modules

| Button | Module | Description |
|---|---|---|
| 👨‍🎓 Student Details | `student.py` | Register students and capture face data |
| 📷 Face Detector | `face_recognition.py` | Run live face recognition and mark attendance |
| 📋 Attendance | `Attendance.py` | View and manage attendance records |
| 🧠 Train Data | `train.py` | Train the LBPH classifier on collected images |
| 🖼️ Photos | — | Open the `data/` folder containing captured images |
| 🚪 Exit | — | Close the application |

---

## 🤝 Contributing

Contributions are welcome! To contribute:

1. Fork the repository
2. Create your feature branch: `git checkout -b feature/YourFeature`
3. Commit your changes: `git commit -m 'Add YourFeature'`
4. Push to the branch: `git push origin feature/YourFeature`
5. Open a Pull Request

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

---

## 👨‍💻 Author

**Rohit Chaudhary**
- GitHub: [@rohitch2710](https://github.com/rohitch2710)
- Live Demo: [face-detection-attendence-system.vercel.app](https://face-detection-attendence-system.vercel.app)

---

> 💡 *Built to make attendance marking smarter, faster, and contactless.*
