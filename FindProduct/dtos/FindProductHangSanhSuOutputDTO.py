from FindProduct.dtos.FindProductHangHoaOutputDTO import FindProductHangHoaOutputDTO


class FindProductHangSanhSuOutputDTO(FindProductHangHoaOutputDTO):
    def __init__(self, maHang, tenHang, soLuongTon, donGia, VAT, maLoai, nhaSanXuat, ngayNhapKho):
        super().__init__(maHang, tenHang, soLuongTon, donGia, VAT)
        self.maLoai = maLoai
        self.nhaSanXuat = nhaSanXuat
        self.ngayNhapKho = ngayNhapKho
        pass

    def __str__(self) -> str:
        return f'{self.maHang} {self.tenHang} {self.soLuongTon} {self.donGia} {self.VAT} {self.maLoai} {self.nhaSanXuat} {self.ngayNhapKho}'
