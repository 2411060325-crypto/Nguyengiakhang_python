import math

so_nguyen = 15
so_thuc = 4.2
so_phuc = 3+4j
print(type(so_nguyen), type(so_thuc), type(so_phuc))
print(float(so_nguyen)) # ep int -> float
print(int(so_thuc)) # ep float -> int (cat phan thap phan)

a = -7
b = 2.6789
c, d = 17, 5
print(abs(a)) # gia tri tuyet doi
print(round(b)) # lam tron
print(round(b, 2)) # lam tron 2 chu so thap phan
print(pow(c, 2)) # c mu 2
print(divmod(c, d)) # tra ve (thuong, du) dang tuple

a_pt, b_pt, c_pt = 1, -3, 2
delta = b_pt**2 - 4*a_pt*c_pt
x1 = (-b_pt + math.sqrt(delta)) / (2 * a_pt)
x2 = (-b_pt - math.sqrt(delta)) / (2 * a_pt)
print(f"Delta = {delta}")
print(f"Nghiem x1 = {round(x1, 2)}, x2 = {round(x2, 2)}")

cau = "Lap trinh Python rat thu vi"
print(cau[0]) # ky tu dau tien
print(cau[-1]) # ky tu cuoi cung
print(cau[4:10]) # cat tu vi tri 4 den truoc vi tri 10
print(cau[:8]) # tu dau den vi tri 8
print(cau[11:]) # tu vi tri 11 den het
print(cau[::-1]) # dao nguoc chuoi

ten = "Nam"
ten_moi = "T" + ten[1:]
print(ten_moi)

cau2 = "   Toi dang HOC Python rat vui   "
print(cau2.strip()) # bo khoang trang 2 dau
print(cau2.strip().upper()) # in hoa toan bo
print(cau2.strip().lower()) # in thuong toan bo
print(cau2.strip().replace("HOC", "hoc"))
print(cau2.strip().split()) # tach thanh danh sach cac tu
print(len(cau2.strip().split())) # dem so tu trong cau
print(cau2.count("o")) # dem so lan xuat hien ky tu 'o'
print(cau2.find("Python")) # vi tri bat dau cua "Python"
print(cau2.strip().startswith("Toi"))
print(cau2.strip().endswith("vui"))
print("-".join(["Python", "that", "thu", "vi"]))

ho_ten_tho = "   nguyen   van an   "
ho_ten_sach = " ".join(ho_ten_tho.split()).title()
print(ho_ten_sach) # Nguyen Van An
