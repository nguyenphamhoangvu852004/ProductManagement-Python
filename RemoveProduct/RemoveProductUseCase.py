from typing import override

from Intefaces.DatabaseBoundary import DatabaseBoundary
from Intefaces.InputBoundary import InputBoundary
from Intefaces.OutputBoundary import OutputBoundary
from Intefaces.RequestData import RequestData
from RemoveProduct.RemoveProductInputDTO import RemoveProductInputDTO
from RemoveProduct.RemoveProductOutputDTO import RemoveProductOutputDTO


class RemoveProductUseCase(InputBoundary):
    def __init__(self, database: DatabaseBoundary, outputBoundary: OutputBoundary):
        super().__init__()
        self.database = database
        self.outputBoundary = outputBoundary

    @override
    def execute(self, requestData: RequestData):
        if isinstance(requestData, RemoveProductInputDTO):
            if self.database.removeProduct(requestData.maHang) == True:
                responseData = RemoveProductOutputDTO(True, "Xoa hang hoa thanh cong")
                self.outputBoundary.exportData(responseData)
            else:
                responseData = RemoveProductOutputDTO(False, "Xoa hang hoa that bai")
                self.outputBoundary.exportData(responseData)
        else:
            responseData = RemoveProductOutputDTO(False, "Xoa hang hoa that bai")
            self.outputBoundary.exportData(responseData)
        return

        pass
