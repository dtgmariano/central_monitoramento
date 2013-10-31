# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created: Thu Oct 31 12:03:48 2013
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

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(800, 600)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.tabWidget = QtGui.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tabGroup = QtGui.QWidget()
        self.tabGroup.setObjectName(_fromUtf8("tabGroup"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.tabGroup)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        spacerItem = QtGui.QSpacerItem(362, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.widget = QtGui.QWidget(self.tabGroup)
        self.widget.setMinimumSize(QtCore.QSize(0, 0))
        self.widget.setObjectName(_fromUtf8("widget"))
        self.horizontalLayout.addWidget(self.widget)
        spacerItem1 = QtGui.QSpacerItem(362, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("icones/group.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabWidget.addTab(self.tabGroup, icon, _fromUtf8(""))
        self.tabPacient = QtGui.QWidget()
        self.tabPacient.setObjectName(_fromUtf8("tabPacient"))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8("icones/single.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabWidget.addTab(self.tabPacient, icon1, _fromUtf8(""))
        self.tabConfig = QtGui.QWidget()
        self.tabConfig.setObjectName(_fromUtf8("tabConfig"))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8("icones/settings.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabWidget.addTab(self.tabConfig, icon2, _fromUtf8(""))
        self.verticalLayout.addWidget(self.tabWidget)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 25))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuConexao = QtGui.QMenu(self.menubar)
        self.menuConexao.setObjectName(_fromUtf8("menuConexao"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.actionAbrir = QtGui.QAction(MainWindow)
        self.actionAbrir.setObjectName(_fromUtf8("actionAbrir"))
        self.actionFechar = QtGui.QAction(MainWindow)
        self.actionFechar.setEnabled(False)
        self.actionFechar.setObjectName(_fromUtf8("actionFechar"))
        self.menuConexao.addAction(self.actionAbrir)
        self.menuConexao.addAction(self.actionFechar)
        self.menubar.addAction(self.menuConexao.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "ICU Monitoring Center", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabGroup), _translate("MainWindow", "Monitors", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabPacient), _translate("MainWindow", "Patient", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabConfig), _translate("MainWindow", "Settings", None))
        self.menuConexao.setTitle(_translate("MainWindow", "Connection", None))
        self.actionAbrir.setText(_translate("MainWindow", "Open", None))
        self.actionFechar.setText(_translate("MainWindow", "Close", None))

