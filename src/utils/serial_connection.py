import serial
import time
import platform

class SerialConnection:
    def __init__(self, port='/dev/ttyUSB0', baudrate=9600, timeout=1):
        self.port = port
        self.baudrate = baudrate
        self.timeout = timeout
        self.serial = None

    def open_connection(self):
        if self.serial is None:
            try:
                self.serial = serial.Serial(self.port, self.baudrate, timeout=self.timeout)
                time.sleep(2)  # Wait for the connection to establish
                return True
            except serial.SerialException as e:
                print(f"Error opening serial port: {e}")
                return False
        return True

    def close_connection(self):
        if self.serial is not None:
            self.serial.close()
            self.serial = None

    def send_data(self, data):
        if self.serial is not None and self.serial.is_open:
            try:
                self.serial.write(data.encode())
                return True
            except serial.SerialException as e:
                print(f"Error sending data: {e}")
                return False
        return False

    def read_data(self):
        if self.serial is not None and self.serial.is_open:
            try:
                return self.serial.readline().decode().strip()
            except serial.SerialException as e:
                print(f"Error reading data: {e}")
                return None
        return None