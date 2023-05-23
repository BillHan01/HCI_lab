# latest edit: 2023/4/28 22:15
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QMovie

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(540, 920)
        MainWindow.setStyleSheet("background-color: rgb(255, 255, 255);")

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.backgroundFig = QtWidgets.QLabel(self.centralwidget)
        self.backgroundFig.setGeometry(QtCore.QRect(0, 0, 540, 540))
        self.background_gif = QMovie("icon/background.gif")
        self.backgroundFig.setMovie(self.background_gif)
        self.background_gif.start()
        self.backgroundFig.setScaledContents(True)
        self.backgroundFig.setObjectName("backgroundFig")

        self.voiceFig = QtWidgets.QLabel(self.centralwidget)
        self.voiceFig.setGeometry(QtCore.QRect(220, 220, 100, 100))
        self.voice_gif = QMovie("icon/voice_icon.gif")
        self.voiceFig.setMovie(self.voice_gif)
        self.voice_gif.start()
        self.voiceFig.setScaledContents(True)
        self.voiceFig.setObjectName("voiceFig")

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(120, 600, 300, 25))
        self.label.setText("Hi! How can I help?")
        self.label.setFont(QtGui.QFont("Calibri", 14))
        self.label.setStyleSheet("color: rgb(0, 117, 210);")
        self.label.setWordWrap(True)
        self.label.setObjectName("label")

        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(120, 625, 301, 25))
        self.label_2.setText("You can:")
        self.label_2.setFont(QtGui.QFont("Calibri", 14))
        self.label_2.setStyleSheet("color: rgb(0, 117, 210);")
        self.label_2.setWordWrap(True)
        self.label_2.setObjectName("label_2")

        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(120, 650, 301, 60))
        self.label_3.setText("1. Enjoy music by saying \"Play Music!\"")
        self.label_3.setFont(QtGui.QFont("Calibri", 14))
        self.label_3.setStyleSheet("color: rgb(0, 117, 210);")
        self.label_3.setWordWrap(True)
        self.label_3.setObjectName("label_3")

        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(120, 710, 301, 60))
        self.label_4.setText("2. Get to know your location by saying \"tell me my location!\"")
        self.label_4.setFont(QtGui.QFont("Calibri", 14))
        self.label_4.setStyleSheet("color: rgb(0, 117, 210);")
        self.label_4.setWordWrap(True)
        self.label_4.setObjectName("label_4")

        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(120, 770, 301, 60))
        self.label_5.setText("3. Enjoy a movie by saying \"watch movie!\"")
        self.label_5.setFont(QtGui.QFont("Calibri", 14))
        self.label_5.setStyleSheet("color: rgb(0, 117, 210);")
        self.label_5.setWordWrap(True)
        self.label_5.setObjectName("label_5")

        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(120, 830, 301, 70))
        self.label_6.setText("4. Say \"Good bye!\" to close the assistant")
        self.label_6.setFont(QtGui.QFont("Calibri", 14))
        self.label_6.setStyleSheet("color: rgb(0, 117, 210);")
        self.label_6.setWordWrap(True)
        self.label_6.setObjectName("label_5")

        self.resultLabel = QtWidgets.QLabel(self.centralwidget)
        self.resultLabel.setGeometry(QtCore.QRect(120, 520, 301, 70))
        self.resultLabel.setText("")
        self.resultLabel.setFont(QtGui.QFont("Calibri", 18))
        self.resultLabel.setStyleSheet("color: rgb(0, 128, 128);")
        self.resultLabel.setWordWrap(True)
        self.resultLabel.setObjectName("resultLabel")

        MainWindow.setCentralWidget(self.centralwidget)

        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Bill's Voice Assistant"))
        self.label.setText(_translate("MainWindow", "Hi! How can I help?"))
        self.label_2.setText(_translate("MainWindow", "You can:"))
        self.label_3.setText(_translate("MainWindow", "1. Enjoy music by saying \"Play Music!\""))
        self.label_4.setText(_translate("MainWindow", "2. Get to know your location by saying \"tell me my location\""))
        self.label_5.setText(_translate("MainWindow", "3. Enjoy a movie by saying \"watch movie!\""))
        self.label_6.setText(_translate("MainWindow", "4. Say \"Good bye!\" to close the assistant"))