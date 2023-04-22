import pytest

lst = ["Aravind", "Lal", "Loll"]

@pytest.fixture(scope="class")
def opening_Browser():
    print("I am first")
    yield
    print("Iam last")

@pytest.fixture()
def dataLoad():
    print("user profile loading...")
    return ["Aravind", "Lal", "Loll"]

@pytest.fixture(params=lst)
def names(request):
    return request.param