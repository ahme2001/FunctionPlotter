from Backend import *

def test_validation_has_2_operators_false():
    flag , expression = validate_expression("2*x+3-*5")
    assert flag == False
    assert expression == "2*x+3-*5"

def test_validation_has_2_operators_true():
    flag , expression = validate_expression("2*x+3*-5")
    assert flag == True
    assert expression == "2*x+3*-5"

def test_validation_has_parentheses_true():
    flag , expression = validate_expression("2*x+(3*-5)")
    assert flag == True
    assert expression == "2*x+(3*-5)"

def test_validation_has_parentheses2_true():
    flag , expression = validate_expression("2(x)+(3*-5)")
    assert flag == True
    assert expression == "2*(x)+(3*-5)"

def test_validation_has_parentheses_false():
    flag , expression = validate_expression("2*x)+(3*-5)")
    assert flag == False
    assert expression == "2*x)+(3*-5)"

def test_validation_has_parentheses2_false():
    flag , expression = validate_expression("2*x+(3*-5)(")
    assert flag == False
    assert expression == "2*x+(3*-5)("

def test_validation_convert_power_sign():
    flag , expression = validate_expression("2^x+3-5")
    assert flag == True
    assert expression == "2**x+3-5"

def test_validation_wrong_function():
    flag , expression = validate_expression("10**x-9")
    assert flag == False
    assert expression == "10**x-9"

def test_validation_with_variable_not_x():
    flag , expression = validate_expression("y+5-9/y")
    assert flag == False
    assert expression == "y+5-9/y"

def test_validation_convert_to_negative():
    flag , expression = validate_expression("x+-5")
    assert flag == True
    assert expression == "x-5"

def test_validation_repeated_x():
    flag , expression = validate_expression("10*xx-9")
    assert flag == True
    assert expression == "10*x*x-9"

def test_linear_function():
    func = 'x + 2'
    x_axis, y_axis = get_points(func, 0, 10)
    assert len(x_axis) == len(y_axis) == 100
    assert x_axis[0] == 0
    assert y_axis[0] == 2
    assert x_axis[-1] == 9.9
    assert y_axis[-1] == 11.9

def test_float_input_function():
    func = 'x*2'
    x_axis, y_axis = get_points(func, -10.5, 2.6)
    assert len(x_axis) == len(y_axis) == 100
    assert x_axis[0] == -10.5
    assert y_axis[0] == -21

def test_division_by_zero():
    func = '1 / x'
    x_axis, y_axis = get_points(func, -10, 10)
    assert len(x_axis) == len(y_axis) == 100
    assert y_axis[50] == float('inf')

def test_min_equals_max():
    func = 'x'
    x_axis, y_axis = get_points(func, 5, 5)
    assert len(x_axis) == len(y_axis) == 100
    assert all(y == 5 for y in y_axis)
