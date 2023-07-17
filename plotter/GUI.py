import sys

from PySide2 import QtCore
from PySide2.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QGridLayout, QLabel, QLineEdit, QPushButton, QMessageBox, QApplication
from PySide2.QtCore import QTimer
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from Backend import *

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Function Plotter")
        self.setGeometry(100, 100, 800, 600)

        # Central Widget
        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)
        self.central_layout = QVBoxLayout(self.central_widget)

        # Input Widget
        self.input_widget = QWidget(self.central_widget)
        self.input_layout = QGridLayout(self.input_widget)

        self.function_label = QLabel("Enter Function:")
        self.function_input = QLineEdit()
        self.min_label = QLabel("Enter Min value:")
        self.min_input = QLineEdit()
        self.max_label = QLabel("Enter Max value:")
        self.max_input = QLineEdit()
        self.plot_button = QPushButton("Plot Funtion")

        self.input_layout.addWidget(self.function_label, 0, 0)
        self.input_layout.addWidget(self.function_input, 0, 1,1,3)
        self.input_layout.addWidget(self.min_label, 1, 0)
        self.input_layout.addWidget(self.min_input, 1, 1)
        self.input_layout.addWidget(self.max_label, 1, 2)
        self.input_layout.addWidget(self.max_input, 1, 3)
        self.input_layout.addWidget(self.plot_button, 2, 0, 1, 2)

        self.central_layout.addWidget(self.input_widget)

        # Plot Widget
        self.plot_widget = QWidget(self.central_widget)
        self.plot_layout = QVBoxLayout(self.plot_widget)

        self.figure = Figure()
        self.canvas = FigureCanvas(self.figure)
        self.plot_layout.addWidget(self.canvas)

        self.central_layout.addWidget(self.plot_widget)

        # Connect Plot Button
        self.plot_button.clicked.connect(self.plot_function)

        # Warning Message Box
        self.warning_message_box = None

        # Warning Timer
        self.warning_timer = QTimer(self)
        self.warning_timer.timeout.connect(self.hide_warning)

    def plot_function(self):
        function = self.function_input.text()
        min_value = self.min_input.text()
        max_value = self.max_input.text()

        # clear plot
        self.figure.clear()
        ax = self.figure.add_subplot(111)
        ax.clear()
        self.canvas.draw()

        if not function:
            self.display_message("Please enter a function.")
            return

        if not min_value or not max_value:
            self.display_message("Please enter minimum and maximum x values.")
            return

        flag, function = validate_expression(function)
        if not flag:
            self.display_message("Invalid function.")
            return

        try:
            min_value = float(min_value)
            max_value = float(max_value)
        except ValueError:
            self.display_message("Invalid x values.")
            return

        if min_value >= max_value:
            self.display_message("Minimum x value should be less than maximum x value.")
            return

        self.figure.clear()
        ax = self.figure.add_subplot(111)
        x_axis , y_axis = get_points(function,min_value,max_value)
        ax.plot(x_axis, y_axis)
        self.canvas.draw()

    def display_message(self, message):
        # Hide existing warning message box if any
        self.hide_warning()

        # Create the warning message box
        self.warning_message_box = QMessageBox(self)
        self.warning_message_box.setText(message)
        self.warning_message_box.setIcon(QMessageBox.Warning)
        self.warning_message_box.setWindowFlags(self.warning_message_box.windowFlags() | QtCore.Qt.WindowStaysOnTopHint)
        self.warning_message_box.show()

        self.warning_timer.start(5000)

    def hide_warning(self):
        if self.warning_message_box:
            self.warning_message_box.hide()
            self.warning_message_box = None




if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
