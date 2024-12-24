from typing import override

from GetProductList.GetProductListDAO import GetProductListDAO
from GetProductList.GetProductListOutputDTO import GetProductListOutputDTO
from GetProductList.GetProductListPresenter import GetProductListPresenter
from GetProductList.GetProductListResponseData import GetProductListResponseData
from Intefaces.DatabaseBoundary import DatabaseBoundary
from Intefaces.InputBoundary import InputBoundary
from Intefaces.OutputBoundary import OutputBoundary
from Intefaces.RequestData import RequestData


class GetProductListUseCase(InputBoundary):
    def __init__(self, getProductListDAO: DatabaseBoundary, getProductListPresenter: OutputBoundary):
        self.getProductListDAO = getProductListDAO
        self.getProductListPresenter = getProductListPresenter
        super().__init__()
        pass

    @override
    def execute(self, requestData: RequestData):
        list = self.getProductListDAO.getProductListFromDatabase()  # type: ignore
        listOutDTO = []
        for item in list:
            productDTO = GetProductListOutputDTO(
                item.maHang,
                item.tenHang,
                item.soLuongTon,
                item.donGia,
                item.tinhVat()
            )
            listOutDTO.append(productDTO)

        responseData = GetProductListResponseData(listOutDTO)
        self.getProductListPresenter.exportData(responseData)

        pass
