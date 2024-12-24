from typing import List

from GetTypeList import GetTypeListPresenter
from GetTypeList.GetTypeListDAO import GetTypeListDAO
from GetTypeList.GetTypeListOutputDTO import GetTypeListOutputDTO
from GetTypeList.GetTypeListResponseData import GetTypeListResponseData
from Intefaces.DatabaseBoundary import DatabaseBoundary
from Intefaces.InputBoundary import InputBoundary
from Intefaces.OutputBoundary import OutputBoundary
from Intefaces.RequestData import RequestData


class GetTypeListUseCase(InputBoundary):
    def __init__(self, getTypeListDAO: DatabaseBoundary, getTypeListPresenter: OutputBoundary):
        super().__init__()
        self.getTypeListDAO = getTypeListDAO
        self.getTypeListPresenter = getTypeListPresenter
        pass

    def execute(self, requestData: 'RequestData'):
        list = self.getTypeListDAO.getTypeListFromDatabase()  # type: ignore
        listOutDTO = []

        for loaiHang in list:
            getTypeListOutputDTO = GetTypeListOutputDTO(loaiHang.tenLoai)
            listOutDTO.append(getTypeListOutputDTO)

        responseData = GetTypeListResponseData(listOutDTO)
        self.getTypeListPresenter.exportData(responseData)
        pass
