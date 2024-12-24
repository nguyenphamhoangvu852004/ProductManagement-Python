from abc import abstractmethod

from Intefaces.ResponseData import ResponseData


class OutputBoundary:
    def __init__(self):
        pass

    @abstractmethod
    def exportData(self,responseData: ResponseData):
        pass