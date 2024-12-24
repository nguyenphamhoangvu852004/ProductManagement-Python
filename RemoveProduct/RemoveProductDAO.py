from Intefaces.DatabaseBoundary import DatabaseBoundary
from connectdb import MysqlConnection


class RemoveProductDAO(DatabaseBoundary):
    def __init__(self):
        super().__init__()

    def removeProduct(self, maHang: str):
        connectdb = MysqlConnection.get_connection()
        try:
            # Sử dụng cursor trong block `with` để tự động đóng khi xong
            with connectdb.cursor() as cursor:
                cursor.execute("DELETE FROM hanghoa WHERE maHang = %s", (maHang,))
                connectdb.commit()
                return True
        except Exception as e:
            # In lỗi chi tiết ra để debug
            print(f"Lỗi khi xóa sản phẩm: {e}")
            return False
