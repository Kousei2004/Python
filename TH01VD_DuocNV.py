print("Hello World")

print('Chào mừng bạn đến với ngôn ngữ lập trình Python!')

name = input('Nhập tên của bạn:')

print('Chúc bạn', name, 'sẽ thành thạo Python sau khóa học này!')

#TH 1.1
# Khởi tạo biến a và A với giá trị ban đầu là 0
a = 0
A = 0

# Vòng lặp đầu tiên: Tính tổng các số từ 1 đến 5 và gán vào biến a
for i in range(1, 6):
    # In ra giá trị của i trong mỗi lần lặp
    print(i)
    # Cộng i vào a và gán kết quả vào a
    a = a + i

# In kết quả của biến a
print("Giá trị của biến a =", a)

# Vòng lặp thứ hai: Tính tổng các số lẻ từ 1 đến 5 và gán vào biến A
for i in range(1, 6, 2):
    # In ra giá trị của i trong mỗi lần lặp (chỉ số lẻ)
    print(i)
    # Cộng i vào A và gán kết quả vào A
    A = A + i

# In kết quả của biến A
print("Giá trị của biến A =", A)

#TH1.2
# Nhập hai số a và b từ người dùng
a = int(input("Nhập vào số a: "))
b = int(input("Nhập vào số b: "))

# Tính toán các phép toán
tong = a + b
hieu = a - b
tich = a * b
thuong = a / b

# In kết quả ra màn hình
print("Tổng a + b =", tong)
print("Hiệu a - b =", hieu)
print("Tích a * b =", tich)
print("Thương a / b =", thuong)

#VD 38
a = 52348252408
b = 523482034
c = 545354645577
d = a + b + c
print(d)

#46
a = 10
b = 8

tong = a + b
hieu = a - b
tich = a * b
thuong = a / b
thuong_nguyen = a // b
thuong_du = a % b
mu = a ** b

print("Tổng:", tong)
print("Hiệu:", hieu)
print("Tích:", tich)
print("Thương:", thuong)
print("Thương nguyên:", thuong_nguyen)
print("Thương dư:", thuong_du)
print("Lũy thừa:", mu)

#47
x = 1985
y = 3.1415926535
z = 'Dai Hoc Cong Nghe Dong A'
n = [5, 7 , 9, 8]
b = True

#-----------------
print("Giá trị của x là:", x, "và kiểu dữ liệu là:", type(x))
print("Giá trị của y là:", y, "và kiểu dữ liệu là:", type(y))
print("Giá trị của z là:", z, "và kiểu dữ liệu là:", type(z))
print("Giá trị của n là:", n, "và kiểu dữ liệu là:", type(n))
print("Giá trị của b là:", b, "và kiểu dữ liệu là:", type(b))

#52
st = "HUMG là Trường đại học hàng đầu tại Việt Nam"
x = 'HUMG' in st
y = 'Python' in st
#Trả về True nếu có trong chuỗi st
#Trả về False nếu không có trong chuỗi st
print('Kết quả kiểm tra HUMG:', x)
print('Kết quả kiểm tra Python:', y)

#62
# Khai báo danh sách học sinh gồm các chuỗi tên của học sinh
hoc_sinh = ['Lê Thùy Dung', 'Trần Đức Hùng', 'Nguyễn Lan Anh', 'Mai Phương Thúy']
print(hoc_sinh)

# Khai báo danh sách điểm chữ gồm các chuỗi ký tự
diem = ['A+', 'A', 'B+', 'C+', 'C', 'D+', 'D', 'F']
print(diem)

# Khai báo danh sách gồm các số nguyên
list_so = [9, 5, 8, 13, 0, 4, 7, -9, 11]
print(list_so)

# Khai báo danh sách với nhiều kiểu dữ liệu khác nhau
person_info = ['Mary', 1998, 'Tokyo, Japan', 1.70, 65]
print(person_info)

# Khai báo danh sách rỗng
list_rong = []
print(list_rong)

#63
# Truy xuất dữ liệu trong danh sách:
# Hiển thị tên học sinh ở vị trí thứ 3
print('Học sinh vị trí thứ 3: ', hoc_sinh[2])

