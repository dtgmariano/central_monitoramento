# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'solo_monitor.ui'
#
# Created: Fri Oct 25 21:07:20 2013
#      by: PyQt4 UI code generator 4.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_SoloMonitForm(object):
    def setupUi(self, SoloMonitForm):
        SoloMonitForm.setObjectName(_fromUtf8("SoloMonitForm"))
        SoloMonitForm.resize(694, 506)
        self.verticalLayout_3 = QtGui.QVBoxLayout(SoloMonitForm)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.parametrosPanel = QtGui.QWidget(SoloMonitForm)
        self.parametrosPanel.setStyleSheet(_fromUtf8(""))
        self.parametrosPanel.setObjectName(_fromUtf8("parametrosPanel"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.parametrosPanel)
        self.verticalLayout_2.setMargin(0)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.ecgchart = PlotWidget(self.parametrosPanel)
        self.ecgchart.setObjectName(_fromUtf8("ecgchart"))
        self.verticalLayout_2.addWidget(self.ecgchart)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.lblbpm = QtGui.QLabel(self.parametrosPanel)
        self.lblbpm.setMinimumSize(QtCore.QSize(150, 0))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.lblbpm.setFont(font)
        self.lblbpm.setAlignment(QtCore.Qt.AlignCenter)
        self.lblbpm.setMargin(10)
        self.lblbpm.setObjectName(_fromUtf8("lblbpm"))
        self.horizontalLayout.addWidget(self.lblbpm)
        self.lblspo = QtGui.QLabel(self.parametrosPanel)
        self.lblspo.setMinimumSize(QtCore.QSize(150, 0))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.lblspo.setFont(font)
        self.lblspo.setAlignment(QtCore.Qt.AlignCenter)
        self.lblspo.setMargin(10)
        self.lblspo.setObjectName(_fromUtf8("lblspo"))
        self.horizontalLayout.addWidget(self.lblspo)
        self.lblnibp = QtGui.QLabel(self.parametrosPanel)
        self.lblnibp.setMinimumSize(QtCore.QSize(150, 0))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.lblnibp.setFont(font)
        self.lblnibp.setAlignment(QtCore.Qt.AlignCenter)
        self.lblnibp.setMargin(10)
        self.lblnibp.setObjectName(_fromUtf8("lblnibp"))
        self.horizontalLayout.addWidget(self.lblnibp)
        self.lbltemp = QtGui.QLabel(self.parametrosPanel)
        self.lbltemp.setMinimumSize(QtCore.QSize(150, 0))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.lbltemp.setFont(font)
        self.lbltemp.setAlignment(QtCore.Qt.AlignCenter)
        self.lbltemp.setMargin(10)
        self.lbltemp.setObjectName(_fromUtf8("lbltemp"))
        self.horizontalLayout.addWidget(self.lbltemp)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.verticalLayout_3.addWidget(self.parametrosPanel)
        self.horizontalLayout_6 = QtGui.QHBoxLayout()
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
        self.btnalarm = QtGui.QPushButton(SoloMonitForm)
        self.btnalarm.setEnabled(True)
        self.btnalarm.setObjectName(_fromUtf8("btnalarm"))
        self.horizontalLayout_6.addWidget(self.btnalarm)
        self.verticalLayout_3.addLayout(self.horizontalLayout_6)
        self.alarmePanel = QtGui.QWidget(SoloMonitForm)
        self.alarmePanel.setObjectName(_fromUtf8("alarmePanel"))
        self.verticalLayout_3.addWidget(self.alarmePanel)

        self.retranslateUi(SoloMonitForm)
        QtCore.QMetaObject.connectSlotsByName(SoloMonitForm)

    def retranslateUi(self, SoloMonitForm):
        SoloMonitForm.setWindowTitle(QtGui.QApplication.translate("SoloMonitForm", "Monitor de Sinais Vitais", None, QtGui.QApplication.UnicodeUTF8))
        self.lblbpm.setText(QtGui.QApplication.translate("SoloMonitForm", "fc: 120 bpm", None, QtGui.QApplication.UnicodeUTF8))
        self.lblspo.setText(QtGui.QApplication.translate("SoloMonitForm", "spo2: 98%", None, QtGui.QApplication.UnicodeUTF8))
        self.lblnibp.setText(QtGui.QApplication.translate("SoloMonitForm", "nibp: 120/80", None, QtGui.QApplication.UnicodeUTF8))
        self.lbltemp.setText(QtGui.QApplication.translate("SoloMonitForm", "temp: 36,5 ºC", None, QtGui.QApplication.UnicodeUTF8))
        self.btnalarm.setText(QtGui.QApplication.translate("SoloMonitForm", "Alarmes Individuais", None, QtGui.QApplication.UnicodeUTF8))

from pyqtgraph import PlotWidget
