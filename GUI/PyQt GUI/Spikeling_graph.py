from PyQt6 import QtCore, QtGui, QtWidgets, QtSerialPort
from PyQt6.QtCore import QIODevice, QTimer
import pyqtgraph
import collections
import serial
import numpy as np

BaudRate = 115200
DarkSolarized = [[0,30,38],[131,148,150],[220,50,47],[38,139,210],[133,153,0],[203,75,22],[42,161,152],[181,137,0],[108,113,196]]

TxStimFre = "None"
TxStimStr = "None"
TxStimCus = "None"
TxPDGain = "None"
TxPDDecay = "None"
TxPDRecovery = "None"
TxVm = "None"
TxNoise = "None"
TxSyn1Gain = "None"
TxSyn1Decay = "None"
TxSyn2Gain = "None"
TxSyn2Decay = "None"
TxMode = "None"
Txa = "None"
Txb = "None"
Txc = "None"
Txd = "None"

SerialTx = [TxStimFre,TxStimStr,TxStimCus,
            TxPDGain,TxPDDecay,TxPDRecovery,
            TxVm,TxNoise,
            TxSyn1Gain,TxSyn1Decay,
            TxSyn2Gain,TxSyn2Decay,
            TxMode, Txa, Txb, Txc, Txd]


def ReadSerial(self):
    self.Oscilloscope1.clear()
    COM = self.SelectPortComboBox.currentText()
    serial_port = serial.Serial(port=COM, baudrate=BaudRate)

    sampleinterval = 0.01
    timewindow = 5.
    min_range = -90
    max_range = 30
    stimrange = ((-min_range) + max_range) / 2

    self._interval = int(sampleinterval * 1000)
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

    self.Oscilloscope1.showGrid(x=True, y=True)
    self.Oscilloscope1.setRange(yRange=[-90, 30])
    self.Oscilloscope1.setLabel('left', 'Membrane potential', 'mV')
    self.Oscilloscope1.setLabel('bottom', 'time', 'ms')
    self.Oscilloscope1.setLabel('right', 'Current Input', 'a.u.')

    self.CurrentPlots = pyqtgraph.ViewBox()
    self.Oscilloscope1.scene().addItem(self.CurrentPlots)
    self.CurrentPlots.setXLink(self.Oscilloscope1)
    self.CurrentPlots.setRange(yRange=[-100, 100])
    self.Oscilloscope1.getAxis("right").linkToView(self.CurrentPlots)

    self.curve5 = self.Oscilloscope1.plot(self.x, self.y5, pen=(DarkSolarized[7]))
    self.curve5.clear()
    self.curve3 = self.Oscilloscope1.plot(self.x, self.y3, pen=(DarkSolarized[5]))
    self.curve3.clear()
    self.curve1 = self.Oscilloscope1.plot(self.x, self.y1, pen=(DarkSolarized[3]))
    self.curve1.clear()
    self.curve0 = self.Oscilloscope1.plot(self.x, self.y0, pen=(DarkSolarized[2]))
    self.curve0.clear()

    self.curve6 = pyqtgraph.PlotCurveItem(self.x, self.y6, pen=(DarkSolarized[8]))
    self.curve6.clear()
    self.curve4 = pyqtgraph.PlotCurveItem(self.x, self.y4, pen=(DarkSolarized[6]))
    self.curve4.clear()
    self.curve2 = pyqtgraph.PlotCurveItem(self.x, self.y2, pen=(DarkSolarized[4]))
    self.curve2.clear()

    self.CurrentPlots.addItem(self.curve6)
    self.CurrentPlots.addItem(self.curve4)
    self.CurrentPlots.addItem(self.curve2)

    def updateViews():
        self.CurrentPlots.setGeometry(self.Oscilloscope1.getViewBox().sceneBoundingRect())
        self.CurrentPlots.linkedViewChanged(self.Oscilloscope1.getViewBox(), self.CurrentPlots.XAxis)

    self.Oscilloscope1.getViewBox().sigResized.connect(updateViews)


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
        if self.StimFreCheckBox.isChecked():
            SerialTx[0] = str(-(self.StimFreSlider.value()))
        else:
            SerialTx[0] = "None"

        if self.StimStrCheckBox.isChecked():
            SerialTx[1] = str((self.StimStrSlider.value()))
        else:
            SerialTx[1] = "None"

        if self.CustomStimulusCheckBox.isChecked():
            SerialTx[2] = "None"
        else:
            SerialTx[2] = "None"

        if self.PhotoGainCheckBox.isChecked():
            SerialTx[3] = str(self.PhotoGainSlider.value())
        else:
            SerialTx[3] = "None"

        if self.PRDecayCheckBox.isChecked():
            SerialTx[4] = str(self.PRDecayValue.text())
        else:
            SerialTx[4] = "None"

        if self.PRRecoveryCheckBox.isChecked():
            SerialTx[5] = str(self.PRRecoveryValue.text())
        else:
            SerialTx[5] = "None"

        if self.MembranePotentialCheckBox.isChecked():
            SerialTx[6] = str(self.MembranePotentialValue.text())
        else:
            SerialTx[6] = "None"

        if self.NoiseLevelCheckBox.isChecked():
            SerialTx[7] = str(self.NoiseLevelSlider.value())
        else:
            SerialTx[7] = "None"

        if self.SynapticGain1CheckBox.isChecked():
            SerialTx[8] = str(self.SynapticGain1Slider.value())
        else:
            SerialTx[8] = "None"

        if self.Synapse1DecayCheckBox.isChecked():
            SerialTx[9] = str(self.Synapse1DecayValue.text())
        else:
            SerialTx[9] = "None"

        if self.SynapticGain2CheckBox.isChecked():
            SerialTx[10] = str(self.SynapticGain2Slider.value())
        else:
            SerialTx[10] = "None"

        if self.Synapse2DecayCheckBox.isChecked():
            SerialTx[11] = str(self.Synapse2DecayValue.text())
        else:
            SerialTx[11] = "None"

        if self.Osc1VmCheckbox.isChecked():
            self.databuffer0.append(getdata0())
            self.y0[:] = self.databuffer0
            self.curve0.setData(self.x, self.y0)
        else:
            self.curve0.clear()

        if self.Osc1StimulusCheckbox.isChecked():
            self.databuffer1.append(getdata1())
            self.y1[:] = self.databuffer1
            self.curve1.setData(self.x, self.y1 * stimrange - 80)
        else:
            self.curve1.clear()

        if self.Osc1InputCurrentCheckbox.isChecked():
            self.databuffer2.append(getdata2())
            self.y2[:] = self.databuffer2
            self.curve2.setData(self.x, self.y2)
        else:
            self.curve2.clear()

        if self.Osc1Syn1VmCheckbox.isChecked():
            self.databuffer3.append(getdata3())
            self.y3[:] = self.databuffer3
            self.curve3.setData(self.x, self.y3)
        else:
            self.curve3.clear()

        if self.Osc1Syn1InputCheckbox.isChecked():
            self.databuffer4.append(getdata4())
            self.y4[:] = self.databuffer4
            self.curve4.setData(self.x, self.y4)
        else:
            self.curve4.clear()

        if self.Osc1Syn2VmCheckbox.isChecked():
            self.databuffer5.append(getdata5())
            self.y5[:] = self.databuffer5
            self.curve5.setData(self.x, self.y5)
        else:
            self.curve5.clear()

        if self.Osc1Syn2InputCheckbox.isChecked():
            self.databuffer6.append(getdata6())
            self.y6[:] = self.databuffer6
            self.curve6.setData(self.x, self.y6)
        else:
            self.curve6.clear()

        # tx = ';'.join(SerialTx)
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

        rx = serial_port.readline()
        rx_serial = str(rx, 'utf8').strip()
        data = rx_serial.split(',')
        print(data[5])




    # QTimer
    self.timer = QtCore.QTimer()
    self.timer.timeout.connect(lambda: updateplot())
    self.timer.start(self._interval)