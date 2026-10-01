# Bài Tập Tìm Giá Trị Cực Tiểu Hàm Số (Python)

Dự án chứa 2 script Python độc lập giải hai bài toán tìm giá trị cực tiểu của hàm số bằng thư viện `scipy`.

## 📌 Cấu Trúc Dự Án

* `bai1.py`: Giải **Bài 1** — Tìm giá trị cực tiểu của $f(x) = x^2 - 2$
* `bai2.py`: Giải **Bài 2** — Tìm giá trị cực tiểu của $g(x) = \frac{1}{3}x^3 - x$

---

## 🛠️ Hướng Dẫn Cài Đặt & Chạy Code

### 1. Cài đặt thư viện cần thiết
Mở Terminal / Command Prompt tại thư mục dự án và chạy:
```bash
pip install numpy scipy
```

### 2. Chạy bài 1
```bash
python bai1.py
```

### 3. Chạy bài 2
```bash
python bai2.py
```

---

## 🚀 Hướng Dẫn Chi Tiết Cách Đẩy Code Lên GitHub

### Bước 1: Chuẩn bị thư mục trên máy tính
1. Tạo 1 thư mục mới trên máy tính (ví dụ tên là `bai-tap-toan`).
2. Lưu 3 file (`bai1.py`, `bai2.py`, `README.md`) vào thư mục này.

### Bước 2: Tạo Repository trên GitHub
1. Mở trang web [GitHub.com](https://github.com) và đăng nhập tài khoản.
2. Nhấn nút **New** (hoặc dấu **+** ở góc phải trên -> chọn **New repository**).
3. Đặt tên tại mục **Repository name**: `bai-tap-cuc-tieu`.
4. Để chế độ **Public**.
5. **Lưu ý:** KHÔNG tích chọn *Add a README file*, *Add .gitignore* hay *Choose a license*.
6. Nhấn nút **Create repository**.

### Bước 3: Đưa Code lên GitHub từ máy tính
Mở Terminal / Command Prompt ngay tại thư mục `bai-tap-toan` và copy từng lệnh sau để chạy:

```bash
# 1. Khởi tạo Git cục bộ
git init

# 2. Thêm tất cả các file vào Git
git add .

# 3. Lưu phiên bản code (Commit)
git commit -m "Khoi tao du an bai tap cuc tieu"

# 4. Đổi tên nhánh chính thành main
git branch -M main

# 5. Liên kết với GitHub (Thay link_repo_cua_ban bằng link URL thực tế trên GitHub)
git remote add origin https://github.com/USERNAME/bai-tap-cuc-tieu.git

# 6. Push (đẩy) code lên GitHub
git push -u origin main
```