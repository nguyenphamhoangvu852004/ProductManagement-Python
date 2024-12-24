from contextlib import nullcontext

from FindProduct.FindProductResponseData import FindProductResponseData
from FindProduct.dtos.FindProductHangDienMayOutputDTO import FindProductHangDienMayOutputDTO
from FindProduct.dtos.FindProductHangSanhSuOutputDTO import FindProductHangSanhSuOutputDTO
from FindProduct.dtos.FindProductHangThucPhamOutputDTO import FindProductHangThucPhamOutputDTO
from FindProduct.viewModel.FindProductHangDienMayViewModel import FindProductHangDienMayViewModel
from FindProduct.viewModel.FindProductHangHoaViewModel import FindProductHangHoaViewModel
from FindProduct.viewModel.FindProductHangSanhSuViewModel import FindProductHangSanhSuViewModel
from FindProduct.viewModel.FindProductHangThucPhamViewModel import FindProductHangThucPhamViewModel
from Intefaces.OutputBoundary import OutputBoundary
from Intefaces.ResponseData import ResponseData
from Intefaces.Subject import Subject


class FindProductPresenter(OutputBoundary, Subject):
    def __init__(self, findProductHangHoaViewModel: FindProductHangHoaViewModel):
        Subject.__init__(self)
        self.findProductHangHoaViewModel = findProductHangHoaViewModel
        self.messageContent = None
        self.status = None
        pass

    def exportData(self, responseData: ResponseData):
        if isinstance(responseData, FindProductResponseData):
            if isinstance(responseData.productDTO, FindProductHangDienMayOutputDTO):
                self.findProductHangHoaViewModel = FindProductHangDienMayViewModel(
                    responseData.productDTO.maHang,
                    responseData.productDTO.tenHang,
                    responseData.productDTO.soLuongTon,
                    responseData.productDTO.donGia,
                    responseData.productDTO.VAT,
                    responseData.productDTO.thoiGianBaoHanh,
                    responseData.productDTO.congSuat
                )
                self.messageContent = "Tìm thấy hàng điện máy"
                self.status = "Success"

                pass
            if isinstance(responseData.productDTO, FindProductHangSanhSuOutputDTO):
                self.findProductHangHoaViewModel = FindProductHangSanhSuViewModel(
                    responseData.productDTO.maHang,
                    responseData.productDTO.tenHang,
                    responseData.productDTO.soLuongTon,
                    responseData.productDTO.donGia,
                    responseData.productDTO.VAT,
                    responseData.productDTO.nhaSanXuat,
                    responseData.productDTO.ngayNhapKho
                )
                self.messageContent = "Tim thấy hàng sành sứ"
                self.status = "Success"
                pass
            if isinstance(responseData.productDTO, FindProductHangThucPhamOutputDTO):
                self.findProductHangHoaViewModel = FindProductHangThucPhamViewModel(
                    responseData.productDTO.maHang,
                    responseData.productDTO.tenHang,
                    responseData.productDTO.soLuongTon,
                    responseData.productDTO.donGia,
                    responseData.productDTO.VAT,
                    responseData.productDTO.ngaySanXuat,
                    responseData.productDTO.ngayHetHan,
                    responseData.productDTO.nhaCungCap
                )
                self.messageContent = "Tìm thấy hàng thực phẩm"
                self.status = "Success"
                pass
            if responseData.isExist is False and responseData.productDTO is None:
                self.findProductHangHoaViewModel = FindProductHangHoaViewModel(
                    "", "", "", "", ""
                )
                self.messageContent = "Không tìm thấy sản phẩm với mã hàng này"
                self.status = "Fail"
                pass
            self.notify(self.findProductHangHoaViewModel)
        pass
