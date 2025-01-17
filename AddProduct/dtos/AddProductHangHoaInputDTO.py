from abc import ABC

from Intefaces.RequestData import RequestData


class AddProductHangHoaInputDTO(RequestData, ABC):
    def __init__(self, tenHang, soLuongTon, donGia, loaiHang):
        super().__init__()
        self.tenHang = tenHang
        self.soLuongTon = soLuongTon
        self.donGia = donGia
        self.loaiHang = loaiHang