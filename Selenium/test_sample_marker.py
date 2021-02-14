import pytest

@pytest.mark.smoke
def test_send_http():
    pass  # perform some webtest test for your app
    print('hello')

test_send_http()

@pytest.mark.smoke
def test_something_quick():
    pass


def test_another():
    pass


class TestClass:
    def test_method(self):
        pass