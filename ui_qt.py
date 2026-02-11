# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'qt.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QGridLayout,
    QLabel, QLineEdit, QMainWindow, QMenuBar,
    QPlainTextEdit, QPushButton, QRadioButton, QSizePolicy,
    QStatusBar, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(857, 689)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.pte_output = QPlainTextEdit(self.centralwidget)
        self.pte_output.setObjectName(u"pte_output")
        self.pte_output.setGeometry(QRect(460, -7, 391, 591))
        self.le_0 = QLineEdit(self.centralwidget)
        self.le_0.setObjectName(u"le_0")
        self.le_0.setGeometry(QRect(130, 10, 113, 22))
        self.le_1 = QLineEdit(self.centralwidget)
        self.le_1.setObjectName(u"le_1")
        self.le_1.setGeometry(QRect(280, 10, 113, 22))
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(90, 10, 49, 21))
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(390, 10, 49, 21))
        self.label_2.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.label_2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.comboBox_sign1 = QComboBox(self.centralwidget)
        self.comboBox_sign1.setObjectName(u"comboBox_sign1")
        self.comboBox_sign1.setGeometry(QRect(20, 70, 61, 24))
        self.le_number1 = QLineEdit(self.centralwidget)
        self.le_number1.setObjectName(u"le_number1")
        self.le_number1.setGeometry(QRect(90, 70, 71, 22))
        self.le_text1 = QLineEdit(self.centralwidget)
        self.le_text1.setObjectName(u"le_text1")
        self.le_text1.setGeometry(QRect(180, 70, 271, 22))
        self.rb_0 = QRadioButton(self.centralwidget)
        self.rb_0.setObjectName(u"rb_0")
        self.rb_0.setGeometry(QRect(20, 10, 92, 20))
        self.rb_0.setChecked(True)
        self.gridLayoutWidget = QWidget(self.centralwidget)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(20, 130, 431, 451))
        self.gl_choices = QGridLayout(self.gridLayoutWidget)
        self.gl_choices.setObjectName(u"gl_choices")
        self.gl_choices.setContentsMargins(0, 0, 0, 0)
        self.label_4 = QLabel(self.gridLayoutWidget)
        self.label_4.setObjectName(u"label_4")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        self.label_4.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gl_choices.addWidget(self.label_4, 0, 1, 1, 1)

        self.label_3 = QLabel(self.gridLayoutWidget)
        self.label_3.setObjectName(u"label_3")
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)

        self.gl_choices.addWidget(self.label_3, 0, 0, 1, 1)

        self.gl_choices.setColumnStretch(0, 1)
        self.gl_choices.setColumnStretch(1, 3)
        self.radioButton_2 = QRadioButton(self.centralwidget)
        self.radioButton_2.setObjectName(u"radioButton_2")
        self.radioButton_2.setGeometry(QRect(20, 110, 92, 20))
        self.pb_roll = QPushButton(self.centralwidget)
        self.pb_roll.setObjectName(u"pb_roll")
        self.pb_roll.setGeometry(QRect(150, 593, 111, 31))
        self.comboBox_sign0 = QComboBox(self.centralwidget)
        self.comboBox_sign0.setObjectName(u"comboBox_sign0")
        self.comboBox_sign0.setGeometry(QRect(20, 40, 61, 24))
        self.le_number0 = QLineEdit(self.centralwidget)
        self.le_number0.setObjectName(u"le_number0")
        self.le_number0.setGeometry(QRect(90, 40, 71, 22))
        self.le_text0 = QLineEdit(self.centralwidget)
        self.le_text0.setObjectName(u"le_text0")
        self.le_text0.setGeometry(QRect(180, 40, 271, 22))
        self.pb_copy = QPushButton(self.centralwidget)
        self.pb_copy.setObjectName(u"pb_copy")
        self.pb_copy.setGeometry(QRect(620, 593, 79, 31))
        self.cb_last = QCheckBox(self.centralwidget)
        self.cb_last.setObjectName(u"cb_last")
        self.cb_last.setGeometry(QRect(30, 600, 78, 20))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 857, 33))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u9ab0\u70b9", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"0<--", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"-->100", None))
        self.rb_0.setText(QCoreApplication.translate("MainWindow", u"\u503e\u5411", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\u9009\u9879", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u6743\u91cd", None))
        self.radioButton_2.setText(QCoreApplication.translate("MainWindow", u"\u9009\u62e9", None))
        self.pb_roll.setText(QCoreApplication.translate("MainWindow", u"Roll", None))
        self.pb_copy.setText(QCoreApplication.translate("MainWindow", u"Copy", None))
        self.cb_last.setText(QCoreApplication.translate("MainWindow", u"\u5927\u6210\u5931\uff01", None))
    # retranslateUi

