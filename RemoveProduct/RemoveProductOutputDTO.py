from Intefaces.ResponseData import ResponseData


class RemoveProductOutputDTO(ResponseData):
    def __init__(self, status: bool, message: str):
        super().__init__()
        self.status = status
        self.message = message
        pass