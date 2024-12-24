import mysql.connector
from mysql.connector import pooling, Error

class MysqlConnection:
    _pool = None

    @staticmethod
    def get_connection():
        """
        Lấy kết nối MySQL từ pool. Nếu pool chưa được tạo, sẽ tạo một pool mới.

        :return: Đối tượng kết nối MySQL từ pool.
        :raises: Error nếu xảy ra lỗi trong quá trình kết nối.
        """
        if MysqlConnection._pool is None:
            try:
                # Tạo một pool kết nối với các tham số cấu hình
                MysqlConnection._pool = mysql.connector.pooling.MySQLConnectionPool(
                    pool_name="mypool",        # Tên của pool
                    pool_size=10,              # Số lượng kết nối tối đa trong pool
                    host="localhost",          # Host MySQL
                    database="products_shop",  # Tên database
                    user="root",               # Tên người dùng MySQL
                    password="nguyenvu",       # Mật khẩu người dùng
                    connection_timeout=300     # Thời gian timeout
                )
            except Error as e:
                raise Exception("Error connecting to MySQL with pool") from e

        # Lấy kết nối từ pool
        connection = MysqlConnection._pool.get_connection()
        return connection
