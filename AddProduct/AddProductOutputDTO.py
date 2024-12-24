from Intefaces.ResponseData import ResponseData


class AddProductOutputDTO(ResponseData):
    def __init__(self, isSuccess: bool, message: str):
        super().__init__()
        self.isSuccess = isSuccess
        self.message = message
