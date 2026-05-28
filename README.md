# Todo App — Fullstack (FastAPI + MySQL + Bootstrap 5)

## Cấu trúc

```
D:\TodoListApp\
├── backend\
│   ├── database.py   # Kết nối MySQL, session
│   ├── models.py     # SQLAlchemy model
│   ├── schemas.py    # Pydantic schemas (validate đầu vào)
│   └── main.py       # FastAPI app (CRUD endpoints)
├── frontend\
│   └── index.html    # UI + JS fetch API (Bootstrap 5 CDN)
├── requirements.txt
└── README.md
```

## Yêu cầu

- Python 3.12+
- MySQL (XAMPP hoặc standalone)

## Cài đặt & Chạy

### 1. Tạo database

```sql
CREATE DATABASE tododb;
```

### 2. Setup venv & dependencies

```powershell
python -m venv venv
.\venv\Scripts\activate
pip install -r requirements.txt
```

### 3. Sửa kết nối database

Mở `backend/database.py`, sửa `DATABASE_URL` nếu cần:

```python
# XAMPP (root, no password)
DATABASE_URL = "mysql+pymysql://root@localhost:3306/tododb"

# Có password
DATABASE_URL = "mysql+pymysql://root:password@localhost:3306/tododb"
```

### 4. Chạy backend

```powershell
cd backend
uvicorn main:app --reload --port 8000
```

API docs: http://localhost:8000/docs

### 5. Mở frontend

Mở `frontend/index.html` bằng browser (double-click hoặc Live Server).

## Tính năng

- **Thêm** công việc (có validate rỗng, quá 200 ký tự)
- **Sửa** tiêu đề inline (click vào text → Enter để lưu, Escape để huỷ)
- **Toggle** done bằng checkbox
- **Xoá** công việc
- Giao diện Bootstrap 5, responsive

## API Endpoints

| Method | Endpoint | Body | Mô tả |
|--------|----------|------|-------|
| GET | `/todos` | — | Lấy danh sách |
| POST | `/todos` | `{ "title": "..." }` | Thêm todo |
| PUT | `/todos/{id}` | `{ "title"?, "done"? }` | Sửa title / toggle done |
| DELETE | `/todos/{id}` | — | Xoá todo |

## Deploy (Railway)

```bash
# Backend: push lên Railway, add MySQL plugin, set DATABASE_URL
# Frontend: deploy static lên Railway / Vercel / Netlify
```
