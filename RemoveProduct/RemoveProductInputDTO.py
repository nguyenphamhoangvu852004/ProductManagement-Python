from Intefaces.RequestData import RequestData


class RemoveProductInputDTO(RequestData):
    def __init__(self, maHang: str):
        super().__init__()
        self.maHang = maHang
        pass
