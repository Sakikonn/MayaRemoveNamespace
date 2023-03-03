# 主窗口

from PySide6.QtWidgets import QMainWindow
from .ui_MainWindow import Ui_MainWindow

class MainWindow(QMainWindow):
    def __init__(self, *args) -> None:
        super().__init__(*args)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.UpdateUIInfo()
        
    def UpdateUIInfo(self):
        # 更新配置文件UI界面信息
        self.ui.ConfigWidget.UpdateUIInfo()
