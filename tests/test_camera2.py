import cv2

cap = cv2.VideoCapture('http://192.168.0.188:81/stream')

while True:
    ret, frame = cap.read()
    if not ret:
        break
    # itt mehet feldolgozás
    cv2.imshow("ESP32-CAM", frame)
    if cv2.waitKey(1) == 27:
        break

cap.release()
cv2.destroyAllWindows()
