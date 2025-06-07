import sys
from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtGui import QPixmap

class BlinkReminder(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setGeometry(100, 100, 300, 200)  # Fixed window size

        # Load and resize the image to fit the window
        pixmap = QPixmap("blink_reminder.png").scaled(300, 200, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        self.label = QLabel(self)
        self.label.setPixmap(pixmap)
        self.label.resize(pixmap.size())

        self.show_timer = QTimer(self)
        self.show_timer.timeout.connect(self.show_window)
        self.show_timer.start(300000)  # Every 5 minutes (300,000 ms)

        self.hide_timer = QTimer(self)
        self.hide_timer.timeout.connect(self.close)

    def show_window(self):
        self.show()
        self.hide_timer.start(3000)  # Hide after 3 seconds

app = QApplication(sys.argv)
window = BlinkReminder()
window.show_window()
app.exec_()  # Keep the application running