ho_ten = input("Nhap ho ten: ")
nam_sinh = int(input("Nhap nam sinh: "))
diem_tb = float(input("Nhap diem trung binh: "))

print("Python", "la", "ngon", "ngu", "lap trinh", sep="-")
print("Dong 1", end=" | ")
print("Dong 2")

print(f"Ho ten: {ho_ten} Nam sinh: {nam_sinh} DTB: {diem_tb:.2f}")
print("Ho ten: {} Nam sinh: {} DTB: {:.2f}".format(ho_ten, nam_sinh, diem_tb))
print("Ho ten: %s Nam sinh: %d DTB: %.2f" % (ho_ten, nam_sinh, diem_tb))

# Chu thich mot dong: khai bao thong tin sinh vien
'''
Chu thich/docstring nhieu dong:
Chuong trinh quan ly diem sinh vien
Buoi 2
'''
ho_ten = "Tran Thi B" # bien luu ho ten

s1 = 'Xin chao'
s2 = "Ban co khoe khong?"
s3 = '''Day la
mot chuoi
nhieu dong'''
s4 = "Duong dan:\nC:\\Python\\data"
s5 = r"Duong dan raw: C:\Python\data"
s6 = "Toi ten la \"Nam\", con ban ten gi?"
print(s1); print(s2); print(s3); print(s4); print(s5); print(s6)
