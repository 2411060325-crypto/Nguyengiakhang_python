import tkinter as tk
from tkinter import messagebox

def xu_ly_submit():
    ho_ten = entry_ho_ten.get().strip()
    tuoi_nhap = entry_tuoi.get().strip()
    email = entry_email.get().strip()

    if ho_ten == "":
        messagebox.showerror("Loi", "Ho ten khong duoc de trong.", parent=cua_so)
        entry_ho_ten.focus_set()
        return

    try:
        tuoi = int(tuoi_nhap)
    except ValueError:
        messagebox.showerror("Loi", "Tuoi phai la mot so nguyen.", parent=cua_so)
        entry_tuoi.focus_set()
        return

    if tuoi <= 0:
        messagebox.showerror("Loi", "Tuoi phai lon hon 0.", parent=cua_so)
        entry_tuoi.focus_set()
        return

    if "@" not in email or "." not in email.split("@")[-1]:
        messagebox.showerror("Loi", "Email khong hop le.", parent=cua_so)
        entry_email.focus_set()
        return

    messagebox.showinfo("Thanh cong", f"Da nhan thong tin: {ho_ten} - {tuoi} tuoi - {email}", parent=cua_so)

cua_so = tk.Tk()
cua_so.title("Hoat dong 6 - Form validate")
cua_so.geometry("430x250")
cua_so.resizable(False, False)
tk.Label(cua_so, text="FORM THONG TIN", font=("Arial", 14, "bold")).grid(row=0, column=0, columnspan=2, pady=10)
tk.Label(cua_so, text="Ho ten:").grid(row=1, column=0, padx=12, pady=8, sticky="w")
entry_ho_ten = tk.Entry(cua_so, width=30)
entry_ho_ten.grid(row=1, column=1, padx=12, pady=8)
tk.Label(cua_so, text="Tuoi:").grid(row=2, column=0, padx=12, pady=8, sticky="w")
entry_tuoi = tk.Entry(cua_so, width=30)
entry_tuoi.grid(row=2, column=1, padx=12, pady=8)
tk.Label(cua_so, text="Email:").grid(row=3, column=0, padx=12, pady=8, sticky="w")
entry_email = tk.Entry(cua_so, width=30)
entry_email.grid(row=3, column=1, padx=12, pady=8)
tk.Button(cua_so, text="Submit", command=xu_ly_submit, width=15).grid(row=4, column=0, columnspan=2, pady=15)
cua_so.mainloop()
