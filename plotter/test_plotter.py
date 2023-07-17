import GUI
import pytest
from PySide2.QtCore import Qt
from pytestqt.qtbot import QtBot

# run this file from debugger not normal run

@pytest.fixture
def app(qtbot: QtBot):
    test_window = GUI.MainWindow()
    test_window.show()
    qtbot.addWidget(test_window)
    yield test_window

def test_invalid_function(app,qtbot):
    app.function_input.setText('x+*6')
    app.min_input.setText('0')
    app.max_input.setText('10')
    qtbot.mouseClick(app.plot_button, Qt.LeftButton)
    assert app.warning_message_box.text() == 'Invalid function.'
    app.close()

def test_empty_function(app,qtbot):
    app.function_input.setText('')
    app.min_input.setText('0')
    app.max_input.setText('10')
    qtbot.mouseClick(app.plot_button, Qt.LeftButton)
    assert app.warning_message_box.text() == "Please enter a function."

def test_empty_min_value(app,qtbot):
    app.function_input.setText('x*6')
    app.min_input.setText('')
    app.max_input.setText('10')
    qtbot.mouseClick(app.plot_button, Qt.LeftButton)
    assert app.warning_message_box.text() == "Please enter minimum and maximum x values."

def test_empty_max_value(app,qtbot):
    app.function_input.setText('x+6')
    app.min_input.setText('10')
    app.max_input.setText('')
    qtbot.mouseClick(app.plot_button, Qt.LeftButton)
    assert app.warning_message_box.text() == "Please enter minimum and maximum x values."

def test_invalid_min_value(app,qtbot):
    app.function_input.setText("x^2")
    app.min_input.setText("a")
    app.max_input.setText("10")
    qtbot.mouseClick(app.plot_button, Qt.LeftButton)
    assert app.warning_message_box.text() == "Invalid x values."
#
def test_invalid_max_value(app,qtbot):
    app.function_input.setText("x^2")
    app.min_input.setText("10")
    app.max_input.setText("a")
    qtbot.mouseClick(app.plot_button, Qt.LeftButton)
    assert app.warning_message_box.text() == "Invalid x values."

def test_min_greater_than_max(app,qtbot):
    app.function_input.setText("x+2")
    app.min_input.setText("10")
    app.max_input.setText("0")
    qtbot.mouseClick(app.plot_button, Qt.LeftButton)
    assert app.warning_message_box.text() == "Minimum x value should be less than maximum x value."

def test_division_by_zero(app,qtbot):
    app.function_input.setText("1/x")
    app.min_input.setText("0")
    app.max_input.setText("10")
    qtbot.mouseClick(app.plot_button, Qt.LeftButton)
    assert app.figure is not None

def test_invalid_function(app,qtbot):
    app.function_input.setText("x**")
    app.min_input.setText("0")
    app.max_input.setText("10")
    qtbot.mouseClick(app.plot_button, Qt.LeftButton)
    assert app.warning_message_box.text() == "Invalid function."

def test_invalid_function2(app,qtbot):
    app.function_input.setText("x/2 + ")
    app.min_input.setText("0")
    app.max_input.setText("10")
    qtbot.mouseClick(app.plot_button, Qt.LeftButton)
    assert app.warning_message_box.text() == "Invalid function."

def test_valid_function(app,qtbot):
    app.function_input.setText("x^2")
    app.min_input.setText("0")
    app.max_input.setText("10")
    qtbot.mouseClick(app.plot_button, Qt.LeftButton)
    assert app.figure is not None

