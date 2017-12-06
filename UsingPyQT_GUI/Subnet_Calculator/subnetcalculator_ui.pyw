"""
Author: Edward Ma
Template given by: Geoff Gillespie
PROG-1102 FINAL PROJECT
December 11, 2016
"""



import sys

from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox,QFileDialog

#ADD IMPORT STATEMENT FOR YOUR GENERATED UI.PY FILE HERE
import subnetcalculator_lib
import csv #needed for file save and open
import ipaddress #for easy IP Address calculation


#CHANGE THE SECOND PARAMETER HERE TO MATCH YOUR GENERATED UI.PY FILE
class MyForm(QMainWindow, subnetcalculator_lib.Ui_mainWindow):
    #Global Variables which I will need later for my calculation!
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
        """
        when user click the calculate button or
        select Calculate from the menu, it will go to the Calculate function
        """
        self.pushButtonCalculate.clicked.connect(self.calculate)
        self.actionCalculate.triggered.connect(self.calculate)
        """
        when user select Clear from the menu, it will go to the EmptyGUI function, and clear everything!
        """
        self.actionClear.triggered.connect(self.EmptyGUI)
        """
        when user select open or Save As from the file menu, it will go to it's appropriate function
        """
        self.actionOpen.triggered.connect(self.file_open)
        self.actionSave_As.triggered.connect(self.file_save)
        """
        let user exit the program, and run it's function
        """
        self.actionExit.triggered.connect(self.ExitSEEYOU)

    # ADD SLOT FUNCTIONS HERE
    """
    if user have not save before hand, the function will check...
    for odd reason this works, but still give me a exit code 1, WHY WHY WHY WHY WHY!!
    """
    def ExitSEEYOU(self):
        if self.unsavedChanges == False:
            reply = QMessageBox.question(self, "HEY!", "Do you want save first?", QMessageBox.Yes, QMessageBox.No)
        else:
            QApplication.closeAllWindows()

        if reply == QMessageBox.Yes:
            self.file_save()
            #if user want to save, this will go to the file_save function and let them do it. i am so nice.
        else:
            QApplication.closeAllWindows()

    """
    let user select the file to open, if they hit cancel.  it will return to the activeWindow.
    noticed that I only need input the value of Network Address and Number Of Host from the file,
    because the program will calculate the rest
    """
    def file_open(self):
        self.InfoList = []
        """ This will automaticaly show file with .txt extension incase user try to be cheeky and break my program. >=( """
        fname = QFileDialog.getOpenFileName(self, 'Open file', '', "Text files (*.txt)")
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
            self.lineEditNetworkAddress.setText(str(self.InfoList[0][0]))
            self.lineEditHostsPerSubnet.setText(str(self.InfoList[1][0]))
            self.calculate()

    """
    let user enter file name, and the program will auto select it as .txt
    as before, if they hit cancel, it will return to active windows.
    """

    def file_save(self):
        self.unsavedChanges = True
        fname = QFileDialog.getSaveFileName(self, 'Save file as', '',"Text files (*.txt)")
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

    """
    Empty the GUI, it's like ... flushing the toilet. clean slate, baby! WOOHOOO!!
    """

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

    """
    this is where the magic happens, all the fancy calculation will error checking.
    because user sometime like to try to break my stuff >=(
    """
    def calculate(self):
        ip = self.lineEditNetworkAddress.text() #enter network address to it's own variable for future calculation
        self.labelDecimalOctets.setText(ip) #since Decimal Octets is the same as IP, no need to do anything
        # enter the number of Hosts user want per subnet to it's own variable for future calculation
        numberOfHost = self.lineEditHostsPerSubnet.text()
        # split the IP address to 4 parts, and check if it and the host number a digit. if not, an error will pop up
        # and clear that section of the GUI. TRY AGAIN!
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

    """ a little bit redundant, but it's same as before """
    def AddInfo(self):
        ip = self.lineEditNetworkAddress.text()
        self.labelDecimalOctets.setText(ip)
        numberOfHost = self.lineEditHostsPerSubnet.text()
        NetworkAdd = (ip.split("."))
        """ calculate each part of the IP address of it's decimal equivalent and add them all back together
        then plug that baby back in to the GUI. """
        decimal1 = int(NetworkAdd[0]) * (256**3)
        decimal2 = int(NetworkAdd[1]) * (256**2)
        decimal3 = int(NetworkAdd[2]) * (256)
        decimal4 = int(NetworkAdd[3])
        decimal_equivalent = decimal1 + decimal2 + decimal3 + decimal4
        decimal_equivalent = str(decimal_equivalent)
        self.labelDecimalAddress.setText(decimal_equivalent)

        """Same as previous, but change decimal Octets to Binary."""

        binOctet1 = '{0:08b}'.format(int(NetworkAdd[0]))
        binOctet2 = '{0:08b}'.format(int(NetworkAdd[1]))
        binOctet3 = '{0:08b}'.format(int(NetworkAdd[2]))
        binOctet4 = '{0:08b}'.format(int(NetworkAdd[3]))
        binOctet = binOctet1+"."+binOctet2+"."+binOctet3+"."+binOctet4
        self.labelBinaryOctets.setText(binOctet)
        """ and from decimal octets to hex """
        hex1 = hex(int(NetworkAdd[0]))[2:].zfill(2).upper()
        hex2 = hex(int(NetworkAdd[1]))[2:].zfill(2).upper()
        hex3 = hex(int(NetworkAdd[2]))[2:].zfill(2).upper()
        hex4 = hex(int(NetworkAdd[3]))[2:].zfill(2).upper()
        TOTALHEX = hex1+"."+hex2+"."+hex3+"."+hex4
        self.labeHexOctets.setText(TOTALHEX)

        """since the first part of the IP dictate what IP class it is, this will check for that
        as well as MAX hosts allow per class minus 2 for the broadcast and network IP
        if user enter a non valid class A, B, or C class, it will go to an error message and make them enter it again"""
        if int(NetworkAdd[0]) >= 0 and int(NetworkAdd[0]) <= 127:
            if int(numberOfHost) <= 16277214:
                # if user enter more host than the class allow, it will go to an error message, and make them enter it again.
                self.labelNetworkClass.setText("Class A")
                numberOfIP = 2**24 #total hosts, since the SM is 255.0.0.0, there's 24 "0's" in binary
                numberOfIP = str(numberOfIP)
                self.labelNumberOfIPAddress.setText(numberOfIP)
                self.SubnetCalClassA() #to each individual SubnetCal per class
            else:
                # as noted from above, this will happen 2 more times!
                QMessageBox.information(self, "ERROR", "Number of Host is too big for this IP Class!", QMessageBox.Ok)
                self.lineEditHostsPerSubnet.clear()
        elif int(NetworkAdd[0]) >= 128 and int(NetworkAdd[0]) <= 191:
            if int(numberOfHost) <= 65534: #that is still alot....
                self.labelNetworkClass.setText("Class B")
                numberOfIP = 2 **16 # 16 0's in binary
                numberOfIP = str(numberOfIP)
                self.SubnetCalClassB() #to each individual SubnetCal per class
                self.labelNumberOfIPAddress.setText(numberOfIP)
            else:
                QMessageBox.information(self, "ERROR", "Number of Host is too big for this IP Class!", QMessageBox.Ok)
                self.lineEditHostsPerSubnet.clear()

        elif int(NetworkAdd[0]) >= 192 and int(NetworkAdd[0]) <= 223:
            if int(numberOfHost) <= 254:
                self.labelNetworkClass.setText("Class C")
                numberOfIP = 2 ** 8 # only 8 0's in binary
                numberOfIP = str(numberOfIP)
                self.labelNumberOfIPAddress.setText(numberOfIP)
                self.SubnetCalClassC() #to each individual SubnetCal per class
            else:
                QMessageBox.information(self, "ERROR", "Number of Host is too big for this IP Class!", QMessageBox.Ok)
                self.lineEditHostsPerSubnet.clear()
        else:
            # as noted from above... try again, man!
            QMessageBox.information(self, "ERROR", "You must enter a Valid Class A, B or C IP Address!", QMessageBox.Ok)
            self.lineEditNetworkAddress.clear()

    """
    the following 3 functions will calculate per class. they are almost identical except for 1 differences
    """
    def SubnetCalClassA(self):
        ip = self.lineEditNetworkAddress.text()
        numberOfHost = self.lineEditHostsPerSubnet.text()
        numberOfHost = int(numberOfHost)
        """ there's total of 36 bits in all class, this will keep going until host per bits are greater than
        the number of host user wanted"""
        for i in range(36):
            self.hostPerBit = 2 ** i
            self.totalHost.append(self.hostPerBit)
            if numberOfHost < self.hostPerBit:
                maskBits = i #the number of bits needed for the user specific subnet
                HostPerBit = str(self.hostPerBit) #make the integer to string so i can put it on the GUI
                # there's ONLY 24 usable bit for a class A address, minus that from bits need,
                # this will calculate the number of subnet
                self.numberOfSubnet = 2 ** (24 - maskBits)
                NumberOfSubnet = str(self.numberOfSubnet)
                # the CIDR notation needed for subnet Mask calculation, which is why this is a a global variable.
                self.CIDR = 32 - maskBits
                self.labelSubnetSize.setText(HostPerBit)
                self.labelNumberOSubnets.setText(NumberOfSubnet)
                break
        self.TheMasks() #this will go to the subnet mask function... aks THE MASK, without Jim Carey
        """For the life of me, I could not get this to work in it own function
        but plugging this in per subnet class function worked... FORGIVE ME SENSEI"""
        self.ListOfIPRanges.clear() #clear the list widget, so user can do multiple calculation
        newip = self.lineEditNetworkAddress.text() #the network IP address user enter
        # once the previous calculation is done, this is needed for IP range calculation
        hostbit = self.labelSubnetSize.text()
        hostbit = int(hostbit) #change str to int for the next calculation
        for ip in range(0, self.numberOfSubnet):
            """this is where the ipaddress module comes in handy!
            the first line is the original network address to original address plus hostbit minus 1
            ex: if host bit needed is 300 and IP is 10.0.0.0
            the next set of subnet size can hold 300 is 512 bits
            so it will show
            10.0.0.0 - 10.0.1.255, then 10.0.2.0 - 10.0.3.255
            without the ipaddress module will probably be like this
            10.0.0.0 - 10.0.0.511 then 10.0.0.512 - 10.0.0.1023"""
            data = (str(ipaddress.ip_address(newip)) + "-" + str((ipaddress.ip_address(newip) + (hostbit - 1))))
            newip = (ipaddress.ip_address(newip) + hostbit)
            self.ipRangeList.append(data)
            self.ListOfIPRanges.addItem(data)

    """same as class A function instead of 24 usable bits, class B only have 16"""

    def SubnetCalClassB(self):
        ip = self.lineEditNetworkAddress.text()
        numberOfHost = self.lineEditHostsPerSubnet.text()
        numberOfHost = int(numberOfHost)
        for i in range(36):  # total bits
            self.hostPerBit = 2 ** i
            self.totalHost.append(self.hostPerBit)
            if numberOfHost < self.hostPerBit:
                maskBits = i
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

    """same as class A function instead of 24 usable bits, class c only have 8"""

    def SubnetCalClassC(self):
        ip = self.lineEditNetworkAddress.text()
        numberOfHost = self.lineEditHostsPerSubnet.text()
        numberOfHost = int(numberOfHost)
        for i in range(36):  # total bits
            self.hostPerBit = 2 ** i
            self.totalHost.append(self.hostPerBit)
            if numberOfHost < self.hostPerBit:
                maskBits = i
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

    """ The subnet mask function! thank you ipaddress module again!"""
    def TheMasks(self):
        ip = self.lineEditNetworkAddress.text() #the network IP is needed, yet again!
        ipCIDR = ip + "/" + str(self.CIDR) #this will show the network IP with CIDR notation for the next calculation
        """this will convert ip with CIDR to a variable name networkMask so that it will show the CIDR notation
        into decimal octets ex: 255.255.254.0 from /23"""
        network = ipaddress.ip_network('{}'.format(ipCIDR))
        networkMask = network.netmask
        netmaskString = str(networkMask) + " or /" + str(self.CIDR)
        self.labelSubnetMask.setText(netmaskString) #show in GUI as ex: 255.255.254.0 or /23 for easy reading!

        """This is similar to the network IP to binary function I used back from the beginning, but this time
        with the network mask instead!"""

        binMask = str(networkMask).split(".")
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
