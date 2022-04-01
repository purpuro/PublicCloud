from weChat import weChatSystem
import pytest
@pytest.mark.run(order=5)
# @pytest.mark.skip()
@pytest.mark.dependency(scope='session',depends=["test_login/test_login.py::test_loginSuccess"])
def test_WeChatExtract(drivers):
    result=weChatSystem.smartMeadieWeChatExtract(drivers)
    print(result)
    assert result == "提取成功！", '微信稿提取成功'
# @pytest.mark.run(order=6)
# def test_WeChatExtract(drivers):
#     print(12345)
@pytest.mark.run(order=6)
@pytest.mark.dependency(scope='session',depends=["test_login/test_login.py::test_loginSuccess"])
def test_followWeChat(drivers):
    result=weChatSystem.followWechat(drivers)
    assert  result =='添加成功', '订阅成功'
@pytest.mark.run(order=7)
@pytest.mark.dependency(scope='session',depends=["test_login/test_login.py::test_loginSuccess"])
def test_unfollowWeChat(drivers):
    result=weChatSystem.unFollowWechat(drivers)
    assert result=='已取消该微信公众号订阅','取消订阅成功'