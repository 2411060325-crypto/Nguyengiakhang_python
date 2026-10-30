import pandas as pd

df = pd.read_csv("diem_sinh_vien.csv")
print("5 dong dau:")
print(df.head())
print("So dong, so cot:", df.shape)
print("Ten cot:", df.columns.tolist())

diem_trung_binh_mon = df.groupby("mon_hoc")["diem"].mean()
print("\\nDiem trung binh theo mon:")
print(diem_trung_binh_mon)

print("\\nDiem trung binh toan bo:", df["diem"].mean())
print("Diem cao nhat:", df["diem"].max())
print("Diem thap nhat:", df["diem"].min())

diem_tb_sv = df.groupby("ho_ten")["diem"].mean().round(2)
print("\\nDiem trung binh tung sinh vien:")
print(diem_tb_sv)

print("\\nSinh vien dat:")
print(diem_tb_sv[diem_tb_sv >= 5.0])
print("\\nSinh vien khong dat:")
print(diem_tb_sv[diem_tb_sv < 5.0])
