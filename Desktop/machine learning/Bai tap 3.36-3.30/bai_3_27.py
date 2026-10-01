"""
Bài 3.27: Dự đoán nhãn với Perceptron
"""
import numpy as np

def perceptron_predict():
    # Khởi tạo vector trọng số w và vector dữ liệu x (đã có bias)
    w = np.array([1, 2, -10])
    x = np.array([3, 4, 1])
    y_true = -1 # Nhãn thực tế
    
    # 1. Tính w^T * x (Tích vô hướng)
    wTx = np.dot(w, x)
    print(f"1. Giá trị wTx = {wTx}")
    
    # 2. Xác định nhãn dự đoán (Hàm kích hoạt Sign)
    # Quy ước: Nếu wTx >= 0 thì nhãn là 1, ngược lại là -1
    y_pred = 1 if wTx >= 0 else -1
    print(f"2. Nhãn dự đoán y_pred = {y_pred}")
    
    # 3. Kiểm tra phân lớp sai
    is_misclassified = (y_pred != y_true)
    print("3. Điểm dữ liệu có bị phân lớp sai không?")
    if is_misclassified:
        print(f"   -> CÓ. Vì nhãn thực tế là {y_true} nhưng dự đoán là {y_pred}.")
    else:
        print("   -> KHÔNG.")

if __name__ == "__main__":
    perceptron_predict()
