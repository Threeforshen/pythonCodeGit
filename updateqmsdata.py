from selenium import webdriver
import savedata

# 1.创建Chrome浏览器对象
driver = webdriver.Chrome("D:/Python/GeckoDriver/chromedriver.exe")

# 2.通过浏览器向服务器发送URL请求
driver.get("file:///D:/PythonCode/testData/index.html")

# 3.通过tag name来定位 tbody
# data_tbody_text=driver.find_element_by_tag_name("tbody").text

data_tbody = driver.find_element_by_tag_name("tbody")
# 4.利用 td的tabindex属性值来获取相应的文本信息
a = 2

query_judge_data='select count(name_qms) from  table_data_qms_halfhour '
cursor = savedata.conn.cursor()
c=cursor.execute(query_judge_data)
rownot=c.fetchall()
print("-------")
print(rownot[0][0])
print("-------")
if rownot[0][0]!=0:
    data_delete='''delete from table_data_qms_halfhour'''
    savedata.conn.execute(data_delete)

for i in range(40):
    # 如果i超出了40，就跳出循环，因为最多只有40个9（即40个帐号）
    if i == 41:
        break
    # 姓名
    data_name = data_tbody.find_element_by_xpath("//td[@tabindex='" + a.__str__() + "' ]").text
    # 今日提交
    data_today_submitted = data_tbody.find_element_by_xpath("//td[@tabindex='" + (a + 2).__str__() + "' ]").text
    # 今日审核
    data_today_reviewed = data_tbody.find_element_by_xpath("//td[@tabindex='" + (a + 4).__str__() + "' ]").text

    data_insert = '''insert into table_data_qms_halfhour
                      (name_qms   ,today_submitted   ,today_reviewed  )
                      values
                      ('%s','%s','%s')''' % (data_name, data_today_submitted, data_today_reviewed)
    savedata.conn.execute(data_insert)
    print("insert_s")

    #print(data_name)
    #print(data_today_submitted)
    #print(data_today_reviewed)
    a = a + 9
savedata.conn.commit()
savedata.conn.close()