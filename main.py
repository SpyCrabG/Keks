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


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        # Инициализация плеера

        # Загрузка UI из файла
        self.ui = uic.loadUi("design\\proect_pizdi.ui", self)
        self.ui.btn2.clicked.connect(self.open_new_window)
        self.ui.btn1.clicked.connect(self.show_music)

        # Отображение окна
        self.show()

    def open_new_window(self):
        self.hide()
        self.win = Window()
        self.win.show()

    def show_music(self):
        music = MusicWindow()
        music.show()


class MusicWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.player = QMediaPlayer()

        self.ui = uic.loadUi("design\\music_menu.ui", self)
        self.setWindowTitle("Плеер")
        self.slider.valueChanged[int].connect(self.change_volume)
        self.slider.setValue(30)
        self.volume = self.slider.value()
        self.music_files = get_music_files()
        self.current_index = 0  # Текущий индекс трека
        self.show()

        # Настройка кнопок
        self.setup_buttons()

        # Отображение окна
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


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        # Загрузка UI из файла
        self.des = uic.loadUi("design\\window2.ui", self)
        self.setWindowTitle("Электронный тамада")
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
        self.btn2.clicked.connect(self.konkurs_menu)
        self.menu.clicked.connect(self.MainMenu1)
        self.ui.lbl.setText(
            "   Гости становятся в круг. \nКаждый по очереди напевает пару строк из \nпесен про праздники и всё, что с ними связано. \nТот, кто не может пропеть, вылетает из игры. \n Оставшейся тройке гостей, \nкоторые проявили себя по полной и\nвспомнили больше всех праздничных песен, \nвручаются призы."
        )

    def MainMenu1(self):
        self.hide()
        self.mainwindow1 = MainWindow()
        self.mainwindow1.show()

    def konkurs_menu(self):
        self.hide()
        self.konk = Window()
        self.konk.show()


