import os
import sys
from PyQt5.QtCore import QCoreApplication, QUrl, QDir, Qt, QTimer
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QPushButton, QVBoxLayout
from PyQt5.QtMultimedia import QMediaContent, QMediaPlayer
from PyQt5 import uic, QtTest
import random

project_path = os.path.abspath(".")  # Путь к папке проекта
music_dir = os.path.join(project_path, "music")  # Путь к папке с музыкой
ui_file = os.path.join(project_path, "design", "project_pizdi.ui")  # Путь к UI-файлу


def get_music_files():
    music_files = [f for f in os.listdir(music_dir) if f.endswith(".mp3")]
    music_files.sort()  # Сортировка по имени (по номеру трека)
    return music_files


def media(t):
    t.player = QMediaPlayer()


class MusicWindow(QWidget):
    def __init__(self):
        super().__init__()

        self = uic.loadUi("design\\music_menu", self)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        # Инициализация плеера
        media(self)

        # Загрузка UI из файла
        self.ui = uic.loadUi("design\\proect_pizdi.ui", self)
        self.slider.valueChanged[int].connect(self.change_volume)
        self.slider.setValue(30)
        self.volume = self.slider.value()

        # Загрузка списка файлов с музыкой
        self.music_files = get_music_files()
        self.current_index = 0  # Текущий индекс трека

        # Настройка кнопок
        self.setup_buttons()

        # Отображение окна
        self.show()
        self.player.setVolume(self.volume)

    def change_volume(self, value):
        self.player.setVolume(value)

    def setup_buttons(self):
        # Кнопка "Назад"
        self.ui.btn1.clicked.connect(self.prev_track)

        # Кнопка "Пауза/Воспроизвести"
        self.ui.btn2.clicked.connect(self.play_pause)

        # Кнопка "Вперед"
        self.ui.btn3.clicked.connect(self.next_track)

        # Кнопка "Открыть новое окно"
        self.ui.btn4.clicked.connect(self.open_new_window)

    def prev_track(self):
        self.current_index -= 1
        if self.current_index < 0:
            self.current_index = len(self.music_files) - 1
        self.play_music()

    def play_pause(self):
        if self.player.state() == QMediaPlayer.PlayingState:
            self.player.pause()
            self.ui.btn2.setText(">")
            self.ui.btn3.setEnabled(False)
            self.ui.btn1.setEnabled(False)
        else:
            self.player.play()
            self.ui.btn2.setText("||")
            self.ui.btn3.setEnabled(True)
            self.ui.btn1.setEnabled(True)

    def next_track(self):
        self.current_index += 1
        if self.current_index >= len(self.music_files):
            self.current_index = 0
        self.play_music()

    def play_music(self):
        music_file = os.path.join(music_dir, self.music_files[self.current_index])
        media_content = QMediaContent(QUrl.fromLocalFile(music_file))
        self.player.setMedia(media_content)
        self.player.play()

    def open_new_window(self):
        self.hide()
        self.win = Window()
        self.win.show()


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        # Загрузка UI из файла
        self.des = uic.loadUi("design\\window2.ui", self)
        self.setWindowTitle("Электронный тамада")
        media(self)
        self.menu.clicked.connect(self.MainMenu)
        self.btn1.clicked.connect(self.KonkursMenu1)
        self.btn2.clicked.connect(self.KonkursMenu2)
        self.btn3.clicked.connect(self.KonkursMenu3)
        self.btn4.clicked.connect(self.KonkursMenu4)
        self.btn5.clicked.connect(self.KonkursMenu5)
        self.btn6.clicked.connect(self.KonkursMenu6)
        self.btn7.clicked.connect(self.KonkursMenu7)
        self.btn8.clicked.connect(self.KonkursMenu8)
        self.btn9.clicked.connect(self.KonkursMenu9)

    def MainMenu(self):
        media(self)
        self.player.stop()
        self.hide()
        self.mainwindow = MainWindow()
        self.mainwindow.show()

    def KonkursMenu1(self):
        self.hide()
        self.konkurswindow = Konkurs1()
        self.konkurswindow.show()

    def KonkursMenu2(self):
        self.hide()
        self.konkurswindow = Konkurs2()
        self.konkurswindow.show()

    def KonkursMenu3(self):
        self.hide()
        self.konkurswindow = Konkurs3()
        self.konkurswindow.show()

    def KonkursMenu4(self):
        self.hide()
        self.konkurswindow = Konkurs4()
        self.konkurswindow.show()

    def KonkursMenu5(self):
        self.hide()
        self.konkurswindow = Konkurs5()
        self.konkurswindow.show()

    def KonkursMenu6(self):
        self.hide()
        self.konkurswindow = Konkurs6()
        self.konkurswindow.show()

    def KonkursMenu7(self):
        self.hide()
        self.konkurswindow = Konkurs7()
        self.konkurswindow.show()

    def KonkursMenu8(self):
        self.hide()
        self.konkurswindow = Konkurs8()
        self.konkurswindow.show()

    def KonkursMenu9(self):
        self.hide()
        self.konkurswindow = Konkurs9()
        self.konkurswindow.show()


