import torch
import cv2

# YOLOv5モデルのロード
model = torch.hub.load('ultralytics/yolov5', 'yolov5s')

# カメラを開く
cap = cv2.VideoCapture(0)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        print("Failed to grab frame")
        break

    # YOLOv5による予測
    results = model(frame)

    # 'person'クラスの検出を取得 (クラスIDは0)
    detected_people = [det for det in results.xyxy[0] if int(det[5]) == 0]

    # 検出された人物の数を取得
    num_people = len(detected_people)

    # 検出された人物の周りに枠を描画
    for det in detected_people:
        x1, y1, x2, y2 = map(int, det[:4])
        cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)

    # 画像に人数を表示
    cv2.putText(frame, f'Number of people detected: {num_people}', (10, 40), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    # 画像を表示
    cv2.imshow('YOLOv5', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
