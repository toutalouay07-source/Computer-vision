# 🎯 Real-Time Object Detection with YOLOv8

Détection d'objets en temps réel via la caméra du PC, avec affichage des boîtes de délimitation et labels. Basé sur YOLOv8 + OpenCV.

---

## 📸 Demo

> La caméra s'ouvre, détecte les objets en direct et affiche :
> - Les boîtes de délimitation colorées
> - Le nom de chaque objet (80 classes COCO)
> - Le nombre total d'objets détectés

---

## 🗂️ Structure du Projet

```
object_detection_project/
├── app.py                 # Script principal
├── requirements.txt       # Dépendances
├── models/                # Weights YOLO (auto-téléchargés)
├── utils/
│   └── detector.py        # Classe ObjectDetector
└── README.md
```

---

## ⚙️ Installation

### 1. Cloner le repo

```bash
git clone https://github.com/ton-username/object-detection-yolo.git
cd object-detection-yolo
```

### 2. Créer un environnement virtuel (recommandé)

```bash
python -m venv venv
source venv/bin/activate        # Linux / Mac
venv\Scripts\activate           # Windows
```

### 3. Installer les dépendances

```bash
pip install -r requirements.txt
```

> ⚠️ Le modèle `yolov8n.pt` (~6MB) sera téléchargé automatiquement au premier lancement.

---

## 🚀 Lancement

```bash
python app.py
```

| Touche | Action |
|--------|--------|
| `q` | Quitter |
| `ESC` | Quitter |

---

## 🧠 Modèles Disponibles

| Modèle | Taille | Vitesse | Précision |
|--------|--------|---------|-----------|
| `yolov8n.pt` | ~6MB | ⚡ Rapide | ✅ Correct |
| `yolov8s.pt` | ~22MB | 🔄 Moyen | ✅✅ Bon |
| `yolov8m.pt` | ~50MB | 🐢 Lent | ✅✅✅ Très bon |

Par défaut le projet utilise `yolov8n` (nano) — idéal pour tourner sur CPU.

---

## 📦 Dataset

Ce projet utilise les **80 classes du dataset COCO**, dont :

`person`, `car`, `bicycle`, `dog`, `cat`, `chair`, `bottle`, `laptop`, `phone`, `book`... et bien d'autres.

---

## 🛠️ Stack Technique

- **YOLOv8** — Ultralytics (modèle pré-entraîné)
- **OpenCV** — Capture caméra & affichage
- **Python 3.10+**

---

## 📁 Requirements

```
ultralytics>=8.0.0
opencv-python>=4.8.0
numpy>=1.24.0
torch>=2.0.0
```

---

## 👤 Auteur

**Louay** — Étudiant  
📍 Maroc  
🔗 [GitHub](https://github.com/toutalouay07-source)
