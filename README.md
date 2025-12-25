To run the project:
1. Clone or download the GitHub repository.
2. Install dependencies using requirements.txt.
3. Ensure MongoDB is running locally.
4. Run the FastAPI server using Uvicorn.
5. Access Swagger documentation at http://127.0.0.1:8000/docs







# Task Management Backend API

This project is a **robust backend system for task management** built using **Python (FastAPI)** and **MongoDB (NoSQL)**.  
It implements **user authentication**, **database integration**, and **CRUD APIs for tasks**, following the given assignment guidelines.

---

## 🚀 Core Features

### 🔐 User Authentication
- User Registration
- User Login
- Authentication structure ready for JWT / session-based auth

### 🗄 Database Integration
- MongoDB (NoSQL) used to store:
  - User information
  - Task details

### 📝 Task CRUD APIs
- Create Task
- Read Tasks
- Update Task
- Delete Task

---

## 🛠 Technologies Used

- **Backend Framework:** FastAPI (Python)
- **Database:** MongoDB (NoSQL)
- **Server:** Uvicorn
- **API Documentation:** Swagger (OpenAPI)

---

## 📁 Project Structure

tasktodo1/
├── app/
│ ├── main.py
│ ├── database.py
│ ├── models.py
│ ├── auth.py
│ └── routes/
│ ├── user.py
│ └── tasks.py
├── requirements.txt
└── README.md

---

## 🔗 API Endpoints

### 🔐 Authentication
| Method | Endpoint  | Description |
|------|-----------|-------------|
| POST | `/register` | Register a new user |
| POST | `/login` | Login user |

### 📝 Tasks (CRUD)
| Method | Endpoint | Description |
|------|----------|-------------|
| POST | `/tasks` | Create a task |
| GET | `/tasks` | Get all tasks |
| PUT | `/tasks/{id}` | Update a task |
| DELETE | `/tasks/{id}` | Delete a task |

---

## ▶️ How to Run the Project

### 1️⃣ Create virtual environment
```bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
mongodb://localhost:27017
uvicorn app.main:app --reload
http://127.0.0.1:8000/docs
📦 Submission Details

✅ Complete backend source code available on GitHub

✅ NoSQL database (MongoDB) used

✅ CRUD APIs implemented as per guidelines

✅ Swagger documentation provided

👤 Author

Amit Mohanty
GitHub: https://github.com/Amit-py-create
