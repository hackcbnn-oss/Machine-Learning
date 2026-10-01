"""
Bài 3.26: Thuật toán Gradient Descent
Hàm số: f(x) = x^2 - 4x + 5
"""

# 1. Định nghĩa hàm số và đạo hàm
def f(x):
    return x**2 - 4*x + 5

def df(x):
    # Đạo hàm f'(x) = 2x - 4
    return 2*x - 4

def gradient_descent():
    # Điểm khởi tạo và tham số
    x = 5.0
    learning_rate = 0.2
    n_steps = 4
    
    print(f"Bước 0 (Khởi tạo): x = {x:.4f}, f(x) = {f(x):.4f}")
    
    # 2 & 3. Thực hiện cập nhật và tính giá trị
    for i in range(1, n_steps + 1):
        grad = df(x)
        x = x - learning_rate * grad # Cập nhật x
        
        print(f"Bước {i}: x = {x:.4f}, Đạo hàm = {grad:.4f}, f(x) = {f(x):.4f}")
        
    # 4. Nhận xét
    print("\n[Nhận xét]")
    print("Sau 4 bước, giá trị x giảm dần từ 5 về gần 2 (điểm cực tiểu).")
    print("Giá trị hàm f(x) giảm dần từ 10 về 1.15.")
    print("=> Thuật toán Gradient Descent đang hội tụ chính xác về Global Minimum.")

if __name__ == "__main__":
    gradient_descent()
