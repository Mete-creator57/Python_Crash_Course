import pytest
from employee import Employee


@pytest.fixture
def employee_instance():
    """Create a class fixture to reuse for another methods"""
    employee = Employee('Mete', 'Tunkiz', 6000)
    return employee


def test_give_default_raise(employee_instance):
    """Test the default promotion"""
    employee_instance.give_raise()
    assert employee_instance.annual_salary == 11000 


