from typing import List

from GetProductList.GetProductListOutputDTO import GetProductListOutputDTO
from Intefaces.ResponseData import ResponseData


class GetProductListResponseData(ResponseData):
    def __init__(self, products: List['GetProductListOutputDTO']):
        super().__init__()
        self.products = products
        pass

    def getProducts(self):
        return self.products
