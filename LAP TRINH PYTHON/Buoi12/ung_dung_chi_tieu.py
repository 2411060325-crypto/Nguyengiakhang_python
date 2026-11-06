import tkinter as tk
from tkinter import ttk, messagebox
from datetime import date
import matplotlib
matplotlib.use("TkAgg")
import matplotlib.pyplot as plt
import csdl_chi_tieu as db

DANH_MUC_THU = ["Luong", "Thuong", "Tro cap", "Ban hang", "Khac"]
DANH_MUC_CHI = ["An uong", "Di chuyen", "Hoc tap", "Mua sam", "Giai tri", "Hoa don", "Y te", "Khac"]

class UngDungChiTieu(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Quan ly chi tieu ca nhan")
        self.geometry("1050x680")
        self.configure(bg="#f2f5fa")
        db.tao_bang_neu_chua_co()
        self.id_dang_chon = None
        self.tao_giao_dien()
        self.tai_lai_du_lieu()

    def tao_giao_dien(self):
        tk.Label(self, text="QUAN LY CHI TIEU CA NHAN", font=("Arial",20,"bold"),
                 bg="#f2f5fa", fg="#183153").pack(pady=12)
        khung = tk.LabelFrame(self, text="Thong tin giao dich", bg="white", padx=12, pady=10)
        khung.pack(fill="x", padx=16, pady=6)
        tk.Label(khung,text="Loai:",bg="white").grid(row=0,column=0,padx=5,pady=5)
        self.loai = ttk.Combobox(khung,values=["Thu","Chi"],state="readonly",width=17)
        self.loai.current(1); self.loai.grid(row=0,column=1,padx=5)
        self.loai.bind("<<ComboboxSelected>>",self.cap_nhat_danh_muc)
        tk.Label(khung,text="Danh muc:",bg="white").grid(row=0,column=2,padx=5)
        self.danh_muc = ttk.Combobox(khung,values=DANH_MUC_CHI,state="readonly",width=17)
        self.danh_muc.current(0); self.danh_muc.grid(row=0,column=3,padx=5)
        tk.Label(khung,text="So tien (VND):",bg="white").grid(row=1,column=0,padx=5,pady=5)
        self.so_tien = tk.Entry(khung,width=20); self.so_tien.grid(row=1,column=1,padx=5)
        tk.Label(khung,text="Ngay YYYY-MM-DD:",bg="white").grid(row=1,column=2,padx=5)
        self.ngay = tk.Entry(khung,width=20); self.ngay.insert(0,date.today().isoformat()); self.ngay.grid(row=1,column=3,padx=5)
        tk.Label(khung,text="Ghi chu:",bg="white").grid(row=2,column=0,padx=5,pady=5)
        self.ghi_chu = tk.Entry(khung,width=55); self.ghi_chu.grid(row=2,column=1,columnspan=3,padx=5,sticky="w")
        nut = tk.Frame(khung,bg="white"); nut.grid(row=3,column=0,columnspan=4,pady=8)
        tk.Button(nut,text="Them giao dich",command=self.them,width=17,bg="#2457a7",fg="white").pack(side="left",padx=4)
        tk.Button(nut,text="Cap nhat",command=self.sua,width=15).pack(side="left",padx=4)
        tk.Button(nut,text="Lam moi o nhap",command=self.lam_moi,width=17).pack(side="left",padx=4)

        tong = tk.Frame(self,bg="#f2f5fa"); tong.pack(fill="x",padx=16,pady=6)
        self.nhan_thu = self.the_tong(tong,"TONG THU","#e7f5ec")
        self.nhan_chi = self.the_tong(tong,"TONG CHI","#fdebea")
        self.nhan_du = self.the_tong(tong,"SO DU","#e9f0ff")

        ds = tk.LabelFrame(self,text="Danh sach giao dich",bg="white",padx=10,pady=8)
        ds.pack(fill="both",expand=True,padx=16,pady=6)
        tim = tk.Frame(ds,bg="white"); tim.pack(fill="x",pady=5)
        tk.Label(tim,text="Tim kiem:",bg="white").pack(side="left")
        self.tu_khoa = tk.Entry(tim,width=32); self.tu_khoa.pack(side="left",padx=6)
        tk.Button(tim,text="Tim",command=self.tim).pack(side="left",padx=3)
        tk.Button(tim,text="Hien tat ca",command=self.tai_lai_du_lieu).pack(side="left",padx=3)
        cot=("id","loai","danhmuc","sotien","ngay","ghichu")
        self.bang=ttk.Treeview(ds,columns=cot,show="headings",height=11)
        ten={"id":"ID","loai":"Loai","danhmuc":"Danh muc","sotien":"So tien (VND)","ngay":"Ngay","ghichu":"Ghi chu"}
        rong={"id":45,"loai":75,"danhmuc":140,"sotien":150,"ngay":115,"ghichu":300}
        for c in cot: self.bang.heading(c,text=ten[c]); self.bang.column(c,width=rong[c])
        self.bang.pack(fill="both",expand=True)
        self.bang.bind("<<TreeviewSelect>>",self.chon_dong)
        nut_duoi=tk.Frame(self,bg="#f2f5fa"); nut_duoi.pack(pady=8)
        tk.Button(nut_duoi,text="Xoa giao dich",command=self.xoa,width=17).grid(row=0,column=0,padx=5)
        tk.Button(nut_duoi,text="Bieu do chi tieu",command=self.thong_ke,width=19).grid(row=0,column=1,padx=5)

    def the_tong(self,khung,tieu_de,mau):
        f=tk.Frame(khung,bg=mau,padx=12,pady=8); f.pack(side="left",fill="x",expand=True,padx=5)
        tk.Label(f,text=tieu_de,bg=mau,font=("Arial",10,"bold")).pack()
        n=tk.Label(f,text="0 VND",bg=mau,font=("Arial",14,"bold")); n.pack(pady=3)
        return n

    def cap_nhat_danh_muc(self,event=None):
        ds=DANH_MUC_THU if self.loai.get()=="Thu" else DANH_MUC_CHI
        self.danh_muc["values"]=ds; self.danh_muc.current(0)

    def lay_du_lieu(self):
        loai=self.loai.get(); dm=self.danh_muc.get()
        tien=self.so_tien.get().strip(); ngay=self.ngay.get().strip(); ghi=self.ghi_chu.get().strip()
        if not loai or not dm or not tien or not ngay:
            messagebox.showerror("Loi","Vui long nhap day du thong tin."); return None
        try:
            tien=float(tien.replace(",","").replace(".",""))
            if tien<=0: raise ValueError
        except ValueError:
            messagebox.showerror("Loi","So tien phai la so lon hon 0."); return None
        try: date.fromisoformat(ngay)
        except ValueError:
            messagebox.showerror("Loi","Ngay phai co dang YYYY-MM-DD."); return None
        return loai,dm,tien,ngay,ghi

    def them(self):
        d=self.lay_du_lieu()
        if d is None:return
        db.them_giao_dich(*d); self.tai_lai_du_lieu(); self.lam_moi()
        messagebox.showinfo("Thanh cong","Da them giao dich.")

    def chon_dong(self,event=None):
        chon=self.bang.selection()
        if not chon:return
        v=self.bang.item(chon[0],"values"); self.id_dang_chon=int(v[0])
        self.loai.set(v[1]); self.cap_nhat_danh_muc(); self.danh_muc.set(v[2])
        for o,gt in [(self.so_tien,str(v[3]).replace(",","")),(self.ngay,v[4]),(self.ghi_chu,v[5])]:
            o.delete(0,tk.END); o.insert(0,gt)

    def sua(self):
        if self.id_dang_chon is None:
            messagebox.showerror("Loi","Hay chon giao dich can cap nhat."); return
        d=self.lay_du_lieu()
        if d is None:return
        db.sua_giao_dich(self.id_dang_chon,*d); self.tai_lai_du_lieu(); self.lam_moi()
        messagebox.showinfo("Thanh cong","Da cap nhat giao dich.")

    def xoa(self):
        chon=self.bang.selection()
        if not chon:
            messagebox.showerror("Loi","Hay chon giao dich can xoa."); return
        id_gd=int(self.bang.item(chon[0],"values")[0])
        if messagebox.askyesno("Xac nhan","Ban co chac muon xoa giao dich nay?"):
            db.xoa_giao_dich(id_gd); self.tai_lai_du_lieu(); self.lam_moi()

    def tim(self):
        self.hien_thi(db.tim_kiem_giao_dich(self.tu_khoa.get().strip()))

    def hien_thi(self,ds):
        for i in self.bang.get_children(): self.bang.delete(i)
        for gd in ds:
            id_gd,loai,dm,tien,ngay,ghi=gd
            self.bang.insert("","end",values=(id_gd,loai,dm,f"{tien:,.0f}",ngay,ghi or ""))

    def tai_lai_du_lieu(self):
        self.hien_thi(db.lay_tat_ca_giao_dich())
        thu,chi=db.thong_ke_tong_quan()
        self.nhan_thu.config(text=f"{thu:,.0f} VND")
        self.nhan_chi.config(text=f"{chi:,.0f} VND")
        self.nhan_du.config(text=f"{thu-chi:,.0f} VND")

    def lam_moi(self):
        self.loai.current(1); self.cap_nhat_danh_muc()
        for o in (self.so_tien,self.ghi_chu): o.delete(0,tk.END)
        self.ngay.delete(0,tk.END); self.ngay.insert(0,date.today().isoformat())
        self.id_dang_chon=None
        for i in self.bang.selection(): self.bang.selection_remove(i)

    def thong_ke(self):
        ds=db.thong_ke_chi_theo_danh_muc()
        if not ds:
            messagebox.showinfo("Thong bao","Chua co du lieu chi tieu."); return
        plt.figure(figsize=(8,5))
        plt.bar([x[0] for x in ds],[x[1] for x in ds],color="cornflowerblue")
        plt.title("Thong ke chi tieu theo danh muc")
        plt.xlabel("Danh muc"); plt.ylabel("So tien (VND)")
        plt.xticks(rotation=20,ha="right"); plt.tight_layout(); plt.show()

if __name__=="__main__":
    app=UngDungChiTieu()
    app.mainloop()
