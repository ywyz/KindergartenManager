import os, pymysql


class SQLConnect:
    def __init__(self):
        self.host = os.getenv("MYSQL_HOST", "localhost")
        self.user = os.getenv("MYSQL_USER", "root")
        self.password = os.getenv("MYSQL_PASSWORD", "")
        self.database = os.getenv("MYSQL_DATABASE", "kindergarden")

    def connect(self):
        return pymysql.connect(
            host=self.host,
            user=self.user,
            password=self.password,
            database=self.database,
            charset="utf8mb4",
            cursorclass=pymysql.cursors.DictCursor,
        )

    def close(self, connection):
        if connection:
            connection.close()

    def execute_query(self, query, params=None):
        connection = self.connect()
        try:
            with connection.cursor() as cursor:
                cursor.execute(query, params)
                result = cursor.fetchall()
            connection.commit()
            return result
        except Exception as e:
            print(f"Error executing query: {e}")
            connection.rollback()
            return None
        finally:
            self.close(connection)

    def get_all(self, table):
        query = f"SELECT * FROM {table}"
        return self.execute_query(query)

    def get_by_id(self, table, id):
        query = f"SELECT * FROM {table} WHERE id = %s"
        return self.execute_query(query, (id,))


    def insert(self, table, data):
        columns = ', '.join(data.keys())
        placeholders = ', '.join(['%s'] * len(data))
        query = f"INSERT INTO {table} ({columns}) VALUES ({placeholders})"
        return self.execute_query(query, tuple(data.values()))
