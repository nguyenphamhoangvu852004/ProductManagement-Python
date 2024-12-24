from typing import override

from Entity.HangHoa import HangHoa


class HangSanhSu(HangHoa):
    def __init__(self, maHang, tenHang, soLuongTon, donGia, tenLoai, nhaSanXuat, ngayNhapKho):
        super().__init__(maHang, tenHang, soLuongTon, donGia, tenLoai)
        self.__nhaSanXuat = nhaSanXuat
        self.__ngayNhapKho = ngayNhapKho

    @property
    def nhaSanXuat(self):
        return self.__nhaSanXuat

    @nhaSanXuat.setter
    def nhaSanXuat(self, value):
        self.__nhaSanXuat = value

    @property
    def ngayNhapKho(self):
        return self.__ngayNhapKho

    @ngayNhapKho.setter
    def ngayNhapKho(self, value):
        self.__ngayNhapKho = value

    @override
    def tinhVat(self):
        return self.donGia * 0.1
