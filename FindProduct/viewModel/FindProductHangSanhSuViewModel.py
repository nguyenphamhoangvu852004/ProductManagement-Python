from FindProduct.viewModel.FindProductHangHoaViewModel import FindProductHangHoaViewModel


class FindProductHangSanhSuViewModel(FindProductHangHoaViewModel):
    def __init__(self, maHang: str, tenHang: str, soLuongTon: str, donGia: str, VAT: str, nhaSanXuat: str,
                 ngayNhapKho: str):
        super().__init__(maHang, tenHang, soLuongTon, donGia, VAT)
        self.nhaSanXuat = nhaSanXuat
        self.ngayNhapKho = ngayNhapKho
