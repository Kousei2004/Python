import numpy as np

def create_random_matrix(n):
    # Tạo ma trận ngẫu nhiên với số nguyên trong khoảng 0-100
    matrix = np.random.randint(0, 101, size=(n, n))
    
    # In thông tin về ma trận
    print("Kiểu dữ liệu của phần tử trong ma trận:", matrix.dtype)
    print("Kích thước của mảng ma trận:", matrix.shape)
    print("Số phần tử của mảng ma trận:", matrix.size)
    print("Số chiều của mảng ma trận:", matrix.ndim)
    
    # In ma trận
    print("\nMa trận:")
    print(matrix)
    
    return matrix

def get_diagonals(matrix):
    # Lấy đường chéo chính
    v_chinh = np.diag(matrix)
    
    # Lấy đường chéo phụ
    v_phu = np.diag(np.fliplr(matrix))
    
    print("\nVector chéo chính (v_chinh):")
    print(v_chinh)
    print("\nVector chéo phụ (v_phu):")
    print(v_phu)
    
    return v_chinh, v_phu

def count_comparison(matrix, x):
    # Đếm số phần tử bằng x
    equal_count = np.sum(matrix == x)
    
    # Đếm số phần tử lớn hơn x
    greater_count = np.sum(matrix > x)
    
    # Đếm số phần tử nhỏ hơn x
    less_count = np.sum(matrix < x)
    
    print(f"\nKết quả so sánh với x = {x}:")
    print(f"Số phần tử bằng {x}: {equal_count}")
    print(f"Số phần tử lớn hơn {x}: {greater_count}")
    print(f"Số phần tử nhỏ hơn {x}: {less_count}")
    
    return equal_count, greater_count, less_count

# Tạo ma trận với n = 12
n = 12
result_matrix = create_random_matrix(n)

# Lấy các vector chéo
v_chinh, v_phu = get_diagonals(result_matrix)

# Nhập và kiểm tra giá trị x
while True:
    try:
        x = int(input("\nNhập giá trị x (0-100): "))
        if 0 <= x <= 100:
            break
        else:
            print("Giá trị x phải nằm trong khoảng 0-100")
    except ValueError:
        print("Vui lòng nhập một số nguyên")

# Đếm và so sánh với x
equal_count, greater_count, less_count = count_comparison(result_matrix, x)