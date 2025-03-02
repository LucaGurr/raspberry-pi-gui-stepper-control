from PyQt5.QtWidgets import QMainWindow, QLabel, QVBoxLayout, QWidget, QPushButton, QComboBox, QLineEdit, QHBoxLayout, QScrollArea
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
        layout = QVBoxLayout()

        # Button zum Verbinden mit dem Raspberry Pi Zero
        self.connect_button = QPushButton("Connect to PI Zero")
        self.connect_button.clicked.connect(self.connect_to_pi)
        layout.addWidget(self.connect_button)

        # Debug-Informationen
        self.debug_info = QLabel("Debug Information")
        self.debug_info.setAlignment(Qt.AlignTop)
        layout.addWidget(self.debug_info)

        # Motorsteuerung
        self.motor_controls = []
        self.add_motor_control(layout)

        # Button zum Hinzufügen weiterer Motorsteuerungen
        self.add_motor_button = QPushButton("Add Motor Control")
        self.add_motor_button.clicked.connect(lambda: self.add_motor_control(layout))
        layout.addWidget(self.add_motor_button)

        # Layout dem zentralen Widget zuweisen
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

    def connect_to_pi(self):
        if self.serial_connection.open_connection():
            self.debug_info.setText("Connected to PI Zero")
        else:
            self.debug_info.setText("Failed to connect to PI Zero")

    def add_motor_control(self, layout):
        motor_control = MotorControl(self.serial_connection)
        self.motor_controls.append(motor_control)
        layout.addWidget(motor_control)