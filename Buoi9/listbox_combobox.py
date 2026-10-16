import tkinter as tk
from tkinter import ttk, messagebox

def mo_listbox():
    cua_so = tk.Toplevel(root)
    cua_so.title("Bai tap 3.1 - Listbox")
    cua_so.geometry("320x300")
    tk.Label(cua_so, text="Chon mon hoc:").pack(pady=8)
    listbox_mon_hoc = tk.Listbox(cua_so, selectmode="single", height=6)
    for mon in ["Toan", "Ly", "Hoa", "Van", "Anh"]:
        listbox_mon_hoc.insert(tk.END, mon)
    listbox_mon_hoc.pack(pady=8)
    nhan_ket_qua = tk.Label(cua_so, text="")
    nhan_ket_qua.pack(pady=5)

    def xem_mon_da_chon():
        lua_chon = listbox_mon_hoc.curselection()
        if lua_chon:
            nhan_ket_qua.config(text="Mon da chon: " + listbox_mon_hoc.get(lua_chon[0]))
        else:
            messagebox.showerror("Loi", "Vui long chon mot mon hoc.", parent=cua_so)

    tk.Button(cua_so, text="Xem mon da chon", command=xem_mon_da_chon).pack(pady=5)

def mo_combobox():
    cua_so = tk.Toplevel(root)
    cua_so.title("Bai tap 3.2 - Combobox")
    cua_so.geometry("320x220")
    tk.Label(cua_so, text="Chon thanh pho:").pack(pady=10)
    combobox_thanh_pho = ttk.Combobox(cua_so, values=["Ha Noi", "Da Nang", "TP.HCM", "Hue"], state="readonly")
    combobox_thanh_pho.current(0)
    combobox_thanh_pho.pack(pady=5)
    nhan_ket_qua = tk.Label(cua_so, text="")
    nhan_ket_qua.pack(pady=5)

    def xem_thanh_pho():
        nhan_ket_qua.config(text="Ban chon: " + combobox_thanh_pho.get())

    tk.Button(cua_so, text="Xac nhan", command=xem_thanh_pho).pack(pady=8)

root = tk.Tk()
root.title("Buoi 9 - Listbox va Combobox")
root.geometry("360x190")
tk.Label(root, text="Chon bai tap", font=("Arial", 13, "bold")).pack(pady=15)
tk.Button(root, text="Bai tap 3.1 - Listbox", command=mo_listbox, width=28).pack(pady=5)
tk.Button(root, text="Bai tap 3.2 - Combobox", command=mo_combobox, width=28).pack(pady=5)
root.mainloop()
