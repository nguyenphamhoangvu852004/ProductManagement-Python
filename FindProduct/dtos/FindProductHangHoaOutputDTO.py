from abc import ABC


class FindProductHangHoaOutputDTO(ABC):
    def __init__(self, maHang, tenHang, soLuongTon, donGia, VAT):
        self.maHang = maHang
        self.tenHang = tenHang
        self.soLuongTon = soLuongTon
        self.donGia = donGia
        self.VAT = VAT
        pass

    def __str__(self):
        return f"FindProductHangHoaOutputDTO(maHang={self.maHang}, tenHang={self.tenHang}, soLuongTon={self.soLuongTon}, donGia={self.donGia}, VAT={self.VAT})"
