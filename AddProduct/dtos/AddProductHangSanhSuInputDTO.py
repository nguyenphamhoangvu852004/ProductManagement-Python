from AddProduct.dtos.AddProductHangHoaInputDTO import AddProductHangHoaInputDTO


class AddProductHangSanhSuInputDTO(AddProductHangHoaInputDTO):
    def __init__(self, tenHang, soLuongTon, donGia, loaiHang, nhaSanXuat, ngayNhapKho):
        super().__init__(tenHang, soLuongTon, donGia, loaiHang)
        self.nhaSanXuat = nhaSanXuat
        self.ngayNhapKho = ngayNhapKho
        pass

    def __str__(self) -> str:
        return f'{self.tenHang} {self.soLuongTon} {self.donGia} {self.loaiHang} {self.nhaSanXuat} {self.ngayNhapKho}'