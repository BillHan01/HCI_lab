# 软件工程2021级 2051973 韩嘉睿
# 用户交互设计 Assignment 2 作业
# latest update: 2023/4/28 22:17

from PyQt5 import QtWidgets, QtGui, QtCore
from asrInterface import Ui_MainWindow
import sys
import threading
import speech_recognition as sr
import os
import webbrowser
import playsound


class ASRThread(QtCore.QThread):
    threadDetected = QtCore.pyqtSignal()  # 定义一个线程开启的信号
    musicDetected = QtCore.pyqtSignal()  # 定义一个识别到"music"的信号
    locationDetected = QtCore.pyqtSignal()  # 定义一个识别到"location"的信号
    movieDetected = QtCore.pyqtSignal()  # 定义一个识别到"movie"的信号
    goodbyeDetected = QtCore.pyqtSignal()   # 定义一个识别到 "goodbye" 的信号

    def __init__(self):
        QtCore.QThread.__init__(self)
        self.recognizer = sr.Recognizer()
        self.microphone = sr.Microphone()
        self.music_file = "City_Mir_wird_kalt_dabei.mp3" # 音乐文件路径
        self.video_file = "lockdown.mp4" # 视频文件路径


    def run(self):
        self.threadDetected.emit()  # 发出信号
        playsound.playsound("sound/chinese_welcome_stinger.wav")
        with self.microphone as source:
            self.recognizer.adjust_for_ambient_noise(source)
            while True:
                audio = self.recognizer.listen(source)
                try:
                    text = self.recognizer.recognize_sphinx(audio)
                    print("You said: ", text)
                    if "music" in text:
                        self.musicDetected.emit()  # 发出信号
                        os.startfile(self.music_file)
                    elif "location" in text:
                        self.locationDetected.emit()  # 发出信号
                        webbrowser.open('https://www.map.google.com')
                    elif "movie" in text:
                        self.movieDetected.emit()  # 发出信号
                        os.startfile(self.video_file)
                    elif "goodbye" in text:
                        self.goodbyeDetected.emit() # 发出信号

                except sr.UnknownValueError:
                    print("Could not understand audio")
                except sr.RequestError as e:
                    print("Could not request results; {0}".format(e))

class myWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(myWindow, self).__init__()
        self.myCommand = " "
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # 创建线程并启动
        self.asr_thread = ASRThread()
        self.asr_thread.threadDetected.connect(self.onThreadDetected)   # 连接信号到槽函数
        self.asr_thread.musicDetected.connect(self.onMusicDetected)  # 连接信号到槽函数
        self.asr_thread.locationDetected.connect(self.onLocationDetected)  # 连接信号到槽函数
        self.asr_thread.movieDetected.connect(self.onMovieDetected)  # 连接信号到槽函数
        self.asr_thread.goodbyeDetected.connect(self.onGoodbyeDetected)  # 连接信号到槽函数
        self.asr_thread.start()

    def onThreadDetected(self):
        text = "Hey! What can I do for you?"
        self.showTextOneByOne(text)
        QtCore.QTimer.singleShot(5000, self.clearResultLabel) # 创建定时器

    def onMusicDetected(self):
        playsound.playsound("sound/confirmation_alert.wav")
        text = "OK! I'll play the music for you."
        self.showTextOneByOne(text)
        QtCore.QTimer.singleShot(5500, self.clearResultLabel) # 创建定时器

    def onLocationDetected(self):
        playsound.playsound("sound/confirmation_alert.wav")
        text = "OK! I'll open the Google Maps for you."
        self.showTextOneByOne(text)
        QtCore.QTimer.singleShot(6000, self.clearResultLabel) # 创建定时器

    def onMovieDetected(self):
        playsound.playsound("sound/confirmation_alert.wav")
        text = "OK! I'll open a Video for you."
        self.showTextOneByOne(text)
        QtCore.QTimer.singleShot(5000, self.clearResultLabel) # 创建定时器

    def onGoodbyeDetected(self):
        playsound.playsound("sound/confirmation_alert.wav")
        QtCore.QTimer.singleShot(1000, self.close)  # 延时3秒后关闭程序

    def clearResultLabel(self):
        self.ui.resultLabel.setText("") # 清空 Label 的文本

    def showTextOneByOne(self, text):
        self.ui.resultLabel.setText("")  # Clear the label text
        # 创建一个 QTimer
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(lambda: self.showNextCharacter(text))
        self.timer.start(100)

    def showNextCharacter(self, text):
        current_text = self.ui.resultLabel.text()
        if len(current_text) < len(text):
            next_char = text[len(current_text)]
            self.ui.resultLabel.setText(current_text + next_char)
        else:
            self.timer.stop()  # 当文本打印完成时，停止 Qtimer

app = QtWidgets.QApplication([])
application = myWindow()
application.show()
sys.exit(app.exec())

