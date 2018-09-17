import sqlite3
# 在d盘下面的qmsvisualization文件下创建一个qmsdata.db的数据库
conn = sqlite3.connect('d:\\qmsvisualization\\qmsdata.db')
print("open database success")

#创建表语句
query_first_table = """create table  if not exists table_data_qms(
id integer primary key autoincrement,
name_qms VARCHAR(20)  ,
today_submitted int ,
week_submitted int ,
today_reviewed int ,
week_reviewed int ,
inall_submitted int ,
inall_reviewed int 
) """

query_second_table="""create table  if not exists table_data_qms_halfhour(
id integer primary key autoincrement,
name_qms VARCHAR(20)  ,
today_submitted int ,
today_reviewed int 
) """

query_test_table="""create table  if not exists table_test(
id integer primary key autoincrement,
name_qms VARCHAR(20)  ,
today_submitted int ,
today_reviewed int 
) """
#执行建表语句
conn.execute(query_first_table)
conn.execute(query_second_table)
conn.execute(query_test_table)
print("Table created successfully")

