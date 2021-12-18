import sys
from PyQt5.QtWidgets import QApplication, QWidget

if __name__ == "__main__":
    app=QApplication(sys.argv)
    w=QWidget()
    w.resize(800,600) # 窗体的大小
    w.move(1000,1000) # 窗体的位置
    w.setWindowTitle("this is my first Desktop App base on PyQt5.")
    w.show()
    app.exit(app.exec_())
