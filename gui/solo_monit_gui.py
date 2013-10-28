# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'solo_monitor.ui'
#
# Created: Mon Oct 28 16:51:43 2013
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
        self.lbFC = QtGui.QLabel(self.parametrosPanel)
        self.lbFC.setMinimumSize(QtCore.QSize(150, 0))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.lbFC.setFont(font)
        self.lbFC.setStyleSheet(_fromUtf8("color: rgb(217, 41, 43);"))
        self.lbFC.setAlignment(QtCore.Qt.AlignCenter)
        self.lbFC.setMargin(10)
        self.lbFC.setObjectName(_fromUtf8("lbFC"))
        self.horizontalLayout.addWidget(self.lbFC)
        self.lbO2 = QtGui.QLabel(self.parametrosPanel)
        self.lbO2.setMinimumSize(QtCore.QSize(150, 0))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.lbO2.setFont(font)
        self.lbO2.setStyleSheet(_fromUtf8("color: rgb(68, 21, 222);"))
        self.lbO2.setAlignment(QtCore.Qt.AlignCenter)
        self.lbO2.setMargin(10)
        self.lbO2.setObjectName(_fromUtf8("lbO2"))
        self.horizontalLayout.addWidget(self.lbO2)
        self.lbPressao = QtGui.QLabel(self.parametrosPanel)
        self.lbPressao.setMinimumSize(QtCore.QSize(150, 0))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.lbPressao.setFont(font)
        self.lbPressao.setStyleSheet(_fromUtf8("color: rgb(245, 232, 46);"))
        self.lbPressao.setAlignment(QtCore.Qt.AlignCenter)
        self.lbPressao.setMargin(10)
        self.lbPressao.setObjectName(_fromUtf8("lbPressao"))
        self.horizontalLayout.addWidget(self.lbPressao)
        self.lbTemperatura = QtGui.QLabel(self.parametrosPanel)
        self.lbTemperatura.setMinimumSize(QtCore.QSize(150, 0))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.lbTemperatura.setFont(font)
        self.lbTemperatura.setStyleSheet(_fromUtf8("color: rgb(0, 170, 0);"))
        self.lbTemperatura.setAlignment(QtCore.Qt.AlignCenter)
        self.lbTemperatura.setMargin(10)
        self.lbTemperatura.setObjectName(_fromUtf8("lbTemperatura"))
        self.horizontalLayout.addWidget(self.lbTemperatura)
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
        self.lbFC.setText(QtGui.QApplication.translate("SoloMonitForm", "fc: 120 bpm", None, QtGui.QApplication.UnicodeUTF8))
        self.lbO2.setText(QtGui.QApplication.translate("SoloMonitForm", "spo2: 98%", None, QtGui.QApplication.UnicodeUTF8))
        self.lbPressao.setText(QtGui.QApplication.translate("SoloMonitForm", "nibp: 120/80", None, QtGui.QApplication.UnicodeUTF8))
        self.lbTemperatura.setText(QtGui.QApplication.translate("SoloMonitForm", "temp: 36,5 ºC", None, QtGui.QApplication.UnicodeUTF8))
        self.btnalarm.setText(QtGui.QApplication.translate("SoloMonitForm", "Alarmes Individuais", None, QtGui.QApplication.UnicodeUTF8))

from pyqtgraph import PlotWidget
