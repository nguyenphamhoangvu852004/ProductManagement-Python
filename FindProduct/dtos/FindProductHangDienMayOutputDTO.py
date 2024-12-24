from FindProduct.dtos.FindProductHangHoaOutputDTO import FindProductHangHoaOutputDTO


class FindProductHangDienMayOutputDTO(FindProductHangHoaOutputDTO):
    def __init__(self, maHang, tenHang, soLuongTon, donGia, maLoai, VAT, thoiGianBaoHanh, congSuat):
        super().__init__(maHang, tenHang, soLuongTon, donGia, VAT)
        self.maLoai = maLoai
        self.thoiGianBaoHanh = thoiGianBaoHanh
        self.congSuat = congSuat

    def __str__(self):
        return f"{self.maHang} - {self.tenHang} - {self.soLuongTon} - {self.donGia} - {self.VAT} - {self.maLoai} - {self.thoiGianBaoHanh} - {self.congSuat}"