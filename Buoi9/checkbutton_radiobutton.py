import tkinter as tk
from tkinter import messagebox

def mo_checkbutton():
    cua_so = tk.Toplevel(root)
    cua_so.title("Hoat dong 1 - Checkbutton")
    cua_so.geometry("320x260")
    tk.Label(cua_so, text="Chon so thich cua ban:", font=("Arial", 12)).pack(pady=10)
    bien_doc_sach = tk.BooleanVar(value=False)
    bien_the_thao = tk.BooleanVar(value=False)
    bien_am_nhac = tk.BooleanVar(value=False)
    tk.Checkbutton(cua_so, text="Doc sach", variable=bien_doc_sach).pack(anchor="w", padx=30)
    tk.Checkbutton(cua_so, text="The thao", variable=bien_the_thao).pack(anchor="w", padx=30)
    tk.Checkbutton(cua_so, text="Am nhac", variable=bien_am_nhac).pack(anchor="w", padx=30)

    def xem_lua_chon():
        ket_qua = []
        if bien_doc_sach.get():
            ket_qua.append("Doc sach")
        if bien_the_thao.get():
            ket_qua.append("The thao")
        if bien_am_nhac.get():
            ket_qua.append("Am nhac")
        if ket_qua:
            messagebox.showinfo("So thich", "Ban da chon: " + ", ".join(ket_qua), parent=cua_so)
        else:
            messagebox.showinfo("So thich", "Ban chua chon so thich nao.", parent=cua_so)

    tk.Button(cua_so, text="Xem lua chon", command=xem_lua_chon).pack(pady=15)

def mo_radiobutton():
    cua_so = tk.Toplevel(root)
    cua_so.title("Hoat dong 2 - Radiobutton")
    cua_so.geometry("320x230")
    bien_loai_tai_khoan = tk.StringVar(value="ca_nhan")
    tk.Label(cua_so, text="Chon loai tai khoan:", font=("Arial", 12)).pack(pady=10)
    tk.Radiobutton(cua_so, text="Ca nhan", variable=bien_loai_tai_khoan, value="ca_nhan").pack(anchor="w", padx=30)
    tk.Radiobutton(cua_so, text="Doanh nghiep", variable=bien_loai_tai_khoan, value="doanh_nghiep").pack(anchor="w", padx=30)
    nhan_ket_qua = tk.Label(cua_so, text="")
    nhan_ket_qua.pack(pady=5)

    def xem_loai_tai_khoan():
        nhan_ket_qua.config(text="Ban da chon: " + bien_loai_tai_khoan.get())

    tk.Button(cua_so, text="Xac nhan", command=xem_loai_tai_khoan).pack(pady=10)

root = tk.Tk()
root.title("Buoi 9 - Hoat dong 1 va 2")
root.geometry("360x180")
tk.Label(root, text="Chon hoat dong muon mo", font=("Arial", 13, "bold")).pack(pady=18)
tk.Button(root, text="Hoat dong 1 - Checkbutton", command=mo_checkbutton, width=28).pack(pady=5)
tk.Button(root, text="Hoat dong 2 - Radiobutton", command=mo_radiobutton, width=28).pack(pady=5)
root.mainloop()
