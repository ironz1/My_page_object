# Math Calculator
#
# Math Calculator is an MS Windows application performing some base mathematical operations.
# Numbers and operation name are provided in text form thought standard input. Calculations result will be returned via standard output.
#
# Usage
# HTTP GET 52.232.60.172:5000/param1/param2/paramN
# e.g. 52.232.60.172:5000/2/3/add
# http://52.232.60.172:5000/2/3/add


# will yield json containing execution result i.e.
# {"return_code": 0, "stdout": "5.0000", "stderr": "", "status": "STATUS_SUCCESS"}
#
# Operations
# Math Calculator supports following operations:
# DIV – Division. Takes 3 arguments; divident (number) , divisor (number), operation name(DIV)
# MUL – Multiplication. Takes 3 arguments; multiplicand (number), multiplier (number),operation name (MUL)
# POW – Exponentation. Takes 3 arguments: base (number), exponent(number), operation name (POW)
# SUB – Substraction. Takes 3 arguments: minuend (number), subtrahend (number), operation name (SUB)
# SUM – Summation. Takes from 2 to 6 arguments. Last argument is always operation name (SUM). Initial arguments are addendans (numbers)
# SQR – Square root. Takes 2 arguments; radicant (number), operation name (SQR)

import requests
import pytest


@pytest.mark.parametrize('input_numbers, expected_result',
                         [('6/2', '3.0000'),
                          ('10/2.49999', '4.0000'),
                          ('-10/2.49', '-4.0161'),
                          ('7/o', 'ERROR')])
def test_div(input_numbers, expected_result):
    w = requests.get(url=f'http://52.232.60.172:5000/{input_numbers}/div')
    response = w.json()
    assert response['stdout'] == expected_result
    assert response['status'] == 'STATUS_SUCCESS'
    assert response['return_code'] == 0
    assert response['stderr'] == ''


@pytest.mark.parametrize('input_numbers, expected_result',
                         [('2/2', '4.0000'),
                          ('-5/3', '-15.0000'),
                          ('2.5/10.5', '26.2500'),
                          ('x/3', 'ERROR'),
                          (pytest.param('5/n', 2, marks=pytest.mark.xfail))])
def test_mul(input_numbers, expected_result):
    request = requests.get(url=f'http://52.232.60.172:5000/{input_numbers}/mul')
    response = request.json()
    assert response['stdout'] == expected_result
    assert response['status'] == 'STATUS_SUCCESS'
    assert response['return_code'] == 0
    assert response['stderr'] == ''


@pytest.mark.parametrize('input_numbers, expected_result', [('2/2/2/2/2', '10.0000'),
                                                            ('-2/-2', '-4.0000'),
                                                            ('1.1250/1.1250', '2.2500'),
                                                            ('1/2/3/4/5/6', 'ERROR')])
def test_sum(input_numbers, expected_result):
    request = requests.get(url=f'http://52.232.60.172:5000/{input_numbers}/sum')
    response = request.json()
    assert response['return_code'] == 0
    assert response['stdout'] == expected_result
    assert response['stderr'] == ''
    assert response['status'] == 'STATUS_SUCCESS'
