from contextlib import nullcontext
from math import trunc

from Entity.HangDienMay import HangDienMay
from Entity.HangHoa import HangHoa
from Entity.HangSanhSu import HangSanhSu
from Entity.HangThucPham import HangThucPham
from Intefaces.DatabaseBoundary import DatabaseBoundary
from connectdb import MysqlConnection


class GetProductListDAO(DatabaseBoundary):
    def __init__(self):
        super().__init__()
        pass

    def getProductListDataMockList(self):
        return [
            HangDienMay("HDM001", "Máy lạnh Samsung", 50, 5000000, "HDM", 24, "2000W"),
            HangDienMay("HDM002", "Tủ lạnh LG", 30, 10000000, "HDM", 36, "3000W"),
            HangDienMay("HDM003", "Lò vi sóng Panasonic", 100, 1500000, "HDM", 12, "800W"),
            HangDienMay("HDM004", "Máy giặt Electrolux", 20, 8000000, "HDM", 24, "1000W"),
            HangDienMay("HDM005", "Máy sưởi Sharp", 60, 1200000, "HDM", 12, "1500W"),
            HangDienMay("HDM006", "Nồi cơm điện Cuckoo", 80, 2000000, "HDM", 18, "900W"),
            HangDienMay("HDM007", "Quạt điều hòa Sunhouse", 120, 2500000, "HDM", 24, "150W"),
            HangDienMay("HDM008", "Bình nước nóng Ariston", 40, 3500000, "HDM", 36, "2000W"),
            HangDienMay("HDM009", "Máy xay sinh tố Philips", 150, 800000, "HDM", 12, "500W"),
            HangDienMay("HDM010", "Máy ép chậm Panasonic", 90, 3000000, "HDM", 24, "200W"),

            HangSanhSu("HSS001", "Sữa tươi Vinamilk", 100, 200000, "HSS", "Vinamilk", "2022-07-01"),
            HangSanhSu("HSS002", "Bánh quy Kinh Đô", 100, 150000, "HSS", "Kinh Đô", "2022-07-01"),
            HangSanhSu("HSS003", "Nước ngọt Coca-Cola", 100, 250000, "HSS", "Coca-Cola", "2022-07-01"),
            HangSanhSu("HSS004", "Bánh ngọt Orion", 100, 200000, "HSS", "Orion", "2022-07-01"),
            HangSanhSu("HSS005", "Sữa chua Vinamilk", 100, 180000, "HSS", "Vinamilk", "2022-07-01"),
            HangSanhSu("HSS006", "Bánh quy Lotte", 100, 220000, "HSS", "Lotte", "2022-07-01"),
            HangSanhSu("HSS007", "Nước ngọt Pepsi", 100, 280000, "HSS", "Pepsi", "2022-07-01"),
            HangSanhSu("HSS008", "Bánh ngọt Calbee", 100, 250000, "HSS", "Calbee", "2022-07-01"),
            HangSanhSu("HSS009", "Sữa tươi Dutch Lady", 100, 220000, "HSS", "Dutch Lady", "2022-07-01"),
            HangSanhSu("HSS010", "Bánh quy Mondelez", 100, 200000, "HSS", "Mondelez", "2022-07-01"),

            HangThucPham("HTP001", "Cà phê Arabica", 100, 2500000, "HTP", "2022-07-01", "2022-07-01", "T&T"),
            HangThucPham("HTP002", "Trà xanh Matcha", 100, 2200000, "HTP", "2022-07-01", "2022-07-01", "T&T"),
            HangThucPham("HTP003", "Sữa chua Hy Lạp", 100, 2800000, "HTP", "2022-07-01", "2022-07-01", "T&T"),
            HangThucPham("HTP004", "Bánh quy socola", 100, 2000000, "HTP", "2022-07-01", "2022-07-01", "T&T"),
            HangThucPham("HTP005", "Nước ép cam", 100, 2500000, "HTP", "2022-07-01", "2022-07-01", "T&T"),
            HangThucPham("HTP006", "Gạo lứt Nhật Bản", 100, 2200000, "HTP", "2022-07-01", "2022-07-01", "T&T"),
            HangThucPham("HTP007", "Mì ăn liền Hàn Quốc", 100, 2000000, "HTP", "2022-07-01", "2022-07-01", "T&T"),
            HangThucPham("HTP008", "Bánh mì sandwich", 100, 2500000, "HTP", "2022-07-01", "2022-07-01", "T&T"),
            HangThucPham("HTP009", "Sữa tươi Organic", 100, 2800000, "HTP", "2022-07-01", "2022-07-01", "T&T"),
            HangThucPham("HTP010", "Trái cây sấy khô", 100, 2000000, "HTP", "2022-07-01", "2022-07-01", "T&T"),

        ]

    def getProductListFromDatabase(self):
        product_list = []
        connectdb = MysqlConnection.get_connection()

        cursor = connectdb.cursor(dictionary=True)
        cursor.execute("SELECT maHang, tenHang, soLuongTon, donGia, maLoai FROM hanghoa")
        for row in cursor.fetchall():
            product_code = row['maLoai']
            if product_code == ("HDM"):
                product = HangDienMay(
                    row['maHang'],
                    row['tenHang'],
                    row['soLuongTon'],
                    row['donGia'],
                    nullcontext, nullcontext, nullcontext
                )
                product_list.append(product)
            if product_code == ("HSS"):
                product = HangSanhSu(
                    row['maHang'],
                    row['tenHang'],
                    row['soLuongTon'],
                    row['donGia'],
                    nullcontext, nullcontext, nullcontext
                )
                product_list.append(product)
            if product_code == ("HTP"):
                product = HangThucPham(
                    row['maHang'],
                    row['tenHang'],
                    row['soLuongTon'],
                    row['donGia'],
                    nullcontext, nullcontext, nullcontext, nullcontext
                )
                product_list.append(product)
        cursor.close()
        return product_list
