import os
import sys
from PyQt5.QtCore import QCoreApplication, QUrl, QDir, Qt, QTimer
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QPushButton, QVBoxLayout, QMessageBox
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
        self.setFixedSize(730, 460)

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
        self.setFixedSize(328, 172)
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
        self.setFixedSize(800, 500)
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
        self.player = QMediaPlayer()
        super().__init__()
        self.ui = uic.loadUi("design\\window3.ui", self)
        self.setWindowTitle("Электронный тамада")
        self.setFixedSize(800, 500)
        self.timer = QTimer(self)
        self.btn2.clicked.connect(self.konkurs_menu)
        self.menu.clicked.connect(self.MainMenu1)
        self.btn1.clicked.connect(self.timer_pause)
        self.ui.lbl.setText(
            "   Гости становятся в круг. \nКаждый по очереди напевает пару строк из \nпесен про праздники и всё, что с ними связано. \nТот, кто не может пропеть, вылетает из игры. \n Оставшейся тройке гостей, \nкоторые проявили себя по полной и\nвспомнили больше всех праздничных песен, \nвручаются призы."
        )
        self.player.setMedia(QMediaContent(QUrl.fromLocalFile("voice\\2.mp3")))
        self.player.play()
        self.timer.timeout.connect(self.update_timer)
        self.timer.start(1000)  # Запускаем таймер с интервалом 1 секунда
        self.remaining_time = 5 * 60  # 5 минут в секундах

    def update_timer(self):
        if self.remaining_time > 0:
            minutes = self.remaining_time // 60
            seconds = self.remaining_time % 60
            self.lbl2.setText(f"{minutes:2}:{seconds:02}")
            self.remaining_time -= 1
        else:
            self.label.setText("Время вышло!")
    def timer_pause(self):
        self.timer.stop()

    def MainMenu1(self):
        self.player.stop()
        self.hide()
        self.mainwindow1 = MainWindow()
        self.mainwindow1.show()

    def konkurs_menu(self):
        self.player.stop()
        self.hide()
        self.konk = Window()
        self.konk.show()


class Konkurs2(QMainWindow):
    def __init__(self):
        super().__init__()
        self.player = QMediaPlayer()
        self.ui1 = uic.loadUi("design\\window3.ui", self)
        self.setWindowTitle("Электронный тамада")
        self.timer = QTimer(self)
        self.setFixedSize(800, 500)
        self.btn2.clicked.connect(self.konkurs_menu)
        self.menu.clicked.connect(self.MainMenu1)
        self.btn1.clicked.connect(self.timer_pause)
        self.lbl.setText(
            "    Этот конкурс подходит для свадеб и требует \n подручные средства.\n Новоиспечённые муж и жена получают доски, \n гвозди и молоток. \n Их задача — сколотить свой первый стул. \n Работа должна быть быстрой, слаженной и \n качественной. \n Гостям будет интересно наблюдать, как \nпроявляется пара в совместном деле по хозяйству. \n Примечание: Вместо досок и инструментов \n можно использовать бумагу и клей."
        )
        self.player.setMedia(QMediaContent(QUrl.fromLocalFile("voice\\1.mp3")))
        self.player.play()
        self.timer.timeout.connect(self.update_timer)
        self.timer.start(1000)  # Запускаем таймер с интервалом 1 секунда
        self.remaining_time = 5 * 60  # 5 минут в секундах

    def update_timer(self):
        if self.remaining_time > 0:
            minutes = self.remaining_time // 60
            seconds = self.remaining_time % 60
            self.lbl2.setText(f"{minutes:2}:{seconds:02}")
            self.remaining_time -= 1
        else:
            self.label.setText("Время вышло!")
    def timer_pause(self):
        self.timer.stop()

    def MainMenu1(self):
        self.player.stop()
        self.hide()
        self.mainwindow1 = MainWindow()
        self.mainwindow1.show()

    def konkurs_menu(self):
        self.player.stop()
        self.hide()
        self.konk = Window()
        self.konk.show()


