#Trang 5
import numpy as np

# Tạo một vector
vector_a = np.array([5, 7, 2, 9, 10, 15, 2, 9, 2, 17, 28, 16], dtype=np.int16)

# In thông tin về vector
print(vector_a)
print('Số phần tử của vector:', vector_a.size)

# Chuyển đổi vector thành ma trận
# Lưu ý: matrix.size = vector.size

# Reshape thành ma trận 3x4
matrix_a = vector_a.reshape((3, 4))
print('\nReshape về ma trận: 3 x 4')
print(matrix_a)
print('Số phần tử của matrix_a:', matrix_a.size)

# Reshape thành ma trận 2x6
matrix_b = vector_a.reshape((2, 6))
print('\nReshape về ma trận: 2 x 6')
print(matrix_b)
print('Số phần tử của matrix_b:', matrix_b.size)

#Trang7
import numpy as np

# Tạo một ma trận 2 chiều
a1_2d = np.array([[1, 2, 3, 4],
                 [5, 6, 7, 8],
                 [9, 10, 11, 12]])
print('Matrix:\n', a1_2d)

print('----------------------------------')
print('a) ravel by row (default order=\'C\')')
print(a1_2d.ravel())

print('\n b) ravel by column (order=\'F\')')
print(a1_2d.ravel(order='F'))

#Trang 9

import numpy as np

x = np.arange(0, 6)
print(x)

# Tách vector x thành 2 vector
# có số phần tử bằng nhau
x1, x2 = np.split(x, 2)
print(x1, x2)

import numpy as np

x = np.arange(1, 10)
print(x)

# Tách vector x thành 3 vector
# tại các vị trí 2 và 6
x1, x2, x3 = np.split(x, [2, 6])
print(x1, x2, x3)

#Trang 11
# Lật ma trận theo cột
A1 = np.flip(A, 1)

# Tương đương với
A1 = np.fliplr(A)

print('Lật ma trận theo cột:\n', A1)

# Lật ma trận theo hàng
A2 = np.flip(A, 0)

# Tương đương với
A2 = np.flipud(A)

print('Lật ma trận theo hàng:\n', A2)

#Trang16
import numpy as np

x = np.arange(8)
print("x =", x)
print('----------------------------------')

# Các phép toán đã giới thiệu trong buổi 01
print("x + 5 =", x + 5)
print("x - 5 =", x - 5)
print("-x =", -x)
print("x * 2 =", x * 2)
print("x / 2 =", x / 2)
print("x // 2 =", x // 2)
print("x % 2 =", x % 2)
print("x ^ 3 =", x ** 3)

import numpy as np

x = np.arange(8)
print("x =", x)
print('----------------------------------')

# Sử dụng các phương thức của NumPy
print("x + 5 =", np.add(x, 5))
print("x - 5 =", np.subtract(x, 5))
print("-x =", np.negative(x))
print("x * 2 =", np.multiply(x, 2))
print("x / 2 =", np.divide(x, 2))
print("x // 2 =", np.floor_divide(x, 2))
print("x % 2 =", np.mod(x, 2))
print("x ^ 3 =", np.power(x, 3))

#Trang17
import numpy as np

x = np.array([-2, -1, 0, 1, 2])
print(x)
print('----------------------------------')
print(np.abs(x))
print(np.absolute(x))

import numpy as np

theta = np.linspace(0, np.pi, 3)
print("theta =", theta)
print('----------------------------------')
print("sin(theta) =", np.sin(theta))
print("cos(theta) =", np.cos(theta))
print("tan(theta) =", np.tan(theta))

#19
import numpy as np

x = np.array([1, 2, 3])
print("x =", x)
print('----------------------------------')
print("e^x =", np.exp(x))
print("2^x =", np.exp2(x))
print("3^x =", np.power(3, x))  

import numpy as np

x = np.array([1, 2, 4, 100])
print("x =", x)
print('----------------------------------')
print("ln(x) =", np.log(x))
print("log2(x) =", np.log2(x))
print("log10(x) =", np.log10(x))

#20
import numpy as np

arr = np.array([20.8999, 67.89899, 54.43409])
print(arr)
print('----------------------------------')
print("#1) Làm tròn tới 1 số sau dấu ,")
print(np.around(arr, 1))
print("#2) Làm tròn tới 2 số sau dấu ,")
print(np.around(arr, 2))
print("#3) Làm tròn xuống số nguyên gần nhất")
print(np.floor(arr))
print("#4) Làm tròn lên số nguyên gần nhất")
print(np.ceil(arr))

#23
import numpy as np

# Tạo một vector ngẫu nhiên gồm 15 số nguyên từ 1 đến 33
a = np.random.randint(1, 33, 15)

print('Vector ban đầu:\n', a)
print('----------------------------------')

# Sắp xếp vector a tăng dần
a_sort = np.sort(a)

# Sắp xếp vector a giảm dần:
# Cách 1: Lật vector a_sort để sắp xếp giảm dần
b_sort = np.flip(a_sort)

# Cách 2: Sử dụng -np.sort(-x)
# b_sort = -np.sort(-a)

print('Vector sắp xếp tăng dần:\n', a_sort)
print('Vector sắp xếp giảm dần:\n', b_sort)

#25
import numpy as np

# Tạo một ma trận mẫu
A = np.array([[8, 27, 2, 8, 3],
              [7, 16, 19, 23, 21],
              [14, 10, 1, 3, 5],
              [29, 11, 19, 12, 29],
              [4, 14, 10, 4, 23]])

# Sắp xếp theo hàng (axis=0)
a_sort1 = np.sort(A, axis=0)
print('Ma trận 1:\n', a_sort1)

# Sắp xếp theo cột (axis=1)
a_sort2 = np.sort(A, axis=1)
print('Ma trận 2:\n', a_sort2)

# Chuyển thành vector và sắp xếp các phần tử tăng dần theo hàng
v_sort = np.sort(A, axis=None)
print('Vector:\n', v_sort)

# Sắp xếp tất cả các phần tử theo thứ tự tăng dần theo hàng
a_sort3 = np.sort(A, axis=None).reshape(A.shape[0], A.shape[1])
print('Ma trận 3:\n', a_sort3)

#28
import numpy as np

x = np.array([17, 2, 11, 1, 9, 15, 1, 3, 8, 1, 12, 13, 5])

# 1) Tìm kiếm các phần tử có giá trị == 1
t1 = np.where(x == 1)
print(t1)
print("1. Số phần tử thỏa mãn điều kiện = 1: ", t1[0].size)

# 2) Tìm kiếm các phần tử có giá trị > 10
t2 = np.where(x > 10)
print(t2)
print("2. Số phần tử thỏa mãn điều kiện > 10: ", t2[0].size)

# Tìm kiếm các phần tử có giá trị [5, 12)
t3 = np.where((x >= 5) & (x < 12))
print(t3)
print("3. Số phần tử thỏa mãn điều kiện [5, 12): ", t3[0].size)

#29
import numpy as np

# Tìm kiếm trên ma trận
arr = np.array([[1, 2, 3, 4, 5, 4, 4],
                [7, 3, 4, 8, 9, 6, 7]])

# Tìm kiếm phần tử > 4
x = np.where(arr > 4)

print('Ma trận A:\n', arr)
print('----------------------------------')
print(x)
print('Số phần tử thỏa mãn điều kiện > 4:', x[0].size)