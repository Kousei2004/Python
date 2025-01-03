import cv2
import numpy as np

def process_image(image_path):
    """
    Thực hiện các thao tác xử lý ảnh cơ bản và hiển thị kết quả
    
    Parameters:
    image_path (str): Đường dẫn đến file ảnh
    """
    # Đọc ảnh
    img = cv2.imread(image_path)
    if img is None:
        print("Không thể đọc ảnh!")
        return
    
    # Chuyển sang ảnh xám
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    # Làm mờ ảnh để giảm nhiễu
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)
    
    # Phát hiện cạnh sử dụng Canny
    edges = cv2.Canny(blurred, 100, 200)
    
    # Điều chỉnh độ tương phản và độ sáng
    alpha = 1.5  # Điều chỉnh độ tương phản
    beta = 30    # Điều chỉnh độ sáng
    adjusted = cv2.convertScaleAbs(img, alpha=alpha, beta=beta)
    
    # Phân ngưỡng ảnh
    _, threshold = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
    
    # Tìm contour
    contours, _ = cv2.findContours(threshold, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    contour_img = img.copy()
    cv2.drawContours(contour_img, contours, -1, (0, 255, 0), 2)
    
    # Hiển thị tất cả các kết quả
    cv2.imshow('Ảnh gốc', img)
    cv2.imshow('Ảnh xám', gray)
    cv2.imshow('Làm mờ', blurred)
    cv2.imshow('Phát hiện cạnh', edges)
    cv2.imshow('Điều chỉnh độ tương phản', adjusted)
    cv2.imshow('Phân ngưỡng', threshold)
    cv2.imshow('Contours', contour_img)
    
    # Đợi phím bất kỳ để thoát
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def detect_faces(image_path):
    """
    Phát hiện khuôn mặt trong ảnh sử dụng Haar Cascade
    
    Parameters:
    image_path (str): Đường dẫn đến file ảnh
    """
    # Đọc ảnh
    img = cv2.imread(image_path)
    if img is None:
        print("Không thể đọc ảnh!")
        return
    
    # Chuyển sang ảnh xám
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    # Load bộ phát hiện khuôn mặt
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    
    # Phát hiện khuôn mặt
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)
    
    # Vẽ hình chữ nhật xung quanh khuôn mặt
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
    
    # Hiển thị kết quả
    cv2.imshow('Phát hiện khuôn mặt', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Ví dụ sử dụng
if __name__ == "__main__":
    # Thay thế 'path_to_image.jpg' bằng đường dẫn đến ảnh của bạn
    image_path = 'path_to_image.jpg'
    
    print("Xử lý ảnh cơ bản...")
    process_image(image_path)
    
    print("Phát hiện khuôn mặt...")
    detect_faces(image_path)