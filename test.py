import cv2
import numpy as np
import matplotlib.pyplot as plt

def display_color_spaces(image_path):
    # Đọc ảnh
    img = cv2.imread(image_path)
    
    # Chuyển đổi sang các không gian màu khác nhau
    rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    lab = cv2.cvtColor(img, cv2.COLOR_BGR2LAB)
    yuv = cv2.cvtColor(img, cv2.COLOR_BGR2YUV)
    
    # Tách các kênh màu
    r, g, b = cv2.split(rgb)
    h, s, v = cv2.split(hsv)
    l, a, b_lab = cv2.split(lab)
    y, u, v_yuv = cv2.split(yuv)
    
    # Hiển thị
    plt.figure(figsize=(15, 12))
    
    # RGB
    plt.subplot(431), plt.imshow(r, cmap='gray'), plt.title('Red Channel')
    plt.subplot(432), plt.imshow(g, cmap='gray'), plt.title('Green Channel')
    plt.subplot(433), plt.imshow(b, cmap='gray'), plt.title('Blue Channel')
    
    # HSV
    plt.subplot(434), plt.imshow(h, cmap='gray'), plt.title('Hue')
    plt.subplot(435), plt.imshow(s, cmap='gray'), plt.title('Saturation')
    plt.subplot(436), plt.imshow(v, cmap='gray'), plt.title('Value')
    
    # LAB
    plt.subplot(437), plt.imshow(l, cmap='gray'), plt.title('Lightness')
    plt.subplot(438), plt.imshow(a, cmap='gray'), plt.title('A Channel')
    plt.subplot(439), plt.imshow(b_lab, cmap='gray'), plt.title('B Channel')
    
    # YUV
    plt.subplot(4,3,10), plt.imshow(y, cmap='gray'), plt.title('Y Channel')
    plt.subplot(4,3,11), plt.imshow(u, cmap='gray'), plt.title('U Channel')
    plt.subplot(4,3,12), plt.imshow(v_yuv, cmap='gray'), plt.title('V Channel')
    
    plt.tight_layout()
    plt.show()

# Mô phỏng quá trình thu nhận ảnh
def simulate_image_acquisition(image_path):
    # Đọc ảnh gốc
    original = cv2.imread(image_path)
    
    # Mô phỏng nhiễu cảm biến
    noise = np.random.normal(0, 25, original.shape).astype(np.uint8)
    noisy_img = cv2.add(original, noise)
    
    # Mô phỏng thay đổi độ sáng
    gamma = 1.5
    brightened = np.array(255 * (original / 255) ** gamma, dtype=np.uint8)
    
    # Mô phỏng mờ do chuyển động
    blurred = cv2.blur(original, (5, 5))
    
    # Hiển thị kết quả
    plt.figure(figsize=(15, 5))
    images = [original, noisy_img, brightened, blurred]
    titles = ['Ảnh Gốc', 'Nhiễu Cảm Biến', 'Thay Đổi Độ Sáng', 'Mờ Do Chuyển Động']
    
    for i in range(4):
        plt.subplot(1, 4, i+1)
        plt.imshow(cv2.cvtColor(images[i], cv2.COLOR_BGR2RGB))
        plt.title(titles[i])
        plt.axis('off')
    
    plt.tight_layout()
    plt.show()

# Sử dụng
image_path = 'star_solved.png'
display_color_spaces(image_path)
simulate_image_acquisition(image_path)