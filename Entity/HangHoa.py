from abc import ABC, abstractmethod, abstractclassmethod

class HangHoa(ABC):
    def __init__(self, maHang, tenHang, soLuongTon, donGia, maLoai):
        self.__maHang = maHang
        self.__tenHang = tenHang
        self.__soLuongTon = soLuongTon
        self.__donGia = donGia
        self.__maLoai = maLoai

    @property
    def maHang(self):
        return self.__maHang

    @maHang.setter
    def maHang(self, value):
        self.__maHang = value

    @property
    def tenHang(self):
        return self.__tenHang

    @tenHang.setter
    def tenHang(self, value):
        self.__tenHang = value

    @property
    def soLuongTon(self):
        return self.__soLuongTon

    @soLuongTon.setter
    def soLuongTon(self, value):
        self.__soLuongTon = value

    @property
    def donGia(self):
        return self.__donGia

    @donGia.setter
    def donGia(self, value):
        self.__donGia = value

    @property
    def maLoai(self):
        return self.__maLoai

    @maLoai.setter
    def maLoai(self, value):
        self.__maLoai = value

    @abstractmethod
    def tinhVat(self):
        pass
