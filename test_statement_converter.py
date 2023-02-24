import pytest
import os
import filecmp as fc
from statement_converter import *

INPUT_FILE_NAME  = 'input_lines.txt'
OUTPUT_FILE_NAME = 'output_lines.txt'
INPUT_FILE_PATH  = './test_data/' + INPUT_FILE_NAME
OUTPUT_FILE_PATH = './test_data/' + OUTPUT_FILE_NAME

''' Test split_line function '''
def test_split_line_defined():
        assert split_line is not None

def test_split_line_returns_three_elements():
        assert len(split_line("12/22 MCDONALD'S F3458 CAMARILLO CA 6.31")) == 3

''' Test line_to_csv function '''
def test_line_to_csv_defined():
    assert line_to_csv is not None

def test_line_to_csv_returns_three_elements():
    assert len(line_to_csv("12/22 MCDONALD'S F3458 CAMARILLO CA 6.31").split(',')) == 3

''' Test convert_file function '''
def test_convert_file_defined():
    assert convert_file is not None

def test_convert_file_raises_exception_on_nonexistant_file():
    with pytest.raises(FileNotFoundError):
        convert_file('fake', 'fake') 

def test_convert_file_saves_new_file(output_file_path):
    #output_path = tmp_path / "output_lines.txt"
    convert_file(INPUT_FILE_PATH, output_file_path)
    assert output_file_path.read_text() is not None

def test_convert_file_writes_to_file(output_file_path):
    convert_file(INPUT_FILE_PATH, output_file_path)
    assert fc.cmp(INPUT_FILE_PATH, output_file_path) is True

''' Fixtures '''
@pytest.fixture
def output_file_path(tmp_path):
    return tmp_path / OUTPUT_FILE_NAME