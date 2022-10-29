from PyQt6.QtSerialPort import QSerialPort, QSerialPortInfo
from PyQt6.QtWidgets import QFileDialog, QWidget
import serial

BaudRate = 115200
portList = []
ports = QSerialPortInfo().availablePorts()
for port in ports:
        portList.append(port.portName())
serial_port = None

class Tab1():

    # Serial Port Functions
    def ChangePort(self):
            COM = self.SelectPortComboBox.currentText()
            serial_port = serial.Serial(COM, BaudRate)
            if serial_port.is_open:
                self.radioButton.setEnabled(True)
                serial_port.close()

# Data Recording Functions
    def BrowseRecordFolder(self):
            FolderName = QFileDialog.getExistingDirectory(self, 'Hey! Select the folder where your experiment will be saved')
            if FolderName:
                    self.SelectedFolderLabel.setText(FolderName)
                    self.FolderNameLabel.setText(FolderName)
                    self.RecordFolderValue.setEnabled(True)
                    self.RecordFolderValue.setPlaceholderText("Enter a file name")

    def RecordFolderText(self):
            FolderName = self.FolderNameLabel.text()
            FileName = self.RecordFolderValue.text()
            self.SelectedFolderLabel.setText(FolderName + '/' + FileName)


    # Stimulus Frequency
    def ActivateStimFre(self):
            if self.StimFreCheckBox.isChecked():
                    self.StimFreSlider.setEnabled(True)
            else:
                    self.StimFreSlider.setEnabled(False)
                    self.StimFreSlider.setValue(0)

    def GetStimFreSliderValue(self):
            StimFreValue = self.StimFreSlider.value()


    # Stimulus Strength
    def ActivateStimStr(self):
            if self.StimStrCheckBox.isChecked():
                    self.StimStrSlider.setEnabled(True)
            else:
                    self.StimStrSlider.setEnabled(False)
                    self.StimStrSlider.setValue(0)

    def GetStimStrSliderValue(self):
            StimStrValue = self.StimStrSlider.value()



    def ActivateCustomStimulus(self):
            if self.CustomStimulusCheckBox.isChecked():
                    self.CustomStimuluComboBox.setEnabled(True)
            else:
                    self.CustomStimuluComboBox.setEnabled(False)

    def ActivatePhotoGain(self):
            if self.PhotoGainCheckBox.isChecked():
                    self.PhotoGainSlider.setEnabled(True)
            else:
                    self.PhotoGainSlider.setEnabled(False)
                    self.PhotoGainSlider.setValue(0)

    def ActivatePRDecay(self):
            if self.PRDecayCheckBox.isChecked():
                    self.PRDecayValue.setEnabled(True)
            else:
                    self.PRDecayValue.setEnabled(False)
                    self.PRDecayValue.setText("0.001")

    def ActivatePRRecovery(self):
            if self.PRRecoveryCheckBox.isChecked():
                    self.PRRecoveryValue.setEnabled(True)
            else:
                    self.PRRecoveryValue.setEnabled(False)
                    self.PRRecoveryValue.setText("0.025")

    def ActivateMembranePotential(self):
            if self.MembranePotentialCheckBox.isChecked():
                    self.MembranePotentialValue.setEnabled(True)
            else:
                    self.MembranePotentialValue.setEnabled(False)
                    self.MembranePotentialValue.setText("-70")

    def ActivateNoiseLevel(self):
            if self.NoiseLevelCheckBox.isChecked():
                    self.NoiseLevelSlider.setEnabled(True)
            else:
                    self.NoiseLevelSlider.setEnabled(False)
                    self.NoiseLevelSlider.setValue(0)

    def ActivateSynapticGain1(self):
            if self.SynapticGain1CheckBox.isChecked():
                    self.SynapticGain1Slider.setEnabled(True)
            else:
                    self.SynapticGain1Slider.setEnabled(False)
                    self.SynapticGain1Slider.setValue(0)

    def ActivateSynapse1Decay(self):
            if self.Synapse1DecayCheckBox.isChecked():
                    self.Synapse1DecayValue.setEnabled(True)
            else:
                    self.Synapse1DecayValue.setEnabled(False)
                    self.Synapse1DecayValue.setText("0.995")

    def ActivateSynapticGain2(self):
            if self.SynapticGain2CheckBox.isChecked():
                    self.SynapticGain2Slider.setEnabled(True)
            else:
                    self.SynapticGain2Slider.setEnabled(False)
                    self.SynapticGain2Slider.setValue(0)

    def ActivateSynapse2Decay(self):
            if self.Synapse2DecayCheckBox.isChecked():
                    self.Synapse2DecayValue.setEnabled(True)
            else:
                    self.Synapse2DecayValue.setEnabled(False)
                    self.Synapse2DecayValue.setText("0.990")


