from typing import override
from tkcalendar import DateEntry
import tkinter as tk

from FindProduct.viewModel.FindProductHangHoaViewModel import FindProductHangHoaViewModel
from Intefaces.Observer import Observer
from MainController import MainController
from ModifyProduct.inputDTOs.ModifyProductHangDienMayInputDTO import ModifyProductHangDienMayInputDTO
from ModifyProduct.inputDTOs.ModifyProductHangHoaInputDTO import ModifyProductHangHoaInputDTO
from ModifyProduct.inputDTOs.ModifyProductHangSanhSuInputDTO import ModifyProductHangSanhSuInputDTO
from ModifyProduct.inputDTOs.ModifyProductHangThucPhamInputDTO import ModifyProductHangThucPhamInputDTO


class ModifyProductView(Observer):
    def __init__(self, mainController: MainController):
        super().__init__()
        self.mainController = mainController
        self.detail_window = None  # Để kiểm tra và quản lý cửa sổ chi tiết
        self.current_view_model = None  # Lưu trữ ViewModel hiện tại

    def showView(self):
        self.buildView()
        pass

    def buildView(self):
        if self.detail_window and tk.Toplevel.winfo_exists(self.detail_window):
            self.detail_window.lift()  # Đưa cửa sổ chi tiết lên trên cùng nếu nó đã tồn tại
        else:
            self.detail_window = tk.Toplevel()  # Tạo cửa sổ mới
            self.detail_window.title("Chi Tiết Sản Phẩm")
            self.detail_window.geometry("400x400")

            # Hiển thị thông báo chờ dữ liệu
            tk.Label(self.detail_window, text="Đang tải dữ liệu sản phẩm...", font=("Arial", 14)).pack(pady=20)
        pass

    @override
    def update(self, data):
        if isinstance(data, FindProductHangHoaViewModel):
            self.current_view_model = data
            self.show_product_detail(data)
        pass

    def show_product_detail(self, viewModel):
        if not self.detail_window or not tk.Toplevel.winfo_exists(self.detail_window):
            return  # Nếu cửa sổ không tồn tại, không thực hiện gì cả

        # Xóa nội dung cũ trong cửa sổ
        for widget in self.detail_window.winfo_children():
            widget.destroy()

        # Dictionary để lưu trữ các Entry
        self.entries = {}

        # Thông tin sản phẩm chính
        labels = {
            "Mã Hàng": viewModel.maHang,
            "Tên Hàng": viewModel.tenHang,
            "Số Lượng Tồn": viewModel.soLuongTon,
            "Đơn Giá": viewModel.donGia,
        }

        # Kiểm tra các thuộc tính mở rộng và thêm nếu có
        optional_attributes = {
            "Thời Gian Bảo Hành": "thoiGianBaoHanh",
            "Công Suất": "congSuat",
            "Nhà Sản Xuất": "nhaSanXuat",
            "Ngày Nhập Kho": "ngayNhapKho",
            "Ngày Sản Xuất": "ngaySanXuat",
            "Ngày Hết Hạn": "ngayHetHan",
            "Nhà Cung Cấp": "nhaCungCap",
        }

        for key, attr in optional_attributes.items():
            if hasattr(viewModel, attr):
                labels[key] = getattr(viewModel, attr)

        # Tạo các input để hiển thị và chỉnh sửa thông tin
        for i, (key, value) in enumerate(labels.items()):
            tk.Label(self.detail_window, text=f"{key}:", font=("Arial", 12, "bold")).grid(row=i, column=0, sticky=tk.W,
                                                                                          padx=10, pady=5)
            if "Ngày" in key:
                entry = DateEntry(self.detail_window, font=("Arial", 12), width=18)
                entry.set_date(value)
            else:
                entry = tk.Entry(self.detail_window, font=("Arial", 12))
                entry.insert(0, value)  # Điền giá trị hiện tại vào Entry
            entry.grid(row=i, column=1, sticky=tk.W, padx=10, pady=5)
            self.entries[key] = entry

        # Nút lưu thay đổi
        save_button = tk.Button(self.detail_window, text="Lưu Thay Đổi", font=("Arial", 12, "bold"),
                                command=self.save_changes)
        save_button.grid(row=len(labels), column=0, columnspan=2, pady=20)

    def save_changes(self):
        updated_data = {}
        requestData: ModifyProductHangHoaInputDTO = None
        for key, entry in self.entries.items():
            if isinstance(entry, DateEntry):
                updated_data[key] = entry.get_date()
            else:
                updated_data[key] = entry.get()
        print("Dữ liệu sau khi chỉnh sửa:", updated_data)

        maloai = updated_data["Mã Hàng"][:3]
        print(maloai)
        if updated_data["Mã Hàng"].startswith("HDM"):
            requestData = ModifyProductHangDienMayInputDTO(
                updated_data["Mã Hàng"],
                updated_data["Tên Hàng"],
                updated_data["Số Lượng Tồn"],
                updated_data["Đơn Giá"],
                maloai,
                updated_data["Thời Gian Bảo Hành"],
                updated_data["Công Suất"],
            )
        elif updated_data["Mã Hàng"].startswith("HSS"):
            requestData = ModifyProductHangSanhSuInputDTO(
                updated_data["Mã Hàng"],
                updated_data["Tên Hàng"],
                updated_data["Số Lượng Tồn"],
                updated_data["Đơn Giá"],
                maloai,
                updated_data["Nhà Sản Xuất"],
                updated_data["Ngày Nhập Kho"],

            )
            print(requestData.__str__())
        elif updated_data["Mã Hàng"].startswith("HTP"):
            requestData = ModifyProductHangThucPhamInputDTO(
                updated_data["Mã Hàng"],
                updated_data["Tên Hàng"],
                updated_data["Số Lượng Tồn"],
                updated_data["Đơn Giá"],
                maloai,
                updated_data["Ngày Sản Xuất"],
                updated_data["Ngày Hết Hạn"],
                updated_data["Nhà Cung Cấp"],
            )
        self.mainController.executeModifyProductUseCase(requestData)
