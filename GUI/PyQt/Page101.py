from PySide6.QtSerialPort import QSerialPort, QSerialPortInfo
from PySide6.QtWidgets import QFileDialog, QWidget
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
                    self.StimFreValue = self.ui.Spikeling_StimFre_slider.value()
                    self.ui.Spikeling_StimFre_readings.setText(str(self.StimFreValue))
                    self.ui.Spikeling_StimFre_readings.setStyleSheet("color: rgb(38, 139, 210); font: 700 10pt;")
            else:
                    self.ui.Spikeling_StimFre_slider.setEnabled(False)
                    self.ui.Spikeling_StimFre_slider.setValue(0)
                    self.ui.Spikeling_StimFre_readings.setText('')
    def GetStimFreSliderValue(self):
            self.StimFreValue = self.ui.Spikeling_StimFre_slider.value()
            self.ui.Spikeling_StimFre_readings.setText(str(self.StimFreValue))
            self.ui.Spikeling_StimFre_readings.setStyleSheet("color: rgb(38, 139, 210); font: 700 10pt;")


    # Stimulus Strength
    def ActivateStimStr(self):
            if self.ui.Spikeling_StimStr_checkBox.isChecked():
                    self.ui.Spikeling_StimStrSlider.setEnabled(True)
                    self.StimStrValue = self.ui.Spikeling_StimStrSlider.value()
                    self.ui.Spikeling_StimStr_readings.setText(str(self.StimStrValue))
                    self.ui.Spikeling_StimStr_readings.setStyleSheet("color: rgb(38, 139, 210); font: 700 10pt;")
            else:
                    self.ui.Spikeling_StimStrSlider.setEnabled(False)
                    self.ui.Spikeling_StimStrSlider.setValue(0)
                    self.ui.Spikeling_StimStr_readings.setText('')
    def GetStimStrSliderValue(self):
            self.StimStrValue = self.ui.Spikeling_StimStrSlider.value()
            self.ui.Spikeling_StimStr_readings.setText(str(self.StimStrValue))
            self.ui.Spikeling_StimStr_readings.setStyleSheet("color: rgb(38, 139, 210); font: 700 10pt;")




    def ActivateCustomStimulus(self):
            if self.ui.Spikeling_CustomStimulus_checkBox.isChecked():
                    self.ui.Spikeling_CustomStimulus_comboBox.setEnabled(True)
            else:
                    self.ui.Spikeling_CustomStimulus_comboBox.setEnabled(False)



    #PhotoGain
    def ActivatePhotoGain(self):
            if self.ui.Spikeling_PR_PhotoGain_checkBox.isChecked():
                    self.ui.Spikeling_PR_PhotoGain_slider.setEnabled(True)
                    self.PhotoGain = self.ui.Spikeling_PR_PhotoGain_slider.value()
                    self.ui.Spikeling_PR_Photogain_readings.setText(str(self.PhotoGain))
                    self.ui.Spikeling_PR_Photogain_readings.setStyleSheet("color: rgb(133, 153, 0); font: 700 10pt;")
            else:
                    self.ui.Spikeling_PR_PhotoGain_slider.setEnabled(False)
                    self.ui.Spikeling_PR_PhotoGain_slider.setValue(0)
                    self.ui.Spikeling_PR_Photogain_readings.setText("")
    def GetPhotoGain(self):
            self.PhotoGain = self.ui.Spikeling_PR_PhotoGain_slider.value()
            self.ui.Spikeling_PR_Photogain_readings.setText(str(self.PhotoGain))
            self.ui.Spikeling_PR_Photogain_readings.setStyleSheet("color: rgb(133, 153, 0); font: 700 10pt;")

    #PhotoDecay
    def ActivatePRDecay(self):
            if self.ui.Spikeling_PR_Decay_checkBox.isChecked():
                    self.ui.Spikeling_PR_Decay_slider.setEnabled(True)
                    self.PhotoDecay = self.ui.Spikeling_PR_Decay_slider.value()
                    self.ui.Spikeling_PR_Decay_readings.setText(str(self.PhotoDecay/100000))
                    self.ui.Spikeling_PR_Decay_readings.setStyleSheet("color: rgb(133, 153, 0); font: 700 10pt;")
            else:
                    self.ui.Spikeling_PR_Decay_slider.setEnabled(False)
                    self.ui.Spikeling_PR_Decay_slider.setValue(100)
                    self.ui.Spikeling_PR_Decay_readings.setText("")

    def GetPRDecay(self):
            self.PhotoDecay = self.ui.Spikeling_PR_Decay_slider.value()
            self.ui.Spikeling_PR_Decay_readings.setText(str(self.PhotoDecay/100000))
            self.ui.Spikeling_PR_Decay_readings.setStyleSheet("color: rgb(133, 153, 0); font: 700 10pt;")

    #PhotoRecovery
    def ActivatePRRecovery(self):
            if self.ui.Spikeling_PR_Recovery_checkBox.isChecked():
                    self.ui.Spikeling_PR_Recovery_slider.setEnabled(True)
                    self.PhotoRecovery = self.ui.Spikeling_PR_Recovery_slider.value()
                    self.ui.Spikeling_PR_Recovery_readings.setText(str(self.PhotoRecovery/1000))
                    self.ui.Spikeling_PR_Recovery_readings.setStyleSheet("color: rgb(133, 153, 0); font: 700 10pt;")
            else:
                    self.ui.Spikeling_PR_Recovery_slider.setEnabled(False)
                    self.ui.Spikeling_PR_Recovery_slider.setValue(25)
                    self.ui.Spikeling_PR_Recovery_readings.setText("")
    def GetPRRecovery(self):
            self.PhotoRecovery = self.ui.Spikeling_PR_Recovery_slider.value()
            self.ui.Spikeling_PR_Recovery_readings.setText(str(self.PhotoRecovery/1000))
            self.ui.Spikeling_PR_Recovery_readings.setStyleSheet("color: rgb(133, 153, 0); font: 700 10pt;")



    #PatchClamp
    def ActivateInjectedCurrent(self):
            if self.ui.Spikeling_PatchClamp_checkBox.isChecked():
                    self.ui.Spikeling_PatchClamp_slider.setEnabled(True)
                    self.InjectedCurrent = self.ui.Spikeling_PatchClamp_slider.value()
                    self.ui.Spikeling_PatchClamp_reading.setText(str(self.InjectedCurrent))
                    self.ui.Spikeling_PatchClamp_reading.setStyleSheet("color: rgb(133, 153, 0); font: 700 10pt;")
            else:
                    self.ui.Spikeling_PatchClamp_slider.setEnabled(False)
                    self.ui.Spikeling_PatchClamp_slider.setValue(0)
                    self.ui.Spikeling_PatchClamp_reading.setText("")
    def GetInjectedCurrent(self):
            self.InjectedCurrent = self.ui.Spikeling_PatchClamp_slider.value()
            self.ui.Spikeling_PatchClamp_reading.setText(str(self.InjectedCurrent))
            self.ui.Spikeling_PatchClamp_reading.setStyleSheet("color: rgb(133, 153, 0); font: 700 10pt;")


    #NoiseLevel
    def ActivateNoiseLevel(self):
            if self.ui.Spikeling_Noise_checkBox.isChecked():
                    self.ui.Spikeling_Noise_slider.setEnabled(True)
                    self.Noise = self.ui.Spikeling_Noise_slider.value()
                    self.ui.Spikeling_Noise_readings.setText(str(self.Noise))
                    self.ui.Spikeling_Noise_readings.setStyleSheet("color: rgb(133, 153, 0); font: 700 10pt;")
            else:
                    self.ui.Spikeling_Noise_slider.setEnabled(False)
                    self.ui.Spikeling_Noise_slider.setValue(0)
                    self.ui.Spikeling_Noise_readings.setText("")
    def GetNoiseLevel(self):
            self.Noise = self.ui.Spikeling_Noise_slider.value()
            self.ui.Spikeling_Noise_readings.setText(str(self.Noise))
            self.ui.Spikeling_Noise_readings.setStyleSheet("color: rgb(133, 153, 0); font: 700 10pt;")


    #Synapse1Gain
    def ActivateSynapticGain1(self):
            if self.ui.Spikeling_Synapse1_checkBox.isChecked():
                    self.ui.Spikeling_Synapse1_slider.setEnabled(True)
                    self.Synapse1Gain = self.ui.Spikeling_Synapse1_slider.value()
                    self.ui.Spikeling_Synapse1_readings.setText(str(self.Synapse1Gain))
                    self.ui.Spikeling_Synapse1_readings.setStyleSheet("color: rgb(42, 161, 152); font: 700 10pt;")
            else:
                    self.ui.Spikeling_Synapse1_slider.setEnabled(False)
                    self.ui.Spikeling_Synapse1_slider.setValue(0)
                    self.ui.Spikeling_Synapse1_readings.setText("")
    def GetSynapticGain1(self):
            self.Synapse1Gain = self.ui.Spikeling_Synapse1_slider.value()
            self.ui.Spikeling_Synapse1_readings.setText(str(self.Synapse1Gain))
            self.ui.Spikeling_Synapse1_readings.setStyleSheet("color: rgb(42, 161, 152); font: 700 10pt;")

    #Synapse1Decay
    def ActivateSynapseDecay1(self):
            if self.ui.Spikeling_Synapse1_Decay_checkBox.isChecked():
                    self.ui.Spikeling_Synapse1_Decay_slider.setEnabled(True)
                    self.Synapse1Decay = self.ui.Spikeling_Synapse1_Decay_slider.value()
                    self.ui.Spikeling_Synapse1_Decay_readings.setText(str(self.Synapse1Decay/1000))
                    self.ui.Spikeling_Synapse1_Decay_readings.setStyleSheet("color: rgb(42, 161, 152); font: 700 10pt;")
            else:
                    self.ui.Spikeling_Synapse1_Decay_slider.setEnabled(False)
                    self.ui.Spikeling_Synapse1_Decay_slider.setValue(995)
                    self.ui.Spikeling_Synapse1_Decay_readings.setText("")
    def GetSynapticDecay1(self):
            self.Synapse1Decay = self.ui.Spikeling_Synapse1_Decay_slider.value()
            self.ui.Spikeling_Synapse1_Decay_readings.setText(str(self.Synapse1Decay/1000))
            self.ui.Spikeling_Synapse1_Decay_readings.setStyleSheet("color: rgb(42, 161, 152); font: 700 10pt;")


    #Synapse2Gain
    def ActivateSynapticGain2(self):
            if self.ui.Spikeling_Synapse2_checkBox.isChecked():
                    self.ui.Spikeling_Synapse2_slider.setEnabled(True)
                    self.Synapse2Gain = self.ui.Spikeling_Synapse2_slider.value()
                    self.ui.Spikeling_Synapse2_readings.setText(str(self.Synapse2Gain))
                    self.ui.Spikeling_Synapse2_readings.setStyleSheet("color: rgb(108, 113, 196); font: 700 10pt;")
            else:
                    self.ui.Spikeling_Synapse2_slider.setEnabled(False)
                    self.ui.Spikeling_Synapse2_slider.setValue(0)
                    self.ui.Spikeling_Synapse2_readings.setText("")
    def GetSynapticGain2(self):
            self.Synapse2Gain = self.ui.Spikeling_Synapse2_slider.value()
            self.ui.Spikeling_Synapse2_readings.setText(str(self.Synapse2Gain))
            self.ui.Spikeling_Synapse2_readings.setStyleSheet("color: rgb(108, 113, 196); font: 700 10pt;")

    #Synapse1Decay
    def ActivateSynapseDecay2(self):
            if self.ui.Spikeling_Synapse2_Decay_checkBox.isChecked():
                    self.ui.Spikeling_Synapse2_Decay_slider.setEnabled(True)
                    self.Synapse2Decay = self.ui.Spikeling_Synapse2_Decay_slider.value()
                    self.ui.Spikeling_Synapse2_Decay_readings.setText(str(self.Synapse2Decay/1000))
                    self.ui.Spikeling_Synapse2_Decay_readings.setStyleSheet("color: rgb(108, 113, 196); font: 700 10pt;")
            else:
                    self.ui.Spikeling_Synapse2_Decay_slider.setEnabled(False)
                    self.ui.Spikeling_Synapse2_Decay_slider.setValue(990)
                    self.ui.Spikeling_Synapse2_Decay_readings.setText("")
    def GetSynapticDecay2(self):
            self.Synapse2Decay = self.ui.Spikeling_Synapse2_Decay_slider.value()
            self.ui.Spikeling_Synapse2_Decay_readings.setText(str(self.Synapse2Decay/1000))
            self.ui.Spikeling_Synapse2_Decay_readings.setStyleSheet("color: rgb(108, 113, 196); font: 700 10pt;")