import tkinter as tk
from tkinter import messagebox
import ast
import operator

phep_tinh = {
    ast.Add: operator.add,
    ast.Sub: operator.sub,
    ast.Mult: operator.mul,
    ast.Div: operator.truediv
}

def tinh_bieu_thuc(node):
    if isinstance(node, ast.Expression):
        return tinh_bieu_thuc(node.body)
    if isinstance(node, ast.Constant) and isinstance(node.value, (int, float)):
        return node.value
    if isinstance(node, ast.BinOp) and type(node.op) in phep_tinh:
        trai = tinh_bieu_thuc(node.left)
        phai = tinh_bieu_thuc(node.right)
        if isinstance(node.op, ast.Div) and phai == 0:
            raise ZeroDivisionError
        return phep_tinh[type(node.op)](trai, phai)
    if isinstance(node, ast.UnaryOp) and isinstance(node.op, (ast.UAdd, ast.USub)):
        gia_tri = tinh_bieu_thuc(node.operand)
        return gia_tri if isinstance(node.op, ast.UAdd) else -gia_tri
    raise ValueError("Bieu thuc khong hop le")

def bam_phim(ky_tu):
    if ky_tu == "C":
        bien_bieu_thuc.set("")
    elif ky_tu == "DEL":
        bien_bieu_thuc.set(bien_bieu_thuc.get()[:-1])
    elif ky_tu == "=":
        try:
            bieu_thuc = bien_bieu_thuc.get().strip()
            if not bieu_thuc:
                return
            cay = ast.parse(bieu_thuc, mode="eval")
            ket_qua = tinh_bieu_thuc(cay)
            bien_bieu_thuc.set(str(ket_qua))
        except ZeroDivisionError:
            messagebox.showerror("Loi", "Khong the chia cho 0.", parent=cua_so)
        except Exception:
            messagebox.showerror("Loi", "Bieu thuc khong hop le.", parent=cua_so)
    else:
        bien_bieu_thuc.set(bien_bieu_thuc.get() + ky_tu)

cua_so = tk.Tk()
cua_so.title("Bai tap mo rong - May tinh bo tui")
cua_so.geometry("340x420")
cua_so.resizable(False, False)
bien_bieu_thuc = tk.StringVar()
o_hien_thi = tk.Entry(cua_so, textvariable=bien_bieu_thuc, font=("Arial", 18), justify="right", state="readonly", readonlybackground="white")
o_hien_thi.grid(row=0, column=0, columnspan=4, padx=12, pady=15, ipady=10, sticky="nsew")
cac_hang = [
    ["7", "8", "9", "/"],
    ["4", "5", "6", "*"],
    ["1", "2", "3", "-"],
    ["C", "0", "DEL", "+"],
    ["(", ")", "=", ""]
]
for i, hang in enumerate(cac_hang):
    for j, ky_tu in enumerate(hang):
        if ky_tu:
            tk.Button(cua_so, text=ky_tu, font=("Arial", 14), width=5, height=2,
                      command=lambda k=ky_tu: bam_phim(k)).grid(row=i + 1, column=j, padx=4, pady=4, sticky="nsew")
cua_so.mainloop()
