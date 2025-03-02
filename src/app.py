from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
import sys
import platform
from gui.main_window import MainWindow
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

def create_app():
    if platform.system() == "Linux":
        from platform.linux import LinuxPlatform as CurrentPlatform
    elif platform.system() == "Windows":
        from platform.windows import WindowsPlatform as CurrentPlatform
    else:
        raise EnvironmentError("Unsupported operating system")

    return CurrentPlatform()


class App:
    def __init__(self):
        self.app = QApplication(sys.argv)
        self.main_window = MainWindow()

    def run(self):
        self.main_window.show()
        sys.exit(self.app.exec_())


if __name__ == "__main__":
    app = App()
    app.run()