from typing import List

from GetTypeList.GetTypeListOutputDTO import GetTypeListOutputDTO
from Intefaces.ResponseData import ResponseData


class GetTypeListResponseData(ResponseData):
    def __init__(self, listOutDTO: 'List[GetTypeListOutputDTO]'):
        super().__init__()
        self.listOutDTO = listOutDTO

    def getLoaiHangs(self):
        return self.listOutDTO