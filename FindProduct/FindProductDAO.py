from Entity.HangDienMay import HangDienMay
from Entity.HangSanhSu import HangSanhSu
from Entity.HangThucPham import HangThucPham
from Intefaces.DatabaseBoundary import DatabaseBoundary
from connectdb import MysqlConnection

from typing import Union

import logging
from typing import Union

class FindProductDAO(DatabaseBoundary):
    def __init__(self):
        super().__init__()

    def findProduct(self, maHangStr: str) -> Union[HangDienMay, HangSanhSu, HangThucPham, None]:
        product = None
        try:
            # Kết nối đến cơ sở dữ liệu
            connectdb = MysqlConnection.get_connection()
            with connectdb.cursor(dictionary=True) as cursor:
                # Truy vấn SQL
                query = """
                    SELECT 
                        hh.maHang, 
                        hh.tenHang, 
                        hh.soLuongTon, 
                        hh.donGia, 
                        lh.tenLoai, 
                        hdm.thoiGianBaoHanh, 
                        hdm.congSuat, 
                        hss.nhaSanXuat, 
                        hss.ngayNhapKho, 
                        htp.ngaySanXuat, 
                        htp.ngayHetHan, 
                        htp.nhaCungCap
                    FROM 
                        hanghoa hh
                    LEFT JOIN 
                        loaihang lh ON hh.maLoai = lh.maLoai
                    LEFT JOIN 
                        hangdienmay hdm ON hh.maHang = hdm.maHang
                    LEFT JOIN 
                        hangsanhsu hss ON hh.maHang = hss.maHang
                    LEFT JOIN 
                        hangthucpham htp ON hh.maHang = htp.maHang
                    WHERE 
                        hh.maHang = %s;
                """
                cursor.execute(query, (maHangStr,))
                row = cursor.fetchone()

                if row:
                    # Ánh xạ dữ liệu thành Entity
                    maHang = row['maHang']
                    if maHang.startswith("HDM"):
                        product = HangDienMay(
                            maHang=row['maHang'],
                            tenHang=row['tenHang'],
                            soLuongTon=row['soLuongTon'],
                            donGia=row['donGia'],
                            tenLoai=row['tenLoai'],
                            thoiGianBaoHanh=row['thoiGianBaoHanh'],
                            congSuat=row['congSuat']
                        )
                    elif maHang.startswith("HSS"):
                        product = HangSanhSu(
                            maHang=row['maHang'],
                            tenHang=row['tenHang'],
                            soLuongTon=row['soLuongTon'],
                            donGia=row['donGia'],
                            tenLoai=row['tenLoai'],
                            nhaSanXuat=row['nhaSanXuat'],
                            ngayNhapKho=row['ngayNhapKho']
                        )
                    elif maHang.startswith("HTP"):
                        product = HangThucPham(
                            maHang=row['maHang'],
                            tenHang=row['tenHang'],
                            soLuongTon=row['soLuongTon'],
                            donGia=row['donGia'],
                            tenLoai=row['tenLoai'],
                            ngaySanXuat=row['ngaySanXuat'],
                            ngayHetHan=row['ngayHetHan'],
                            nhaCungCap=row['nhaCungCap']
                        )

        except Exception as e:
            logging.error(f"Error while finding product with maHang {maHangStr}: {e}")
        finally:
            if connectdb:
                connectdb.close()

        return product
