import unittest
from contextlib import nullcontext

from ModifyProduct.ModifyProductDAO import ModifyProductDAO
from ModifyProduct.ModifyProductPresenter import ModifyProductPresenter
from ModifyProduct.ModifyProductUseCase import ModifyProductUseCase
from ModifyProduct.ModifyProductViewModel import ModifyProductViewModel
from ModifyProduct.inputDTOs.ModifyProductHangDienMayInputDTO import ModifyProductHangDienMayInputDTO
from ModifyProduct.inputDTOs.ModifyProductHangThucPhamInputDTO import ModifyProductHangThucPhamInputDTO


class ModifyProductTest(unittest.TestCase):
    def test_modify_product(self):
        database = ModifyProductDAO()
        viewModel = ModifyProductViewModel("","")
        presenter = ModifyProductPresenter(viewModel)

        useCase = ModifyProductUseCase(presenter, database)

        requestData = ModifyProductHangThucPhamInputDTO("HTP002", "Hang thuc pham sau khi chinh sua", 100, 10000, "HTP", "2022-01-02", "2024-12-2","Nha cung cap kjsdaflksdjlf;jasd so 1 the gioi")
        useCase.execute(requestData)
