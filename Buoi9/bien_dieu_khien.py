import tkinter as tk
from tkinter import messagebox

def xem_gia_tri_bien():
    try:
        tuoi = bien_tuoi.get()
    except tk.TclError:
        messagebox.showerror("Loi", "Tuoi phai la so nguyen.")
        return
    thong_tin = (
        "Ho ten (StringVar): " + bien_ho_ten.get() + "\n"
        + "Tuoi (IntVar): " + str(tuoi) + "\n"
        + "Dong y dieu khoan (BooleanVar): " + str(bien_dong_y_dieu_khoan.get())
    )
    messagebox.showinfo("Gia tri bien", thong_tin)
    bien_tuoi.set(tuoi + 1)

cua_so = tk.Tk()
cua_so.title("Hoat dong 5 - Bien dieu khien")
cua_so.geometry("390x240")
bien_ho_ten = tk.StringVar(value="Nguyen Van A")
bien_tuoi = tk.IntVar(value=18)
bien_dong_y_dieu_khoan = tk.BooleanVar(value=False)
tk.Label(cua_so, text="Ho ten:").grid(row=0, column=0, padx=10, pady=10, sticky="w")
tk.Entry(cua_so, textvariable=bien_ho_ten, width=25).grid(row=0, column=1, padx=10, pady=10)
tk.Label(cua_so, text="Tuoi:").grid(row=1, column=0, padx=10, pady=10, sticky="w")
tk.Entry(cua_so, textvariable=bien_tuoi, width=25).grid(row=1, column=1, padx=10, pady=10)
tk.Checkbutton(cua_so, text="Dong y dieu khoan", variable=bien_dong_y_dieu_khoan).grid(row=2, column=0, columnspan=2, pady=10)
tk.Button(cua_so, text="Xem gia tri bien (va +1 tuoi)", command=xem_gia_tri_bien).grid(row=3, column=0, columnspan=2, pady=10)
cua_so.mainloop()
