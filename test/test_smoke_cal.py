from Framework_RentCalculator_Project.src.app_logic import *
from Framework_RentCalculator_Project.test_data.test_data_file import *
import pytest
from time import sleep

def test_mortgage_calculator(cal_setup):
    cal_setup.get_mortgage_link()
    sleep(5)
    cal_setup.get_calculate()
    sleep(5)
    cal_setup.get_monthly_pay()
