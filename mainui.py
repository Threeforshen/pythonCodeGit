import sys
from PyQt5.QtWidgets import (QWidget, QToolTip, QDesktopWidget, QMessageBox,QTextEdit,QLabel,
    QPushButton, QApplication,QMainWindow, QAction, qApp, QHBoxLayout, QVBoxLayout,QGridLayout,
    QLineEdit,QMenu,QTextBrowser)
from PyQt5.QtGui import QFont,QIcon
from PyQt5.QtCore import QCoreApplication


class Main_UI_QMS(QMainWindow):
    def __init__(self):
        super().__init__()
        self.InitUI()

    def InitUI(self):
        self.statusBar().showMessage("Everything is ok！")
        self.setGeometry(100,100,1200,500)
        self.setWindowTitle('Manger for QMS')
        self.setStyleSheet("background-color:# F5F5F5")

        saveMenu = QMenu('保存方式(&S)', self)
        saveAct = QAction(QIcon('save.png'), '保存...', self)
        saveAct.setShortcut('Ctrl+S')
        saveAct.setStatusTip('保存文件')
        saveasAct = QAction(QIcon('saveas.png'), '另存为...(&O)', self)
        saveasAct.setStatusTip('文件另存为')
        saveMenu.addAction(saveAct)
        saveMenu.addAction(saveasAct)

        menubar = self.menuBar()
        fileMenu = menubar.addMenu('Start(&F)')
        fileMenu.addMenu(saveMenu)
        fileMenu.addSeparator()

        #label
        self.lb_today=QLabel('今天：',self)
        self.lb_today.move(50,30)

        self.qt_log=QTextBrowser()
        self.qt_log.resize(50,50)
        self.qt_log.move(100,300)
        self.qt_log.setFont(QFont("Microsoft YaHei"))
        self.qt_log.setStyleSheet("background-color:red")

        #btn
        self.btn_start_now_update=QPushButton(self)
        self.btn_start_now_update.setText('Update Now')#button内容
        #self.closeButton.setIcon(QIcon("close.png"))  # icon图标
        self.btn_start_now_update.move(100, 100)

        self.btn_start_interval_update = QPushButton('Interval Update', self)
        self.btn_start_interval_update.move(100,200)
        self.show()

        self.btn_start_now_update.clicked.connect(lambda :self.btn_update())
        self.btn_start_interval_update.clicked.connect(lambda: self.btn_update())

    def btn_update(self):
        sender = self.sender()
        if sender==self.btn_start_now_update:

            message="你好"
            self.qt_log.setText("122655")
            self.statusBar().showMessage('Now Updating!')

           # updateqmsdata()
        elif sender==self.btn_start_interval_update:
            self.statusBar().showMessage('Update for 15min')






if  __name__=='__main__':
    app=QApplication(sys.argv)
    muq=Main_UI_QMS()
    sys.exit(app.exec_())