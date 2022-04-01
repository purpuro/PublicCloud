import time
import datetime
from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
#微信稿提取系统-提取微信稿：输入微信稿链接提取
def smartMeadieWeChatExtract(driver):
    #进入微信稿提取系统
    locatorWechat= (By.CSS_SELECTOR, '.header-left.el-popover__reference')
    try:
        WebDriverWait(driver, 60, 0.5).until(EC.element_to_be_clickable(locatorWechat))
    except:
        return "跳转微信稿提取系统超时"
    ActionChains(driver).move_to_element(
        driver.find_element_by_css_selector(".header-left.el-popover__reference")).perform()
    driver.find_element_by_css_selector('.product-box>.apps-box>.app-item:nth-child(2)>:nth-child(1)>:nth-child(2)>.egs>span').click()
    # driver.find_element_by_xpath(
    #     '//*[@class="el-popover el-popper header-pop"]/div/div[3]/div[2]/div[1]/ul/li/span').click()
    """
    time.sleep(2)
    driver.find_element_by_css_selector('[placeholder="按时间筛选"]').click()
    time.sleep(1)
    # 筛选时间为：昨天
    driver.find_element_by_css_selector('.el-scrollbar>.el-select-dropdown__wrap.el-scrollbar__wrap>.el-scrollbar__view.el-select-dropdown__list>li:nth-child(3)').click()
    # 左侧搜索列表
    time.sleep(1)
    driver.find_element_by_css_selector('input[placeholder="搜索已订阅的公众号"]').send_keys("哈哈")
    time.sleep(1)
    # 一键清空输入信息
    driver.find_element_by_xpath('//*[@class="searchAisdeinput"]/img').click()
    """
    time.sleep(2)
    ActionChains(driver).move_to_element(
        driver.find_element_by_css_selector(".titleArea")).perform()
    driver.find_element_by_css_selector(".draw").click()
    startTime1 = datetime.datetime.now()
    print("开始时间：", startTime1)
    # 提取遮罩--提取中
    locator1 = (By.CSS_SELECTOR, '.el-loading-mask.loading-style.is-fullscreen')
    try:
        WebDriverWait(driver, 60, 0.5).until_not(EC.presence_of_element_located(locator1))
        loadingState = True
    except:
        return "稿件提取-提取中loading超时"
    if loadingState==True:
        locator2 = (By.XPATH, '/html/body/div[3][@role=\'alert\']')
    # //div[@style='min-width: 320px;' and @class='header-tool']
        try:
            WebDriverWait(driver, 60, 0.5).until(EC.visibility_of_element_located(locator2))
            extractSuccess1 = True
        except:
            return "按钮提取-提取成功提示语超时未弹出"
    if extractSuccess1 == True:
        endTime1 = datetime.datetime.now()
        print("结束时间：", endTime1)
        totalTime1 = (endTime1 - startTime1).total_seconds()
        print("稿件提取渲染时间为：", totalTime1)
        text= driver.find_element_by_xpath('/html/body/div[3]/p').text
        if text!="提取成功！":
            return "稿件提取失败"
    WebDriverWait(driver, 60, 0.5).until_not(EC.visibility_of_element_located(locator2))
    file = open(r"C:\Users\1234\Desktop\1234.txt", "r")
    detail=file.readlines()#获取文件内容
    lineNum=len(detail)#文件行数
    print('总行数：',lineNum)
    while lineNum>0:
        for num in range(len(detail)):
        # num = random.randint(0, lineNum - 1)  # 随机数
            # 提取遮罩--提取中
            locator = (By.CSS_SELECTOR, '.el-loading-mask.loading-style.is-fullscreen')
            startTime=datetime.datetime.now()
            print("开始时间：",startTime)

            # 显式等待 判断某个元素是否被加到了dom树里，并不代表该元素一定可见
            # 60s等待时间，0.5s步长，遮罩消失再进行下一步
            try:
                WebDriverWait(driver, 60, 0.5).until_not(EC.presence_of_element_located(locator))
                loadingState= True
            except:
                return "按钮提取-提取中loading超时"
            endTime=datetime.datetime.now()
            print("结束时间：",endTime)
            totalTime=(endTime-startTime).total_seconds()
            print("按钮提取渲染时间为：",totalTime)
            if loadingState:
                print("能点击了")
                time.sleep(2)
                # 点击提取微信稿按钮
                driver.find_element_by_xpath('//li[@class="weixin"]/span').click()
                url = detail[num]
                driver.find_element_by_xpath(
               '//*[@id="app"]/div/section/main/div/div[2]/div/div[2]/div/div[2]/div/input').send_keys(url)
            # 点击确定按钮
                driver.find_element_by_xpath(
               '//*[@id="app"]/div/section/main/div/div[2]/div/div[2]/div/div[3]/span/button[2]/span').click()
                # 提示语图层
                locator3 = (By.XPATH, '/html/body/div[3][@role=\'alert\']')
                # //div[@style='min-width: 320px;' and @class='header-tool']
                try:
                    WebDriverWait(driver, 60, 0.5).until(EC.visibility_of_element_located(locator3))
                    extractSuccess= True
                except:
                    return "按钮提取-提取成功提示语超时未弹出"
                if extractSuccess:
                    s1 = driver.find_element_by_xpath('/html/body/div[3]').get_attribute("class")
                    print("属性：", s1)
                    s2 = driver.find_element_by_xpath('/html/body/div[3]/p').text
                    print("文字：", s2)

                # 显示等待 等待提示语消失
                WebDriverWait(driver, 60, 0.5).until_not(EC.visibility_of_element_located(locator3))
                # 定位提取反馈信息弹窗 提取成功 提取失败 无可用套餐
                # WebDriverWait(driver, 61, 0.3).until(EC.visibility_of_element_located(locator1))
                # s=driver.find_element_by_css_selector('.el-message__content').text
                # print(s)
                print("第%d行的链接为：%s" % (num + 1, detail[num]))
                # print("提取耗时%f秒" % contentURL.elapsed.total_seconds())
                lineNum = lineNum - 1
                print("剩余行数：", lineNum)
                if lineNum==0 or s2!="提取成功！":
                    return s2

