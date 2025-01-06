import cv2
import numpy as np
import matplotlib.pyplot as plt

def display_image_modes(image_path):
    # Đọc ảnh
    img = cv2.imread(image_path)
    if img is None:
        raise FileNotFoundError("Không thể đọc file ảnh")
    
    # Chuyển từ BGR sang RGB
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    
    # Chuyển sang ảnh xám
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # OpenCV đọc ảnh ở dạng BGR nên thứ tự là:
    # B = img[x,y,0]
    # G = img[x,y,1]
    # R = img[x,y,2]
    # # Tính giá trị độ xám
    # gray[x,y] = 0.299*R + 0.587*G + 0.114*B
    
    # Chuyển sang ảnh nhị phân
    _, img_binary = cv2.threshold(img_gray, 127, 255, cv2.THRESH_BINARY)
    
    # Hiển thị ảnh
    plt.figure(figsize=(15, 5))
    
    plt.subplot(131)
    plt.title('Ảnh Màu')
    plt.imshow(img_rgb)
    plt.axis('off')
    
    plt.subplot(132)
    plt.title('Ảnh Xám')
    plt.imshow(img_gray, cmap='gray')
    plt.axis('off')
    
    plt.subplot(133)
    plt.title('Ảnh Nhị Phân')
    plt.imshow(img_binary, cmap='gray')
    plt.axis('off')
    
    plt.tight_layout()
    plt.show()

# Sử dụng
try:
    display_image_modes('star_solved.png')
except Exception as e:
    print(f"Lỗi: {str(e)}")

# Quá trình thu nhận ảnh: ánh sáng → cảm biến → xử lý tín hiệu → xử lý màu → nén/lưu trữ.