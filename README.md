# CropGuard — Indian Crop Disease Detection & Treatment

AI-powered crop disease detection system for Indian agriculture. Upload a leaf image → get instant disease diagnosis with treatment recommendations specific to the Indian market.

## 🎯 Features

- **Image-based disease detection** — CNN model identifies diseases from leaf photos
- **Smart treatment recommendations** — Organic + chemical solutions with Indian brand names and dosage per acre
- **Prediction history** — Save and review past analyses (requires login)
- **JWT authentication** — Secure register/login system
- **Demo mode** — Works with a trained model 

## 🛠 Tech Stack

| Layer | Technology |
|-------|-----------|
| Frontend | React 19, MUI, React Router, Axios |
| Backend | FastAPI, Motor (async MongoDB), PyJWT |
| Database | MongoDB |
| ML | PyTorch, MobileNetV2 (transfer learning) |

## 📁 Project Structure

```
CropGuard AI/
├── Server/
│   ├── app/
│   │   ├── main.py          # FastAPI entry
│   │   ├── config.py        # Environment config
│   │   ├── database.py      # MongoDB connection
│   │   ├── auth.py          # JWT + bcrypt
│   │   ├── models.py        # Pydantic schemas
│   │   ├── routes/          # API endpoints
│   │   └── services/        # ML inference + disease data
│   ├── model/               # Trained model files
│   └── requirements.txt
├── Frontend/
│   ├── src/
│   │   ├── api/client.js    # Axios + JWT
│   │   ├── context/         # Auth state
│   │   ├── pages/           # Login, Register, History, DiseaseDetail
│   │   └── components/      # UI components
│   └── package.json
└── README.md
```

## 🚀 Quick Start

### Prerequisites
- Node.js 18+
- Python 3.10+
- MongoDB (local)

### 1. Start MongoDB
```bash
# Option A: Local install
mongod --dbpath /data/db
```

### 2. Start Backend
```bash
cd Server
pip install -r requirements.txt
uvicorn app.main:app --reload --port 8000
```

### 3. Start Frontend
```bash
cd Frontend
npm install
npm run dev
```

Open http://localhost:5173 in your browser.


## 📡 API Endpoints

| Method | Endpoint | Auth | Description |
|--------|----------|------|-------------|
| GET | `/` | — | Health check |
| POST | `/api/register` | — | Create account |
| POST | `/api/login` | — | Get JWT token |
| POST | `/api/predict` | Optional | Upload image → disease prediction |
| GET | `/api/history` | Required | User's prediction history |
| GET | `/api/diseases` | — | List all diseases |
| GET | `/api/diseases/{key}` | — | Disease detail |
| GET | `/api/crops` | — | List supported crops |

### Sample Request — Predict
```bash
curl -X POST http://localhost:8000/api/predict \
  -H "Authorization: Bearer <token>" \
  -F "file=@leaf_photo.jpg"
```

## 📊 Dataset

- **20K+ Multi-Class Crop Disease Images** (42 classes)
- Pre-split Train/Validation folders
- Trained with PyTorch MobileNetV2 transfer learning
