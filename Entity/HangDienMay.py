from typing import override

from Entity.HangHoa import HangHoa


class HangDienMay(HangHoa):
    def __init__(self, maHang, tenHang, soLuongTon, donGia, tenLoai, thoiGianBaoHanh, congSuat):
        super().__init__(maHang, tenHang, soLuongTon, donGia, tenLoai)
        self.__thoiGianBaoHanh = thoiGianBaoHanh
        self.__congSuat = congSuat

    @property
    def thoiGianBaoHanh(self):
        return self.__thoiGianBaoHanh

    @thoiGianBaoHanh.setter
    def thoiGianBaoHanh(self, value):
        self.__thoiGianBaoHanh = value

    @property
    def congSuat(self):
        return self.__congSuat

    @congSuat.setter
    def congSuat(self, value):
        self.__congSuat = value

    @override
    def tinhVat(self):
        return self.donGia * 0.1

