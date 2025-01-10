import numpy as np
#Trang 13
a = np.array([1, 2, 5, 7, 0, 8])

print(a)
print("Loại dữ liệu của biến a:", type(a))
print("Kiểu dữ liệu của phần tử trong mảng a:", a.dtype)
print("Kích thước của mảng a:", a.shape)
print("Số phần tử của mảng a:", a.size)
print("Số chiều của mảng a:", a.ndim)

#14
# Tạo mảng 2 chiều (2D - Ma trận)
b = np.array([(4, 5, 6.0), (1, 2, 3.5)])

print(b)
print("Loại dữ liệu của biến b:", type(b))
print("Kiểu dữ liệu của phần tử trong mảng b:", b.dtype)
print("Kích thước của mảng b:", b.shape)
print("Số phần tử của mảng b:", b.size)
print("Số chiều của mảng b:", b.ndim)

#15
c = np.array([[(2,4,0,6), (4,7,5,6)],
              [(0,3,2,1), (9,4,5,6)],
              [(5,8,6,4), (1,4,6,8)]]) # mảng 3 chiều (3D)

print(c)
print("Phần tử đầu tiên của mảng c:", c[0,0,0])
print("Kiểu dữ liệu của phần tử trong mảng c:", c.dtype)
print("Kích thước của mảng c:", c.shape)
print("Số phần tử của mảng c:", c.size)
print("Số chiều của mảng c:", c.ndim)

#18
array_zeros = np.zeros((5, 3))

print(array_zeros)
print("Kiểu dữ liệu trong mảng array_zeros:", array_zeros.dtype)
print("Kích thước của mảng array_zeros:", array_zeros.shape)
print("Số phần tử của mảng array_zeros:", array_zeros.size)
print("Số chiều của mảng array_zeros:", array_zeros.ndim)

#19
array_eye = np.eye(5)

print(array_eye)
print("Kiểu dữ liệu của phần tử trong mảng array_eye:", array_eye.dtype)
print("Kích thước của mảng array_eye:", array_eye.shape)
print("Số phần tử của mảng array_eye:", array_eye.size)

#20
array_random = np.random.random((7, 5))

print(array_random)
print("Kiểu dữ liệu của phần tử trong mảng array_random:", array_random.dtype)
print("Kích thước của mảng array_random:", array_random.shape)
print("Số phần tử của mảng array_random:", array_random.size)
print("Số chiều của mảng array_random:", array_random.ndim)

#22
# Phương thức arange(a, b, steps):
# Tạo vector:
# Phần tử đầu tiên = a,
# kết thúc < b,
# mỗi phần tử cách nhau một khoảng = steps
d = np.arange(1, 15, 2)
print('Vector d:', d)
print('Số phần tử của vector d:', d.size)

print()

# Phương thức linspace(a, b, num)
# Tạo vector:
# Phần tử đầu tiên = a,
# Phần tử kết thúc = b,
# Số phần tử của ma trận = num
f = np.linspace(1, 15, 11)
print('Vector f:', f)
print('Số phần tử của vector f:', f.size)

#25
# Đọc dữ liệu từ file Diem_2A.txt
path = 'Data_Exercise/Diem_2A.txt'
diem_2a = np.loadtxt(path, delimiter=',', dtype=np.int)

print(diem_2a)
print("Kiểu dữ liệu của phần tử trong mảng diem_2a:", diem_2a.dtype)
print("Kích thước của mảng diem_2a:", diem_2a.shape)
print("Số phần tử của mảng diem_2a:", diem_2a.size)
print("Số chiều của mảng diem_2a:", diem_2a.ndim)