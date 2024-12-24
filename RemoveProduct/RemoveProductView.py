from FindProduct.viewModel.FindProductHangHoaViewModel import FindProductHangHoaViewModel
from Intefaces.Observer import Observer
import tkinter as tk

from MainController import MainController
from RemoveProduct.RemoveProductViewModel import RemoveProductViewModel


class RemoveProductView(Observer):
    def __init__(self,controller:MainController):
        self.controller = controller
        self.detail_window = None  # Để kiểm tra và quản lý cửa sổ chi tiết
        self.current_view_model = None  # Lưu trữ ViewModel hiện tại

    def showView(self):
        if self.detail_window and tk.Toplevel.winfo_exists(self.detail_window):
            self.detail_window.lift()  # Đưa cửa sổ chi tiết lên trên cùng nếu nó đã tồn tại
        else:
            self.detail_window = tk.Toplevel()  # Tạo cửa sổ mới
            self.detail_window.title("Chi Tiết Sản Phẩm")
            self.detail_window.geometry("400x400")

            # Hiển thị thông báo chờ dữ liệu
            tk.Label(self.detail_window, text="Đang tải dữ liệu sản phẩm...", font=("Arial", 14)).pack(pady=20)

    def update(self, data):
        if isinstance(data, FindProductHangHoaViewModel):
            self.show_product_detail(data)
            self.current_view_model = data
        elif isinstance(data, RemoveProductViewModel):
            self.show_dialog(data)
    def show_product_detail(self, viewModel):
        if not self.detail_window or not tk.Toplevel.winfo_exists(self.detail_window):
            return  # Nếu cửa sổ không tồn tại, không thực hiện gì cả

        # Xóa nội dung cũ trong cửa sổ
        for widget in self.detail_window.winfo_children():
            widget.destroy()

        # Thêm các thông tin chi tiết sản phẩm
        labels = {
            "Mã Hàng": viewModel.maHang,
            "Tên Hàng": viewModel.tenHang,
            "Số Lượng Tồn": viewModel.soLuongTon,
            "Đơn Giá": viewModel.donGia,
            "VAT": viewModel.VAT,
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

        # Tạo các label để hiển thị thông tin
        for i, (key, value) in enumerate(labels.items()):
            tk.Label(self.detail_window, text=f"{key}:", font=("Arial", 12, "bold")).grid(row=i, column=0, sticky=tk.W, padx=10, pady=5)
            tk.Label(self.detail_window, text=value, font=("Arial", 12)).grid(row=i, column=1, sticky=tk.W, padx=10, pady=5)

        # Dòng chữ "Bạn có muốn xóa hay không?"
        tk.Label(self.detail_window, text="Bạn có muốn xóa hay không?", font=("Arial", 14, "bold"), fg="red").grid(row=len(labels), column=0, columnspan=2, pady=20)

        # Tạo các nút "Có" và "Không"
        button_frame = tk.Frame(self.detail_window)
        button_frame.grid(row=len(labels) + 1, column=0, columnspan=2, pady=10)

        tk.Button(button_frame, text="Có", font=("Arial", 12), bg="green", fg="white", width=10, command=self.confirm_delete).pack(side=tk.LEFT, padx=10)
        tk.Button(button_frame, text="Không", font=("Arial", 12), bg="red", fg="white", width=10, command=self.cancel_delete).pack(side=tk.LEFT, padx=10)

    def confirm_delete(self):
        self.controller.executeRemoveProductUseCase(self.current_view_model.maHang)
        self.controller.executeGetProductListUseCase()
    def cancel_delete(self):
        """
        Xử lý khi người dùng chọn 'Không'.
        """
        print("Hủy xóa sản phẩm.")
        if self.detail_window:
            self.detail_window.destroy()

    def show_dialog(self, message):
        if  message.isSuccess == "True":
            tk.messagebox.showinfo("Success", message.message)
            self.detail_window.destroy()
        else:
            tk.messagebox.showerror("Failed", message.message)