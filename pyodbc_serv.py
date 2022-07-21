import pyodbc

connect = pyodbc.connect('DRIVER={SQL Server};'
                         'SERVER=103.24.99.76;'
                         'DATABASE=Portal_data;'
                         'UID=testUser;'
                         'PWD=Abcd.1234;')

cursor = connect.cursor()

"""Create table named my_alfa_sales"""

cursor.execute('''create table my_alfa_sales(
        company_name TEXT NOT NULL,
        all_value TEXT NOT NULL);
        ''')

connect.commit()

"""Insert the data from alfa_sales"""

cursor.execute('''INSERT INTO my_alfa_sales (company_name, all_value)
                    SELECT company_name, all_value FROM alfa_sales''')

connect.commit()

"""List of all tables"""

# for row in cursor.tables():
#     if row[3] == 'TABLE':
#         print(row[2])

"""Select the data from new table"""

# cursor.execute('select * from my_alfa_sales')
# rows = cursor.fetchmany(9)
# for row in rows:
#     print(row)
