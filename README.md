# FunctionPlotter
## Description
This is a Python GUI program that allows the user to plot an arbitrary function of `x`. The user can input a function in the form of a mathematical expression with `x`, as well as specify the minimum and maximum values of x for the plot. The program supports basic arithmetic operators (+, -, *, /) and the power operator (^). The plot is displayed using Matplotlib, and the figure is embedded in the PySide2 application.

## Requirements
To run the program, you need the following:
- Python 3.x
- PySide2
- Matplotlib

You can install the required packages using the following command:
```
pip install PySide2 matplotlib
```
## Usage
To run the program, execute the following command:
```
python function_plotter.py
```
The program's GUI window will open, allowing you to enter the function and the range of x values. Press the "Plot Function" button to display the plot.
## Implementation
The program is implemented in Python using the PySide2 library for the graphical user interface and Matplotlib for plotting. The main GUI window is created using the `QWidget` class, and the plot is displayed using `FigureCanvasQTAgg`. The function validation and plotting are done using separate functions.

The main components of the code are:

1. The MainWindow class: This class represents the main GUI window of the program. It contains input fields for entering the function and range of x values, a button to trigger the plot, and a plot area to display the function plot.

2. Error Handling: The program performs input validation and displays warning messages to the user if there are any issues with the input.

3. Integration with Matplotlib: The program utilizes Matplotlib to plot the user-entered function.

4. validate_expression function: This function is responsible for validating the user-entered function. It checks for invalid characters and ensures that the expression is well-formed. remove all white-spaces from expression and add * if number is written behind x directly eg. `2x => 2*x`. check also for correct parenthesis `()`

5. get_points function: This function calculates the (x, y) points required for plotting the function over the specified range of x values.

## Automated Tests
The code includes automated tests using `pytest` and `pytest-qt`. These tests cover end-to-end testing for some of the program's main features, including function validation, plotting, and handling of invalid inputs. The test codes are included in the repository for verification.
To run automated tests:
- install the required packages using the following command:
```
pip install pytest pytest-qt
```
- execute the following command:
```
pytest
```
## snapshots 
- Correct Inputs
    - ![test case 1](assets\1.png) 
    - ![test case 2](assets\2.png) 
    - ![test case 3](assets\3.png) 
    - ![test case 4](assets\9.png) 
    - ![test case 5](assets\10.png) 

- Wrong Inputs
    - ![test case 1](assets\4.png) 
    - ![test case 2](assets\5.png) 
    - ![test case 3](assets\6.png) 
    - ![test case 4](assets\7.png) 
    - ![test case 5](assets\8.png)
    - ![test case 6](assets\11.png) 

## License
Feel free to use and modify it according to your needs.
Happy plotting!
