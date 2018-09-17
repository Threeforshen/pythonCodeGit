import savedata


data_insert = '''insert into table_test 
    (name_qms   ,today_submitted   ,today_reviewed  )
    values 
    ('sq',42,21)'''
savedata.conn.execute(data_insert)

cursor=savedata.conn.cursor()
query_judge_data = '''select count(name_qms) from  table_test  '''
c=cursor.execute(query_judge_data)
r=c.fetchall()
print(r)
print(r[0])

"""
if rowcount_test.rowcount != -1 :
    print("shuju")
else:
    print("426")
"""
savedata.conn.commit()
cursor.close()
savedata.conn.close()
