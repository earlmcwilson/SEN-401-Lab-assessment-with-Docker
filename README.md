# SEN-401-Lab-assessment-with-Docker

## Project Structure

```
SEN-401-Lab-assessment-with-Docker/
├── docker-compose.yml          # Orchestrates backend + frontend containers
├── .dockerignore
├── students.db                 # Seed SQLite data
├── README.md
│
├── fastapi_backend/            # Service 1: REST API
│   ├── Dockerfile
│   ├── requirements.txt
│   ├── main.py                 # FastAPI app entrypoint
│   ├── core/config.py          # Settings (DATABASE_URL, APP_NAME)
│   ├── database/db.py          # SQLAlchemy engine/session
│   ├── models/student_model.py # Student ORM model
│   ├── schemas/student_schema.py
│   ├── routers/student_router.py
│   └── services/student_service.py
│
└── main_application/           # Service 2: Web UI
    ├── Dockerfile
    ├── requirements.txt
    ├── app.py                  # Streamlit entrypoint / page navigation
    ├── pages/
    │   ├── 1_Home.py
    │   ├── 2_Dashboard.py
    │   └── 3_Student_detail.py
    └── utils/helper.py         # API client (reads API_BASE_URL from env)
```

---

## How to Run

**Requirements:** Docker Desktop (or Docker Engine + the Compose plugin)

```bash
git clone https://github.com/earlmcwilson/SEN-401-Lab-assessment-with-Docker.git
cd SEN-401-Lab-assessment-with-Docker
docker compose up --build
```

