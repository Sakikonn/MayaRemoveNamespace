# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainWindow.ui'
##
## Created by: Qt User Interface Compiler version 6.4.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QHeaderView, QLabel,
    QLineEdit, QMainWindow, QMenuBar, QPushButton,
    QSizePolicy, QStatusBar, QTabWidget, QTableWidgetItem,
    QToolButton, QVBoxLayout, QWidget)

from Blocks.ConfigWidget import ConfigWidget
from Blocks.MyWidget import MyWidget
from WidgetComponents.Files_Table import Files_Table

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(662, 584)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.BatchProcessing = QWidget()
        self.BatchProcessing.setObjectName(u"BatchProcessing")
        self.verticalLayout_2 = QVBoxLayout(self.BatchProcessing)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.MyWidget = MyWidget(self.BatchProcessing)
        self.MyWidget.setObjectName(u"MyWidget")
        self.verticalLayout_3 = QVBoxLayout(self.MyWidget)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.LET_DirPath = QLineEdit(self.MyWidget)
        self.LET_DirPath.setObjectName(u"LET_DirPath")

        self.horizontalLayout.addWidget(self.LET_DirPath)

        self.TBT_SelectDir = QToolButton(self.MyWidget)
        self.TBT_SelectDir.setObjectName(u"TBT_SelectDir")

        self.horizontalLayout.addWidget(self.TBT_SelectDir)


        self.verticalLayout_3.addLayout(self.horizontalLayout)

        self.Files_Table = Files_Table(self.MyWidget)
        if (self.Files_Table.columnCount() < 1):
            self.Files_Table.setColumnCount(1)
        __qtablewidgetitem = QTableWidgetItem()
        self.Files_Table.setHorizontalHeaderItem(0, __qtablewidgetitem)
        self.Files_Table.setObjectName(u"Files_Table")
        self.Files_Table.horizontalHeader().setStretchLastSection(True)
        self.Files_Table.verticalHeader().setVisible(False)

        self.verticalLayout_3.addWidget(self.Files_Table)

        self.PBT_Start = QPushButton(self.MyWidget)
        self.PBT_Start.setObjectName(u"PBT_Start")

        self.verticalLayout_3.addWidget(self.PBT_Start)


        self.verticalLayout_2.addWidget(self.MyWidget)

        self.tabWidget.addTab(self.BatchProcessing, "")
        self.ConfigSettingTab = QWidget()
        self.ConfigSettingTab.setObjectName(u"ConfigSettingTab")
        self.verticalLayout_4 = QVBoxLayout(self.ConfigSettingTab)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.ConfigWidget = ConfigWidget(self.ConfigSettingTab)
        self.ConfigWidget.setObjectName(u"ConfigWidget")
        self.verticalLayout_6 = QVBoxLayout(self.ConfigWidget)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.HL_Config_0 = QHBoxLayout()
        self.HL_Config_0.setObjectName(u"HL_Config_0")
        self.label = QLabel(self.ConfigWidget)
        self.label.setObjectName(u"label")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)

        self.HL_Config_0.addWidget(self.label)

        self.LET_DirMayaPy = QLineEdit(self.ConfigWidget)
        self.LET_DirMayaPy.setObjectName(u"LET_DirMayaPy")
        self.LET_DirMayaPy.setEnabled(False)

        self.HL_Config_0.addWidget(self.LET_DirMayaPy)

        self.TBP_SelectMayaPyPath = QToolButton(self.ConfigWidget)
        self.TBP_SelectMayaPyPath.setObjectName(u"TBP_SelectMayaPyPath")

        self.HL_Config_0.addWidget(self.TBP_SelectMayaPyPath)


        self.verticalLayout_6.addLayout(self.HL_Config_0)

        self.HL_Config_1 = QHBoxLayout()
        self.HL_Config_1.setObjectName(u"HL_Config_1")
        self.label_2 = QLabel(self.ConfigWidget)
        self.label_2.setObjectName(u"label_2")

        self.HL_Config_1.addWidget(self.label_2)

        self.LE_CharacterName = QLineEdit(self.ConfigWidget)
        self.LE_CharacterName.setObjectName(u"LE_CharacterName")

        self.HL_Config_1.addWidget(self.LE_CharacterName)


        self.verticalLayout_6.addLayout(self.HL_Config_1)

        self.HL_Config_2 = QHBoxLayout()
        self.HL_Config_2.setObjectName(u"HL_Config_2")
        self.label_3 = QLabel(self.ConfigWidget)
        self.label_3.setObjectName(u"label_3")

        self.HL_Config_2.addWidget(self.label_3)

        self.LE_ModelName = QLineEdit(self.ConfigWidget)
        self.LE_ModelName.setObjectName(u"LE_ModelName")

        self.HL_Config_2.addWidget(self.LE_ModelName)


        self.verticalLayout_6.addLayout(self.HL_Config_2)

        self.HL_Config_3 = QHBoxLayout()
        self.HL_Config_3.setObjectName(u"HL_Config_3")
        self.label_4 = QLabel(self.ConfigWidget)
        self.label_4.setObjectName(u"label_4")

        self.HL_Config_3.addWidget(self.label_4)

        self.LE_SkeletalName = QLineEdit(self.ConfigWidget)
        self.LE_SkeletalName.setObjectName(u"LE_SkeletalName")

        self.HL_Config_3.addWidget(self.LE_SkeletalName)


        self.verticalLayout_6.addLayout(self.HL_Config_3)


        self.verticalLayout_4.addWidget(self.ConfigWidget)

        self.PB_Config_Save = QPushButton(self.ConfigSettingTab)
        self.PB_Config_Save.setObjectName(u"PB_Config_Save")

        self.verticalLayout_4.addWidget(self.PB_Config_Save)

        self.tabWidget.addTab(self.ConfigSettingTab, "")

        self.verticalLayout.addWidget(self.tabWidget)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 662, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.PBT_Start.clicked.connect(self.MyWidget.PBT_StartClicked)
        self.TBT_SelectDir.clicked.connect(self.MyWidget.TBT_SelectDirClicked)
        self.LET_DirPath.textChanged.connect(self.MyWidget.LET_DirPathTextChenge)
        self.LE_CharacterName.textChanged.connect(self.ConfigWidget.ConfigChange)
        self.LE_ModelName.textChanged.connect(self.ConfigWidget.ConfigChange)
        self.LE_SkeletalName.textChanged.connect(self.ConfigWidget.ConfigChange)
        self.PB_Config_Save.clicked.connect(self.ConfigWidget.SaveConfigEvent)
        self.TBP_SelectMayaPyPath.clicked.connect(self.ConfigWidget.TBP_SelectMayaPyPathClicked)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.TBT_SelectDir.setText(QCoreApplication.translate("MainWindow", u"...", None))
        ___qtablewidgetitem = self.Files_Table.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Files_Name", None));
        self.PBT_Start.setText(QCoreApplication.translate("MainWindow", u"\u5f00\u59cb\u5904\u7406", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.BatchProcessing), QCoreApplication.translate("MainWindow", u"\u6279\u5904\u7406", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"MayaPyLocation", None))
        self.TBP_SelectMayaPyPath.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u89d2\u8272\u7ec4\u540d", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u6a21\u578b\u7ec4\u540d", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\u9aa8\u9abc\u7ec4\u540d", None))
        self.PB_Config_Save.setText(QCoreApplication.translate("MainWindow", u"\u4fdd\u5b58", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.ConfigSettingTab), QCoreApplication.translate("MainWindow", u"\u914d\u7f6e\u4fe1\u606f", None))
    # retranslateUi

