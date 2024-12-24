from typing import override

from Intefaces.OutputBoundary import OutputBoundary
from Intefaces.ResponseData import ResponseData
from ModifyProduct.ModifyProductViewModel import ModifyProductViewModel
from ModifyProduct.outputDTOs.ModifyProductOutputDTO import ModifyProductOutputDTO


class ModifyProductPresenter(OutputBoundary):
    def __init__(self, viewModel: ModifyProductViewModel):
        super().__init__()
        self.viewModel = viewModel
        pass

    @override
    def exportData(self, responseData: ResponseData):
        if not isinstance(responseData, ModifyProductOutputDTO):
            self.viewModel = ModifyProductViewModel("False", "Co Loi Xay Ra")
        else:
            self.viewModel = ModifyProductViewModel(str(responseData.isSuccess), responseData.message)
        pass
