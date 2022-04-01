from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import time
import requests
import json
import base64
# import smartMedia
import re
import sys
loginUrl = "http://yun.test.pdmiryun.com/statics/cloud-application-site/#/login"
# 登录请求函数
# loginWay 1代表机构登录 2代表个人登录
def loginRequest(userName,passWord,loginWay):
    # 登录接口
    loginUrl = 'http://yun.test.pdmiryun.com/auth/login'
    user = (("%s,%s"%(int(loginWay)+1,userName)))
    data = {'username': user, 'password': passWord}
    # 创建Session，并使用Session登录
    global ses
    ses = requests.Session()
    # 登录密令进行
    secret = "yun-test-h5:yun-test-h5"
    secretCode = "Basic "+str(base64.b64encode(secret.encode("utf-8")), "utf-8")
    headers = {'Authorization': secretCode,'from':'test','Accept-Language':'zh-CN,zh;q=0.9,en;q=0.8'}
    global access
    respone = ses.post(loginUrl, data, headers=headers)
    respone_json = json.loads(respone.content)
    print("登录接口耗费时间：",respone.elapsed.total_seconds())
    # 登录成功后，设置cookie
    print(respone_json)
    if respone_json['status']=="200":
        print("头信息：",respone.headers['Server'])
        # print(respone.headers)
        respone_header=respone.headers["Set-Cookie"]
        # 匹配第一次出现的access_token
        result = re.findall(".*access_token=(.*?); Domain=.*", respone_header)
        access=result[0]
        # print(access)
        # print(result[0])

    # print(respone_json['status'])

    return respone_json
