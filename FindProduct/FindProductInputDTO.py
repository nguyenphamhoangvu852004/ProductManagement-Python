from Intefaces.RequestData import RequestData


class FindProductInputDTO(RequestData):
    def __init__(self, maHangStr: str):
        super().__init__()
        self.maHangStr = maHangStr
        pass

    @property
    def getMaHangStr(self) -> str:
        return self.maHangStr
