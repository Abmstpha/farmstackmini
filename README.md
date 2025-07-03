# 🐍 FarmStack Mini - Notes Management App

Welcome to **FarmStack Mini**, a lightweight full-stack application that allows users to **log in, create, view, and delete notes** through a secure API and a friendly Streamlit UI.

---

## 🚀 Features

✅ **User Authentication** (JWT-based)  
✅ **Create Notes** (linked to logged-in user)  
✅ **View Personal Notes**  
✅ **Delete Notes** securely  
✅ **Clean and simple Streamlit UI**  
✅ **Swagger UI** for API testing  

---

## 🧠 Tech Stack

- **Backend**: FastAPI + MongoDB (ODMantic)  
- **Frontend**: Streamlit  
- **Auth**: JWT Bearer Token  
- **Database**: MongoDB Atlas  
- **Docs**: Swagger UI (`http://localhost:8000/docs`)

---

## 📁 Project Structure

```
farmstackmini/
├── fastapi/              ← Backend (FastAPI)
│   ├── app/              ← App logic (routers, models, schemas, services)
│   ├── main.py           ← App entrypoint
│   └── requirements.txt  ← Backend dependencies
├── ui/                   ← Streamlit frontend
│   └── main.py           ← Main UI file
├── Swagger UI details.pdf ← Visualized backend testing doc
└── README.md             ← This file
```

---

---

## 🔧 Setup Instructions

### 🐍 1. Backend (FastAPI)
```bash
cd fastapi
pip install -r requirements.txt
uvicorn app.main:app --reload
```

Open: [http://localhost:8000/docs](http://localhost:8000/docs)

---

### 📊 2. Frontend (Streamlit)
```bash
cd ui
streamlit run main.py
```

Open: [http://localhost:8501](http://localhost:8501)

---

## 📄 Swagger Documentation

📎 `Swagger UI details.pdf` contains the tested backend endpoints, payloads, and sample responses.

---

## 👤 Default User Credentials

```bash
Username: Abdellahi
Password: secret
```

---

## 🤝 Contributing

Feel free to fork this repo, add features (e.g., note editing, register), and open PRs.

---

## 🧠 Author

👨‍💻 [Abdellahi El Moustapha](https://github.com/Abmstpha)

