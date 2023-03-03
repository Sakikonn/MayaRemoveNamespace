import sys
from typing import Optional
from PySide6 import QtWidgets
from PySide6.QtWidgets import QMainWindow,QWidget
from PySide6.QtCore import QDir
import PySide6.QtWidgets
import PySide6.QtCore

from Window.MainWindow import MainWindow

if __name__ == "__main__":
    # 添加顶级目录
    sys.path.append(QDir.currentPath())

    app = QtWidgets.QApplication(sys.argv)

    widget = MainWindow()
    widget.show()


    sys.exit(app.exec())