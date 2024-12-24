from FindProduct.dtos.FindProductHangHoaOutputDTO import FindProductHangHoaOutputDTO
from Intefaces.ResponseData import ResponseData


class FindProductResponseData(ResponseData):
    def __init__(self, productDTO: FindProductHangHoaOutputDTO, isExist: bool, message: str):
        super().__init__()
        self.productDTO = productDTO
        self.isExist = isExist
        self.message = message

    def __str__(self) -> str:
        return f"FindProductResponseData(productDTO={self.productDTO},isExist={self.isExist},message={self.message})"
