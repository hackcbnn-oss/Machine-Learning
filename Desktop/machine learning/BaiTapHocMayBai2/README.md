# Bài Toán Hồi Quy Tuyến Tính (Linear Regression)

Dự án nhỏ thực hành tính toán dự đoán cân nặng dựa trên chiều cao sử dụng thuật toán **Linear Regression**.

## 📌 Bài Toán & Mô Hình

Cho bảng dữ liệu gồm 15 mẫu chiều cao ($x$) and cân nặng ($y$). Sử dụng tập dữ liệu loại trừ dòng 4 và dòng 6 để huấn luyện mô hình, ta tìm được ma trận trọng số:

$$w = \begin{bmatrix} -33.73541021 \\ 0.55920496 \end{bmatrix}$$

Trong đó:
- $w_0 = -33.73541021$ (Bias)
- $w_1 = 0.55920496$ (Weight/Slope)

Phương trình dự đoán:
$$y = w_1 \cdot x + w_0$$

## 🧪 Kết Quả Kiểm Thử (Dòng 4 & Dòng 6)

- **Dòng 4** ($x = 155$ cm):
  $$y_1 = 0.55920496 \times 155 - 33.73541021 \approx 52.94\text{ kg}$$
  *(Thực tế: 52 kg | Sai số: 0.94 kg)*

- **Dòng 6** ($x = 160$ cm):
  $$y_2 = 0.55920496 \times 160 - 33.73541021 \approx 55.74\text{ kg}$$
  *(Thực tế: 56 kg | Sai số: 0.26 kg)*

## 🚀 Hướng Dẫn Chạy Dự Án

1. **Cài đặt thư viện phụ thuộc:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Chạy chương trình:**
   ```bash
   python main.py
   ```
