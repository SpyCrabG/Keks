import os
import sys
from PyQt5.QtCore import QCoreApplication, QUrl, QDir, Qt
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QPushButton, QVBoxLayout
from PyQt5.QtMultimedia import QMediaContent, QMediaPlayer
from PyQt5 import uic
import random

project_path = os.path.abspath(".")  # Путь к папке проекта
music_dir = os.path.join(project_path, "music")  # Путь к папке с музыкой
ui_file = os.path.join(project_path, "design", "project_pizdi.ui")  # Путь к UI-файлу


def get_music_files():
    music_files = [f for f in os.listdir(music_dir) if f.endswith(".mp3")]
    music_files.sort()  # Сортировка по имени (по номеру трека)
    return music_files


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        # Инициализация плеера
        self.player = QMediaPlayer()

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
        rng = range(1, 8)
        r = random.choice(rng)
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
        self.hide()
        self.mainwindow = MainWindow()
        self.mainwindow.show()

    def KonkursMenu1(self):
        self.hide()
        self.konkurswindow = Konkurs + "1" + ()
        self.konkurswindow.show()
        self.ui.lbl.setText("Гости становятся в круг. \nКаждый по очереди напевает пару строк из песен про праздники и всё, что с ними связано. \nТот, кто не может пропеть, вылетает из игры. \n Оставшейся тройке гостей, \nкоторые проявили себя по полной и вспомнили больше всех праздничных песен, \nвручаются призы.")

    def KonkursMenu2(self):
        self.hide()
        self.konkurswindow = Konkurs()
        self.konkurswindow.show()

    def KonkursMenu3(self):
        self.hide()
        self.konkurswindow = Konkurs()
        self.konkurswindow.show()

    def KonkursMenu4(self):
        self.hide()
        self.konkurswindow = Konkurs()
        self.konkurswindow.show()

    def KonkursMenu5(self):
        self.hide()
        self.konkurswindow = Konkurs()
        self.konkurswindow.show()

    def KonkursMenu6(self):
        self.hide()
        self.konkurswindow = Konkurs()
        self.konkurswindow.show()

    def KonkursMenu7(self):
        self.hide()
        self.konkurswindow = Konkurs()
        self.konkurswindow.show()

    def KonkursMenu8(self):
        self.hide()
        self.konkurswindow = Konkurs()
        self.konkurswindow.show()

    def KonkursMenu9(self):
        self.hide()
        text1 = "Гости становятся в круг. \nКаждый по очереди напевает пару строк из песен про праздники и всё, что с ними связано. \nТот, кто не может пропеть, вылетает из игры. \n Оставшейся тройке гостей, \nкоторые проявили себя по полной и вспомнили больше всех праздничных песен, \nвручаются призы."
        #text2 =






        self.konkurswindow = Konkurs()
        self.konkurswindow.show()


class Konkurs(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui1 = uic.loadUi("design\\window3.ui", self)
        self.setWindowTitle("Электронный тамада")
        self.menu.clicked.connect(self.MainMenu1)

    def MainMenu1(self):
        self.hide()
        self.mainwindow1 = MainWindow()
        self.mainwindow1.show()
class Konkurs1(QMainWindow):
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


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    app.exec_()
