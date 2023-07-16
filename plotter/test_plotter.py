from GUI import *
import pytest
from pytestqt.qt_compat import qt_api


def test_empty_function(qtbot):
    window = MainWindow()
    window.function_input.setText("")
    window.min_input.setText("0")
    window.max_input.setText("10")
    window.plot_function()
    assert window.statusBar().currentMessage() == "Please enter a function."

def test_empty_min_value(qtbot):
    window = MainWindow()
    window.function_input.setText("x^2")
    window.min_input.setText("")
    window.max_input.setText("10")
    window.plot_function()
    assert window.statusBar().currentMessage() == "Please enter minimum and maximum x values."

def test_empty_max_value(qtbot):
    window = MainWindow()
    window.function_input.setText("x^2")
    window.min_input.setText("0")
    window.max_input.setText("")
    window.plot_function()
    assert window.statusBar().currentMessage() == "Please enter minimum and maximum x values."

def test_invalid_min_value(qtbot):
    window = MainWindow()
    window.function_input.setText("x^2")
    window.min_input.setText("a")
    window.max_input.setText("10")
    window.plot_function()
    assert window.statusBar().currentMessage() == "Invalid x values."

def test_invalid_max_value(qtbot):
    window = MainWindow()
    window.function_input.setText("x*2")
    window.min_input.setText("0")
    window.max_input.setText("a")
    window.plot_function()
    assert window.statusBar().currentMessage() == "Invalid x values."

def test_min_greater_than_max(qtbot):
    window = MainWindow()
    window.function_input.setText("x+2")
    window.min_input.setText("10")
    window.max_input.setText("0")
    window.plot_function()
    assert window.statusBar().currentMessage() == "Minimum x value should be less than maximum x value."

def test_division_by_zero(qtbot):
    window = MainWindow()
    window.function_input.setText("1/x")
    window.min_input.setText("0")
    window.max_input.setText("10")
    window.plot_function()
    assert window.statusBar().currentMessage() == ""

def test_invalid_function(qtbot):
    window = MainWindow()
    window.function_input.setText("x**")
    window.min_input.setText("0")
    window.max_input.setText("10")
    window.plot_function()
    assert window.statusBar().currentMessage() == "Invalid function."

def test_invalid_function2(qtbot):
    window = MainWindow()
    window.function_input.setText("x/2 + ")
    window.min_input.setText("0")
    window.max_input.setText("10")
    window.plot_function()
    assert window.statusBar().currentMessage() == "Invalid function."

def test_valid_function(qtbot):
    window = MainWindow()
    window.function_input.setText("x^2")
    window.min_input.setText("0")
    window.max_input.setText("10")
    window.plot_function()
    assert window.statusBar().currentMessage() == ""






