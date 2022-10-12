import pymysql
conn=pymysql.connect(user='root',password='welcome$1234',host='127.0.0.1',database='testpythondb')
cur=conn.cursor()

sql=''' create table if not exists employee (
Id int Auto_increment primary key,Name varchar(255),Age int,Address varchar(500),Salary decimal(10,2))
'''
cur.execute(sql)
cur.close()
conn.close()

noemples=int(input("enter how many employees to insert "))
def insert_rows(name,age,address,sal):
    conn = pymysql.connect(user='root', password='welcome$1234', host='127.0.0.1', database='testpythondb')
    cur = conn.cursor()
    row_data=f"insert into employee (name,age,address,Salary) values('{name}','{age}','{address}','{sal}' )"
    print(row_data)
    try:
        cur.execute(row_data)
        conn.commit()
        print("1 row inserted")
    except Exception as ex:
        print('Error')
        message=f'''An exception of type {type(ex).__name__} occured.Arguments:{ex.args}'''
        print(message)
        conn.rollback()
    finally:
        cur.close()
        conn.close()

for i in range(noemples):
    name=input("enter employee name")
    age=int(input("enter age of employee"))
    address=input("enter address of employee")
    sal=float(input("enter salary of employee"))
    insert_rows(name,age,address,sal)
    print('----------------------')

