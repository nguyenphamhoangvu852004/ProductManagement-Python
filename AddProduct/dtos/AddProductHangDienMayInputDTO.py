from AddProduct.dtos.AddProductHangHoaInputDTO import AddProductHangHoaInputDTO


class AddProductHangDienMayInputDTO(AddProductHangHoaInputDTO):
    def __init__(self, tenHang, soLuongTon, donGia, loaiHang, thoiGianBaoHanh, congSuat):
        super().__init__(tenHang, soLuongTon, donGia, loaiHang)
        self.thoiGianBaoHanh = thoiGianBaoHanh
        self.congSuat = congSuat

    def __str__(self):
        return f"{self.tenHang} - {self.soLuongTon} - {self.donGia} - {self.loaiHang} - {self.thoiGianBaoHanh} - {self.congSuat}"