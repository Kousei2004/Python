# Phần 1: Bài toán phân lớp với Decision Tree
import numpy as np
from sklearn.datasets import make_classification
from sklearn.tree import DecisionTreeClassifier

# Tạo dataset cho bài toán phân lớp
print("=== Bài toán phân lớp ===")
X_clf, y_clf = make_classification(
    n_samples=1000,      # 1000 mẫu
    n_features=8,        # 8 đặc trưng
    n_classes=2,         # 2 lớp
    random_state=42      # Để kết quả có thể tái tạo lại được
)

# Tạo và huấn luyện mô hình Decision Tree
dt_model = DecisionTreeClassifier(random_state=42)
dt_model.fit(X_clf, y_clf)

# In kết quả
print(f"Kích thước dữ liệu: {X_clf.shape}")
print(f"Số lượng mẫu cho mỗi lớp: {np.bincount(y_clf)}")
print(f"Độ chính xác của mô hình: {dt_model.score(X_clf, y_clf):.4f}")

# Phần 2: Bài toán phân cụm và trực quan hóa
import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs

def create_cluster_dataset(cluster_std):
    # Tạo dataset
    X, y = make_blobs(
        n_samples=10000,     # 10000 mẫu
        n_features=2,        # 2 đặc trưng
        centers=5,           # 5 tâm cụm
        cluster_std=cluster_std,  # Độ phân tán của cụm
        random_state=42
    )
    
    # Vẽ biểu đồ scatter
    plt.figure(figsize=(10, 6))
    plt.scatter(X[:, 0], X[:, 1], c=y, cmap='viridis')
    plt.colorbar()
    plt.title(f'Biểu đồ phân cụm (cluster_std={cluster_std})')
    plt.xlabel('Feature 1')
    plt.ylabel('Feature 2')
    plt.show()
    
    return X, y

print("\n=== Bài toán phân cụm ===")
# Tạo dataset với cluster_std = 0.5
X_cluster, y_cluster = create_cluster_dataset(0.5)
print(f"Kích thước dữ liệu phân cụm: {X_cluster.shape}")
print(f"Số lượng cụm: {len(np.unique(y_cluster))}")

# Thử nghiệm với các giá trị cluster_std khác nhau
print("\nThử nghiệm với các giá trị cluster_std khác nhau:")
std_values = [0.1, 0.3, 0.7, 1.0]
for std in std_values:
    print(f"\nTạo dataset với cluster_std = {std}")
    X, y = create_cluster_dataset(std)

print("\nNhận xét về ảnh hưởng của tham số cluster_std:")
print("1. cluster_std = 0.1: Các cụm rất tập trung, ranh giới rõ ràng")
print("2. cluster_std = 0.3: Các cụm vẫn tách biệt nhưng bắt đầu có sự phân tán")
print("3. cluster_std = 0.5: Các cụm phân tán vừa phải, vẫn có thể phân biệt được")
print("4. cluster_std = 0.7: Các cụm bắt đầu có sự chồng lấn")
print("5. cluster_std = 1.0: Các cụm chồng lấn nhiều, khó phân biệt ranh giới")