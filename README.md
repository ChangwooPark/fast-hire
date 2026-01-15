# [FastHire: 실시간 DM 기반 구인구직 플랫폼]
FastHire는 FastAPI와 React를 활용한 현대적인 구인구직 API 서버 및 웹 서비스 프로젝트입니다. 구인자와 구직자가 게시물을 통해 연결되고, 실시간 DM(WebSocket)을 통해 직접 소통할 수 있는 기능을 제공합니다.

<br>

---

## 🛠 Tech Stack

### Backend

* **Framework** : FastAPI (Asynchronous Python Framework)

* **Database** : PostgreSQL (Scheduled)

* **ORM** : SQLAlchemy 2.0 / Alembic (Migration)

* **Auth** : JWT (JSON Web Token)

### Frontend
* **Framework** : React (Vite + SWC)

* **Language** : TypeScript

* **Styling** : Tailwind CSS

<br>

---
## 📂 Project Structure

```bash
fast-hire/
├── backend/          # FastAPI 서버
│   ├── .venv/        # 가상환경
│   ├── main.py       # 진입점 및 CORS 설정
│   └── requirements.txt
└── frontend/         # React 클라이언트
    ├── src/          # 소스 코드
    ├── public/       # 정적 자산
    └── tailwind.config.js

```

<br>

---

## 📋 Features (Roadmap)
* [ ] **Auth** : 구인자/구직자 회원가입 및 JWT 기반 로그인

* [ ] **Job Board** : 구인 게시물 CRUD (작성, 조회, 수정, 삭제)

* [ ] **Real-time DM** : WebSocket을 활용한 1:1 채팅 기능

* [ ] **Profile** : 사용자 프로필 관리 및 이력서 업로드

<br>

---
## 🏃 Getting Started

1. Backend Setup
```bash
cd backend

# 가상환경 활성화 (Windows 기준)
.venv\Scripts\activate

# 의존성 설치
pip install -r requirements.txt

# 서버 실행
uvicorn main:app --reload
```

2. Frontend Setup
```bash
cd frontend

# 의존성 설치 (Vite 자동 설치 미수행 시)
npm install

# 개발 서버 실행
npm run dev
```

<br>

---

## Note

* 본 프로젝트는 학습 목적으로 진행되는 개인 프로젝트입니다.
* 백엔드 포트: 8000, 프론트엔드 포트: 5173