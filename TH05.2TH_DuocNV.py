#Bai 3.1
import numpy as np

# Giả sử vector_weigth có 100 phần tử (ví dụ từ 1 đến 100)
vector_weigth = np.arange(1, 101)  # Tạo vector từ 1 đến 100

# Chuyển đổi thành ma trận 10x10
matrix_10x10 = vector_weigth.reshape(10, 10)

# In kết quả
print("Vector ban đầu:")
print(vector_weigth)

print("\nMa trận 10x10:")
print(matrix_10x10)


#Bai 3.2/49
import numpy as np

# Tạo ma trận weight ngẫu nhiên (10x10) với định thức khác 0
np.random.seed(0)  # Đặt seed để kết quả tái lập
matrix_weight = np.random.randint(1, 10, (10, 10))  # Ma trận 10x10 với số ngẫu nhiên từ 1-9

# Tính định thức
determinant = np.linalg.det(matrix_weight)

print("Ma trận weight:")
print(matrix_weight)

if determinant != 0:
    # Tính ma trận nghịch đảo
    inverse_matrix = np.linalg.inv(matrix_weight)
    print("\nMa trận weight có tồn tại ma trận nghịch đảo.")
    print("Ma trận nghịch đảo (weight^-1):")
    print(inverse_matrix)
else:
    print("\nMa trận weight không tồn tại ma trận nghịch đảo (determinant = 0).")

#Bai 3.3/49
# Tạo vector chứa các phần tử trên đường chéo chính
vector_diagonal = np.diag(matrix_weight)

# Tính trace của ma trận
trace = np.trace(matrix_weight)

print("\nVector chứa các phần tử trên đường chéo chính:")
print(vector_diagonal)

print("\nTrace của ma trận weight:")
print(trace)

#Bai3.4/50
import numpy as np

# Tạo ma trận weight ngẫu nhiên (10x10)
np.random.seed(0)  # Đặt seed để kết quả có thể tái lập
matrix_weight = np.random.randint(1, 10, (10, 10))  # Ma trận 10x10 với số nguyên từ 1 đến 9

print("Ma trận weight:")
print(matrix_weight)

# Lấy các phần tử ma trận đường chéo trên (i < j)
upper_triangular = matrix_weight[np.triu_indices_from(matrix_weight, k=1)]

# Lấy các phần tử ma trận đường chéo dưới (i > j)
lower_triangular = matrix_weight[np.tril_indices_from(matrix_weight, k=-1)]

# Tìm giá trị lớn nhất
max_upper = np.max(upper_triangular)
max_lower = np.max(lower_triangular)

print("\nGiá trị lớn nhất trong ma trận đường chéo trên (không bao gồm đường chéo chính):", max_upper)
print("Giá trị lớn nhất trong ma trận đường chéo dưới (không bao gồm đường chéo chính):", max_lower)

#Bai 4.1
import numpy as np

# Tạo vector_height và vector_weight với 100 phần tử
np.random.seed(0)
vector_height = np.random.randint(1, 10, 100)  # Vector chứa các số nguyên từ 1 đến 9
vector_weight = np.random.randint(1, 10, 100)  # Vector chứa các số nguyên từ 1 đến 9

# Chuyển vector thành ma trận kích thước 10x10
matrix_height = vector_height.reshape(10, 10)
matrix_weight = vector_weight.reshape(10, 10)

# Hiển thị ma trận
print("Ma trận height:")
print(matrix_height)
print("\nMa trận weight:")
print(matrix_weight)

# So sánh hai ma trận
comparison_equal = matrix_height == matrix_weight
comparison_greater = matrix_height > matrix_weight
comparison_less = matrix_height < matrix_weight

# Thực hiện các phép toán cộng, trừ, nhân
matrix_add = matrix_height + matrix_weight  # Cộng hai ma trận
matrix_subtract = matrix_height - matrix_weight  # Trừ hai ma trận
matrix_hadamard = matrix_height * matrix_weight  # Nhân từng phần tử (Hadamard product)
matrix_dot = np.dot(matrix_height, matrix_weight)  # Nhân ma trận (dot product)

# Hiển thị kết quả
print("\nSo sánh (==):")
print(comparison_equal)
print("\nSo sánh (>):")
print(comparison_greater)
print("\nSo sánh (<):")
print(comparison_less)

print("\nKết quả cộng hai ma trận:")
print(matrix_add)

print("\nKết quả trừ hai ma trận:")
print(matrix_subtract)

print("\nKết quả nhân từng phần tử (Hadamard product):")
print(matrix_hadamard)

print("\nKết quả nhân ma trận (dot product):")
print(matrix_dot)

#Bai 5.1
import numpy as np

# Tạo ma trận Height và Weight ngẫu nhiên (10x10)
np.random.seed(0)
matrix_height = np.random.randint(1, 10, (10, 10))  # Ma trận Height
matrix_weight = np.random.randint(1, 10, (10, 10))  # Ma trận Weight

# Hiển thị ma trận
print("Ma trận Height:")
print(matrix_height)
print("\nMa trận Weight:")
print(matrix_weight)

# Tính hạng của ma trận Height và Weight
rank_height = np.linalg.matrix_rank(matrix_height)
rank_weight = np.linalg.matrix_rank(matrix_weight)

print("\nHạng của ma trận Height:", rank_height)
print("Hạng của ma trận Weight:", rank_weight)

# Kiểm tra nếu ma trận khả nghịch và tính ma trận nghịch đảo
try:
    inverse_height = np.linalg.inv(matrix_height)
    print("\nMa trận nghịch đảo của ma trận Height:")
    print(inverse_height)
except np.linalg.LinAlgError:
    print("\nMa trận Height không có ma trận nghịch đảo.")

try:
    inverse_weight = np.linalg.inv(matrix_weight)
    print("\nMa trận nghịch đảo của ma trận Weight:")
    print(inverse_weight)
except np.linalg.LinAlgError:
    print("\nMa trận Weight không có ma trận nghịch đảo.")

#Bai 5.2
