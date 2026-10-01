import pandas as pd
import numpy as np

def main():
    # 1. Đọc dữ liệu từ file CSV
    data_path = 'data/data.csv'
    df = pd.read_csv(data_path)
    print("=== DỮ LIỆU ĐẦU VÀO ===")
    print(df.head(15))
    print("\n" + "="*40 + "\n")

    # 2. Khai báo trọng số mô hình w theo đề bài
    w0 = -33.73541021
    w1 = 0.55920496

    print(f"Mô hình Hồi quy tuyến tính: y = {w1} * x + ({w0})")
    print("\n" + "="*40 + "\n")

    # 3. Lấy ra dữ liệu kiểm thử (Dòng 4 và Dòng 6)
    test_rows = df[df['STT'].isin([4, 6])]

    print("=== KẾT QUẢ DỰ ĐOÁN VÀ KIỂM THỬ ===")
    for _, row in test_rows.iterrows():
        stt = int(row['STT'])
        height = row['Height']
        actual_weight = row['Weight']

        predicted_weight = w1 * height + w0
        error = abs(predicted_weight - actual_weight)

        print(f"STT {stt}:")
        print(f"  - Chiều cao (x): {height} cm")
        print(f"  - Cân nặng thực tế: {actual_weight} kg")
        print(f"  - Cân nặng dự đoán (y): {predicted_weight:.4f} kg")
        print(f"  - Sai số lệch (Error): {error:.4f} kg\n")

if __name__ == '__main__':
    main()
