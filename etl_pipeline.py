import pandas as pd
import sqlite3

# -----------------------------
# 1. Extract: قراءة البيانات من ملف CSV
# -----------------------------
data = pd.read_csv("sales_data.csv")

print("✅ Data Extracted Successfully!")
print(data.head())

# -----------------------------
# 2. Transform: تنظيف البيانات
# -----------------------------
# إزالة القيم الفارغة
data.dropna(inplace=True)

# تعديل أسماء الأعمدة (مسافة -> Underscore)
data.columns = [col.strip().replace(" ", "_").lower() for col in data.columns]

print("✅ Data Transformed Successfully!")
print(data.head())

# -----------------------------
# 3. Load: تحميل البيانات داخل SQLite
# -----------------------------
conn = sqlite3.connect("sales.db")
data.to_sql("sales", conn, if_exists="replace", index=False)

print("✅ Data Loaded Successfully into SQLite Database!")