# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'subnetcalculator.ui'
#
# Created by: PyQt5 UI code generator 5.7
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_mainWindow(object):
    def setupUi(self, mainWindow):
        mainWindow.setObjectName("mainWindow")
        mainWindow.resize(701, 499)
        self.centralwidget = QtWidgets.QWidget(mainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(10, 10, 311, 111))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName("groupBox")
        self.labelSubnetSize = QtWidgets.QLabel(self.groupBox)
        self.labelSubnetSize.setGeometry(QtCore.QRect(155, 82, 141, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.labelSubnetSize.setFont(font)
        self.labelSubnetSize.setFrameShape(QtWidgets.QFrame.Box)
        self.labelSubnetSize.setText("")
        self.labelSubnetSize.setObjectName("labelSubnetSize")
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(12, 82, 152, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(12, 52, 148, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.lineEditHostsPerSubnet = QtWidgets.QLineEdit(self.groupBox)
        self.lineEditHostsPerSubnet.setGeometry(QtCore.QRect(156, 52, 141, 22))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEditHostsPerSubnet.setFont(font)
        self.lineEditHostsPerSubnet.setObjectName("lineEditHostsPerSubnet")
        self.lineEditNetworkAddress = QtWidgets.QLineEdit(self.groupBox)
        self.lineEditNetworkAddress.setGeometry(QtCore.QRect(125, 22, 171, 22))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEditNetworkAddress.setFont(font)
        self.lineEditNetworkAddress.setReadOnly(False)
        self.lineEditNetworkAddress.setObjectName("lineEditNetworkAddress")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(12, 22, 117, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 130, 311, 321))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_2.setFont(font)
        self.groupBox_2.setObjectName("groupBox_2")
        self.ListOfIPRanges = QtWidgets.QListWidget(self.groupBox_2)
        self.ListOfIPRanges.setGeometry(QtCore.QRect(10, 20, 291, 291))
        self.ListOfIPRanges.setObjectName("ListOfIPRanges")
        self.groupBox_3 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_3.setGeometry(QtCore.QRect(330, 10, 361, 121))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_3.setFont(font)
        self.groupBox_3.setObjectName("groupBox_3")
        self.labeHexOctets = QtWidgets.QLabel(self.groupBox_3)
        self.labeHexOctets.setGeometry(QtCore.QRect(84, 94, 271, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.labeHexOctets.setFont(font)
        self.labeHexOctets.setFrameShape(QtWidgets.QFrame.Box)
        self.labeHexOctets.setText("")
        self.labeHexOctets.setObjectName("labeHexOctets")
        self.label_7 = QtWidgets.QLabel(self.groupBox_3)
        self.label_7.setGeometry(QtCore.QRect(12, 94, 76, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.labelBinaryOctets = QtWidgets.QLabel(self.groupBox_3)
        self.labelBinaryOctets.setGeometry(QtCore.QRect(101, 70, 251, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.labelBinaryOctets.setFont(font)
        self.labelBinaryOctets.setFrameShape(QtWidgets.QFrame.Box)
        self.labelBinaryOctets.setText("")
        self.labelBinaryOctets.setObjectName("labelBinaryOctets")
        self.label_6 = QtWidgets.QLabel(self.groupBox_3)
        self.label_6.setGeometry(QtCore.QRect(12, 70, 93, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.labelDecimalAddress = QtWidgets.QLabel(self.groupBox_3)
        self.labelDecimalAddress.setGeometry(QtCore.QRect(120, 46, 231, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.labelDecimalAddress.setFont(font)
        self.labelDecimalAddress.setFrameShape(QtWidgets.QFrame.Box)
        self.labelDecimalAddress.setText("")
        self.labelDecimalAddress.setObjectName("labelDecimalAddress")
        self.label_5 = QtWidgets.QLabel(self.groupBox_3)
        self.label_5.setGeometry(QtCore.QRect(12, 46, 112, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_4 = QtWidgets.QLabel(self.groupBox_3)
        self.label_4.setGeometry(QtCore.QRect(12, 22, 101, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.labelDecimalOctets = QtWidgets.QLabel(self.groupBox_3)
        self.labelDecimalOctets.setGeometry(QtCore.QRect(109, 22, 241, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.labelDecimalOctets.setFont(font)
        self.labelDecimalOctets.setFrameShape(QtWidgets.QFrame.Box)
        self.labelDecimalOctets.setText("")
        self.labelDecimalOctets.setObjectName("labelDecimalOctets")
        self.groupBox_4 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_4.setGeometry(QtCore.QRect(340, 140, 351, 211))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_4.setFont(font)
        self.groupBox_4.setFlat(False)
        self.groupBox_4.setObjectName("groupBox_4")
        self.label_12 = QtWidgets.QLabel(self.groupBox_4)
        self.label_12.setGeometry(QtCore.QRect(12, 167, 88, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.labelNumberOSubnets = QtWidgets.QLabel(self.groupBox_4)
        self.labelNumberOSubnets.setGeometry(QtCore.QRect(96, 167, 251, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.labelNumberOSubnets.setFont(font)
        self.labelNumberOSubnets.setFrameShape(QtWidgets.QFrame.Box)
        self.labelNumberOSubnets.setText("")
        self.labelNumberOSubnets.setObjectName("labelNumberOSubnets")
        self.label_11 = QtWidgets.QLabel(self.groupBox_4)
        self.label_11.setGeometry(QtCore.QRect(12, 132, 83, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.labelBinaryMask = QtWidgets.QLabel(self.groupBox_4)
        self.labelBinaryMask.setGeometry(QtCore.QRect(90, 130, 251, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.labelBinaryMask.setFont(font)
        self.labelBinaryMask.setFrameShape(QtWidgets.QFrame.Box)
        self.labelBinaryMask.setText("")
        self.labelBinaryMask.setObjectName("labelBinaryMask")
        self.labelNumberOfIPAddress = QtWidgets.QLabel(self.groupBox_4)
        self.labelNumberOfIPAddress.setGeometry(QtCore.QRect(114, 62, 231, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.labelNumberOfIPAddress.setFont(font)
        self.labelNumberOfIPAddress.setFrameShape(QtWidgets.QFrame.Box)
        self.labelNumberOfIPAddress.setText("")
        self.labelNumberOfIPAddress.setObjectName("labelNumberOfIPAddress")
        self.label_9 = QtWidgets.QLabel(self.groupBox_4)
        self.label_9.setGeometry(QtCore.QRect(12, 62, 106, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.label_8 = QtWidgets.QLabel(self.groupBox_4)
        self.label_8.setGeometry(QtCore.QRect(12, 27, 96, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.labelNetworkClass = QtWidgets.QLabel(self.groupBox_4)
        self.labelNetworkClass.setGeometry(QtCore.QRect(104, 27, 241, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.labelNetworkClass.setFont(font)
        self.labelNetworkClass.setFrameShape(QtWidgets.QFrame.Box)
        self.labelNetworkClass.setText("")
        self.labelNetworkClass.setObjectName("labelNetworkClass")
        self.label_10 = QtWidgets.QLabel(self.groupBox_4)
        self.label_10.setGeometry(QtCore.QRect(12, 97, 88, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.labelSubnetMask = QtWidgets.QLabel(self.groupBox_4)
        self.labelSubnetMask.setGeometry(QtCore.QRect(96, 97, 251, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.labelSubnetMask.setFont(font)
        self.labelSubnetMask.setFrameShape(QtWidgets.QFrame.Box)
        self.labelSubnetMask.setText("")
        self.labelSubnetMask.setObjectName("labelSubnetMask")
        self.label_11.raise_()
        self.labelBinaryMask.raise_()
        self.labelNumberOfIPAddress.raise_()
        self.label_9.raise_()
        self.label_8.raise_()
        self.labelNetworkClass.raise_()
        self.label_10.raise_()
        self.labelSubnetMask.raise_()
        self.label_12.raise_()
        self.labelNumberOSubnets.raise_()
        self.pushButtonCalculate = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonCalculate.setGeometry(QtCore.QRect(570, 380, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButtonCalculate.setFont(font)
        self.pushButtonCalculate.setObjectName("pushButtonCalculate")
        mainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(mainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 701, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuTools = QtWidgets.QMenu(self.menubar)
        self.menuTools.setObjectName("menuTools")
        mainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(mainWindow)
        self.statusbar.setObjectName("statusbar")
        mainWindow.setStatusBar(self.statusbar)
        self.actionOpen = QtWidgets.QAction(mainWindow)
        self.actionOpen.setObjectName("actionOpen")
        self.actionSave_As = QtWidgets.QAction(mainWindow)
        self.actionSave_As.setObjectName("actionSave_As")
        self.actionCalculate = QtWidgets.QAction(mainWindow)
        self.actionCalculate.setObjectName("actionCalculate")
        self.actionClear = QtWidgets.QAction(mainWindow)
        self.actionClear.setObjectName("actionClear")
        self.actionExit = QtWidgets.QAction(mainWindow)
        self.actionExit.setObjectName("actionExit")
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionSave_As)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionExit)
        self.menuTools.addAction(self.actionCalculate)
        self.menuTools.addAction(self.actionClear)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuTools.menuAction())

        self.retranslateUi(mainWindow)
        QtCore.QMetaObject.connectSlotsByName(mainWindow)

    def retranslateUi(self, mainWindow):
        _translate = QtCore.QCoreApplication.translate
        mainWindow.setWindowTitle(_translate("mainWindow", "Subnet Calculator"))
        self.groupBox.setTitle(_translate("mainWindow", "Network Information"))
        self.label_3.setText(_translate("mainWindow", "Calculated Subnet Size:"))
        self.label_2.setText(_translate("mainWindow", "# of Hosts Per Subnet:"))
        self.label.setText(_translate("mainWindow", "Network Address:"))
        self.groupBox_2.setTitle(_translate("mainWindow", "List of IP Ranges"))
        self.groupBox_3.setTitle(_translate("mainWindow", "Address Informaton"))
        self.label_7.setText(_translate("mainWindow", "Hex Octets:"))
        self.label_6.setText(_translate("mainWindow", "Binary Octets:"))
        self.label_5.setText(_translate("mainWindow", "Decimal Address:"))
        self.label_4.setText(_translate("mainWindow", "Decimal Octets:"))
        self.groupBox_4.setTitle(_translate("mainWindow", "Netmask Information"))
        self.label_12.setText(_translate("mainWindow", "# of Subnets:"))
        self.label_11.setText(_translate("mainWindow", "Binary Mask:"))
        self.label_9.setText(_translate("mainWindow", "# of IP Address:"))
        self.label_8.setText(_translate("mainWindow", "Network Class:"))
        self.label_10.setText(_translate("mainWindow", "Subnet Mask:"))
        self.pushButtonCalculate.setText(_translate("mainWindow", "Calculate!"))
        self.menuFile.setTitle(_translate("mainWindow", "File"))
        self.menuTools.setTitle(_translate("mainWindow", "Tools"))
        self.actionOpen.setText(_translate("mainWindow", "Open"))
        self.actionOpen.setShortcut(_translate("mainWindow", "Ctrl+O"))
        self.actionSave_As.setText(_translate("mainWindow", "Save As.."))
        self.actionSave_As.setShortcut(_translate("mainWindow", "Ctrl+S"))
        self.actionCalculate.setText(_translate("mainWindow", "Calculate"))
        self.actionCalculate.setShortcut(_translate("mainWindow", "Ctrl+Shift+C"))
        self.actionClear.setText(_translate("mainWindow", "Clear"))
        self.actionClear.setShortcut(_translate("mainWindow", "Ctrl+Del"))
        self.actionExit.setText(_translate("mainWindow", "Exit"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    mainWindow = QtWidgets.QMainWindow()
    ui = Ui_mainWindow()
    ui.setupUi(mainWindow)
    mainWindow.show()
    sys.exit(app.exec_())

