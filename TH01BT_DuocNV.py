#Bài 1
# Nhập số lượng kẹo và số học sinh
n = int(input("Nhập vào số lượng kẹo của cô (N): "))
m = int(input("Nhập vào số học sinh trong lớp (M): "))

# Tính số kẹo mỗi học sinh nhận được và số kẹo còn lại
so_keo_moi_hs = n // m
keo_con_lai = n % m

# Hiển thị kết quả
print(f"Mỗi học sinh được nhận: {so_keo_moi_hs} cái kẹo")
print(f"Số kẹo cô còn lại: {keo_con_lai} cái kẹo")

#Bài 2
from datetime import datetime

# Nhập họ tên và năm sinh
ho_ten = input("Nhập vào họ tên: ")
nam_sinh = int(input("Nhập vào năm sinh: "))

# Lấy năm hiện tại
nam_hien_tai = datetime.now().year

# Tính tuổi
tuoi = nam_hien_tai - nam_sinh

# Hiển thị kết quả
print(f"Bạn \"{ho_ten.upper()}\" năm nay {tuoi} tuổi!")

#Bài 3
# Nhập số tháng từ người dùng
x = int(input("Nhập vào số tháng x: "))

# Giả sử ban đầu có 1 cặp thỏ (2 con thỏ)
so_tho_ban_dau = 2

# Tính số thỏ sau x tháng
so_tho_sau_x_thang = so_tho_ban_dau * (2 ** x)

# Hiển thị kết quả
print(f"Trong rừng có: {so_tho_sau_x_thang} con thỏ")

#Bài 3
import re

# Đoạn văn cần xử lý
doan_van = """
Nước Việt Nam là một, dân tộc Việt Nam là một. Sông có thể cạn núi có thể mòn, song chân lý ấy không bao giờ thay đổi. (HỒ CHÍ MINH, 1890 – 1969)
"""

# 1. Cho biết số ký tự trong đoạn văn
so_ky_tu = len(doan_van)
print(f"Số ký tự trong đoạn văn: {so_ky_tu}")

# 2. Kiểm tra có chứa từ "hồ chí minh" và "non sông" (không phân biệt hoa thường)
tu_can_tim = ["hồ chí minh", "non sông"]
for tu in tu_can_tim:
    if re.search(tu, doan_van, re.IGNORECASE):
        print(f"Đoạn văn có chứa từ: '{tu}'")
    else:
        print(f"Đoạn văn không chứa từ: '{tu}'")

# 3. Tách đoạn văn thành các câu bởi dấu chấm
cau_boi_dau = re.split(r'\.\s*', doan_van.strip())
print("Các câu trong đoạn văn:")
for i, cau in enumerate(cau_boi_dau):
    if cau:  # Bỏ qua các câu rỗng
        print(f"Câu {i + 1}: {cau}")

# 4. Kiểm tra có ký tự nào khác ký tự chữ và số hay không
ky_tu_khac = re.findall(r'[^a-zA-Z0-9\s]', doan_van)
if ky_tu_khac:
    print("Đoạn văn có chứa các ký tự khác chữ và số:", ''.join(set(ky_tu_khac)))
else:
    print("Đoạn văn không có ký tự khác chữ và số.")

# 5. Thay thế các từ "Việt Nam" bằng "VIỆT NAM"
doan_van_thay_the = doan_van.replace("Việt Nam", "VIỆT NAM")
print("Đoạn văn sau khi thay thế:")
print(doan_van_thay_the)

#Bài 5
grades = ['C', 'B', 'D', 'A', 'F', 'A', 'B', 'F', 'B', 'B', 'C', 'A', 'D', 'F', 'B']

total_students = len(grades)
print("1.Tổng số học sinh trong lớp:", total_students)

failed_students = grades.count('F')
print("2.Số học sinh phải học lại là:", failed_students)

b_or_higher = sum(1 for grade in grades if grade in ['A', 'B'])
print("3.Số học sinh có điểm từ B trở lên là:", b_or_higher)

new_grades = grades[1:-1]
print("4.Bảng điểm mới:", new_grades)

print("\nBảng điểm lớp Japan01:")
print(grades)
print("-" * 10 + "THỐNG KÊ" + "-" * 10)
print(f"1.Tổng số học sinh trong lớp: {total_students}")
print(f"2.Số học sinh phải học lại là: {failed_students}")
print(f"3.Số học sinh có điểm từ B trở lên là: {b_or_higher}")
print(f"4.Bảng điểm mới: {new_grades}")