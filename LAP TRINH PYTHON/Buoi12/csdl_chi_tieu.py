import sqlite3
import sys
from pathlib import Path

if getattr(sys, "frozen", False):
    THU_MUC = Path(sys.executable).resolve().parent
else:
    THU_MUC = Path(__file__).resolve().parent
TEN_FILE_CSDL = THU_MUC / "chi_tieu.db"

def ket_noi_csdl():
    return sqlite3.connect(TEN_FILE_CSDL)

def tao_bang_neu_chua_co():
    with ket_noi_csdl() as ket_noi:
        ket_noi.execute("""CREATE TABLE IF NOT EXISTS giao_dich (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            loai TEXT NOT NULL, danh_muc TEXT NOT NULL,
            so_tien REAL NOT NULL, ngay TEXT NOT NULL, ghi_chu TEXT)""")

def them_giao_dich(loai, danh_muc, so_tien, ngay, ghi_chu):
    with ket_noi_csdl() as ket_noi:
        ket_noi.execute("INSERT INTO giao_dich (loai,danh_muc,so_tien,ngay,ghi_chu) VALUES (?,?,?,?,?)",
                        (loai,danh_muc,so_tien,ngay,ghi_chu))

def lay_tat_ca_giao_dich():
    with ket_noi_csdl() as ket_noi:
        return ket_noi.execute("SELECT id,loai,danh_muc,so_tien,ngay,ghi_chu FROM giao_dich ORDER BY ngay DESC,id DESC").fetchall()

def sua_giao_dich(id_gd, loai, danh_muc, so_tien, ngay, ghi_chu):
    with ket_noi_csdl() as ket_noi:
        ket_noi.execute("UPDATE giao_dich SET loai=?,danh_muc=?,so_tien=?,ngay=?,ghi_chu=? WHERE id=?",
                        (loai,danh_muc,so_tien,ngay,ghi_chu,id_gd))

def xoa_giao_dich(id_gd):
    with ket_noi_csdl() as ket_noi:
        ket_noi.execute("DELETE FROM giao_dich WHERE id=?", (id_gd,))

def tim_kiem_giao_dich(tu_khoa):
    tu_khoa = "%" + tu_khoa + "%"
    with ket_noi_csdl() as ket_noi:
        return ket_noi.execute("""SELECT id,loai,danh_muc,so_tien,ngay,ghi_chu FROM giao_dich
            WHERE loai LIKE ? OR danh_muc LIKE ? OR ngay LIKE ? OR ghi_chu LIKE ?
            ORDER BY ngay DESC,id DESC""", (tu_khoa,tu_khoa,tu_khoa,tu_khoa)).fetchall()

def thong_ke_tong_quan():
    with ket_noi_csdl() as ket_noi:
        return ket_noi.execute("""SELECT
            COALESCE(SUM(CASE WHEN loai='Thu' THEN so_tien ELSE 0 END),0),
            COALESCE(SUM(CASE WHEN loai='Chi' THEN so_tien ELSE 0 END),0)
            FROM giao_dich""").fetchone()

def thong_ke_chi_theo_danh_muc():
    with ket_noi_csdl() as ket_noi:
        return ket_noi.execute("""SELECT danh_muc,SUM(so_tien) FROM giao_dich
            WHERE loai='Chi' GROUP BY danh_muc ORDER BY SUM(so_tien) DESC""").fetchall()
