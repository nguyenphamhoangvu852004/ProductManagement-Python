from ModifyProduct.inputDTOs.ModifyProductHangHoaInputDTO import ModifyProductHangHoaInputDTO


class ModifyProductHangThucPhamInputDTO(ModifyProductHangHoaInputDTO):
    def __init__(self, maHang, tenHang, soLuongTon, donGia, maLoai, ngaySanXuat, ngayHetHan, nhaCungCap):
        super().__init__(maHang, tenHang, soLuongTon, donGia, maLoai)
        self.ngaySanXuat = ngaySanXuat
        self.ngayHetHan = ngayHetHan
        self.nhaCungCap = nhaCungCap
