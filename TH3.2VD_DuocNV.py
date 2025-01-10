print('VD page 21')
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def getArea(self):
        return round(self.width * self.height, 1)

    def getPerimeter(self):
        return round(2 * (self.width + self.height), 1)
#
#
#---------------------------------------------------
print('VD page 26')
# Lấy thuộc tính width, height của đối tượng rec1
x = r1.width
y = r1.height

print('----Thuộc tính----------------')
print('1. Thuộc tính Chiều rộng: ', x)
print('2. Thuộc tính Chiều dài:   ', y)

# Gọi phương thức getArea, getPerimeter của đối tượng rec1
dt = r1.getArea()
cv = r1.getPerimeter()

print('------Phương thức---')
print('1. Phương thức tính Diện tích:', dt)
print('2. Phương thức tính Chu vi:  ', cv)

#
#---------------------------------------
print('VD page 37')
print('vd1')
# Mở file để đọc dữ liệu
f = open("Testfile.txt")
# Đọc nội dung của file vào biến st
st = f.read()
# In nội dung file
print("Nội dung file:")
print(st)
#--------------------------------------
print('vd2')
# Mở file để đọc dữ liệu
f = open("Testfile.txt", "r")
# Đọc 10 ký tự đầu tiên của file
st1 = f.read(15)
# In 10 ký tự đầu tiên
print(st1, "- Số ký tự là:", len(st1))
#

#---------------------------------
print('VD page 38')
# Mở file để đọc dữ liệu
f = open("Testfile.txt")

# Đọc từng dòng dữ liệu của file
print(f.readline())
print(f.readline())

# Đóng file dữ liệu
f.close()
#-------------------------------
# Mở file để đọc dữ liệu
f = open("Testfile.txt", "r")

# Đọc tất cả các dòng của file
for x in f:
    print(x)

# Đóng file dữ liệu
f.close()

#
#-------------------------------
print('VD page 39')
# Mở file với chế độ ghi đè (w):
# Nếu như file không tồn tại thì nó sẽ tạo mới file và ghi nội dung,
# còn nếu như file đã tồn tại nó sẽ ghi đè nội dung lên file cũ.
f1 = open("Ghifile.txt", "w")

# Dữ liệu muốn ghi vào file
st = 'Welcome to Python for Analysis!'

# Ghi dữ liệu vào file
f1.write(st)

# Đóng file
f1.close()
#

#------------------------------------
print('VD page 40')
# Mở file với chế độ ghi đè (w):
# Nếu như file không tồn tại thì nó sẽ tạo mới file và ghi nội dung,
# còn nếu như file đã tồn tại nó sẽ ghi đè nội dung lên file cũ.
f1 = open("Ghifile.txt", "w")

# Dữ liệu muốn ghi vào file
st = 'Welcome to Python for Analysis!'

# Ghi dữ liệu vào file
f1.write(st)

# Đóng file
f1.close()
#

#-------------------------------------------
print('DV page 40')
# Mở file với chế độ ghi tiếp (a):
# Nếu file đã tồn tại rồi thì nó sẽ ghi tiếp nội dung,
# và nếu như file chưa tồn tại thì nó sẽ tạo một file mới và ghi nội dung vào đó.
f1 = open("Ghifile.txt", "a+")

# Dữ liệu muốn ghi vào file
st = 'This is new line.....'

# Ghi tiếp dữ liệu vào file
f1.write(st)

# Đóng file
f1.close()

# open and read the file after the appending:
f = open("Ghifile.txt", "r")
print(f.read())
#

#--------------------------------
print('DV page 41')
# Lấy các thông số của file
f2 = open('Ghifile.txt')

print('1. Tên file: ', f2.name)
print('2. Chế độ mở file: ', f2.mode)
print('3. Trạng thái đóng file: ', f2.closed)

#
#--------------------------------
print('DV page 42')
# Mở file để ghi
fo = open("data.txt", "w")

# Ghi dữ liệu lên file
fo.write("Tobe or not tobe. \n Nghi lon de thanh cong ! \n")

# Đóng file
fo.close()

print("Ghi file thành công!")
#------------------------------------------
# Ghi dữ liệu vào file
obj = open("test.txt", "w")
obj.write("Chao mung cac ban den voi khoa CNTT")
obj.close()

# Đọc toàn bộ file
obj1 = open("test.txt", "r")
s = obj1.read()
print(s)
obj1.close()

# Đọc 20 ký tự đầu tiên
obj2 = open("test.txt", "r")
s1 = obj2.read(20)
print(s1)
obj2.close()

