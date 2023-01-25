from PyQt6.QtSerialPort import QSerialPort, QSerialPortInfo
from PyQt6.QtWidgets import QFileDialog, QWidget
import Settings
import serial
from sys import platform


portList = []
ports = QSerialPortInfo().availablePorts()
for port in ports:
        if platform == "linux" or platform == "linux2":
            portList.append(port.systemLocation())
            print(port.systemLocation())
        else:
            portList.append(port.portName())
serial_port = None

class Spikeling101():

    def ShowPage(self):
        self.ui.mainbody_stackedWidget.setCurrentWidget(self.ui.page_101)
        self.ui.Spikeling_Oscilloscope_widget.setBackground(Settings.DarkSolarized[0])

    # Serial Port Functions
    def ChangePort(self):
            COM = self.ui.Spikeling_SelectPortComboBox.currentText()
            serial_port = serial.Serial(COM, Settings.BaudRate)
            if serial_port.is_open:
                self.ui.Spikeling_ConnectButton.setEnabled(True)
                serial_port.close()

# Data Recording Functions
    def BrowseRecordFolder(self):
            FolderName = QFileDialog.getExistingDirectory(self,
                                                          caption = 'Hey! Select the folder where your experiment will be saved',
                                                          directory = ".\Recordings")
            if FolderName:
                    self.Spikeling_DataRecording_SelectRecordFolder_label.setText(FolderName)
                    self.Spikeling_FolderNameLabel.setText(FolderName)
                    self.Spikeling_DataRecording_RecordFolder_value.setEnabled(True)
                    self.Spikeling_DataRecording_RecordFolder_value.setPlaceholderText("Enter a file name")

    def RecordFolderText(self):
            FolderName = self.ui.Spikeling_FolderNameLabel.text()
            FileName = self.ui.Spikeling_DataRecording_RecordFolder_value.text()
            self.ui.Spikeling_SelectedFolderLabel.setText(FolderName + '/' + FileName)

    def RecordButton(self):
        if self.ui.Spikeling_DataRecording_Record_pushButton.isChecked():
            self.ui.Spikeling_DataRecording_Record_pushButton.setText("Stop Recording")
            self.ui.Spikeling_DataRecording_Record_pushButton.setStyleSheet("color: rgb(250, 250, 250);\n"
                                                "background-color: rgb(50, 220, 47);")

        else:
            self.ui.Spikeling_DataRecording_Record_pushButton.setText("Record")
            self.ui.Spikeling_DataRecording_Record_pushButton.setStyleSheet("color: rgb(250, 250, 250);\n"
                                                "background-color: rgb(220, 50, 47);")

    # Stimulus Frequency
    def ActivateStimFre(self):
            if self.ui.Spikeling_StimFre_checkBox.isChecked():
                    self.ui.Spikeling_StimFre_slider.setEnabled(True)
            else:
                    self.ui.Spikeling_StimFre_slider.setEnabled(False)
                    self.ui.Spikeling_StimFre_slider.setValue(0)

    def GetStimFreSliderValue(self):
            StimFreValue = self.ui.Spikeling_StimFre_slider.value()


    # Stimulus Strength
    def ActivateStimStr(self):
            if self.ui.Spikeling_StimStr_checkBox.isChecked():
                    self.ui.Spikeling_StimStrSlider.setEnabled(True)
            else:
                    self.ui.Spikeling_StimStrSlider.setEnabled(False)
                    self.ui.Spikeling_StimStrSlider.setValue(0)

    def GetStimStrSliderValue(self):
            StimStrValue = self.ui.Spikeling_StimStrSlider.value()



    def ActivateCustomStimulus(self):
            if self.ui.Spikeling_CustomStimulus_checkBox.isChecked():
                    self.ui.Spikeling_CustomStimulus_comboBox.setEnabled(True)
            else:
                    self.ui.Spikeling_CustomStimulus_comboBox.setEnabled(False)

    def ActivatePhotoGain(self):
            if self.ui.Spikeling_PR_PhotoGain_checkBox.isChecked():
                    self.ui.Spikeling_PR_PhotoGain_slider.setEnabled(True)
            else:
                    self.ui.Spikeling_PR_PhotoGain_slider.setEnabled(False)
                    self.ui.Spikeling_PR_PhotoGain_slider.setValue(0)

    def ActivatePRDecay(self):
            if self.ui.Spikeling_PR_Decay_checkBox.isChecked():
                    self.ui.Spikeling_PR_Decay_value.setEnabled(True)
            else:
                    self.ui.Spikeling_PR_Decay_value.setEnabled(False)
                    self.ui.Spikeling_PR_Decay_value.setText("0.001")

    def ActivatePRRecovery(self):
            if self.ui.Spikeling_PR_Recovery_checkBox.isChecked():
                    self.ui.Spikeling_PR_Recovery_value.setEnabled(True)
            else:
                    self.ui.Spikeling_PR_Recovery_value.setEnabled(False)
                    self.ui.Spikeling_PR_Recovery_value.setText("0.025")

    def ActivateMembranePotential(self):
            if self.ui.Spikeling_PatchClamp_checkBox.isChecked():
                    self.ui.Spikeling_PatchClamp_slider.setEnabled(True)
            else:
                    self.ui.Spikeling_PatchClamp_slider.setEnabled(False)
                    self.ui.Spikeling_PatchClamp_slider.setValue(0)

    def ActivateNoiseLevel(self):
            if self.ui.Spikeling_Noise_checkBox.isChecked():
                    self.ui.Spikeling_Noise_slider.setEnabled(True)
            else:
                    self.ui.Spikeling_Noise_slider.setEnabled(False)
                    self.ui.Spikeling_Noise_slider.setValue(0)

    def ActivateSynapticGain1(self):
            if self.ui.Spikeling_Synapse1_checkBox.isChecked():
                    self.ui.Spikeling_Synapse1_slider.setEnabled(True)
            else:
                    self.ui.Spikeling_Synapse1_slider.setEnabled(False)
                    self.ui.Spikeling_Synapse1_slider.setValue(0)

    def ActivateSynapse1Decay(self):
            if self.ui.Spikeling_Synapse1_Decay_checkBox.isChecked():
                    self.ui.Spikeling_Synapse1_Decay_value.setEnabled(True)
            else:
                    self.ui.Spikeling_Synapse1_Decay_value.setEnabled(False)
                    self.ui.Spikeling_Synapse1_Decay_value.setText("0.995")

    def ActivateSynapticGain2(self):
            if self.ui.Spikeling_Synapse2_checkBox.isChecked():
                    self.ui.Spikeling_Synapse2_slider.setEnabled(True)
            else:
                    self.ui.Spikeling_Synapse2_slider.setEnabled(False)
                    self.ui.Spikeling_Synapse2_slider.setValue(0)

    def ActivateSynapse2Decay(self):
            if self.ui.Spikeling_Synapse2_Decay_checkBox.isChecked():
                    self.ui.Spikeling_Synapse2_Decay_value.setEnabled(True)
            else:
                    self.ui.Spikeling_Synapse2_Decay_value.setEnabled(False)
                    self.ui.Spikeling_Synapse2_Decay_value.setText("0.990")


