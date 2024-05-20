import sys
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtWidgets import QWidget, QApplication, \
    QLCDNumber, QSlider, QVBoxLayout, QHBoxLayout, QPushButton

class MusicWindow(QWidget):
    def __init__(self):
        super().__init__()
class MainWindow(QWidget):

    def __init__(self):
        super().__init__()

        self.lcd = QLCDNumber(self)
        # Устанавливаем значение по умолчанию на дисплей

        self.slider = QSlider(Qt.Horizontal, self)
        # Устанавливаем минимальное и максимальное значение
        self.slider.setMinimum(1)
        self.slider.setMaximum(90)
        self.slider.valueChanged.connect(self.lcd.display)

        self.start_btn = QPushButton('Start', self)
        self.start_btn.clicked.connect(self.start_btn_clicked)
        self.toggle_btns()

        hbox = QHBoxLayout()
        hbox.addWidget(self.slider)
        hbox.addWidget(self.start_btn)

        vbox = QVBoxLayout()
        vbox.addWidget(self.lcd)
        vbox.addLayout(hbox)

        self.setLayout(vbox)

        self.setWindowTitle('Timer PyQt5')
        self.resize(400, 300)

    def toggle_btns(self, value=True):
        self.slider.setEnabled(value)
        self.start_btn.setEnabled(value)

    def start_btn_clicked(self):
        # Отключаем слайдер и кнопку старта
        self.toggle_btns(False)
        # запускаем отсчет
        self.tick_timer()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())