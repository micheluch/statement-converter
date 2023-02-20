import pytest
from statement_converter import *

class TestClassSplitLine:
    def test_split_line_defined(self):
        assert split_line is not None

    def test_split_line_returns_three_elements(self):
        assert len(split_line("12/22 MCDONALD'S F3458 CAMARILLO CA 6.31")) == 3

def test_line_to_csv_defined():
    assert line_to_csv is not None

def test_line_to_csv_returns_three_elements():
    assert len(line_to_csv("12/22 MCDONALD'S F3458 CAMARILLO CA 6.31").split(',')) == 3