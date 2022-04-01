from selenium import webdriver
import pytest
@pytest.fixture(scope="session")
def drivers():
    print("主配置文件1")
    global driver
    driver = webdriver.Chrome()  # 调用浏览器驱动
    # driver.delete_all_cookies() # 清空cookies
    driver.delete_cookie('Set-Cookie')
    driver.maximize_window()  # 窗口最大化
    yield driver
    driver.close()