class Konkurs3(QMainWindow):
    def __init__(self):
        super().__init__()
        self.player = QMediaPlayer()
        self.ui1 = uic.loadUi("design\\window3.ui", self)
        self.setWindowTitle("Электронный тамада")
        self.timer = QTimer(self)
        self.setFixedSize(800, 500)
        self.btn2.clicked.connect(self.konkurs_menu)
        self.menu.clicked.connect(self.MainMenu1)
        self.btn1.clicked.connect(self.timer_pause)
        self.lbl.setText(
            "  Некоторые гости могут быть не знакомы друг \n с другом. Тамада проводит конкурс: первый выходит \n “машинист” — дружок, \n называет своё имя и увлечение жизни. \n Затем он “прицепляет” следующего гостя, \n который в свою очередь называет своё имя, \n увлечение по жизни. \n Процесс продолжается, пока весь “паровозик” не будет собран. \nТак все гости познакомятся и узнают \n друг друга ближе."
        )
        self.player.setMedia(QMediaContent(QUrl.fromLocalFile("voice\\3.mp3")))
        self.player.play()
        self.timer.timeout.connect(self.update_timer)
        self.timer.start(1000)  # Запускаем таймер с интервалом 1 секунда
        self.remaining_time = 5 * 60  # 5 минут в секундах

    def update_timer(self):
        if self.remaining_time > 0:
            minutes = self.remaining_time // 60
            seconds = self.remaining_time % 60
            self.lbl2.setText(f"{minutes:2}:{seconds:02}")
            self.remaining_time -= 1
        else:
            self.label.setText("Время вышло!")
    def timer_pause(self):
        self.timer.stop()

    def MainMenu1(self):
        self.player.stop()
        self.hide()
        self.mainwindow1 = MainWindow()
        self.mainwindow1.show()

    def konkurs_menu(self):
        self.player.stop()
        self.hide()
        self.konk = Window()
        self.konk.show()


class Konkurs4(QMainWindow):
    def __init__(self):
        super().__init__()
        self.player = QMediaPlayer()
        self.ui1 = uic.loadUi("design\\window3.ui", self)
        self.setWindowTitle("Электронный тамада")
        self.timer = QTimer(self)
        self.setFixedSize(800, 500)
        self.btn2.clicked.connect(self.konkurs_menu)
        self.menu.clicked.connect(self.MainMenu1)
        self.btn1.clicked.connect(self.timer_pause)
        self.lbl.setText(
            "  Игроки выбирают случайным образом \n одного человека, который будет прятать \n определенный предмет. \n Спрятав его, все остальные игроки должны \nначать искать этот предмет до тех пор, \n пока не истечет отведенное время. Если \n предмет не нашли, то побеждает тот человек, \n который его прятал, а если наоборот, то \n побеждают те, кто его искал."
        )
        self.player.setMedia(QMediaContent(QUrl.fromLocalFile("voice\\4.mp3")))
        self.player.play()
        self.timer.timeout.connect(self.update_timer)
        self.timer.start(1000)  # Запускаем таймер с интервалом 1 секунда
        self.remaining_time = 5 * 60  # 5 минут в секундах

    def update_timer(self):
        if self.remaining_time > 0:
            minutes = self.remaining_time // 60
            seconds = self.remaining_time % 60
            self.lbl2.setText(f"{minutes:2}:{seconds:02}")
            self.remaining_time -= 1
        else:
            self.label.setText("Время вышло!")
    def timer_pause(self):
        self.timer.stop()

    def MainMenu1(self):
        self.player.stop()
        self.hide()
        self.mainwindow1 = MainWindow()
        self.mainwindow1.show()

    def konkurs_menu(self):
        self.player.stop()
        self.hide()
        self.konk = Window()
        self.konk.show()


