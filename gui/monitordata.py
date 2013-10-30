from PyQt4.QtCore import *
from PyQt4.QtGui import *
from monitordata_gui import Ui_Form
                
class MyMonitor(QWidget):
        def __init__(self, parent = None):
                super(MyMonitor, self).__init__(parent)
                self.ui = Ui_Form()
                self.ui.setupUi(self)
                self.controller = None
                
        def conecta(self, mainWindow, controller):
                self.controller = controller
                self.ui.lbPaciente.setCursor(QCursor(Qt.PointingHandCursor))
                self.ui.lbPaciente.mousePressEvent = lambda event: self.ui.lbPaciente.emit(SIGNAL("clicked()"))
                QObject.connect(self.ui.lbPaciente, SIGNAL('clicked()'), lambda fonte = self: mainWindow.trocaControle(fonte))


if __name__ == "__main__":
        import sys
        app = QApplication(sys.argv)
        frm = MyMonitor()
        frm.show()
        app.exec_()