# 首页登录测试函数
# loginWay 0代表机构登录,1代表个人登录
# userName 用户名 passWord 密码
# isContinue 是否继续 0否 1是
def loginIn(loginWay,userName,passWord,driver):
    # driver.refresh()
    # 获取当前使用何种方式登录
    driver.get(loginUrl)
    if loginWay =="0":
        print("使用机构方式登录")
        a = driver.find_element_by_xpath('//div[@class="tit clearfix"]/span[1]')
        a.click()
        # print(a.text)
        # 机构账号登录
        # 定位机构用户账号
        # js = 'document.querySelector(\'input[type="tel"]\').value="";'
        # driver.execute_script(js)
        driver.find_element_by_xpath('//input[@type="tel"]').clear()
        driver.find_element_by_xpath('//input[@type="tel"]').send_keys(userName)
        # 获取输入框的输入值
        s=driver.find_element_by_xpath('//input[@type="tel"]').get_property('value')
        # print("这是输入框的值：%s"%s)
        # 定位机构账号密码
        driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/p[2]/div/input').clear()
        driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/p[2]/div/input').send_keys(passWord)
        # print("账号长度：", len(userName))
        # print("密码长度：", len(passWord))
        # 账号为空
        if userName=="":
            # 定位登录按钮
            driver.find_element_by_css_selector('.h_btn').click()
            # a=driver.find_element_by_xpath('//input[@type="tel"]').get_property('placeholder')
            # print("值:%s"%a)
            # 显式等待 判断某个元素是否被加到了dom树里，并不代表该元素一定可见
            # 60s等待时间，0.5s步长，遮罩消失再进行下一步
            locator=(By.CSS_SELECTOR, '.el-message__content')
            try:
                WebDriverWait(driver, 10, 0.1).until(EC.visibility_of_element_located(locator))
                F = driver.find_element_by_css_selector('.el-message__content')

                return F.text #请输入账号
            except:
                print('超时未定位到元素')
                driver.close()
                return False
        # 账号不为空，密码为空
        elif userName!="" and passWord=="":
            # 定位登录按钮
            driver.find_element_by_css_selector('.h_btn').click()
            locator1 = (By.CSS_SELECTOR, '.el-message__content')
            try:
                WebDriverWait(driver, 10, 0.1).until(EC.visibility_of_element_located(locator1))
                F = driver.find_element_by_css_selector('.el-message__content')
                # print("无密码：%s"%F)
                return F.text #请输入密码
            except:
                print('超时未定位到元素1')
                # driver.close()
                return False
        # 用户不存在
        elif userName !=None and passWord!=None:
            # 定位登录按钮
            driver.find_element_by_css_selector('.h_btn').click()
            respone=loginRequest(userName,passWord,loginWay)
            # print("msg:",respone['msg'])
            if respone['status']=="500":
                text = driver.find_element_by_css_selector("span.errTip").text
                if text ==respone['msg']:
                    print("用户不存在/密码错误测试通过")
                    return text #当前用户不存在
                else:
                    print("登录异常:%s"%respone['msg'])
                    return respone['msg']
            elif respone['status']=="200":
                print("接口返回成功")
                return respone['msg']#操作成功
    elif loginWay=="1":
        print("使用个人方式登录")
        driver.find_element_by_xpath('//div[@class="tit clearfix"]/span[2]').click()
        a = driver.find_element_by_css_selector('span.act')
        print(a.text)
        # 个人登录
        # 定位个人用户账号
        driver.find_element_by_xpath('//input[@type="tel"]').clear()
        driver.find_element_by_xpath('//input[@type="tel"]').send_keys(userName)
        x=driver.find_element_by_xpath('//input[@type="tel"]').get_property('value')
        print(x)
        # 定位个人用户密码
        driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/p[2]/div/input').clear()
        driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/p[2]/div/input').send_keys(passWord)
        # 定位登录按钮
        driver.find_element_by_css_selector('.h_btn').click()
        # 个人账号为空
        if userName == "":
            locator = (By.CSS_SELECTOR, '.el-message__content')
            try:
                WebDriverWait(driver, 10, 0.5).until(EC.visibility_of_element_located(locator))
                F = driver.find_element_by_css_selector('.el-message__content')
                return F.text
            except:
                print('超时未定位到元素')
                driver.close()
                return False
        # 个人密码为空
        elif userName != "" and passWord == "":

            locator = (By.CSS_SELECTOR, '.el-message__content')
            try:
                WebDriverWait(driver, 10, 0.5).until(EC.visibility_of_element_located(locator))
                F = driver.find_element_by_css_selector('.el-message__content')
                print(F.text)
                return F.text
            except:
                print('超时未定位到元素')
                driver.close()
                return False
        # 用户不存在
        elif userName != "" and passWord != "":
            driver.find_element_by_css_selector('.h_btn').click()
            respone = loginRequest(userName, passWord, loginWay)
            # 定位登录按钮
            print(type(respone['status']))
            print(respone['status'])


            if respone['status'] == "500":
                text = driver.find_element_by_css_selector("span.errTip").text
                if text == respone['msg']:
                    print("用户不存在/密码错误测试通过")
                    return text#用户不存在
                else:
                    print("登录异常%s" % respone['msg'])
                    return respone['msg']
            elif respone['status'] == "200":
                print("接口返回成功")
                return respone['msg']
            else:
                print("都不是",respone)
                return False
def start():
    code = 1
    while code:
        # input输入值为string类型
        loginCode = (input("请输入登录方式：(0机构/1个人)"))
        if loginCode == "0":
            print("机构登录")
            userName = input("请输入用户名或手机号：")
            passWord = input("请输入密码：")
            print("账号长度：", len(userName))
            print("密码长度：", len(passWord))
            loginIn(loginCode, userName, passWord)
            code = 0
        elif loginCode=="1":
            print("个人登录")
            userName = input("请输入手机号：")
            while len(userName)!=11 or userName.isdigit()==0:
                print("手机号位数11位，请重新输入")
                userName = input("请输入手机号：")
            passWord = input("请输入密码：")
            loginIn(loginCode, userName, passWord)
            code = 0
        else:
            print("输入格式有误，请重新输入")
            code = 1
    return
# start()
