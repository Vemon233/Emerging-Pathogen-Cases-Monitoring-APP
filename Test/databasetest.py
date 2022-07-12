import pymysql

conn = pymysql.connect(
                        host='localhost',
                        port=3306,
                        charset='UTF8',
                        user='root',
                        db='disease',
                        password='521365zhh',
                        )
print("success")

