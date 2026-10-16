import tkinter as tk

def khi_keo_thanh_truot(gia_tri):
    nhan_gia_tri.config(text="Gia tri hien tai: " + str(int(float(gia_tri))))

cua_so = tk.Tk()
cua_so.title("Hoat dong 4 - Scale")
cua_so.geometry("360x180")
tk.Label(cua_so, text="Keo thanh truot tu 0 den 100").pack(pady=12)
thanh_truot = tk.Scale(cua_so, from_=0, to=100, orient="horizontal", command=khi_keo_thanh_truot)
thanh_truot.pack(pady=10, padx=20, fill="x")
nhan_gia_tri = tk.Label(cua_so, text="Gia tri hien tai: 0")
nhan_gia_tri.pack()
cua_so.mainloop()
