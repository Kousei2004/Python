import numpy as np

# Đọc dữ liệu từ file, tách thành tên thành phố và nhiệt độ
thanh_pho = []
nhiet_do = []

with open('Temp.txt', 'r') as file:
    for line in file:
        data = line.strip().split()
        thanh_pho.append(data[0])  # Lấy tên thành phố (phần tử đầu tiên)
        nhiet_do.append([float(temp) for temp in data[1:]])  # Chuyển các số còn lại thành float

# Chuyển dữ liệu nhiệt độ thành mảng numpy để tính toán
mang_nhiet_do = np.array(nhiet_do)

# Tính các thống kê cho từng thành phố
nhiet_do_cao_nhat = np.max(mang_nhiet_do, axis=1)
nhiet_do_thap_nhat = np.min(mang_nhiet_do, axis=1)
nhiet_do_trung_binh = np.mean(mang_nhiet_do, axis=1)

# Tính thống kê tổng thể cho tất cả các thành phố
cao_nhat_tong = np.max(mang_nhiet_do)
thap_nhat_tong = np.min(mang_nhiet_do)
trung_binh_tong = np.mean(mang_nhiet_do)

# Hiển thị kết quả
print("Thống kê theo từng thành phố:")
print("-" * 50)
for i, tp in enumerate(thanh_pho):
    print(f"Thành phố {tp}:")
    print(f"  Nhiệt độ cao nhất: {nhiet_do_cao_nhat[i]:.1f}")
    print(f"  Nhiệt độ thấp nhất: {nhiet_do_thap_nhat[i]:.1f}")
    print(f"  Nhiệt độ trung bình: {nhiet_do_trung_binh[i]:.1f}")
    print()

print("Thống kê tổng thể:")
print("-" * 50)
print(f"Nhiệt độ cao nhất trong tất cả các thành phố: {cao_nhat_tong:.1f}")
print(f"Nhiệt độ thấp nhất trong tất cả các thành phố: {thap_nhat_tong:.1f}")
print(f"Nhiệt độ trung bình của tất cả các thành phố: {trung_binh_tong:.1f}")