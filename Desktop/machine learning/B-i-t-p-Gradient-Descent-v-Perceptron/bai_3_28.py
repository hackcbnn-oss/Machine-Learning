"""
Bài 3.28: Cập nhật trọng số Perceptron
"""
import numpy as np

def perceptron_update():
    # Khởi tạo dữ liệu
    w = np.array([-2, 1, 0])
    x = np.array([2, 3, 1])
    y_true = 1
    
    # 1. Kiểm tra mẫu bị phân lớp sai hay không
    wTx = np.dot(w, x)
    y_pred = 1 if wTx >= 0 else -1
    
    print(f"Giá trị wTx ban đầu = {wTx}")
    print(f"Nhãn dự đoán ban đầu = {y_pred}")
    print(f"Nhãn thực tế = {y_true}")
    
    if y_pred != y_true:
        print("\n=> Kết luận 1: Mẫu bị phân lớp SAI. Cần cập nhật trọng số.")
        
        # 2. Thực hiện 1 bước cập nhật: w_new = w_old + y * x (learning_rate = 1)
        w_new = w + y_true * x
        print(f"\n2. Trọng số w sau cập nhật: {w_new}")
        
        # 3. Tính lại giá trị wTx sau cập nhật
        wTx_new = np.dot(w_new, x)
        y_pred_new = 1 if wTx_new >= 0 else -1
        print(f"3. Giá trị wTx sau cập nhật = {wTx_new}")
        print(f"   Nhãn dự đoán mới = {y_pred_new} (Đã dự đoán ĐÚNG so với nhãn thực tế y=1)")
    else:
        print("\n=> Mẫu phân lớp đúng, không cần cập nhật.")

if __name__ == "__main__":
    perceptron_update()
