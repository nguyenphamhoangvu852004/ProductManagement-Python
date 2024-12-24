from abc import ABC


class FindProductHangHoaViewModel(ABC):
    def __init__(self, maHang: str, tenHang: str, soLuongTon: str, donGia: str, VAT: str):
        self.maHang = maHang
        self.tenHang = tenHang
        self.soLuongTon = soLuongTon
        self.donGia = donGia
        self.VAT = VAT
