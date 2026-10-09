import tkinter as tk

# Hoat dong 1: Cua so Tkinter co ban
cua_so = tk.Tk()
cua_so.title("Cua so Tkinter dau tien")
cua_so.geometry("400x300")
cua_so.resizable(False, False)

nhan = tk.Label(cua_so, text="Xin chao Tkinter!", font=("Arial", 16))
nhan.pack(pady=20)

# Hoat dong 2: Su dung Frame de chia khu vuc giao dien
khung_tren = tk.Frame(cua_so, bg="lightblue", height=80)
khung_tren.pack(fill="x")
khung_tren.pack_propagate(False)

khung_duoi = tk.Frame(cua_so, bg="lightyellow")
khung_duoi.pack(fill="both", expand=True)

tk.Label(khung_tren, text="Khu vuc tieu de", bg="lightblue").pack(pady=10)
tk.Label(khung_duoi, text="Khu vuc noi dung", bg="lightyellow").pack(pady=10)

cua_so.mainloop()
