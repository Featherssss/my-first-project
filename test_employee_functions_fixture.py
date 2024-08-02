import pytest
from employee_functions import Employee

@pytest.fixture
def individual():
    """夹具"""
    elliot = Employee('elliot','liu',50000)
    return elliot

def test_give_default_raise(individual):
    """测试默认增加工资"""
    individual.give_raise()
    assert individual.salary == 55000
    
def test_give_custom_raise(individual):
    """测试增加指定工资"""
    individual.give_raise(10000)
    assert individual.salary == 60000