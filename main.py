import sys


from PyQt5.QtWidgets import QApplication, QMainWindow



if __name__ == '__main__':
    # 创建QApplication对象
    app = QApplication(sys.argv)
    # 创建窗口对象
    w = QMainWindow()
    # 设置窗口尺寸
    w.resize(300, 200)
    # 移动窗口
    w.move(300, 300)
    # 设置窗口标题
    w.setWindowTitle('窗口')

    w.show()

    # 进入主循环
    sys.exit(app.exec_())