class Konkurs1(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = uic.loadUi("design\\window3.ui", self)
        self.setWindowTitle("Электронный тамада")
        self.menu.clicked.connect(self.MainMenu1)
        self.ui.lbl.setText(
            "   Гости становятся в круг. \nКаждый по очереди напевает пару строк из \nпесен про праздники и всё, что с ними связано. \nТот, кто не может пропеть, вылетает из игры. \n Оставшейся тройке гостей, \nкоторые проявили себя по полной и\nвспомнили больше всех праздничных песен, \nвручаются призы."
        )

    def MainMenu1(self):
        self.hide()
        self.mainwindow1 = MainWindow()
        self.mainwindow1.show()


class Konkurs2(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui1 = uic.loadUi("design\\window3.ui", self)
        self.setWindowTitle("Электронный тамада")
        self.menu.clicked.connect(self.MainMenu1)
        self.lbl.setText(
            "    Этот конкурс подходит для свадеб и требует \n подручные средства.\n Новоиспечённые муж и жена получают доски, \n гвозди и молоток. \n Их задача — сколотить свой первый стул. \n Работа должна быть быстрой, слаженной и \n качественной. \n Гостям будет интересно наблюдать, как \nпроявляется пара в совместном деле по хозяйству. \n Примечание: Вместо досок и инструментов \n можно использовать бумагу и клей."
        )

    def MainMenu1(self):
        self.hide()
        self.mainwindow1 = MainWindow()
        self.mainwindow1.show()


class Konkurs3(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui1 = uic.loadUi("design\\window3.ui", self)
        self.setWindowTitle("Электронный тамада")
        self.menu.clicked.connect(self.MainMenu1)
        self.lbl.setText("1")

    def MainMenu1(self):
        self.hide()
        self.mainwindow1 = MainWindow()
        self.mainwindow1.show()


class Konkurs4(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui1 = uic.loadUi("design\\window3.ui", self)
        self.setWindowTitle("Электронный тамада")
        self.menu.clicked.connect(self.MainMenu1)
        self.lbl.setText("1")

    def MainMenu1(self):
        self.hide()
        self.mainwindow1 = MainWindow()
        self.mainwindow1.show()


class Konkurs5(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui1 = uic.loadUi("design\\window3.ui", self)
        self.setWindowTitle("Электронный тамада")
        self.menu.clicked.connect(self.MainMenu1)
        self.lbl.setText("1")

    def MainMenu1(self):
        self.hide()
        self.mainwindow1 = MainWindow()
        self.mainwindow1.show()


class Konkurs6(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui1 = uic.loadUi("design\\window3.ui", self)
        self.setWindowTitle("Электронный тамада")
        self.menu.clicked.connect(self.MainMenu1)
        self.lbl.setText("1")

    def MainMenu1(self):
        self.hide()
        self.mainwindow1 = MainWindow()
        self.mainwindow1.show()


class Konkurs7(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui1 = uic.loadUi("design\\window3.ui", self)
        self.setWindowTitle("Электронный тамада")
        self.menu.clicked.connect(self.MainMenu1)
        self.lbl.setText("1")

    def MainMenu1(self):
        self.hide()
        self.mainwindow1 = MainWindow()
        self.mainwindow1.show()


class Konkurs8(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui1 = uic.loadUi("design\\window3.ui", self)
        self.setWindowTitle("Электронный тамада")
        self.menu.clicked.connect(self.MainMenu1)
        self.lbl.setText("1")

    def MainMenu1(self):
        self.hide()
        self.mainwindow1 = MainWindow()
        self.mainwindow1.show()


class Konkurs9(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui1 = uic.loadUi("design\\window3.ui", self)
        self.setWindowTitle("Электронный тамада")
        self.menu.clicked.connect(self.MainMenu1)
        self.lbl.setText("1")
        self.lbl2.display(1)

    def MainMenu1(self):
        self.hide()
        self.mainwindow1 = MainWindow()
        self.mainwindow1.show()

    def timer(self):
        lbl_timer = self.lbl2.value()
        if lbl_timer > 0:
            self.lbl2.display()
            QTimer().singleShot(1000, self.timer)
        else:
            # Значение дисплея стало 0
            # Включаем элементы интерфейса обратно
            self.toggle_btns()
            # Устанавливаем на дисплей выбранную на слайдере настройку
            self.lbl2.display(self.slider.value())


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    app.exec_()
