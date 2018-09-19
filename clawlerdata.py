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
for i in range(40):
    # 如果i超出了40，就跳出循环，因为最多只有40个9（即40个帐号）
    if i == 41:
        break
    # 姓名
    data_name = data_tbody.find_element_by_xpath("//td[@tabindex='" + a.__str__() + "' ]").text
    # 今日提交
    data_today_submitted = data_tbody.find_element_by_xpath("//td[@tabindex='" + (a + 2).__str__() + "' ]").text
    # 本周提交
    data_week_submitted = data_tbody.find_element_by_xpath("//td[@tabindex='" + (a + 3).__str__() + "' ]").text
    # 今日审核
    data_today_reviewed = data_tbody.find_element_by_xpath("//td[@tabindex='" + (a + 4).__str__() + "' ]").text
    # 本周审核
    data_week_reviewed = data_tbody.find_element_by_xpath("//td[@tabindex='" + (a + 5).__str__() + "' ]").text
    # 总共提交
    data_all_submitted = data_tbody.find_element_by_xpath("//td[@tabindex='" + (a + 6).__str__() + "' ]").text
    # 总共审核
    data_all_reviewed = data_tbody.find_element_by_xpath("//td[@tabindex='" + (a + 7).__str__() + "' ]").text

    #注意，insert变量要使用 %s 来进行替换
    data_insert = '''insert into table_data_qms 
    (name_qms   ,today_submitted  ,week_submitted  ,today_reviewed  ,week_reviewed  ,inall_submitted  ,inall_reviewed  )
    values 
    ('%s','%s','%s','%s','%s','%s','%s')'''%(data_name,data_today_submitted,data_week_submitted,data_today_reviewed,data_week_reviewed,data_all_submitted,data_all_reviewed)
    savedata.conn.execute(data_insert)


    print(data_name)
    print(data_today_submitted)
    print(data_week_submitted)
    print(data_today_reviewed)
    print(data_week_reviewed)
    print(data_all_submitted)
    print(data_all_reviewed)
    a = a + 9
savedata.conn.commit()
savedata.conn.close()