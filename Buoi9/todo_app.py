import tkinter as tk
from tkinter import messagebox

danh_sach_cong_viec = []

def lam_moi_listbox():
    listbox_cong_viec.delete(0, tk.END)
    for noi_dung, da_hoan_thanh in danh_sach_cong_viec:
        tien_to = "[Da xong] " if da_hoan_thanh else "[Chua xong] "
        listbox_cong_viec.insert(tk.END, tien_to + noi_dung)

def them_cong_viec():
    noi_dung = bien_cong_viec_moi.get().strip()
    if noi_dung == "":
        messagebox.showerror("Loi", "Vui long nhap noi dung cong viec truoc khi them.", parent=cua_so)
        entry_cong_viec.focus_set()
        return
    danh_sach_cong_viec.append((noi_dung, False))
    bien_cong_viec_moi.set("")
    lam_moi_listbox()
    entry_cong_viec.focus_set()

def xoa_cong_viec():
    lua_chon = listbox_cong_viec.curselection()
    if not lua_chon:
        messagebox.showerror("Loi", "Vui long chon mot cong viec trong danh sach de xoa.", parent=cua_so)
        return
    danh_sach_cong_viec.pop(lua_chon[0])
    lam_moi_listbox()

def danh_dau_hoan_thanh():
    lua_chon = listbox_cong_viec.curselection()
    if not lua_chon:
        messagebox.showerror("Loi", "Vui long chon mot cong viec de danh dau hoan thanh.", parent=cua_so)
        return
    vi_tri = lua_chon[0]
    noi_dung, da_hoan_thanh = danh_sach_cong_viec[vi_tri]
    danh_sach_cong_viec[vi_tri] = (noi_dung, not da_hoan_thanh)
    lam_moi_listbox()

cua_so = tk.Tk()
cua_so.title("Ung dung Ghi chu cong viec - To-do list")
cua_so.geometry("560x430")
cua_so.resizable(False, False)
bien_cong_viec_moi = tk.StringVar()
tk.Label(cua_so, text="TO-DO LIST", font=("Arial", 18, "bold")).grid(row=0, column=0, columnspan=3, pady=18)
tk.Label(cua_so, text="Cong viec moi:").grid(row=1, column=0, padx=10, pady=8, sticky="e")
entry_cong_viec = tk.Entry(cua_so, textvariable=bien_cong_viec_moi, width=36)
entry_cong_viec.grid(row=1, column=1, padx=8, pady=8, sticky="w")
tk.Button(cua_so, text="Them", command=them_cong_viec, width=10).grid(row=1, column=2, padx=8, pady=8)
listbox_cong_viec = tk.Listbox(cua_so, width=65, height=13, font=("Arial", 10))
listbox_cong_viec.grid(row=2, column=0, columnspan=3, padx=15, pady=12)
tk.Button(cua_so, text="Danh dau hoan thanh", command=danh_dau_hoan_thanh, width=22).grid(row=3, column=0, padx=8, pady=12)
tk.Button(cua_so, text="Xoa cong viec", command=xoa_cong_viec, width=16).grid(row=3, column=1, padx=8, pady=12)
tk.Button(cua_so, text="Thoat", command=cua_so.destroy, width=10).grid(row=3, column=2, padx=8, pady=12)
tk.Label(cua_so, text="Chon cong viec roi bam Danh dau hoan thanh hoac Xoa.", fg="gray").grid(row=4, column=0, columnspan=3, pady=5)
entry_cong_viec.focus_set()
if __name__ == "__main__":
    cua_so.mainloop()
