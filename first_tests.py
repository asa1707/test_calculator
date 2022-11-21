import pytest
from app.calculator import Calculator

class TestCalc:
    def setup(self):
        self.calc = Calculator

    def test_multiply_calculate_correcty(self):
        assert self.calc.multiply(self, 2, 2) == 4

    def test_multiply_calculate_failed(self):
        assert self.calc.division(self, 4, 2) == 2

    def test_multiply_calculate_failed(self):
        assert self.calc.subtraction(self, 3, 2) == 1

    def test_multiply_calculate_failed(self):
        assert self.calc.adding(self, 7, 2) == 9