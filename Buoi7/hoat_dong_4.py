# Danh sach phong
danh_sach_phong = [
    {"ma_phong": "P101", "loai_phong": "Don", "gia": 300000, "trang_thai": "Trong", "ten_khach": ""},
    {"ma_phong": "P102", "loai_phong": "Doi", "gia": 500000, "trang_thai": "Trong", "ten_khach": ""},
    {"ma_phong": "P103", "loai_phong": "VIP", "gia": 900000, "trang_thai": "Trong", "ten_khach": ""},
    {"ma_phong": "P104", "loai_phong": "Don", "gia": 300000, "trang_thai": "Trong", "ten_khach": ""}
]

# Lich su doanh thu
lich_su_doanh_thu = []


# 1. Hien thi danh sach phong
def hien_thi_danh_sach_phong():
    print("\n" + "=" * 75)
    print(f"{'Ma phong':<12}{'Loai phong':<15}{'Gia/dem':<18}{'Trang thai':<15}{'Khach':<15}")
    print("-" * 75)

    for phong in danh_sach_phong:
        print(f"{phong['ma_phong']:<12}{phong['loai_phong']:<15}"
              f"{phong['gia']:>10,} VND  "
              f"{phong['trang_thai']:<12}{phong['ten_khach']:<15}")

    print("=" * 75)


# 2. Tim phong theo ma
def tim_phong_theo_ma(ma_phong):
    for phong in danh_sach_phong:
        if phong["ma_phong"] == ma_phong:
            return phong
    return None


# 3. Xem phong trong
def xem_phong_trong():
    phong_trong = []

    for phong in danh_sach_phong:
        if phong["trang_thai"] == "Trong":
            phong_trong.append(phong)

    if len(phong_trong) == 0:
        print("Hien khong con phong trong nao.")
        return

    print("\nCAC PHONG DANG TRONG:")
    for phong in phong_trong:
        print(f"{phong['ma_phong']} - {phong['loai_phong']} - "
              f"{phong['gia']:,} VND/dem")


# 4. Them phong
def them_phong(ma_phong, loai_phong, gia):
    if tim_phong_theo_ma(ma_phong) is not None:
        print(f"Ma phong {ma_phong} da ton tai, khong the them.")
        return

    danh_sach_phong.append({
        "ma_phong": ma_phong,
        "loai_phong": loai_phong,
        "gia": gia,
        "trang_thai": "Trong",
        "ten_khach": ""
    })

    print(f"Da them phong {ma_phong} thanh cong.")


# 5. Dat phong
def dat_phong(ma_phong, ten_khach):
    phong = tim_phong_theo_ma(ma_phong)

    if phong is None:
        print(f"Khong tim thay phong {ma_phong}.")
        return

    if phong["trang_thai"] == "Da dat":
        print(f"Phong {ma_phong} da co khach, khong the dat.")
        return

    phong["trang_thai"] = "Da dat"
    phong["ten_khach"] = ten_khach

    print(f"Dat phong {ma_phong} cho khach {ten_khach} thanh cong.")


# 6. Tra phong
def tra_phong(ma_phong, so_dem):
    phong = tim_phong_theo_ma(ma_phong)

    if phong is None:
        print(f"Khong tim thay phong {ma_phong}.")
        return

    if phong["trang_thai"] == "Trong":
        print(f"Phong {ma_phong} dang trong, khong co khach de tra.")
        return

    if so_dem <= 0:
        print("So dem phai lon hon 0.")
        return

    thanh_tien = phong["gia"] * so_dem

    lich_su_doanh_thu.append({
        "ma_phong": ma_phong,
        "ten_khach": phong["ten_khach"],
        "so_dem": so_dem,
        "thanh_tien": thanh_tien
        })

    print(f"Khach {phong['ten_khach']} tra phong {ma_phong} sau {so_dem} dem.")
    print(f"Tong tien phai thanh toan: {thanh_tien:,} VND")

    phong["trang_thai"] = "Trong"
    phong["ten_khach"] = ""


# 7. Hien thi lich su doanh thu
def hien_thi_doanh_thu():
    if len(lich_su_doanh_thu) == 0:
        print("Chua co lich su doanh thu.")
        return

    tong_doanh_thu = 0

    print("\nLICH SU DOANH THU")
    print("-" * 75)

    for lich_su in lich_su_doanh_thu:
        print(f"Phong: {lich_su['ma_phong']} | "
              f"Khach: {lich_su['ten_khach']} | "
              f"So dem: {lich_su['so_dem']} | "
              f"Tien: {lich_su['thanh_tien']:,} VND")

        tong_doanh_thu += lich_su["thanh_tien"]

    print("-" * 75)
    print(f"TONG DOANH THU: {tong_doanh_thu:,} VND")


# 8. Chuong trinh chinh
def menu():
    while True:
        print("\n========== QUAN LY KHACH SAN ==========")
        print("1. Hien thi danh sach phong")
        print("2. Xem phong trong")
        print("3. Them phong")
        print("4. Dat phong")
        print("5. Tra phong")
        print("6. Xem lich su doanh thu")
        print("0. Thoat")

        lua_chon = input("Nhap lua chon: ")

        if lua_chon == "1":
            hien_thi_danh_sach_phong()

        elif lua_chon == "2":
            xem_phong_trong()

        elif lua_chon == "3":
            ma_phong = input("Nhap ma phong: ")
            loai_phong = input("Nhap loai phong (Don/Doi/VIP): ")

            try:
                gia = int(input("Nhap gia phong moi dem: "))

                if gia <= 0:
                    print("Gia phong phai lon hon 0.")
                else:
                    them_phong(ma_phong, loai_phong, gia)

            except ValueError:
                print("Gia phong phai la mot so nguyen.")

        elif lua_chon == "4":
            ma_phong = input("Nhap ma phong muon dat: ")
            ten_khach = input("Nhap ten khach hang: ")

            if ten_khach.strip() == "":
                print("Ten khach hang khong duoc de trong.")
            else:
                dat_phong(ma_phong, ten_khach)

        elif lua_chon == "5":
            ma_phong = input("Nhap ma phong muon tra: ")

            try:
                so_dem = int(input("Nhap so dem da o: "))
                tra_phong(ma_phong, so_dem)

            except ValueError:
                print("So dem phai la mot so nguyen.")

        elif lua_chon == "6":
            hien_thi_doanh_thu()

        elif lua_chon == "0":
            print("Da thoat chuong trinh.")
            break

        else:
            print("Lua chon khong hop le, vui long nhap lai.")


# Chay chuong trinh
menu()