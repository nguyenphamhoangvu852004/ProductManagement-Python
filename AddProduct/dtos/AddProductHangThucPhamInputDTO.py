from AddProduct.dtos.AddProductHangHoaInputDTO import AddProductHangHoaInputDTO


class AddProductHangThucPhamInputDTO(AddProductHangHoaInputDTO):
    def __init__(self, tenHang, soLuongTon, donGia, loaiHang, ngaySanXuat, ngayHetHan, nhaCungCap):
        super().__init__(tenHang, soLuongTon, donGia, loaiHang)
        self.ngaySanXuat = ngaySanXuat
        self.ngayHetHan = ngayHetHan
        self.nhaCungCap = nhaCungCap
        pass

    def __str__(self):
        return f"Ten hang: {self.tenHang}\nSo luong ton: {self.soLuongTon}\nDon gia: {self.donGia}\nLoai hang: {self.loaiHang}"