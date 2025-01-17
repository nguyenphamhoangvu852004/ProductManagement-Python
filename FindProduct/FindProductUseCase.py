from typing import override

from Entity.HangDienMay import HangDienMay
from Entity.HangSanhSu import HangSanhSu
from Entity.HangThucPham import HangThucPham
from FindProduct.FindProductInputDTO import FindProductInputDTO
from FindProduct.FindProductResponseData import FindProductResponseData
from FindProduct.dtos.FindProductHangDienMayOutputDTO import FindProductHangDienMayOutputDTO
from FindProduct.dtos.FindProductHangSanhSuOutputDTO import FindProductHangSanhSuOutputDTO
from FindProduct.dtos.FindProductHangThucPhamOutputDTO import FindProductHangThucPhamOutputDTO
from Intefaces.DatabaseBoundary import DatabaseBoundary
from Intefaces.InputBoundary import InputBoundary
from Intefaces.OutputBoundary import OutputBoundary
from Intefaces.RequestData import RequestData
from Intefaces.ResponseData import ResponseData


class FindProductUseCase(InputBoundary):

    def __init__(self, databaseBoundary: DatabaseBoundary, outputBoundary: OutputBoundary):
        self.databaseBoundary = databaseBoundary
        self.outputBoundary = outputBoundary
        super().__init__()

    @override
    def execute(self, requestData: RequestData):
        maHang = requestData.getMaHangStr  # type:ignore
        hangHoa = self.databaseBoundary.findProduct(maHang)  # type: ignore
        if hangHoa is None:
            responseData = FindProductResponseData(None, False, "Khong tim thay hang hoa")
            self.outputBoundary.exportData(responseData)
            return
        if isinstance(hangHoa, HangDienMay):
            responseData = FindProductResponseData(
                FindProductHangDienMayOutputDTO(hangHoa.maHang, hangHoa.tenHang, hangHoa.soLuongTon,
                                                hangHoa.donGia, hangHoa.maLoai, hangHoa.tinhVat(),
                                                hangHoa.thoiGianBaoHanh, hangHoa.congSuat)
                , True, "Tim thay hang hoa")
            self.outputBoundary.exportData(responseData)
            return
        if isinstance(hangHoa, HangSanhSu):
            responseData = FindProductResponseData(
                FindProductHangSanhSuOutputDTO(hangHoa.maHang, hangHoa.tenHang, hangHoa.soLuongTon,
                                               hangHoa.donGia, hangHoa.tinhVat(), hangHoa.maLoai, hangHoa.nhaSanXuat,
                                               hangHoa.ngayNhapKho),
                True, "Tim thay hang hoa")
            self.outputBoundary.exportData(responseData)
            return
        if isinstance(hangHoa, HangThucPham):
            responseData = FindProductResponseData(
                FindProductHangThucPhamOutputDTO(hangHoa.maHang, hangHoa.tenHang, hangHoa.soLuongTon,
                                                 hangHoa.donGia, hangHoa.tinhVat(), hangHoa.maLoai,
                                                 hangHoa.ngaySanXuat, hangHoa.ngayHetHan, hangHoa.nhaCungCap),
                True, "Tim thay hang hoa")
            self.outputBoundary.exportData(responseData)
            return
        self.outputBoundary.exportData(hangHoa)
        return
        pass
