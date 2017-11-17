import sys

from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from PyQt5.QtGui import QPixmap
#ADD IMPORT STATEMENT FOR YOUR GENERATED UI.PY FILE HERE
import EdsCountry_lib
import csv
#CHANGE THE SECOND PARAMETER HERE TO MATCH YOUR GENERATED UI.PY FILE
class MyForm(QMainWindow, EdsCountry_lib.Ui_MainWindow):
    CountryList = []
        # DO NOT MODIFY THIS CODE
    def __init__(self, parent=None):
        super(MyForm, self).__init__(parent)
        self.setupUi(self)
        # END DO NOT MODIFY

        # ADD SLOTS HERE
        # setup form by automatically loading data from file and filling UI list
        # when the form starts up

        """
        Automatically load Country onto List widget, and hide everything else.
        """
        self.LoadCountryFile()
        self.CountryListWidget()
        self.CountryFlagLabel.hide()
        self.CountryNameLabel.hide()
        self.label.hide()
        self.label_2.hide()
        self.label_3.hide()
        self.label_4.hide()
        self.lineEditPop.hide()
        self.KMilecomboBox.hide()
        self.radioButtonMile.hide()
        self.radioButtonKM.hide()
        self.labelPopDens.hide()
        self.labelPerPop.hide()
        self.pushButtonUPDATE.hide()
        self.labelTotalArea.hide()

        """
        when user click on a country name, it will show everything. it's like MAGIC!
        such as population density and population percentage.
        """
        self.listWidgetCountry.itemClicked.connect(self.ShowEverything)

        """
        automaticly run function needed for calcution of population density and population percentage
        of the country when row is change
        """
        self.listWidgetCountry.currentRowChanged.connect(self.List_RowChanged)
        self.listWidgetCountry.currentRowChanged.connect(self.PopDens)
        self.listWidgetCountry.currentRowChanged.connect(self.PercentPop)
        """
        when user click or select from combo box, it will preform the function needed for the
        data they requested.
        """
        self.radioButtonMile.clicked.connect(self.PopDens)
        self.radioButtonKM.clicked.connect(self.PopDensKM)
        self.pushButtonUPDATE.clicked.connect(self.Update)
        self.KMilecomboBox.currentIndexChanged.connect(self.ComboBox)
        """
        Just an exit from file menu
        """
        self.actionExit.triggered.connect(self.ExitSEEYOU)
    # ADD SLOT FUNCTIONS HERE
    """
    function to close the window
    """
    def ExitSEEYOU(self):
        QApplication.closeAllWindows()

    """
    function that show the display with data for the country selected
    """
    def ShowEverything(self):
        self.CountryNameLabel.show()
        self.label.show()
        self.label_2.show()
        self.label_3.show()
        self.label_4.show()
        self.lineEditPop.show()
        self.KMilecomboBox.show()
        self.radioButtonMile.show()
        self.radioButtonKM.show()
        self.labelTotalArea.show()
        self.labelPopDens.show()
        self.labelPerPop.show()
        self.pushButtonUPDATE.show()
        self.CountryFlagLabel.show()

    """
    combo box function 0 is first item, 1 is second item. if there was more item in the combo box, they
    would go from index 0,1,2,3 etc
    """
    def ComboBox(self):
        newIndex = self.listWidgetCountry.currentRow()
        if self.KMilecomboBox.currentIndex() == 0:
            Area = float(self.CountryList[newIndex][2])
            areaString = '{:,}'.format(Area)
            self.labelTotalArea.setText(areaString)
        elif self.KMilecomboBox.currentIndex() == 1:
            Area = float(self.CountryList[newIndex][2])*2.59
            areaString = '{:,}'.format(round(Area, 2))
            self.labelTotalArea.setText(areaString)

    """
    When row is changed, this function will show the data pertaining to that row of code in the 2D list
    and run flag image function, and automatically reselect sq mile and mile button everytime the user change
    the country
    """
    def List_RowChanged(self, newIndex):
        self.CountryNameLabel.setText(self.CountryList[newIndex][0])
        Pop = round(float(self.CountryList[newIndex][1]))
        popString = '{:,}'.format(Pop)
        self.lineEditPop.setText(popString)
        Area = round(float(self.CountryList[newIndex][2]))
        areaString = '{:,}'.format(Area)
        self.labelTotalArea.setText(areaString)
        self.radioButtonMile.setChecked(True)
        self.FlagImage()
        self.KMilecomboBox.setCurrentIndex(0)

    """
    fancy function to show the country flag, with error fix. For some odd reason Python can't read
    Côte from the list and read it as CÃ´te, and i thought i was bad with english
    """
    def FlagImage(self):
        newIndex = self.listWidgetCountry.currentRow()
        imageCountry = self.CountryList[newIndex][0]
        image = QPixmap("Flags\{}.png".format(imageCountry).replace(" ", "_").replace("CÃ´te", "Côte"))
        self.CountryFlagLabel.setPixmap(image)

    """
    update new population value to the list by running SaveToMemory function
    """
    def Update(self):
        self.unsavedChanges = True
        self.SaveToMemory()
        #display pop up message
        QMessageBox.information(self, "Pop up Window", "Changed is saved", QMessageBox.Ok)

    def SaveToMemory(self):
        selectedIndex = self.listWidgetCountry.currentRow()
        oldPop = self.CountryList[selectedIndex][1]
        pop = self.lineEditPop.text()
        self.CountryList[selectedIndex][1] = pop
        newPop = self.CountryList[selectedIndex][1].split(',')
        self.CountryList[selectedIndex][1] = ''.join(newPop)
        """
        update new data back to the file.
        """
        with open("countries.txt", "w") as OUTPUT:
            for x in self.CountryList:
                OUTPUT.write((',').join(x) + "\n")

            #ADD HELPER FUNCTIONS HERE
    """
    function to open countries.txt file with csv reader and read data into countries list
    """
    def LoadCountryFile(self):
        self.CountryList.clear()

        with open("countries.txt", "r") as INPUT:
            # load data into reader object
            DataList = csv.reader(INPUT)
            # loop through each line in reader...each line is a list of values
            for x in DataList:
                # add each list to the people list variable declared above
                self.CountryList.append(x)
        """
        fix weird read error on the list
        """

        self.CountryList[47][0] = "Côte d'Ivoire"

    """
    show said CountryList into List Widget name listWidgetCountry
    """
    def CountryListWidget(self):
        self.listWidgetCountry.clear()
        # load the list with the names of the people in the people[] list
        # that was loaded from the text file
        for i in self.CountryList:
            self.listWidgetCountry.addItem(i[0])
    """
    function to calculate population percentage by using a for loop for lenght of country list
    and add all the population together, then divided population for each country over total world population and
    times by 100 to get percentage.
    """
    def PercentPop(self, newIndex):
        pop = 0
        for y in range(len(self.CountryList)):
            pop += float(self.CountryList[y][1])

        PP = (((float(self.CountryList[newIndex][1]))/(pop)) * 100)
        PPString = '{:.2f}'.format(PP)+ str("%")
        self.labelPerPop.setText(PPString)

    """
    function to calculate population density by dividing population of selected country over
    county sq mile.
    """
    def PopDens(self):
        newIndex = self.listWidgetCountry.currentRow()
        x = float(self.CountryList[newIndex][1]) / float(self.CountryList[newIndex][2])
        xString = '{:.2f}'.format(x)
        self.labelPopDens.setText(xString)

    """
    similar to previous function, but to pop per sq KM instead
    1 sq mile = 2.59 sq KM
    """
    def PopDensKM(self):
        newIndex = self.listWidgetCountry.currentRow()
        x = float(self.CountryList[newIndex][1]) / ((float(self.CountryList[newIndex][2])*2.59))
        xString = '{:.2f}'.format(x)
        self.labelPopDens.setText(xString)
        self.radioButtonMile.setChecked(False)

# DO NOT MODIFY THIS CODE
if __name__ == "__main__":
    app = QApplication(sys.argv)
    the_form = MyForm()
    the_form.show()
    sys.exit(app.exec_())
# END DO NOT MODIFY
