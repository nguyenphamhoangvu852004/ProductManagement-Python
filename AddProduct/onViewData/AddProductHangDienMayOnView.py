from AddProduct.onViewData.AddProductHangHoaOnView import AddProductHangHoaOnView


class AddProductHangDienMayOnView(AddProductHangHoaOnView):
    def __init__(self, tenHang, soLuongTon, donGia, tenLoaiHang, thoiGianBaoHanh, congSuat):
        super().__init__(tenHang, soLuongTon, donGia, tenLoaiHang)
        self.thoiGianBaoHanh = thoiGianBaoHanh
        self.congSuat = congSuat
        pass

