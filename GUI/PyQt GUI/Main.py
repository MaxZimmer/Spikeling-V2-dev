

########################################################################
# Libraries import

import sys
import os
import serial

# Import QT libraries
from PySide2 import *
from PyQt6.QtSerialPort import QSerialPort, QSerialPortInfo
from Custom_Widgets.Widgets import *

# Import GUI .ui file
from Spikeling_UI import Ui_MainWindow

# Import GUI page scripts
import Page000, Page101, Page102, Page103, Page301
import Settings, Spikeling_graph


# Setting UART parameters
#ports = Settings.COM()
portList = []
ports = QSerialPortInfo().availablePorts()
for port in ports:
    if sys.platform == "linux" or sys.platform == "linux2":
        portList.append(port.systemLocation())
        print(port.systemLocation())
    else:
        portList.append(port.portName())


########################################################################
## MAIN WINDOW CLASS
########################################################################
class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

    # Apply JsonStyle sheet
        loadJsonStyle(self, self.ui)

    ########################################################################
    # Set menu/navigation buttons

        # Left Menu Container
        self.ui.SpikelingMenu_pushButton.clicked.connect(lambda: self.ui.centerMenuContainer.expandMenu())
        self.ui.SpikelingMenu_pushButton.clicked.connect(lambda: self.ui.centerMenuSubContainer_menu_stackedwidget.setCurrentWidget(self.ui.Spikeling_SubMenu_page))
        self.ui.ImagingMenu_pushButton.clicked.connect(lambda: self.ui.centerMenuContainer.expandMenu())
        self.ui.ImagingMenu_pushButton.clicked.connect(lambda: self.ui.centerMenuSubContainer_menu_stackedwidget.setCurrentWidget(self.ui.Imaging_SubMenu_page))
        self.ui.NeuronGeneratorMenu_pushButton.clicked.connect(lambda: self.ui.centerMenuContainer.collapseMenu())
        #self.ui.NeuronGeneratorMenu_pushButton.clicked.connect(lambda: self.ui.centerMenuSubContainer_menu_stackedwidget.setCurrentWidget(self.ui.NeuronGenerator_SubMenu_page))
        self.ui.NeuronGeneratorMenu_pushButton.clicked.connect(lambda: Page301.ShowPage(self))
        self.ui.StimuluGeneratorMenu_pushButton.clicked.connect(lambda: self.ui.centerMenuContainer.expandMenu())
        self.ui.StimuluGeneratorMenu_pushButton.clicked.connect(lambda: self.ui.centerMenuSubContainer_menu_stackedwidget.setCurrentWidget(self.ui.StimulusGenerator_SubMenu_page))
        self.ui.ExercisesMenu_pushButton.clicked.connect(lambda: self.ui.centerMenuContainer.expandMenu())
        self.ui.ExercisesMenu_pushButton.clicked.connect(lambda: self.ui.centerMenuSubContainer_menu_stackedwidget.setCurrentWidget(self.ui.Exercises_SubMenu_page))
        self.ui.SettingsMenu_pushButton.clicked.connect(lambda: self.ui.centerMenuContainer.expandMenu())
        self.ui.SettingsMenu_pushButton.clicked.connect(lambda: self.ui.centerMenuSubContainer_menu_stackedwidget.setCurrentWidget(self.ui.Settings_SubMenu_page))
        self.ui.AboutMenu_pushButton.clicked.connect(lambda: self.ui.centerMenuContainer.expandMenu())
        self.ui.AboutMenu_pushButton.clicked.connect(lambda: self.ui.centerMenuSubContainer_menu_stackedwidget.setCurrentWidget(self.ui.About_SubMenu_page))
        self.ui.HelpMenu_pushButton.clicked.connect(lambda: self.ui.centerMenuContainer.expandMenu())
        self.ui.HelpMenu_pushButton.clicked.connect(lambda: self.ui.centerMenuSubContainer_menu_stackedwidget.setCurrentWidget(self.ui.Help_SubMenu_page))
        self.ui.GitHubMenu_pushButton.clicked.connect(lambda: self.ui.centerMenuContainer.expandMenu())
        self.ui.GitHubMenu_pushButton.clicked.connect(lambda: self.ui.centerMenuSubContainer_menu_stackedwidget.setCurrentWidget(self.ui.GitHub_SubMenu_page))
        self.ui.centerMenuSubContainer_exit_pushButton.clicked.connect(lambda: self.ui.centerMenuContainer.collapseMenu())


        # Spikeling 101 parameters navigation button
        self.ui.Spikeling_StimulusParameter_pushButton.clicked.connect(lambda: self.ui.Spikeling_CenterMenuContainer.expandMenu())
        self.ui.Spikeling_NeuronParameter_pushButton.clicked.connect(lambda: self.ui.Spikeling_CenterMenuContainer.expandMenu())
        self.ui.Spikeling_parameter_exit_pushButton.clicked.connect(lambda: self.ui.Spikeling_CenterMenuContainer.collapseMenu())


    ########################################################################
    # Home Page - page000
        # Display Home page on start up
        self.ui.mainbody_stackedWidget.setCurrentWidget(self.ui.page_000)
        self.GifMovie = QtGui.QMovie(":/resources/resources/spikeling.gif")
        self.ui.mainbody_content_SpikelingGif.setMovie(self.GifMovie)
        self.GifMovie.start()

    # Spikeling Page - page101

        # Display page101 when spikeling button is clicked
        self.ui.Neuron_pushButton.clicked.connect(lambda: Page101.Spikeling101.ShowPage(self))

        # Update connected port COM and append them
        for i in range(len(ports)):
            self.ui.Spikeling_SelectPortComboBox.addItem("")
        for i in range(len(ports)):
            self.ui.Spikeling_SelectPortComboBox.setItemText(i + 1, str(portList[i]))
        # COM port connections
        self.ui.Spikeling_SelectPortComboBox.currentIndexChanged.connect(lambda: Page101.Spikeling101.ChangePort(self))

        # Start reading serial when connect button is clicked and plot the reading on the oscilloscope
        self.ui.Spikeling_ConnectButton.clicked.connect(lambda: Spikeling_graph.ReadSerial(self))

        # Create buffer data record folder
        self.ui.Spikeling_FolderNameLabel = QtWidgets.QLabel(self.ui.Spikeling_DataRecording_box)
        self.ui.Spikeling_FolderNameLabel.setObjectName("FolderNameLabel")

        # Data Recording
        self.ui.Spikeling_DataRecording_RecordFolder_value.textChanged.connect(lambda: Page101.Spikeling101.RecordFolderText(self))
        self.ui.Spikeling_DataRecording_RecordFolderDir_pushButton.clicked.connect(lambda: Page101.Spikeling101.BrowseRecordFolder(self.ui))
        self.ui.Spikeling_DataRecording_Record_pushButton.setCheckable(True)
        self.ui.Spikeling_DataRecording_Record_pushButton.clicked.connect(lambda: Page101.Spikeling101.RecordButton(self))

        # Stimulation parameters
        # Display stimulation parameter page when StimulusParameter button is clicked
        self.ui.Spikeling_StimulusParameter_pushButton.clicked.connect(lambda: self.ui.Spikeling_CenterMenuContainer.expandMenu())
        self.ui.Spikeling_StimulusParameter_pushButton.clicked.connect(lambda: self.ui.Spikeling_parameter_stackedwidget.setCurrentWidget(self.ui.StimulusParameter_page))
        self.ui.Spikeling_StimFre_checkBox.toggled.connect(lambda: Page101.Spikeling101.ActivateStimFre(self))
        self.ui.Spikeling_StimFre_slider.valueChanged.connect(lambda: Page101.Spikeling101.GetStimFreSliderValue(self))
        self.ui.Spikeling_StimStr_checkBox.toggled.connect(lambda: Page101.Spikeling101.ActivateStimStr(self))
        self.ui.Spikeling_StimStrSlider.valueChanged.connect(lambda: Page101.Spikeling101.GetStimStrSliderValue(self))
        self.ui.Spikeling_CustomStimulus_checkBox.toggled.connect(lambda: Page101.Spikeling101.ActivateCustomStimulus(self))
        self.ui.Spikeling_PR_PhotoGain_checkBox.toggled.connect(lambda: Page101.Spikeling101.ActivatePhotoGain(self))
        self.ui.Spikeling_PR_Decay_checkBox.toggled.connect(lambda: Page101.Spikeling101.ActivatePRDecay(self))
        self.ui.Spikeling_PR_Recovery_checkBox.toggled.connect(lambda: Page101.Spikeling101.ActivatePRRecovery(self))

        # Neuron parameters
        # Display neuron parameter page when NeuronParameter button is clicked
        self.ui.Spikeling_NeuronParameter_pushButton.clicked.connect(lambda: self.ui.Spikeling_CenterMenuContainer.expandMenu())
        self.ui.Spikeling_NeuronParameter_pushButton.clicked.connect(lambda: self.ui.Spikeling_parameter_stackedwidget.setCurrentWidget(self.ui.NeuronParameter_page))
        self.ui.Spikeling_PatchClamp_checkBox.toggled.connect(lambda: Page101.Spikeling101.ActivateMembranePotential(self))
        self.ui.Spikeling_Noise_checkBox.toggled.connect(lambda: Page101.Spikeling101.ActivateNoiseLevel(self))
        self.ui.Spikeling_Synapse1_checkBox.toggled.connect(lambda: Page101.Spikeling101.ActivateSynapticGain1(self))
        self.ui.Spikeling_Synapse1_Decay_checkBox.toggled.connect(lambda: Page101.Spikeling101.ActivateSynapse1Decay(self))
        self.ui.Spikeling_Synapse2_checkBox.toggled.connect(lambda: Page101.Spikeling101.ActivateSynapticGain2(self))
        self.ui.Spikeling_Synapse2_Decay_checkBox.toggled.connect(lambda: Page101.Spikeling101.ActivateSynapse2Decay(self))

    # Spikeling Tutorial - page 102
        # Display page102 when tutorial button is clicked
        self.ui.NeuronTutorial_pushButton.clicked.connect(lambda: Page102.Spikeling102.ShowPage(self))

    # Spikeling Data Analysis - page 103
        # Display page103 when data analysis button is clicked
        self.ui.NeuronDataAnalysis_pushButton.clicked.connect(lambda: Page103.Spikeling103.ShowPage(self))
        # Raw Data Analysis part
        self.ui.DataAnalysis_LoadData_pushButton.clicked.connect(lambda: Page103.Spikeling103.LoadData(self.ui))
        self.ui.DataAnalysis_LoadData_Display_pushButton.clicked.connect(lambda: Page103.Spikeling103.DisplayRawData(self))
        self.ui.DataAnalysis_SaveImage_pushButton.clicked.connect(lambda: Page103.Spikeling103.SaveRawDataImage(self))
        # Find spike analysis part
        self.ui.DataAnalysis_Spike_Display_pushButton.clicked.connect(lambda: Page103.Spikeling103.FindSpike(self))
        self.ui.DataAnalysis_Spike_Export_pushButton.clicked.connect(lambda: Page103.Spikeling103.SaveSpikeTraces(self))
        self.ui.DataAnalysis_Spike_SaveImage_pushButton.clicked.connect(lambda: Page103.Spikeling103.SaveSpikeImage(self))
        # Compute average trace and spike raster plot
        self.ui.DataAnalysis_Average_Display_pushButton.clicked.connect(lambda: Page103.Spikeling103.AverageTraces(self))
        self.ui.DataAnalysis_Average_Save_pushButton.clicked.connect(lambda: Page103.Spikeling103.SaveAverageTraces(self))
        self.ui.DataAnalysis_Average_SaveImage_pushButton.clicked.connect(lambda: Page103.Spikeling103.SaveAverageImage(self))
        # Switch Neuron display pages on raw data page
        self.ui.DataAnalysis_Neuron0Vm_pushButton10.clicked.connect(lambda: self.ui.DataAnalysis_Display_StackedWidget.setCurrentWidget(self.ui.page_103_1_0))
        self.ui.DataAnalysis_Neuron0Vm_pushButton11.clicked.connect(lambda: self.ui.DataAnalysis_Display_StackedWidget.setCurrentWidget(self.ui.page_103_1_0))
        self.ui.DataAnalysis_Neuron0Vm_pushButton12.clicked.connect(lambda: self.ui.DataAnalysis_Display_StackedWidget.setCurrentWidget(self.ui.page_103_1_0))
        self.ui.DataAnalysis_Neuron0Vm_pushButton20.clicked.connect(lambda: self.ui.DataAnalysis_Display_StackedWidget.setCurrentWidget(self.ui.page_103_2_0))
        self.ui.DataAnalysis_Neuron0Vm_pushButton21.clicked.connect(lambda: self.ui.DataAnalysis_Display_StackedWidget.setCurrentWidget(self.ui.page_103_2_0))
        self.ui.DataAnalysis_Neuron0Vm_pushButton22.clicked.connect(lambda: self.ui.DataAnalysis_Display_StackedWidget.setCurrentWidget(self.ui.page_103_2_0))
        self.ui.DataAnalysis_Neuron0Vm_pushButton30.clicked.connect(lambda: self.ui.DataAnalysis_Display_StackedWidget.setCurrentWidget(self.ui.page_103_3_0))
        self.ui.DataAnalysis_Neuron0Vm_pushButton31.clicked.connect(lambda: self.ui.DataAnalysis_Display_StackedWidget.setCurrentWidget(self.ui.page_103_3_0))
        self.ui.DataAnalysis_Neuron0Vm_pushButton32.clicked.connect(lambda: self.ui.DataAnalysis_Display_StackedWidget.setCurrentWidget(self.ui.page_103_3_0))
        # Switch Neuron display pages on find spike age
        self.ui.DataAnalysis_Neuron1Vm_pushButton10.clicked.connect(lambda: self.ui.DataAnalysis_Display_StackedWidget.setCurrentWidget(self.ui.page_103_1_1))
        self.ui.DataAnalysis_Neuron1Vm_pushButton11.clicked.connect(lambda: self.ui.DataAnalysis_Display_StackedWidget.setCurrentWidget(self.ui.page_103_1_1))
        self.ui.DataAnalysis_Neuron1Vm_pushButton12.clicked.connect(lambda: self.ui.DataAnalysis_Display_StackedWidget.setCurrentWidget(self.ui.page_103_1_1))
        self.ui.DataAnalysis_Neuron1Vm_pushButton20.clicked.connect(lambda: self.ui.DataAnalysis_Display_StackedWidget.setCurrentWidget(self.ui.page_103_2_1))
        self.ui.DataAnalysis_Neuron1Vm_pushButton21.clicked.connect(lambda: self.ui.DataAnalysis_Display_StackedWidget.setCurrentWidget(self.ui.page_103_2_1))
        self.ui.DataAnalysis_Neuron1Vm_pushButton22.clicked.connect(lambda: self.ui.DataAnalysis_Display_StackedWidget.setCurrentWidget(self.ui.page_103_2_1))
        self.ui.DataAnalysis_Neuron1Vm_pushButton30.clicked.connect(lambda: self.ui.DataAnalysis_Display_StackedWidget.setCurrentWidget(self.ui.page_103_3_1))
        self.ui.DataAnalysis_Neuron1Vm_pushButton31.clicked.connect(lambda: self.ui.DataAnalysis_Display_StackedWidget.setCurrentWidget(self.ui.page_103_3_1))
        self.ui.DataAnalysis_Neuron1Vm_pushButton32.clicked.connect(lambda: self.ui.DataAnalysis_Display_StackedWidget.setCurrentWidget(self.ui.page_103_3_1))
        # Switch Neuron display pages on compute and average page
        self.ui.DataAnalysis_Neuron2Vm_pushButton10.clicked.connect(lambda: self.ui.DataAnalysis_Display_StackedWidget.setCurrentWidget(self.ui.page_103_1_2))
        self.ui.DataAnalysis_Neuron2Vm_pushButton11.clicked.connect(lambda: self.ui.DataAnalysis_Display_StackedWidget.setCurrentWidget(self.ui.page_103_1_2))
        self.ui.DataAnalysis_Neuron2Vm_pushButton12.clicked.connect(lambda: self.ui.DataAnalysis_Display_StackedWidget.setCurrentWidget(self.ui.page_103_1_2))
        self.ui.DataAnalysis_Neuron2Vm_pushButton20.clicked.connect(lambda: self.ui.DataAnalysis_Display_StackedWidget.setCurrentWidget(self.ui.page_103_2_2))
        self.ui.DataAnalysis_Neuron2Vm_pushButton21.clicked.connect(lambda: self.ui.DataAnalysis_Display_StackedWidget.setCurrentWidget(self.ui.page_103_2_2))
        self.ui.DataAnalysis_Neuron2Vm_pushButton22.clicked.connect(lambda: self.ui.DataAnalysis_Display_StackedWidget.setCurrentWidget(self.ui.page_103_2_2))
        self.ui.DataAnalysis_Neuron2Vm_pushButton30.clicked.connect(lambda: self.ui.DataAnalysis_Display_StackedWidget.setCurrentWidget(self.ui.page_103_3_2))
        self.ui.DataAnalysis_Neuron2Vm_pushButton31.clicked.connect(lambda: self.ui.DataAnalysis_Display_StackedWidget.setCurrentWidget(self.ui.page_103_3_2))
        self.ui.DataAnalysis_Neuron2Vm_pushButton32.clicked.connect(lambda: self.ui.DataAnalysis_Display_StackedWidget.setCurrentWidget(self.ui.page_103_3_2))

    # Neuron Generator Page - page301
        # Display page301 when neuron button is clicked
        self.ui.NeuronGeneratorMenu_pushButton.clicked.connect(lambda: Page301.ShowPage(self))
        # Draw Neuron model based on parameters a, b, c & d
        self.ui.DisplayNeuronPushButton.clicked.connect(lambda: Page301.NeuronGenerator.DrawNeuron(self))

        ########################################################################
    # Display
        self.show()



########################################################################
## EXECUTE APP
########################################################################
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())
########################################################################
## END===>
########################################################################  