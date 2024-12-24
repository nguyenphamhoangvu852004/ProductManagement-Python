import mysql

from Entity.LoaiHang import LoaiHang
from Intefaces.DatabaseBoundary import DatabaseBoundary
from connectdb import MysqlConnection


class GetTypeListDAO(DatabaseBoundary):
    def __init__(self):
        super().__init__()
        pass

    def getTypeListDataMockList(self):
        return [
            LoaiHang("HDM", "Hàng Điện Máy"),
            LoaiHang("HSS", "Hàng Sành Sứ"),
            LoaiHang("HTP", "Hàng Thực Phẩm"),
        ]
        pass

    def getTypeListFromDatabase(self):
        type_list = []
        connection = None
        cursor = None
        try:
            # Lấy kết nối từ pool
            connection = MysqlConnection.get_connection()
            cursor = connection.cursor(dictionary=True)

            # Thực hiện truy vấn
            cursor.execute("SELECT maLoai, tenLoai FROM loaihang")
            for row in cursor.fetchall():
                type_list.append(LoaiHang(row['maLoai'], row['tenLoai']))
        except mysql.connector.Error as e:
            print(f"Database error: {e}")
            raise
        finally:
            # Đóng cursor và trả kết nối về pool
            if cursor:
                cursor.close()
            if connection:
                connection.close()

        return type_list

