import time
import datetime
from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
# //*[@class="el-popover el-popper header-pop"]/div/div[3]/div[1]/div[1]/ul/li[4]/span
# .apps-box>div:nth-child(1)>div:nth-child(1)>ul>li:nth-child(4)
# 进入答题系统
def quertionAnswer(driver):
    # 进入答题系统
    locatorWechat = (By.CSS_SELECTOR, '.header-left.el-popover__reference')
    try:
        WebDriverWait(driver, 60, 0.5).until(EC.element_to_be_clickable(locatorWechat))
    except:
        return "跳转答题系统超时"
    ActionChains(driver).move_to_element(
        driver.find_element_by_css_selector(".header-left.el-popover__reference")).perform()
    driver.find_element_by_css_selector(
        '.apps-box>div:nth-child(1)>div:nth-child(1)>ul>li:nth-child(4)>span').click()
    print("跳转答题")