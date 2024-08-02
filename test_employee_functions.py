import pytest
from employee_functions import Employee

def test_give_default_raise():
    """测试默认增加工资"""
    elliot = Employee('elliot','liu',50000)
    elliot.give_raise()
    assert elliot.salary == 55000
    
def test_give_custom_raise():
    """测试增加指定工资"""
    elliot = Employee('elliot','liu',50000)
    elliot.give_raise(10000)
    assert elliot.salary == 60000