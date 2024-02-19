# YOLOv5 Real-time People Detector with Webcam
このプログラムは、YOLOv5を使用してWebカメラのリアルタイムビデオストリームから人を検出するものです。  

# 必要なパッケージをインストール
pip install -r requirements.txt  

# 実行方法
1. detect.pyを実行  
　　リアルタイムでWebカメラからの映像が表示され、検出された人の周りに緑の枠が表示されます。  
　　画面の上部には、検出された人の数が表示されます。  
2. qキーを押すことで、プログラムを終了できます。  
# コードの詳細
**torch.hub.load('ultralytics/yolov5', 'yolov5s')** : YOLOv5の小さなバージョンのモデルをロードします。  
**cv2.VideoCapture(0)**: デフォルトのカメラデバイスを開きます。  
**results = model(frame)**: フレームに対してYOLOv5モデルで検出を行います。  
**detected_people = [det for det in results.xyxy[0] if int(det[5]) == 0]**: 'person'クラスの検出を取得します。YOLOv5のクラスIDで、人はID 0になっています。  
次に、検出された人の周りに枠を描画し、画像に人数を表示します。  
**cv2.imshow('YOLOv5', frame)**: 加工されたフレームを表示します。  
**if cv2.waitKey(1) & 0xFF == ord('q')**: qキーが押されたら、ループから抜け出します。  
# 注意点
Webカメラやハードウェアの性能によっては、リアルタイムの検出のパフォーマンスが変わる可能性があります。また、YOLOv5の他のモデル（'yolov5m', 'yolov5l', 'yolov5x'など）を使用して、精度と速度のバランスを調整することもできます。
