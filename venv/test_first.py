import pytest

@pytest.mark.smoke
def test_add(a,b):
    print(a+b)


def test_multi(a,b):
    print(a * b)

test_add(3,4)
test_multi(3,3)