class Konkurs5(QMainWindow):
    def __init__(self):
        super().__init__()
        self.player = QMediaPlayer()
        self.ui1 = uic.loadUi("design\\window3.ui", self)
        self.setWindowTitle("Электронный тамада")
        self.timer = QTimer(self)
        self.setFixedSize(800, 500)
        self.btn2.clicked.connect(self.konkurs_menu)
        self.menu.clicked.connect(self.MainMenu1)
        self.btn1.clicked.connect(self.timer_pause)
        self.lbl.setText(
            "   Игроки должны открыть \n на своих телефонах фотографии, \n которые так или иначе связаны \n с участниками игры. \n Когда фотографии будут открыты, \n игрокам потребуется положить телефоны \n рядом с друг другом, \n тем самым образовывая фотоколлаж. "
        )
        self.player.setMedia(QMediaContent(QUrl.fromLocalFile("voice\\5.mp3")))
        self.player.play()
        self.timer.timeout.connect(self.update_timer)
        self.timer.start(1000)  # Запускаем таймер с интервалом 1 секунда
        self.remaining_time = 5 * 60  # 5 минут в секундах

    def update_timer(self):
        if self.remaining_time > 0:
            minutes = self.remaining_time // 60
            seconds = self.remaining_time % 60
            self.lbl2.setText(f"{minutes:2}:{seconds:02}")
            self.remaining_time -= 1
        else:
            self.label.setText("Время вышло!")
    def timer_pause(self):
        self.timer.stop()

    def MainMenu1(self):
        self.player.stop()
        self.hide()
        self.mainwindow1 = MainWindow()
        self.mainwindow1.show()

    def konkurs_menu(self):
        self.player.stop()
        self.hide()
        self.konk = Window()
        self.konk.show()


class Konkurs6(QMainWindow):
    def __init__(self):
        super().__init__()
        self.player = QMediaPlayer()
        self.ui1 = uic.loadUi("design\\window3.ui", self)
        self.setWindowTitle("Электронный тамада")
        self.timer = QTimer(self)
        self.setFixedSize(800, 500)
        self.btn2.clicked.connect(self.konkurs_menu)
        self.menu.clicked.connect(self.MainMenu1)
        self.btn1.clicked.connect(self.timer_pause)
        self.lbl.setText(
            "  Каждый из участников конкурса должен \n  написать на листке причину, \n по которой он пришел на праздник, \n а после положить листок с причиной в банку. \n Кто-то из участников должен вызваться \n добровольцем и задать случайному человеку \n вопрос \n «Зачем он пришел на праздник?», а после \n достать из банки листок. \n Если человеку, которому задали вопрос, \n попался его собственный листок, \n то он побеждает."
        )
        self.player.setMedia(QMediaContent(QUrl.fromLocalFile("voice\\6.mp3")))
        self.player.play()
        self.timer.timeout.connect(self.update_timer)
        self.timer.start(1000)  # Запускаем таймер с интервалом 1 секунда
        self.remaining_time = 5 * 60  # 5 минут в секундах

    def update_timer(self):
        if self.remaining_time > 0:
            minutes = self.remaining_time // 60
            seconds = self.remaining_time % 60
            self.lbl2.setText(f"{minutes:2}:{seconds:02}")
            self.remaining_time -= 1
        else:
            self.label.setText("Время вышло!")

    def MainMenu1(self):
        self.player.stop()
        self.hide()
        self.mainwindow1 = MainWindow()
        self.mainwindow1.show()

    def konkurs_menu(self):
        self.player.stop()
        self.hide()
        self.konk = Window()
        self.konk.show()
    def timer_pause(self):
        self.timer.stop()


