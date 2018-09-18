import sys
from PyQt5.QtWidgets import (QWidget, QToolTip, QDesktopWidget, QMessageBox,QTextEdit,QLabel,
    QPushButton, QApplication,QMainWindow, QAction, qApp, QHBoxLayout, QVBoxLayout,QGridLayout,
    QLineEdit)
from PyQt5.QtGui import QFont,QIcon
from PyQt5.QtCore import QCoreApplication


# def show_w():
#     '显示窗口'
#
#     app = QApplication(sys.argv)  # 所有的PyQt5应用必须创建一个应用（Application）对象。
#     # sys.argv参数是一个来自命令行的参数列表。
#
#     w = QWidget()  # Qwidget组件是PyQt5中所有用户界面类的基础类。我们给QWidget提供了默认的构造方法。
#     # 默认构造方法没有父类。没有父类的widget组件将被作为窗口使用。
#
#     w.resize(500, 500)  # resize()方法调整了widget组件的大小。它现在是500px宽，500px高。
#     w.move(500, 100)  # move()方法移动widget组件到一个位置，这个位置是屏幕上x=500,y=200的坐标。
#     w.setWindowTitle('Simple')  # 设置了窗口的标题。这个标题显示在标题栏中。
#     w.show()  # show()方法在屏幕上显示出widget。一个widget对象在这里第一次被在内存中创建，并且之后在屏幕上显示。
#
#     sys.exit(app.exec_())  # 应用进入主循环。在这个地方，事件处理开始执行。主循环用于接收来自窗口触发的事件，
#     # 并且转发他们到widget应用上处理。如果我们调用exit()方法或主widget组件被销毁，主循环将退出。
#     # sys.exit()方法确保一个不留垃圾的退出。系统环境将会被通知应用是怎样被结束的。


# # ##***提示文本***## #
# class PromptText(QWidget):
#
#     def __init__(self):
#         super().__init__()
#         self.initUI()
#
#     def initUI(self):
#         QToolTip.setFont(QFont('SansSerif', 10))  # 这个静态方法设置了用于提示框的字体。
#         # 这里使用10px大小的SansSerif字体。
#         self.setToolTip('This is a <b>QWidget</b> widget')  # 调用setTooltip()方法创建提示框。
#         # 可以在提示框中使用富文本格式。
#         btn = QPushButton('Button', self)  # 创建按钮
#         btn.setToolTip('This is a <b>QPushButton</b> widget')  # 设置按钮提示框
#         btn.resize(btn.sizeHint())  # 改变按钮大小
#         btn.move(300, 100)  # 移动按钮位置
#         self.setGeometry(300, 100, 600, 600)
#         self.setWindowTitle('Tooltips')
#         self.show()


# # ##***关闭窗口***## #
# class CloseW(QWidget):
#
#     def __init__(self):
#         super().__init__()
#         self.initUI()
#
#     def initUI(self):
#         qbtn = QPushButton('Quit', self)  # 创建了一个按钮。按钮是一个QPushButton类的实例。
#         # 构造方法的第一个参数是显示在button上的标签文本。第二个参数是父组件。
#         # 父组件是Example组件，它继承了QWiget类。
#         qbtn.clicked.connect(QCoreApplication.instance().quit)
#         qbtn.resize(qbtn.sizeHint())
#         qbtn.move(500, 50)
#         self.setGeometry(300, 100, 600, 600)
#         self.setWindowTitle('excise')
#         self.show()

#
# # ##***Message Box***## #
# class MessageBox(QWidget):
#
#     def __init__(self):
#         super().__init__()
#         self.initUI()
#
#     def initUI(self):
#         qbtn = QPushButton('Quit', self)  # 创建了一个按钮。按钮是一个QPushButton类的实例。
#         # 构造方法的第一个参数是显示在button上的标签文本。第二个参数是父组件。
#         # 父组件是Example组件，它继承了QWiget类。
#         qbtn.clicked.connect(QCoreApplication.instance().quit)
#         qbtn.resize(qbtn.sizeHint())
#         qbtn.move(500, 50)
#         self.setGeometry(300, 100, 600, 600)
#         self.setWindowTitle('excise')
#         self.show()
#
#     def closeEvent(self, event):
#
#         reply = QMessageBox.question(self, 'Message',
#                                      "Are you sure to quit?", QMessageBox.Yes |
#                                      QMessageBox.No, QMessageBox.No)
#         if reply == QMessageBox.Yes:
#             event.accept()
#         else:
#             event.ignore()


# ##***屏幕居中窗口***## #
class CenterW(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.resize(250, 150)
        self.center()  # 将窗口居中放置的代码在自定义的center()方法中。
        self.setWindowTitle('Center')
        self.show()

    def center(self):
        qr = self.frameGeometry()  # 获得主窗口的一个矩形特定几何图形。这包含了窗口的框架。
        cp = QDesktopWidget().availableGeometry().center()  # 算出相对于显示器的绝对值。
        # 并且从这个绝对值中，我们获得了屏幕中心点。
        qr.moveCenter(cp)  # 矩形已经设置好了它的宽和高。现在我们把矩形的中心设置到屏幕的中间去。
        # 矩形的大小并不会改变。
        self.move(qr.topLeft())  # 移动了应用窗口的左上方的点到qr矩形的左上方的点，因此居中显示在我们的屏幕上。



if __name__=='__main__':
    #最简单的显示窗口
    #show_window()

    #提示文本
    # app = QApplication(sys.argv)
    # ex = PromptText()
    # sys.exit(app.exec_())

    #关闭窗口
    # app = QApplication(sys.argv)
    # ex = CloseW()
    # sys.exit(app.exec_())

    #提示消息框
    # app = QApplication(sys.argv)
    # ex = MessageBox()
    # sys.exit(app.exec_())

    #屏幕居中
    app = QApplication(sys.argv)
    ex = CenterW()
    sys.exit(app.exec_())

