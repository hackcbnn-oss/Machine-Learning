"""
Bài 3.30: Áp dụng Perceptron vào bài toán phân lớp nhị phân thực tế
Dataset: Breast Cancer (Phân loại khối u Lành tính / Ác tính)
"""
import numpy as np
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

# Import Class Perceptron tự viết từ file bai_3_29.py
from bai_3_29 import Perceptron

def main():
    print("--- ĐANG TẢI DỮ LIỆU BREAST CANCER ---")
    data = datasets.load_breast_cancer()
    X = data.data
    y = data.target # Nhãn: 0 (Malignant - Ác tính), 1 (Benign - Lành tính)

    # Chuyển đổi nhãn từ {0, 1} sang {-1, 1} để phù hợp với hàm kích hoạt của Perceptron
    y_converted = np.where(y == 0, -1, 1)

    print("--- CHIA TẬP DỮ LIỆU (80% Train, 20% Test) ---")
    X_train, X_test, y_train, y_test = train_test_split(
        X, y_converted, test_size=0.2, random_state=42
    )

    print("--- HUẤN LUYỆN MÔ HÌNH PERCEPTRON ---")
    # Khởi tạo mô hình
    p = Perceptron(learning_rate=0.01, n_iterations=1000)
    # Huấn luyện
    p.fit(X_train, y_train)

    print("--- ĐANG DỰ BÁO VÀ ĐÁNH GIÁ ---")
    # Dự báo trên tập Test
    predictions = p.predict(X_test)

    # Tính toán các độ đo (Metrics)
    accuracy = accuracy_score(y_test, predictions)
    precision = precision_score(y_test, predictions)
    recall = recall_score(y_test, predictions)
    f1 = f1_score(y_test, predictions)

    print("\n" + "="*50)
    print("KẾT QUẢ ĐÁNH GIÁ MÔ HÌNH TRÊN TẬP TEST:")
    print("="*50)
    print(f"1. Accuracy  (Độ chính xác)  : {accuracy:.4f}")
    print(f"2. Precision (Độ chuẩn xác)  : {precision:.4f}")
    print(f"3. Recall    (Độ nhạy/bao phủ): {recall:.4f}")
    print(f"4. F1-score  (Điểm F1)       : {f1:.4f}")
    print("="*50)

if __name__ == "__main__":
    main()
