import tkinter as tk
from typing import override

from AddProduct.AddProductOutputDTO import AddProductOutputDTO
from AddProduct.AddProductViewModel import AddProductViewModel
from Intefaces.OutputBoundary import OutputBoundary
from Intefaces.ResponseData import ResponseData
from Intefaces.Subject import Subject


class AddProductPresenter(OutputBoundary, Subject):
    def __init__(self):
        Subject.__init__(self)
        self.addProductViewModel = AddProductViewModel(None, None)
        pass

    @override
    def exportData(self, responseData: ResponseData):
        if isinstance(responseData, AddProductOutputDTO):
            self.addProductViewModel = AddProductViewModel(str(responseData.isSuccess), responseData.message)
            self.notify(self.addProductViewModel)
        pass
