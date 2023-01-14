from PyQt6.QtWidgets import QFileDialog #,QWidget
import numpy as np
import pandas as pd
#import pyqtgraph as pg
#from pyqtgraph.Qt import QtGui, QtCore

#from numpy import random

#from pyqtgraph.Qt import QtGui, QtCore
#from pyqtgraph import MultiPlotWidget
#from pyqtgraph.metaarray import *

DarkSolarized = [[0, 30, 38], [131, 148, 150],
                 [220, 50, 47], [38, 139, 210], [133, 153, 0],
                 [203, 75, 22], [42, 161, 152], [181, 137, 0], [108, 113, 196]]


class Spikeling103():

    def ShowPage(self):
        self.ui.mainbody_stackedWidget.setCurrentWidget(self.ui.page_103)
        self.ui.DataAnalysis_Display_StackedWidget.setCurrentWidget(self.ui.page_103_1_0)
        self.ui.DataAnalysis_Oscilloscope_widget1_0_0.setBackground(DarkSolarized[0])
        self.ui.DataAnalysis_Oscilloscope_widget1_0_1.setBackground(DarkSolarized[0])
        self.ui.DataAnalysis_Oscilloscope_widget1_0_2.setBackground(DarkSolarized[0])
        self.ui.DataAnalysis_Oscilloscope_widget1_0_3.setBackground(DarkSolarized[0])

    def LoadData(self):
        FileName = QFileDialog.getOpenFileName(self,
                                               caption='Select recording file to load',
                                               directory="./Recordings",
                                               filter='csv files (*.csv)')
        self.DataAnalysis_LoadData_label.setText(FileName[0])
        Df = pd.read_csv(FileName[0])
        self.df_DataAnalysis_Vm = Df["Spikeling Vm"]
        self.df_DataAnalysis_ITotal = Df["Total Current Input"]
        self.df_DataAnalysis_Stimulus = Df["Stimulus"]
        self.df_DataAnalysis_Synapse1Vm = Df["Synapse 1 Vm"]
        self.df_DataAnalysis_Synapse1Input = Df["Synapse 1 Input"]
        self.df_DataAnalysis_Synapse2Vm = Df["Synapse 2 Vm"]
        self.df_DataAnalysis_Synapse2Input = Df["Synapse 2 Input"]

    def DisplayRawData(self):
        self.ui.DataAnalysis_Display_StackedWidget.setCurrentWidget(self.ui.page_103_1_0)

        self.ui.df_DataAnalysis_x = np.linspace(0, len(self.ui.df_DataAnalysis_Vm) - 1, len(self.ui.df_DataAnalysis_Vm))

        self.ui.df_DataAnalysis_y0 = np.zeros(len(self.ui.df_DataAnalysis_Vm))
        self.ui.df_DataAnalysis_y0 = self.ui.df_DataAnalysis_Vm

        self.ui.df_DataAnalysis_y1 = np.zeros(len(self.ui.df_DataAnalysis_Vm))
        self.ui.df_DataAnalysis_y1 = self.ui.df_DataAnalysis_ITotal

        self.ui.df_DataAnalysis_y2 = np.zeros(len(self.ui.df_DataAnalysis_Vm))
        self.ui.df_DataAnalysis_y2 = self.ui.df_DataAnalysis_Stimulus

        self.ui.df_DataAnalysis_y3 = np.zeros(len(self.ui.df_DataAnalysis_Vm))
        self.ui.df_DataAnalysis_y3 = self.ui.df_DataAnalysis_Synapse1Vm

        self.ui.df_DataAnalysis_y4 = np.zeros(len(self.ui.df_DataAnalysis_Vm))
        self.ui.df_DataAnalysis_y4 = self.ui.df_DataAnalysis_Synapse1Input

        self.ui.df_DataAnalysis_y5 = np.zeros(len(self.ui.df_DataAnalysis_Vm))
        self.ui.df_DataAnalysis_y5 = self.ui.df_DataAnalysis_Synapse2Vm

        self.ui.df_DataAnalysis_y6 = np.zeros(len(self.ui.df_DataAnalysis_Vm))
        self.ui.df_DataAnalysis_y6 = self.ui.df_DataAnalysis_Synapse2Input


        self.ui.DataAnalysis_Oscilloscope_widget1_0_0.plot(x=self.ui.df_DataAnalysis_x, y=self.ui.df_DataAnalysis_y0,
                                                         pen=(DarkSolarized[2]))
        self.ui.DataAnalysis_Oscilloscope_widget1_0_1.plot(x=self.ui.df_DataAnalysis_x, y=self.ui.df_DataAnalysis_y1,
                                                         pen=(DarkSolarized[4]))
        self.ui.DataAnalysis_Oscilloscope_widget1_0_2.plot(x=self.ui.df_DataAnalysis_x, y=self.ui.df_DataAnalysis_y2,
                                                           pen=(DarkSolarized[3]))
        self.ui.DataAnalysis_Oscilloscope_widget1_0_3.plot(x=self.ui.df_DataAnalysis_x, y=self.ui.df_DataAnalysis_y6,
                                                         pen=(DarkSolarized[8]))
        self.ui.DataAnalysis_Oscilloscope_widget1_0_3.plot(x=self.ui.df_DataAnalysis_x, y=self.ui.df_DataAnalysis_y4,
                                                         pen=(DarkSolarized[6]))

        self.ui.DataAnalysis_Oscilloscope_widget1_1_0.plot(x=self.ui.df_DataAnalysis_x, y=self.ui.df_DataAnalysis_y3,
                                                         pen=(DarkSolarized[5]))
        self.ui.DataAnalysis_Oscilloscope_widget1_1_1.plot(x=self.ui.df_DataAnalysis_x, y=self.ui.df_DataAnalysis_y4,
                                                         pen=(DarkSolarized[6]))
        self.ui.DataAnalysis_Oscilloscope_widget1_1_2.plot(x=self.ui.df_DataAnalysis_x, y=self.ui.df_DataAnalysis_y2,
                                                           pen=(DarkSolarized[3]))

        self.ui.DataAnalysis_Oscilloscope_widget1_2_0.plot(x=self.ui.df_DataAnalysis_x, y=self.ui.df_DataAnalysis_y5,
                                                         pen=(DarkSolarized[7]))
        self.ui.DataAnalysis_Oscilloscope_widget1_2_1.plot(x=self.ui.df_DataAnalysis_x, y=self.ui.df_DataAnalysis_y6,
                                                         pen=(DarkSolarized[8]))
        self.ui.DataAnalysis_Oscilloscope_widget1_2_2.plot(x=self.ui.df_DataAnalysis_x, y=self.ui.df_DataAnalysis_y2,
                                                           pen=(DarkSolarized[3]))

        self.ui.DataAnalysis_Spike_frame.setStyleSheet("background-color: rgb(7,54,66)")
        self.ui.DataAnalysis_Spike_lineEdit.setEnabled(True)
        self.ui.DataAnalysis_Spike_Display_pushButton.setEnabled(True)

    def FindSpike(self):
        self.ui.DataAnalysis_Display_StackedWidget.setCurrentWidget(self.ui.page_103_2_1)

        self.spike_threshold = self.ui.DataAnalysis_Spike_lineEdit.text()

        self.n_spikes0 = 0
        self.spike_points0 = []
        self.n_spikes1 = 0
        self.spike_points1 = []
        self.n_spikes2 = 0
        self.spike_points2 = []

        for x in range(1, len(self.ui.df_DataAnalysis_Vm) - 1):
            if (self.ui.df_DataAnalysis_Vm[x] > int(self.spike_threshold) and self.ui.df_DataAnalysis_Vm[x - 1] < int(
                    self.spike_threshold)):  # looks for all instances where subsequent Vm points jump from <10 to >10
                self.spike_points0.append(x)
                self.n_spikes0 += 1
                self.spike_points1.append(x)
                self.n_spikes1 += 1
                self.spike_points2.append(x)
                self.n_spikes2 += 1
        self.ui.DataAnalysis_Spike_result_label.setText(str(self.n_spikes0) + " spikes detected")

        # Compute spike rate
        self.ui.spike_rate0 = np.zeros(len(self.ui.df_DataAnalysis_Vm))
        self.ui.spike_rate1 = np.zeros(len(self.ui.df_DataAnalysis_Vm))
        self.ui.spike_rate2 = np.zeros(len(self.ui.df_DataAnalysis_Vm))

        for x in range(0, self.n_spikes0 - 1):
            self.current_rate0 = 1 / (self.spike_points0[x + 1] - self.spike_points0[x])
            self.ui.spike_rate0[self.spike_points0[x]:self.spike_points0[x + 1]] = self.current_rate0

        for x in range(0, self.n_spikes1 - 1):
            self.current_rate1 = 1 / (self.spike_points1[x + 1] - self.spike_points1[x])
            self.ui.spike_rate1[self.spike_points1[x]:self.spike_points1[x + 1]] = self.current_rate1

        for x in range(0, self.n_spikes2 - 1):
            self.current_rate2 = 1 / (self.spike_points2[x + 1] - self.spike_points2[x])
            self.ui.spike_rate2[self.spike_points2[x]:self.spike_points2[x + 1]] = self.current_rate2

        self.ui.DataAnalysis_Oscilloscope_widget2_0_0.setBackground(DarkSolarized[0])
        self.ui.DataAnalysis_Oscilloscope_widget2_0_1.setBackground(DarkSolarized[0])
        self.ui.DataAnalysis_Oscilloscope_widget2_0_2.setBackground(DarkSolarized[0])
        self.ui.DataAnalysis_Oscilloscope_widget2_0_3.setBackground(DarkSolarized[0])
        self.ui.DataAnalysis_Oscilloscope_widget2_1_0.setBackground(DarkSolarized[0])
        self.ui.DataAnalysis_Oscilloscope_widget2_1_1.setBackground(DarkSolarized[0])
        self.ui.DataAnalysis_Oscilloscope_widget2_1_2.setBackground(DarkSolarized[0])
        self.ui.DataAnalysis_Oscilloscope_widget2_1_3.setBackground(DarkSolarized[0])
        self.ui.DataAnalysis_Oscilloscope_widget2_2_0.setBackground(DarkSolarized[0])
        self.ui.DataAnalysis_Oscilloscope_widget2_2_1.setBackground(DarkSolarized[0])
        self.ui.DataAnalysis_Oscilloscope_widget2_2_2.setBackground(DarkSolarized[0])
        self.ui.DataAnalysis_Oscilloscope_widget2_2_3.setBackground(DarkSolarized[0])

        self.ui.ySpike0 = np.zeros(len(self.spike_points0))
        for i in range(len(self.spike_points0)):
            self.ui.ySpike0[i] = 45

        self.ui.DataAnalysis_Oscilloscope_widget2_0_0.plot(x=self.ui.df_DataAnalysis_x, y=self.ui.spike_rate0,
                                                           pen=(255, 255, 255))
        self.ui.DataAnalysis_Oscilloscope_widget2_0_1.plot(x=self.spike_points0, y=self.ui.ySpike0, pen=None,
                                                           symbol='o', symbolBrush=(220, 50, 47), symbolSize=5)
        self.ui.DataAnalysis_Oscilloscope_widget2_0_1.plot(x=self.ui.df_DataAnalysis_x, y=self.ui.df_DataAnalysis_y0,
                                                           pen=(DarkSolarized[2]))
        self.ui.DataAnalysis_Oscilloscope_widget2_0_2.plot(x=self.ui.df_DataAnalysis_x, y=self.ui.df_DataAnalysis_y1,
                                                           pen=(DarkSolarized[4]))
        self.ui.DataAnalysis_Oscilloscope_widget2_0_3.plot(x=self.ui.df_DataAnalysis_x, y=self.ui.df_DataAnalysis_y2,
                                                           pen=(DarkSolarized[3]))
        self.ui.DataAnalysis_Oscilloscope_widget2_1_0.plot(x=self.ui.df_DataAnalysis_x, y=self.ui.spike_rate1,
                                                           pen=(255, 255, 255))
        self.ui.DataAnalysis_Oscilloscope_widget2_1_2.plot(x=self.ui.df_DataAnalysis_x, y=self.ui.df_DataAnalysis_y4,
                                                           pen=(DarkSolarized[6]))
        self.ui.DataAnalysis_Oscilloscope_widget2_1_3.plot(x=self.ui.df_DataAnalysis_x, y=self.ui.df_DataAnalysis_y2,
                                                           pen=(DarkSolarized[3]))
        self.ui.DataAnalysis_Oscilloscope_widget2_2_0.plot(x=self.ui.df_DataAnalysis_x, y=self.ui.spike_rate2,
                                                           pen=(255, 255, 255))
        self.ui.DataAnalysis_Oscilloscope_widget2_2_2.plot(x=self.ui.df_DataAnalysis_x, y=self.ui.df_DataAnalysis_y6,
                                                           pen=(DarkSolarized[8]))
        self.ui.DataAnalysis_Oscilloscope_widget2_2_3.plot(x=self.ui.df_DataAnalysis_x, y=self.ui.df_DataAnalysis_y2,
                                                           pen=(DarkSolarized[3]))

        self.ui.DataAnalysis_Average_frame.setStyleSheet("background-color: rgb(7,54,66)")
        self.ui.DataAnalysis_Average_Display_pushButton.setEnabled(True)
        self.ui.DataAnalysis_Average_Save_pushButton.setEnabled(True)

    def AverageTraces(self):
        self.ui.DataAnalysis_Display_StackedWidget.setCurrentWidget(self.ui.page_103_3_1)

        self.ui.DataAnalysis_Oscilloscope_widget3_0_0.setBackground(DarkSolarized[0])
        self.ui.DataAnalysis_Oscilloscope_widget3_0_1.setBackground(DarkSolarized[0])
        self.ui.DataAnalysis_Oscilloscope_widget3_0_2.setBackground(DarkSolarized[0])
        self.ui.DataAnalysis_Oscilloscope_widget3_0_3.setBackground(DarkSolarized[0])
        self.ui.DataAnalysis_Oscilloscope_widget3_1_0.setBackground(DarkSolarized[0])
        self.ui.DataAnalysis_Oscilloscope_widget3_1_1.setBackground(DarkSolarized[0])
        self.ui.DataAnalysis_Oscilloscope_widget3_1_2.setBackground(DarkSolarized[0])
        self.ui.DataAnalysis_Oscilloscope_widget3_1_3.setBackground(DarkSolarized[0])
        self.ui.DataAnalysis_Oscilloscope_widget3_2_0.setBackground(DarkSolarized[0])
        self.ui.DataAnalysis_Oscilloscope_widget3_2_1.setBackground(DarkSolarized[0])
        self.ui.DataAnalysis_Oscilloscope_widget3_2_2.setBackground(DarkSolarized[0])
        self.ui.DataAnalysis_Oscilloscope_widget3_2_3.setBackground(DarkSolarized[0])

        self.stimulus_times = []
        for x in range(0, len(self.ui.df_DataAnalysis_y0) - 1):  # goes through each timepoint
            if (self.ui.df_DataAnalysis_y2[x] < self.ui.df_DataAnalysis_y2[
                x + 1]):  # checks if the stimulus went from 0 to 1
                self.stimulus_times.append(x)  ## make a list of times (in points) when stimulus increased
        self.loop_duration = self.stimulus_times[1] - self.stimulus_times[0]  # compute arraylength for single stimulus

        self.Spikerate0_loops = []
        self.Vm0_loops = []
        self.Spike0_loops = []
        self.ITotal_loops = []
        self.Stim_loops = []

        self.stimulus_times = np.where(self.ui.df_DataAnalysis_y2[:] > np.roll(self.ui.df_DataAnalysis_y2[:], axis=0,
                                                                               shift=1))  ## make a list of times when stimulus increased (again)
        self.Spikerate0_loops = np.vstack(
            [self.ui.spike_rate0[x:x + self.loop_duration] for x in self.stimulus_times[0][:-1]])
        self.Vm0_loops = np.vstack(
            [self.ui.df_DataAnalysis_y0[x:x + self.loop_duration] for x in self.stimulus_times[0][:-1]])
        self.ITotal_loops = np.vstack(
            [self.ui.df_DataAnalysis_y1[x:x + self.loop_duration] for x in self.stimulus_times[0][:-1]])
        self.Stim_loops = np.vstack(
            [self.ui.df_DataAnalysis_y2[x:x + self.loop_duration] for x in self.stimulus_times[0][:-1]])
        for i, x in enumerate(self.stimulus_times[0][:-1]):
            self.Spike0_loops.append(
                [self.ui.df_DataAnalysis_x[sp] - self.ui.df_DataAnalysis_x[x] for sp in self.spike_points0 if
                 sp > x and sp < x + self.loop_duration])

        self.ui.DataAnalysis_Average_label.setText(
            str(len(self.Stim_loops)) + " loops (" + str(self.loop_duration) + "ms each)")

        self.ui.StimLoop_x = np.linspace(0, self.loop_duration - 1, self.loop_duration)

        for i in range(0, len(self.Stim_loops) - 1):
            self.ui.DataAnalysis_Oscilloscope_widget3_0_0.plot(x=self.ui.StimLoop_x, y=self.Spikerate0_loops[i],
                                                               pen=(DarkSolarized[1]))

            self.ui.ySpikeLoops0 = np.zeros(len(self.Spike0_loops[i]))
            for j in range(len(self.Spike0_loops[i])):
                self.ui.ySpikeLoops0[j] = i
            self.ui.DataAnalysis_Oscilloscope_widget3_0_1.plot(x=self.Spike0_loops[i], y=self.ui.ySpikeLoops0, pen=None,
                                                               symbol='o', symbolBrush=(220, 50, 47), symbolSize=5)
            self.ui.DataAnalysis_Oscilloscope_widget3_0_1.setXRange(0, self.loop_duration)

            self.ui.DataAnalysis_Oscilloscope_widget3_0_2.plot(x=self.ui.StimLoop_x, y=self.Vm0_loops[i],
                                                               pen=(DarkSolarized[1]))
            self.ui.DataAnalysis_Oscilloscope_widget3_0_3.plot(x=self.ui.StimLoop_x, y=self.ITotal_loops[i],
                                                               pen=(DarkSolarized[1]))

        self.SpikeRate_mean = np.mean(self.Spikerate0_loops, axis=0)
        self.Vm0_mean = np.mean(self.Vm0_loops, axis=0)
        self.ITotal_mean = np.mean(self.ITotal_loops, axis=0)
        self.Stim_mean = np.mean(self.Stim_loops, axis=0)

        self.ui.DataAnalysis_Oscilloscope_widget3_0_0.plot(x=self.ui.StimLoop_x, y=self.SpikeRate_mean,
                                                           pen={'color':(255, 255, 255), 'width':2})
        self.ui.DataAnalysis_Oscilloscope_widget3_0_2.plot(x=self.ui.StimLoop_x, y=self.Vm0_mean,
                                                           pen={'color':(DarkSolarized[2]), 'width':2})
        self.ui.DataAnalysis_Oscilloscope_widget3_0_3.plot(x=self.ui.StimLoop_x, y=self.ITotal_mean,
                                                           pen={'color':(DarkSolarized[4]), 'width':2})


