# src/gui/main_window.py
from PyQt5.QtWidgets import QMainWindow, QLabel, QVBoxLayout, QWidget, QPushButton
from PyQt5.QtCore import Qt
from utils.serial_connection import SerialConnection
from gui.motor_control import MotorControl

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Main Window")
        self.setGeometry(100, 100, 800, 600)

        self.serial_connection = SerialConnection()

        # Haupt-Widget und Layout erstellen
        central_widget = QWidget()
        self.layout = QVBoxLayout()

        # Button zum Verbinden mit dem Raspberry Pi Zero
        self.connect_button = QPushButton("Connect to PI Zero")
        self.connect_button.clicked.connect(self.connect_to_pi)
        self.layout.addWidget(self.connect_button)

        # Debug-Informationen
        self.debug_info = QLabel("Debug Information")
        self.debug_info.setAlignment(Qt.AlignTop)
        self.layout.addWidget(self.debug_info)

        # Motorsteuerung
        self.motor_controls = []

        # Button zum Drehen aller Motoren
        self.rotate_all_button = QPushButton("Rotate All Motors")
        self.rotate_all_button.clicked.connect(self.rotate_all_motors)
        self.layout.addWidget(self.rotate_all_button)
        self.rotate_all_button.setVisible(False)  # Initially hidden

        # Button zum Hinzufügen weiterer Motorsteuerungen
        self.add_motor_button = QPushButton("Add Motor Control")
        self.add_motor_button.clicked.connect(self.add_motor_control)
        self.layout.addWidget(self.add_motor_button)

        # Layout dem zentralen Widget zuweisen
        central_widget.setLayout(self.layout)
        self.setCentralWidget(central_widget)

        # Initial motor control
        self.add_motor_control()

    def connect_to_pi(self):
        if self.serial_connection.open_connection():
            self.debug_info.setText("Connected to PI Zero")
        else:
            self.debug_info.setText("Failed to connect to PI Zero")

    def add_motor_control(self):
        motor_control = MotorControl(self.serial_connection)
        self.motor_controls.append(motor_control)
        self.layout.addWidget(motor_control)
        self.update_rotate_all_button_visibility()

    def rotate_all_motors(self):
        for motor_control in self.motor_controls:
            motor_control.rotate()  # Assuming MotorControl has a rotate method

    def update_rotate_all_button_visibility(self):
        self.rotate_all_button.setVisible(len(self.motor_controls) > 1)