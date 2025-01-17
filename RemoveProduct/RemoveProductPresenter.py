from typing import override

from Intefaces.OutputBoundary import OutputBoundary
from Intefaces.ResponseData import ResponseData
from Intefaces.Subject import Subject
from RemoveProduct.RemoveProductOutputDTO import RemoveProductOutputDTO
from RemoveProduct.RemoveProductViewModel import RemoveProductViewModel


class RemoveProductPresenter(OutputBoundary, Subject):
    def __init__(self, ):
        Subject.__init__(self)
        self.removeProductViewModel = RemoveProductViewModel(None, None)
        pass

    @override
    def exportData(self, responseData: ResponseData):
        if isinstance(responseData, RemoveProductOutputDTO):
            self.removeProductViewModel = RemoveProductViewModel(str(responseData.status), responseData.message)
            self.notify(self.removeProductViewModel)
        pass
