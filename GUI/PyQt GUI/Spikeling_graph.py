#from PyQt6 import QtCore, QtGui, QtWidgets, QtSerialPort
#from PyQt6.QtCore import QIODevice, QTimer
from PyQt5 import QtCore, QtGui, QtWidgets, QtSerialPort
from PyQt5.QtCore import QIODevice, QTimer
#from PySide2.QtCore import QIODevice, QTimer
import pyqtgraph
import collections
import serial
import numpy as np
import pandas as pd
import Data_recording
import Settings

BaudRate = 115200


TxStimFre = "F"
TxStimStr = "F"
TxStimCus = "F"
TxPDGain = "F"
TxPDDecay = "F"
TxPDRecovery = "F"
TxVm = "F"
TxNoise = "F"
TxSyn1Gain = "F"
TxSyn1Decay = "F"
TxSyn2Gain = "F"
TxSyn2Decay = "F"
TxMode = "F"
Txa = "F"
Txb = "F"
Txc = "F"
Txd = "F"

SerialTx = [TxStimFre,TxStimStr,TxStimCus,
            TxPDGain,TxPDDecay,TxPDRecovery,
            TxVm,TxNoise,
            TxSyn1Gain,TxSyn1Decay,
            TxSyn2Gain,TxSyn2Decay,
            TxMode, Txa, Txb, Txc, Txd]


