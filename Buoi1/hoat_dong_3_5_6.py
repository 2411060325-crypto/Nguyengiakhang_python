
print("--- HOAT DONG 3: PEP8 ---")
ten = "Nguyen Van A"
diem_toan = 8.5
diem_van = 7.0
so_luong_mon_hoc = 2
MUC_LUONG_TOI_THIEU = 5000000  

print(f"Họ tên: {ten}")
print(f"Điểm Toán: {diem_toan}, Điểm Văn: {diem_van}")
print(f"Số lượng môn: {so_luong_mon_hoc}")
print(f"Mức lương tối thiểu: {MUC_LUONG_TOI_THIEU}\n")

print("--- HOAT DONG 4: TỪ KHÓA ---")
import keyword

print("Danh sách từ khóa:", keyword.kwlist)
print("Số lượng từ khóa:", len(keyword.kwlist), "\n")

print("--- HOAT DONG 5: TOÁN TỬ ---")

# Bài tập 5.1: Toán tử số học
a = 17
b = 5
print(f"a = {a}, b = {b}")
print("a + b =", a + b)
print("a - b =", a - b)
print("a * b =", a * b)
print("a / b =", a / b)      # Phép chia thực
print("a // b =", a // b)    # Phép chia lấy phần nguyên
print("a % b =", a % b)      # Phép chia lấy phần dư
print("a ** b =", a ** b)    # Phép lũy thừa

# Bài tập 5.2: Toán tử so sánh & logic
diem = 6.5
tuoi = 20
dat_loai_kha = (diem >= 6.5) and (diem < 8.0)
chua_du_18_hoac_tren_60 = (tuoi < 18) or (tuoi > 60)
phu_dinh_tuoi = not chua_du_18_hoac_tren_60

print(f"\nĐiểm đạt loại Khá?: {dat_loai_kha}")
print(f"Tuổi < 18 hoặc > 60?: {chua_du_18_hoac_tren_60}")
print(f"Phủ định điều kiện tuổi: {phu_dinh_tuoi}")

# Bài tập 5.3: Toán tử gán & toán tử đặc biệt
x = 10
x += 5
print(f"\nx sau khi += 5: {x}")
x -= 3
print(f"x sau khi -= 3: {x}")
x *= 2
print(f"x sau khi *= 2: {x}")
x /= 4
print(f"x sau khi /= 4: {x}")
x //= 2
print(f"x sau khi //= 2: {x}")
x **= 3
print(f"x sau khi **= 3: {x}")

danh_sach = [1, 2, 3, "python"]
print("3 có trong danh_sach không?:", 3 in danh_sach)

list_a = [1, 2, 3]
list_b = list_a
list_c = [1, 2, 3]
print("list_b is list_a (cùng vùng nhớ):", list_b is list_a)
print("list_c is list_a (khác vùng nhớ):", list_c is list_a)

# Bài tập 5.4: Độ ưu tiên toán tử
print("\nKết quả bài tập 5.4:")
print("2 + 3 * 4 ** 2 =", 2 + 3 * 4 ** 2)          # 2 + 3 * 16 = 50
print("(2 + 3) * 4 ** 2 =", (2 + 3) * 4 ** 2)      # 5 * 16 = 80
print("10 > 5 and 3 < 1 or not False =", 10 > 5 and 3 < 1 or not False)  # True and False or True -> True


print("\n--- HOAT DONG 6: BIẾN & DYNAMIC TYPING ---")

# Bài tập 6.1
bien = 10
print(bien, type(bien))
bien = "Xin chao"
print(bien, type(bien))
bien = 3.14
print(bien, type(bien))
bien = True
print(bien, type(bien))

# Bài tập 6.2: Mini bài toán tổng hợp
ho_ten = "Nguyen Van A"
diem_toan = 8.0
diem_ly = 7.5
diem_hoa = 9.0

dtb = (diem_toan + diem_ly + diem_hoa) / 3
la_gioi = dtb >= 8.0
la_kha = dtb >= 6.5 and dtb < 8.0
la_trung_binh = dtb >= 5.0 and dtb < 6.5
la_yeu = dtb < 5.0

print(f"\n{ho_ten} DTB: {round(dtb, 2)}")
print("Dat loai Gioi?", la_gioi)
print("Dat loai Kha?", la_kha)
print("Dat loai Trung binh?", la_trung_binh)
print("Dat loai Yeu?", la_yeu)
print("Kieu du lieu cua la_gioi:", type(la_gioi))