class Konkurs7(QMainWindow):
    def __init__(self):
        super().__init__()
        self.player = QMediaPlayer()
        self.ui1 = uic.loadUi("design\\window3.ui", self)
        self.setWindowTitle("Электронный тамада")
        self.timer = QTimer(self)
        self.setFixedSize(800, 500)
        self.btn2.clicked.connect(self.konkurs_menu)
        self.menu.clicked.connect(self.MainMenu1)
        self.btn1.clicked.connect(self.timer_pause)
        self.lbl.setText(
            "  Выберите несколько известных песен \n и включите их для участников. \n  Попросите их угадать \n название песни и исполнителя, \n когда они услышат её отрывок."
        )
        self.player.setMedia(QMediaContent(QUrl.fromLocalFile("voice\\7.mp3")))
        self.player.play()
        self.timer.timeout.connect(self.update_timer)
        self.timer.start(1000)  # Запускаем таймер с интервалом 1 секунда
        self.remaining_time = 5 * 60  # 5 минут в секундах

    def update_timer(self):
        if self.remaining_time > 0:
            minutes = self.remaining_time // 60
            seconds = self.remaining_time % 60
            self.lbl2.setText(f"{minutes:2}:{seconds:02}")
            self.remaining_time -= 1
        else:
            self.label.setText("Время вышло!")
    def timer_pause(self):
        self.timer.stop()

    def MainMenu1(self):
        self.player.stop()
        self.hide()
        self.mainwindow1 = MainWindow()
        self.mainwindow1.show()

    def konkurs_menu(self):
        self.player.stop()
        self.hide()
        self.konk = Window()
        self.konk.show()


class Konkurs8(QMainWindow):
    def __init__(self):
        super().__init__()
        self.player = QMediaPlayer()
        self.ui1 = uic.loadUi("design\\window3.ui", self)
        self.setWindowTitle("Электронный тамада")
        self.setFixedSize(800, 500)
        self.timer = QTimer(self)
        self.btn2.clicked.connect(self.konkurs_menu)
        self.menu.clicked.connect(self.MainMenu1)
        self.btn1.clicked.connect(self.timer_pause)
        self.lbl.setText(
            "  Разделите участников на пары\n и предложите им исполнить быстрый танец \n под разную музыку. \n Побеждает пара, которая лучше всех проявит \n свои танцевальные навыки \n и получит больше аплодисментов от зрителей."
        )
        self.player.setMedia(QMediaContent(QUrl.fromLocalFile("voice\\8.mp3")))
        self.player.play()
        self.timer.timeout.connect(self.update_timer)
        self.timer.start(1000)  # Запускаем таймер с интервалом 1 секунда
        self.remaining_time = 5 * 60  # 5 минут в секундах

    def update_timer(self):
        if self.remaining_time > 0:
            minutes = self.remaining_time // 60
            seconds = self.remaining_time % 60
            self.lbl2.setText(f"{minutes:2}:{seconds:02}")
            self.remaining_time -= 1
        else:
            self.label.setText("Время вышло!")
    def timer_pause(self):
        self.timer.stop()

    def MainMenu1(self):
        self.player.stop()
        self.hide()
        self.mainwindow1 = MainWindow()
        self.mainwindow1.show()

    def konkurs_menu(self):
        self.player.stop()
        self.hide()
        self.konk = Window()
        self.konk.show()


