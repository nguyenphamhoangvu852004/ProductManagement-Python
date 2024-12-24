import unittest
from contextlib import nullcontext

from FindProduct.FindProductUseCase import FindProductUseCase
from FindProduct.FindProductPresenter import FindProductPresenter
from FindProduct.FindProductDAO import FindProductDAO
from FindProduct.FindProductInputDTO import FindProductInputDTO
from FindProduct.viewModel.FindProductHangHoaViewModel import FindProductHangHoaViewModel


class TestFindProduct(unittest.TestCase):
    def test_findProduct(self):
        databaseBoundary = FindProductDAO()
        viewModel = FindProductHangHoaViewModel(nullcontext, nullcontext, nullcontext, nullcontext, nullcontext)
        outputBoundary = FindProductPresenter(viewModel)
        useCase = FindProductUseCase(databaseBoundary, outputBoundary)
        requestData = FindProductInputDTO("HTP001")
        useCase.execute(requestData)

        print(outputBoundary.findProductHangHoaViewModel)