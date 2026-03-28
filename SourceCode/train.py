from ultralytics import YOLO


model = YOLO('yolov8n.pt') 

results = model.train(
    data='data.yaml', 
    epochs=50, 
    imgsz=640, 
    device='cpu' 
)

print("Huấn luyện hoàn tất. Kết quả lưu tại thư mục runs/")
