from FindProduct.viewModel.FindProductHangHoaViewModel import FindProductHangHoaViewModel


class FindProductHangDienMayViewModel(FindProductHangHoaViewModel):
    def __init__(self, maHang: str, tenHang: str, soLuongTon: str, donGia: str, VAT: str, thoiGianBaoHanh: str,
                 congSuat: str):
        super().__init__(maHang, tenHang, soLuongTon, donGia, VAT)
        self.thoiGianBaoHanh = thoiGianBaoHanh
        self.congSuat = congSuat
