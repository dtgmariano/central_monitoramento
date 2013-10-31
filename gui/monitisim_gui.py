# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'monitsim.ui'
#
# Created: Thu Oct 31 11:39:55 2013
#      by: PyQt4 UI code generator 4.10.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MonitSimForm(object):
    def setupUi(self, MonitSimForm):
        MonitSimForm.setObjectName(_fromUtf8("MonitSimForm"))
        MonitSimForm.resize(636, 288)
        self.horizontalLayout_2 = QtGui.QHBoxLayout(MonitSimForm)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.ecgChart = PlotWidget(MonitSimForm)
        self.ecgChart.setObjectName(_fromUtf8("ecgChart"))
        self.horizontalLayout.addWidget(self.ecgChart)
        self.horizontalLayout_2.addLayout(self.horizontalLayout)
        self.glMonitor = QtGui.QGridLayout()
        self.glMonitor.setObjectName(_fromUtf8("glMonitor"))
        self.imgPaciente = QtGui.QLabel(MonitSimForm)
        self.imgPaciente.setMaximumSize(QtCore.QSize(32, 32))
        self.imgPaciente.setText(_fromUtf8(""))
        self.imgPaciente.setPixmap(QtGui.QPixmap(_fromUtf8("icones/img_paciente.png")))
        self.imgPaciente.setObjectName(_fromUtf8("imgPaciente"))
        self.glMonitor.addWidget(self.imgPaciente, 1, 0, 1, 1)
        self.imgMonitor = QtGui.QLabel(MonitSimForm)
        self.imgMonitor.setMaximumSize(QtCore.QSize(32, 32))
        self.imgMonitor.setText(_fromUtf8(""))
        self.imgMonitor.setPixmap(QtGui.QPixmap(_fromUtf8("icones/img_monitor1.png")))
        self.imgMonitor.setObjectName(_fromUtf8("imgMonitor"))
        self.glMonitor.addWidget(self.imgMonitor, 0, 0, 1, 1)
        self.lbPressao = QtGui.QLabel(MonitSimForm)
        self.lbPressao.setMaximumSize(QtCore.QSize(120, 32))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.lbPressao.setFont(font)
        self.lbPressao.setObjectName(_fromUtf8("lbPressao"))
        self.glMonitor.addWidget(self.lbPressao, 2, 1, 1, 1)
        self.imgPressao = QtGui.QLabel(MonitSimForm)
        self.imgPressao.setMaximumSize(QtCore.QSize(32, 32))
        self.imgPressao.setText(_fromUtf8(""))
        self.imgPressao.setPixmap(QtGui.QPixmap(_fromUtf8("icones/pressao.png")))
        self.imgPressao.setObjectName(_fromUtf8("imgPressao"))
        self.glMonitor.addWidget(self.imgPressao, 2, 0, 1, 1)
        self.lbO2 = QtGui.QLabel(MonitSimForm)
        self.lbO2.setMaximumSize(QtCore.QSize(120, 32))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.lbO2.setFont(font)
        self.lbO2.setObjectName(_fromUtf8("lbO2"))
        self.glMonitor.addWidget(self.lbO2, 3, 1, 1, 1)
        self.lbPaciente = QtGui.QLabel(MonitSimForm)
        self.lbPaciente.setMaximumSize(QtCore.QSize(120, 32))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.lbPaciente.setFont(font)
        self.lbPaciente.setObjectName(_fromUtf8("lbPaciente"))
        self.glMonitor.addWidget(self.lbPaciente, 1, 1, 1, 1)
        self.imgO2 = QtGui.QLabel(MonitSimForm)
        self.imgO2.setMaximumSize(QtCore.QSize(32, 32))
        self.imgO2.setText(_fromUtf8(""))
        self.imgO2.setPixmap(QtGui.QPixmap(_fromUtf8("icones/spo.png")))
        self.imgO2.setObjectName(_fromUtf8("imgO2"))
        self.glMonitor.addWidget(self.imgO2, 3, 0, 1, 1)
        self.lbFC = QtGui.QLabel(MonitSimForm)
        self.lbFC.setMaximumSize(QtCore.QSize(120, 32))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.lbFC.setFont(font)
        self.lbFC.setTextFormat(QtCore.Qt.RichText)
        self.lbFC.setObjectName(_fromUtf8("lbFC"))
        self.glMonitor.addWidget(self.lbFC, 5, 1, 1, 1)
        self.lbTemperatura = QtGui.QLabel(MonitSimForm)
        self.lbTemperatura.setMaximumSize(QtCore.QSize(120, 32))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.lbTemperatura.setFont(font)
        self.lbTemperatura.setObjectName(_fromUtf8("lbTemperatura"))
        self.glMonitor.addWidget(self.lbTemperatura, 4, 1, 1, 1)
        self.imgTemperatura = QtGui.QLabel(MonitSimForm)
        self.imgTemperatura.setMaximumSize(QtCore.QSize(32, 32))
        self.imgTemperatura.setText(_fromUtf8(""))
        self.imgTemperatura.setPixmap(QtGui.QPixmap(_fromUtf8("icones/temp.png")))
        self.imgTemperatura.setObjectName(_fromUtf8("imgTemperatura"))
        self.glMonitor.addWidget(self.imgTemperatura, 4, 0, 1, 1)
        self.imgFC = QtGui.QLabel(MonitSimForm)
        self.imgFC.setMaximumSize(QtCore.QSize(32, 32))
        self.imgFC.setText(_fromUtf8(""))
        self.imgFC.setPixmap(QtGui.QPixmap(_fromUtf8("icones/fc.png")))
        self.imgFC.setObjectName(_fromUtf8("imgFC"))
        self.glMonitor.addWidget(self.imgFC, 5, 0, 1, 1)
        self.lbMonitor = QtGui.QLabel(MonitSimForm)
        self.lbMonitor.setMaximumSize(QtCore.QSize(120, 16777215))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.lbMonitor.setFont(font)
        self.lbMonitor.setObjectName(_fromUtf8("lbMonitor"))
        self.glMonitor.addWidget(self.lbMonitor, 0, 1, 1, 1)
        self.horizontalLayout_2.addLayout(self.glMonitor)

        self.retranslateUi(MonitSimForm)
        QtCore.QMetaObject.connectSlotsByName(MonitSimForm)

    def retranslateUi(self, MonitSimForm):
        MonitSimForm.setWindowTitle(_translate("MonitSimForm", "ICU Monitor Simulator", None))
        self.lbPressao.setText(_translate("MonitSimForm", "000/00 mmmHG", None))
        self.lbO2.setText(_translate("MonitSimForm", "00 %", None))
        self.lbPaciente.setText(_translate("MonitSimForm", "<html><head/><body><p>John Doo</p></body></html>", None))
        self.lbFC.setText(_translate("MonitSimForm", "<html><head/><body><p>00 BPM</p></body></html>", None))
        self.lbTemperatura.setText(_translate("MonitSimForm", "<html><head/><body><p>00 <span style=\" vertical-align:super;\">o</span>C</p></body></html>", None))
        self.lbMonitor.setText(_translate("MonitSimForm", "<html><head/><body><p>01</p></body></html>", None))

from pyqtgraph import PlotWidget
