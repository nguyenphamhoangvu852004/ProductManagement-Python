class LoaiHang:
    def __init__(self, maLoai, tenLoai ):
        self.__maLoai = maLoai
        self.__tenLoai = tenLoai

    @property
    def tenLoai(self):
        return self.__tenLoai