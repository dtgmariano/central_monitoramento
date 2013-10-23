# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'monitgui.ui'
#
# Created: Wed Oct 23 19:17:24 2013
#      by: PyQt4 UI code generator 4.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_MonitForm(object):
    def setupUi(self, MonitForm):
        MonitForm.setObjectName(_fromUtf8("MonitForm"))
        MonitForm.resize(699, 206)
        self.lblBpm = QtGui.QLabel(MonitForm)
        self.lblBpm.setGeometry(QtCore.QRect(630, 40, 66, 17))
        self.lblBpm.setObjectName(_fromUtf8("lblBpm"))
        self.lblSpo = QtGui.QLabel(MonitForm)
        self.lblSpo.setGeometry(QtCore.QRect(630, 70, 66, 17))
        self.lblSpo.setObjectName(_fromUtf8("lblSpo"))
        self.graphicsView = PlotWidget(MonitForm)
        self.graphicsView.setGeometry(QtCore.QRect(10, 10, 611, 192))
        self.graphicsView.setObjectName(_fromUtf8("graphicsView"))

        self.retranslateUi(MonitForm)
        QtCore.QMetaObject.connectSlotsByName(MonitForm)

    def retranslateUi(self, MonitForm):
        MonitForm.setWindowTitle(QtGui.QApplication.translate("MonitForm", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.lblBpm.setText(QtGui.QApplication.translate("MonitForm", "TextLabel", None, QtGui.QApplication.UnicodeUTF8))
        self.lblSpo.setText(QtGui.QApplication.translate("MonitForm", "TextLabel", None, QtGui.QApplication.UnicodeUTF8))

from pyqtgraph import PlotWidget
