# -*- coding: utf-8 -*-
"""
Chương trình huấn luyện Cây quyết định (Decision Tree) 
cho 2 bài toán: 
1. Buys Computer (ID3 và CART)
2. Rủi ro tín dụng (ID3 và CART)
"""

import pandas as pd
from sklearn.tree import DecisionTreeClassifier, export_text
from sklearn.preprocessing import LabelEncoder

print("=== BÀI TOÁN 1: BUYS COMPUTER ===")
df1 = pd.read_csv('buys_computer.csv')
print("Dữ liệu gốc:")
print(df1)

# Tiền xử lý mã hóa dữ liệu dạng chữ sang số cho Bài 1
df1_encoded = df1.copy()
le_dict1 = {}
for col in df1_encoded.columns:
    le = LabelEncoder()
    df1_encoded[col] = le.fit_transform(df1_encoded[col])
    le_dict1[col] = le

X1 = df1_encoded.drop(columns=['buys_computer'])
y1 = df1_encoded['buys_computer']

# 1. ID3 (Entropy)
clf_id3_1 = DecisionTreeClassifier(criterion='entropy', random_state=42)
clf_id3_1.fit(X1, y1)
print("\n--- Cây quyết định ID3 (Bài 1) ---")
print(export_text(clf_id3_1, feature_names=list(X1.columns)))

# 2. CART (Gini)
clf_cart_1 = DecisionTreeClassifier(criterion='gini', random_state=42)
clf_cart_1.fit(X1, y1)
print("\n--- Cây quyết định CART (Bài 1) ---")
print(export_text(clf_cart_1, feature_names=list(X1.columns)))


print("\n" + "="*40 + "\n")
print("=== BÀI TOÁN 2: RỦI RO TÍN DỤNG ===")
df2 = pd.read_csv('credit_risk.csv')
print("Dữ liệu gốc:")
print(df2)

df2_encoded = df2.drop(columns=['ID']).copy()
le_dict2 = {}
for col in df2_encoded.columns:
    if df2_encoded[col].dtype == 'object':
        le = LabelEncoder()
        df2_encoded[col] = le.fit_transform(df2_encoded[col])
        le_dict2[col] = le

X2 = df2_encoded.drop(columns=['Rui_ro_tin_dung'])
y2 = df2_encoded['Rui_ro_tin_dung']

# 1. ID3 (Entropy) cho Bài 2
clf_id3_2 = DecisionTreeClassifier(criterion='entropy', random_state=42)
clf_id3_2.fit(X2, y2)
print("\n--- Cây quyết định ID3 (Bài 2) ---")
print(export_text(clf_id3_2, feature_names=list(X2.columns)))

# 2. CART (Gini) cho Bài 2
clf_cart_2 = DecisionTreeClassifier(criterion='gini', random_state=42)
clf_cart_2.fit(X2, y2)
print("\n--- Cây quyết định CART (Bài 2) ---")
print(export_text(clf_cart_2, feature_names=list(X2.columns)))
