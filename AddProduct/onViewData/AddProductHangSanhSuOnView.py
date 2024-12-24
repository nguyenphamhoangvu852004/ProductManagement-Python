from AddProduct.onViewData.AddProductHangHoaOnView import AddProductHangHoaOnView


class AddProductHangSanhSuOnView(AddProductHangHoaOnView):
    def __init__(self, tenHang, soLuongTon, donGia, tenLoaiHang, nhaSanXuat, ngayNhapKho):
        super().__init__(tenHang, soLuongTon, donGia, tenLoaiHang)
        self.nhaSanXuat = nhaSanXuat
        self.ngayNhapKho = ngayNhapKho
