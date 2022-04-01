from login import login
import pytest
from selenium.webdriver import ActionChains
import time
# username="18901065191"#个人账号
username='ldk'
password="111111"
loginWay="0"
@pytest.mark.run(order=1)
def test_loseUsername(drivers):
    result=login.loginIn(loginWay, '', password, drivers)
    print(result)
    assert result == "请输入账号", '缺少账号通过'

@pytest.mark.run(order=2)
def test_losePassword(drivers):
    result=login.loginIn(loginWay, username, '', drivers)
    print(result)
    assert result == "请输入密码", '缺少密码通过'

@pytest.mark.run(order=3)
def test_noneUser(drivers):
    result=login.loginIn(loginWay, 'username', "password", drivers)
    print(result)
    assert result == "当前账号不存在", '无用户通过'
@pytest.mark.dependency()
@pytest.mark.run(order=4)
def test_loginSuccess(drivers):
    result=login.loginIn(loginWay, username, password, drivers)
    print(result)
    assert result=='操作成功','登录成功'

# def test_dianji(drivers):
#     ActionChains(drivers).move_to_element(drivers.find_element_by_css_selector(".header-left.el-popover__reference")).perform()
#     # driver.find_element_by_css_selector('.product-box>.apps-box>.app-item:nth-child(2)>:nth-child(1)>:nth-child(2)>.egs>span').click()
#     time.sleep(0.5)
#     drivers.find_element_by_xpath('//*[@class="el-popover el-popper header-pop"]/div/div[3]/div[2]/div[1]/ul/li/span').click()
