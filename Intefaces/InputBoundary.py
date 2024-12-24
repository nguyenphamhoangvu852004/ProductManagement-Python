from abc import ABC, abstractmethod

from Intefaces.RequestData import RequestData


class InputBoundary(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def execute(self, requestData: RequestData):
        pass
