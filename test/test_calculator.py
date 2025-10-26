import pytest
from calculator import add
from calculator import subtract


# 测试正常情况
def test_add_normal():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(0, 0) == 0


# 测试边界情况（如大数值）
def test_add_boundary():
    assert add(1000000, 2000000) == 3000000


# 测试异常情况（如非数值输入）
def test_add_exception():
    with pytest.raises(TypeError):
        add("2", 3)  # 字符串与数字相加
    with pytest.raises(TypeError):
        add(None, 5)


def test_subtract_normal():
    assert subtract(5, 3) == 2
    assert subtract(-2, -3) == 1


def test_subtract_boundary():
    assert subtract(1000, 999) == 1


def test_subtract_exception():
    with pytest.raises(TypeError):
        subtract("5", 2)

