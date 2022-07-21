import pyodbc

connect = pyodbc.connect('DRIVER={SQL Server};'
                         'SERVER=103.24.99.76;'
                         'DATABASE=Portal_data;'
                         'UID=testUser;'
                         'PWD=Abcd.1234;')


'''Список всех таблиц'''
# cursor = connect.cursor()
# for row in cursor.tables():
#     print(row.table_name)

'''Таблица alfa_sales'''
cursor = connect.cursor()
cursor.execute('select * from alfa_sales')
rows = cursor.fetchall()
for row in rows:
    print(row[0], row[1])


