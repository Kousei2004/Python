import numpy as np

# Ma trận Height và Weight có sẵn
matrix_height = np.array([
    [6, 1, 4, 4, 8, 4, 6, 3, 5, 8],
    [7, 9, 9, 2, 7, 8, 8, 9, 2, 6],
    [5, 3, 4, 9, 6, 5, 3, 7, 9, 2],
    [9, 6, 1, 8, 4, 6, 2, 7, 1, 3],
    [2, 8, 7, 3, 9, 5, 3, 2, 8, 6],
    [7, 2, 4, 1, 5, 8, 7, 9, 3, 6],
    [3, 6, 7, 2, 4, 9, 1, 5, 8, 2],
    [4, 1, 3, 7, 8, 9, 5, 2, 6, 7],
    [2, 4, 5, 9, 7, 8, 1, 3, 6, 8],
    [8, 9, 6, 4, 3, 2, 7, 5, 4, 6]
])

matrix_weight = np.array([
    [4, 8, 1, 3, 5, 8, 6, 3, 7, 8],
    [4, 6, 3, 5, 8, 4, 7, 9, 9, 1],
    [7, 2, 5, 1, 4, 6, 9, 8, 3, 5],
    [9, 6, 4, 7, 8, 2, 5, 3, 6, 4],
    [6, 2, 7, 3, 9, 5, 1, 4, 8, 2],
    [7, 4, 9, 5, 8, 3, 7, 8, 6, 1],
    [8, 9, 4, 6, 5, 1, 9, 7, 2, 6],
    [2, 1, 3, 4, 7, 5, 2, 8, 6, 3],
    [5, 3, 8, 1, 2, 9, 7, 4, 6, 9],
    [9, 8, 6, 4, 3, 7, 5, 3, 1, 2]
])

# Kiểm tra khả nghịch của ma trận bằng cách tính hạng của nó
rank_height = np.linalg.matrix_rank(matrix_height)
rank_weight = np.linalg.matrix_rank(matrix_weight)

# Kiểm tra xem ma trận có khả nghịch không và tính nghịch đảo nếu có
def calculate_inverse(matrix, name):
    try:
        inverse_matrix = np.linalg.inv(matrix)
        print(f"\nMa trận nghịch đảo của {name}:")
        print(inverse_matrix)
    except np.linalg.LinAlgError:
        print(f"\nMa trận {name} không khả nghịch.")

# Tính nghịch đảo cho ma trận Height và Weight
calculate_inverse(matrix_height, "Height")
calculate_inverse(matrix_weight, "Weight")

# Hiển thị hạng của ma trận
print("\nHạng của ma trận Height:", rank_height)
print("Hạng của ma trận Weight:", rank_weight)
