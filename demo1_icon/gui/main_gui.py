# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     main_gui
   Description :
   Author :       pfc
   date：          2018/8/20
-------------------------------------------------
   Change Activity:
                   2018/8/20:
-------------------------------------------------
"""
__author__ = 'pfc'

from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QWidget


class Ico(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        self.setGeometry(300, 300, 300, 220)
        self.setWindowTitle('Alter Ico')
        self.setWindowIcon(QIcon('../resource/favicon.ico'))
