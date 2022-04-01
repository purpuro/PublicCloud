from selenium import webdriver
from selenium.webdriver import ActionChains
import time
#定位页面是否包含元素，根据link_text方法
def isElementExist(driver, element):
    flag = True
    browser = driver
    try:
        browser.find_element_by_css_selector(element)
        return flag
    except:
        flag = False
        return flag
driver = webdriver.Chrome()  # 调用浏览器驱动
driver.maximize_window()  # 窗口最大化
driver.get("https://graph.qq.com/oauth2.0/show?which=Login&display=pc&response_type=code&redirect_uri=http%3A%2F%2Fspcdp.cdposs.qq.com%2Fauth%2Fcallback&client_id=101477813&state=http%3A%2F%2Fspcdp.cdposs.qq.com%2F")
time.sleep(1)
driver.switch_to.frame('ptlogin_iframe')
driver.find_element_by_xpath('//*[@id="switcher_plogin"]').click()
driver.find_element_by_xpath('//*[@id="u"]').send_keys('738243852')
driver.find_element_by_xpath('//*[@id="p"]').send_keys('738243852.')
driver.find_element_by_xpath('//*[@id="login_button"]').click()
# driver.switch_to.default_content()  # 退出iframe框架
time.sleep(1)
driver.switch_to.frame('tcaptcha_iframe')

flag=1
while flag<100:
    # 定位滑块
    slider = driver.find_element_by_xpath('//*[@id="tcaptcha_drag_thumb"]')
    a = ActionChains(driver)
    a.click_and_hold(slider).move_by_offset(100+flag, 0).perform()
    a.release().perform()  # 鼠标释放
    elementFlag=isElementExist(driver,'.tc-opera.show-success')
    print(elementFlag)
    flag+=1

