#1
a = 10
b = 8

tong = a + b
hieu = a - b
tich = a * b
thuong = a / b
thuong_nguyen = a // b
thuong_du = a % b
mu = a ** b

#2
a = 10
b = 8

print('1) Lớn hơn (a > b):', a>b)
print('2) Nhỏ hơn (a < b):', a<b)
print('3) Bằng (a == b):', a==b)
print('4) Lớn hơn hoặc bằng (a>=b):',a>=b)
print('5) Nhỏ hơn hoặc bằng (a<=b):',a<=b)
print('6) Khác (a!=b):',a!=b)

#3
x = 15
y = True

kt = (x>3) and (x<10)  # hoặc: kt = (x>3) & (x<10)
kt2 = (x>3) or (x<10)   # hoặc: kt2 = (x>3) | (x<10)
kt3 = not y

print('1) Phép toán AND:', kt)
print('2) Phép toán OR:', kt2)
print('3) Phép toán NOT:', kt3)

#4
# Nhập số tiền từ người dùng
so_tien = input("Nhập vào số tiền bạn có: ")

# Chuyển đổi số tiền nhập vào thành kiểu số nguyên
so_tien = int(so_tien)

# Kiểm tra nếu số tiền lớn hơn hoặc bằng 1 tỷ
if so_tien >= 1000000000:
    # Nếu đúng, in ra thông báo chúc mừng
    print("Bạn đã là một tỷ phú!")
else:
    # Nếu sai, in ra thông báo khuyến khích
    print("Bạn còn phải kiếm nhiều tiền hơn!")
    
#5
num = 3
         if num > 0:
             print(num, "là số dương.")
         print("Thông điệp này luôn được in.")
num = -1
         if num > 0:
             print(num, "là số dương.")
         print("Thông điệp này luôn được in.")

#6
num = -1
if num >= 0:
  print("Số dương")
else:
  print("Số âm")
  
num = 3
if num >= 0:
  print("Số dương")
else:
  print("Số âm")
  
#7
# Nhập số nguyên N
N = int(input("Nhập vào một số nguyên: "))

# Kiểm tra số chẵn hay số lẻ
if N % 2 == 0:
    print("Đây là số chẵn!")
else:
    print("Đây là số lẻ!")

#8
# Nhập vào giới tính (0=Nam, 1=Nữ)
gioi_tinh = int(input("Nhập vào giới tính (0=Nam, 1=Nữ): "))

# Kiểm tra giới tính và hiển thị thông báo tương ứng
if gioi_tinh == 0:
    print("Chào anh đẹp trai!")
elif gioi_tinh == 1:
    print("Chào chị xinh gái!")
else:
    print("Cảnh báo: Giới tính không xác định!")

#9
num = float(input("Nhập một số: "))
if num >= 0:
  if num == 0:
    print("Số Không")
  else:
    print("Số dương")
else:
  print("Số âm")
  
#10
n = int(input('Em sinh tháng mấy?'))
i = -1
while (i <= n):
    print(i, ') I Love You!')
    i = i + 1
print('-----------------HUMG-----------------')

#11
n = int(input('Em sinh tháng mấy?'))
i = 1
while (i <= n):
    print(i, ') I Love You!')
    # Chỉ hiển thị tối đa 3 lần
    if (i == 3):
        break;  # Thoát ra khỏi vòng lặp while
    i = i + 1
print('-----------------HUMG-----------------')

#12
n = 20
i = 1
while (i <= n):
    i = i + 1
    if (i % 3 == 0):
        continue  # Bỏ qua các lệnh phía sau nếu không chia hết cho 3
    print(i)
print('-----------------HUMG-----------------')

#13
# chỉ cho phép nhập tháng sinh 1 - 12
while True:
    n = int(input('Em sinh tháng mấy?'))
    if (1 <= n <= 12):
        # Tháng sinh nhập vào hợp lệ!
        break;
    print('Tháng không đúng, vui lòng nhập lại')
# Câu lệnh ngoài vòng lặp while
print('Chào em cô gái tháng', n)

#14
n = int(input("Nhập vào một số nguyên dương: "))

tich = 1
tong = 0

for i in range(1, n+1):
    tich = tich * i
    tong = tong + i

print(n, "! = ", tich)
print(n, "+ = ", tong)

#15
chuoi = 'HUMG IN MY MIND'
for ky_tu in chuoi:
    print(ky_tu)
    
    chuoi = 'HUMG IN MY MIND'
dem = 0
for ky_tu in chuoi:
    if ky_tu == 'M':
        dem += 1
print('Số ký tự M có trong chuỗi là:', dem)

#16
hoc_sinh = ['Lê Thùy Dung', 'Trần Đức Hùng', 'Nguyễn Lan Anh', 'Mai Phương Thúy', 'Trần Thanh Thủy', 'Kiều Thành Công']
print('Danh sách học sinh bao gồm:')
tt = 1
for i in hoc_sinh:
    print(tt, ')', i)
    tt = tt + 1

#17

for i in range(5):
    print('i =', i)

for i in range(5, 10):
    print('i =', i)
    
for i in range(2, 11, 2):
    print('i =', i)
    
#18
for i in range(2, 10):
    print('Bảng cửu chương:', i)
    for j in range(1, 11):
        print(i, 'x', j, '=', i * j)
    print('-------------------')