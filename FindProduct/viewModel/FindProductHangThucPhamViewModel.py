from FindProduct.viewModel.FindProductHangHoaViewModel import FindProductHangHoaViewModel


class FindProductHangThucPhamViewModel(FindProductHangHoaViewModel):
    def __init__(self, maHang: str, tenHang: str, soLuongTon: str, donGia: str, VAT: str, ngaySanXuat: str,
                 ngayHetHan: str, nhaCungCap: str):
        super().__init__(maHang, tenHang, soLuongTon, donGia, VAT)
        self.ngaySanXuat = ngaySanXuat
        self.ngayHetHan = ngayHetHan
        self.nhaCungCap = nhaCungCap
