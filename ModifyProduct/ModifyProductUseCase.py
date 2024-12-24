from typing import override

from Entity.HangDienMay import HangDienMay
from Entity.HangSanhSu import HangSanhSu
from Entity.HangThucPham import HangThucPham
from Intefaces.DatabaseBoundary import DatabaseBoundary
from Intefaces.InputBoundary import InputBoundary
from Intefaces.OutputBoundary import OutputBoundary
from Intefaces.RequestData import RequestData
from ModifyProduct.inputDTOs.ModifyProductHangDienMayInputDTO import ModifyProductHangDienMayInputDTO
from ModifyProduct.inputDTOs.ModifyProductHangHoaInputDTO import ModifyProductHangHoaInputDTO
from ModifyProduct.inputDTOs.ModifyProductHangSanhSuInputDTO import ModifyProductHangSanhSuInputDTO
from ModifyProduct.inputDTOs.ModifyProductHangThucPhamInputDTO import ModifyProductHangThucPhamInputDTO
from ModifyProduct.outputDTOs.ModifyProductOutputDTO import ModifyProductOutputDTO


class ModifyProductUseCase(InputBoundary):
    def __init__(self, outputBoundary: OutputBoundary, databaseBoundary: DatabaseBoundary):
        super().__init__()
        self.outputBoundary = outputBoundary
        self.databaseBoundary = databaseBoundary
        pass

    @override
    def execute(self, requestData: RequestData):
        if not isinstance(requestData, ModifyProductHangHoaInputDTO):
            responseData = ModifyProductOutputDTO(False, "Du Lieu Khong Dung")
            self.outputBoundary.exportData(responseData)
            return

        if isinstance(requestData, ModifyProductHangHoaInputDTO):
            if isinstance(requestData, ModifyProductHangDienMayInputDTO):
                product = HangDienMay(
                    requestData.maHang,
                    requestData.tenHang,
                    requestData.soLuongTon,
                    requestData.donGia,
                    requestData.maLoai,
                    requestData.thoiGianBaoHanh,
                    requestData.congSuat
                )
                if not self.databaseBoundary.modifyProductDatabase(product):
                    responseData = ModifyProductOutputDTO(False, "Du Lieu Khong Dung")
                    self.outputBoundary.exportData(responseData)
                    return
                responseData = ModifyProductOutputDTO(True, "Cap nhat hang hoa thanh cong")
                self.outputBoundary.exportData(responseData)
                return
            if isinstance(requestData, ModifyProductHangThucPhamInputDTO):
                product = HangThucPham(
                    requestData.maHang,
                    requestData.tenHang,
                    requestData.soLuongTon,
                    requestData.donGia,
                    requestData.maLoai,
                    requestData.ngaySanXuat,
                    requestData.ngayHetHan,
                    requestData.nhaCungCap
                )
                if not self.databaseBoundary.modifyProductDatabase(product):
                    responseData = ModifyProductOutputDTO(False, "Du Lieu Khong Dung")
                    self.outputBoundary.exportData(responseData)
                    return
                responseData = ModifyProductOutputDTO(True, "Cap nhat hang hoa thanh cong")
                self.outputBoundary.exportData(responseData)
                return

            if isinstance(requestData, ModifyProductHangSanhSuInputDTO):
                product = HangSanhSu(
                    requestData.maHang,
                    requestData.tenHang,
                    requestData.soLuongTon,
                    requestData.donGia,
                    requestData.maLoai,
                    requestData.ngayNhapKho,
                    requestData.nhaSanXuat
                )
                if not self.databaseBoundary.modifyProductDatabase(product):
                    responseData = ModifyProductOutputDTO(False, "Du Lieu Khong Dung")
                    self.outputBoundary.exportData(responseData)
                    return
                responseData = ModifyProductOutputDTO(True, "Cap nhat hang hoa thanh cong")
                self.outputBoundary.exportData(responseData)
                return
        pass