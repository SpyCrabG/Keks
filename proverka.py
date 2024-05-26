import os
import sys
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtCore import QCoreApplication, QUrl, QDir, Qt, QTimer
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QPushButton, QVBoxLayout
from PyQt5.QtMultimedia import QMediaContent, QMediaPlayer
from PyQt5 import uic, QtTest
import random
from playsound import playsound
import sys
from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QMessageBox

class TimerApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Пять минутный таймер")
        self.setGeometry(100, 100, 300, 100)

        self.label = QLabel(self)
        self.label.setGeometry(10, 10, 280, 30)

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_timer)
        self.timer.start(1000)  # Запускаем таймер с интервалом 1 секунда
        self.remaining_time = 2 # 5 минут в секундах

    def update_timer(self):
        if self.remaining_time > 0:
            minutes = self.remaining_time // 60
            seconds = self.remaining_time % 60
            self.label.setText(f"Осталось времени: {minutes:02}:{seconds:02}")
            self.remaining_time -= 1
        else:
            QMessageBox.critical(
                self,
                "Ошибка ",
                "Выделите элемент который хотите изменить",
                QMessageBox.Ok,
            )


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = TimerApp()
    window.show()
    sys.exit(app.exec_())
