# 语音助手程序 README.md

## **前言**

- 本项目来自同济大学软件学院2023年春季用户交互设计课程的 Assignment 2。是一个基于 Python 编写的语音助手程序。用户可以通过语音下达指令，让语音助手协助完成播放音乐、打开网页、播放视频等任务。

## **作者**

此程序由 同济大学软件工程专业 2021 级韩嘉睿 开发，如有问题或更好的建议，请联系作者。

## **环境需求**

- Windows 10 家庭版系统
- Python 3.10.10
- PyQt5 5.15.9
- SpeechRecognition 3.10.0
- PyAudio 0.2.13
- Playsound 1.3.0

## **安装步骤**

1. 安装 Python 3.10.10
2. 安装 PyQt5：在命令行中运行 **`pip install pyqt5`**
3. 安装 SpeechRecognition：在命令行中运行 **`pip install SpeechRecognition`**
4. 安装 PyAudio：在命令行中运行 **`pip install pyaudio`**
5. 安装 Playsound：在命令行中运行 **`pip install playsound`**
6. 注意，项目在speech虚拟环境下完成开发。目录中提供了虚拟环境的所有依赖项和版本信息，保存在environment.txt文件中。可以在命令行中运行 **`conda create --name speech --file environment.txt`**创建虚拟环境。

## **使用说明**

1. 下载并解压缩代码
2. 在命令行中进入程序所在目录，运行 **`python asr.py`**
3. 在程序开始运行后，会有一段程序开启提示音。等待提示音结束后，语音识别模块自动开启。
4. 在语音识别模块开启后，可以根据文本提示对着麦克风说出命令，例如 "listen to music"、"tell me my location"、”watch a movie” 等。
5. 当程序接收并识别出指令后，会执行相应的动作，并播放音效提示，且在界面中进行文本提示。
6. 当需要退出程序时，可以说出 "goodbye"，程序会自动退出。

## **注意事项**

1. 程序的语音识别基于 Sphinx 引擎，需要用户安装英语语言包。可以在命令行中运行以下命令来安装语言包：**`pip install pocketsphinx --upgrade`**
2. 程序需要使用麦克风来录音，如果无法录音或录音质量不好，可以尝试调整麦克风设备的音量或距离。
3. 程序中使用了 Playsound 库来播放音效，需要用户的系统支持 MP3 和 WAV 格式的音频文件。
4. 程序可能会因为网络问题而无法打开网页或播放视频。如果出现此类问题，请检查网络连接并重试。