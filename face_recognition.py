import cv2

def wait_for_face():
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
    cap = cv2.VideoCapture(0)  # Kamerayı aç

    print("Yüz algılanana kadar bekleniyor...")

    while True:
        ret, frame = cap.read()
        if not ret:
            continue

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  # Görüntüyü gri tonlamaya çevir
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5, minSize=(50, 50))

        if len(faces) > 0:
            print("Yüz algılandı!")
            cap.release()
            cv2.destroyAllWindows()
            return True  # Yüz bulunduğunda fonksiyonu sonlandır

        cv2.imshow("Yüz Algılama", frame)
        if cv2.waitKey(1) & 0xFF == ord("q"):  # 'q' tuşuna basılırsa çık
            break

    cap.release()
    cv2.destroyAllWindows()
    return False
