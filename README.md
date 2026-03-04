<p align="center">
  <img src="frontend/src/assets/logo-larger.jpeg" alt="Sous & You" width="120" style="border-radius: 10px;"/>
</p>

<h1 align="center">Sous & You</h1>
<p align="center">AI-powered recipe assistant — solving "What should I cook?"</p>

<p align="center">
  <img src="https://img.shields.io/badge/Angular-17-DD0031?style=flat-square&logo=angular" alt="Angular">
  <img src="https://img.shields.io/badge/Flask-Python-000?style=flat-square&logo=flask" alt="Flask">
  <img src="https://img.shields.io/badge/AWS-Cloud-FF9900?style=flat-square&logo=amazonaws" alt="AWS">
  <img src="https://img.shields.io/badge/Redis-Cache-DC382D?style=flat-square&logo=redis" alt="Redis">
</p>

---

## Overview

**Sous & You** is a conversational AI chatbot that recommends personalized recipes based on your time, dietary restrictions, skill level, available ingredients, and budget.

**How it works:**
```
User Query → Flask API → AI Search → Personalized Recipes → Chat Response
```

---

## Quick Start
```bash
# 1. Clone & setup
git clone https://github.com/CSCI-577A/SousAndYou.git
cd SousAndYou

# 2. Start Redis
docker run --name redis -p 6379:6379 -d redis

# 3. Run backend (localhost:5000)
cd backend && pip install -r requirements.txt && python3 flask_api.py

# 4. Run frontend (localhost:4200)
cd frontend && npm install && ng serve
```

---

## Project Structure
```
├── frontend/          # Angular 17 app
│   └── src/app/
│       ├── pages/     # home (chat), about (team)
│       └── shared/    # navbar
├── backend/           # Flask API + Redis
└── .github/workflows/ # CI/CD
```

---

## Tech Stack

**Frontend:** Angular 17 · TypeScript · RxJS  
**Backend:** Python · Flask · Redis  
**Cloud:** AWS (EC2, S3)  
**CI/CD:** GitHub Actions

---

## Team

| Name | Role |
|------|------|
| Alex Hunter | Backend |
| Ankita Khatri | Frontend & Deployment |
| April Dawoud | Frontend |
| Benson Li | Backend & Deployment |
| Charlotte Hausman | PM & Scrum Master |
| Emily Koch | Database |
| Mahati Malladi | Database & QA |
| Paris Acosta | Backend & Database |
| Shweta Sankaranarayanan | Frontend & QA |

---

<p align="center"><sub>USC CSCI-577A · Spring 2025</sub></p>
