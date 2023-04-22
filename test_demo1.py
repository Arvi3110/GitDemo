import pytest
from pyTestsDemo.BaseClass import BaseClass

def test_firstProgram():
    print("Helo")


@pytest.mark.smoke
def test_secondProgram():
    print("GOOOOD")


@pytest.mark.xfail
def test_firstGreet():
    a = 9
    b = 10
    assert a * b == 90, "Do not match"

@pytest.mark.usefixtures("names")
class TestNames(BaseClass):
    def test_names(self, names):
        log = self.getLogger()
        log.info(names[0])
        log.info(names[2])