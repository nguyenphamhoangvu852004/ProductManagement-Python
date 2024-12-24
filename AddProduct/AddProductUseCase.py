from contextlib import nullcontext
from datetime import datetime
from typing import override

from AddProduct.AddProductOutputDTO import AddProductOutputDTO
from AddProduct.dtos.AddProductHangDienMayInputDTO import AddProductHangDienMayInputDTO
from AddProduct.dtos.AddProductHangSanhSuInputDTO import AddProductHangSanhSuInputDTO
from AddProduct.dtos.AddProductHangThucPhamInputDTO import AddProductHangThucPhamInputDTO
from Entity.HangDienMay import HangDienMay
from Entity.HangSanhSu import HangSanhSu
from Entity.HangThucPham import HangThucPham
from Intefaces.DatabaseBoundary import DatabaseBoundary
from Intefaces.InputBoundary import InputBoundary
from Intefaces.OutputBoundary import OutputBoundary
from Intefaces.RequestData import RequestData


class AddProductUseCase(InputBoundary):
    def __init__(self, databaseBoundary: DatabaseBoundary, presenter: OutputBoundary):
        self.databaseBoundary = databaseBoundary
        self.presenter = presenter
        super().__init__()

    def _convert_date(self, date_str: str) -> str:
        """
        Chuyển đổi ngày từ định dạng dd/mm/yyyy sang yyyy-mm-dd.
        Nếu có lỗi khi chuyển đổi, sẽ in thông báo và trả về None.
        """
        try:
            return datetime.strptime(date_str, "%d/%m/%Y").strftime("%Y-%m-%d")
        except ValueError as e:
            print(f"Lỗi khi chuyển đổi ngày: {e}")
            return None

    def _create_product(self, request_data, product_type: str):
        """
        Tạo đối tượng sản phẩm dựa trên loại sản phẩm và dữ liệu nhập vào.
        """
        if product_type == "HSS":
            return HangSanhSu(nullcontext,
                              request_data.tenHang,
                              request_data.soLuongTon,
                              request_data.donGia,
                              "HSS",
                              request_data.nhaSanXuat,
                              self._convert_date(request_data.ngayNhapKho))

        if product_type == "HDM":
            return HangDienMay(nullcontext,
                               request_data.tenHang,
                               request_data.soLuongTon,
                               request_data.donGia,
                               "HDM",
                               request_data.thoiGianBaoHanh,
                               request_data.congSuat)

        if product_type == "HTP":
            return HangThucPham(nullcontext,
                                request_data.tenHang,
                                request_data.soLuongTon,
                                request_data.donGia,
                                "HTP",
                                self._convert_date(request_data.ngaySanXuat),
                                self._convert_date(request_data.ngayHetHan),
                                request_data.nhaCungCap)

        return None

    def _handle_response(self, success: bool):
        """
        Xử lý và trả về phản hồi sau khi thêm sản phẩm.
        """
        response_data = AddProductOutputDTO(
            success,
            "Them hang hoa thanh cong" if success else "Them hang hoa that bai"
        )
        self.presenter.exportData(response_data)

    @override
    def execute(self, requestData: RequestData):
        """
        Thực hiện thêm sản phẩm, xử lý dữ liệu từ các đối tượng DTO.
        """
        product = None
        if isinstance(requestData, AddProductHangSanhSuInputDTO):
            product = self._create_product(requestData, "HSS")
        elif isinstance(requestData, AddProductHangDienMayInputDTO):
            product = self._create_product(requestData, "HDM")
        elif isinstance(requestData, AddProductHangThucPhamInputDTO):
            product = self._create_product(requestData, "HTP")

        if product:
            success = self.databaseBoundary.addProduct(product)
            self._handle_response(success)