# Hiển thị tên người - chiều cao trong biến person_info
print('Họ tên:', person_info[0], '---Chiều cao:', person_info[3])

# Truy xuất nhiều phần tử trong danh sách
print(list_so[3:8])

#65
list_a = [8, 4, 8, 2]
list_b = [3, 0, 7, 6, 5]

# --- Cộng hai danh sách (+) ---:
list_ab = list_a + list_b
print('List mới: ', list_ab)

# Lấy độ dài của danh sách list_ab: len(list_ab)
print(list_ab, 'Có số phần tử là: ', len(list_ab))

#66
# Kiểm tra phần tử có thuộc danh sách không?
print(list_ab)

# Kiểm tra phần tử 0:
bol_0 = 0 in list_ab
print('Phần tử 0 có thuộc list_ab ?', bol_0)

# Kiểm tra phần tử 9:
bol_9 = 9 in list_ab
print('Phần tử 9 có thuộc list_ab ?', bol_9)

#67
# Thêm phần tử vào danh sách:
print('Danh sách ban đầu: \n', list_ab)

# Thêm vào cuối danh sách:
list_ab.append(10)
print('Danh sách thêm vào cuối:\n', list_ab)

# Thêm vào vị trí bất kỳ trong danh sách
list_ab.insert(1,100)
print('Danh sách thêm vào vị trí thứ 2: \n', list_ab)

#69
# Thêm phần tử vào danh sách:
print('Danh sách ban đầu: \n', list_ab)

# Thêm vào cuối danh sách:
list_ab.append(10)
print('Danh sách thêm vào cuối:\n', list_ab)

# Thêm vào vị trí bất kỳ trong danh sách
list_ab.insert(1,100)
print('Danh sách thêm vào vị trí thứ 2: \n', list_ab)

#70
# Xóa phần tử khỏi danh sách:
print('Danh sách ban đầu: \n', list_ab)

# Xóa phần tử cuối
list_ab.pop()
print('Danh sách xóa phần tử cuối:\n', list_ab)

# Xóa phần tử tại vị trí số 2
del list_ab[1]
print('Danh sách xóa phần tử ở vị trí số 2:\n', list_ab)

# Xóa phần tử có giá trị 0 xuất hiện đầu tiên
list_ab.remove(0)
print('Xóa phần tử có giá trị 0 đầu tiên:\n', list_ab)

#70
# Đếm số lần xuất hiện của một phần tử trong danh sách:
print('Danh sách ban đầu: \n', list_ab)

# Số lần xuất hiện số 8 trong danh sách
print(' Số 8 xuất hiện: ', list_ab.count(8))

# Số lần xuất hiện số 1 trong danh sách
print(' Số 1 xuất hiện: ', list_ab.count(1))

#71
# Trường hợp danh sách:
ds_a = [4, 5, 8, 9]  # Khai báo danh sách ds_a
ds_b = ds_a  # Gán giá trị của biến ds_a cho ds_b
ds_b[1] = 10  # Thay đổi giá trị vị trí số 2 trong ds_b

print('Biến ds_a: ', ds_a)
print('Biến ds_b: ', ds_b)

#72
# Sao chép một danh sách độc lập:
ds_a = [4, 5, 8, 9]  # Khai báo danh sách ds_a
ds_b = ds_a.copy()  # Sao chép ds_a cho ds_b
ds_b[1] = 10  # Thay đổi giá trị vị trí số 2 trong ds_b

print('Biến ds_a: ', ds_a)
print('Biến ds_b: ', ds_b)

#73
# Khai báo biến kiểu dữ liệu Boolean:
x = True
y = False

# Khai báo biến kiểu dữ liệu boolean qua biểu thức
z = 5 > 8
w = 12 == 12

print('Kiểu dữ liệu của biến x:', type(x), ', Giá trị: ', x)
print('Kiểu dữ liệu của biến y:', type(y), ', Giá trị: ', y)
print('Kiểu dữ liệu của biến z:', type(z), ', Giá trị: ', z)
print('Kiểu dữ liệu của biến w:', type(w), ', Giá trị: ', w)