
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox
from test2 import Ui_MainWindow


class mywindow(QtWidgets.QMainWindow, Ui_MainWindow):
      def __init__(self):
          super(mywindow, self).__init__()
          self.setupUi(self)
          self.comlist = ["COM1", "COM2", "COM3", "COM4", "COM5", "COM6"]
          for i in self.comlist:
              self.comboBox.addItem(i)
          self.radioButton.setChecked(True)
      def connectdev(self):
          if self.radioButton.isChecked():
              print("Connecting with serial.....")
              com = self.comboBox.currentText()
              print(com)
              ptr = self.lineEdit.text()
              if ptr.isdigit():
                 reply = QMessageBox.information(
                      self,
                      "Connect dev:",
                      ptr,
                      QMessageBox.Yes
                      )
              else: reply = QMessageBox.information(self,"Warnning", "设备ID只能是数字！", QMessageBox.Yes)
          elif self.radioButton_2.isChecked():
              print("该功能没上线")
              reply = QMessageBox.information(
                  self,
                  "网络连接功能",
                  "远程连接功能尚在完善中。。。。",
                  QMessageBox.Yes
              )
          else:
              print(" 请选择一种连接方式")
              reply = QMessageBox.information(
                  self,
                  "Warnning",
                  "请选择其中一种连接方式！",
                  QMessageBox.Yes
              )




if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui=mywindow()
    ui.show()

    sys.exit(app.exec_())


