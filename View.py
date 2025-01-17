from tkinter.simpledialog import Dialog

from GetProductList.GetProductListViewModel import GetProductListViewModel
from GetTypeList.GetTypeListViewModel import GetTypeListViewModel
from Intefaces.Observer import Observer

import tkinter as tk
from tkinter import ttk


class View(Observer):
    def __init__(self, addProductView, findProductView, removeProductView, modifyProductView, mainController):
        self.mainController = mainController
        self.addProductView = addProductView
        self.findProductView = findProductView
        self.removeProductView = removeProductView
        self.modifyProductView = modifyProductView

        self.frame = tk.Tk()
        self.frame.title("Product Management")
        self.frame.geometry("1200x600")

        # Tạo tiêu đề
        titleLabel = tk.Label(self.frame, text="DANH SÁCH SẢN PHẨM", font=("Arial", 24, 'bold'))
        titleLabel.pack(pady=10, anchor='center')

        # Tạo bảng sản phẩm
        self.table_frame = tk.Frame(self.frame)
        self.table_frame.pack(fill=tk.BOTH, expand=True)

        # Tạo panel điều khiển
        self.controlPanel = tk.Frame(self.frame)
        self.controlPanel.pack(fill=tk.X, pady=10)

        # Nút reload
        reload_button = tk.Button(
            self.controlPanel,
            text="⟳",
            font=("Arial", 16),
            borderwidth=0,
            command=self.reload_products
        )
        reload_button.grid(row=0, column=0, padx=5)

        # Tạo ComboBox
        self.comboBoxLabel = tk.Label(self.controlPanel, text="Chọn danh mục:", font=("Arial", 12))
        self.comboBoxLabel.grid(row=0, column=1, padx=10)

        self.categoryComboBox = ttk.Combobox(self.controlPanel, state="readonly", font=("Arial", 12))
        self.categoryComboBox.grid(row=0, column=2, padx=5)

        self.addButton = tk.Button(self.controlPanel, text="ADD", font=("Arial", 12), command=self.openAddProductView)
        self.addButton.grid(row=0, column=3, padx=5)

        self.removeButton = tk.Button(self.controlPanel, text="REMOVE", font=("Arial", 12),
                                      command=self.openRemoveProductView)
        self.removeButton.grid(row=0, column=4, padx=5)

        self.modifyButton = tk.Button(self.controlPanel, text="MODIFY", font=("Arial", 12), command=self.openModifyProductView)
        self.modifyButton.grid(row=0, column=5, padx=5)

    def reload_products(self):
        self.mainController.executeGetProductListUseCase()

    def update(self, data):
        if isinstance(data[0], GetProductListViewModel):
            self.update_products(data)
        if isinstance(data[0], GetTypeListViewModel):
            self.update_category_comboBox(data)

    def update_products(self, products):
        # Kiểm tra xem bảng có cần làm mới không
        for widget in self.table_frame.winfo_children():
            widget.destroy()

        # Nếu không có sản phẩm nào, không tạo bảng
        if not products:
            return

        columns = ["Mã Hàng", "Tên Hàng", "Số Lượng Tồn", "Đơn Giá", "VAT"]
        self.tree = ttk.Treeview(self.table_frame, columns=columns, show="headings")

        # Tạo tiêu đề cho các cột
        for col in columns:
            self.tree.heading(col, text=col)

        # Thêm dữ liệu vào bảng
        for product in products:
            self.tree.insert("", "end", values=(
                product.maHang,
                product.tenHang,
                product.soLuongTon,
                product.donGia,
                product.vat
            ))
            # Gắn sự kiện double-click vào bảng
        self.tree.bind("<Double-1>", self.on_table_double_click)

        self.tree.pack(fill=tk.BOTH, expand=True)

    def update_category_comboBox(self, categories):
        self.categoryComboBox['values'] = ["Tất Cả"] + [category.tenHang for category in categories]
        self.categoryComboBox.current(0)

    def openAddProductView(self):
        print("Mo cua so")
        self.addProductView.show()
        self.mainController.executeGetTypeListUseCase()

    def on_table_double_click(self, event):
        # Lấy item được chọn
        selected_item = self.tree.selection()

        if selected_item:
            # Lấy giá trị từ item
            item_values = self.tree.item(selected_item, "values")

            self.findProductView.showView()

            self.mainController.executeFindProductUseCase(item_values[0])

    def openRemoveProductView(self):
        # Lấy item được chọn
        selected_item = self.tree.selection()

        if not selected_item:
            tk.messagebox.showwarning("Warning", "Vui lòng chọn sản phẩm")
            pass
        else:
            self.removeProductView.showView()
        # Lấy giá trị từ item
            item_values = self.tree.item(selected_item, "values")
            self.mainController.executeFindProductUseCase(item_values[0])

    def openModifyProductView(self):
        selected_item = self.tree.selection()
        if not selected_item:
            tk.messagebox.showwarning("Warning", "Vui lòng chọn sản phẩm")
            pass
        else:
            self.modifyProductView.showView()
        item_values = self.tree.item(selected_item, "values")
        self.mainController.executeFindProductUseCase(item_values[0])