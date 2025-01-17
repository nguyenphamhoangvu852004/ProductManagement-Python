from abc import ABC

from Intefaces.RequestData import RequestData


class ModifyProductHangHoaInputDTO(RequestData, ABC):
    def __init__(self, maHang, tenHang, soLuongTon, donGia, maLoai):
        super().__init__()
        self.maHang = maHang
        self.tenHang = tenHang
        self.soLuongTon = soLuongTon
        self.donGia = donGia
        self.maLoai = maLoai
