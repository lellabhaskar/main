                #1
# import pymysql
# conn= pymysql.connect(user='root',password='welcome$1234',host='127.0.0.1')
# cur=conn.cursor()
# cur.execute(('create database testpythondb'))
#
# cur.close()
# conn.close()
# print('success')

                    #2

# import pymysql
# conn= pymysql.connect(user='root',password='welcome$1234',host='127.0.0.1',database='testpythondb')
#
# cur=conn.cursor()
# sqltablestruct='''
# create table if not exists players(id int Auto_increment primary key,name varchar(255),
# country varchar(255),ipl_team varchar(255))
# '''
# #cur.execute(sqltablestruct)y
# cur.execute('show tables')
#
# for table in cur:
#     print(table[0])
# cur.close()
# conn.close()
# print('success')


                            #3

# import pymysql
# def insert_rows(name,country,team):
#     conn= pymysql.connect(user='root',password='welcome$1234',host='127.0.0.1',database='testpythondb')
#     cur=conn.cursor()
#     sql_query=f"insert into players(Name,Country,IPL_team) values ('{name}','{country}','{team}')"
#     #sql_query=f"insert into players(Name,Country,IPL_team) values ('Sachin','India','Mumbai')"
#     print(sql_query)
#
#     try:
#         cur.execute(sql_query)
#         conn.commit()
#         print("1 row inserted")
#     except Exception as ex:
#         print('Error')
#         message=f'''An exception of type {type(ex).__name__} occured.Arguments:{ex.args}'''
#         print(message)
#         conn.rollback()
#     finally:
#         cur.close()
#         conn.close()
                        #4
# import pymysql
# conn= pymysql.connect(user='root',password='welcome$1234',host='127.0.0.1',database='testpythondb')
# cur=conn.cursor()
#
# sql_query=f"select *from players "
# #sql_query=f"update players set name='Dravid' where id=2"
#
# print(sql_query)
# cur.execute(sql_query)
# #conn.commit()
#
# while True:
#     row= cur.fetchone()
#     if row is not None:
#         print(row)
#     else:
#         break
# cur.close()
# conn.close()

                    #5
# import pymysql
# def delete_rows(name):
#     conn= pymysql.connect(user='root',password='welcome$1234',host='127.0.0.1',database='testpythondb')
#     cur=conn.cursor()
#     sql_query=f"delete from  players where name= '{name}' "
#     #sql_query=f"insert into players(Name,Country,IPL_team) values ('Sachin','India','Mumbai')"
#     print(sql_query)
#
#     try:
#         cur.execute(sql_query)
#         conn.commit()
#         print("1 row inserted")
#     except Exception as ex:
#         print('Error')
#         message=f'''An exception of type {type(ex).__name__} occured.Arguments:{ex.args}'''
#         print(message)
#         conn.rollback()
#     finally:
#         cur.close()
#         conn.close()



                                    #6


import pymysql
conn= pymysql.connect(user='root',password='welcome$1234',host='127.0.0.1',database='testpythondb')
cur=conn.cursor()

#sql_query="describe players "
#sql_query="alter table players add role varchar(255) "
sql_query="select *from players "
#sql_qurey='alter table players rename column role to speciality'
#sql_query='alter table players drop column speciality'
print(sql_query)
cur.execute(sql_query)

fetchsechme=cur.fetchall()
for index in fetchsechme:
     print(index)


cur.close()
conn.close()

def print_hi(name):
    pass


if __name__ == '__main__':
    pass
    #print_hi('PyCharm')
    # n = int(input('how many rows : '))
    # for i in range(n):
    #     name=input('Enter name:')
    #     country=input('Enter country:')
    #     team=input('Enter IPL Team:')
    #
    #     insert_rows(name,country,team)
    #
    #     print('----' )
    # n = int(input('how many rows need to delete : '))
    # for i in range(n):
    #     name=input('Enter name:')
    #     delete_rows(name)
    #     print('----' )
    square = [x ** 2 for x in [1, 2, 3, 4]]
    print(square)




