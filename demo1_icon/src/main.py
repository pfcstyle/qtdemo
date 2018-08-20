# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     main.py
   Description :
   Author :       pfc
   date：          2018/8/20
-------------------------------------------------
   Change Activity:
                   2018/8/20:
-------------------------------------------------
"""
__author__ = 'pfc'

import sys
from PyQt5.QtWidgets import QApplication
from main_gui import Ico

sys._excepthook = sys.excepthook


def my_exception_hook(exctype, value, traceback):
    # Print the error and traceback
    print(exctype, value, traceback)
    # Call the normal Exception hook after
    sys._excepthook(exctype, value, traceback)
    sys.exit(1)


# Set the exception hook to our wrapping function
sys.excepthook = my_exception_hook


def main():
    app = QApplication(sys.argv)
    ex = Ico()
    ex.show()
    try:
        sys.exit(app.exec_())
    except:
        print("Exiting")


if __name__ == '__main__':
    main()
