import os
import sys
from PyQt5.QtCore import QCoreApplication, QUrl, QDir
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QPushButton, QVBoxLayout
from PyQt5.QtMultimedia import QMediaContent, QMediaPlayer
from PyQt5 import uic

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

        # Загрузка UI из файла
        self.ui = uic.loadUi('design\\proect_pizdi.ui', self)

        # Инициализация плеера
        self.player = QMediaPlayer()

        # Загрузка списка файлов с музыкой
        self.music_files = get_music_files()
        self.current_index = 0  # Текущий индекс трека

        # Настройка кнопок
        self.setup_buttons()

        # Отображение окна
        self.show()

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
        else:
            self.player.play()

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
        # ... (Реализация открытия нового окна)
        pass

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())
