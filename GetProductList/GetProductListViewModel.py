import string


class GetProductListViewModel:
    def __init__(self, maHang: 'string', tenHang: 'string', soLuongTon: 'string', donGia: 'string', vat: 'string'):
        self.maHang = maHang
        self.tenHang = tenHang
        self.soLuongTon = soLuongTon
        self.donGia = donGia
        self.vat = vat
        pass

    @property
    def maHang(self):
        return self._maHang

    @maHang.setter
    def maHang(self, value):
        self._maHang = value

    @property
    def tenHang(self):
        return self._tenHang

    @tenHang.setter
    def tenHang(self, value):
        self._tenHang = value

    @property
    def soLuongTon(self):
        return self._soLuongTon

    @soLuongTon.setter
    def soLuongTon(self, value):
        self._soLuongTon = value

    @property
    def donGia(self):
        return self._donGia

    @donGia.setter
    def donGia(self, value):
        self._donGia = value

    @property
    def vat(self):
        return self._vat

    @vat.setter
    def vat(self, value):
        self._vat = value