class Konkurs2(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui1 = uic.loadUi("design\\window3.ui", self)
        self.setWindowTitle("Электронный тамада")
        self.btn2.clicked.connect(self.konkurs_menu)
        self.menu.clicked.connect(self.MainMenu1)
        self.lbl.setText(
            "    Этот конкурс подходит для свадеб и требует \n подручные средства.\n Новоиспечённые муж и жена получают доски, \n гвозди и молоток. \n Их задача — сколотить свой первый стул. \n Работа должна быть быстрой, слаженной и \n качественной. \n Гостям будет интересно наблюдать, как \nпроявляется пара в совместном деле по хозяйству. \n Примечание: Вместо досок и инструментов \n можно использовать бумагу и клей."
        )

    def MainMenu1(self):
        self.hide()
        self.mainwindow1 = MainWindow()
        self.mainwindow1.show()

    def konkurs_menu(self):
        self.hide()
        self.konk = Window()
        self.konk.show()


class Konkurs3(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui1 = uic.loadUi("design\\window3.ui", self)
        self.setWindowTitle("Электронный тамада")
        self.btn2.clicked.connect(self.konkurs_menu)
        self.menu.clicked.connect(self.MainMenu1)
        self.lbl.setText(
            "  Некоторые гости могут быть не знакомы друг \n с другом. \n Тамада проводит конкурс: первый выходит \n “машинист” — дружок, \n называет своё имя и увлечение жизни. \n Затем он “прицепляет” следующего гостя, \n который в свою очередь называет своё имя, \n увлечение по жизни. \n Процесс продолжается, пока весь “паровозик” не будет собран. \nТак все гости познакомятся и узнают \n друг друга ближе."
        )

    def MainMenu1(self):
        self.hide()
        self.mainwindow1 = MainWindow()
        self.mainwindow1.show()

    def konkurs_menu(self):
        self.hide()
        self.konk = Window()
        self.konk.show()


class Konkurs4(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui1 = uic.loadUi("design\\window3.ui", self)
        self.setWindowTitle("Электронный тамада")
        self.btn2.clicked.connect(self.konkurs_menu)
        self.menu.clicked.connect(self.MainMenu1)
        self.lbl.setText(
            "  Игроки выбирают случайным образом \n одного человека, который будет прятать \n определенный предмет. \n Спрятав его, все остальные игроки должны \nначать искать этот предмет до тех пор, \n пока не истечет отведенное время. Если \n предмет не нашли, то побеждает тот человек, \n который его прятал, а если наоборот, то \n побеждают те, кто его искал."
        )

    def MainMenu1(self):
        self.hide()
        self.mainwindow1 = MainWindow()
        self.mainwindow1.show()

    def konkurs_menu(self):
        self.hide()
        self.konk = Window()
        self.konk.show()


class Konkurs5(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui1 = uic.loadUi("design\\window3.ui", self)
        self.setWindowTitle("Электронный тамада")
        self.btn2.clicked.connect(self.konkurs_menu)
        self.menu.clicked.connect(self.MainMenu1)
        self.lbl.setText(
            "   Игроки должны открыть \n на своих телефонах фотографии, \n которые так или иначе связаны \n с участниками игры. \n Когда фотографии будут открыты, \n игрокам потребуется положить телефоны \n рядом с друг другом, \n тем самым образовывая фотоколлаж. "
        )

    def MainMenu1(self):
        self.hide()
        self.mainwindow1 = MainWindow()
        self.mainwindow1.show()

    def konkurs_menu(self):
        self.hide()
        self.konk = Window()
        self.konk.show()


class Konkurs6(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui1 = uic.loadUi("design\\window3.ui", self)
        self.setWindowTitle("Электронный тамада")
        self.btn2.clicked.connect(self.konkurs_menu)
        self.menu.clicked.connect(self.MainMenu1)
        self.lbl.setText(
            "  Каждый из участников конкурса должен \n  написать на листке причину, \n по которой он пришел на праздник, \n а после положить листок с причиной в банку. \n Кто-то из участников должен вызваться \n добровольцем и задать случайному человеку \n вопрос \n «Зачем он пришел на праздник?», а после \n достать из банки листок. \n Если человеку, которому задали вопрос, \n попался его собственный листок, \n то он побеждает."
        )

    def MainMenu1(self):
        self.hide()
        self.mainwindow1 = MainWindow()
        self.mainwindow1.show()

    def konkurs_menu(self):
        self.hide()
        self.konk = Window()
        self.konk.show()


class Konkurs7(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui1 = uic.loadUi("design\\window3.ui", self)
        self.setWindowTitle("Электронный тамада")
        self.btn2.clicked.connect(self.konkurs_menu)
        self.menu.clicked.connect(self.MainMenu1)
        self.lbl.setText(
            "  Выберите несколько известных песен \n и включите их для участников. \n  Попросите их угадать \n название песни и исполнителя, \n когда они услышат её отрывок."
        )

    def MainMenu1(self):
        self.hide()
        self.mainwindow1 = MainWindow()
        self.mainwindow1.show()

    def konkurs_menu(self):
        self.hide()
        self.konk = Window()
        self.konk.show()


class Konkurs8(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui1 = uic.loadUi("design\\window3.ui", self)
        self.setWindowTitle("Электронный тамада")
        self.btn2.clicked.connect(self.konkurs_menu)
        self.menu.clicked.connect(self.MainMenu1)
        self.lbl.setText(
            "  Разделите участников на пары\n и предложите им исполнить быстрый танец \n под разную музыку. \n Побеждает пара, которая лучше всех проявит \n свои танцевальные навыки \n и получит больше аплодисментов от зрителей."
        )

    def MainMenu1(self):
        self.hide()
        self.mainwindow1 = MainWindow()
        self.mainwindow1.show()

    def konkurs_menu(self):
        self.hide()
        self.konk = Window()
        self.konk.show()


class Konkurs9(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui1 = uic.loadUi("design\\window3.ui", self)
        self.setWindowTitle("Электронный тамада")
        self.menu.clicked.connect(self.MainMenu1)
        self.btn2.clicked.connect(self.konkurs_menu)
        spis1 = [
            "   Этот конкурс подходит для свадеб и требует \n подручные средства.\n Новоиспечённые муж и жена получают доски, \n гвозди и молоток. \n Их задача — сколотить свой первый стул. \n Работа должна быть быстрой, слаженной и \n качественной. \n Гостям будет интересно наблюдать, как \nпроявляется пара в совместном деле по хозяйству. \n Примечание: Вместо досок и инструментов \n можно использовать бумагу и клей."
        ]
        spis2 = [
            "   Гости становятся в круг. \nКаждый по очереди напевает пару строк из \nпесен про праздники и всё, что с ними связано. \nТот, кто не может пропеть, вылетает из игры. \n Оставшейся тройке гостей, \nкоторые проявили себя по полной и\nвспомнили больше всех праздничных песен, \nвручаются призы."
        ]
        spis3 = [
            "   Некоторые гости могут быть не знакомы друг \n с другом. \n Тамада проводит конкурс: первый выходит \n “машинист” — дружок, \n называет своё имя и увлечение жизни. \n Затем он “прицепляет” следующего гостя, \n который в свою очередь называет своё имя, \n увлечение по жизни. \n Процесс продолжается, пока весь “паровозик” не будет собран. \nТак все гости познакомятся и узнают \n друг друга ближе."
        ]
        spis4 = ["   Игроки выбирают случайным образом \n одного человека, который будет прятать \n определенный предмет. \n Спрятав его, все остальные игроки должны \nначать искать этот предмет до тех пор, \n пока не истечет отведенное время. Если \n предмет не нашли, то побеждает тот человек, \n который его прятал, а если наоборот, то \n побеждают те, кто его искал."]
        spis5 = ["   Игроки должны открыть \n на своих телефонах фотографии, \n которые так или иначе связаны \n с участниками игры. \n Когда фотографии будут открыты, \n игрокам потребуется положить телефоны \n рядом с друг другом, \n тем самым образовывая фотоколлаж. "]
        spis6 = ["   Каждый из участников конкурса должен \n  написать на листке причину, \n по которой он пришел на праздник, \n а после положить листок с причиной в банку. \n Кто-то из участников должен вызваться \n добровольцем и задать случайному человеку \n вопрос \n «Зачем он пришел на праздник?», а после \n достать из банки листок. \n Если человеку, которому задали вопрос, \n попался его собственный листок, \n то он побеждает."]
        spis7 = ["   Выберите несколько известных песен \n и включите их для участников. \n  Попросите их угадать \n название песни и исполнителя, \n когда они услышат её отрывок."]
        spis8 = ["  Разделите участников на пары\n и предложите им исполнить быстрый танец \n под разную музыку. \n Побеждает пара, которая лучше всех проявит \n свои танцевальные навыки \n и получит больше аплодисментов от зрителей."]
        self.lbl.setText(random.choice(spis1 + spis2 + spis3 + spis4 + spis5 + spis6 + spis7 + spis8))

    def MainMenu1(self):
        self.hide()
        self.mainwindow1 = MainWindow()
        self.mainwindow1.show()

    def konkurs_menu(self):
        self.hide()
        self.konk = Window()
        self.konk.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window2 = MusicWindow()
    app.exec_()
