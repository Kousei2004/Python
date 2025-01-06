import cv2  # OpenCV - thư viện xử lý ảnh
import numpy as np  # NumPy - thư viện tính toán với mảng
import matplotlib.pyplot as plt  # Matplotlib - thư viện vẽ đồ thị và hiển thị ảnh

def convert_bgr_to_rgb(img):
    """
    Chuyển đổi ảnh từ BGR sang RGB
    - Trong OpenCV, ảnh được đọc theo định dạng BGR (Blue-Green-Red)
    - Cần chuyển sang RGB (Red-Green-Blue) để hiển thị đúng màu sắc
    """
    height, width = img.shape[:2]  # Lấy kích thước ảnh (cao, rộng)
    rgb_img = np.zeros_like(img)   # Tạo một ảnh mới với kích thước giống ảnh gốc
    
    # Duyệt qua từng pixel trong ảnh
    for i in range(height):
        for j in range(width):
            # Hoán đổi kênh B và R, giữ nguyên kênh G
            rgb_img[i,j,0] = img[i,j,2]  # R = B cũ
            rgb_img[i,j,1] = img[i,j,1]  # G giữ nguyên
            rgb_img[i,j,2] = img[i,j,0]  # B = R cũ
    
    return rgb_img

def convert_to_grayscale(img):
    """
    Chuyển đổi ảnh màu sang ảnh xám
    Sử dụng công thức: Y = 0.299*R + 0.587*G + 0.114*B
    - Hệ số 0.299, 0.587, 0.114 dựa trên cách mắt người nhìn màu sắc
    - Mắt người nhạy cảm nhất với màu xanh lá (G) nên hệ số của G lớn nhất
    """
    height, width = img.shape[:2]
    gray_img = np.zeros((height, width), dtype=np.uint8)  # Tạo ảnh xám (2 chiều)
    
    for i in range(height):
        for j in range(width):
            # Lấy giá trị BGR của pixel hiện tại
            B = img[i,j,0]
            G = img[i,j,1]
            R = img[i,j,2]
            
            # Áp dụng công thức chuyển đổi
            gray_value = 0.299*R + 0.587*G + 0.114*B
            
            # Đảm bảo giá trị nằm trong khoảng 0-255
            gray_img[i,j] = np.clip(gray_value, 0, 255)
    
    return gray_img

def convert_to_binary(gray_img, threshold=127):
    """
    Chuyển đổi ảnh xám sang ảnh nhị phân (đen trắng)
    - threshold: ngưỡng phân tách (mặc định 127)
    - Pixel có giá trị > ngưỡng => trắng (255)
    - Pixel có giá trị <= ngưỡng => đen (0)
    """
    height, width = gray_img.shape
    binary_img = np.zeros((height, width), dtype=np.uint8)
    
    for i in range(height):
        for j in range(width):
            # So sánh với ngưỡng để quyết định đen/trắng
            if gray_img[i,j] > threshold:
                binary_img[i,j] = 255  # Màu trắng
            else:
                binary_img[i,j] = 0    # Màu đen
    
    return binary_img

def display_image_modes(image_path):
    """
    Hiển thị ảnh ở 3 chế độ: Màu, Xám và Nhị phân
    """
    # 1. Đọc ảnh
    img = cv2.imread(image_path)
    if img is None:
        raise FileNotFoundError("Không thể đọc file ảnh")
    
    # 2. Xử lý ảnh qua 3 bước
    img_rgb = convert_bgr_to_rgb(img)            # Chuyển BGR -> RGB
    img_gray = convert_to_grayscale(img)         # Chuyển sang ảnh xám
    img_binary = convert_to_binary(img_gray)     # Chuyển sang ảnh nhị phân
    
    # 3. Hiển thị kết quả
    plt.figure(figsize=(15, 5))
    
    # Hiển thị ảnh màu
    plt.subplot(131)
    plt.title('Ảnh Màu (RGB)\nR=Red, G=Green, B=Blue')
    plt.imshow(img_rgb)
    plt.axis('off')
    
    # Hiển thị ảnh xám
    plt.subplot(132)
    plt.title('Ảnh Xám\nY = 0.299*R + 0.587*G + 0.114*B')
    plt.imshow(img_gray, cmap='gray')
    plt.axis('off')
    
    # Hiển thị ảnh nhị phân
    plt.subplot(133)
    plt.title('Ảnh Nhị phân\nNgưỡng = 127\n>127: Trắng (255)\n≤127: Đen (0)')
    plt.imshow(img_binary, cmap='gray')
    plt.axis('off')
    
    plt.tight_layout()
    plt.show()

# Chạy chương trình
try:
    display_image_modes('star_solved.png')
except Exception as e:
    print(f"Lỗi: {str(e)}")