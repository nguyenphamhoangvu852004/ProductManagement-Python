from AddProduct.onViewData.AddProductHangHoaOnView import AddProductHangHoaOnView


class AddProductHangThucPhamOnView(AddProductHangHoaOnView):
    def __init__(self, tenHang, soLuongTon, donGia, tenLoaiHang, ngaySanXuat, ngayHetHan, nhaCungCap):
        super().__init__(tenHang, soLuongTon, donGia, tenLoaiHang)
        self.ngaySanXuat = ngaySanXuat
        self.ngayHetHan = ngayHetHan
        self.nhaCungCap = nhaCungCap
        pass