from PyQt4.QtCore import *
from PyQt4.QtGui import *
from config_gui import Ui_Form

class ConfigForm(QWidget):
	def __init__(self, parent = None):
		super(ConfigForm,self).__init__(parent)
		self.ui = Ui_Form()
		self.ui.setupUi(self)