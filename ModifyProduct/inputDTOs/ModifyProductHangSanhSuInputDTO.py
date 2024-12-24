from ModifyProduct.inputDTOs.ModifyProductHangHoaInputDTO import ModifyProductHangHoaInputDTO


class ModifyProductHangSanhSuInputDTO(ModifyProductHangHoaInputDTO):
    def __init__(self, maHang, tenHang, soLuongTon, donGia,maLoai, nhaSanXuat, ngayNhapKho):
        super().__init__(maHang, tenHang, soLuongTon, donGia,maLoai)
        self.nhaSanXuat = nhaSanXuat
        self.ngayNhapKho = ngayNhapKho
