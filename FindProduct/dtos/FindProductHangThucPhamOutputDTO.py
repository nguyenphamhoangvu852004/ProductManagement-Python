from FindProduct.dtos.FindProductHangHoaOutputDTO import FindProductHangHoaOutputDTO


class FindProductHangThucPhamOutputDTO(FindProductHangHoaOutputDTO):
    def __init__(self, maHang, tenHang, soLuongTon, donGia, VAT, maLoai, ngaySanXuat, ngayHetHan, nhaCungCap):
        super().__init__(maHang, tenHang, soLuongTon, donGia, VAT)
        self.maLoai = maLoai
        self.ngaySanXuat = ngaySanXuat
        self.ngayHetHan = ngayHetHan
        self.nhaCungCap = nhaCungCap
        pass
    def __str__(self):
        return f"{self.maHang} {self.tenHang} {self.soLuongTon} {self.donGia} {self.VAT} {self.maLoai} {self.ngaySanXuat} {self.ngayHetHan} {self.nhaCungCap}"