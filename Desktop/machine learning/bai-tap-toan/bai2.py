import numpy as np
from scipy.optimize import minimize

def g(x):
    """
    Bài 2: Hàm số g(x) = (1/3)x^3 - x
    Đạo hàm g'(x) = x^2 - 1 = 0 => x = -1 (cực đại), x = 1 (cực tiểu)
    """
    return (1/3) * x**3 - x

def main():
    print("========================================")
    print(" BÀI 2: TÌM GIÁ TRỊ CỰC TIỂU HÀM SỐ")
    print(" g(x) = (1/3)x^3 - x")
    print("========================================\n")

    # Khởi tạo điểm x0 = 1.0 (gần điểm cực tiểu lý thuyết x = 1)
    res = minimize(g, x0=1.0)
    
    print(f"Hàm số đạt cực tiểu tại x = {res.x[0]:.4f}")
    print(f"Giá trị cực tiểu g_min = {res.fun:.4f}\n")
    print("========================================")

if __name__ == "__main__":
    main()