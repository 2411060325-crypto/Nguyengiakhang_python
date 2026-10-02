danh_sach_sinh_vien = [
    {"ma_sv": "SV001", "ho_ten": "Nguyen Van An", "tuoi": 20, "diem": 8.5},
    {"ma_sv": "SV002", "ho_ten": "Tran Thi Binh", "tuoi": 19, "diem": 7.5},
    {"ma_sv": "SV003", "ho_ten": "Le Van Nam", "tuoi": 21, "diem": 9.0}
]

def hien_thi_danh_sach():
    if len(danh_sach_sinh_vien) == 0:
        print("-> Danh sach sinh vien dang trong.")
        return

    print("\n" + "=" * 65)
    print(f"{'Ma SV':<10}{'Ho ten':<25}{'Tuoi':<10}{'Diem':<10}")
    print("-" * 65)

    for sv in danh_sach_sinh_vien:
        print(f"{sv['ma_sv']:<10}{sv['ho_ten']:<25}{sv['tuoi']:<10}{sv['diem']:<10}")

    print("=" * 65)


def tim_sinh_vien(ma_sv):
    for sv in danh_sach_sinh_vien:
        if sv["ma_sv"] == ma_sv:
            return sv
    return None


def nhap_so_nguyen(loi_nhac):
    while True:
        try:
            return int(input(loi_nhac))
        except ValueError:
            print("-> Du lieu khong hop le, vui long nhap so nguyen.")


def nhap_diem():
    while True:
        try:
            diem = float(input("Nhap diem: "))
            if 0 <= diem <= 10:
                return diem
            print("-> Diem phai nam trong khoang 0 den 10.")
        except ValueError:
            print("-> Du lieu khong hop le, vui long nhap so.")


def them_sinh_vien():
    ma_sv = input("Nhap ma sinh vien: ").strip().upper()

    if tim_sinh_vien(ma_sv) is not None:
        print(f"-> Ma sinh vien {ma_sv} da ton tai.")
        return

    ho_ten = input("Nhap ho ten: ").strip().title()
    tuoi = nhap_so_nguyen("Nhap tuoi: ")
    diem = nhap_diem()

    danh_sach_sinh_vien.append({
        "ma_sv": ma_sv,
        "ho_ten": ho_ten,
        "tuoi": tuoi,
        "diem": diem
    })

    print(f"-> Da them sinh vien {ma_sv} thanh cong.")


def sua_sinh_vien():
    ma_sv = input("Nhap ma sinh vien can sua: ").strip().upper()
    sv = tim_sinh_vien(ma_sv)

    if sv is None:
        print(f"-> Khong tim thay sinh vien {ma_sv}.")
        return

    sv["ho_ten"] = input("Nhap ho ten moi: ").strip().title()
    sv["tuoi"] = nhap_so_nguyen("Nhap tuoi moi: ")
    sv["diem"] = nhap_diem()

    print("-> Da cap nhat thong tin sinh vien thanh cong.")


def xoa_sinh_vien():
    ma_sv = input("Nhap ma sinh vien can xoa: ").strip().upper()
    sv = tim_sinh_vien(ma_sv)

    if sv is None:
        print(f"-> Khong tim thay sinh vien {ma_sv}.")
        return

    danh_sach_sinh_vien.remove(sv)
    print(f"-> Da xoa sinh vien {ma_sv} thanh cong.")


def tim_kiem_sinh_vien():
    ma_sv = input("Nhap ma sinh vien can tim: ").strip().upper()
    sv = tim_sinh_vien(ma_sv)

    if sv is None:
        print(f"-> Khong tim thay sinh vien {ma_sv}.")
        return

    print("\nThong tin sinh vien:")
    print("Ma SV:", sv["ma_sv"])
    print("Ho ten:", sv["ho_ten"])
    print("Tuoi:", sv["tuoi"])
    print("Diem:", sv["diem"])


def thong_ke():
    if len(danh_sach_sinh_vien) == 0:
        print("-> Chua co sinh vien.")
        return

    tong_diem = 0
    sinh_vien_gioi = 0

    for sv in danh_sach_sinh_vien:
        tong_diem += sv["diem"]
        if sv["diem"] >= 8:
            sinh_vien_gioi += 1

    diem_trung_binh = tong_diem / len(danh_sach_sinh_vien)

    print("\nTHONG KE")
    print("So luong sinh vien:", len(danh_sach_sinh_vien))
    print("Diem trung binh:", round(diem_trung_binh, 2))
    print("So sinh vien co diem tu 8 tro len:", sinh_vien_gioi)


def hien_thi_menu():
    print("\n===== QUAN LY SINH VIEN =====")
    print("1. Hien thi danh sach sinh vien")
    print("2. Them sinh vien")
    print("3. Sua sinh vien")
    print("4. Xoa sinh vien")
    print("5. Tim kiem sinh vien")
    print("6. Thong ke")
    print("0. Thoat chuong trinh")


def chay_chuong_trinh():
    while True:
        hien_thi_menu()
        lua_chon = input("Nhap lua chon cua ban: ").strip()

        if lua_chon == "1":
            hien_thi_danh_sach()
        elif lua_chon == "2":
            them_sinh_vien()
        elif lua_chon == "3":
            sua_sinh_vien()
        elif lua_chon == "4":
            xoa_sinh_vien()
        elif lua_chon == "5":
            tim_kiem_sinh_vien()
        elif lua_chon == "6":
            thong_ke()
        elif lua_chon == "0":
            print("Cam on da su dung chuong trinh. Tam biet!")
            break
        else:
            print("-> Lua chon khong hop le, vui long chon lai.")


if __name__ == "__main__":
    chay_chuong_trinh()
