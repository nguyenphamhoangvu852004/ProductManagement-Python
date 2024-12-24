from typing import override, List

from GetProductList.GetProductListResponseData import GetProductListResponseData
from GetProductList.GetProductListViewModel import GetProductListViewModel
from Intefaces.OutputBoundary import OutputBoundary
from Intefaces.ResponseData import ResponseData
from Intefaces.Subject import Subject


class GetProductListPresenter(OutputBoundary, Subject):
    def __init__(self, getProductListViewModel: List['GetProductListViewModel']):
        Subject.__init__(self)  # Gọi trực tiếp constructor của Subject
        self._getProductListViewModel = getProductListViewModel


    @override
    def exportData(self, responseData: 'ResponseData'):
        if isinstance(responseData, GetProductListResponseData):
            listOutDTO = responseData.getProducts()

            self._getProductListViewModel.clear()
            for productDTO in listOutDTO:
                productViewModel = GetProductListViewModel(
                    productDTO.maHang,
                    productDTO.tenHang,
                    productDTO.soLuongTon,
                    productDTO.donGia,
                    productDTO.VAT
                )
                self._getProductListViewModel.append(productViewModel)

            self.notify(self.fetchProductListViewModel())
        pass

    def fetchProductListViewModel(self):
        return self._getProductListViewModel
