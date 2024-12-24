from AddProduct.AddProductViewModel import AddProductViewModel
from AddProduct.onViewData.AddProductHangDienMayOnView import AddProductHangDienMayOnView
from AddProduct.onViewData.AddProductHangSanhSuOnView import AddProductHangSanhSuOnView
from AddProduct.onViewData.AddProductHangThucPhamOnView import AddProductHangThucPhamOnView
from GetTypeList.GetTypeListViewModel import GetTypeListViewModel
from Intefaces.Observer import Observer

import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

class AddProductView(Observer):
    def __init__(self, mainController):
        super().__init__()
        self.mainController = mainController
        self.frame = None
        self.categoryComboBox = None
        self.dynamicFields = {}

    def show(self):
        try:
            if self.frame is None or not self.frame.winfo_exists():
                self.create_window()
            self.frame.deiconify()
        except tk.TclError:
            self.create_window()
            self.frame.deiconify()

    def create_window(self):
        # Tạo cửa sổ chính với giao diện hiện đại
        self.frame = tk.Tk()
        self.frame.title("Thêm Sản Phẩm")
        self.frame.geometry("800x700")
        self.frame.configure(bg="#f0f2f5")  # Màu nền nhẹ nhàng

        # Tạo khung chính
        main_frame = tk.Frame(self.frame, bg="#ffffff", padx=20, pady=20)
        main_frame.pack(expand=True, fill=tk.BOTH, padx=40, pady=40)

        # Tạo tiêu đề
        title_label = tk.Label(
            main_frame,
            text="THÊM SẢN PHẨM MỚI",
            font=("Arial", 22, "bold"),
            fg="#2c3e50",
            bg="#ffffff"
        )
        title_label.pack(pady=(0, 30))

        # Frame chứa nội dung chính
        content_frame = tk.Frame(main_frame, bg="#ffffff")
        content_frame.pack(expand=True, fill=tk.BOTH)

        # Cấu hình lưới
        content_frame.grid_columnconfigure(0, weight=1)
        content_frame.grid_columnconfigure(1, weight=2)

        # Các trường nhập liệu chính
        input_fields = [
            ("Tên hàng", "tenHangInput"),
            ("Số lượng tồn", "soLuongTonInput"),
            ("Đơn giá", "donGiaInput")
        ]

        for idx, (label_text, attr_name) in enumerate(input_fields):
            label = tk.Label(
                content_frame,
                text=label_text,
                font=("Arial", 14),
                fg="#34495e",
                bg="#ffffff",
                anchor="w"
            )
            label.grid(row=idx, column=0, sticky="w", padx=10, pady=10)

            entry = tk.Entry(
                content_frame,
                font=("Arial", 14),
                bd=1,
                relief="solid",
                width=40
            )
            entry.grid(row=idx, column=1, sticky="ew", padx=10, pady=10)
            setattr(self, attr_name, entry)

        # Combobox chọn loại hàng
        category_label = tk.Label(
            content_frame,
            text="Chọn loại hàng",
            font=("Arial", 14),
            fg="#34495e",
            bg="#ffffff"
        )
        category_label.grid(row=len(input_fields), column=0, sticky="w", padx=10, pady=10)

        self.categoryComboBox = ttk.Combobox(
            content_frame,
            state="readonly",
            font=("Arial", 14),
            width=37
        )
        self.categoryComboBox.grid(row=len(input_fields), column=1, sticky="ew", padx=10, pady=10)

        # Frame cho các trường động
        self.dynamicFrame = tk.Frame(content_frame, bg="#ffffff")
        self.dynamicFrame.grid(row=len(input_fields) + 1, column=0, columnspan=2, sticky="ew", padx=10, pady=10)

        # Nút thêm sản phẩm
        add_button = tk.Button(
            content_frame,
            text="Thêm sản phẩm",
            font=("Arial", 16, "bold"),
            bg="#3498db",
            fg="white",
            relief=tk.FLAT,
            padx=20,
            pady=10,
            command=self.add_product
        )
        add_button.grid(row=len(input_fields) + 2, column=0, columnspan=2, sticky="ew", padx=10, pady=20)

        # Sự kiện
        self.categoryComboBox.bind("<<ComboboxSelected>>", self.on_category_change)

        # Ẩn cửa sổ khi khởi tạo
        self.frame.withdraw()

    def add_product(self):
        tenHang = self.tenHangInput.get().strip()
        soLuongTon = self.soLuongTonInput.get().strip()
        donGia = self.donGiaInput.get().strip()
        selected_category = self.categoryComboBox.get()

        # Kiểm tra dữ liệu nhập vào
        if not tenHang or not soLuongTon or not donGia or not selected_category:
            raise ValueError("Vui lòng nhập đầy đủ thông tin.")

        # Chuyển đổi kiểu dữ liệu
        soLuongTon = int(soLuongTon)  # Nếu là số nguyên
        donGia = float(donGia)  # Nếu là số thực

        # Xử lý trường động theo loại hàng
        if selected_category == "Hàng Sành Sứ":
            nhaSanXuat = self.dynamicFields["nhaSanXuat"].get().strip()
            ngayNhapKho = self.dynamicFields["ngayNhapKho"].get().strip()
            hangHoaOnView = AddProductHangSanhSuOnView(
                tenHang, soLuongTon, donGia, selected_category, nhaSanXuat, ngayNhapKho
            )
        elif selected_category == "Hàng Thực Phẩm":
            ngaySanXuat = self.dynamicFields["ngaySanXuat"].get().strip()
            ngayHetHan = self.dynamicFields["ngayHetHan"].get().strip()
            nhaCungCap = self.dynamicFields["nhaCungCap"].get().strip()
            hangHoaOnView = AddProductHangThucPhamOnView(
                tenHang, soLuongTon, donGia, selected_category, ngaySanXuat, ngayHetHan, nhaCungCap
            )
        elif selected_category == "Hàng Điện Máy":
            thoiGianBaoHanh = self.dynamicFields["thoiGianBaoHanh"].get().strip()
            congSuat = self.dynamicFields["congSuat"].get().strip()
            hangHoaOnView = AddProductHangDienMayOnView(
                tenHang, soLuongTon, donGia, selected_category, thoiGianBaoHanh, congSuat
            )
        else:
            raise ValueError("Loại hàng không hợp lệ.")

        self.mainController.executeAddProductUseCase(hangHoaOnView)

    def update(self, data):
        if isinstance(data, AddProductViewModel):
            self.update_notify_dialog_box(data)
        elif isinstance(data, list) and data and isinstance(data[0], GetTypeListViewModel):
            self.update_category_comboBox(data)

    def update_category_comboBox(self, categories):
        if self.categoryComboBox:
            self.categoryComboBox['values'] = [category.tenHang for category in categories]
            self.categoryComboBox.current(0)

    def on_category_change(self, event):
        selected_category = self.categoryComboBox.get()
        self.update_dynamic_fields(selected_category)

    def update_dynamic_fields(self, category):
        # Xóa các trường động cũ
        for widget in self.dynamicFrame.winfo_children():
            widget.destroy()

        # Thêm các trường động tùy theo loại hàng
        if category == "Hàng Thực Phẩm":
            # Sử dụng DateEntry thay cho Entry thông thường
            self.add_dynamic_date_field("Ngày sản xuất:", "ngaySanXuat")
            self.add_dynamic_date_field("Ngày hết hạn:", "ngayHetHan")
            self.add_dynamic_field("Nhà cung cấp:", "nhaCungCap")
        elif category == "Hàng Điện Máy":
            self.add_dynamic_field("Thời gian bảo hành:", "thoiGianBaoHanh")
            self.add_dynamic_field("Công suất:", "congSuat")
        elif category == "Hàng Sành Sứ":
            self.add_dynamic_field("Nhà sản xuất:", "nhaSanXuat")
            self.add_dynamic_date_field("Ngày nhập kho:", "ngayNhapKho")

    def add_dynamic_field(self, label_text, field_key):
        label = tk.Label(
            self.dynamicFrame,
            text=label_text,
            font=("Arial", 14),
            fg="#34495e",
            bg="#ffffff"
        )
        label.pack(pady=5, anchor="w")

        entry = tk.Entry(
            self.dynamicFrame,
            font=("Arial", 14),
            bd=1,
            relief="solid",
            width=40
        )
        entry.pack(pady=5, anchor="w")
        self.dynamicFields[field_key] = entry

    def add_dynamic_date_field(self, label_text, field_key):
        label = tk.Label(
            self.dynamicFrame,
            text=label_text,
            font=("Arial", 14),
            fg="#34495e",
            bg="#ffffff"
        )
        label.pack(pady=5, anchor="w")

        # Sử dụng DateEntry từ thư viện tkcalendar
        date_entry = DateEntry(
            self.dynamicFrame,
            width=37,
            background='darkblue',
            foreground='white',
            borderwidth=2,
            font=("Arial", 14),
            date_pattern='dd/mm/yyyy'  # Định dạng ngày tháng Việt Nam
        )
        date_entry.pack(pady=5, anchor="w")
        self.dynamicFields[field_key] = date_entry

    def update_notify_dialog_box(self, data):
        if data.isSuccess == "True":
            tk.messagebox.showinfo("Thêm sản phẩm", data.message)
            self.frame.destroy()
        else:
            tk.messagebox.showerror("Thêm sản phẩm", data.message)
