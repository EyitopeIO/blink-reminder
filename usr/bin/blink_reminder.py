import sys
import random
from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow, QDesktopWidget
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtGui import QPixmap

class BlinkReminder(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setFixedSize(300, 200)

        pixmap = QPixmap("/usr/share/blink-reminder/blink_reminder.png").scaled(300, 200, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        self.label = QLabel(self)
        self.label.setPixmap(pixmap)
        self.label.resize(pixmap.size())

        self.show_timer = QTimer(self)
        self.show_timer.timeout.connect(self.show_window)
        self.show_timer.start(300000)  # 5 minutes

        self.hide_timer = QTimer(self)
        self.hide_timer.timeout.connect(self.hide)

    def show_window(self):
        screen_geometry = QDesktopWidget().availableGeometry()
        screen_width = screen_geometry.width()
        screen_height = screen_geometry.height()

        max_x = screen_width - self.width()
        max_y = screen_height - self.height()

        rand_x = random.randint(0, max_x)
        rand_y = random.randint(0, max_y)

        self.move(rand_x, rand_y)
        self.show()
        self.hide_timer.start(3000)  # Hide after 3 seconds

app = QApplication(sys.argv)
window = BlinkReminder()
window.show_window()
app.exec_()