#订阅微信号
def followWechat(driver):
    # driver.refresh()
    #进入微信稿提取系统()
    locatorWechat = (By.CSS_SELECTOR, '.header-left.el-popover__reference')
    try:
        WebDriverWait(driver, 60, 0.5).until(EC.element_to_be_clickable(locatorWechat))
    except:
        return "跳转微信稿提取系统超时"
    ActionChains(driver).move_to_element(
        driver.find_element_by_css_selector(".header-left.el-popover__reference")).perform()
    driver.find_element_by_css_selector(
        '.product-box>.apps-box>.app-item:nth-child(2)>:nth-child(1)>:nth-child(2)>.egs>span').click()
    time.sleep(2)
    followAreaClass=driver.find_element_by_css_selector('.subIsShowOut>div:nth-child(1)').get_attribute("class")
    print(followAreaClass)
    if followAreaClass=="subscribedArea":
        #已有订阅
        driver.find_element_by_css_selector('div.searchButton').click()
    elif followAreaClass=="unsub-area":
        #无订阅
        driver.find_element_by_css_selector('.sub-button').click()
    driver.find_element_by_css_selector('input[placeholder="请输入微信公众号名称或者微信账号"]').send_keys("河南")
    #搜索
    driver.find_element_by_xpath('/html/body/div[3]/div/div[2]/div/div[1]/div/div/button/span').click()
    # 等待订阅按钮加入页面
    locatorSearchResult=(By.CSS_SELECTOR, '.sub')
    try:
        WebDriverWait(driver, 60, 0.5).until(EC.visibility_of_element_located(locatorSearchResult))
        searchStatus = True
    except:
        # 关闭订阅微信号搜索页面
        driver.find_element_by_xpath('/html/body/div[3]/div/div[1]/button/i').click()
        return "执行搜索超时无数据"
    if searchStatus ==True:
        # 点击订阅按钮
        driver.find_elements_by_css_selector('.sub')[0].click()
        # 获取第一个微信号的名称
        WeChatName=driver.find_elements_by_css_selector('.name')[0].text
        print("微信号名称：%s"%WeChatName)
    # 提示语图层
    locatorTips = (By.XPATH, '/html/body/div[5][@role=\'alert\']')
    # //div[@style='min-width: 320px;' and @class='header-tool']
    try:
        WebDriverWait(driver, 60, 0.5).until(EC.visibility_of_element_located(locatorTips))
        TipsStatus = True
    except:
        # 关闭订阅微信号搜索页面
        driver.find_element_by_xpath('/html/body/div[3]/div/div[1]/button/i').click()
        return "提取成功提示语超时未弹出"
    if TipsStatus:
        s1 = driver.find_element_by_xpath('/html/body/div[5]').get_attribute("class")
        print("属性：", s1)
        s2 = driver.find_element_by_xpath('/html/body/div[5]/p').text
        print("文字：", s2)
        # 等待提示语消失
        WebDriverWait(driver, 60, 0.5).until_not(EC.visibility_of_element_located(locatorTips))
        # 关闭订阅微信号搜索页面
        driver.find_element_by_xpath('/html/body/div[3]/div/div[1]/button/i').click()
        time.sleep(2)
        # 列表第一个微信号名称是否与订阅名称相同
        listName = driver.find_element_by_css_selector('.list>li:nth-child(1)>div>span').text
        print("列表的名称：%s" % listName)
        if WeChatName!=listName:
            return "订阅名称与回显名称不相同"
        return s2
