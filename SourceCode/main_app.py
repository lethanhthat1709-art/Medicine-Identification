import cv2
import os
import tkinter as tk
from tkinter import font
from PIL import Image, ImageTk
from ultralytics import YOLO

model = YOLO('best.pt') 

class ThuocDetectionApp:
    def __init__(self, window, window_title):
        self.window = window
        self.window.title(window_title)
        
        self.window.geometry("1000x620") 
        self.window.resizable(False, False) 
        self.window.configure(bg="#1e1e1e")

        self.window.protocol("WM_DELETE_WINDOW", self.close_app)

        title_font = font.Font(family="Helvetica", size=18, weight="bold")
        btn_font = font.Font(family="Helvetica", size=12, weight="bold")
        info_font = font.Font(family="Helvetica", size=12)

        self.cap = cv2.VideoCapture(0)
        self.delay = 30
        self.img_counter = 1
        self.current_frame = None

        self.lbl_title = tk.Label(window, text="HỆ THỐNG NHẬN DIỆN THUỐC", 
                                  font=title_font, fg="#00ffcc", bg="#1e1e1e", pady=10)
        self.lbl_title.pack()

        main_frame = tk.Frame(window, bg="#1e1e1e")
        main_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)

    
        left_frame = tk.Frame(main_frame, bg="#1e1e1e")
        left_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        
        center_left = tk.Frame(left_frame, bg="#1e1e1e")
        center_left.pack(expand=True) 

        self.canvas = tk.Canvas(center_left, width=640, height=480, bg="black", highlightthickness=2, highlightbackground="#00ffcc")
        self.canvas.pack(pady=5)

        btn_frame = tk.Frame(center_left, bg="#1e1e1e")
        btn_frame.pack(pady=10)

        self.btn_capture = tk.Button(btn_frame, text="📸 CHỤP ẢNH MÀN HÌNH", font=btn_font, bg="#007acc", fg="white", 
                                     activebackground="#005999", activeforeground="white", width=22, command=self.take_snapshot)
        self.btn_capture.pack(side=tk.LEFT, padx=10)

        self.btn_quit = tk.Button(btn_frame, text="ĐÓNG ỨNG DỤNG", font=btn_font, bg="#ff3333", fg="white", 
                                  activebackground="#cc0000", activeforeground="white", width=20, command=self.close_app)
        self.btn_quit.pack(side=tk.LEFT, padx=10)

    
        
        right_frame = tk.Frame(main_frame, bg="#2d2d2d", width=320, highlightthickness=1, highlightbackground="#555555")
        right_frame.pack_propagate(False) 
        right_frame.pack(side=tk.RIGHT, fill=tk.Y, padx=(10, 0))

    
        right_content = tk.Frame(right_frame, bg="#2d2d2d")
        right_content.pack(fill=tk.BOTH, expand=True, padx=15, pady=15)

        lbl_stats_title = tk.Label(right_content, text="📊 THỐNG KÊ REALTIME", font=btn_font, fg="#00ffcc", bg="#2d2d2d")
        lbl_stats_title.pack(pady=(0, 10))

        self.lbl_stats = tk.Label(right_content, text="Đang chờ dữ liệu...", font=info_font, fg="white", bg="#2d2d2d", justify=tk.LEFT)
        self.lbl_stats.pack(anchor="w")

        tk.Frame(right_content, height=2, bg="#555555").pack(fill=tk.X, pady=20) # Vạch kẻ ngang

        lbl_warn_title = tk.Label(right_content, text="⚠️ THÔNG TIN / CẢNH BÁO", font=btn_font, fg="#ffcc00", bg="#2d2d2d")
        lbl_warn_title.pack(pady=(0, 10))

        self.lbl_warn = tk.Label(right_content, text="Chưa phát hiện thuốc.", font=info_font, fg="white", bg="#2d2d2d", justify=tk.LEFT, wraplength=280)
        self.lbl_warn.pack(anchor="w")

        
       
        self.thuoc_info = {
            "BrainForte": (
                "💊 CHỈ ĐỊNH:\n"
                "- Hỗ trợ bổ não, tăng cường tuần hoàn máu não.\n"
                "- Giảm căng thẳng, mệt mỏi, đau đầu.\n\n"
                "🔔 HƯỚNG DẪN SỬ DỤNG:\n"
                "- Người lớn: Uống 1 viên/lần, 2 lần/ngày.\n"
                "- Uống sau bữa ăn 30 phút.\n\n"
                "⚠️ CHỐNG CHỈ ĐỊNH:\n"
                "- Phụ nữ có thai, người đang xuất huyết."
            ),
            
            "Loparamide": (
                "💊 CHỈ ĐỊNH:\n"
                "- Điều trị triệu chứng tiêu chảy cấp và mạn tính.\n\n"
                "🚫 CẢNH BÁO ĐẶC BIỆT (NGUY HIỂM):\n"
                "- TUYỆT ĐỐI KHÔNG dùng cho trẻ em dưới 12 tuổi.\n"
                "- Không dùng khi bị lỵ cấp, tổn thương gan.\n\n"
                "⚠️ TÁC DỤNG PHỤ:\n"
                "- Khô miệng, buồn nôn, chóng mặt, buồn ngủ."
            ),
            
            "Sadapron300": (
                "💊 CHỈ ĐỊNH:\n"
                "- Điều trị bệnh Gout, làm giảm nồng độ axit uric trong máu.\n\n"
                "🔔 HƯỚNG DẪN SỬ DỤNG:\n"
                "- Uống 1 viên/ngày sau bữa ăn.\n"
                "- Cần uống nhiều nước (ít nhất 2 lít/ngày) trong quá trình dùng thuốc.\n\n"
                "⚠️ LƯU Ý Y TẾ:\n"
                "- Ngừng thuốc ngay và báo cho bác sĩ nếu bị phát ban, dị ứng da."
            )
        }

        self.update_frame()
        self.window.mainloop()

    def update_frame(self):
        success, frame = self.cap.read()
        
        if success:

            
            results = model(frame, conf=0.7, iou=0.45, verbose=False)
            
            annotated_frame = results[0].plot()
            self.current_frame = annotated_frame 

            
            detections = results[0].boxes.cls.cpu().tolist()
            names = results[0].names
            
            count_dict = {"BrainForte": 0, "Loparamide": 0, "Sadapron300": 0}
            detected_classes = []

            for cls_id in detections:
                class_name = names[int(cls_id)]
                if class_name in count_dict:
                    count_dict[class_name] += 1
                    detected_classes.append(class_name)

            
            stats_text = ""
            for name, count in count_dict.items():
                stats_text += f"▶ Số lượng {name}: {count} vỉ\n\n"
            self.lbl_stats.config(text=stats_text.strip())

            
            if detected_classes:
                main_drug = detected_classes[0] 
                self.lbl_warn.config(text=self.thuoc_info.get(main_drug, "Không có thông tin."))
            else:
                self.lbl_warn.config(text="Đang quét...")

            
            cv2_image = cv2.cvtColor(annotated_frame, cv2.COLOR_BGR2RGB)
            pil_image = Image.fromarray(cv2_image)
            self.photo = ImageTk.PhotoImage(image=pil_image)
            self.canvas.create_image(0, 0, image=self.photo, anchor=tk.NW)

        self.window.after(self.delay, self.update_frame)

    def take_snapshot(self):
        """Hàm thực thi khi bấm nút chụp ảnh"""
        if self.current_frame is not None:
            filename = f"ket_qua_{self.img_counter}.jpg"
            # Lưu ảnh bằng OpenCV
            cv2.imwrite(filename, self.current_frame)
            print(f"[THÀNH CÔNG] Đã lưu hình ảnh: {filename}")
            
        
            self.btn_capture.config(text="✔️ ĐÃ LƯU ẢNH!")
            self.window.after(1000, lambda: self.btn_capture.config(text="📸 CHỤP ẢNH MÀN HÌNH"))
            
            self.img_counter += 1

    def close_app(self):
        self.cap.release()
        self.window.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = ThuocDetectionApp(root, "Nhận Diện Thuốc - PTIT")
