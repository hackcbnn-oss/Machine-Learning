import matplotlib.pyplot as plt
import numpy as np

# ==========================================
# 1. TẠO DỮ LIỆU GIẢ LẬP
# ==========================================
np.random.seed(2)

means = [[2, 2], [4, 2]]
cov = [[0.3, 0.2], [0.2, 0.3]]
N = 10

# Tạo 2 nhóm dữ liệu (2 classes)
X0 = np.random.multivariate_normal(means[0], cov, N).T
X1 = np.random.multivariate_normal(means[1], cov, N).T

# Gộp dữ liệu và tạo nhãn (1 và -1)
X = np.concatenate((X0, X1), axis=1)
y = np.concatenate((np.ones((1, N)), -1 * np.ones((1, N))), axis=1)

# Thêm Bias (1) vào đầu mỗi điểm dữ liệu
X = np.concatenate((np.ones((1, 2 * N)), X), axis=0)

# ==========================================
# 2. CÁC HÀM CHO THUẬT TOÁN PLA
# ==========================================
def h(w, x):
    """Hàm dự đoán nhãn"""
    return np.sign(np.dot(w.T, x))

def has_converged(X, y, w):
    """Kiểm tra xem tất cả các điểm đã được phân loại đúng chưa"""
    return np.array_equal(h(w, X), y)

def perceptron(X, y, w_init):
    """Thuật toán Perceptron"""
    w = [w_init]
    N = X.shape[1]
    d = X.shape[0]
    
    while True:
        mix_id = np.random.permutation(N)
        for i in range(N):
            xi = X[:, mix_id[i]].reshape(d, 1)
            yi = y[0, mix_id[i]]
            
            # Nếu dự đoán sai -> Cập nhật trọng số
            if h(w[-1], xi)[0] != yi:
                w_new = w[-1] + yi * xi
                w.append(w_new)
                
        # Dừng lại nếu đã phân loại đúng toàn bộ
        if has_converged(X, y, w[-1]):
            break
            
    return w

# ==========================================
# 3. CHẠY THUẬT TOÁN
# ==========================================
d = X.shape[0]
w_init = np.random.randn(d, 1)

# Lấy lịch sử cập nhật trọng số
w_history = perceptron(X, y, w_init)
w_final = w_history[-1]

print(f"Thuật toán hội tụ sau {len(w_history) - 1} lần cập nhật.")
print("Trọng số cuối cùng:\n", w_final)

# ==========================================
# 4. TRỰC QUAN HÓA (VẼ ĐỒ THỊ)
# ==========================================
plt.figure(figsize=(8, 6))

# Vẽ 2 nhóm dữ liệu
plt.plot(X0[0, :], X0[1, :], "b^", markersize=8, label="Lớp +1 (Xanh)")
plt.plot(X1[0, :], X1[1, :], "ro", markersize=8, label="Lớp -1 (Đỏ)")

# Vẽ đường ranh giới (Decision Boundary)
# Đường thẳng có phương trình: w0 + w1*x1 + w2*x2 = 0 => x2 = (-w0 - w1*x1)/w2
x1_vals = np.array([0, 6])
x2_vals = (-w_final[0] - w_final[1] * x1_vals) / w_final[2]

plt.plot(x1_vals, x2_vals, "k-", linewidth=2, label="Đường phân chia (PLA)")

# Cài đặt hiển thị đồ thị
plt.legend()
plt.title("Minh họa thuật toán Perceptron (PLA)")
plt.xlabel("Đặc trưng x1")
plt.ylabel("Đặc trưng x2")
plt.xlim(0, 6)
plt.ylim(0, 4)
plt.grid(True, linestyle='--', alpha=0.6)

# Hiển thị
plt.show()