#取消订阅
def unFollowWechat(driver):
    # time.sleep(2)
    ActionChains(driver).move_to_element(
        driver.find_element_by_css_selector(".iconArea")).perform()
    driver.find_element_by_css_selector('.unsubArea').click()
    # 提示语图层
    locatorTips = (By.XPATH, '/html/body/div[4][@role=\'alert\']')
    # //div[@style='min-width: 320px;' and @class='header-tool']
    try:
        WebDriverWait(driver, 60, 0.5).until(EC.visibility_of_element_located(locatorTips))
        TipsStatus = True
    except:
        return "提取成功提示语超时未弹出"
    if TipsStatus:
        s1 = driver.find_element_by_xpath('/html/body/div[4]').get_attribute("class")
        print("属性：", s1)
        s2 = driver.find_element_by_xpath('/html/body/div[4]/p').text
        return s2

"""

    time.sleep(1)
    # 点击订阅按钮
    driver.find_element_by_css_selector('div.searchButton').click()
    driver.find_element_by_css_selector('input[placeholder="请输入微信公众号名称或者微信账号"]').send_keys("河南")
    time.sleep(1)
    # 删除字符
    driver.find_element_by_css_selector('input[placeholder="请输入微信公众号名称或者微信账号"]').send_keys(Keys.BACK_SPACE)

    time.sleep(2)
    # 查询微信公号
    driver.find_element_by_xpath('/html/body/div[3]/div/div[2]/div/div[1]/div/div/button').click()
    time.sleep(2)
    # 添加订阅
    # driver.find_elements_by_css_selector('.sub-button')[0].click()
    print("这是第一个的状态：%s"%driver.find_elements_by_css_selector('.sub-button')[0].text)
    time.sleep(2)
    # 点击关闭订阅按钮
    driver.find_element_by_xpath('/html/body/div[3]/div/div[1]/button/i').click()
    time.sleep(1)
    # driver.find_element_by_css_selector('div.pf-menu>div.pf-menu-listArea>div.subscribedArea>ul.list>li:nth-child(3)').click()
    # driver.find_element_by_css_selector('.pf-menu>.pf-menu-listArea>.subscribedArea>ul.list>li:nth-child(3)').click()
    # 获取订阅列表微信号名称
    weChatName=driver.find_element_by_xpath('//*[@id="app"]/div/section/aside/div/div[2]/div/ul/li[1]/div[1]/span').text
    print(weChatName)
    time.sleep(2)
    # 鼠标悬浮展示功能入口
    ActionChains(driver).move_to_element(driver.find_element_by_css_selector('.pf-menu>.pf-menu-listArea>.subscribedArea>ul.list>li:nth-child(3)')).perform()
    time.sleep(1)
    # 取消订阅
    driver.find_element_by_css_selector('.pf-menu>.pf-menu-listArea>.subscribedArea>ul.list>li:nth-child(3)>.unsubArea').click()
    time.sleep(1)
    ss=driver.find_element_by_css_selector('.el-message.el-message--success>p.el-message__content').text
    print(ss)
"""