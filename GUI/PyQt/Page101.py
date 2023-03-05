from PySide6.QtSerialPort import QSerialPort, QSerialPortInfo
from PySide6.QtWidgets import QFileDialog, QWidget
import Settings
import serial
import numpy as np
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
            self.COM = self.ui.Spikeling_SelectPortComboBox.currentText()
            self.BaudRate = Settings.BaudRate
            self.serial_port = serial.Serial(self.COM, self.BaudRate)
            if self.serial_port.is_open:
                self.ui.Spikeling_ConnectButton.setEnabled(True)
                self.serial_port.close()

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
            if self.ui.StimFre_toggleButton.isChecked():
                    self.Stim_DutyCycle = 500
                    self.Stim_MinCycle = 10
                    self.ui.Spikeling_StimFre_slider.setEnabled(True)
                    self.StimFreValue = self.ui.Spikeling_StimFre_slider.value()*(-1)
                    self.setTextStimFre = str(int(np.around(10000/(self.Stim_DutyCycle + (self.StimFreValue*self.Stim_DutyCycle/100) + self.Stim_MinCycle))))
                    self.ui.Spikeling_StimFre_readings.setText(self.setTextStimFre)
                    self.ui.Spikeling_StimFre_readings.setStyleSheet("color: rgb" + str(tuple(Settings.DarkSolarized[5])) + "; font: 700 10pt;")
                    if self.serial_port.is_open:
                        self.serial_port.write(str('FR1 ' + str(self.StimFreValue) + '\n').encode('utf-8'))
            else:
                    self.ui.Spikeling_StimFre_slider.setEnabled(False)
                    self.ui.Spikeling_StimFre_slider.setValue(0)
                    self.ui.Spikeling_StimFre_readings.setText('')
                    if self.serial_port.is_open:
                            self.serial_port.write(str('FR0' + '\n').encode('utf-8'))

    def GetStimFreSliderValue(self):
            self.StimFreValue = self.ui.Spikeling_StimFre_slider.value()*(-1)
            self.setTextStimFre = str(int(np.around(10000/(self.Stim_DutyCycle + (self.StimFreValue*self.Stim_DutyCycle/100) + self.Stim_MinCycle))))
            self.ui.Spikeling_StimFre_readings.setText(self.setTextStimFre)
            self.ui.Spikeling_StimFre_readings.setStyleSheet("color: rgb" + str(tuple(Settings.DarkSolarized[5])) + "; font: 700 10pt;")
            if self.serial_port.is_open:
                self.serial_port.write(str('FR1 ' + str(self.StimFreValue) + '\n').encode('utf-8'))


    # Stimulus Strength
    def ActivateStimStr(self):
            if self.ui.StimStr_toggleButton.isChecked():
                    self.ui.Spikeling_StimStrSlider.setEnabled(True)
                    self.StimStrValue = self.ui.Spikeling_StimStrSlider.value()
                    self.ui.Spikeling_StimStr_readings.setText(str(self.StimStrValue))
                    self.ui.Spikeling_StimStr_readings.setStyleSheet("color: rgb" + str(tuple(Settings.DarkSolarized[5])) + "; font: 700 10pt;")
                    if self.serial_port.is_open:
                        self.serial_port.write(str('ST1 ' + str(self.StimStrValue) + '\n').encode('utf-8'))
            else:
                    self.ui.Spikeling_StimStrSlider.setEnabled(False)
                    self.ui.Spikeling_StimStrSlider.setValue(0)
                    self.ui.Spikeling_StimStr_readings.setText('')
                    if self.serial_port.is_open:
                            self.serial_port.write(str('ST0' + '\n').encode('utf-8'))

    def GetStimStrSliderValue(self):
            self.StimStrValue = self.ui.Spikeling_StimStrSlider.value()
            self.ui.Spikeling_StimStr_readings.setText(str(self.StimStrValue))
            self.ui.Spikeling_StimStr_readings.setStyleSheet("color: rgb" + str(tuple(Settings.DarkSolarized[5])) + "; font: 700 10pt;")
            if self.serial_port.is_open:
                self.serial_port.write(str('ST1 ' + str(self.StimStrValue) + '\n').encode('utf-8'))


    # Custom Stimulus
    def ActivateCustomStimulus(self):
            if self.ui.StimCus_toggleButton.isChecked():
                    self.ui.Spikeling_CustomStimulus_comboBox.setEnabled(True)
            else:
                    self.ui.Spikeling_CustomStimulus_comboBox.setEnabled(False)


    # PhotoGain
    def ActivatePhotoGain(self):
            if self.ui.PhotoGain_toggleButton.isChecked():
                    self.ui.Spikeling_PR_PhotoGain_slider.setEnabled(True)
                    self.PhotoGain = self.ui.Spikeling_PR_PhotoGain_slider.value()
                    self.ui.Spikeling_PR_Photogain_readings.setText(str(self.PhotoGain))
                    self.ui.Spikeling_PR_Photogain_readings.setStyleSheet("color: rgb" + str(tuple(Settings.DarkSolarized[4])) + "; font: 700 10pt;")
                    if self.serial_port.is_open:
                            self.serial_port.write(str('PG1 ' + str(self.PhotoGain) + '\n').encode('utf-8'))
            else:
                    self.ui.Spikeling_PR_PhotoGain_slider.setEnabled(False)
                    self.ui.Spikeling_PR_PhotoGain_slider.setValue(0)
                    self.ui.Spikeling_PR_Photogain_readings.setText("")
                    if self.serial_port.is_open:
                            self.serial_port.write(str('PG0' + '\n').encode('utf-8'))

    def GetPhotoGain(self):
            self.PhotoGain = self.ui.Spikeling_PR_PhotoGain_slider.value()
            self.ui.Spikeling_PR_Photogain_readings.setText(str(self.PhotoGain))
            self.ui.Spikeling_PR_Photogain_readings.setStyleSheet("color: rgb" + str(tuple(Settings.DarkSolarized[4])) + "; font: 700 10pt;")
            if self.serial_port.is_open:
                    self.serial_port.write(str('PG1 ' + str(self.PhotoGain) + '\n').encode('utf-8'))


    # PhotoDecay
    def ActivatePRDecay(self):
            if self.ui.PhotoDecay_toggleButton.isChecked():
                    self.ui.Spikeling_PR_Decay_slider.setEnabled(True)
                    self.PhotoDecay = self.ui.Spikeling_PR_Decay_slider.value()
                    self.ui.Spikeling_PR_Decay_readings.setText(str(self.PhotoDecay/100000))
                    self.ui.Spikeling_PR_Decay_readings.setStyleSheet("color: rgb" + str(tuple(Settings.DarkSolarized[4])) + "; font: 700 10pt;")
                    if self.serial_port.is_open:
                            self.serial_port.write(str('PD1 ' + str(self.PhotoDecay) + '\n').encode('utf-8'))
            else:
                    self.ui.Spikeling_PR_Decay_slider.setEnabled(False)
                    self.ui.Spikeling_PR_Decay_slider.setValue(100)
                    self.ui.Spikeling_PR_Decay_readings.setText("")
                    if self.serial_port.is_open:
                            self.serial_port.write(str('PD0' + '\n').encode('utf-8'))

    def GetPRDecay(self):
            self.PhotoDecay = self.ui.Spikeling_PR_Decay_slider.value()
            self.ui.Spikeling_PR_Decay_readings.setText(str(self.PhotoDecay/100000))
            self.ui.Spikeling_PR_Decay_readings.setStyleSheet("color: rgb" + str(tuple(Settings.DarkSolarized[4])) + "; font: 700 10pt;")
            if self.serial_port.is_open:
                    self.serial_port.write(str('PD1 ' + str(self.PhotoDecay) + '\n').encode('utf-8'))


    # PhotoRecovery
    def ActivatePRRecovery(self):
            if self.ui.PhotoRecovery_toggleButton.isChecked():
                    self.ui.Spikeling_PR_Recovery_slider.setEnabled(True)
                    self.PhotoRecovery = self.ui.Spikeling_PR_Recovery_slider.value()
                    self.ui.Spikeling_PR_Recovery_readings.setText(str(self.PhotoRecovery/1000))
                    self.ui.Spikeling_PR_Recovery_readings.setStyleSheet("color: rgb" + str(tuple(Settings.DarkSolarized[4])) + "; font: 700 10pt;")
                    if self.serial_port.is_open:
                            self.serial_port.write(str('PR1 ' + str(self.PhotoRecovery) + '\n').encode('utf-8'))
            else:
                    self.ui.Spikeling_PR_Recovery_slider.setEnabled(False)
                    self.ui.Spikeling_PR_Recovery_slider.setValue(25)
                    self.ui.Spikeling_PR_Recovery_readings.setText("")
                    if self.serial_port.is_open:
                            self.serial_port.write(str('PR0' + '\n').encode('utf-8'))

    def GetPRRecovery(self):
            self.PhotoRecovery = self.ui.Spikeling_PR_Recovery_slider.value()
            self.ui.Spikeling_PR_Recovery_readings.setText(str(self.PhotoRecovery/1000))
            self.ui.Spikeling_PR_Recovery_readings.setStyleSheet("color: rgb" + str(tuple(Settings.DarkSolarized[4])) + "; font: 700 10pt;")
            if self.serial_port.is_open:
                    self.serial_port.write(str('PR1 ' + str(self.PhotoRecovery) + '\n').encode('utf-8'))


    # PatchClamp
    def ActivateInjectedCurrent(self):
            if self.ui.PatchClamp_toggleButton.isChecked():
                    self.ui.Spikeling_PatchClamp_slider.setEnabled(True)
                    self.InjectedCurrent = self.ui.Spikeling_PatchClamp_slider.value()
                    self.ui.Spikeling_PatchClamp_reading.setText(str(self.InjectedCurrent))
                    self.ui.Spikeling_PatchClamp_reading.setStyleSheet("color: rgb" + str(tuple(Settings.DarkSolarized[4])) + "; font: 700 10pt;")
                    if self.serial_port.is_open:
                            self.serial_port.write(str('IC1 ' + str(self.InjectedCurrent) + '\n').encode('utf-8'))
            else:
                    self.ui.Spikeling_PatchClamp_slider.setEnabled(False)
                    self.ui.Spikeling_PatchClamp_slider.setValue(0)
                    self.ui.Spikeling_PatchClamp_reading.setText("")
                    if self.serial_port.is_open:
                            self.serial_port.write(str('IC0' + '\n').encode('utf-8'))

    def GetInjectedCurrent(self):
            self.InjectedCurrent = self.ui.Spikeling_PatchClamp_slider.value()
            self.ui.Spikeling_PatchClamp_reading.setText(str(self.InjectedCurrent))
            self.ui.Spikeling_PatchClamp_reading.setStyleSheet("color: rgb" + str(tuple(Settings.DarkSolarized[4])) + "; font: 700 10pt;")
            if self.serial_port.is_open:
                self.serial_port.write(str('IC1 ' + str(self.InjectedCurrent) + '\n').encode('utf-8'))


    # NoiseLevel
    def ActivateNoiseLevel(self):
            if self.ui.Noise_toggleButton.isChecked():
                    self.ui.Spikeling_Noise_slider.setEnabled(True)
                    self.Noise = self.ui.Spikeling_Noise_slider.value()
                    self.ui.Spikeling_Noise_readings.setText(str(self.Noise))
                    self.ui.Spikeling_Noise_readings.setStyleSheet("color: rgb" + str(tuple(Settings.DarkSolarized[4])) + "; font: 700 10pt;")
                    if self.serial_port.is_open:
                        self.serial_port.write(str('NO1 ' + str(self.Noise) + '\n').encode('utf-8'))
            else:
                    self.ui.Spikeling_Noise_slider.setEnabled(False)
                    self.ui.Spikeling_Noise_slider.setValue(0)
                    self.ui.Spikeling_Noise_readings.setText("")
                    if self.serial_port.is_open:
                            self.serial_port.write(str('NO0' + '\n').encode('utf-8'))

    def GetNoiseLevel(self):
            self.Noise = self.ui.Spikeling_Noise_slider.value()
            self.ui.Spikeling_Noise_readings.setText(str(self.Noise))
            self.ui.Spikeling_Noise_readings.setStyleSheet("color: rgb" + str(tuple(Settings.DarkSolarized[4])) + "; font: 700 10pt;")
            if self.serial_port.is_open:
                self.serial_port.write(str('NO1 ' + str(self.Noise) + '\n').encode('utf-8'))


    # Synapse1Gain
    def ActivateSynapticGain1(self):
            if self.ui.Synapse1_toggleButton.isChecked():
                    self.ui.Spikeling_Synapse1_slider.setEnabled(True)
                    self.Synapse1Gain = self.ui.Spikeling_Synapse1_slider.value()
                    self.ui.Spikeling_Synapse1_readings.setText(str(self.Synapse1Gain))
                    self.ui.Spikeling_Synapse1_readings.setStyleSheet("color: rgb" + str(tuple(Settings.DarkSolarized[7])) + "; font: 700 10pt;")
                    if self.serial_port.is_open:
                        self.serial_port.write(str('SG11 ' + str(self.Synapse1Gain) + '\n').encode('utf-8'))
            else:
                    self.ui.Spikeling_Synapse1_slider.setEnabled(False)
                    self.ui.Spikeling_Synapse1_slider.setValue(0)
                    self.ui.Spikeling_Synapse1_readings.setText("")
                    if self.serial_port.is_open:
                            self.serial_port.write(str('SG10' + '\n').encode('utf-8'))

    def GetSynapticGain1(self):
            self.Synapse1Gain = self.ui.Spikeling_Synapse1_slider.value()
            self.ui.Spikeling_Synapse1_readings.setText(str(self.Synapse1Gain))
            self.ui.Spikeling_Synapse1_readings.setStyleSheet("color: rgb" + str(tuple(Settings.DarkSolarized[7])) + "; font: 700 10pt;")
            if self.serial_port.is_open:
                self.serial_port.write(str('SG11 ' + str(self.Synapse1Gain) + '\n').encode('utf-8'))


    # Synapse1Decay
    def ActivateSynapseDecay1(self):
            if self.ui.Synapse1Decay_toggleButton.isChecked():
                    self.ui.Spikeling_Synapse1_Decay_slider.setEnabled(True)
                    self.Synapse1Decay = self.ui.Spikeling_Synapse1_Decay_slider.value()
                    self.ui.Spikeling_Synapse1_Decay_readings.setText(str(self.Synapse1Decay/1000))
                    self.ui.Spikeling_Synapse1_Decay_readings.setStyleSheet("color: rgb" + str(tuple(Settings.DarkSolarized[7])) + "; font: 700 10pt;")
                    if self.serial_port.is_open:
                        self.serial_port.write(str('SD11 ' + str(self.Synapse1Decay) + '\n').encode('utf-8'))
            else:
                    self.ui.Spikeling_Synapse1_Decay_slider.setEnabled(False)
                    self.ui.Spikeling_Synapse1_Decay_slider.setValue(995)
                    self.ui.Spikeling_Synapse1_Decay_readings.setText("")
                    if self.serial_port.is_open:
                            self.serial_port.write(str('SD10' + '\n').encode('utf-8'))

    def GetSynapticDecay1(self):
            self.Synapse1Decay = self.ui.Spikeling_Synapse1_Decay_slider.value()
            self.ui.Spikeling_Synapse1_Decay_readings.setText(str(self.Synapse1Decay/1000))
            self.ui.Spikeling_Synapse1_Decay_readings.setStyleSheet("color: rgb" + str(tuple(Settings.DarkSolarized[7])) + "; font: 700 10pt;")
            if self.serial_port.is_open:
                self.serial_port.write(str('SD11 ' + str(self.Synapse1Decay) + '\n').encode('utf-8'))


    # Synapse2Gain
    def ActivateSynapticGain2(self):
            if self.ui.Synapse2_toggleButton.isChecked():
                    self.ui.Spikeling_Synapse2_slider.setEnabled(True)
                    self.Synapse2Gain = self.ui.Spikeling_Synapse2_slider.value()
                    self.ui.Spikeling_Synapse2_readings.setText(str(self.Synapse2Gain))
                    self.ui.Spikeling_Synapse2_readings.setStyleSheet("color: rgb" + str(tuple(Settings.DarkSolarized[10])) + "; font: 700 10pt;")
                    if self.serial_port.is_open:
                        self.serial_port.write(str('SG21 ' + str(self.Synapse2Gain) + '\n').encode('utf-8'))
            else:
                    self.ui.Spikeling_Synapse2_slider.setEnabled(False)
                    self.ui.Spikeling_Synapse2_slider.setValue(0)
                    self.ui.Spikeling_Synapse2_readings.setText("")
                    if self.serial_port.is_open:
                            self.serial_port.write(str('SG20' + '\n').encode('utf-8'))

    def GetSynapticGain2(self):
            self.Synapse2Gain = self.ui.Spikeling_Synapse2_slider.value()
            self.ui.Spikeling_Synapse2_readings.setText(str(self.Synapse2Gain))
            self.ui.Spikeling_Synapse2_readings.setStyleSheet("color: rgb" + str(tuple(Settings.DarkSolarized[10])) + "; font: 700 10pt;")
            if self.serial_port.is_open:
                self.serial_port.write(str('SG21 ' + str(self.Synapse2Gain) + '\n').encode('utf-8'))


    # Synapse1Decay
    def ActivateSynapseDecay2(self):
            if self.ui.Synapse2Decay_toggleButton.isChecked():
                    self.ui.Spikeling_Synapse2_Decay_slider.setEnabled(True)
                    self.Synapse2Decay = self.ui.Spikeling_Synapse2_Decay_slider.value()
                    self.ui.Spikeling_Synapse2_Decay_readings.setText(str(self.Synapse2Decay/1000))
                    self.ui.Spikeling_Synapse2_Decay_readings.setStyleSheet("color: rgb" + str(tuple(Settings.DarkSolarized[10])) + "; font: 700 10pt;")
                    if self.serial_port.is_open:
                        self.serial_port.write(str('SD21 ' + str(self.Synapse2Decay) + '\n').encode('utf-8'))
            else:
                    self.ui.Spikeling_Synapse2_Decay_slider.setEnabled(False)
                    self.ui.Spikeling_Synapse2_Decay_slider.setValue(990)
                    self.ui.Spikeling_Synapse2_Decay_readings.setText("")
                    if self.serial_port.is_open:
                            self.serial_port.write(str('SD20' + '\n').encode('utf-8'))

    def GetSynapticDecay2(self):
            self.Synapse2Decay = self.ui.Spikeling_Synapse2_Decay_slider.value()
            self.ui.Spikeling_Synapse2_Decay_readings.setText(str(self.Synapse2Decay/1000))
            self.ui.Spikeling_Synapse2_Decay_readings.setStyleSheet("color: rgb" + str(tuple(Settings.DarkSolarized[10])) + "; font: 700 10pt;")
            if self.serial_port.is_open:
                self.serial_port.write(str('SD21 ' + str(self.Synapse2Decay) + '\n').encode('utf-8'))