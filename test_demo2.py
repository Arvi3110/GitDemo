import pytest


def test_secondGreet():
    msg = "This is a mighty play"
    assert "ujg" in msg


@pytest.mark.smoke
def test_thirdProgram():
    print("Aravind")