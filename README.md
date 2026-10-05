# 🎯 Real-Time Object Detection with YOLOv8

Détection d'objets en temps réel via la caméra du PC, avec affichage des boîtes de délimitation et labels. Basé sur YOLOv8 + OpenCV.

---

## 📸 Demo

> La caméra s'ouvre, détecte les objets en direct et affiche :
> - Les boîtes de délimitation colorées
> - Le nom de chaque objet (80 classes COCO)
> - Le nombre total d'objets détectés

---



| Touche | Action |
|--------|--------|
| `q` | Quitter |


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
