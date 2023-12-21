import cv2
import numpy as np
from datetime import datetime

def capture_and_convert():
    # Öffne die Verbindung zur Webcam
    cap = cv2.VideoCapture(0)

    # Überprüfe, ob die Verbindung zur Webcam erfolgreich geöffnet wurde
    if not cap.isOpened():
        print("Fehler beim Öffnen der Webcam.")
        return

    try:
        # Erfasse ein Bild von der Webcam
        ret, frame = cap.read()

        # Überprüfe, ob das Bild erfolgreich erfasst wurde
        if not ret:
            print("Fehler beim Erfassen des Bildes.")
            return

        # Konvertiere das Bild in Schwarz-Weiß
        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Ändere die Auflösung auf 224x224 Pixel
        resized_frame = cv2.resize(gray_frame, (224, 224))

        # Erzeuge einen Zeitstempel für den Dateinamen
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

        # Speichere das Schwarz-Weiß-Bild im Ordner des Skripts mit 224x224 Pixeln
        filename = f"{timestamp}_schwarzweiss_224x224.jpg"
        cv2.imwrite(filename, resized_frame)
        print(f"Schwarz-Weiß-Bild wurde als '{filename}' gespeichert (Auflösung: 224x224 Pixel).")

    finally:
        # Schließe die Verbindung zur Webcam
        cap.release()

if __name__ == "__main__":
    capture_and_convert()