def ReadSerial(self):
    self.recordflag = False
    self.Dataset0 = Data_recording.DynamicArray()
    self.Dataset1 = Data_recording.DynamicArray()
    self.Dataset2 = Data_recording.DynamicArray()
    self.Dataset3 = Data_recording.DynamicArray()
    self.Dataset4 = Data_recording.DynamicArray()
    self.Dataset5 = Data_recording.DynamicArray()
    self.Dataset6 = Data_recording.DynamicArray()

    self.ui.Spikeling_Oscilloscope_widget.clear()
    COM = self.ui.Spikeling_SelectPortComboBox.currentText()
    serial_port = serial.Serial(port=COM, baudrate=BaudRate)


    sampleinterval = 1
    timewindow = 750.
    min_range = -90
    max_range = 30
    stimrange = ((-min_range) + max_range) / 2

    self._interval = int(sampleinterval)
    self._bufsize = int(timewindow / sampleinterval)

    self.databuffer0 = collections.deque([0.0] * self._bufsize, self._bufsize)
    self.databuffer1 = collections.deque([0.0] * self._bufsize, self._bufsize)
    self.databuffer2 = collections.deque([0.0] * self._bufsize, self._bufsize)
    self.databuffer3 = collections.deque([0.0] * self._bufsize, self._bufsize)
    self.databuffer4 = collections.deque([0.0] * self._bufsize, self._bufsize)
    self.databuffer5 = collections.deque([0.0] * self._bufsize, self._bufsize)
    self.databuffer6 = collections.deque([0.0] * self._bufsize, self._bufsize)

    self.x = np.linspace(-timewindow, 0.0, self._bufsize)
    self.y0 = np.zeros(self._bufsize, dtype=float)
    self.y1 = np.zeros(self._bufsize, dtype=float)
    self.y2 = np.zeros(self._bufsize, dtype=float)
    self.y3 = np.zeros(self._bufsize, dtype=float)
    self.y4 = np.zeros(self._bufsize, dtype=float)
    self.y5 = np.zeros(self._bufsize, dtype=float)
    self.y6 = np.zeros(self._bufsize, dtype=float)

    self.ui.Spikeling_Oscilloscope_widget.showGrid(x=True, y=True)
    self.ui.Spikeling_Oscilloscope_widget.setRange(yRange=[-90, 30])
    self.ui.Spikeling_Oscilloscope_widget.setLabel('left', 'Membrane potential', 'mV')
    self.ui.Spikeling_Oscilloscope_widget.setLabel('bottom', 'time', 'ms')
    self.ui.Spikeling_Oscilloscope_widget.setLabel('right', 'Current Input', 'a.u.')

    self.CurrentPlots = pyqtgraph.ViewBox()
    self.ui.Spikeling_Oscilloscope_widget.scene().addItem(self.CurrentPlots)
    self.CurrentPlots.setXLink(self.ui.Spikeling_Oscilloscope_widget)
    self.CurrentPlots.setRange(yRange=[-100, 100])
    self.ui.Spikeling_Oscilloscope_widget.getAxis("right").linkToView(self.CurrentPlots)

    self.curve5 = self.ui.Spikeling_Oscilloscope_widget.plot(self.x, self.y5, pen=(Settings.DarkSolarized[8]))
    self.curve5.clear()
    self.curve3 = self.ui.Spikeling_Oscilloscope_widget.plot(self.x, self.y3, pen=(Settings.DarkSolarized[6]))
    self.curve3.clear()
    self.curve1 = self.ui.Spikeling_Oscilloscope_widget.plot(self.x, self.y1, pen=(Settings.DarkSolarized[5]))
    self.curve1.clear()
    self.curve0 = self.ui.Spikeling_Oscilloscope_widget.plot(self.x, self.y0, pen=(Settings.DarkSolarized[3]))
    self.curve0.clear()

    self.curve6 = pyqtgraph.PlotCurveItem(self.x, self.y6, pen=(Settings.DarkSolarized[9]))
    self.curve6.clear()
    self.curve4 = pyqtgraph.PlotCurveItem(self.x, self.y4, pen=(Settings.DarkSolarized[7]))
    self.curve4.clear()
    self.curve2 = pyqtgraph.PlotCurveItem(self.x, self.y2, pen=(Settings.DarkSolarized[4]))
    self.curve2.clear()

    self.CurrentPlots.addItem(self.curve6)
    self.CurrentPlots.addItem(self.curve4)
    self.CurrentPlots.addItem(self.curve2)

    def updateViews():
        self.CurrentPlots.setGeometry(self.ui.Spikeling_Oscilloscope_widget.getViewBox().sceneBoundingRect())
        self.CurrentPlots.linkedViewChanged(self.ui.Spikeling_Oscilloscope_widget.getViewBox(), self.CurrentPlots.XAxis)

    self.ui.Spikeling_Oscilloscope_widget.getViewBox().sigResized.connect(updateViews)

    def getdata0():
        rx = serial_port.readline()
        rx_serial = str(rx, 'utf8').strip()
        data = rx_serial.split(',')
        v = data[0]
        return v

    def getdata1():
        rx = serial_port.readline()
        rx_serial = str(rx, 'utf8').strip()
        data = rx_serial.split(',')
        s = data[1]
        return s

    def getdata2():
        rx = serial_port.readline()
        rx_serial = str(rx, 'utf8').strip()
        data = rx_serial.split(',')
        i = data[2]
        return i

    def getdata3():
        rx = serial_port.readline()
        rx_serial = str(rx, 'utf8').strip()
        data = rx_serial.split(',')
        v2 = data[3]
        return v2

    def getdata4():
        rx = serial_port.readline()
        rx_serial = str(rx, 'utf8').strip()
        data = rx_serial.split(',')
        i2 = data[4]
        return i2

    def getdata5():
        rx = serial_port.readline()
        rx_serial = str(rx, 'utf8').strip()
        data = rx_serial.split(',')
        v3 = data[5]
        return v3

    def getdata6():
        rx = serial_port.readline()
        rx_serial = str(rx, 'utf8').strip()
        data = rx_serial.split(',')
        i3 = data[6]
        return i3

    def updateplot():
        if self.ui.Spikeling_StimFre_checkBox.isChecked():
            SerialTx[0] = str(-(self.ui.Spikeling_StimFre_slider.value()))
        else:
            SerialTx[0] = "F"

        if self.ui.Spikeling_StimStr_checkBox.isChecked():
            SerialTx[1] = str((self.ui.Spikeling_StimStrSlider.value()))
        else:
            SerialTx[1] = "F"

        if self.ui.Spikeling_CustomStimulus_checkBox.isChecked():
            SerialTx[2] = "F"
        else:
            SerialTx[2] = "F"

        if self.ui.Spikeling_PR_PhotoGain_checkBox.isChecked():
            SerialTx[3] = str(self.ui.Spikeling_PR_PhotoGain_slider.value())
        else:
            SerialTx[3] = "F"

        if self.ui.Spikeling_PR_Decay_checkBox.isChecked():
            SerialTx[4] = str(self.ui.Spikeling_PR_Decay_value.text())
        else:
            SerialTx[4] = "F"

        if self.ui.Spikeling_PR_Recovery_checkBox.isChecked():
            SerialTx[5] = str(self.ui.Spikeling_PR_Recovery_value.text())
        else:
            SerialTx[5] = "F"

        if self.ui.Spikeling_PatchClamp_checkBox.isChecked():
            SerialTx[6] = str(self.ui.Spikeling_PatchClamp_slider.value())
        else:
            SerialTx[6] = "F"

        if self.ui.Spikeling_Noise_checkBox.isChecked():
            SerialTx[7] = str(self.ui.Spikeling_Noise_slider.value())
        else:
            SerialTx[7] = "F"

        if self.ui.Spikeling_Synapse1_checkBox.isChecked():
            SerialTx[8] = str(self.ui.Spikeling_Synapse1_slider.value())
        else:
            SerialTx[8] = "F"

        if self.ui.Spikeling_Synapse1_Decay_checkBox.isChecked():
            SerialTx[9] = str(self.ui.Spikeling_Synapse1_Decay_value.text())
        else:
            SerialTx[9] = "F"

        if self.ui.Spikeling_Synapse2_checkBox.isChecked():
            SerialTx[10] = str(self.ui.Spikeling_Synapse2_slider.value())
        else:
            SerialTx[10] = "F"

        if self.ui.Spikeling_Synapse2_Decay_checkBox.isChecked():
            SerialTx[11] = str(self.ui.Spikeling_Synapse2_Decay_value.text())
        else:
            SerialTx[11] = "F"

        if self.ui.Spikeling_VmCheckbox.isChecked():
            self.databuffer0.append(getdata0())
            self.y0[:] = self.databuffer0
            self.curve0.setData(self.x, self.y0)
        else:
            self.curve0.clear()

        if self.ui.Spikeling_StimulusCheckbox.isChecked():
            self.databuffer1.append(getdata1())
            self.y1[:] = self.databuffer1
            self.curve1.setData(self.x, self.y1 * stimrange - 80)
        else:
            self.curve1.clear()

        if self.ui.Spikeling_InputCurrentCheckbox.isChecked():
            self.databuffer2.append(getdata2())
            self.y2[:] = self.databuffer2
            self.curve2.setData(self.x, self.y2)
        else:
            self.curve2.clear()

        if self.ui.Spikeling_Syn1VmCheckbox.isChecked():
            self.databuffer3.append(getdata3())
            self.y3[:] = self.databuffer3
            self.curve3.setData(self.x, self.y3)
        else:
            self.curve3.clear()

        if self.ui.Spikeling_Syn1InputCheckbox.isChecked():
            self.databuffer4.append(getdata4())
            self.y4[:] = self.databuffer4
            self.curve4.setData(self.x, self.y4)
        else:

            self.curve4.clear()

        if self.ui.Spikeling_Syn2VmCheckbox.isChecked():
            self.databuffer5.append(getdata5())
            self.y5[:] = self.databuffer5
            self.curve5.setData(self.x, self.y5)
        else:
            self.curve5.clear()

        if self.ui.Spikeling_Syn2InputCheckbox.isChecked():
            self.databuffer6.append(getdata6())
            self.y6[:] = self.databuffer6
            self.curve6.setData(self.x, self.y6)
        else:
            self.curve6.clear()


        tx0 = SerialTx[0]
        Tx0 = tx0 + ';'
        serial_port.write(Tx0.encode())

        tx1 = SerialTx[1]
        Tx1 = tx1 + ';'
        serial_port.write(Tx1.encode())

        tx2 = SerialTx[2]
        Tx2 = tx2 + ';'
        serial_port.write(Tx2.encode())

        tx3 = SerialTx[3]
        Tx3 = tx3 + ';'
        serial_port.write(Tx3.encode())

        tx4 = SerialTx[4]
        Tx4 = tx4 + ';'
        serial_port.write(Tx4.encode())

        tx5 = SerialTx[5]
        Tx5 = tx5 + ';'
        serial_port.write(Tx5.encode())

        tx6 = SerialTx[6]
        Tx6 = tx6 + ';'
        serial_port.write(Tx6.encode())

        tx7 = SerialTx[7]
        Tx7 = tx7 + ';'
        serial_port.write(Tx7.encode())

        tx8 = SerialTx[8]
        Tx8 = tx8 + ';'
        serial_port.write(Tx8.encode())

        tx9 = SerialTx[9]
        Tx9 = tx9 + ';'
        serial_port.write(Tx9.encode())

        tx10 = SerialTx[10]
        Tx10 = tx10 + ';'
        serial_port.write(Tx10.encode())

        tx11 = SerialTx[11]
        Tx11 = tx11 + ';'
        serial_port.write(Tx11.encode())

        tx12 = SerialTx[12]
        Tx12 = tx12 + ';'
        serial_port.write(Tx12.encode())

        tx13 = SerialTx[13]
        Tx13 = tx13 + ';'
        serial_port.write(Tx13.encode())

        tx14 = SerialTx[14]
        Tx14 = tx14 + ';'
        serial_port.write(Tx14.encode())

        tx15 = SerialTx[15]
        Tx15 = tx15 + ';'
        serial_port.write(Tx15.encode())

        tx16 = SerialTx[16]
        Tx16 = tx16 + ';'
        serial_port.write(Tx16.encode())

        # rx = serial_port.readline()
        # rx_serial = str(rx, 'utf8').strip()
        # data = rx_serial.split(',')

        if self.ui.Spikeling_DataRecording_Record_pushButton.isChecked() == False and self.recordflag == True:
            self.Dataset = np.empty([7, len(self.Dataset0)], dtype=float)
            for i in range(len(self.Dataset0)):
                self.Dataset[0][i] = self.Dataset0[i]
                self.Dataset[1][i] = self.Dataset1[i]
                self.Dataset[2][i] = self.Dataset2[i]
                self.Dataset[3][i] = self.Dataset3[i]
                self.Dataset[4][i] = self.Dataset4[i]
                self.Dataset[5][i] = self.Dataset5[i]
                self.Dataset[6][i] = self.Dataset6[i]

            dict = {'Spikeling Vm': self.Dataset[0], 'Stimulus': self.Dataset[1], 'Total Current Input': self.Dataset[2],
                    'Synapse 1 Vm': self.Dataset[3], 'Synapse 1 Input': self.Dataset[4],
                    'Synapse 2 Vm': self.Dataset[5], 'Synapse 2 Input': self.Dataset[6]}
            df = pd.DataFrame(dict)
            self.RecordingFileName = str(self.ui.Spikeling_SelectedFolderLabel.text())
            df.to_csv(self.RecordingFileName + '.csv', index=False)
            self.recordflag = False

        if self.ui.Spikeling_DataRecording_Record_pushButton.isChecked() == True:
            self.recordflag = True

            self.Dataset0.append(self.y0[-1])
            self.Dataset1.append(self.y1[-1])
            self.Dataset2.append(self.y2[-1])
            self.Dataset3.append(self.y3[-1])
            self.Dataset4.append(self.y4[-1])
            self.Dataset5.append(self.y5[-1])
            self.Dataset6.append(self.y6[-1])

    # QTimer
    self.timer = QtCore.QTimer()
    self.timer.timeout.connect(lambda: updateplot())
    self.timer.start(self._interval)