class Konkurs9(QMainWindow):
    def __init__(self):
        super().__init__()
        self.player = QMediaPlayer()
        self.player.setVolume(50)
        self.ui1 = uic.loadUi("design\\window3.ui", self)
        self.setWindowTitle("Электронный тамада")
        self.setFixedSize(800, 500)
        self.menu.clicked.connect(self.MainMenu1)
        self.btn2.clicked.connect(self.konkurs_menu)
        self.btn1.clicked.connect(self.timer_pause)

        def proverka(number):
            self.player.setMedia(
                QMediaContent(QUrl.fromLocalFile("voice\\" + number + ".mp3"))
            )
            self.player.play()
            self.timer = QTimer(self)

        spis1 = [
            "   Этот конкурс подходит для свадеб и требует \n подручные средства.\n Новоиспечённые муж и жена получают доски, \n гвозди и молоток. \n Их задача — сколотить свой первый стул. \n Работа должна быть быстрой, слаженной и \n качественной. \n Гостям будет интересно наблюдать, как \nпроявляется пара в совместном деле по хозяйству. \n Примечание: Вместо досок и инструментов \n можно использовать бумагу и клей."
        ]
        spis2 = [
            "   Гости становятся в круг. \n Каждый по очереди напевает пару строк из \n песен про праздники и всё, что с ними связано. \n Тот, кто не может пропеть, вылетает из игры. \n Оставшейся тройке гостей, \n которые проявили себя по полной и\n вспомнили больше всех праздничных песен, \n вручаются призы."
        ]
        spis3 = [
            "   Некоторые гости могут быть не знакомы друг \n с другом. \n Тамада проводит конкурс: первый выходит \n “машинист” — дружок, \n называет своё имя и увлечение жизни. \n Затем он “прицепляет” следующего гостя, \n который в свою очередь называет своё имя, \n увлечение по жизни. \n Процесс продолжается, пока весь “паровозик” \n не будет собран. \n Так все гости познакомятся и узнают \n друг друга ближе."
        ]
        spis4 = [
            "   Игроки выбирают случайным образом \n одного человека, который будет прятать \n определенный предмет. \n Спрятав его, все остальные игроки должны \nначать искать этот предмет до тех пор, \n пока не истечет отведенное время. Если \n предмет не нашли, то побеждает тот человек, \n который его прятал, а если наоборот, то \n побеждают те, кто его искал."
        ]
        spis5 = [
            "   Игроки должны открыть \n на своих телефонах фотографии, \n которые так или иначе связаны \n с участниками игры. \n Когда фотографии будут открыты, \n игрокам потребуется положить телефоны \n рядом с друг другом, \n тем самым образовывая фотоколлаж. "
        ]
        spis6 = [
            "   Каждый из участников конкурса должен \n  написать на листке причину, \n по которой он пришел на праздник, \n а после положить листок с причиной в банку. \n Кто-то из участников должен вызваться \n добровольцем и задать случайному человеку \n вопрос \n «Зачем он пришел на праздник?», а после \n достать из банки листок. \n Если человеку, которому задали вопрос, \n попался его собственный листок, \n то он побеждает."
        ]
        spis7 = [
            "   Выберите несколько известных песен \n и включите их для участников. \n  Попросите их угадать \n название песни и исполнителя, \n когда они услышат её отрывок."
        ]
        spis8 = [
            "  Разделите участников на пары \n и предложите им исполнить быстрый танец \n под разную музыку. \n Побеждает пара, которая лучше всех проявит \n свои танцевальные навыки \n и получит больше аплодисментов от зрителей."
        ]

        a = random.choice(spis1 + spis2 + spis3 + spis4 + spis5 + spis6 + spis7 + spis8)

        self.lbl.setText(a)

        if "Этот конкурс подходит для свадеб" in a:
            num = "1"
            proverka(num)
        elif "Гости становятся в круг" in a:
            num = "2"
            proverka(num)
        elif "Некоторые гости могут быть не знакомы друг" in a:
            num = "3"
            proverka(num)
        elif "Игроки выбирают случайным образом" in a:
            num = "4"
            proverka(num)
        elif "Игроки должны открыть" in a:
            num = "5"
            proverka(num)
        elif "Каждый из участников конкурса должен" in a:
            num = "6"
            proverka(num)
        elif "Выберите несколько известных песен" in a:
            num = "7"
            proverka(num)
        else:
            num = "8"
            proverka(num)
        self.timer.timeout.connect(self.update_timer)
        self.timer.start(1000)  # Запускаем таймер с интервалом 1 секунда
        self.remaining_time = 5 * 60  # 5 минут в секундах

    def update_timer(self):
        if self.remaining_time > 0:
            minutes = self.remaining_time // 60
            seconds = self.remaining_time % 60
            self.lbl2.setText(f"{minutes:2}:{seconds:02}")
            self.remaining_time -= 1
        else:
            QMessageBox.critical(
                self,
                "Таймер",
                "Время истекло",
                QMessageBox.Ok,
            )
    def timer_pause(self):
        self.timer.stop()

    def MainMenu1(self):
        self.player.stop()
        self.hide()
        self.mainwindow1 = MainWindow()
        self.mainwindow1.show()

    def konkurs_menu(self):
        self.player.stop()
        self.hide()
        self.konk = Window()
        self.konk.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window2 = MusicWindow()
    app.exec_()