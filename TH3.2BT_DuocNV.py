print('Bai 8: Xây dựng lớp Person')
class Person:
    def __init__(self, name="ChatGPT", year=2000, height=170, weight=65):
        # Phương thức khởi tạo __init__: Đây là nơi định nghĩa các thuộc tính của lớp.
        # Nếu không có giá trị nào được truyền vào, các giá trị mặc định sẽ được sử dụng.
        self.name = name           # Tên của Person
        self.year = year           # Năm sinh của Person
        self.height = height       # Chiều cao của Person (cm)
        self.weight = weight       # Cân nặng của Person (kg)

    def Getting(self):
        # Phương thức Getting: Hiển thị thông tin của Person
        # In ra các thuộc tính của đối tượng Person (họ tên, năm sinh, chiều cao và cân nặng)
        print(f"Name: {self.name}")
        print(f"Year of birth: {self.year}")
        print(f"Height: {self.height} cm")
        print(f"Weight: {self.weight} kg")

    def Bmi(self):
        # Phương thức Bmi: Tính toán chỉ số BMI của Person
        # Công thức BMI = weight (kg) / (height (m))^2
        # Chúng ta cần chuyển chiều cao từ cm sang mét trước khi tính toán BMI
        height_in_meters = self.height / 100  # Chuyển chiều cao từ cm sang mét
        bmi = self.weight / (height_in_meters ** 2)  # Công thức tính BMI
        return round(bmi, 2)  # Trả về giá trị BMI đã được làm tròn đến 2 chữ số thập phân

# Tạo một đối tượng Person với các giá trị mặc định
person = Person()

# Gọi phương thức Getting để hiển thị thông tin của Person
person.Getting()

# Gọi phương thức Bmi để tính chỉ số BMI và in ra kết quả
bmi_value = person.Bmi()
print(f"BMI: {bmi_value}")
#
#-------------------------------------------------
print('Bài 15:  Đọc/Ghi file')
# Bước 1: Đọc dữ liệu từ file "dayso1_bai17.txt"
try:
    with open("dayso1_bai17.txt", "r") as file:
        # Đọc dãy số từ file và chuyển thành danh sách các số nguyên
        numbers = list(map(int, file.read().split()))
except FileNotFoundError:
    print("File 'dayso1_bai17.txt' không tồn tại!")
    exit()

# Kiểm tra nếu file không có dữ liệu
if not numbers:
    print("Dãy số trong file rỗng!")
    exit()

# Bước 2: Tìm phần tử lớn nhất và nhỏ nhất trong dãy
max_value = max(numbers)
min_value = min(numbers)

# Tìm chỉ số của phần tử lớn nhất và nhỏ nhất xuất hiện đầu tiên
max_index = numbers.index(max_value)
min_index = numbers.index(min_value)

# Bước 3: Đổi chỗ phần tử lớn nhất và nhỏ nhất
numbers[max_index], numbers[min_index] = numbers[min_index], numbers[max_index]

# Bước 4: Lưu dãy số đã đổi chỗ vào file "dayso2_bai17.txt"
with open("dayso2_bai17.txt", "w") as file:
    file.write(" ".join(map(str, numbers)))

# In thông báo hoàn thành
print("Dãy số đã được đổi chỗ và lưu vào file 'dayso2_bai17.txt'.")
