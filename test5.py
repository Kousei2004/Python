import cv2
import numpy as np
import matplotlib.pyplot as plt

def convert_bgr_to_rgb(img):
    """
    Chuyển đổi ảnh từ BGR sang RGB
    - Trong OpenCV, ảnh được đọc theo định dạng BGR (Blue-Green-Red)
    - Cần chuyển sang RGB (Red-Green-Blue) để hiển thị đúng màu sắc
    """
    height, width = img.shape[:2]
    rgb_img = np.zeros_like(img)
    
    for i in range(height):
        for j in range(width):
            rgb_img[i,j,0] = img[i,j,2]  # R = B cũ
            rgb_img[i,j,1] = img[i,j,1]  # G giữ nguyên
            rgb_img[i,j,2] = img[i,j,0]  # B = R cũ
    
    return rgb_img

def convert_to_grayscale(img):
    """
    Chuyển đổi ảnh màu sang ảnh xám
    Sử dụng công thức: Y = 0.299*R + 0.587*G + 0.114*B
    """
    height, width = img.shape[:2]
    gray_img = np.zeros((height, width), dtype=np.uint8)
    
    for i in range(height):
        for j in range(width):
            B = img[i,j,0]
            G = img[i,j,1]
            R = img[i,j,2]
            gray_value = 0.299*R + 0.587*G + 0.114*B
            gray_img[i,j] = np.clip(gray_value, 0, 255)
    
    return gray_img

def convert_to_binary(gray_img, threshold=127):
    """
    Chuyển đổi ảnh xám sang ảnh nhị phân (đen trắng)
    """
    height, width = gray_img.shape
    binary_img = np.zeros((height, width), dtype=np.uint8)
    
    for i in range(height):
        for j in range(width):
            binary_img[i,j] = 255 if gray_img[i,j] > threshold else 0
    
    return binary_img

def display_matrix(img, title, max_size=8):
    """
    Hiển thị ma trận pixel của ảnh
    - max_size: kích thước tối đa để hiển thị toàn bộ pixel
    """
    height, width = img.shape[:2]
    
    print(f"\n{'-'*50}")
    print(f"{title}:")
    print(f"Kích thước ảnh: {height}x{width} pixel")
    
    # Xác định vùng hiển thị
    disp_h = min(height, max_size)
    disp_w = min(width, max_size)
    
    # In ra chỉ số cột
    print("\nChỉ số cột:")
    print("   ", end="")
    for j in range(disp_w):
        print(f"{j:^12}", end="")
    print("\n" + "-"*((disp_w * 12) + 4))
    
    # Hiển thị ma trận với chỉ số hàng
    if len(img.shape) == 3:  # Ảnh màu (3 kênh)
        for i in range(disp_h):
            print(f"{i:2} |", end="")
            for j in range(disp_w):
                if title.find("BGR") >= 0:
                    print(f"B:{img[i,j,0]:3d}", end=" ")
                    print(f"G:{img[i,j,1]:3d}", end=" ")
                    print(f"R:{img[i,j,2]:3d}", end="|")
                else:  # RGB
                    print(f"R:{img[i,j,0]:3d}", end=" ")
                    print(f"G:{img[i,j,1]:3d}", end=" ")
                    print(f"B:{img[i,j,2]:3d}", end="|")
            print()  # Xuống dòng sau mỗi hàng
    else:  # Ảnh xám hoặc nhị phân (1 kênh)
        for i in range(disp_h):
            print(f"{i:2} |", end="")
            for j in range(disp_w):
                print(f"{img[i,j]:^11}|", end="")
            print()
    
    print("-"*((disp_w * 12) + 4))
    
    if height > max_size or width > max_size:
        print(f"* Chỉ hiển thị {max_size}x{max_size} pixel đầu tiên của ảnh")
    print(f"{'-'*50}\n")

def display_image_modes(image_path):
    """
    Hiển thị ảnh ở 3 chế độ: Màu, Xám và Nhị phân
    Kèm theo ma trận pixel tương ứng
    """
    # 1. Đọc ảnh
    img = cv2.imread(image_path)
    if img is None:
        raise FileNotFoundError("Không thể đọc file ảnh")
    
    # 2. Xử lý ảnh qua 3 bước
    img_rgb = convert_bgr_to_rgb(img)
    img_gray = convert_to_grayscale(img)
    img_binary = convert_to_binary(img_gray)
    
    # 3. Hiển thị ma trận pixel
    print("\n=== HIỂN THỊ GIÁ TRỊ PIXEL CỦA ẢNH ===")
    display_matrix(img, "Ma trận ảnh gốc (BGR)")
    display_matrix(img_rgb, "Ma trận ảnh RGB")
    display_matrix(img_gray, "Ma trận ảnh xám")
    display_matrix(img_binary, "Ma trận ảnh nhị phân")
    
    # 4. Hiển thị hình ảnh
    plt.figure(figsize=(15, 5))
    
    plt.subplot(131)
    plt.title('Ảnh Màu (RGB)\nR=Đỏ, G=Xanh lá, B=Xanh dương')
    plt.imshow(img_rgb)
    plt.axis('off')
    
    plt.subplot(132)
    plt.title('Ảnh Xám\nĐộ xám = 0.299*R + 0.587*G + 0.114*B')
    plt.imshow(img_gray, cmap='gray')
    plt.axis('off')
    
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