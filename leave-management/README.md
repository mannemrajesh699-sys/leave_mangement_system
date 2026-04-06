# Leave Management System

A full-stack Leave Management System that allows employees to apply for leave and managers to approve or reject requests. This project is designed to automate leave tracking and reduce manual work in organizations.

---

## 🚀 Features

* Employee leave application
* Manager approval / rejection system
* Leave status tracking
* REST API integration
* Simple and clean UI
* Database-driven system

---

## 🧱 Tech Stack

### Backend

* FastAPI
* PostgreSQL
* SQLAlchemy

### Frontend

* HTML / CSS / JavaScript (or your UI framework)

### Tools

* Git & GitHub
* pgAdmin (for database management)

---

## 📁 Project Structure

```
leave_management_system/
│
├── backend/
│   ├── main.py
│   ├── database.py
│   ├── models.py
│   ├── schemas.py
│   ├── crud.py
│   └── routers/
│       └── employees.py
│
├── frontend/
│   ├── index.html
│   ├── script.js
│   └── style.css
│
└── README.md
```

---

## ⚙️ Installation & Setup

### 1. Clone the Repository

```bash
git clone https://github.com/mannemrajesh699-sys/leave_mangement_system.git
cd leave_mangement_system
```

### 2. Create Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate   # Windows
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Database

Update your `database.py`:

```python
DATABASE_URL = "postgresql://username:password@localhost/db_name"
```

---

### 5. Run Backend Server

```bash
uvicorn main:app --reload
```


---

### 6. Run Frontend

Open `index.html` in browser
OR use Live Server (VS Code)

---

## 📡 API Endpoints

| Method | Endpoint    | Description          |
| ------ | ----------- | -------------------- |
| POST   | /employees/ | Create employee      |
| GET    | /employees/ | Get all employees    |
| POST   | /leave/     | Apply leave          |
| GET    | /leave/     | Get leave requests   |
| PUT    | /leave/{id} | Approve/Reject leave |

---

## 🧠 How It Works

* Employee submits leave request
* Request is stored in database
* Manager reviews request
* Status updated (Approved / Rejected)

Leave management systems typically automate workflows like applications and approvals to reduce manual tracking and improve efficiency. ([GitHub][1])

---

## 🧪 Future Improvements

* Authentication (JWT)
* Role-based access (Admin / Employee)
* Dashboard with analytics
* Email notifications
* Leave balance tracking

---

## 🤝 Contributing

Pull requests are welcome. For major changes, open an issue first.

---

## 📜 License

This project is open-source and available under the MIT License.

---

## 👨‍💻 Author

Rajesh Mannem
GitHub: https://github.com/mannemrajesh699-sys

[1]: https://github.com/NehaW4/Employee-Leave-Management-System-PHP?utm_source=chatgpt.com "NehaW4/Employee-Leave-Management-System-PHP"

API will run at:

```
http://localhost:8501/

```