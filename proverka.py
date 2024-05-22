import sys
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtWidgets import QWidget, QApplication, \
    QLCDNumber, QSlider, QVBoxLayout, QHBoxLayout, QPushButton
import random
spis1 = ["помоги"]
spis2 = ["не помоги"]

print("Случайный список:", random.choice(spis1 + spis2))