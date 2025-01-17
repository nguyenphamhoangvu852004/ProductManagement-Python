from AddProduct.AddProductUseCase import AddProductUseCase
from AddProduct.dtos.AddProductHangDienMayInputDTO import AddProductHangDienMayInputDTO
from AddProduct.dtos.AddProductHangSanhSuInputDTO import AddProductHangSanhSuInputDTO
from AddProduct.dtos.AddProductHangThucPhamInputDTO import AddProductHangThucPhamInputDTO
from AddProduct.onViewData.AddProductHangDienMayOnView import AddProductHangDienMayOnView
from AddProduct.onViewData.AddProductHangHoaOnView import AddProductHangHoaOnView
from AddProduct.onViewData.AddProductHangSanhSuOnView import AddProductHangSanhSuOnView
from AddProduct.onViewData.AddProductHangThucPhamOnView import AddProductHangThucPhamOnView
from FindProduct.FindProductInputDTO import FindProductInputDTO
from FindProduct.FindProductUseCase import FindProductUseCase
from GetProductList.GetProductListInputDTO import GetProductListInputDTO
from GetProductList.GetProductListUseCase import GetProductListUseCase
from GetTypeList.GetTypeListInputDTO import GetTypeListInputDTO
from GetTypeList.GetTypeListUseCase import GetTypeListUseCase
from ModifyProduct.ModifyProductUseCase import ModifyProductUseCase
from RemoveProduct.RemoveProductInputDTO import RemoveProductInputDTO
from RemoveProduct.RemoveProductUseCase import RemoveProductUseCase


class MainController:
    def __init__(self, getProductListUseCase: GetProductListUseCase, getTypeListUseCase: GetTypeListUseCase,
                 findProductUseCase: FindProductUseCase, removeProductUseCase: RemoveProductUseCase,
                 addProductUseCase: AddProductUseCase,
                 modifyProductUseCase: ModifyProductUseCase):
        self.getProductListUseCase = getProductListUseCase
        self.getTypeListUseCase = getTypeListUseCase
        self.findProductUseCase = findProductUseCase
        self.removeProductUseCase = removeProductUseCase
        self.addProductUseCase = addProductUseCase
        self.modifyProductUseCase = modifyProductUseCase
        pass

    def executeGetProductListUseCase(self):
        getProductListInputDTO = GetProductListInputDTO()
        self.getProductListUseCase.execute(getProductListInputDTO)
        pass

    def executeGetTypeListUseCase(self):
        getTypeListInputDTO = GetTypeListInputDTO()
        self.getTypeListUseCase.execute(getTypeListInputDTO)
        pass

    def executeFindProductUseCase(self, maHang):
        requestData = FindProductInputDTO(maHang)
        self.findProductUseCase.execute(requestData)
        pass

    def executeRemoveProductUseCase(self, maHang: str):
        requestData = RemoveProductInputDTO(maHang)
        self.removeProductUseCase.execute(requestData)
        pass

    def executeAddProductUseCase(self, hangHoaOnView: AddProductHangHoaOnView):
        if isinstance(hangHoaOnView, AddProductHangThucPhamOnView):
            requestData = AddProductHangThucPhamInputDTO(hangHoaOnView.tenHang, hangHoaOnView.soLuongTon,
                                                         hangHoaOnView.donGia, hangHoaOnView.tenLoaiHang,
                                                         hangHoaOnView.ngaySanXuat, hangHoaOnView.ngayHetHan,
                                                         hangHoaOnView.nhaCungCap)
            self.addProductUseCase.execute(requestData)
            pass
        elif isinstance(hangHoaOnView, AddProductHangSanhSuOnView):
            requestData = AddProductHangSanhSuInputDTO(hangHoaOnView.tenHang, hangHoaOnView.soLuongTon,
                                                       hangHoaOnView.donGia, hangHoaOnView.tenLoaiHang,
                                                       hangHoaOnView.nhaSanXuat, hangHoaOnView.ngayNhapKho)

            self.addProductUseCase.execute(requestData)
            pass
        elif isinstance(hangHoaOnView, AddProductHangDienMayOnView):
            requestData = AddProductHangDienMayInputDTO(hangHoaOnView.tenHang, hangHoaOnView.soLuongTon,
                                                        hangHoaOnView.donGia, hangHoaOnView.tenLoaiHang,
                                                        hangHoaOnView.thoiGianBaoHanh, hangHoaOnView.congSuat)
            self.addProductUseCase.execute(requestData)
            pass
        pass

    def executeModifyProductUseCase(self, data):
            self.modifyProductUseCase.execute(data)
