import cv2
from ultralytics import YOLO

model = YOLO('best.pt')

cap = cv2.VideoCapture(0)

print("Đang khởi động mắt thần... Bấm phím 'q' để thoát !")

while cap.isOpened():
    success, frame = cap.read()
    if not success:
        print("Lỗi: Không đọc được Camera!")
        break

    results = model(frame, verbose=False)

    annotated_frame = results[0].plot()

    cv2.imshow("Nhan dien Thuoc - YOLOv8", annotated_frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()