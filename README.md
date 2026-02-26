# CropGuard — Indian Crop Disease Detection & Treatment

AI-powered crop disease detection system for Indian agriculture. Upload a leaf image → get instant disease diagnosis with treatment recommendations specific to the Indian market.

## 🎯 Features

- **Image-based disease detection** — CNN model (MobileNetV2) identifies diseases from leaf photos
- **Smart treatment recommendations** — Organic + chemical solutions with Indian brand names and dosage per acre
- **42 diseases & pests covered** — Rice, Wheat, Tomato, Potato, Cotton, Maize, Sugarcane
- **Prediction history** — Save and review past analyses (requires login)
- **JWT authentication** — Secure register/login system
- **Demo mode** — Works without a trained model (returns realistic sample results)

## 🛠 Tech Stack

| Layer | Technology |
|-------|-----------|
| Frontend | React 19, MUI, React Router, Axios |
| Backend | FastAPI, Motor (async MongoDB), PyJWT |
| Database | MongoDB |
| ML | PyTorch, MobileNetV2 (transfer learning) |
| Deploy | Docker, Docker Compose |

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
│   ├── Dockerfile
│   └── requirements.txt
├── Frontend/
│   ├── src/
│   │   ├── api/client.js    # Axios + JWT
│   │   ├── context/         # Auth state
│   │   ├── pages/           # Login, Register, History, DiseaseDetail
│   │   └── components/      # UI components
│   └── package.json
├── docker-compose.yml
└── README.md
```

## 🚀 Quick Start

### Prerequisites
- Node.js 18+
- Python 3.10+
- MongoDB (local or Docker)

### 1. Start MongoDB
```bash
# Option A: Docker
docker run -d -p 27017:27017 --name cropguard-mongo mongo:7

# Option B: Local install
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

### Docker (Alternative)
```bash
docker-compose up -d
```

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

### Sample Response
```json
{
  "crop_name": "Tomato",
  "disease_name": "Tomato Late Blight",
  "confidence": 92,
  "severity": "High",
  "spread_risk": "High",
  "description": "Late blight is the most destructive disease...",
  "organic_treatment": ["Spray Bordeaux mixture (1%)...", "..."],
  "chemical_treatment": ["Metalaxyl 8% + Mancozeb 64% WP (Ridomil Gold)...", "..."],
  "dosage": "Ridomil Gold: 500 g/acre in 200 litres...",
  "prevention": ["Use disease-free transplants...", "..."],
  "status": "Diseased"
}
```

## 🌾 Supported Crops & Diseases (42 Classes)

| Crop | Diseases & Pests |
|------|----------|
| Rice | Blast, Brown Spot, Bacterial Leaf Blight, Tungro |
| Wheat | Leaf Rust, Powdery Mildew, Flag Smut, Leaf Smut, Black Rust, Yellow Rust, Leaf Blight, Scab, Stem Fly, Aphid, Mite |
| Tomato | Late Blight, Early Blight, Leaf Curl Virus, Septoria |
| Potato | Late Blight, Early Blight |
| Cotton | Bacterial Blight, Leaf Curl, Anthracnose, American Bollworm, Bollworm, Pink Bollworm, Aphid, Whitefly, Mealy Bug, Thrips, Boll Rot, Red Bug, Wilt |
| Maize | Northern Leaf Blight, Common Rust, Gray Leaf Spot, Armyworm, Fall Armyworm, Ear Rot, Stem Borer |
| Sugarcane | Red Rot, Smut, Mosaic, Red Rust, Yellow Rust |

## 📊 Dataset

- **20K+ Multi-Class Crop Disease Images** (42 classes)
- Pre-split Train/Validation folders
- Trained with PyTorch MobileNetV2 transfer learning

## 📝 License

MIT
