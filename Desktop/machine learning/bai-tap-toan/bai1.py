import numpy as np
from scipy.optimize import minimize

def f(x):
    """
    Bài 1: Hàm số f(x) = x^2 - 2
    """
    return x**2 - 2

def main():
    print("========================================")
    print(" BÀI 1: TÌM GIÁ TRỊ CỰC TIỂU HÀM SỐ")
    print(" f(x) = x^2 - 2")
    print("========================================\n")

    # Khởi tạo điểm đoán x0 = 0.0
    res = minimize(f, x0=0.0)
    
    print(f"Hàm số đạt cực tiểu tại x = {res.x[0]:.4f}")
    print(f"Giá trị cực tiểu f_min = {res.fun:.4f}\n")
    print("========================================")

if __name__ == "__main__":
    main()