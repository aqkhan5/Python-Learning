# 🏫 EduPulse - School Record Management System

A modern, interactive, and object-oriented **School Record Management System** built in Python. EduPulse allows educational institutions to manage student registrations, teacher profiles, and academic performance through both a **stunning Streamlit Web Dashboard** and a traditional **Terminal CLI Interface**.

---

## 🌟 Key Features

- **👨‍🎓 Student Management**:
  - Register new students with automatic email validation and unique roll number checks.
  - Record and update subject grades.
  - View individual student profile cards complete with average score calculation and visual progress bars.
  - Interactive student directory with real-time subject count breakdown.

- **👩‍🏫 Faculty & Teacher Management**:
  - Register teachers with employee ID verification and subject specializations.
  - Browse full faculty profiles in a clean directory view.

- **📊 Interactive Web Dashboard**:
  - Key performance indicator (KPI) metric cards (Total Students, Total Teachers, Average System Score, Grades Recorded).
  - Student performance bar charts.
  - Live inspection and 1-click download of the JSON database.

- **🏗️ Object-Oriented Architecture (OOP)**:
  - `Person` (Abstract Base Class using Python's `abc` module) with static email validation (`validate_email`).
  - `Student` and `Teacher` classes inheriting from `Person` with clean encapsulation.

- **💾 Persistent JSON Storage**:
  - All records automatically load from and save to `school_records.json`.

---

## 📂 Project Structure

```text
School Record management System/
├── app.py                         # Streamlit Web Application UI
├── School_management_system.py    # Core OOP Models (Person, Student, Teacher) & CLI Interface
├── school_records.json            # Persistent JSON Database
├── README.md                      # Project Documentation
└── .venv/                         # Python Virtual Environment
```

---

## 🚀 Getting Started

### 1. Prerequisites
- Python 3.10+ installed on your system.

### 2. Installation & Setup

Clone or navigate to the project directory:

```bash
cd "School Record management System"
```

Activate the virtual environment (or create one):

```bash
# Create virtual environment (if not already created)
python3 -m venv .venv

# Activate virtual environment
source .venv/bin/activate

# Install required dependencies
pip install streamlit pandas
```

---

## 🖥️ Usage

### Option A: Run the Web Dashboard (Recommended)

To launch the interactive web user interface:

```bash
streamlit run app.py
```

Or using the virtual environment directly:

```bash
.venv/bin/streamlit run app.py
```

Open your browser and navigate to **`http://localhost:8501`**.

---

### Option B: Run in Terminal (CLI Mode)

To run the traditional command-line interface:

```bash
python3 School_management_system.py
```

#### Terminal Menu Options:
1. Register as Student
2. Register as Teacher
3. Add Marks (Student only)
4. Show Student Details
5. Show Teacher Details

---

## 💾 Data Schema (`school_records.json`)

The application automatically persists data in the following JSON format:

```json
{
    "students": [
        {
            "name": "Abdul Qadeer Khan",
            "age": 25,
            "email": "aq242@gmail.com",
            "roll_no": 47,
            "grades": {
                "Mathematics": 92,
                "Physics": 88
            }
        }
    ],
    "teachers": [
        {
            "name": "Dr. Sarah Conner",
            "age": 38,
            "email": "sarah@school.edu",
            "subject": "Computer Science",
            "employee_id": 501
        }
    ]
}
```

---

## 💡 Object-Oriented Design Highlights

- **Abstraction**: `Person(ABC)` defines mandatory abstract methods `get_roles()`, `register()`, and `show_details()`.
- **Inheritance**: `Student` and `Teacher` subclass `Person` and fulfill the class contract.
- **Validation**: Static method `Person.validate_email()` verifies standard email formats before saving data.

---

## 📄 License

Distributed under the MIT License. Free for educational and commercial use.
