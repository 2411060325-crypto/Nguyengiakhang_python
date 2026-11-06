import tkinter as tk
from tkinter import ttk, messagebox
import matplotlib
matplotlib.use("TkAgg")
import matplotlib.pyplot as plt

import csdl_sach as db


DANH_SACH_THE_LOAI = [
    "Ky nang song", "Tieu thuyet", "Lich su",
    "Khoa hoc", "Kinh te", "Khac"
]


class UngDungTuSach(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Quan ly Tu sach ca nhan")
        self.geometry("760x570")
        self.minsize(700, 520)
        self.configure(bg="#f3f6fb")

        db.tao_bang_neu_chua_co()
        self.danh_sach_hien_tai = []
        self.khoi_tao_giao_dien()
        self.tai_lai_danh_sach_sach()

    def khoi_tao_giao_dien(self):
        tieu_de = tk.Label(
            self, text="QUAN LY TU SACH CA NHAN",
            font=("Arial", 18, "bold"), bg="#f3f6fb", fg="#183153"
        )
        tieu_de.pack(pady=(16, 10))

        khung_nhap = tk.LabelFrame(
            self, text="Thong tin sach", font=("Arial", 10, "bold"),
            padx=12, pady=10, bg="#ffffff"
        )
        khung_nhap.pack(fill="x", padx=18, pady=6)

        tk.Label(khung_nhap, text="Ten sach:", bg="#ffffff").grid(
            row=0, column=0, sticky="w", pady=7
        )
        self.o_nhap_ten_sach = tk.Entry(khung_nhap, width=38)
        self.o_nhap_ten_sach.grid(row=0, column=1, padx=8, pady=7, sticky="w")

        tk.Label(khung_nhap, text="Tac gia:", bg="#ffffff").grid(
            row=1, column=0, sticky="w", pady=7
        )
        self.o_nhap_tac_gia = tk.Entry(khung_nhap, width=38)
        self.o_nhap_tac_gia.grid(row=1, column=1, padx=8, pady=7, sticky="w")

        tk.Label(khung_nhap, text="The loai:", bg="#ffffff").grid(
            row=2, column=0, sticky="w", pady=7
        )
        self.chon_the_loai = ttk.Combobox(
            khung_nhap, values=DANH_SACH_THE_LOAI,
            width=35, state="readonly"
        )
        self.chon_the_loai.current(0)
        self.chon_the_loai.grid(row=2, column=1, padx=8, pady=7, sticky="w")

        tk.Button(
            khung_nhap, text="Them sach", command=self.xu_ly_them_sach,
            bg="#2457a7", fg="white", activebackground="#183f7a",
            font=("Arial", 10, "bold"), padx=16, pady=5
        ).grid(row=0, column=2, rowspan=3, padx=18)

        khung_ds = tk.LabelFrame(
            self, text="Danh sach sach", font=("Arial", 10, "bold"),
            padx=10, pady=10, bg="#ffffff"
        )
        khung_ds.pack(fill="both", expand=True, padx=18, pady=8)

        cot = ("id", "ten", "tacgia", "theloai", "trangthai")
        self.bang_sach = ttk.Treeview(
            khung_ds, columns=cot, show="headings", height=12
        )
        self.bang_sach.heading("id", text="ID")
        self.bang_sach.heading("ten", text="Ten sach")
        self.bang_sach.heading("tacgia", text="Tac gia")
        self.bang_sach.heading("theloai", text="The loai")
        self.bang_sach.heading("trangthai", text="Trang thai")
        self.bang_sach.column("id", width=45, anchor="center")
        self.bang_sach.column("ten", width=210)
        self.bang_sach.column("tacgia", width=175)
        self.bang_sach.column("theloai", width=120)
        self.bang_sach.column("trangthai", width=100, anchor="center")

        thanh_cuon = ttk.Scrollbar(
            khung_ds, orient="vertical", command=self.bang_sach.yview
        )
        self.bang_sach.configure(yscrollcommand=thanh_cuon.set)
        self.bang_sach.pack(side="left", fill="both", expand=True)
        thanh_cuon.pack(side="right", fill="y")

        khung_nut = tk.Frame(self, bg="#f3f6fb")
        khung_nut.pack(pady=(4, 12))

        tk.Button(
            khung_nut, text="Danh dau da doc",
            command=self.xu_ly_danh_dau_da_doc, width=17
        ).grid(row=0, column=0, padx=5)
        tk.Button(
            khung_nut, text="Xoa sach",
            command=self.xu_ly_xoa_sach, width=13
        ).grid(row=0, column=1, padx=5)
        tk.Button(
            khung_nut, text="Thong ke theo the loai",
            command=self.xu_ly_thong_ke, width=22
        ).grid(row=0, column=2, padx=5)
        tk.Button(
            khung_nut, text="Lam moi",
            command=self.tai_lai_danh_sach_sach, width=12
        ).grid(row=0, column=3, padx=5)

        self.nhan_tong = tk.Label(
            self, text="", bg="#f3f6fb", fg="#34445c",
            font=("Arial", 9, "italic")
        )
        self.nhan_tong.pack(pady=(0, 8))

    def tai_lai_danh_sach_sach(self):
        for dong in self.bang_sach.get_children():
            self.bang_sach.delete(dong)

        self.danh_sach_hien_tai = db.lay_toan_bo_sach()
        for sach in self.danh_sach_hien_tai:
            id_sach, ten_sach, tac_gia, the_loai, da_doc = sach
            trang_thai = "Da doc" if da_doc == 1 else "Chua doc"
            self.bang_sach.insert(
                "", tk.END,
                values=(id_sach, ten_sach, tac_gia, the_loai, trang_thai)
            )

        so_sach = len(self.danh_sach_hien_tai)
        so_da_doc = sum(1 for sach in self.danh_sach_hien_tai if sach[4] == 1)
        self.nhan_tong.config(
            text=f"Tong so: {so_sach} cuon sach | Da doc: {so_da_doc}"
        )

    def xu_ly_them_sach(self):
        ten_sach = self.o_nhap_ten_sach.get().strip()
        tac_gia = self.o_nhap_tac_gia.get().strip()
        the_loai = self.chon_the_loai.get()

        if ten_sach == "" or tac_gia == "":
            messagebox.showerror(
                "Loi", "Vui long nhap day du ten sach va tac gia."
            )
            return

        db.them_sach(ten_sach, tac_gia, the_loai)
        self.o_nhap_ten_sach.delete(0, tk.END)
        self.o_nhap_tac_gia.delete(0, tk.END)
        self.tai_lai_danh_sach_sach()
        messagebox.showinfo("Thanh cong", f"Da them sach: {ten_sach}")

    def lay_id_sach_dang_chon(self):
        lua_chon = self.bang_sach.selection()
        if not lua_chon:
            messagebox.showerror("Loi", "Vui long chon mot cuon sach.")
            return None
        gia_tri = self.bang_sach.item(lua_chon[0], "values")
        return int(gia_tri[0])

    def xu_ly_xoa_sach(self):
        id_sach = self.lay_id_sach_dang_chon()
        if id_sach is None:
            return
        xac_nhan = messagebox.askyesno(
            "Xac nhan", "Ban co chac chan muon xoa cuon sach nay?"
        )
        if xac_nhan:
            db.xoa_sach(id_sach)
            self.tai_lai_danh_sach_sach()

    def xu_ly_danh_dau_da_doc(self):
        id_sach = self.lay_id_sach_dang_chon()
        if id_sach is None:
            return
        db.danh_dau_da_doc(id_sach)
        self.tai_lai_danh_sach_sach()
        messagebox.showinfo("Thanh cong", "Da cap nhat trang thai sach.")

    def xu_ly_thong_ke(self):
        du_lieu = db.thong_ke_theo_the_loai()
        if not du_lieu:
            messagebox.showinfo("Thong bao", "Chua co du lieu sach de thong ke.")
            return

        cac_the_loai = [dong[0] for dong in du_lieu]
        so_luong = [dong[1] for dong in du_lieu]

        plt.figure(figsize=(8, 5))
        plt.bar(cac_the_loai, so_luong, color="cornflowerblue")
        plt.title("So luong sach theo the loai")
        plt.xlabel("The loai")
        plt.ylabel("So luong sach")
        plt.xticks(rotation=20, ha="right")
        plt.tight_layout()
        plt.show()


if __name__ == "__main__":
    ung_dung = UngDungTuSach()
    ung_dung.mainloop()
