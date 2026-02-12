# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'fight.ui'
##
## Created by: Qt User Interface Compiler version 6.10.2
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QLineEdit,
    QMainWindow, QMenuBar, QPlainTextEdit, QPushButton,
    QSizePolicy, QStatusBar, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(790, 599)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayoutWidget = QWidget(self.centralwidget)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(0, 0, 421, 511))
        self.gl_status = QGridLayout(self.gridLayoutWidget)
        self.gl_status.setObjectName(u"gl_status")
        self.gl_status.setContentsMargins(0, 0, 0, 0)
        self.label_7 = QLabel(self.gridLayoutWidget)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gl_status.addWidget(self.label_7, 6, 0, 1, 1)

        self.label_6 = QLabel(self.gridLayoutWidget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gl_status.addWidget(self.label_6, 5, 0, 1, 1)

        self.label_2 = QLabel(self.gridLayoutWidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gl_status.addWidget(self.label_2, 1, 0, 1, 1)

        self.label_3 = QLabel(self.gridLayoutWidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gl_status.addWidget(self.label_3, 2, 0, 1, 1)

        self.label_4 = QLabel(self.gridLayoutWidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gl_status.addWidget(self.label_4, 3, 0, 1, 1)

        self.label = QLabel(self.gridLayoutWidget)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gl_status.addWidget(self.label, 0, 0, 1, 1)

        self.label_5 = QLabel(self.gridLayoutWidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gl_status.addWidget(self.label_5, 4, 0, 1, 1)

        self.pb_roll = QPushButton(self.centralwidget)
        self.pb_roll.setObjectName(u"pb_roll")
        self.pb_roll.setGeometry(QRect(30, 510, 79, 31))
        self.pte_output = QPlainTextEdit(self.centralwidget)
        self.pte_output.setObjectName(u"pte_output")
        self.pte_output.setGeometry(QRect(420, 0, 371, 511))
        self.pb_test = QPushButton(self.centralwidget)
        self.pb_test.setObjectName(u"pb_test")
        self.pb_test.setGeometry(QRect(130, 510, 79, 31))
        self.pb_copy = QPushButton(self.centralwidget)
        self.pb_copy.setObjectName(u"pb_copy")
        self.pb_copy.setGeometry(QRect(590, 510, 79, 31))
        self.pb_create_enemy = QPushButton(self.centralwidget)
        self.pb_create_enemy.setObjectName(u"pb_create_enemy")
        self.pb_create_enemy.setGeometry(QRect(220, 510, 111, 31))
        self.le_target_winrate = QLineEdit(self.centralwidget)
        self.le_target_winrate.setObjectName(u"le_target_winrate")
        self.le_target_winrate.setGeometry(QRect(340, 516, 113, 20))
        self.pb_character_card = QPushButton(self.centralwidget)
        self.pb_character_card.setObjectName(u"pb_character_card")
        self.pb_character_card.setGeometry(QRect(500, 510, 79, 31))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 790, 33))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Fight Simulator", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Health", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Defense", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Agility", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Strength", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Intelligence", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Name", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Attack", None))
        self.pb_roll.setText(QCoreApplication.translate("MainWindow", u"Roll", None))
        self.pb_test.setText(QCoreApplication.translate("MainWindow", u"Test(10000)", None))
        self.pb_copy.setText(QCoreApplication.translate("MainWindow", u"Copy", None))
        self.pb_create_enemy.setText(QCoreApplication.translate("MainWindow", u"\u65d7\u9f13\u76f8\u5f53\u7684\u5bf9\u624b", None))
        self.pb_character_card.setText(QCoreApplication.translate("MainWindow", u"\u89d2\u8272\u5361", None))
    # retranslateUi

