from Entity.HangDienMay import HangDienMay
from Entity.HangSanhSu import HangSanhSu
from Entity.HangThucPham import HangThucPham
from Intefaces.DatabaseBoundary import DatabaseBoundary
from connectdb import MysqlConnection


class AddProductDAO(DatabaseBoundary):
    def __init__(self):
        super().__init__()

    def generateProductCode(self, prefix):
        """
        Sinh mã hàng tự động dựa trên tiền tố (prefix).
        """
        connectdb = MysqlConnection.get_connection()
        if not connectdb or not connectdb.is_connected():
            print("Lỗi kết nối cơ sở dữ liệu trong generateProductCode.")
            return None

        cursor = None
        try:
            cursor = connectdb.cursor()
            # Lấy mã hàng lớn nhất bắt đầu bằng tiền tố
            query = f"SELECT MAX(maHang) FROM hanghoa WHERE maHang LIKE '{prefix}%'"
            cursor.execute(query)
            max_code = cursor.fetchone()[0]

            if max_code:
                # Lấy phần số của mã hàng và cộng thêm 1
                current_number = int(max_code[len(prefix):])  # Lấy số sau tiền tố
                number = current_number + 1
            else:
                # Nếu chưa có mã hàng nào, khởi tạo số đếm bắt đầu từ 1
                number = 1

            # Tạo mã mới theo định dạng PREFIX001, PREFIX002, ...
            new_code = f"{prefix}{number:03}"  # Đảm bảo số luôn có ít nhất 3 chữ số
            return new_code
        except Exception as e:
            print(f"Lỗi khi tạo mã sản phẩm: {e}")
            return None
        finally:
            if cursor:
                cursor.close()
            if connectdb:
                connectdb.close()

    def addProduct(self, product):
        """
        Thêm sản phẩm mới vào cơ sở dữ liệu dựa trên loại sản phẩm.
        """
        connectdb = MysqlConnection.get_connection()
        if not connectdb or not connectdb.is_connected():
            print("Lỗi kết nối cơ sở dữ liệu trong addProduct.")
            return False

        cursor = None
        try:
            cursor = connectdb.cursor()

            # Xác định tiền tố mã hàng
            if isinstance(product, HangDienMay):
                prefix = "HDM"
            elif isinstance(product, HangSanhSu):
                prefix = "HSS"
            elif isinstance(product, HangThucPham):
                prefix = "HTP"
            else:
                raise ValueError("Loại sản phẩm không hợp lệ.")

            # Sinh mã hàng tự động
            product.maHang = self.generateProductCode(prefix)
            if not product.maHang:
                raise Exception("Không thể tạo mã hàng.")

            # Chèn dữ liệu vào bảng `hanghoa`
            cursor.execute(
                """
                INSERT INTO hanghoa (maHang, tenHang, soLuongTon, donGia, maLoai)
                VALUES (%s, %s, %s, %s, %s)
                """,
                (product.maHang, product.tenHang, product.soLuongTon, product.donGia, product.maLoai)
            )

            # Chèn dữ liệu vào bảng chi tiết dựa trên loại sản phẩm
            if isinstance(product, HangDienMay):
                cursor.execute(
                    """
                    INSERT INTO hangdienmay (maHang, thoiGianBaoHanh, congSuat)
                    VALUES (%s, %s, %s)
                    """,
                    (product.maHang, product.thoiGianBaoHanh, product.congSuat)
                )
            elif isinstance(product, HangSanhSu):
                cursor.execute(
                    """
                    INSERT INTO hangsanhsu (maHang, nhaSanXuat, ngayNhapKho)
                    VALUES (%s, %s, %s)
                    """,
                    (product.maHang, product.nhaSanXuat, product.ngayNhapKho)
                )
            elif isinstance(product, HangThucPham):
                cursor.execute(
                    """
                    INSERT INTO hangthucpham (maHang, ngaySanXuat, ngayHetHan, nhaCungCap)
                    VALUES (%s, %s, %s, %s)
                    """,
                    (product.maHang, product.ngaySanXuat, product.ngayHetHan, product.nhaCungCap)
                )

            # Lưu thay đổi
            connectdb.commit()
            return True
        except Exception as e:
            print(f"Lỗi khi thêm sản phẩm: {e}")
            if connectdb:
                connectdb.rollback()
            return False
        finally:
            if cursor:
                cursor.close()
            if connectdb:
                connectdb.close()
