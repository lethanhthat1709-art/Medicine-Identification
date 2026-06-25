# Hệ thống nhận diện và phân loại các loại thuốc uống phổ biến dựa trên mô hình YOLO

## 📝 Giới thiệu dự án
Dự án được thực hiện nhằm nghiên cứu và triển khai một hệ thống thị giác máy tính có khả năng phát hiện và phân loại các loại thuốc phổ biến thông qua hình ảnh. Hệ thống sử dụng thuật toán **YOLOv8** để xác định vị trí (bounding box) và tên thuốc với độ chính xác cao và tốc độ xử lý nhanh.

### 💡 Ý nghĩa thực tiễn
- Hỗ trợ người dùng nhận diện nhanh tên thuốc, giảm nguy cơ uống nhầm.
- Có tiềm năng tích hợp vào quy trình kiểm kê tại các nhà thuốc hoặc kho dược.

## 🛠 Công nghệ sử dụng
- **Ngôn ngữ:** Python
- **Mô hình AI:** YOLOv8 (Ultralytics)
- **Xử lý ảnh:** OpenCV
- **Giao diện:** Tkinter / Pillow
- **Môi trường:** Google Colab / Local PC

## 🚀 Hướng dẫn cài đặt và chạy chương trình

### Yêu cầu hệ thống
- **Python:** Phiên bản 3.8 trở lên.
- **Phần cứng:** Máy tính có Webcam hoạt động bình thường (phục vụ nhận diện Real-time).

### Các bước thực thi
**Bước 1: Tải mã nguồn**
Mở Terminal/Command Prompt và chạy lệnh sau để tải dự án về máy:
```bash
git clone [https://github.com/lethanhthat1709-art/Medicine-Identification.git](https://github.com/lethanhthat1709-art/Medicine-Identification.git)
cd Medicine-Identification
Bước 2: Cài đặt thư viện
Di chuyển vào thư mục chứa mã nguồn và cài đặt các thư viện phụ thuộc:

Bash


cd SourceCode
pip install -r requirements.txt
(Hoặc cài đặt thủ công: pip install ultralytics opencv-python pillow)

Bước 3: Khởi động phần mềm
Đảm bảo bạn đang ở trong thư mục SourceCode (nơi chứa file main_app.py và trọng số best.pt), chạy lệnh sau để mở giao diện:

Bash


python main_app.py
📁 Cấu trúc thư mục
SourceCode/: Chứa mã nguồn huấn luyện AI, trọng số mô hình và code triển khai giao diện.

Documents/: Chứa các tài liệu, báo cáo tiến độ tuần, báo cáo giữa kỳ và báo cáo cuối kỳ (PDF/Word).

👥 Thông tin sinh viên
Họ và tên: Lê Nhật Quang

Mã sinh viên: B23DCVT359

Lớp: D23CQCE02-B

Giảng viên hướng dẫn: Kim Ngọc Bách
