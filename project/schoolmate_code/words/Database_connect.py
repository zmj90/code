import pymysql


class Database:
    def __init__(self, database: str,password:str):
        """
        建立数据库连接，并生成游标
        :param database: 数据库名
        """
        self.db = pymysql.connect(
            host='localhost',
            port=3306,
            user='root',
            password=password,
            database=database,
            charset='utf8'
        )
        self.cur = self.db.cursor()

    def close(self):
        """
        关闭游标和数据库连接
        """
        self.cur.close()
        self.db.close()
