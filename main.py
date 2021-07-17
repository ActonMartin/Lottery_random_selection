from PyQt5.QtWidgets import QApplication,QMainWindow
from ui.ui_ui import Ui_MainWindow
from PyQt5.QtGui import QIcon,QPalette,QBrush,QPixmap
import sys
import random
import time

class Lottery(QMainWindow):
    def __init__(self):
        super(Lottery, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowIcon(QIcon('ui/ico.png'))
        self.setWindowTitle("中国福利彩票")
        palette = QPalette()
        palette.setBrush(QPalette.Background, QBrush(QPixmap('ui/background.jpg')))
        self.setPalette(palette)
        self.ui.pushButton.clicked.connect(self.choose)
        self.ui.label.setStyleSheet("color:red")
        self.ui.label_2.setStyleSheet("color:red")
        self.ui.label_3.setStyleSheet("color:red")
        self.ui.label_4.setStyleSheet("color:red")
        self.ui.label_5.setStyleSheet("color:red")
        self.ui.label_6.setStyleSheet("color:red")
        self.ui.label_7.setStyleSheet("color:blue")

    def choose(self):
        start = time.time()
        while True:
            now = time.time()
            if now - start >= 2:
                break
            self.red_list = random.sample(range(1,34),6)
            self.red_list = sorted(self.red_list)
            self.blue_list = random.sample(range(1,17),1)
            a,b,c,d,e,f = self.red_list[0],self.red_list[1],self.red_list[2],self.red_list[3],self.red_list[4],self.red_list[5]
            g = self.blue_list[0]
            self.ui.label.setText(str(a))
            self.ui.label_2.setText(str(b))
            self.ui.label_3.setText(str(c))
            self.ui.label_4.setText(str(d))
            self.ui.label_5.setText(str(e))
            self.ui.label_6.setText(str(f))
            self.ui.label_7.setText(str(g))
            self.ui.label.repaint()
            self.ui.label_2.repaint()
            self.ui.label_3.repaint()
            self.ui.label_4.repaint()
            self.ui.label_5.repaint()
            self.ui.label_6.repaint()
            self.ui.label_7.repaint()


if __name__ == "__main__":
    App = QApplication(sys.argv)
    Windows = Lottery()
    Windows.show()
    sys.exit(App.exec_())