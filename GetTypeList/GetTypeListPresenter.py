from typing import List

from GetTypeList.GetTypeListResponseData import GetTypeListResponseData
from GetTypeList.GetTypeListViewModel import GetTypeListViewModel
from Intefaces.OutputBoundary import OutputBoundary
from Intefaces.Subject import Subject


class GetTypeListPresenter(OutputBoundary, Subject):
    def __init__(self, getTypeListViewModel: List['GetTypeListViewModel']):
        Subject.__init__(self)
        self.getTypeListViewModel = getTypeListViewModel
        pass

    def exportData(self, responseData: 'GetTypeListResponseData'):
        # Làm mới danh sách để tránh trùng lặp
        self.getTypeListViewModel.clear()

        # Thêm dữ liệu mới vào ViewModel
        for loaiHang in responseData.getLoaiHangs():
            self.getTypeListViewModel.append(GetTypeListViewModel(loaiHang.tenLoai))

        # Gửi thông báo tới các Observer
        self.notify(self.getTypeListViewModel)

    def fetchTypeListViewModel(self):
        return self.getTypeListViewModel