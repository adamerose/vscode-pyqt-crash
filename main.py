from PyQt5 import QtCore, QtGui, QtWidgets
app = QtWidgets.QApplication([])
app.setWindowIcon(QtGui.QIcon("icon.png"))
window = QtWidgets.QMainWindow()
window.show()
app.exec_()
