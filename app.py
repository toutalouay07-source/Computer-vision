import cv2
from ultralytics import YOLO
import os

# On charge le model YOLO
model = YOLO("yolov8n.pt")

#Ouvrir la Camera 
cap = cv2.VideoCapture(0) #0 = camera par defaut

if not cap.isOpened():
    print("❌ Caméra non détectée!")
    exit()
print("✅ Caméra active. Appuie sur 'q' pour quitter")

while True:
    ret,frame = cap.read()

    if not ret:
        print("❌ Erreur de lecture")
        break

    # Detection YOLO 
    results = model(frame, conf=0.5) # conf=0.5 : confance minimale

    # Dessiner les resultats sur le frame 
    annotated_frame = results[0].plot()

    #Afficher
    cv2.imshow("YOLO Detection - Object Detection" , annotated_frame)

    #Quitter avec 'q'

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.relase()
cv2.destroyAllWindows()
