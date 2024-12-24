from abc import ABC


class AddProductHangHoaOnView(ABC):
    def __init__(self, tenHang, soLuongTon, donGia, tenLoaiHang):
        super().__init__()
        self.tenHang = tenHang
        self.soLuongTon = soLuongTon
        self.donGia = donGia
        self.tenLoaiHang = tenLoaiHang
        pass
