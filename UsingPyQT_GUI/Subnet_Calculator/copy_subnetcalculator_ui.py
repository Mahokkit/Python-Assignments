import sys

from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox,QFileDialog, QAction

#ADD IMPORT STATEMENT FOR YOUR GENERATED UI.PY FILE HERE
import subnetcalculator_lib
import csv
import ipaddress


#CHANGE THE SECOND PARAMETER HERE TO MATCH YOUR GENERATED UI.PY FILE
class MyForm(QMainWindow, subnetcalculator_lib.Ui_mainWindow):
    NetworkAdd =[]
    totalHost = []
    ipRangeList = []
    InfoList = []
    unsavedChanges = False

        # DO NOT MODIFY THIS CODE
    def __init__(self, parent=None):
        super(MyForm, self).__init__(parent)
        self.setupUi(self)
        # END DO NOT MODIFY

        # ADD SLOTS HERE
        self.pushButtonCalculate.clicked.connect(self.calculate)
        self.actionCalculate.triggered.connect(self.calculate)
        self.actionClear.triggered.connect(self.EmptyGUI)
        self.actionOpen.triggered.connect(self.file_open)
        self.actionSave_As.triggered.connect(self.file_save)
        self.actionExit.triggered.connect(self.ExitSEEYOU)



    # ADD SLOT FUNCTIONS HERE
    def ExitSEEYOU(self):
        if self.unsavedChanges == False:
            reply = QMessageBox.question(self, "HEY!", "Do you want save first?", QMessageBox.Yes, QMessageBox.No)
        else:
            QApplication.closeAllWindows()

        if reply == QMessageBox.Yes:
            self.file_save()
            self.unsavedChanges = True
        else:
            QApplication.closeAllWindows()

    def file_open(self):
        self.InfoList = []
        fname = QFileDialog.getOpenFileName(self, 'Open file', '')
        print(list(fname))
        filename = list(fname)
        if filename[0] == '':
            QApplication.activeWindow()
        else:
            with open(filename[0], "r") as INPUT:
                DataList = csv.reader(INPUT)
                # loop through each line in reader...each line is a list of values
                for x in DataList:
                    # add each list to the people list variable declared above
                    self.InfoList.append(x)
            NetworkAddress = str(self.InfoList[0][0])
            HostPerSubNet = str(self.InfoList[1][0])
            self.lineEditNetworkAddress.setText(NetworkAddress)
            self.lineEditHostsPerSubnet.setText(HostPerSubNet)
            self.calculate()

    def file_save(self):
        self.unsavedChanges = True
        fname = QFileDialog.getSaveFileName(self, 'Save file as', '')
        filename = list(fname)
        if filename[0] == '':
            QApplication.activeWindow()
        else:
            with open(filename[0], "w") as OUTPUT:
                OUTPUT.write(self.lineEditNetworkAddress.text()+"\n")
                OUTPUT.write(self.lineEditHostsPerSubnet.text() + "\n")
                OUTPUT.write(self.labelSubnetSize.text() + "\n")
                OUTPUT.write(self.labelDecimalOctets.text() + "\n")
                OUTPUT.write(self.labelDecimalAddress.text() + "\n")
                OUTPUT.write(self.labelBinaryOctets.text() + "\n")
                OUTPUT.write(self.labeHexOctets.text() + "\n")
                OUTPUT.write(self.labelNetworkClass.text() + "\n")
                OUTPUT.write(self.labelNumberOfIPAddress.text() + "\n")
                OUTPUT.write(self.labelSubnetMask.text() + "\n")
                OUTPUT.write(self.labelBinaryMask.text() + "\n")
                OUTPUT.write(self.labelNumberOSubnets.text() + "\n")
                for x in self.ipRangeList:
                    OUTPUT.write(x + "\n")

    def EmptyGUI(self):
        self.lineEditNetworkAddress.clear()
        self.lineEditHostsPerSubnet.clear()
        self.labelSubnetSize.clear()
        self.ListOfIPRanges.clear()
        self.labelDecimalOctets.clear()
        self.labelDecimalAddress.clear()
        self.labelBinaryOctets.clear()
        self.labelNetworkClass.clear()
        self.labelNumberOfIPAddress.clear()
        self.labelSubnetMask.clear()
        self.labelBinaryMask.clear()
        self.labelNumberOSubnets.clear()
        self.labeHexOctets.clear()

    def calculate(self):
        ip = self.lineEditNetworkAddress.text()
        self.labelDecimalOctets.setText(ip)
        numberOfHost = self.lineEditHostsPerSubnet.text()
        NetworkAdd = (ip.split("."))
        if NetworkAdd[0].isdigit() and NetworkAdd[1].isdigit() and NetworkAdd[2].isdigit() and NetworkAdd[3].isdigit():
            if int(NetworkAdd[0]) < 255 and int(NetworkAdd[1]) < 255 and int(NetworkAdd[2]) < 255 and int(NetworkAdd[3]) < 255:
                if numberOfHost.isdigit():
                    self.AddInfo()
                else:
                    QMessageBox.information(self, "ERROR", "Invalid Number of Host!", QMessageBox.Ok)
                    self.lineEditHostsPerSubnet.clear()
            else:
                QMessageBox.information(self, "ERROR", "Invalid IPv4 Address!", QMessageBox.Ok)
                self.lineEditNetworkAddress.clear()
        else:
            QMessageBox.information(self, "ERROR", "Invalid IPv4 Address!", QMessageBox.Ok)
            self.lineEditNetworkAddress.clear()

    #ADD HELPER FUNCTIONS HERE

    def AddInfo(self):
        ip = self.lineEditNetworkAddress.text()
        self.labelDecimalOctets.setText(ip)
        numberOfHost = self.lineEditHostsPerSubnet.text()
        NetworkAdd = (ip.split("."))
        decimal1 = int(NetworkAdd[0]) * (256**3)
        decimal2 = int(NetworkAdd[1]) * (256**2)
        decimal3 = int(NetworkAdd[2]) * (256)
        decimal4 = int(NetworkAdd[3])
        decimal_equivalent = decimal1 + decimal2 + decimal3 + decimal4
        decimal_equivalent = str(decimal_equivalent)
        self.labelDecimalAddress.setText(decimal_equivalent)

        binOctet1 = '{0:08b}'.format(int(NetworkAdd[0]))
        binOctet2 = '{0:08b}'.format(int(NetworkAdd[1]))
        binOctet3 = '{0:08b}'.format(int(NetworkAdd[2]))
        binOctet4 = '{0:08b}'.format(int(NetworkAdd[3]))
        binOctet = binOctet1+"."+binOctet2+"."+binOctet3+"."+binOctet4
        self.labelBinaryOctets.setText(binOctet)

        hex1 = hex(int(NetworkAdd[0]))[2:].zfill(2).upper()
        hex2 = hex(int(NetworkAdd[1]))[2:].zfill(2).upper()
        hex3 = hex(int(NetworkAdd[2]))[2:].zfill(2).upper()
        hex4 = hex(int(NetworkAdd[3]))[2:].zfill(2).upper()
        TOTALHEX = hex1+"."+hex2+"."+hex3+"."+hex4
        self.labeHexOctets.setText(TOTALHEX)

        if int(NetworkAdd[0]) >= 0 and int(NetworkAdd[0]) <= 127:
            if int(numberOfHost) <= 16277214:
                self.labelNetworkClass.setText("Class A")
                numberOfIP = 2**24
                numberOfIP = str(numberOfIP)
                self.labelNumberOfIPAddress.setText(numberOfIP)
                self.SubnetCalClassA()
            else:
                QMessageBox.information(self, "ERROR", "Number of Host is too big for this IP Class!", QMessageBox.Ok)
                self.lineEditHostsPerSubnet.clear()
        elif int(NetworkAdd[0]) >= 128 and int(NetworkAdd[0]) <= 191:
            if int(numberOfHost) <= 65534:
                self.labelNetworkClass.setText("Class B")
                numberOfIP = 2 **16
                numberOfIP = str(numberOfIP)
                self.SubnetCalClassB()
                self.labelNumberOfIPAddress.setText(numberOfIP)
            else:
                QMessageBox.information(self, "ERROR", "Number of Host is too big for this IP Class!", QMessageBox.Ok)
                self.lineEditHostsPerSubnet.clear()

        elif int(NetworkAdd[0]) >= 192 and int(NetworkAdd[0]) <= 223:
            if int(numberOfHost) <= 254:
                self.labelNetworkClass.setText("Class C")
                numberOfIP = 2 ** 8
                numberOfIP = str(numberOfIP)
                self.labelNumberOfIPAddress.setText(numberOfIP)
                self.SubnetCalClassC()
            else:
                QMessageBox.information(self, "ERROR", "Number of Host is too big for this IP Class!", QMessageBox.Ok)
                self.lineEditHostsPerSubnet.clear()
        else:
            QMessageBox.information(self, "ERROR", "You must enter a Valid Class A, B or C IP Address!", QMessageBox.Ok)
            self.lineEditNetworkAddress.clear()

    def SubnetCalClassA(self):
        ip = self.lineEditNetworkAddress.text()
        numberOfHost = self.lineEditHostsPerSubnet.text()
        numberOfHost = int(numberOfHost)
        for i in range(36):  # total bits
            self.hostPerBit = 2 ** i
            self.totalHost.append(self.hostPerBit)
            if numberOfHost < self.hostPerBit:
                maskBits = i
                netBlocks = self.hostPerBit / 256
                bitsUsed = netBlocks - maskBits
                HostPerBit = str(self.hostPerBit)
                self.numberOfSubnet = 2 ** (24 - maskBits)
                NumberOfSubnet = str(self.numberOfSubnet)
                self.CIDR = 32 - maskBits
                self.labelSubnetSize.setText(HostPerBit)
                self.labelNumberOSubnets.setText(NumberOfSubnet)
                break
        self.TheMasks()

        self.ListOfIPRanges.clear()
        newip = self.lineEditNetworkAddress.text()
        hostbit = self.labelSubnetSize.text()
        hostbit = int(hostbit)
        for ip in range(0, self.numberOfSubnet):
            data = (str(ipaddress.ip_address(newip)) + "-" + str((ipaddress.ip_address(newip) + (hostbit - 1))))
            newip = (ipaddress.ip_address(newip) + hostbit)
            self.ipRangeList.append(data)
            self.ListOfIPRanges.addItem(data)
        #self.ListOfIPRanges()

    def SubnetCalClassB(self):
        ip = self.lineEditNetworkAddress.text()
        numberOfHost = self.lineEditHostsPerSubnet.text()
        numberOfHost = int(numberOfHost)
        for i in range(36):  # total bits
            self.hostPerBit = 2 ** i
            self.totalHost.append(self.hostPerBit)
            if numberOfHost < self.hostPerBit:
                maskBits = i
                netBlocks = self.hostPerBit / 256
                bitsUsed = netBlocks - maskBits
                hostPerBit = str(self.hostPerBit)
                self.numberOfSubnet = 2 ** (16 - maskBits)
                NumberOfSubnet = str(self.numberOfSubnet)
                self.CIDR = 32 - maskBits
                self.labelSubnetSize.setText(hostPerBit)
                self.labelNumberOSubnets.setText(NumberOfSubnet)
                break
        self.TheMasks()

        self.ListOfIPRanges.clear()
        newip = self.lineEditNetworkAddress.text()
        hostbit = self.labelSubnetSize.text()
        hostbit = int(hostbit)
        for ip in range(0, self.numberOfSubnet):
            data = (str(ipaddress.ip_address(newip)) + "-" + str((ipaddress.ip_address(newip) + (hostbit - 1))))
            newip = (ipaddress.ip_address(newip) + hostbit)
            self.ipRangeList.append(data)
            self.ListOfIPRanges.addItem(data)
        #self.ListOfIPRanges()

    def SubnetCalClassC(self):
        ip = self.lineEditNetworkAddress.text()
        numberOfHost = self.lineEditHostsPerSubnet.text()
        numberOfHost = int(numberOfHost)
        for i in range(36):  # total bits
            self.hostPerBit = 2 ** i
            self.totalHost.append(self.hostPerBit)
            if numberOfHost < self.hostPerBit:
                maskBits = i
                netBlocks = self.hostPerBit / 256
                bitsUsed = netBlocks - maskBits
                hostPerBit = str(self.hostPerBit)
                self.numberOfSubnet = 2 ** (8 - maskBits)
                NumberOfSubnet = str(self.numberOfSubnet)
                self.CIDR = 32 - maskBits
                self.labelSubnetSize.setText(hostPerBit)
                self.labelNumberOSubnets.setText(NumberOfSubnet)
                break
        self.TheMasks()

        self.ListOfIPRanges.clear()
        newip = self.lineEditNetworkAddress.text()
        hostbit = self.labelSubnetSize.text()
        hostbit = int(hostbit)
        for ip in range(0, self.numberOfSubnet):
            data = (str(ipaddress.ip_address(newip)) + "-" + str((ipaddress.ip_address(newip) + (hostbit - 1))))
            newip = (ipaddress.ip_address(newip) + hostbit)
            self.ipRangeList.append(data)
            self.ListOfIPRanges.addItem(data)
        #self.ListOfIPRanges()

    """
    def ListOfIPRanges(self):
        self.ListOfIPRanges.clear()
        newip = self.lineEditNetworkAddress.text()
        hostbit = self.labelSubnetSize.text()
        hostbit = int(hostbit)
        for ip in range(0, self.numberOfSubnet):
            data = (str(ipaddress.ip_address(newip)) + "-" + str((ipaddress.ip_address(newip) + (hostbit - 1))))
            newip = (ipaddress.ip_address(newip) + hostbit)
            self.ipRangeList.append(data)
            self.ListOfIPRanges.addItem(data)

    """


    def TheMasks(self):
        self.labelSubnetMask.clear()
        self.labelBinaryMask.clear()
        ip = self.lineEditNetworkAddress.text()
        ipCIDR = ip + "/" + str(self.CIDR)
        network = ipaddress.ip_network('{}'.format(ipCIDR))
        netmask = network.netmask
        netmaskString = str(netmask) + " or /" + str(self.CIDR)
        self.labelSubnetMask.setText(netmaskString)

        binMask = str(netmask).split(".")
        binMask1 = '{0:08b}'.format(int(binMask[0]))
        binMask2 = '{0:08b}'.format(int(binMask[1]))
        binMask3 = '{0:08b}'.format(int(binMask[2]))
        binMask4 = '{0:08b}'.format(int(binMask[3]))

        binMaskCombine = binMask1 + "." + binMask2 + "." + binMask3 + "." + binMask4
        self.labelBinaryMask.setText(binMaskCombine)

# DO NOT MODIFY THIS CODE
if __name__ == "__main__":
    app = QApplication(sys.argv)
    the_form = MyForm()
    the_form.show()
    sys.exit(app.exec_())
# END DO NOT MODIFY
