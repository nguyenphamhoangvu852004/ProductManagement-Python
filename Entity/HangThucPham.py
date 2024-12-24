from typing import override

from Entity.HangHoa import HangHoa


class HangThucPham(HangHoa):
    def __init__(self, maHang, tenHang, soLuongTon, donGia, tenLoai, ngaySanXuat, ngayHetHan, nhaCungCap):
        super().__init__(maHang, tenHang, soLuongTon, donGia, tenLoai)
        self.__ngaySanXuat = ngaySanXuat
        self.__ngayHetHan = ngayHetHan
        self.__nhaCungCap = nhaCungCap

    @property
    def ngaySanXuat(self):
        return self.__ngaySanXuat

    @ngaySanXuat.setter
    def ngaySanXuat(self, value):
        self.__ngaySanXuat = value

    @property
    def ngayHetHan(self):
        return self.__ngayHetHan

    @ngayHetHan.setter
    def ngayHetHan(self, value):
        self.__ngayHetHan = value

    @property
    def nhaCungCap(self):
        return self.__nhaCungCap

    @nhaCungCap.setter
    def nhaCungCap(self, value):
        self.__nhaCungCap = value

    @override
    def tinhVat(self):
        return self.donGia * 0.05
