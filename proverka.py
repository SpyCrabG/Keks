import os
import sys
from PyQt5.QtCore import QCoreApplication, QUrl, QDir, Qt, QTimer
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QPushButton, QVBoxLayout
from PyQt5.QtMultimedia import QMediaContent, QMediaPlayer
from PyQt5 import uic, QtTest
import random
from playsound import playsound

playsound("voice/1.mp3")