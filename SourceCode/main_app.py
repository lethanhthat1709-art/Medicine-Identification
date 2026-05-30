import cv2
import tkinter as tk
from tkinter import font
from PIL import Image, ImageTk
from ultralytics import YOLO

model = YOLO('best.pt') 

class ThuocDetectionApp:
    def __init__(self, window, window_title):
        self.window = window
        self.window.title(window_title)
        self.window.geometry("800x600")
        self.window.configure(bg="#1e1e1e") # 
        self.window.protocol("WM_DELETE_WINDOW", self.close_app)

        self.cap = cv2.VideoCapture(0)

        title_font = font.Font(family="Helvetica", size=18, weight="bold")
        btn_font = font.Font(family="Helvetica", size=12, weight="bold")

        self.lbl_title = tk.Label(window, text="HỆ THỐNG NHẬN DIỆN THUỐC BẰNG YOLOv8", 
                                  font=title_font, fg="#00ffcc", bg="#1e1e1e", pady=10)
        self.lbl_title.pack()

        self.canvas = tk.Canvas(window, width=640, height=480, bg="black", highlightthickness=2, highlightbackground="#00ffcc")
        self.canvas.pack(pady=10)

        self.btn_quit = tk.Button(window, text="ĐÓNG ỨNG DỤNG", font=btn_font, bg="#ff3333", fg="white", 
                                  activebackground="#cc0000", activeforeground="white",
                                  width=20, command=self.close_app)
        self.btn_quit.pack(pady=10)

        self.delay = 30
        self.update_frame()

        self.window.mainloop()

    def update_frame(self):
        success, frame = self.cap.read()
        
        if success:
            frame = cv2.flip(frame, 1)

            results = model(frame, verbose=False)
            
            annotated_frame = results[0].plot()

            cv2_image = cv2.cvtColor(annotated_frame, cv2.COLOR_BGR2RGB)
            
            pil_image = Image.fromarray(cv2_image)
            self.photo = ImageTk.PhotoImage(image=pil_image)

            self.canvas.create_image(0, 0, image=self.photo, anchor=tk.NW)

        self.window.after(self.delay, self.update_frame)

    def close_app(self):
        self.cap.release()
        self.window.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = ThuocDetectionApp(root, "Nhận Diện Thuốc - Đồ Án PTIT")