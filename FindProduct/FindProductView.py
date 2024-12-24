from Intefaces.Observer import Observer
import tkinter as tk


class FindProductView(Observer):
    def __init__(self):
        super().__init__()
        self.detail_window = None  # Để kiểm tra và quản lý cửa sổ chi tiết

    def showView(self):
        """
        Hiển thị cửa sổ chi tiết sản phẩm.
        """
        if self.detail_window and tk.Toplevel.winfo_exists(self.detail_window):
            self.detail_window.lift()  # Đưa cửa sổ chi tiết lên trên cùng nếu nó đã tồn tại
        else:
            self.detail_window = tk.Toplevel()  # Tạo cửa sổ mới
            self.detail_window.title("Chi Tiết Sản Phẩm")
            self.detail_window.geometry("400x300")

            # Hiển thị thông báo chờ dữ liệu
            tk.Label(self.detail_window, text="Đang tải dữ liệu sản phẩm...", font=("Arial", 14)).pack(pady=20)

    def update(self, data):
        self.show_product_detail(data)

    def show_product_detail(self, viewModel):
        """
        Hiển thị thông tin chi tiết sản phẩm trong cửa sổ.
        """
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
            tk.Label(self.detail_window, text=f"{key}:", font=("Arial", 12, "bold")).grid(row=i, column=0, sticky=tk.W,
                                                                                          padx=10, pady=5)
            tk.Label(self.detail_window, text=value, font=("Arial", 12)).grid(row=i, column=1, sticky=tk.W, padx=10,
                                                                              pady=5)
