import numpy as np
import pandas as pd
from scipy import stats
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['Arial Unicode MS']  # Hỗ trợ tiếng Việt

# Dữ liệu 1: Diện tích và Giá
du_lieu_1 = {
    'dien_tich': [1460, 2108, 1743, 1499, 1864, 2391, 1977, 1610, 1530, 1759, 1821, 2216],
    'gia': [288700, 309300, 301400, 291100, 302400, 314900, 305400, 297000, 292400, 298200, 304300, 311700]
}

# Dữ liệu 2: Khoảng cách và Giá
du_lieu_2 = {
    'khoang_cach': [2.6, 0.8, 1.0, 0.6, 1.5, 2.0, 3.4, 1.2, 3.6, 1.7],
    'gia': [214, 376, 280, 362, 200, 190, 236, 244, 128, 165]
}

# Tạo DataFrame
df1 = pd.DataFrame(du_lieu_1)
df2 = pd.DataFrame(du_lieu_2)

# Tính hệ số tương quan Pearson
tuong_quan_1 = stats.pearsonr(df1['dien_tich'], df1['gia'])
tuong_quan_2 = stats.pearsonr(df2['khoang_cach'], df2['gia'])

# Tạo biểu đồ
plt.figure(figsize=(12, 5))

# Biểu đồ 1: Diện tích và Giá
plt.subplot(1, 2, 1)
plt.scatter(df1['dien_tich'], df1['gia'])
plt.xlabel('Diện tích (feet vuông)')
plt.ylabel('Giá ($)')
plt.title(f'Diện tích và Giá\nHệ số tương quan: {tuong_quan_1[0]:.3f}')

# Biểu đồ 2: Khoảng cách và Giá
plt.subplot(1, 2, 2)
plt.scatter(df2['khoang_cach'], df2['gia'])
plt.xlabel('Khoảng cách từ trung tâm (dặm)')
plt.ylabel('Giá (nghìn $)')
plt.title(f'Khoảng cách và Giá\nHệ số tương quan: {tuong_quan_2[0]:.3f}')

# In kết quả
print("Kết quả phân tích tương quan:")
print(f"\nDữ liệu 1 - Diện tích và Giá:")
print(f"Hệ số tương quan: {tuong_quan_1[0]:.3f}")
print(f"Giá trị P: {tuong_quan_1[1]:.3f}")

print(f"\nDữ liệu 2 - Khoảng cách từ trung tâm và Giá:")
print(f"Hệ số tương quan: {tuong_quan_2[0]:.3f}")
print(f"Giá trị P: {tuong_quan_2[1]:.3f}")