from Entity.HangDienMay import HangDienMay
from Entity.HangHoa import HangHoa
from Entity.HangSanhSu import HangSanhSu
from Entity.HangThucPham import HangThucPham
from Intefaces.DatabaseBoundary import DatabaseBoundary
from connectdb import MysqlConnection


class ModifyProductDAO(DatabaseBoundary):
    def __init__(self):
        super().__init__()
        pass

    def modifyProductDatabase(self, product: HangHoa):
        if not isinstance(product, HangHoa):
            return False

        connection = None
        try:
            # Lấy kết nối từ MysqlConnection
            connection = MysqlConnection.get_connection()
            cursor = connection.cursor()

            # Bước 1: Update bảng hanghoa
            query_hanghoa = """
            UPDATE hanghoa 
            SET tenHang = %s, soLuongTon = %s, donGia = %s, maLoai = %s
            WHERE maHang = %s
            """
            cursor.execute(query_hanghoa,
                           (product.tenHang, product.soLuongTon, product.donGia, product.maLoai, product.maHang))

            # Bước 2: Update bảng chi tiết
            if isinstance(product, HangDienMay):
                query_dienmay = """
                UPDATE hangdienmay 
                SET thoiGianBaoHanh = %s, congSuat = %s 
                WHERE maHang = %s
                """
                cursor.execute(query_dienmay, (product.thoiGianBaoHanh, product.congSuat, product.maHang))

            elif isinstance(product, HangSanhSu):
                query_sanhsu = """
                UPDATE hangsanhsu 
                SET nhaSanXuat = %s, ngayNhapKho = %s 
                WHERE maHang = %s
                """
                cursor.execute(query_sanhsu, (product.nhaSanXuat, product.ngayNhapKho, product.maHang))

            elif isinstance(product, HangThucPham):
                query_thucpham = """
                UPDATE hangthucpham 
                SET ngaySanXuat = %s, ngayHetHan = %s, nhaCungCap = %s 
                WHERE maHang = %s
                """
                cursor.execute(query_thucpham,
                               (product.ngaySanXuat, product.ngayHetHan, product.nhaCungCap, product.maHang))

            # Commit thay đổi
            connection.commit()
            return True

        except Exception as e:
            print(f"Error: {e}")
            if connection:
                connection.rollback()
            return False

        finally:
            # Đảm bảo kết nối được trả lại pool
            if connection and connection.is_connected():
                cursor.close()
                connection.close()
