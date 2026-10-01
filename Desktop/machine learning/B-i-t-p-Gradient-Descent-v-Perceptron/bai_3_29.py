"""
Bài 3.29: Xây dựng class Perceptron bằng Python (OOP)
Lưu ý: File này đóng vai trò như một thư viện tự viết, sẽ được import vào bài 3.30.
"""
import numpy as np

class Perceptron:
    def __init__(self, learning_rate=0.01, n_iterations=1000):
        self.learning_rate = learning_rate
        self.n_iterations = n_iterations
        self.weights = None
        self.bias = None

    def fit(self, X, y):
        # Lấy số lượng mẫu và số lượng đặc trưng
        n_samples, n_features = X.shape
        
        # Khởi tạo trọng số (weights) và bias bằng 0
        self.weights = np.zeros(n_features)
        self.bias = 0

        # Chuẩn hóa nhãn y về định dạng {-1, 1}
        y_ = np.where(y <= 0, -1, 1)

        # Quá trình huấn luyện (Training)
        for _ in range(self.n_iterations):
            for idx, x_i in enumerate(X):
                # Tính tích vô hướng: w*x + bias
                linear_output = np.dot(x_i, self.weights) + self.bias
                
                # Cập nhật nếu dự đoán sai (y * f(x) <= 0)
                if y_[idx] * linear_output <= 0:
                    update = self.learning_rate * y_[idx]
                    self.weights += update * x_i
                    self.bias += update

    def predict(self, X):
        # Tính toán output tuyến tính cho toàn bộ tập X
        linear_output = np.dot(X, self.weights) + self.bias
        # Trả về nhãn 1 nếu >= 0, ngược lại trả về -1
        return np.where(linear_output >= 0, 1, -1)

if __name__ == "__main__":
    print("Class Perceptron đã được định nghĩa thành công!")
    print("Hãy chạy file bai_3_30.py để xem class này hoạt động trên tập dữ liệu thực tế.")
