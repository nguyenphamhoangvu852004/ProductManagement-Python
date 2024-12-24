from ModifyProduct.inputDTOs.ModifyProductHangHoaInputDTO import ModifyProductHangHoaInputDTO


class ModifyProductHangDienMayInputDTO(ModifyProductHangHoaInputDTO):
    def __init__(self, maHang, tenHang, soLuongTon, donGia, maLoai, thoiGianBaoHanh, congSuat):
        super().__init__(maHang, tenHang, soLuongTon, donGia, maLoai)
        self.thoiGianBaoHanh = thoiGianBaoHanh
        self.congSuat = congSuat
