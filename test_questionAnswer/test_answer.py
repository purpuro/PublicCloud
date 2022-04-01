import pytest
from questionAnswer import questionAnswer
import time
@pytest.mark.dependency(scope='session',depends=["test_login/test_login.py::test_loginSuccess"])
def test_log(drivers):
    questionAnswer.quertionAnswer(drivers)
    time.sleep(5)
    print("haha")