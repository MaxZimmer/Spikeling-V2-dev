# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Spikeling_UI.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from pyqtgraph import PlotWidget
from Custom_Widgets.Widgets import QCustomSlideMenu

import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1280, 720)
        MainWindow.setMinimumSize(QSize(1280, 720))
        MainWindow.setStyleSheet(u"*{\n"
"	border: none;\n"
"	background-color: transparent;\n"
"	background: transparent;\n"
"	padding: 0;\n"
"	margin: 0;\n"
"	color: rgb(147,161,161);\n"
"}\n"
"\n"
"#centralwidget{\n"
"	background-color:  rgb(0, 43, 54);\n"
"}\n"
"\n"
"#leftMenuSubContainer{\n"
"	background-color: rgb(11, 30, 38);\n"
"}\n"
"\n"
"#leftMenuSubContainer QPushButton{\n"
"	text-align: left;\n"
"	padding: 10px 5px;\n"
"	border-top-left-radius:15px;\n"
"	border-bottom-left-radius: 15px;\n"
"	background-color: rgb(0, 43, 54);\n"
"}\n"
"\n"
"#centerMenuSubContainer{\n"
"	background-color: rgb(0, 43, 54);\n"
"}\n"
"\n"
"#centerMenuSubContainer_exit_frame{\n"
"	background-color: rgb(11, 30, 38);\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"#centerMenuSubContainer_menu_stackedwidget QPushButton{\n"
"	text-align: center;\n"
"	padding: 10px 0px;\n"
"	border-radius:20px;\n"
"	background-color: rgb(7, 54, 66);\n"
"}\n"
"\n"
"#header_widget{\n"
"	background-color: rgb(11, 30, 38);\n"
"}\n"
"\n"
"#footer_widget{\n"
"	background-color: rgb(11, 30, "
                        "38);\n"
"}\n"
"\n"
"#Spikeling_rightMenuSubContainer{\n"
"	background-color: rgb(11, 30, 38);\n"
"}\n"
"#Spikeling_parameter_stackedwidget{\n"
"	background-color: rgb(7, 54, 66);\n"
"}\n"
"\n"
"\n"
"#Spikeling_rightMenuSubContainer QPushButton{\n"
"	text-align: left;\n"
"	padding: 10px 0px;\n"
"	border-top-right-radius:15px;\n"
"	border-bottom-right-radius: 15px;\n"
"	background-color: rgb(7, 54, 66);\n"
"}\n"
"#Spikeling_rightMenuSubContainer_frame QPushButton{\n"
"	background-color: rgb(0, 43, 54);\n"
"}\n"
"\n"
"#Spikeling_CenterMenuContainer{\n"
"	background-color: rgb(7, 54, 66)\n"
"}\n"
"\n"
"#Spikeling_parameter_exit_frame{\n"
"	background-color: rgb(11, 30, 38);\n"
"	border-top-left-radius:10px;\n"
"	border-bottom-left-radius: 10px;\n"
"}\n"
"\n"
"\n"
"\n"
"#NeuronGenerator_subframe2 QLineEdit{\n"
"	background-color: rgb(7, 54, 66);\n"
"	border: 2px solid rgb(147,161,161);\n"
"}\n"
"#NeuronGenerator_subframe2 QPushButton{\n"
"	background-color: rgb(7, 54, 66);\n"
"	border: 2px solid rgb(147,161,161);\n"
""
                        "	border-radius: 10px;\n"
"	padding: 5px;\n"
"}\n"
"#NeuronGenerator_subframe1_Izhik_frame QTextBrowser{\n"
"	background-color: rgb(7, 54, 66);\n"
"	border: 2px solid rgb(147,161,161);\n"
"}\n"
"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setMinimumSize(QSize(1280, 720))
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.leftMenuContainer = QCustomSlideMenu(self.centralwidget)
        self.leftMenuContainer.setObjectName(u"leftMenuContainer")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.leftMenuContainer.sizePolicy().hasHeightForWidth())
        self.leftMenuContainer.setSizePolicy(sizePolicy)
        self.leftMenuContainer.setMaximumSize(QSize(40, 16777215))
        self.leftMenuContainer.setStyleSheet(u"")
        self.verticalLayout = QVBoxLayout(self.leftMenuContainer)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.leftMenuSubContainer = QWidget(self.leftMenuContainer)
        self.leftMenuSubContainer.setObjectName(u"leftMenuSubContainer")
        sizePolicy.setHeightForWidth(self.leftMenuSubContainer.sizePolicy().hasHeightForWidth())
        self.leftMenuSubContainer.setSizePolicy(sizePolicy)
        self.leftMenuSubContainer.setMinimumSize(QSize(0, 0))
        self.leftMenuSubContainer.setStyleSheet(u"")
        self.verticalLayout_4 = QVBoxLayout(self.leftMenuSubContainer)
        self.verticalLayout_4.setSpacing(20)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(5, 37, 0, 15)
        self.menu_frame = QFrame(self.leftMenuSubContainer)
        self.menu_frame.setObjectName(u"menu_frame")
        self.menu_frame.setStyleSheet(u"")
        self.menu_frame.setFrameShape(QFrame.StyledPanel)
        self.menu_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_64 = QVBoxLayout(self.menu_frame)
        self.verticalLayout_64.setSpacing(10)
        self.verticalLayout_64.setObjectName(u"verticalLayout_64")
        self.verticalLayout_64.setContentsMargins(0, 5, 0, 5)
        self.menu_pushButton = QPushButton(self.menu_frame)
        self.menu_pushButton.setObjectName(u"menu_pushButton")
        font = QFont()
        font.setPointSize(12)
        self.menu_pushButton.setFont(font)
        icon = QIcon()
        icon.addFile(u":/resources/resources/MenuLeft.png", QSize(), QIcon.Normal, QIcon.Off)
        self.menu_pushButton.setIcon(icon)
        self.menu_pushButton.setIconSize(QSize(30, 30))

        self.verticalLayout_64.addWidget(self.menu_pushButton)


        self.verticalLayout_4.addWidget(self.menu_frame)

        self.menus_frame = QFrame(self.leftMenuSubContainer)
        self.menus_frame.setObjectName(u"menus_frame")
        self.menus_frame.setStyleSheet(u"")
        self.menus_frame.setFrameShape(QFrame.StyledPanel)
        self.menus_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_37 = QVBoxLayout(self.menus_frame)
        self.verticalLayout_37.setSpacing(10)
        self.verticalLayout_37.setObjectName(u"verticalLayout_37")
        self.verticalLayout_37.setContentsMargins(0, 0, 0, 0)
        self.SpikelingMenu_pushButton = QPushButton(self.menus_frame)
        self.SpikelingMenu_pushButton.setObjectName(u"SpikelingMenu_pushButton")
        self.SpikelingMenu_pushButton.setFont(font)
        icon1 = QIcon()
        icon1.addFile(u":/resources/resources/Neuron.png", QSize(), QIcon.Normal, QIcon.Off)
        self.SpikelingMenu_pushButton.setIcon(icon1)
        self.SpikelingMenu_pushButton.setIconSize(QSize(24, 24))

        self.verticalLayout_37.addWidget(self.SpikelingMenu_pushButton)

        self.ImagingMenu_pushButton = QPushButton(self.menus_frame)
        self.ImagingMenu_pushButton.setObjectName(u"ImagingMenu_pushButton")
        self.ImagingMenu_pushButton.setFont(font)
        icon2 = QIcon()
        icon2.addFile(u":/resources/resources/Imaging.png", QSize(), QIcon.Normal, QIcon.Off)
        self.ImagingMenu_pushButton.setIcon(icon2)
        self.ImagingMenu_pushButton.setIconSize(QSize(24, 24))

        self.verticalLayout_37.addWidget(self.ImagingMenu_pushButton)

        self.NeuronGeneratorMenu_pushButton = QPushButton(self.menus_frame)
        self.NeuronGeneratorMenu_pushButton.setObjectName(u"NeuronGeneratorMenu_pushButton")
        self.NeuronGeneratorMenu_pushButton.setFont(font)
        icon3 = QIcon()
        icon3.addFile(u":/resources/resources/StimGen.png", QSize(), QIcon.Normal, QIcon.Off)
        self.NeuronGeneratorMenu_pushButton.setIcon(icon3)
        self.NeuronGeneratorMenu_pushButton.setIconSize(QSize(24, 24))

        self.verticalLayout_37.addWidget(self.NeuronGeneratorMenu_pushButton)

        self.StimuluGeneratorMenu_pushButton = QPushButton(self.menus_frame)
        self.StimuluGeneratorMenu_pushButton.setObjectName(u"StimuluGeneratorMenu_pushButton")
        self.StimuluGeneratorMenu_pushButton.setFont(font)
        icon4 = QIcon()
        icon4.addFile(u":/resources/resources/Stimulus.png", QSize(), QIcon.Normal, QIcon.Off)
        self.StimuluGeneratorMenu_pushButton.setIcon(icon4)
        self.StimuluGeneratorMenu_pushButton.setIconSize(QSize(24, 24))

        self.verticalLayout_37.addWidget(self.StimuluGeneratorMenu_pushButton)

        self.ExercisesMenu_pushButton = QPushButton(self.menus_frame)
        self.ExercisesMenu_pushButton.setObjectName(u"ExercisesMenu_pushButton")
        self.ExercisesMenu_pushButton.setFont(font)
        icon5 = QIcon()
        icon5.addFile(u":/resources/resources/Exercices.png", QSize(), QIcon.Normal, QIcon.Off)
        self.ExercisesMenu_pushButton.setIcon(icon5)
        self.ExercisesMenu_pushButton.setIconSize(QSize(24, 24))

        self.verticalLayout_37.addWidget(self.ExercisesMenu_pushButton)


        self.verticalLayout_4.addWidget(self.menus_frame)

        self.options_frame = QFrame(self.leftMenuSubContainer)
        self.options_frame.setObjectName(u"options_frame")
        self.options_frame.setStyleSheet(u"")
        self.options_frame.setFrameShape(QFrame.StyledPanel)
        self.options_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.options_frame)
        self.verticalLayout_5.setSpacing(10)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_5.addItem(self.verticalSpacer)

        self.SettingsMenu_pushButton = QPushButton(self.options_frame)
        self.SettingsMenu_pushButton.setObjectName(u"SettingsMenu_pushButton")
        self.SettingsMenu_pushButton.setFont(font)
        icon6 = QIcon()
        icon6.addFile(u":/resources/resources/Tutorial.png", QSize(), QIcon.Normal, QIcon.Off)
        self.SettingsMenu_pushButton.setIcon(icon6)
        self.SettingsMenu_pushButton.setIconSize(QSize(24, 24))

        self.verticalLayout_5.addWidget(self.SettingsMenu_pushButton)

        self.AboutMenu_pushButton = QPushButton(self.options_frame)
        self.AboutMenu_pushButton.setObjectName(u"AboutMenu_pushButton")
        self.AboutMenu_pushButton.setFont(font)
        icon7 = QIcon()
        icon7.addFile(u":/resources/resources/About.png", QSize(), QIcon.Normal, QIcon.Off)
        self.AboutMenu_pushButton.setIcon(icon7)
        self.AboutMenu_pushButton.setIconSize(QSize(24, 24))

        self.verticalLayout_5.addWidget(self.AboutMenu_pushButton)

        self.HelpMenu_pushButton = QPushButton(self.options_frame)
        self.HelpMenu_pushButton.setObjectName(u"HelpMenu_pushButton")
        self.HelpMenu_pushButton.setFont(font)
        icon8 = QIcon()
        icon8.addFile(u":/resources/resources/Help.png", QSize(), QIcon.Normal, QIcon.Off)
        self.HelpMenu_pushButton.setIcon(icon8)
        self.HelpMenu_pushButton.setIconSize(QSize(24, 24))

        self.verticalLayout_5.addWidget(self.HelpMenu_pushButton)

        self.GitHubMenu_pushButton = QPushButton(self.options_frame)
        self.GitHubMenu_pushButton.setObjectName(u"GitHubMenu_pushButton")
        self.GitHubMenu_pushButton.setFont(font)
        icon9 = QIcon()
        icon9.addFile(u":/resources/resources/GitHub.png", QSize(), QIcon.Normal, QIcon.Off)
        self.GitHubMenu_pushButton.setIcon(icon9)
        self.GitHubMenu_pushButton.setIconSize(QSize(24, 24))

        self.verticalLayout_5.addWidget(self.GitHubMenu_pushButton)


        self.verticalLayout_4.addWidget(self.options_frame)


        self.verticalLayout.addWidget(self.leftMenuSubContainer)


        self.horizontalLayout.addWidget(self.leftMenuContainer)

        self.centerMenuContainer = QCustomSlideMenu(self.centralwidget)
        self.centerMenuContainer.setObjectName(u"centerMenuContainer")
        self.centerMenuContainer.setStyleSheet(u"")
        self.verticalLayout_7 = QVBoxLayout(self.centerMenuContainer)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.centerMenuSubContainer = QWidget(self.centerMenuContainer)
        self.centerMenuSubContainer.setObjectName(u"centerMenuSubContainer")
        self.verticalLayout_6 = QVBoxLayout(self.centerMenuSubContainer)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.centerMenuSubContainer_exit_frame = QFrame(self.centerMenuSubContainer)
        self.centerMenuSubContainer_exit_frame.setObjectName(u"centerMenuSubContainer_exit_frame")
        self.centerMenuSubContainer_exit_frame.setFrameShape(QFrame.StyledPanel)
        self.centerMenuSubContainer_exit_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.centerMenuSubContainer_exit_frame)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.centerMenuSubContainer_exit_label = QLabel(self.centerMenuSubContainer_exit_frame)
        self.centerMenuSubContainer_exit_label.setObjectName(u"centerMenuSubContainer_exit_label")
        self.centerMenuSubContainer_exit_label.setFont(font)

        self.horizontalLayout_5.addWidget(self.centerMenuSubContainer_exit_label, 0, Qt.AlignRight)

        self.centerMenuSubContainer_exit_pushButton = QPushButton(self.centerMenuSubContainer_exit_frame)
        self.centerMenuSubContainer_exit_pushButton.setObjectName(u"centerMenuSubContainer_exit_pushButton")
        icon10 = QIcon()
        icon10.addFile(u":/resources/resources/DropMenuLeft.png", QSize(), QIcon.Normal, QIcon.Off)
        self.centerMenuSubContainer_exit_pushButton.setIcon(icon10)

        self.horizontalLayout_5.addWidget(self.centerMenuSubContainer_exit_pushButton, 0, Qt.AlignRight)


        self.verticalLayout_6.addWidget(self.centerMenuSubContainer_exit_frame, 0, Qt.AlignTop)

        self.centerMenuSubContainer_menu_stackedwidget = QStackedWidget(self.centerMenuSubContainer)
        self.centerMenuSubContainer_menu_stackedwidget.setObjectName(u"centerMenuSubContainer_menu_stackedwidget")
        self.centerMenuSubContainer_menu_stackedwidget.setMinimumSize(QSize(200, 0))
        self.centerMenuSubContainer_menu_stackedwidget.setStyleSheet(u"")
        self.Spikeling_SubMenu_page = QWidget()
        self.Spikeling_SubMenu_page.setObjectName(u"Spikeling_SubMenu_page")
        self.verticalLayout_8 = QVBoxLayout(self.Spikeling_SubMenu_page)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.Spikeling_SubMenu_label_frame = QFrame(self.Spikeling_SubMenu_page)
        self.Spikeling_SubMenu_label_frame.setObjectName(u"Spikeling_SubMenu_label_frame")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.Spikeling_SubMenu_label_frame.sizePolicy().hasHeightForWidth())
        self.Spikeling_SubMenu_label_frame.setSizePolicy(sizePolicy1)
        self.Spikeling_SubMenu_label_frame.setMinimumSize(QSize(0, 25))
        self.Spikeling_SubMenu_label_frame.setMaximumSize(QSize(16777215, 25))
        self.Spikeling_SubMenu_label_frame.setFrameShape(QFrame.StyledPanel)
        self.Spikeling_SubMenu_label_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_18 = QVBoxLayout(self.Spikeling_SubMenu_label_frame)
        self.verticalLayout_18.setSpacing(0)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.verticalLayout_18.setContentsMargins(0, 5, 0, 0)
        self.Spikeling_SubMenu_label = QLabel(self.Spikeling_SubMenu_label_frame)
        self.Spikeling_SubMenu_label.setObjectName(u"Spikeling_SubMenu_label")

        self.verticalLayout_18.addWidget(self.Spikeling_SubMenu_label)


        self.verticalLayout_8.addWidget(self.Spikeling_SubMenu_label_frame, 0, Qt.AlignHCenter|Qt.AlignTop)

        self.Spikeling_SubMenu_button_frame = QFrame(self.Spikeling_SubMenu_page)
        self.Spikeling_SubMenu_button_frame.setObjectName(u"Spikeling_SubMenu_button_frame")
        self.Spikeling_SubMenu_button_frame.setFrameShape(QFrame.StyledPanel)
        self.Spikeling_SubMenu_button_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_19 = QVBoxLayout(self.Spikeling_SubMenu_button_frame)
        self.verticalLayout_19.setSpacing(6)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.verticalLayout_19.setContentsMargins(9, 9, 9, 9)
        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_19.addItem(self.verticalSpacer_5)

        self.Neuron_pushButton = QPushButton(self.Spikeling_SubMenu_button_frame)
        self.Neuron_pushButton.setObjectName(u"Neuron_pushButton")
        self.Neuron_pushButton.setFont(font)
        self.Neuron_pushButton.setIcon(icon1)
        self.Neuron_pushButton.setIconSize(QSize(30, 30))

        self.verticalLayout_19.addWidget(self.Neuron_pushButton)

        self.verticalSpacer_6 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_19.addItem(self.verticalSpacer_6)

        self.NeuronTutorial_pushButton = QPushButton(self.Spikeling_SubMenu_button_frame)
        self.NeuronTutorial_pushButton.setObjectName(u"NeuronTutorial_pushButton")
        self.NeuronTutorial_pushButton.setFont(font)
        self.NeuronTutorial_pushButton.setIcon(icon6)
        self.NeuronTutorial_pushButton.setIconSize(QSize(30, 30))

        self.verticalLayout_19.addWidget(self.NeuronTutorial_pushButton)

        self.verticalSpacer_7 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_19.addItem(self.verticalSpacer_7)

        self.NeuronDataAnalysis_pushButton = QPushButton(self.Spikeling_SubMenu_button_frame)
        self.NeuronDataAnalysis_pushButton.setObjectName(u"NeuronDataAnalysis_pushButton")
        self.NeuronDataAnalysis_pushButton.setFont(font)
        icon11 = QIcon()
        icon11.addFile(u":/resources/resources/DataAnalysis.png", QSize(), QIcon.Normal, QIcon.Off)
        self.NeuronDataAnalysis_pushButton.setIcon(icon11)
        self.NeuronDataAnalysis_pushButton.setIconSize(QSize(30, 30))

        self.verticalLayout_19.addWidget(self.NeuronDataAnalysis_pushButton)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_19.addItem(self.verticalSpacer_4)


        self.verticalLayout_8.addWidget(self.Spikeling_SubMenu_button_frame)

        self.centerMenuSubContainer_menu_stackedwidget.addWidget(self.Spikeling_SubMenu_page)
        self.Imaging_SubMenu_page = QWidget()
        self.Imaging_SubMenu_page.setObjectName(u"Imaging_SubMenu_page")
        self.verticalLayout_10 = QVBoxLayout(self.Imaging_SubMenu_page)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.Imaging_SubMenu_label_frame = QFrame(self.Imaging_SubMenu_page)
        self.Imaging_SubMenu_label_frame.setObjectName(u"Imaging_SubMenu_label_frame")
        self.Imaging_SubMenu_label_frame.setFrameShape(QFrame.StyledPanel)
        self.Imaging_SubMenu_label_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_20 = QVBoxLayout(self.Imaging_SubMenu_label_frame)
        self.verticalLayout_20.setSpacing(0)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.verticalLayout_20.setContentsMargins(0, 0, 0, 0)
        self.Imaging_SubMenu_label = QLabel(self.Imaging_SubMenu_label_frame)
        self.Imaging_SubMenu_label.setObjectName(u"Imaging_SubMenu_label")

        self.verticalLayout_20.addWidget(self.Imaging_SubMenu_label)


        self.verticalLayout_10.addWidget(self.Imaging_SubMenu_label_frame, 0, Qt.AlignHCenter|Qt.AlignTop)

        self.Imaging_SubMenu_button_frame = QFrame(self.Imaging_SubMenu_page)
        self.Imaging_SubMenu_button_frame.setObjectName(u"Imaging_SubMenu_button_frame")
        self.Imaging_SubMenu_button_frame.setFrameShape(QFrame.StyledPanel)
        self.Imaging_SubMenu_button_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_59 = QVBoxLayout(self.Imaging_SubMenu_button_frame)
        self.verticalLayout_59.setObjectName(u"verticalLayout_59")
        self.verticalSpacer_8 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_59.addItem(self.verticalSpacer_8)

        self.ImagingIdeal_pushButton = QPushButton(self.Imaging_SubMenu_button_frame)
        self.ImagingIdeal_pushButton.setObjectName(u"ImagingIdeal_pushButton")
        self.ImagingIdeal_pushButton.setFont(font)
        self.ImagingIdeal_pushButton.setIcon(icon2)
        self.ImagingIdeal_pushButton.setIconSize(QSize(30, 30))

        self.verticalLayout_59.addWidget(self.ImagingIdeal_pushButton)

        self.verticalSpacer_9 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_59.addItem(self.verticalSpacer_9)

        self.ImagingStimulation_pushButton = QPushButton(self.Imaging_SubMenu_button_frame)
        self.ImagingStimulation_pushButton.setObjectName(u"ImagingStimulation_pushButton")
        self.ImagingStimulation_pushButton.setFont(font)
        self.ImagingStimulation_pushButton.setIcon(icon2)
        self.ImagingStimulation_pushButton.setIconSize(QSize(30, 30))

        self.verticalLayout_59.addWidget(self.ImagingStimulation_pushButton)

        self.verticalSpacer_10 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_59.addItem(self.verticalSpacer_10)

        self.ImagingTutorial_pushButton = QPushButton(self.Imaging_SubMenu_button_frame)
        self.ImagingTutorial_pushButton.setObjectName(u"ImagingTutorial_pushButton")
        self.ImagingTutorial_pushButton.setFont(font)
        self.ImagingTutorial_pushButton.setIcon(icon6)
        self.ImagingTutorial_pushButton.setIconSize(QSize(30, 30))

        self.verticalLayout_59.addWidget(self.ImagingTutorial_pushButton)

        self.verticalSpacer_11 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_59.addItem(self.verticalSpacer_11)

        self.ImagingDataAnalysis_pushButton = QPushButton(self.Imaging_SubMenu_button_frame)
        self.ImagingDataAnalysis_pushButton.setObjectName(u"ImagingDataAnalysis_pushButton")
        self.ImagingDataAnalysis_pushButton.setFont(font)
        self.ImagingDataAnalysis_pushButton.setIcon(icon11)
        self.ImagingDataAnalysis_pushButton.setIconSize(QSize(30, 30))

        self.verticalLayout_59.addWidget(self.ImagingDataAnalysis_pushButton)

        self.verticalSpacer_12 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_59.addItem(self.verticalSpacer_12)


        self.verticalLayout_10.addWidget(self.Imaging_SubMenu_button_frame)

        self.centerMenuSubContainer_menu_stackedwidget.addWidget(self.Imaging_SubMenu_page)
        self.NeuronGenerator_SubMenu_page = QWidget()
        self.NeuronGenerator_SubMenu_page.setObjectName(u"NeuronGenerator_SubMenu_page")
        self.verticalLayout_11 = QVBoxLayout(self.NeuronGenerator_SubMenu_page)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.label_8 = QLabel(self.NeuronGenerator_SubMenu_page)
        self.label_8.setObjectName(u"label_8")

        self.verticalLayout_11.addWidget(self.label_8, 0, Qt.AlignHCenter|Qt.AlignTop)

        self.centerMenuSubContainer_menu_stackedwidget.addWidget(self.NeuronGenerator_SubMenu_page)
        self.StimulusGenerator_SubMenu_page = QWidget()
        self.StimulusGenerator_SubMenu_page.setObjectName(u"StimulusGenerator_SubMenu_page")
        self.verticalLayout_15 = QVBoxLayout(self.StimulusGenerator_SubMenu_page)
        self.verticalLayout_15.setSpacing(0)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.label_9 = QLabel(self.StimulusGenerator_SubMenu_page)
        self.label_9.setObjectName(u"label_9")

        self.verticalLayout_15.addWidget(self.label_9, 0, Qt.AlignHCenter|Qt.AlignTop)

        self.centerMenuSubContainer_menu_stackedwidget.addWidget(self.StimulusGenerator_SubMenu_page)
        self.Exercises_SubMenu_page = QWidget()
        self.Exercises_SubMenu_page.setObjectName(u"Exercises_SubMenu_page")
        self.verticalLayout_16 = QVBoxLayout(self.Exercises_SubMenu_page)
        self.verticalLayout_16.setSpacing(0)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.Exercices_SubMenu_label_frame = QFrame(self.Exercises_SubMenu_page)
        self.Exercices_SubMenu_label_frame.setObjectName(u"Exercices_SubMenu_label_frame")
        self.Exercices_SubMenu_label_frame.setFrameShape(QFrame.StyledPanel)
        self.Exercices_SubMenu_label_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_60 = QVBoxLayout(self.Exercices_SubMenu_label_frame)
        self.verticalLayout_60.setObjectName(u"verticalLayout_60")
        self.Exercices_SubMenu_label = QLabel(self.Exercices_SubMenu_label_frame)
        self.Exercices_SubMenu_label.setObjectName(u"Exercices_SubMenu_label")

        self.verticalLayout_60.addWidget(self.Exercices_SubMenu_label)


        self.verticalLayout_16.addWidget(self.Exercices_SubMenu_label_frame, 0, Qt.AlignHCenter|Qt.AlignTop)

        self.Exercices_SubMenu_button_frame = QFrame(self.Exercises_SubMenu_page)
        self.Exercices_SubMenu_button_frame.setObjectName(u"Exercices_SubMenu_button_frame")
        self.Exercices_SubMenu_button_frame.setFrameShape(QFrame.StyledPanel)
        self.Exercices_SubMenu_button_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_61 = QVBoxLayout(self.Exercices_SubMenu_button_frame)
        self.verticalLayout_61.setObjectName(u"verticalLayout_61")
        self.verticalSpacer_13 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_61.addItem(self.verticalSpacer_13)

        self.Exercice101_pushButton = QPushButton(self.Exercices_SubMenu_button_frame)
        self.Exercice101_pushButton.setObjectName(u"Exercice101_pushButton")
        font1 = QFont()
        font1.setPointSize(10)
        self.Exercice101_pushButton.setFont(font1)

        self.verticalLayout_61.addWidget(self.Exercice101_pushButton)

        self.verticalSpacer_15 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_61.addItem(self.verticalSpacer_15)

        self.Exercice102_pushButton = QPushButton(self.Exercices_SubMenu_button_frame)
        self.Exercice102_pushButton.setObjectName(u"Exercice102_pushButton")
        self.Exercice102_pushButton.setFont(font1)

        self.verticalLayout_61.addWidget(self.Exercice102_pushButton)

        self.verticalSpacer_14 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_61.addItem(self.verticalSpacer_14)


        self.verticalLayout_16.addWidget(self.Exercices_SubMenu_button_frame)

        self.centerMenuSubContainer_menu_stackedwidget.addWidget(self.Exercises_SubMenu_page)
        self.Settings_SubMenu_page = QWidget()
        self.Settings_SubMenu_page.setObjectName(u"Settings_SubMenu_page")
        self.verticalLayout_38 = QVBoxLayout(self.Settings_SubMenu_page)
        self.verticalLayout_38.setSpacing(0)
        self.verticalLayout_38.setObjectName(u"verticalLayout_38")
        self.verticalLayout_38.setContentsMargins(0, 0, 0, 0)
        self.label_11 = QLabel(self.Settings_SubMenu_page)
        self.label_11.setObjectName(u"label_11")

        self.verticalLayout_38.addWidget(self.label_11)

        self.centerMenuSubContainer_menu_stackedwidget.addWidget(self.Settings_SubMenu_page)
        self.About_SubMenu_page = QWidget()
        self.About_SubMenu_page.setObjectName(u"About_SubMenu_page")
        self.verticalLayout_50 = QVBoxLayout(self.About_SubMenu_page)
        self.verticalLayout_50.setSpacing(0)
        self.verticalLayout_50.setObjectName(u"verticalLayout_50")
        self.verticalLayout_50.setContentsMargins(0, 0, 0, 0)
        self.label_12 = QLabel(self.About_SubMenu_page)
        self.label_12.setObjectName(u"label_12")

        self.verticalLayout_50.addWidget(self.label_12)

        self.centerMenuSubContainer_menu_stackedwidget.addWidget(self.About_SubMenu_page)
        self.Help_SubMenu_page = QWidget()
        self.Help_SubMenu_page.setObjectName(u"Help_SubMenu_page")
        self.verticalLayout_51 = QVBoxLayout(self.Help_SubMenu_page)
        self.verticalLayout_51.setSpacing(0)
        self.verticalLayout_51.setObjectName(u"verticalLayout_51")
        self.verticalLayout_51.setContentsMargins(0, 0, 0, 0)
        self.label_13 = QLabel(self.Help_SubMenu_page)
        self.label_13.setObjectName(u"label_13")

        self.verticalLayout_51.addWidget(self.label_13)

        self.centerMenuSubContainer_menu_stackedwidget.addWidget(self.Help_SubMenu_page)
        self.GitHub_SubMenu_page = QWidget()
        self.GitHub_SubMenu_page.setObjectName(u"GitHub_SubMenu_page")
        self.verticalLayout_52 = QVBoxLayout(self.GitHub_SubMenu_page)
        self.verticalLayout_52.setSpacing(0)
        self.verticalLayout_52.setObjectName(u"verticalLayout_52")
        self.verticalLayout_52.setContentsMargins(0, 0, 0, 0)
        self.label_14 = QLabel(self.GitHub_SubMenu_page)
        self.label_14.setObjectName(u"label_14")

        self.verticalLayout_52.addWidget(self.label_14)

        self.centerMenuSubContainer_menu_stackedwidget.addWidget(self.GitHub_SubMenu_page)

        self.verticalLayout_6.addWidget(self.centerMenuSubContainer_menu_stackedwidget)


        self.verticalLayout_7.addWidget(self.centerMenuSubContainer, 0, Qt.AlignLeft)


        self.horizontalLayout.addWidget(self.centerMenuContainer)

        self.main_window = QWidget(self.centralwidget)
        self.main_window.setObjectName(u"main_window")
        self.main_window.setStyleSheet(u"")
        self.verticalLayout_2 = QVBoxLayout(self.main_window)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.header_widget = QWidget(self.main_window)
        self.header_widget.setObjectName(u"header_widget")
        self.header_widget.setStyleSheet(u"")
        self.horizontalLayout_2 = QHBoxLayout(self.header_widget)
        self.horizontalLayout_2.setSpacing(6)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(9, 9, 9, 9)
        self.app_ID_frame = QFrame(self.header_widget)
        self.app_ID_frame.setObjectName(u"app_ID_frame")
        self.app_ID_frame.setFrameShape(QFrame.StyledPanel)
        self.app_ID_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_78 = QHBoxLayout(self.app_ID_frame)
        self.horizontalLayout_78.setSpacing(0)
        self.horizontalLayout_78.setObjectName(u"horizontalLayout_78")
        self.horizontalLayout_78.setContentsMargins(0, 0, 0, 0)
        self.appTitle_pushButton = QPushButton(self.app_ID_frame)
        self.appTitle_pushButton.setObjectName(u"appTitle_pushButton")
        icon12 = QIcon()
        icon12.addFile(u":/Images/Icons/Spikeling.png", QSize(), QIcon.Normal, QIcon.Off)
        self.appTitle_pushButton.setIcon(icon12)
        self.appTitle_pushButton.setIconSize(QSize(24, 24))

        self.horizontalLayout_78.addWidget(self.appTitle_pushButton, 0, Qt.AlignLeft)

        self.appTitle_label = QLabel(self.app_ID_frame)
        self.appTitle_label.setObjectName(u"appTitle_label")
        font2 = QFont()
        font2.setPointSize(10)
        font2.setBold(False)
        font2.setItalic(True)
        font2.setUnderline(True)
        font2.setKerning(False)
        self.appTitle_label.setFont(font2)

        self.horizontalLayout_78.addWidget(self.appTitle_label, 0, Qt.AlignTop)


        self.horizontalLayout_2.addWidget(self.app_ID_frame, 0, Qt.AlignLeft)

        self.app_frame = QFrame(self.header_widget)
        self.app_frame.setObjectName(u"app_frame")
        self.app_frame.setFrameShape(QFrame.StyledPanel)
        self.app_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.app_frame)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.reduce_pushButton = QPushButton(self.app_frame)
        self.reduce_pushButton.setObjectName(u"reduce_pushButton")
        icon13 = QIcon()
        icon13.addFile(u":/resources/resources/Artboard 1.png", QSize(), QIcon.Normal, QIcon.Off)
        self.reduce_pushButton.setIcon(icon13)
        self.reduce_pushButton.setIconSize(QSize(24, 24))

        self.horizontalLayout_4.addWidget(self.reduce_pushButton)

        self.expand_pushButton = QPushButton(self.app_frame)
        self.expand_pushButton.setObjectName(u"expand_pushButton")
        icon14 = QIcon()
        icon14.addFile(u":/resources/resources/Expand.png", QSize(), QIcon.Normal, QIcon.Off)
        self.expand_pushButton.setIcon(icon14)
        self.expand_pushButton.setIconSize(QSize(24, 24))

        self.horizontalLayout_4.addWidget(self.expand_pushButton)

        self.exit_pushButton = QPushButton(self.app_frame)
        self.exit_pushButton.setObjectName(u"exit_pushButton")
        icon15 = QIcon()
        icon15.addFile(u":/resources/resources/Exit.png", QSize(), QIcon.Normal, QIcon.Off)
        self.exit_pushButton.setIcon(icon15)
        self.exit_pushButton.setIconSize(QSize(24, 24))

        self.horizontalLayout_4.addWidget(self.exit_pushButton)


        self.horizontalLayout_2.addWidget(self.app_frame, 0, Qt.AlignRight|Qt.AlignTop)


        self.verticalLayout_2.addWidget(self.header_widget)

        self.mainBodyContainer = QWidget(self.main_window)
        self.mainBodyContainer.setObjectName(u"mainBodyContainer")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.mainBodyContainer.sizePolicy().hasHeightForWidth())
        self.mainBodyContainer.setSizePolicy(sizePolicy2)
        self.mainBodyContainer.setStyleSheet(u"")
        self.horizontalLayout_7 = QHBoxLayout(self.mainBodyContainer)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.mainbody_stackedWidget = QStackedWidget(self.mainBodyContainer)
        self.mainbody_stackedWidget.setObjectName(u"mainbody_stackedWidget")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.mainbody_stackedWidget.sizePolicy().hasHeightForWidth())
        self.mainbody_stackedWidget.setSizePolicy(sizePolicy3)
        self.mainbody_stackedWidget.setMinimumSize(QSize(600, 600))
        self.mainbody_stackedWidget.setStyleSheet(u"")
        self.page_000 = QWidget()
        self.page_000.setObjectName(u"page_000")
        self.verticalLayout_30 = QVBoxLayout(self.page_000)
        self.verticalLayout_30.setSpacing(0)
        self.verticalLayout_30.setObjectName(u"verticalLayout_30")
        self.verticalLayout_30.setContentsMargins(0, 0, 0, 0)
        self.mainbody_header_text = QLabel(self.page_000)
        self.mainbody_header_text.setObjectName(u"mainbody_header_text")
        sizePolicy4 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.mainbody_header_text.sizePolicy().hasHeightForWidth())
        self.mainbody_header_text.setSizePolicy(sizePolicy4)
        self.mainbody_header_text.setStyleSheet(u"background-color: rgb(7, 54, 66);\n"
"color: rgb(238, 232, 213);")

        self.verticalLayout_30.addWidget(self.mainbody_header_text, 0, Qt.AlignTop)

        self.mainbody_content_frame = QFrame(self.page_000)
        self.mainbody_content_frame.setObjectName(u"mainbody_content_frame")
        sizePolicy5 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.mainbody_content_frame.sizePolicy().hasHeightForWidth())
        self.mainbody_content_frame.setSizePolicy(sizePolicy5)
        self.mainbody_content_frame.setFrameShape(QFrame.StyledPanel)
        self.mainbody_content_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_76 = QHBoxLayout(self.mainbody_content_frame)
        self.horizontalLayout_76.setSpacing(20)
        self.horizontalLayout_76.setObjectName(u"horizontalLayout_76")
        self.horizontalLayout_76.setContentsMargins(0, 0, 0, 0)
        self.mainbody_content_text = QLabel(self.mainbody_content_frame)
        self.mainbody_content_text.setObjectName(u"mainbody_content_text")
        sizePolicy5.setHeightForWidth(self.mainbody_content_text.sizePolicy().hasHeightForWidth())
        self.mainbody_content_text.setSizePolicy(sizePolicy5)
        self.mainbody_content_text.setWordWrap(True)

        self.horizontalLayout_76.addWidget(self.mainbody_content_text, 0, Qt.AlignVCenter)

        self.mainbody_content_SpikelingGif = QLabel(self.mainbody_content_frame)
        self.mainbody_content_SpikelingGif.setObjectName(u"mainbody_content_SpikelingGif")
        sizePolicy5.setHeightForWidth(self.mainbody_content_SpikelingGif.sizePolicy().hasHeightForWidth())
        self.mainbody_content_SpikelingGif.setSizePolicy(sizePolicy5)
        self.mainbody_content_SpikelingGif.setMinimumSize(QSize(320, 360))
        self.mainbody_content_SpikelingGif.setMaximumSize(QSize(480, 540))
        self.mainbody_content_SpikelingGif.setAutoFillBackground(False)
        self.mainbody_content_SpikelingGif.setPixmap(QPixmap(u":/resources/resources/spikeling.gif"))
        self.mainbody_content_SpikelingGif.setScaledContents(True)

        self.horizontalLayout_76.addWidget(self.mainbody_content_SpikelingGif)


        self.verticalLayout_30.addWidget(self.mainbody_content_frame, 0, Qt.AlignVCenter)

        self.mainbody_footer_text = QLabel(self.page_000)
        self.mainbody_footer_text.setObjectName(u"mainbody_footer_text")
        sizePolicy3.setHeightForWidth(self.mainbody_footer_text.sizePolicy().hasHeightForWidth())
        self.mainbody_footer_text.setSizePolicy(sizePolicy3)
        self.mainbody_footer_text.setMinimumSize(QSize(0, 100))
        self.mainbody_footer_text.setScaledContents(False)
        self.mainbody_footer_text.setWordWrap(True)

        self.verticalLayout_30.addWidget(self.mainbody_footer_text)

        self.mainbody_stackedWidget.addWidget(self.page_000)
        self.page_101 = QWidget()
        self.page_101.setObjectName(u"page_101")
        self.horizontalLayout_34 = QHBoxLayout(self.page_101)
        self.horizontalLayout_34.setSpacing(0)
        self.horizontalLayout_34.setObjectName(u"horizontalLayout_34")
        self.horizontalLayout_34.setContentsMargins(0, 0, 0, 0)
        self.Spikeling_widget = QWidget(self.page_101)
        self.Spikeling_widget.setObjectName(u"Spikeling_widget")
        sizePolicy4.setHeightForWidth(self.Spikeling_widget.sizePolicy().hasHeightForWidth())
        self.Spikeling_widget.setSizePolicy(sizePolicy4)
        self.horizontalLayout_33 = QHBoxLayout(self.Spikeling_widget)
        self.horizontalLayout_33.setSpacing(0)
        self.horizontalLayout_33.setObjectName(u"horizontalLayout_33")
        self.horizontalLayout_33.setContentsMargins(0, 0, 0, 0)
        self.Spikeling_frame = QFrame(self.Spikeling_widget)
        self.Spikeling_frame.setObjectName(u"Spikeling_frame")
        self.Spikeling_frame.setFrameShape(QFrame.StyledPanel)
        self.Spikeling_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_26 = QVBoxLayout(self.Spikeling_frame)
        self.verticalLayout_26.setSpacing(0)
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.verticalLayout_26.setContentsMargins(0, 0, 0, 0)
        self.Spikeling_top_subframe = QFrame(self.Spikeling_frame)
        self.Spikeling_top_subframe.setObjectName(u"Spikeling_top_subframe")
        sizePolicy1.setHeightForWidth(self.Spikeling_top_subframe.sizePolicy().hasHeightForWidth())
        self.Spikeling_top_subframe.setSizePolicy(sizePolicy1)
        self.Spikeling_top_subframe.setFrameShape(QFrame.StyledPanel)
        self.Spikeling_top_subframe.setFrameShadow(QFrame.Raised)
        self.verticalLayout_29 = QVBoxLayout(self.Spikeling_top_subframe)
        self.verticalLayout_29.setSpacing(0)
        self.verticalLayout_29.setObjectName(u"verticalLayout_29")
        self.verticalLayout_29.setContentsMargins(0, 0, 0, 0)
        self.Spikeling_connection_frame1 = QFrame(self.Spikeling_top_subframe)
        self.Spikeling_connection_frame1.setObjectName(u"Spikeling_connection_frame1")
        self.Spikeling_connection_frame1.setFrameShape(QFrame.StyledPanel)
        self.Spikeling_connection_frame1.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_59 = QHBoxLayout(self.Spikeling_connection_frame1)
        self.horizontalLayout_59.setSpacing(5)
        self.horizontalLayout_59.setObjectName(u"horizontalLayout_59")
        self.horizontalLayout_59.setContentsMargins(0, 0, 0, 0)
        self.Spikeling_SelectPortLabel = QLabel(self.Spikeling_connection_frame1)
        self.Spikeling_SelectPortLabel.setObjectName(u"Spikeling_SelectPortLabel")
        self.Spikeling_SelectPortLabel.setFont(font)

        self.horizontalLayout_59.addWidget(self.Spikeling_SelectPortLabel)

        self.Spikeling_SelectPortComboBox = QComboBox(self.Spikeling_connection_frame1)
        self.Spikeling_SelectPortComboBox.addItem("")
        self.Spikeling_SelectPortComboBox.setObjectName(u"Spikeling_SelectPortComboBox")

        self.horizontalLayout_59.addWidget(self.Spikeling_SelectPortComboBox)

        self.Spikeling_ConnectButton = QRadioButton(self.Spikeling_connection_frame1)
        self.Spikeling_ConnectButton.setObjectName(u"Spikeling_ConnectButton")
        self.Spikeling_ConnectButton.setEnabled(False)
        self.Spikeling_ConnectButton.setFont(font)

        self.horizontalLayout_59.addWidget(self.Spikeling_ConnectButton)


        self.verticalLayout_29.addWidget(self.Spikeling_connection_frame1, 0, Qt.AlignLeft|Qt.AlignTop)

        self.Spikeling_top_subframe2 = QFrame(self.Spikeling_top_subframe)
        self.Spikeling_top_subframe2.setObjectName(u"Spikeling_top_subframe2")
        self.Spikeling_top_subframe2.setFrameShape(QFrame.StyledPanel)
        self.Spikeling_top_subframe2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_58 = QHBoxLayout(self.Spikeling_top_subframe2)
        self.horizontalLayout_58.setSpacing(5)
        self.horizontalLayout_58.setObjectName(u"horizontalLayout_58")
        self.horizontalLayout_58.setContentsMargins(0, 0, 0, 0)
        self.Spikeling_NeuronModeLabel = QLabel(self.Spikeling_top_subframe2)
        self.Spikeling_NeuronModeLabel.setObjectName(u"Spikeling_NeuronModeLabel")
        self.Spikeling_NeuronModeLabel.setStyleSheet(u"")

        self.horizontalLayout_58.addWidget(self.Spikeling_NeuronModeLabel)

        self.Spikeling_NeuronModeComboBox = QComboBox(self.Spikeling_top_subframe2)
        self.Spikeling_NeuronModeComboBox.addItem("")
        self.Spikeling_NeuronModeComboBox.addItem("")
        self.Spikeling_NeuronModeComboBox.addItem("")
        self.Spikeling_NeuronModeComboBox.addItem("")
        self.Spikeling_NeuronModeComboBox.addItem("")
        self.Spikeling_NeuronModeComboBox.addItem("")
        self.Spikeling_NeuronModeComboBox.addItem("")
        self.Spikeling_NeuronModeComboBox.addItem("")
        self.Spikeling_NeuronModeComboBox.addItem("")
        self.Spikeling_NeuronModeComboBox.addItem("")
        self.Spikeling_NeuronModeComboBox.addItem("")
        self.Spikeling_NeuronModeComboBox.addItem("")
        self.Spikeling_NeuronModeComboBox.addItem("")
        self.Spikeling_NeuronModeComboBox.setObjectName(u"Spikeling_NeuronModeComboBox")
        self.Spikeling_NeuronModeComboBox.setStyleSheet(u"font: 12pt \"Segoe UI\";")

        self.horizontalLayout_58.addWidget(self.Spikeling_NeuronModeComboBox)

        self.Spikeling_NeuronBrowsePushButton = QPushButton(self.Spikeling_top_subframe2)
        self.Spikeling_NeuronBrowsePushButton.setObjectName(u"Spikeling_NeuronBrowsePushButton")

        self.horizontalLayout_58.addWidget(self.Spikeling_NeuronBrowsePushButton)


        self.verticalLayout_29.addWidget(self.Spikeling_top_subframe2, 0, Qt.AlignHCenter|Qt.AlignTop)


        self.verticalLayout_26.addWidget(self.Spikeling_top_subframe)

        self.Spikeling_Oscilloscope_frame = QFrame(self.Spikeling_frame)
        self.Spikeling_Oscilloscope_frame.setObjectName(u"Spikeling_Oscilloscope_frame")
        self.Spikeling_Oscilloscope_frame.setFrameShape(QFrame.StyledPanel)
        self.Spikeling_Oscilloscope_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_50 = QHBoxLayout(self.Spikeling_Oscilloscope_frame)
        self.horizontalLayout_50.setSpacing(0)
        self.horizontalLayout_50.setObjectName(u"horizontalLayout_50")
        self.horizontalLayout_50.setContentsMargins(0, 0, 0, 0)
        self.Spikeling_Oscilloscope_widget = PlotWidget(self.Spikeling_Oscilloscope_frame)
        self.Spikeling_Oscilloscope_widget.setObjectName(u"Spikeling_Oscilloscope_widget")
        sizePolicy5.setHeightForWidth(self.Spikeling_Oscilloscope_widget.sizePolicy().hasHeightForWidth())
        self.Spikeling_Oscilloscope_widget.setSizePolicy(sizePolicy5)
        self.Spikeling_Oscilloscope_widget.setAutoFillBackground(False)
        self.Spikeling_Oscilloscope_widget.setStyleSheet(u"")
        self.Spikeling_Syn2InputCheckbox = QCheckBox(self.Spikeling_Oscilloscope_widget)
        self.Spikeling_Syn2InputCheckbox.setObjectName(u"Spikeling_Syn2InputCheckbox")
        self.Spikeling_Syn2InputCheckbox.setEnabled(True)
        self.Spikeling_Syn2InputCheckbox.setGeometry(QRect(690, 0, 102, 16))
        self.Spikeling_Syn2InputCheckbox.setAutoFillBackground(False)
        self.Spikeling_Syn2InputCheckbox.setStyleSheet(u"color: rgb(108, 113, 196);")
        self.Spikeling_Syn2InputCheckbox.setChecked(False)
        self.Spikeling_Syn2VmCheckbox = QCheckBox(self.Spikeling_Oscilloscope_widget)
        self.Spikeling_Syn2VmCheckbox.setObjectName(u"Spikeling_Syn2VmCheckbox")
        self.Spikeling_Syn2VmCheckbox.setEnabled(True)
        self.Spikeling_Syn2VmCheckbox.setGeometry(QRect(590, 0, 92, 16))
        self.Spikeling_Syn2VmCheckbox.setAutoFillBackground(False)
        self.Spikeling_Syn2VmCheckbox.setStyleSheet(u"color: rgb(181, 137, 0);")
        self.Spikeling_Syn2VmCheckbox.setChecked(False)
        self.Spikeling_Syn1InputCheckbox = QCheckBox(self.Spikeling_Oscilloscope_widget)
        self.Spikeling_Syn1InputCheckbox.setObjectName(u"Spikeling_Syn1InputCheckbox")
        self.Spikeling_Syn1InputCheckbox.setEnabled(True)
        self.Spikeling_Syn1InputCheckbox.setGeometry(QRect(410, 0, 102, 16))
        self.Spikeling_Syn1InputCheckbox.setAutoFillBackground(False)
        self.Spikeling_Syn1InputCheckbox.setStyleSheet(u"color: rgb(42, 161, 152);")
        self.Spikeling_Syn1InputCheckbox.setChecked(False)
        self.Spikeling_Syn1VmCheckbox = QCheckBox(self.Spikeling_Oscilloscope_widget)
        self.Spikeling_Syn1VmCheckbox.setObjectName(u"Spikeling_Syn1VmCheckbox")
        self.Spikeling_Syn1VmCheckbox.setEnabled(True)
        self.Spikeling_Syn1VmCheckbox.setGeometry(QRect(310, 0, 92, 16))
        self.Spikeling_Syn1VmCheckbox.setAutoFillBackground(False)
        self.Spikeling_Syn1VmCheckbox.setStyleSheet(u"color: rgb(203, 75, 22);")
        self.Spikeling_Syn1VmCheckbox.setChecked(False)
        self.Spikeling_StimulusCheckbox = QCheckBox(self.Spikeling_Oscilloscope_widget)
        self.Spikeling_StimulusCheckbox.setObjectName(u"Spikeling_StimulusCheckbox")
        self.Spikeling_StimulusCheckbox.setEnabled(True)
        self.Spikeling_StimulusCheckbox.setGeometry(QRect(150, 0, 65, 16))
        self.Spikeling_StimulusCheckbox.setAutoFillBackground(False)
        self.Spikeling_StimulusCheckbox.setStyleSheet(u"color: rgb(38, 139, 210);")
        self.Spikeling_StimulusCheckbox.setChecked(True)
        self.Spikeling_InputCurrentCheckbox = QCheckBox(self.Spikeling_Oscilloscope_widget)
        self.Spikeling_InputCurrentCheckbox.setObjectName(u"Spikeling_InputCurrentCheckbox")
        self.Spikeling_InputCurrentCheckbox.setEnabled(True)
        self.Spikeling_InputCurrentCheckbox.setGeometry(QRect(50, 0, 90, 16))
        self.Spikeling_InputCurrentCheckbox.setAutoFillBackground(False)
        self.Spikeling_InputCurrentCheckbox.setStyleSheet(u"color: rgb(133, 153, 0);")
        self.Spikeling_InputCurrentCheckbox.setChecked(True)
        self.Spikeling_VmCheckbox = QCheckBox(self.Spikeling_Oscilloscope_widget)
        self.Spikeling_VmCheckbox.setObjectName(u"Spikeling_VmCheckbox")
        self.Spikeling_VmCheckbox.setEnabled(True)
        self.Spikeling_VmCheckbox.setGeometry(QRect(10, 0, 37, 16))
        self.Spikeling_VmCheckbox.setAutoFillBackground(False)
        self.Spikeling_VmCheckbox.setStyleSheet(u"color: rgb(220, 50, 47);")
        self.Spikeling_VmCheckbox.setChecked(True)

        self.horizontalLayout_50.addWidget(self.Spikeling_Oscilloscope_widget)


        self.verticalLayout_26.addWidget(self.Spikeling_Oscilloscope_frame)

        self.Spikeling_bottom_subframe = QFrame(self.Spikeling_frame)
        self.Spikeling_bottom_subframe.setObjectName(u"Spikeling_bottom_subframe")
        self.Spikeling_bottom_subframe.setFrameShape(QFrame.StyledPanel)
        self.Spikeling_bottom_subframe.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_51 = QHBoxLayout(self.Spikeling_bottom_subframe)
        self.horizontalLayout_51.setSpacing(0)
        self.horizontalLayout_51.setObjectName(u"horizontalLayout_51")
        self.horizontalLayout_51.setContentsMargins(0, 0, 0, 0)
        self.Spikeling_DataRecording_box = QGroupBox(self.Spikeling_bottom_subframe)
        self.Spikeling_DataRecording_box.setObjectName(u"Spikeling_DataRecording_box")
        sizePolicy1.setHeightForWidth(self.Spikeling_DataRecording_box.sizePolicy().hasHeightForWidth())
        self.Spikeling_DataRecording_box.setSizePolicy(sizePolicy1)
        self.Spikeling_DataRecording_box.setMinimumSize(QSize(0, 100))
        self.Spikeling_DataRecording_box.setMaximumSize(QSize(16777215, 100))
        self.Spikeling_DataRecording_box.setStyleSheet(u"")
        self.horizontalLayout_52 = QHBoxLayout(self.Spikeling_DataRecording_box)
        self.horizontalLayout_52.setSpacing(0)
        self.horizontalLayout_52.setObjectName(u"horizontalLayout_52")
        self.horizontalLayout_52.setContentsMargins(0, 0, 0, 0)
        self.Spikeling_DataRecording_left_frame = QFrame(self.Spikeling_DataRecording_box)
        self.Spikeling_DataRecording_left_frame.setObjectName(u"Spikeling_DataRecording_left_frame")
        self.Spikeling_DataRecording_left_frame.setFrameShape(QFrame.StyledPanel)
        self.Spikeling_DataRecording_left_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_27 = QVBoxLayout(self.Spikeling_DataRecording_left_frame)
        self.verticalLayout_27.setSpacing(0)
        self.verticalLayout_27.setObjectName(u"verticalLayout_27")
        self.verticalLayout_27.setContentsMargins(0, 0, 0, 0)
        self.Spikeling_DataRecording_recordingMode_frame = QFrame(self.Spikeling_DataRecording_left_frame)
        self.Spikeling_DataRecording_recordingMode_frame.setObjectName(u"Spikeling_DataRecording_recordingMode_frame")
        self.Spikeling_DataRecording_recordingMode_frame.setFrameShape(QFrame.StyledPanel)
        self.Spikeling_DataRecording_recordingMode_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_54 = QHBoxLayout(self.Spikeling_DataRecording_recordingMode_frame)
        self.horizontalLayout_54.setSpacing(0)
        self.horizontalLayout_54.setObjectName(u"horizontalLayout_54")
        self.horizontalLayout_54.setContentsMargins(0, 0, 0, 0)
        self.Spikeling_DataRecording_ComboBox = QComboBox(self.Spikeling_DataRecording_recordingMode_frame)
        self.Spikeling_DataRecording_ComboBox.addItem("")
        self.Spikeling_DataRecording_ComboBox.addItem("")
        self.Spikeling_DataRecording_ComboBox.setObjectName(u"Spikeling_DataRecording_ComboBox")

        self.horizontalLayout_54.addWidget(self.Spikeling_DataRecording_ComboBox)


        self.verticalLayout_27.addWidget(self.Spikeling_DataRecording_recordingMode_frame)

        self.Spikeling_DataRecording_Loops_frame = QFrame(self.Spikeling_DataRecording_left_frame)
        self.Spikeling_DataRecording_Loops_frame.setObjectName(u"Spikeling_DataRecording_Loops_frame")
        self.Spikeling_DataRecording_Loops_frame.setFrameShape(QFrame.StyledPanel)
        self.Spikeling_DataRecording_Loops_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_53 = QHBoxLayout(self.Spikeling_DataRecording_Loops_frame)
        self.horizontalLayout_53.setSpacing(0)
        self.horizontalLayout_53.setObjectName(u"horizontalLayout_53")
        self.horizontalLayout_53.setContentsMargins(0, 0, 0, 0)
        self.Spikeling_DataRecording_Loop_frame = QFrame(self.Spikeling_DataRecording_Loops_frame)
        self.Spikeling_DataRecording_Loop_frame.setObjectName(u"Spikeling_DataRecording_Loop_frame")
        self.Spikeling_DataRecording_Loop_frame.setFrameShape(QFrame.StyledPanel)
        self.Spikeling_DataRecording_Loop_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_55 = QHBoxLayout(self.Spikeling_DataRecording_Loop_frame)
        self.horizontalLayout_55.setSpacing(0)
        self.horizontalLayout_55.setObjectName(u"horizontalLayout_55")
        self.horizontalLayout_55.setContentsMargins(0, 0, 0, 0)
        self.Spikeling_DataRecording_NumberOfLoops_abel = QLabel(self.Spikeling_DataRecording_Loop_frame)
        self.Spikeling_DataRecording_NumberOfLoops_abel.setObjectName(u"Spikeling_DataRecording_NumberOfLoops_abel")

        self.horizontalLayout_55.addWidget(self.Spikeling_DataRecording_NumberOfLoops_abel)


        self.horizontalLayout_53.addWidget(self.Spikeling_DataRecording_Loop_frame, 0, Qt.AlignLeft)

        self.Spikeling_DataRecording_numberofloop_frame = QFrame(self.Spikeling_DataRecording_Loops_frame)
        self.Spikeling_DataRecording_numberofloop_frame.setObjectName(u"Spikeling_DataRecording_numberofloop_frame")
        self.Spikeling_DataRecording_numberofloop_frame.setFrameShape(QFrame.StyledPanel)
        self.Spikeling_DataRecording_numberofloop_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_81 = QHBoxLayout(self.Spikeling_DataRecording_numberofloop_frame)
        self.horizontalLayout_81.setSpacing(0)
        self.horizontalLayout_81.setObjectName(u"horizontalLayout_81")
        self.horizontalLayout_81.setContentsMargins(0, 0, 0, 0)
        self.Spikeling_DataRecording_NumberOfLoops_value = QLineEdit(self.Spikeling_DataRecording_numberofloop_frame)
        self.Spikeling_DataRecording_NumberOfLoops_value.setObjectName(u"Spikeling_DataRecording_NumberOfLoops_value")
        font3 = QFont()
        font3.setPointSize(10)
        font3.setBold(True)
        self.Spikeling_DataRecording_NumberOfLoops_value.setFont(font3)
        self.Spikeling_DataRecording_NumberOfLoops_value.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_81.addWidget(self.Spikeling_DataRecording_NumberOfLoops_value)


        self.horizontalLayout_53.addWidget(self.Spikeling_DataRecording_numberofloop_frame, 0, Qt.AlignLeft|Qt.AlignVCenter)


        self.verticalLayout_27.addWidget(self.Spikeling_DataRecording_Loops_frame)


        self.horizontalLayout_52.addWidget(self.Spikeling_DataRecording_left_frame)

        self.Spikeling_DataRecording_right_frame = QFrame(self.Spikeling_DataRecording_box)
        self.Spikeling_DataRecording_right_frame.setObjectName(u"Spikeling_DataRecording_right_frame")
        self.Spikeling_DataRecording_right_frame.setFrameShape(QFrame.StyledPanel)
        self.Spikeling_DataRecording_right_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_28 = QVBoxLayout(self.Spikeling_DataRecording_right_frame)
        self.verticalLayout_28.setSpacing(0)
        self.verticalLayout_28.setObjectName(u"verticalLayout_28")
        self.verticalLayout_28.setContentsMargins(0, 0, 0, 0)
        self.Spikeling_DataRecording_directory_frame = QFrame(self.Spikeling_DataRecording_right_frame)
        self.Spikeling_DataRecording_directory_frame.setObjectName(u"Spikeling_DataRecording_directory_frame")
        self.Spikeling_DataRecording_directory_frame.setFrameShape(QFrame.StyledPanel)
        self.Spikeling_DataRecording_directory_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_56 = QHBoxLayout(self.Spikeling_DataRecording_directory_frame)
        self.horizontalLayout_56.setSpacing(0)
        self.horizontalLayout_56.setObjectName(u"horizontalLayout_56")
        self.horizontalLayout_56.setContentsMargins(0, 0, 0, 0)
        self.Spikeling_DataRecording_SelectRecordFolder_label = QLabel(self.Spikeling_DataRecording_directory_frame)
        self.Spikeling_DataRecording_SelectRecordFolder_label.setObjectName(u"Spikeling_DataRecording_SelectRecordFolder_label")

        self.horizontalLayout_56.addWidget(self.Spikeling_DataRecording_SelectRecordFolder_label)

        self.Spikeling_DataRecording_RecordFolder_value = QLineEdit(self.Spikeling_DataRecording_directory_frame)
        self.Spikeling_DataRecording_RecordFolder_value.setObjectName(u"Spikeling_DataRecording_RecordFolder_value")
        self.Spikeling_DataRecording_RecordFolder_value.setEnabled(False)

        self.horizontalLayout_56.addWidget(self.Spikeling_DataRecording_RecordFolder_value)

        self.Spikeling_DataRecording_RecordFolderDir_pushButton = QPushButton(self.Spikeling_DataRecording_directory_frame)
        self.Spikeling_DataRecording_RecordFolderDir_pushButton.setObjectName(u"Spikeling_DataRecording_RecordFolderDir_pushButton")
        self.Spikeling_DataRecording_RecordFolderDir_pushButton.setFont(font3)

        self.horizontalLayout_56.addWidget(self.Spikeling_DataRecording_RecordFolderDir_pushButton)


        self.verticalLayout_28.addWidget(self.Spikeling_DataRecording_directory_frame)

        self.Spikeling_DataRecording_record_frame = QFrame(self.Spikeling_DataRecording_right_frame)
        self.Spikeling_DataRecording_record_frame.setObjectName(u"Spikeling_DataRecording_record_frame")
        self.Spikeling_DataRecording_record_frame.setFrameShape(QFrame.StyledPanel)
        self.Spikeling_DataRecording_record_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_57 = QHBoxLayout(self.Spikeling_DataRecording_record_frame)
        self.horizontalLayout_57.setSpacing(0)
        self.horizontalLayout_57.setObjectName(u"horizontalLayout_57")
        self.horizontalLayout_57.setContentsMargins(0, 0, 0, 0)
        self.Spikeling_SelectedFolderLabel = QLabel(self.Spikeling_DataRecording_record_frame)
        self.Spikeling_SelectedFolderLabel.setObjectName(u"Spikeling_SelectedFolderLabel")
        sizePolicy4.setHeightForWidth(self.Spikeling_SelectedFolderLabel.sizePolicy().hasHeightForWidth())
        self.Spikeling_SelectedFolderLabel.setSizePolicy(sizePolicy4)
        self.Spikeling_SelectedFolderLabel.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_57.addWidget(self.Spikeling_SelectedFolderLabel)

        self.Spikeling_DataRecording_Record_pushButton = QPushButton(self.Spikeling_DataRecording_record_frame)
        self.Spikeling_DataRecording_Record_pushButton.setObjectName(u"Spikeling_DataRecording_Record_pushButton")
        sizePolicy6 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.Spikeling_DataRecording_Record_pushButton.sizePolicy().hasHeightForWidth())
        self.Spikeling_DataRecording_Record_pushButton.setSizePolicy(sizePolicy6)
        self.Spikeling_DataRecording_Record_pushButton.setMinimumSize(QSize(150, 0))
        font4 = QFont()
        font4.setPointSize(12)
        font4.setBold(True)
        self.Spikeling_DataRecording_Record_pushButton.setFont(font4)
        self.Spikeling_DataRecording_Record_pushButton.setStyleSheet(u"color: rgb(250, 250, 250);\n"
"background-color: rgb(220, 50, 47);")

        self.horizontalLayout_57.addWidget(self.Spikeling_DataRecording_Record_pushButton)


        self.verticalLayout_28.addWidget(self.Spikeling_DataRecording_record_frame)


        self.horizontalLayout_52.addWidget(self.Spikeling_DataRecording_right_frame)


        self.horizontalLayout_51.addWidget(self.Spikeling_DataRecording_box)


        self.verticalLayout_26.addWidget(self.Spikeling_bottom_subframe)


        self.horizontalLayout_33.addWidget(self.Spikeling_frame)


        self.horizontalLayout_34.addWidget(self.Spikeling_widget)

        self.Spikeling_CenterMenuContainer = QCustomSlideMenu(self.page_101)
        self.Spikeling_CenterMenuContainer.setObjectName(u"Spikeling_CenterMenuContainer")
        self.Spikeling_CenterMenuContainer.setMinimumSize(QSize(175, 0))
        self.Spikeling_CenterMenuContainer.setMaximumSize(QSize(175, 16777215))
        self.verticalLayout_54 = QVBoxLayout(self.Spikeling_CenterMenuContainer)
        self.verticalLayout_54.setSpacing(0)
        self.verticalLayout_54.setObjectName(u"verticalLayout_54")
        self.verticalLayout_54.setContentsMargins(0, 0, 0, 0)
        self.Spikeling_parameter_exit_frame = QFrame(self.Spikeling_CenterMenuContainer)
        self.Spikeling_parameter_exit_frame.setObjectName(u"Spikeling_parameter_exit_frame")
        self.Spikeling_parameter_exit_frame.setFrameShape(QFrame.StyledPanel)
        self.Spikeling_parameter_exit_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_86 = QHBoxLayout(self.Spikeling_parameter_exit_frame)
        self.horizontalLayout_86.setSpacing(0)
        self.horizontalLayout_86.setObjectName(u"horizontalLayout_86")
        self.horizontalLayout_86.setContentsMargins(0, 0, 0, 0)
        self.Spikeling_parameter_exit_pushButton = QPushButton(self.Spikeling_parameter_exit_frame)
        self.Spikeling_parameter_exit_pushButton.setObjectName(u"Spikeling_parameter_exit_pushButton")
        icon16 = QIcon()
        icon16.addFile(u":/resources/resources/DropMenuRight.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Spikeling_parameter_exit_pushButton.setIcon(icon16)
        self.Spikeling_parameter_exit_pushButton.setIconSize(QSize(20, 20))

        self.horizontalLayout_86.addWidget(self.Spikeling_parameter_exit_pushButton)

        self.Spikeling_parameter_exit_label = QLabel(self.Spikeling_parameter_exit_frame)
        self.Spikeling_parameter_exit_label.setObjectName(u"Spikeling_parameter_exit_label")
        self.Spikeling_parameter_exit_label.setFont(font)

        self.horizontalLayout_86.addWidget(self.Spikeling_parameter_exit_label, 0, Qt.AlignRight)


        self.verticalLayout_54.addWidget(self.Spikeling_parameter_exit_frame)

        self.Spikeling_parameter_stackedwidget = QStackedWidget(self.Spikeling_CenterMenuContainer)
        self.Spikeling_parameter_stackedwidget.setObjectName(u"Spikeling_parameter_stackedwidget")
        self.Spikeling_parameter_stackedwidget.setMinimumSize(QSize(175, 0))
        self.Spikeling_parameter_stackedwidget.setMaximumSize(QSize(175, 16777215))
        self.StimulusParameter_page = QWidget()
        self.StimulusParameter_page.setObjectName(u"StimulusParameter_page")
        self.StimulusParameter_page.setMinimumSize(QSize(175, 0))
        self.StimulusParameter_page.setMaximumSize(QSize(175, 16777215))
        self.verticalLayout_58 = QVBoxLayout(self.StimulusParameter_page)
        self.verticalLayout_58.setSpacing(5)
        self.verticalLayout_58.setObjectName(u"verticalLayout_58")
        self.verticalLayout_58.setContentsMargins(5, 5, 5, 5)
        self.Spikeling_Stimulus_label_frame = QFrame(self.StimulusParameter_page)
        self.Spikeling_Stimulus_label_frame.setObjectName(u"Spikeling_Stimulus_label_frame")
        self.Spikeling_Stimulus_label_frame.setFrameShape(QFrame.StyledPanel)
        self.Spikeling_Stimulus_label_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_83 = QHBoxLayout(self.Spikeling_Stimulus_label_frame)
        self.horizontalLayout_83.setSpacing(0)
        self.horizontalLayout_83.setObjectName(u"horizontalLayout_83")
        self.horizontalLayout_83.setContentsMargins(0, 0, 0, 0)
        self.StimulusLabel = QLabel(self.Spikeling_Stimulus_label_frame)
        self.StimulusLabel.setObjectName(u"StimulusLabel")
        self.StimulusLabel.setStyleSheet(u"color: rgb(147, 161, 161);")

        self.horizontalLayout_83.addWidget(self.StimulusLabel, 0, Qt.AlignTop)


        self.verticalLayout_58.addWidget(self.Spikeling_Stimulus_label_frame)

        self.Spikeling_StimFre_frame = QFrame(self.StimulusParameter_page)
        self.Spikeling_StimFre_frame.setObjectName(u"Spikeling_StimFre_frame")
        sizePolicy2.setHeightForWidth(self.Spikeling_StimFre_frame.sizePolicy().hasHeightForWidth())
        self.Spikeling_StimFre_frame.setSizePolicy(sizePolicy2)
        self.Spikeling_StimFre_frame.setFrameShape(QFrame.StyledPanel)
        self.Spikeling_StimFre_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_22 = QVBoxLayout(self.Spikeling_StimFre_frame)
        self.verticalLayout_22.setSpacing(0)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.verticalLayout_22.setContentsMargins(0, 0, 0, 0)
        self.Spikeling_StimFre_checkBox_frame = QFrame(self.Spikeling_StimFre_frame)
        self.Spikeling_StimFre_checkBox_frame.setObjectName(u"Spikeling_StimFre_checkBox_frame")
        self.Spikeling_StimFre_checkBox_frame.setFrameShape(QFrame.StyledPanel)
        self.Spikeling_StimFre_checkBox_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_38 = QHBoxLayout(self.Spikeling_StimFre_checkBox_frame)
        self.horizontalLayout_38.setSpacing(0)
        self.horizontalLayout_38.setObjectName(u"horizontalLayout_38")
        self.horizontalLayout_38.setContentsMargins(0, 0, 0, 0)
        self.Spikeling_StimFre_checkBox = QCheckBox(self.Spikeling_StimFre_checkBox_frame)
        self.Spikeling_StimFre_checkBox.setObjectName(u"Spikeling_StimFre_checkBox")

        self.horizontalLayout_38.addWidget(self.Spikeling_StimFre_checkBox)


        self.verticalLayout_22.addWidget(self.Spikeling_StimFre_checkBox_frame)

        self.Spikeling_StimFre_slider_frame = QFrame(self.Spikeling_StimFre_frame)
        self.Spikeling_StimFre_slider_frame.setObjectName(u"Spikeling_StimFre_slider_frame")
        self.Spikeling_StimFre_slider_frame.setFrameShape(QFrame.StyledPanel)
        self.Spikeling_StimFre_slider_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_40 = QHBoxLayout(self.Spikeling_StimFre_slider_frame)
        self.horizontalLayout_40.setSpacing(0)
        self.horizontalLayout_40.setObjectName(u"horizontalLayout_40")
        self.horizontalLayout_40.setContentsMargins(0, 0, 0, 0)
        self.Spikeling_StimFre_slider = QSlider(self.Spikeling_StimFre_slider_frame)
        self.Spikeling_StimFre_slider.setObjectName(u"Spikeling_StimFre_slider")
        self.Spikeling_StimFre_slider.setEnabled(False)
        self.Spikeling_StimFre_slider.setMinimum(-100)
        self.Spikeling_StimFre_slider.setMaximum(100)
        self.Spikeling_StimFre_slider.setSingleStep(10)
        self.Spikeling_StimFre_slider.setPageStep(25)
        self.Spikeling_StimFre_slider.setOrientation(Qt.Horizontal)
        self.Spikeling_StimFre_slider.setTickPosition(QSlider.TicksBelow)
        self.Spikeling_StimFre_slider.setTickInterval(20)

        self.horizontalLayout_40.addWidget(self.Spikeling_StimFre_slider)


        self.verticalLayout_22.addWidget(self.Spikeling_StimFre_slider_frame)

        self.Spikeling_StimFre_values_frames = QFrame(self.Spikeling_StimFre_frame)
        self.Spikeling_StimFre_values_frames.setObjectName(u"Spikeling_StimFre_values_frames")
        self.Spikeling_StimFre_values_frames.setFrameShape(QFrame.StyledPanel)
        self.Spikeling_StimFre_values_frames.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_77 = QHBoxLayout(self.Spikeling_StimFre_values_frames)
        self.horizontalLayout_77.setSpacing(0)
        self.horizontalLayout_77.setObjectName(u"horizontalLayout_77")
        self.horizontalLayout_77.setContentsMargins(0, 0, 0, 0)
        self.Spikeling_StimFre_values_min = QLabel(self.Spikeling_StimFre_values_frames)
        self.Spikeling_StimFre_values_min.setObjectName(u"Spikeling_StimFre_values_min")

        self.horizontalLayout_77.addWidget(self.Spikeling_StimFre_values_min)

        self.Spikeling_StimFre_values_0 = QLabel(self.Spikeling_StimFre_values_frames)
        self.Spikeling_StimFre_values_0.setObjectName(u"Spikeling_StimFre_values_0")
        self.Spikeling_StimFre_values_0.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_77.addWidget(self.Spikeling_StimFre_values_0)

        self.Spikeling_StimFre_values_max = QLabel(self.Spikeling_StimFre_values_frames)
        self.Spikeling_StimFre_values_max.setObjectName(u"Spikeling_StimFre_values_max")
        self.Spikeling_StimFre_values_max.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_77.addWidget(self.Spikeling_StimFre_values_max)


        self.verticalLayout_22.addWidget(self.Spikeling_StimFre_values_frames, 0, Qt.AlignTop)

        self.Spikeling_StimFre_image_frame = QFrame(self.Spikeling_StimFre_frame)
        self.Spikeling_StimFre_image_frame.setObjectName(u"Spikeling_StimFre_image_frame")
        self.Spikeling_StimFre_image_frame.setFrameShape(QFrame.StyledPanel)
        self.Spikeling_StimFre_image_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_39 = QHBoxLayout(self.Spikeling_StimFre_image_frame)
        self.horizontalLayout_39.setSpacing(0)
        self.horizontalLayout_39.setObjectName(u"horizontalLayout_39")
        self.horizontalLayout_39.setContentsMargins(0, 0, 0, 0)
        self.Spikeling_StimFre_image = QLabel(self.Spikeling_StimFre_image_frame)
        self.Spikeling_StimFre_image.setObjectName(u"Spikeling_StimFre_image")
        sizePolicy.setHeightForWidth(self.Spikeling_StimFre_image.sizePolicy().hasHeightForWidth())
        self.Spikeling_StimFre_image.setSizePolicy(sizePolicy)
        self.Spikeling_StimFre_image.setMinimumSize(QSize(0, 20))
        self.Spikeling_StimFre_image.setMaximumSize(QSize(16777215, 20))
        self.Spikeling_StimFre_image.setPixmap(QPixmap(u":/resources/resources/StimFrequency.png"))
        self.Spikeling_StimFre_image.setScaledContents(True)

        self.horizontalLayout_39.addWidget(self.Spikeling_StimFre_image)


        self.verticalLayout_22.addWidget(self.Spikeling_StimFre_image_frame)


        self.verticalLayout_58.addWidget(self.Spikeling_StimFre_frame)

        self.Spikeling_StimStr_frame = QFrame(self.StimulusParameter_page)
        self.Spikeling_StimStr_frame.setObjectName(u"Spikeling_StimStr_frame")
        sizePolicy2.setHeightForWidth(self.Spikeling_StimStr_frame.sizePolicy().hasHeightForWidth())
        self.Spikeling_StimStr_frame.setSizePolicy(sizePolicy2)
        self.Spikeling_StimStr_frame.setFrameShape(QFrame.StyledPanel)
        self.Spikeling_StimStr_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_23 = QVBoxLayout(self.Spikeling_StimStr_frame)
        self.verticalLayout_23.setSpacing(0)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.verticalLayout_23.setContentsMargins(0, 0, 0, 0)
        self.Spikeling_StimStr_checkBox_frame = QFrame(self.Spikeling_StimStr_frame)
        self.Spikeling_StimStr_checkBox_frame.setObjectName(u"Spikeling_StimStr_checkBox_frame")
        self.Spikeling_StimStr_checkBox_frame.setFrameShape(QFrame.StyledPanel)
        self.Spikeling_StimStr_checkBox_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_42 = QHBoxLayout(self.Spikeling_StimStr_checkBox_frame)
        self.horizontalLayout_42.setSpacing(0)
        self.horizontalLayout_42.setObjectName(u"horizontalLayout_42")
        self.horizontalLayout_42.setContentsMargins(0, 0, 0, 0)
        self.Spikeling_StimStr_checkBox = QCheckBox(self.Spikeling_StimStr_checkBox_frame)
        self.Spikeling_StimStr_checkBox.setObjectName(u"Spikeling_StimStr_checkBox")

        self.horizontalLayout_42.addWidget(self.Spikeling_StimStr_checkBox)


        self.verticalLayout_23.addWidget(self.Spikeling_StimStr_checkBox_frame)

        self.Spikeling_StimStr_Slider_frame = QFrame(self.Spikeling_StimStr_frame)
        self.Spikeling_StimStr_Slider_frame.setObjectName(u"Spikeling_StimStr_Slider_frame")
        self.Spikeling_StimStr_Slider_frame.setFrameShape(QFrame.StyledPanel)
        self.Spikeling_StimStr_Slider_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_43 = QHBoxLayout(self.Spikeling_StimStr_Slider_frame)
        self.horizontalLayout_43.setSpacing(0)
        self.horizontalLayout_43.setObjectName(u"horizontalLayout_43")
        self.horizontalLayout_43.setContentsMargins(0, 0, 0, 0)
        self.Spikeling_StimStrSlider = QSlider(self.Spikeling_StimStr_Slider_frame)
        self.Spikeling_StimStrSlider.setObjectName(u"Spikeling_StimStrSlider")
        self.Spikeling_StimStrSlider.setEnabled(False)
        self.Spikeling_StimStrSlider.setMinimum(-100)
        self.Spikeling_StimStrSlider.setMaximum(100)
        self.Spikeling_StimStrSlider.setOrientation(Qt.Horizontal)
        self.Spikeling_StimStrSlider.setTickPosition(QSlider.TicksBelow)
        self.Spikeling_StimStrSlider.setTickInterval(20)

        self.horizontalLayout_43.addWidget(self.Spikeling_StimStrSlider)


        self.verticalLayout_23.addWidget(self.Spikeling_StimStr_Slider_frame)

        self.Spikeling_StimStr_values_frame = QFrame(self.Spikeling_StimStr_frame)
        self.Spikeling_StimStr_values_frame.setObjectName(u"Spikeling_StimStr_values_frame")
        self.Spikeling_StimStr_values_frame.setFrameShape(QFrame.StyledPanel)
        self.Spikeling_StimStr_values_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_65 = QHBoxLayout(self.Spikeling_StimStr_values_frame)
        self.horizontalLayout_65.setSpacing(0)
        self.horizontalLayout_65.setObjectName(u"horizontalLayout_65")
        self.horizontalLayout_65.setContentsMargins(0, 0, 0, 0)
        self.Spikeling_StimStr_values_min = QLabel(self.Spikeling_StimStr_values_frame)
        self.Spikeling_StimStr_values_min.setObjectName(u"Spikeling_StimStr_values_min")

        self.horizontalLayout_65.addWidget(self.Spikeling_StimStr_values_min)

        self.Spikeling_StimStr_values_0 = QLabel(self.Spikeling_StimStr_values_frame)
        self.Spikeling_StimStr_values_0.setObjectName(u"Spikeling_StimStr_values_0")
        self.Spikeling_StimStr_values_0.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_65.addWidget(self.Spikeling_StimStr_values_0)

        self.Spikeling_StimStr_values_max = QLabel(self.Spikeling_StimStr_values_frame)
        self.Spikeling_StimStr_values_max.setObjectName(u"Spikeling_StimStr_values_max")
        self.Spikeling_StimStr_values_max.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_65.addWidget(self.Spikeling_StimStr_values_max)


        self.verticalLayout_23.addWidget(self.Spikeling_StimStr_values_frame, 0, Qt.AlignTop)

        self.Spikeling_StimStr_image_frame = QFrame(self.Spikeling_StimStr_frame)
        self.Spikeling_StimStr_image_frame.setObjectName(u"Spikeling_StimStr_image_frame")
        self.Spikeling_StimStr_image_frame.setFrameShape(QFrame.StyledPanel)
        self.Spikeling_StimStr_image_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_41 = QHBoxLayout(self.Spikeling_StimStr_image_frame)
        self.horizontalLayout_41.setSpacing(0)
        self.horizontalLayout_41.setObjectName(u"horizontalLayout_41")
        self.horizontalLayout_41.setContentsMargins(0, 0, 0, 0)
        self.Spikeling_StimStr_image = QLabel(self.Spikeling_StimStr_image_frame)
        self.Spikeling_StimStr_image.setObjectName(u"Spikeling_StimStr_image")
        sizePolicy1.setHeightForWidth(self.Spikeling_StimStr_image.sizePolicy().hasHeightForWidth())
        self.Spikeling_StimStr_image.setSizePolicy(sizePolicy1)
        self.Spikeling_StimStr_image.setMinimumSize(QSize(40, 0))
        self.Spikeling_StimStr_image.setMaximumSize(QSize(16777215, 40))
        self.Spikeling_StimStr_image.setPixmap(QPixmap(u":/resources/resources/StimStrenght.png"))
        self.Spikeling_StimStr_image.setScaledContents(True)

        self.horizontalLayout_41.addWidget(self.Spikeling_StimStr_image)


        self.verticalLayout_23.addWidget(self.Spikeling_StimStr_image_frame)


        self.verticalLayout_58.addWidget(self.Spikeling_StimStr_frame)

        self.Spikeling_parameter_middle_line = QFrame(self.StimulusParameter_page)
        self.Spikeling_parameter_middle_line.setObjectName(u"Spikeling_parameter_middle_line")
        self.Spikeling_parameter_middle_line.setFrameShape(QFrame.HLine)
        self.Spikeling_parameter_middle_line.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_58.addWidget(self.Spikeling_parameter_middle_line)

        self.Spikeling_CustomStimulus_frame = QFrame(self.StimulusParameter_page)
        self.Spikeling_CustomStimulus_frame.setObjectName(u"Spikeling_CustomStimulus_frame")
        sizePolicy2.setHeightForWidth(self.Spikeling_CustomStimulus_frame.sizePolicy().hasHeightForWidth())
        self.Spikeling_CustomStimulus_frame.setSizePolicy(sizePolicy2)
        self.Spikeling_CustomStimulus_frame.setFrameShape(QFrame.StyledPanel)
        self.Spikeling_CustomStimulus_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_24 = QVBoxLayout(self.Spikeling_CustomStimulus_frame)
        self.verticalLayout_24.setSpacing(0)
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.verticalLayout_24.setContentsMargins(0, 10, 0, 10)
        self.Spikeling_CustomStimulus_checkBox_frame = QFrame(self.Spikeling_CustomStimulus_frame)
        self.Spikeling_CustomStimulus_checkBox_frame.setObjectName(u"Spikeling_CustomStimulus_checkBox_frame")
        self.Spikeling_CustomStimulus_checkBox_frame.setFrameShape(QFrame.StyledPanel)
        self.Spikeling_CustomStimulus_checkBox_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_46 = QHBoxLayout(self.Spikeling_CustomStimulus_checkBox_frame)
        self.horizontalLayout_46.setSpacing(0)
        self.horizontalLayout_46.setObjectName(u"horizontalLayout_46")
        self.horizontalLayout_46.setContentsMargins(0, 0, 0, 0)
        self.Spikeling_CustomStimulus_checkBox = QCheckBox(self.Spikeling_CustomStimulus_checkBox_frame)
        self.Spikeling_CustomStimulus_checkBox.setObjectName(u"Spikeling_CustomStimulus_checkBox")

        self.horizontalLayout_46.addWidget(self.Spikeling_CustomStimulus_checkBox)


        self.verticalLayout_24.addWidget(self.Spikeling_CustomStimulus_checkBox_frame)

        self.Spikeling_CustomStimulus_comboBox_frame = QFrame(self.Spikeling_CustomStimulus_frame)
        self.Spikeling_CustomStimulus_comboBox_frame.setObjectName(u"Spikeling_CustomStimulus_comboBox_frame")
        self.Spikeling_CustomStimulus_comboBox_frame.setFrameShape(QFrame.StyledPanel)
        self.Spikeling_CustomStimulus_comboBox_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_45 = QHBoxLayout(self.Spikeling_CustomStimulus_comboBox_frame)
        self.horizontalLayout_45.setSpacing(0)
        self.horizontalLayout_45.setObjectName(u"horizontalLayout_45")
        self.horizontalLayout_45.setContentsMargins(0, 0, 0, 0)
        self.Spikeling_CustomStimulus_comboBox = QComboBox(self.Spikeling_CustomStimulus_comboBox_frame)
        self.Spikeling_CustomStimulus_comboBox.setObjectName(u"Spikeling_CustomStimulus_comboBox")
        self.Spikeling_CustomStimulus_comboBox.setEnabled(False)
        sizePolicy3.setHeightForWidth(self.Spikeling_CustomStimulus_comboBox.sizePolicy().hasHeightForWidth())
        self.Spikeling_CustomStimulus_comboBox.setSizePolicy(sizePolicy3)

        self.horizontalLayout_45.addWidget(self.Spikeling_CustomStimulus_comboBox)


        self.verticalLayout_24.addWidget(self.Spikeling_CustomStimulus_comboBox_frame)

        self.Spikeling_CustomStimulus_display_frame = QFrame(self.Spikeling_CustomStimulus_frame)
        self.Spikeling_CustomStimulus_display_frame.setObjectName(u"Spikeling_CustomStimulus_display_frame")
        self.Spikeling_CustomStimulus_display_frame.setFrameShape(QFrame.StyledPanel)
        self.Spikeling_CustomStimulus_display_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_44 = QHBoxLayout(self.Spikeling_CustomStimulus_display_frame)
        self.horizontalLayout_44.setSpacing(0)
        self.horizontalLayout_44.setObjectName(u"horizontalLayout_44")
        self.horizontalLayout_44.setContentsMargins(0, 0, 0, 0)
        self.Spikeling_CustomStimulus_display = QWidget(self.Spikeling_CustomStimulus_display_frame)
        self.Spikeling_CustomStimulus_display.setObjectName(u"Spikeling_CustomStimulus_display")
        self.Spikeling_CustomStimulus_display.setEnabled(False)
        sizePolicy1.setHeightForWidth(self.Spikeling_CustomStimulus_display.sizePolicy().hasHeightForWidth())
        self.Spikeling_CustomStimulus_display.setSizePolicy(sizePolicy1)
        self.Spikeling_CustomStimulus_display.setMinimumSize(QSize(0, 50))
        self.Spikeling_CustomStimulus_display.setMaximumSize(QSize(16777215, 50))
        self.Spikeling_CustomStimulus_display.setStyleSheet(u"background-color: rgb(0, 30, 38);")

        self.horizontalLayout_44.addWidget(self.Spikeling_CustomStimulus_display)


        self.verticalLayout_24.addWidget(self.Spikeling_CustomStimulus_display_frame)


        self.verticalLayout_58.addWidget(self.Spikeling_CustomStimulus_frame)

        self.Spikeling_parameter_bottom_line = QFrame(self.StimulusParameter_page)
        self.Spikeling_parameter_bottom_line.setObjectName(u"Spikeling_parameter_bottom_line")
        self.Spikeling_parameter_bottom_line.setFrameShape(QFrame.HLine)
        self.Spikeling_parameter_bottom_line.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_58.addWidget(self.Spikeling_parameter_bottom_line)

        self.Spikeling_PR_label = QLabel(self.StimulusParameter_page)
        self.Spikeling_PR_label.setObjectName(u"Spikeling_PR_label")
        self.Spikeling_PR_label.setStyleSheet(u"")

        self.verticalLayout_58.addWidget(self.Spikeling_PR_label)

        self.Spikeling_PR_frame = QFrame(self.StimulusParameter_page)
        self.Spikeling_PR_frame.setObjectName(u"Spikeling_PR_frame")
        sizePolicy2.setHeightForWidth(self.Spikeling_PR_frame.sizePolicy().hasHeightForWidth())
        self.Spikeling_PR_frame.setSizePolicy(sizePolicy2)
        self.Spikeling_PR_frame.setFrameShape(QFrame.StyledPanel)
        self.Spikeling_PR_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_31 = QVBoxLayout(self.Spikeling_PR_frame)
        self.verticalLayout_31.setSpacing(0)
        self.verticalLayout_31.setObjectName(u"verticalLayout_31")
        self.verticalLayout_31.setContentsMargins(0, 0, 0, 0)
        self.Spikeling_PR_PhotoGain_checkBox_frame = QFrame(self.Spikeling_PR_frame)
        self.Spikeling_PR_PhotoGain_checkBox_frame.setObjectName(u"Spikeling_PR_PhotoGain_checkBox_frame")
        self.Spikeling_PR_PhotoGain_checkBox_frame.setFrameShape(QFrame.StyledPanel)
        self.Spikeling_PR_PhotoGain_checkBox_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_49 = QHBoxLayout(self.Spikeling_PR_PhotoGain_checkBox_frame)
        self.horizontalLayout_49.setSpacing(0)
        self.horizontalLayout_49.setObjectName(u"horizontalLayout_49")
        self.horizontalLayout_49.setContentsMargins(0, 0, 0, 0)
        self.Spikeling_PR_PhotoGain_checkBox = QCheckBox(self.Spikeling_PR_PhotoGain_checkBox_frame)
        self.Spikeling_PR_PhotoGain_checkBox.setObjectName(u"Spikeling_PR_PhotoGain_checkBox")

        self.horizontalLayout_49.addWidget(self.Spikeling_PR_PhotoGain_checkBox)


        self.verticalLayout_31.addWidget(self.Spikeling_PR_PhotoGain_checkBox_frame)

        self.Spikeling_PR_PhotoGain_slider_frame = QFrame(self.Spikeling_PR_frame)
        self.Spikeling_PR_PhotoGain_slider_frame.setObjectName(u"Spikeling_PR_PhotoGain_slider_frame")
        self.Spikeling_PR_PhotoGain_slider_frame.setFrameShape(QFrame.StyledPanel)
        self.Spikeling_PR_PhotoGain_slider_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_48 = QHBoxLayout(self.Spikeling_PR_PhotoGain_slider_frame)
        self.horizontalLayout_48.setSpacing(0)
        self.horizontalLayout_48.setObjectName(u"horizontalLayout_48")
        self.horizontalLayout_48.setContentsMargins(0, 0, 0, 0)
        self.Spikeling_PR_PhotoGain_slider = QSlider(self.Spikeling_PR_PhotoGain_slider_frame)
        self.Spikeling_PR_PhotoGain_slider.setObjectName(u"Spikeling_PR_PhotoGain_slider")
        self.Spikeling_PR_PhotoGain_slider.setEnabled(False)
        self.Spikeling_PR_PhotoGain_slider.setMinimum(-100)
        self.Spikeling_PR_PhotoGain_slider.setMaximum(100)
        self.Spikeling_PR_PhotoGain_slider.setSingleStep(10)
        self.Spikeling_PR_PhotoGain_slider.setPageStep(25)
        self.Spikeling_PR_PhotoGain_slider.setOrientation(Qt.Horizontal)
        self.Spikeling_PR_PhotoGain_slider.setTickPosition(QSlider.TicksBelow)
        self.Spikeling_PR_PhotoGain_slider.setTickInterval(20)

        self.horizontalLayout_48.addWidget(self.Spikeling_PR_PhotoGain_slider)


        self.verticalLayout_31.addWidget(self.Spikeling_PR_PhotoGain_slider_frame)

        self.Spikeling_PR_PhotoGain_values_frame = QFrame(self.Spikeling_PR_frame)
        self.Spikeling_PR_PhotoGain_values_frame.setObjectName(u"Spikeling_PR_PhotoGain_values_frame")
        self.Spikeling_PR_PhotoGain_values_frame.setFrameShape(QFrame.StyledPanel)
        self.Spikeling_PR_PhotoGain_values_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_82 = QHBoxLayout(self.Spikeling_PR_PhotoGain_values_frame)
        self.horizontalLayout_82.setSpacing(0)
        self.horizontalLayout_82.setObjectName(u"horizontalLayout_82")
        self.horizontalLayout_82.setContentsMargins(0, 0, 0, 0)
        self.Spikeling_PR_PhotoGain_values_min = QLabel(self.Spikeling_PR_PhotoGain_values_frame)
        self.Spikeling_PR_PhotoGain_values_min.setObjectName(u"Spikeling_PR_PhotoGain_values_min")

        self.horizontalLayout_82.addWidget(self.Spikeling_PR_PhotoGain_values_min)

        self.Spikeling_PR_PhotoGain_values_0 = QLabel(self.Spikeling_PR_PhotoGain_values_frame)
        self.Spikeling_PR_PhotoGain_values_0.setObjectName(u"Spikeling_PR_PhotoGain_values_0")

        self.horizontalLayout_82.addWidget(self.Spikeling_PR_PhotoGain_values_0, 0, Qt.AlignHCenter)

        self.Spikeling_PR_PhotoGain_values_max = QLabel(self.Spikeling_PR_PhotoGain_values_frame)
        self.Spikeling_PR_PhotoGain_values_max.setObjectName(u"Spikeling_PR_PhotoGain_values_max")
        self.Spikeling_PR_PhotoGain_values_max.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_82.addWidget(self.Spikeling_PR_PhotoGain_values_max)


        self.verticalLayout_31.addWidget(self.Spikeling_PR_PhotoGain_values_frame, 0, Qt.AlignTop)

        self.Spikeling_PR_Decay_frame = QFrame(self.Spikeling_PR_frame)
        self.Spikeling_PR_Decay_frame.setObjectName(u"Spikeling_PR_Decay_frame")
        self.Spikeling_PR_Decay_frame.setFrameShape(QFrame.StyledPanel)
        self.Spikeling_PR_Decay_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_36 = QHBoxLayout(self.Spikeling_PR_Decay_frame)
        self.horizontalLayout_36.setSpacing(21)
        self.horizontalLayout_36.setObjectName(u"horizontalLayout_36")
        self.horizontalLayout_36.setContentsMargins(0, 0, 0, 0)
        self.Spikeling_PR_Decay_checkBox = QCheckBox(self.Spikeling_PR_Decay_frame)
        self.Spikeling_PR_Decay_checkBox.setObjectName(u"Spikeling_PR_Decay_checkBox")

        self.horizontalLayout_36.addWidget(self.Spikeling_PR_Decay_checkBox, 0, Qt.AlignLeft)

        self.Spikeling_PR_Decay_value = QLineEdit(self.Spikeling_PR_Decay_frame)
        self.Spikeling_PR_Decay_value.setObjectName(u"Spikeling_PR_Decay_value")
        self.Spikeling_PR_Decay_value.setEnabled(False)
        sizePolicy4.setHeightForWidth(self.Spikeling_PR_Decay_value.sizePolicy().hasHeightForWidth())
        self.Spikeling_PR_Decay_value.setSizePolicy(sizePolicy4)
        self.Spikeling_PR_Decay_value.setMinimumSize(QSize(75, 0))
        self.Spikeling_PR_Decay_value.setMaximumSize(QSize(75, 16777215))
        self.Spikeling_PR_Decay_value.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_36.addWidget(self.Spikeling_PR_Decay_value)


        self.verticalLayout_31.addWidget(self.Spikeling_PR_Decay_frame)

        self.Spikeling_PR_Recovery_frame = QFrame(self.Spikeling_PR_frame)
        self.Spikeling_PR_Recovery_frame.setObjectName(u"Spikeling_PR_Recovery_frame")
        self.Spikeling_PR_Recovery_frame.setFrameShape(QFrame.StyledPanel)
        self.Spikeling_PR_Recovery_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_37 = QHBoxLayout(self.Spikeling_PR_Recovery_frame)
        self.horizontalLayout_37.setSpacing(5)
        self.horizontalLayout_37.setObjectName(u"horizontalLayout_37")
        self.horizontalLayout_37.setContentsMargins(0, 0, 0, 0)
        self.Spikeling_PR_Recovery_checkBox = QCheckBox(self.Spikeling_PR_Recovery_frame)
        self.Spikeling_PR_Recovery_checkBox.setObjectName(u"Spikeling_PR_Recovery_checkBox")

        self.horizontalLayout_37.addWidget(self.Spikeling_PR_Recovery_checkBox, 0, Qt.AlignLeft)

        self.Spikeling_PR_Recovery_value = QLineEdit(self.Spikeling_PR_Recovery_frame)
        self.Spikeling_PR_Recovery_value.setObjectName(u"Spikeling_PR_Recovery_value")
        self.Spikeling_PR_Recovery_value.setEnabled(False)
        sizePolicy4.setHeightForWidth(self.Spikeling_PR_Recovery_value.sizePolicy().hasHeightForWidth())
        self.Spikeling_PR_Recovery_value.setSizePolicy(sizePolicy4)
        self.Spikeling_PR_Recovery_value.setMinimumSize(QSize(75, 0))
        self.Spikeling_PR_Recovery_value.setMaximumSize(QSize(75, 16777215))
        self.Spikeling_PR_Recovery_value.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_37.addWidget(self.Spikeling_PR_Recovery_value)


        self.verticalLayout_31.addWidget(self.Spikeling_PR_Recovery_frame)


        self.verticalLayout_58.addWidget(self.Spikeling_PR_frame)

        self.Spikeling_parameter_stackedwidget.addWidget(self.StimulusParameter_page)
        self.NeuronParameter_page = QWidget()
        self.NeuronParameter_page.setObjectName(u"NeuronParameter_page")
        self.NeuronParameter_page.setMinimumSize(QSize(175, 0))
        self.NeuronParameter_page.setMaximumSize(QSize(175, 16777215))
        self.verticalLayout_57 = QVBoxLayout(self.NeuronParameter_page)
        self.verticalLayout_57.setSpacing(0)
        self.verticalLayout_57.setObjectName(u"verticalLayout_57")
        self.verticalLayout_57.setContentsMargins(0, 0, 0, 0)
        self.Spikeling_NeuronParameter_frame = QFrame(self.NeuronParameter_page)
        self.Spikeling_NeuronParameter_frame.setObjectName(u"Spikeling_NeuronParameter_frame")
        sizePolicy3.setHeightForWidth(self.Spikeling_NeuronParameter_frame.sizePolicy().hasHeightForWidth())
        self.Spikeling_NeuronParameter_frame.setSizePolicy(sizePolicy3)
        self.Spikeling_NeuronParameter_frame.setMinimumSize(QSize(175, 0))
        self.Spikeling_NeuronParameter_frame.setMaximumSize(QSize(175, 16777215))
        self.Spikeling_NeuronParameter_frame.setFrameShape(QFrame.StyledPanel)
        self.Spikeling_NeuronParameter_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_17 = QVBoxLayout(self.Spikeling_NeuronParameter_frame)
        self.verticalLayout_17.setSpacing(5)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.verticalLayout_17.setContentsMargins(5, 5, 5, 5)
        self.Spikeling_PatchClamp_frame = QFrame(self.Spikeling_NeuronParameter_frame)
        self.Spikeling_PatchClamp_frame.setObjectName(u"Spikeling_PatchClamp_frame")
        self.Spikeling_PatchClamp_frame.setFrameShape(QFrame.StyledPanel)
        self.Spikeling_PatchClamp_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_21 = QVBoxLayout(self.Spikeling_PatchClamp_frame)
        self.verticalLayout_21.setSpacing(0)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.verticalLayout_21.setContentsMargins(0, 0, 0, 0)
        self.Spikeling_PatchClamp_label_frame = QFrame(self.Spikeling_PatchClamp_frame)
        self.Spikeling_PatchClamp_label_frame.setObjectName(u"Spikeling_PatchClamp_label_frame")
        self.Spikeling_PatchClamp_label_frame.setFrameShape(QFrame.StyledPanel)
        self.Spikeling_PatchClamp_label_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_84 = QHBoxLayout(self.Spikeling_PatchClamp_label_frame)
        self.horizontalLayout_84.setSpacing(0)
        self.horizontalLayout_84.setObjectName(u"horizontalLayout_84")
        self.horizontalLayout_84.setContentsMargins(0, 0, 0, 0)
        self.Spikeling_PatchClamp_label = QLabel(self.Spikeling_PatchClamp_label_frame)
        self.Spikeling_PatchClamp_label.setObjectName(u"Spikeling_PatchClamp_label")
        self.Spikeling_PatchClamp_label.setStyleSheet(u"color: rgb(147, 161, 161);")

        self.horizontalLayout_84.addWidget(self.Spikeling_PatchClamp_label)


        self.verticalLayout_21.addWidget(self.Spikeling_PatchClamp_label_frame)

        self.Spikeling_PatchClamp_checkBox_frame = QFrame(self.Spikeling_PatchClamp_frame)
        self.Spikeling_PatchClamp_checkBox_frame.setObjectName(u"Spikeling_PatchClamp_checkBox_frame")
        self.Spikeling_PatchClamp_checkBox_frame.setFrameShape(QFrame.StyledPanel)
        self.Spikeling_PatchClamp_checkBox_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_85 = QHBoxLayout(self.Spikeling_PatchClamp_checkBox_frame)
        self.horizontalLayout_85.setSpacing(0)
        self.horizontalLayout_85.setObjectName(u"horizontalLayout_85")
        self.horizontalLayout_85.setContentsMargins(0, 0, 0, 0)
        self.Spikeling_PatchClamp_checkBox = QCheckBox(self.Spikeling_PatchClamp_checkBox_frame)
        self.Spikeling_PatchClamp_checkBox.setObjectName(u"Spikeling_PatchClamp_checkBox")
        self.Spikeling_PatchClamp_checkBox.setFont(font1)
        self.Spikeling_PatchClamp_checkBox.setTristate(False)

        self.horizontalLayout_85.addWidget(self.Spikeling_PatchClamp_checkBox)


        self.verticalLayout_21.addWidget(self.Spikeling_PatchClamp_checkBox_frame)

        self.Spikeling_PatchClamp_slider_frame = QFrame(self.Spikeling_PatchClamp_frame)
        self.Spikeling_PatchClamp_slider_frame.setObjectName(u"Spikeling_PatchClamp_slider_frame")
        self.Spikeling_PatchClamp_slider_frame.setFrameShape(QFrame.StyledPanel)
        self.Spikeling_PatchClamp_slider_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_63 = QHBoxLayout(self.Spikeling_PatchClamp_slider_frame)
        self.horizontalLayout_63.setSpacing(0)
        self.horizontalLayout_63.setObjectName(u"horizontalLayout_63")
        self.horizontalLayout_63.setContentsMargins(0, 0, 0, 0)
        self.Spikeling_PatchClamp_slider = QSlider(self.Spikeling_PatchClamp_slider_frame)
        self.Spikeling_PatchClamp_slider.setObjectName(u"Spikeling_PatchClamp_slider")
        self.Spikeling_PatchClamp_slider.setEnabled(False)
        self.Spikeling_PatchClamp_slider.setMinimum(-100)
        self.Spikeling_PatchClamp_slider.setMaximum(100)
        self.Spikeling_PatchClamp_slider.setOrientation(Qt.Horizontal)
        self.Spikeling_PatchClamp_slider.setTickPosition(QSlider.TicksBelow)
        self.Spikeling_PatchClamp_slider.setTickInterval(20)

        self.horizontalLayout_63.addWidget(self.Spikeling_PatchClamp_slider)


        self.verticalLayout_21.addWidget(self.Spikeling_PatchClamp_slider_frame)

        self.Spikeling_PatchClamp_values_frame = QFrame(self.Spikeling_PatchClamp_frame)
        self.Spikeling_PatchClamp_values_frame.setObjectName(u"Spikeling_PatchClamp_values_frame")
        self.Spikeling_PatchClamp_values_frame.setFrameShape(QFrame.StyledPanel)
        self.Spikeling_PatchClamp_values_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_64 = QHBoxLayout(self.Spikeling_PatchClamp_values_frame)
        self.horizontalLayout_64.setSpacing(0)
        self.horizontalLayout_64.setObjectName(u"horizontalLayout_64")
        self.horizontalLayout_64.setContentsMargins(0, 0, 0, 0)
        self.Spikeling_PatchClamp_values_min = QLabel(self.Spikeling_PatchClamp_values_frame)
        self.Spikeling_PatchClamp_values_min.setObjectName(u"Spikeling_PatchClamp_values_min")

        self.horizontalLayout_64.addWidget(self.Spikeling_PatchClamp_values_min)

        self.Spikeling_PatchClamp_values_0 = QLabel(self.Spikeling_PatchClamp_values_frame)
        self.Spikeling_PatchClamp_values_0.setObjectName(u"Spikeling_PatchClamp_values_0")
        self.Spikeling_PatchClamp_values_0.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_64.addWidget(self.Spikeling_PatchClamp_values_0)

        self.Spikeling_PatchClamp_values_max = QLabel(self.Spikeling_PatchClamp_values_frame)
        self.Spikeling_PatchClamp_values_max.setObjectName(u"Spikeling_PatchClamp_values_max")
        self.Spikeling_PatchClamp_values_max.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_64.addWidget(self.Spikeling_PatchClamp_values_max)


        self.verticalLayout_21.addWidget(self.Spikeling_PatchClamp_values_frame, 0, Qt.AlignTop)


        self.verticalLayout_17.addWidget(self.Spikeling_PatchClamp_frame)

        self.Spikeling_neuronparameters_top_line = QFrame(self.Spikeling_NeuronParameter_frame)
        self.Spikeling_neuronparameters_top_line.setObjectName(u"Spikeling_neuronparameters_top_line")
        self.Spikeling_neuronparameters_top_line.setFrameShape(QFrame.HLine)
        self.Spikeling_neuronparameters_top_line.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_17.addWidget(self.Spikeling_neuronparameters_top_line)

        self.Spikeling_Noise_frame = QFrame(self.Spikeling_NeuronParameter_frame)
        self.Spikeling_Noise_frame.setObjectName(u"Spikeling_Noise_frame")
        self.Spikeling_Noise_frame.setFrameShape(QFrame.StyledPanel)
        self.Spikeling_Noise_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_25 = QVBoxLayout(self.Spikeling_Noise_frame)
        self.verticalLayout_25.setSpacing(0)
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.verticalLayout_25.setContentsMargins(0, 0, 0, 0)
        self.Spikeling_Noise_label_frame = QFrame(self.Spikeling_Noise_frame)
        self.Spikeling_Noise_label_frame.setObjectName(u"Spikeling_Noise_label_frame")
        self.Spikeling_Noise_label_frame.setFrameShape(QFrame.StyledPanel)
        self.Spikeling_Noise_label_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_88 = QHBoxLayout(self.Spikeling_Noise_label_frame)
        self.horizontalLayout_88.setSpacing(0)
        self.horizontalLayout_88.setObjectName(u"horizontalLayout_88")
        self.horizontalLayout_88.setContentsMargins(0, 0, 0, 0)
        self.Spikeling_Noise_label = QLabel(self.Spikeling_Noise_label_frame)
        self.Spikeling_Noise_label.setObjectName(u"Spikeling_Noise_label")
        self.Spikeling_Noise_label.setStyleSheet(u"color: rgb(147, 161, 161);")

        self.horizontalLayout_88.addWidget(self.Spikeling_Noise_label)


        self.verticalLayout_25.addWidget(self.Spikeling_Noise_label_frame)

        self.Spikeling_Noise_checkBox_frame = QFrame(self.Spikeling_Noise_frame)
        self.Spikeling_Noise_checkBox_frame.setObjectName(u"Spikeling_Noise_checkBox_frame")
        self.Spikeling_Noise_checkBox_frame.setFrameShape(QFrame.StyledPanel)
        self.Spikeling_Noise_checkBox_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_91 = QHBoxLayout(self.Spikeling_Noise_checkBox_frame)
        self.horizontalLayout_91.setSpacing(0)
        self.horizontalLayout_91.setObjectName(u"horizontalLayout_91")
        self.horizontalLayout_91.setContentsMargins(0, 0, 0, 0)
        self.Spikeling_Noise_checkBox = QCheckBox(self.Spikeling_Noise_checkBox_frame)
        self.Spikeling_Noise_checkBox.setObjectName(u"Spikeling_Noise_checkBox")

        self.horizontalLayout_91.addWidget(self.Spikeling_Noise_checkBox)


        self.verticalLayout_25.addWidget(self.Spikeling_Noise_checkBox_frame)

        self.Spikeling_Noise_slider_frame = QFrame(self.Spikeling_Noise_frame)
        self.Spikeling_Noise_slider_frame.setObjectName(u"Spikeling_Noise_slider_frame")
        self.Spikeling_Noise_slider_frame.setFrameShape(QFrame.StyledPanel)
        self.Spikeling_Noise_slider_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_90 = QHBoxLayout(self.Spikeling_Noise_slider_frame)
        self.horizontalLayout_90.setSpacing(0)
        self.horizontalLayout_90.setObjectName(u"horizontalLayout_90")
        self.horizontalLayout_90.setContentsMargins(0, 0, 0, 0)
        self.Spikeling_Noise_slider = QSlider(self.Spikeling_Noise_slider_frame)
        self.Spikeling_Noise_slider.setObjectName(u"Spikeling_Noise_slider")
        self.Spikeling_Noise_slider.setEnabled(False)
        self.Spikeling_Noise_slider.setMaximum(100)
        self.Spikeling_Noise_slider.setOrientation(Qt.Horizontal)
        self.Spikeling_Noise_slider.setTickPosition(QSlider.TicksBelow)
        self.Spikeling_Noise_slider.setTickInterval(10)

        self.horizontalLayout_90.addWidget(self.Spikeling_Noise_slider)


        self.verticalLayout_25.addWidget(self.Spikeling_Noise_slider_frame)

        self.Spikeling_Noise_value_frame = QFrame(self.Spikeling_Noise_frame)
        self.Spikeling_Noise_value_frame.setObjectName(u"Spikeling_Noise_value_frame")
        self.Spikeling_Noise_value_frame.setFrameShape(QFrame.StyledPanel)
        self.Spikeling_Noise_value_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_89 = QHBoxLayout(self.Spikeling_Noise_value_frame)
        self.horizontalLayout_89.setSpacing(0)
        self.horizontalLayout_89.setObjectName(u"horizontalLayout_89")
        self.horizontalLayout_89.setContentsMargins(0, 0, 0, 0)
        self.Spikeling_Noise_0_value = QLabel(self.Spikeling_Noise_value_frame)
        self.Spikeling_Noise_0_value.setObjectName(u"Spikeling_Noise_0_value")
        self.Spikeling_Noise_0_value.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_89.addWidget(self.Spikeling_Noise_0_value, 0, Qt.AlignLeft)

        self.Spikeling_Noise_max_value = QLabel(self.Spikeling_Noise_value_frame)
        self.Spikeling_Noise_max_value.setObjectName(u"Spikeling_Noise_max_value")
        self.Spikeling_Noise_max_value.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_89.addWidget(self.Spikeling_Noise_max_value, 0, Qt.AlignRight)


        self.verticalLayout_25.addWidget(self.Spikeling_Noise_value_frame, 0, Qt.AlignTop)


        self.verticalLayout_17.addWidget(self.Spikeling_Noise_frame)

        self.Spikeling_neuronparameters_middle_line = QFrame(self.Spikeling_NeuronParameter_frame)
        self.Spikeling_neuronparameters_middle_line.setObjectName(u"Spikeling_neuronparameters_middle_line")
        self.Spikeling_neuronparameters_middle_line.setFrameShape(QFrame.HLine)
        self.Spikeling_neuronparameters_middle_line.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_17.addWidget(self.Spikeling_neuronparameters_middle_line)

        self.Spikeling_Synapse1_frame = QFrame(self.Spikeling_NeuronParameter_frame)
        self.Spikeling_Synapse1_frame.setObjectName(u"Spikeling_Synapse1_frame")
        self.Spikeling_Synapse1_frame.setFrameShape(QFrame.StyledPanel)
        self.Spikeling_Synapse1_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_32 = QVBoxLayout(self.Spikeling_Synapse1_frame)
        self.verticalLayout_32.setSpacing(0)
        self.verticalLayout_32.setObjectName(u"verticalLayout_32")
        self.verticalLayout_32.setContentsMargins(0, 0, 0, 0)
        self.Spikeling_Synapse1_label_frame = QFrame(self.Spikeling_Synapse1_frame)
        self.Spikeling_Synapse1_label_frame.setObjectName(u"Spikeling_Synapse1_label_frame")
        self.Spikeling_Synapse1_label_frame.setFrameShape(QFrame.StyledPanel)
        self.Spikeling_Synapse1_label_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_92 = QHBoxLayout(self.Spikeling_Synapse1_label_frame)
        self.horizontalLayout_92.setSpacing(0)
        self.horizontalLayout_92.setObjectName(u"horizontalLayout_92")
        self.horizontalLayout_92.setContentsMargins(0, 0, 0, 0)
        self.Spikeling_Synapse1_label = QLabel(self.Spikeling_Synapse1_label_frame)
        self.Spikeling_Synapse1_label.setObjectName(u"Spikeling_Synapse1_label")
        self.Spikeling_Synapse1_label.setStyleSheet(u"color: rgb(147, 161, 161);")

        self.horizontalLayout_92.addWidget(self.Spikeling_Synapse1_label)


        self.verticalLayout_32.addWidget(self.Spikeling_Synapse1_label_frame)

        self.Spikeling_Synapse1_checkBox_frame = QFrame(self.Spikeling_Synapse1_frame)
        self.Spikeling_Synapse1_checkBox_frame.setObjectName(u"Spikeling_Synapse1_checkBox_frame")
        self.Spikeling_Synapse1_checkBox_frame.setFrameShape(QFrame.StyledPanel)
        self.Spikeling_Synapse1_checkBox_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_94 = QHBoxLayout(self.Spikeling_Synapse1_checkBox_frame)
        self.horizontalLayout_94.setSpacing(0)
        self.horizontalLayout_94.setObjectName(u"horizontalLayout_94")
        self.horizontalLayout_94.setContentsMargins(0, 0, 0, 0)
        self.Spikeling_Synapse1_checkBox = QCheckBox(self.Spikeling_Synapse1_checkBox_frame)
        self.Spikeling_Synapse1_checkBox.setObjectName(u"Spikeling_Synapse1_checkBox")

        self.horizontalLayout_94.addWidget(self.Spikeling_Synapse1_checkBox)


        self.verticalLayout_32.addWidget(self.Spikeling_Synapse1_checkBox_frame)

        self.Spikeling_Synapse1_slider_frame = QFrame(self.Spikeling_Synapse1_frame)
        self.Spikeling_Synapse1_slider_frame.setObjectName(u"Spikeling_Synapse1_slider_frame")
        self.Spikeling_Synapse1_slider_frame.setFrameShape(QFrame.StyledPanel)
        self.Spikeling_Synapse1_slider_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_95 = QHBoxLayout(self.Spikeling_Synapse1_slider_frame)
        self.horizontalLayout_95.setSpacing(0)
        self.horizontalLayout_95.setObjectName(u"horizontalLayout_95")
        self.horizontalLayout_95.setContentsMargins(0, 0, 0, 0)
        self.Spikeling_Synapse1_slider = QSlider(self.Spikeling_Synapse1_slider_frame)
        self.Spikeling_Synapse1_slider.setObjectName(u"Spikeling_Synapse1_slider")
        self.Spikeling_Synapse1_slider.setEnabled(False)
        self.Spikeling_Synapse1_slider.setMinimum(-100)
        self.Spikeling_Synapse1_slider.setMaximum(100)
        self.Spikeling_Synapse1_slider.setOrientation(Qt.Horizontal)
        self.Spikeling_Synapse1_slider.setTickPosition(QSlider.TicksBelow)
        self.Spikeling_Synapse1_slider.setTickInterval(20)

        self.horizontalLayout_95.addWidget(self.Spikeling_Synapse1_slider)


        self.verticalLayout_32.addWidget(self.Spikeling_Synapse1_slider_frame)

        self.Spikeling_Synapse1_values_frame = QFrame(self.Spikeling_Synapse1_frame)
        self.Spikeling_Synapse1_values_frame.setObjectName(u"Spikeling_Synapse1_values_frame")
        self.Spikeling_Synapse1_values_frame.setFrameShape(QFrame.StyledPanel)
        self.Spikeling_Synapse1_values_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_96 = QHBoxLayout(self.Spikeling_Synapse1_values_frame)
        self.horizontalLayout_96.setSpacing(0)
        self.horizontalLayout_96.setObjectName(u"horizontalLayout_96")
        self.horizontalLayout_96.setContentsMargins(0, 0, 0, 0)
        self.Spikeling_Synapse1_min = QLabel(self.Spikeling_Synapse1_values_frame)
        self.Spikeling_Synapse1_min.setObjectName(u"Spikeling_Synapse1_min")

        self.horizontalLayout_96.addWidget(self.Spikeling_Synapse1_min)

        self.Spikeling_Synapse1_0 = QLabel(self.Spikeling_Synapse1_values_frame)
        self.Spikeling_Synapse1_0.setObjectName(u"Spikeling_Synapse1_0")

        self.horizontalLayout_96.addWidget(self.Spikeling_Synapse1_0, 0, Qt.AlignHCenter|Qt.AlignTop)

        self.Spikeling_Synapse1_max = QLabel(self.Spikeling_Synapse1_values_frame)
        self.Spikeling_Synapse1_max.setObjectName(u"Spikeling_Synapse1_max")
        self.Spikeling_Synapse1_max.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_96.addWidget(self.Spikeling_Synapse1_max)


        self.verticalLayout_32.addWidget(self.Spikeling_Synapse1_values_frame, 0, Qt.AlignTop)

        self.Spikeling_Synapse1_Decay_frame = QFrame(self.Spikeling_Synapse1_frame)
        self.Spikeling_Synapse1_Decay_frame.setObjectName(u"Spikeling_Synapse1_Decay_frame")
        self.Spikeling_Synapse1_Decay_frame.setFrameShape(QFrame.StyledPanel)
        self.Spikeling_Synapse1_Decay_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_93 = QHBoxLayout(self.Spikeling_Synapse1_Decay_frame)
        self.horizontalLayout_93.setSpacing(21)
        self.horizontalLayout_93.setObjectName(u"horizontalLayout_93")
        self.horizontalLayout_93.setContentsMargins(0, 0, 0, 0)
        self.Spikeling_Synapse1_Decay_checkBox = QCheckBox(self.Spikeling_Synapse1_Decay_frame)
        self.Spikeling_Synapse1_Decay_checkBox.setObjectName(u"Spikeling_Synapse1_Decay_checkBox")

        self.horizontalLayout_93.addWidget(self.Spikeling_Synapse1_Decay_checkBox)

        self.Spikeling_Synapse1_Decay_value = QLineEdit(self.Spikeling_Synapse1_Decay_frame)
        self.Spikeling_Synapse1_Decay_value.setObjectName(u"Spikeling_Synapse1_Decay_value")
        self.Spikeling_Synapse1_Decay_value.setEnabled(False)
        sizePolicy4.setHeightForWidth(self.Spikeling_Synapse1_Decay_value.sizePolicy().hasHeightForWidth())
        self.Spikeling_Synapse1_Decay_value.setSizePolicy(sizePolicy4)
        self.Spikeling_Synapse1_Decay_value.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_93.addWidget(self.Spikeling_Synapse1_Decay_value)


        self.verticalLayout_32.addWidget(self.Spikeling_Synapse1_Decay_frame)


        self.verticalLayout_17.addWidget(self.Spikeling_Synapse1_frame)

        self.Spikeling_neuronparameters_bottom_line = QFrame(self.Spikeling_NeuronParameter_frame)
        self.Spikeling_neuronparameters_bottom_line.setObjectName(u"Spikeling_neuronparameters_bottom_line")
        self.Spikeling_neuronparameters_bottom_line.setFrameShape(QFrame.HLine)
        self.Spikeling_neuronparameters_bottom_line.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_17.addWidget(self.Spikeling_neuronparameters_bottom_line)

        self.Spikeling_Synapse2_frame = QFrame(self.Spikeling_NeuronParameter_frame)
        self.Spikeling_Synapse2_frame.setObjectName(u"Spikeling_Synapse2_frame")
        self.Spikeling_Synapse2_frame.setFrameShape(QFrame.StyledPanel)
        self.Spikeling_Synapse2_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_33 = QVBoxLayout(self.Spikeling_Synapse2_frame)
        self.verticalLayout_33.setSpacing(0)
        self.verticalLayout_33.setObjectName(u"verticalLayout_33")
        self.verticalLayout_33.setContentsMargins(0, 0, 0, 0)
        self.Spikeling_Synapse2_label_frame = QFrame(self.Spikeling_Synapse2_frame)
        self.Spikeling_Synapse2_label_frame.setObjectName(u"Spikeling_Synapse2_label_frame")
        self.Spikeling_Synapse2_label_frame.setFrameShape(QFrame.StyledPanel)
        self.Spikeling_Synapse2_label_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_97 = QHBoxLayout(self.Spikeling_Synapse2_label_frame)
        self.horizontalLayout_97.setSpacing(0)
        self.horizontalLayout_97.setObjectName(u"horizontalLayout_97")
        self.horizontalLayout_97.setContentsMargins(0, 0, 0, 0)
        self.Spikeling_Synapse2_label = QLabel(self.Spikeling_Synapse2_label_frame)
        self.Spikeling_Synapse2_label.setObjectName(u"Spikeling_Synapse2_label")
        self.Spikeling_Synapse2_label.setStyleSheet(u"color: rgb(147, 161, 161);")

        self.horizontalLayout_97.addWidget(self.Spikeling_Synapse2_label)


        self.verticalLayout_33.addWidget(self.Spikeling_Synapse2_label_frame)

        self.Spikeling_Synapse2_checkBox_frame = QFrame(self.Spikeling_Synapse2_frame)
        self.Spikeling_Synapse2_checkBox_frame.setObjectName(u"Spikeling_Synapse2_checkBox_frame")
        self.Spikeling_Synapse2_checkBox_frame.setFrameShape(QFrame.StyledPanel)
        self.Spikeling_Synapse2_checkBox_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_99 = QHBoxLayout(self.Spikeling_Synapse2_checkBox_frame)
        self.horizontalLayout_99.setSpacing(0)
        self.horizontalLayout_99.setObjectName(u"horizontalLayout_99")
        self.horizontalLayout_99.setContentsMargins(0, 0, 0, 0)
        self.Spikeling_Synapse2_checkBox = QCheckBox(self.Spikeling_Synapse2_checkBox_frame)
        self.Spikeling_Synapse2_checkBox.setObjectName(u"Spikeling_Synapse2_checkBox")
        self.Spikeling_Synapse2_checkBox.setEnabled(True)

        self.horizontalLayout_99.addWidget(self.Spikeling_Synapse2_checkBox)


        self.verticalLayout_33.addWidget(self.Spikeling_Synapse2_checkBox_frame)

        self.Spikeling_Synapse2_slider_frame = QFrame(self.Spikeling_Synapse2_frame)
        self.Spikeling_Synapse2_slider_frame.setObjectName(u"Spikeling_Synapse2_slider_frame")
        self.Spikeling_Synapse2_slider_frame.setFrameShape(QFrame.StyledPanel)
        self.Spikeling_Synapse2_slider_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_100 = QHBoxLayout(self.Spikeling_Synapse2_slider_frame)
        self.horizontalLayout_100.setSpacing(0)
        self.horizontalLayout_100.setObjectName(u"horizontalLayout_100")
        self.horizontalLayout_100.setContentsMargins(0, 0, 0, 0)
        self.Spikeling_Synapse2_slider = QSlider(self.Spikeling_Synapse2_slider_frame)
        self.Spikeling_Synapse2_slider.setObjectName(u"Spikeling_Synapse2_slider")
        self.Spikeling_Synapse2_slider.setEnabled(False)
        self.Spikeling_Synapse2_slider.setMinimum(-100)
        self.Spikeling_Synapse2_slider.setMaximum(100)
        self.Spikeling_Synapse2_slider.setOrientation(Qt.Horizontal)
        self.Spikeling_Synapse2_slider.setTickPosition(QSlider.TicksBelow)
        self.Spikeling_Synapse2_slider.setTickInterval(20)

        self.horizontalLayout_100.addWidget(self.Spikeling_Synapse2_slider)


        self.verticalLayout_33.addWidget(self.Spikeling_Synapse2_slider_frame)

        self.Spikeling_Synapse2_values_frame = QFrame(self.Spikeling_Synapse2_frame)
        self.Spikeling_Synapse2_values_frame.setObjectName(u"Spikeling_Synapse2_values_frame")
        self.Spikeling_Synapse2_values_frame.setFrameShape(QFrame.StyledPanel)
        self.Spikeling_Synapse2_values_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_60 = QHBoxLayout(self.Spikeling_Synapse2_values_frame)
        self.horizontalLayout_60.setSpacing(0)
        self.horizontalLayout_60.setObjectName(u"horizontalLayout_60")
        self.horizontalLayout_60.setContentsMargins(0, 0, 0, 0)
        self.Spikeling_Synapse2_min = QLabel(self.Spikeling_Synapse2_values_frame)
        self.Spikeling_Synapse2_min.setObjectName(u"Spikeling_Synapse2_min")

        self.horizontalLayout_60.addWidget(self.Spikeling_Synapse2_min)

        self.Spikeling_Synapse2_0 = QLabel(self.Spikeling_Synapse2_values_frame)
        self.Spikeling_Synapse2_0.setObjectName(u"Spikeling_Synapse2_0")
        self.Spikeling_Synapse2_0.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_60.addWidget(self.Spikeling_Synapse2_0)

        self.Spikeling_Synapse2_max = QLabel(self.Spikeling_Synapse2_values_frame)
        self.Spikeling_Synapse2_max.setObjectName(u"Spikeling_Synapse2_max")
        self.Spikeling_Synapse2_max.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_60.addWidget(self.Spikeling_Synapse2_max)


        self.verticalLayout_33.addWidget(self.Spikeling_Synapse2_values_frame, 0, Qt.AlignTop)

        self.Spikeling_Synapse2_Decay_frame = QFrame(self.Spikeling_Synapse2_frame)
        self.Spikeling_Synapse2_Decay_frame.setObjectName(u"Spikeling_Synapse2_Decay_frame")
        sizePolicy4.setHeightForWidth(self.Spikeling_Synapse2_Decay_frame.sizePolicy().hasHeightForWidth())
        self.Spikeling_Synapse2_Decay_frame.setSizePolicy(sizePolicy4)
        self.Spikeling_Synapse2_Decay_frame.setFrameShape(QFrame.StyledPanel)
        self.Spikeling_Synapse2_Decay_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_98 = QHBoxLayout(self.Spikeling_Synapse2_Decay_frame)
        self.horizontalLayout_98.setSpacing(21)
        self.horizontalLayout_98.setObjectName(u"horizontalLayout_98")
        self.horizontalLayout_98.setContentsMargins(0, 0, 0, 0)
        self.Spikeling_Synapse2_Decay_checkBox = QCheckBox(self.Spikeling_Synapse2_Decay_frame)
        self.Spikeling_Synapse2_Decay_checkBox.setObjectName(u"Spikeling_Synapse2_Decay_checkBox")

        self.horizontalLayout_98.addWidget(self.Spikeling_Synapse2_Decay_checkBox)

        self.Spikeling_Synapse2_Decay_value = QLineEdit(self.Spikeling_Synapse2_Decay_frame)
        self.Spikeling_Synapse2_Decay_value.setObjectName(u"Spikeling_Synapse2_Decay_value")
        self.Spikeling_Synapse2_Decay_value.setEnabled(False)
        sizePolicy4.setHeightForWidth(self.Spikeling_Synapse2_Decay_value.sizePolicy().hasHeightForWidth())
        self.Spikeling_Synapse2_Decay_value.setSizePolicy(sizePolicy4)
        self.Spikeling_Synapse2_Decay_value.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_98.addWidget(self.Spikeling_Synapse2_Decay_value)


        self.verticalLayout_33.addWidget(self.Spikeling_Synapse2_Decay_frame)


        self.verticalLayout_17.addWidget(self.Spikeling_Synapse2_frame)


        self.verticalLayout_57.addWidget(self.Spikeling_NeuronParameter_frame)

        self.Spikeling_parameter_stackedwidget.addWidget(self.NeuronParameter_page)

        self.verticalLayout_54.addWidget(self.Spikeling_parameter_stackedwidget)


        self.horizontalLayout_34.addWidget(self.Spikeling_CenterMenuContainer)

        self.Spikeling_rightMenuContainer = QCustomSlideMenu(self.page_101)
        self.Spikeling_rightMenuContainer.setObjectName(u"Spikeling_rightMenuContainer")
        self.Spikeling_rightMenuContainer.setMinimumSize(QSize(40, 0))
        self.Spikeling_rightMenuContainer.setMaximumSize(QSize(40, 16777215))
        self.verticalLayout_53 = QVBoxLayout(self.Spikeling_rightMenuContainer)
        self.verticalLayout_53.setSpacing(0)
        self.verticalLayout_53.setObjectName(u"verticalLayout_53")
        self.verticalLayout_53.setContentsMargins(0, 0, 0, 0)
        self.Spikeling_rightMenuSubContainer = QWidget(self.Spikeling_rightMenuContainer)
        self.Spikeling_rightMenuSubContainer.setObjectName(u"Spikeling_rightMenuSubContainer")
        self.verticalLayout_55 = QVBoxLayout(self.Spikeling_rightMenuSubContainer)
        self.verticalLayout_55.setSpacing(0)
        self.verticalLayout_55.setObjectName(u"verticalLayout_55")
        self.verticalLayout_55.setContentsMargins(0, 0, 5, 0)
        self.Spikeling_rightMenuSubContainer_frame = QFrame(self.Spikeling_rightMenuSubContainer)
        self.Spikeling_rightMenuSubContainer_frame.setObjectName(u"Spikeling_rightMenuSubContainer_frame")
        self.Spikeling_rightMenuSubContainer_frame.setFrameShape(QFrame.StyledPanel)
        self.Spikeling_rightMenuSubContainer_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_79 = QHBoxLayout(self.Spikeling_rightMenuSubContainer_frame)
        self.horizontalLayout_79.setSpacing(0)
        self.horizontalLayout_79.setObjectName(u"horizontalLayout_79")
        self.horizontalLayout_79.setContentsMargins(0, 0, 0, 0)
        self.Spikeling_rightMenuSubContainer_pushButton = QPushButton(self.Spikeling_rightMenuSubContainer_frame)
        self.Spikeling_rightMenuSubContainer_pushButton.setObjectName(u"Spikeling_rightMenuSubContainer_pushButton")
        self.Spikeling_rightMenuSubContainer_pushButton.setStyleSheet(u"")
        icon17 = QIcon()
        icon17.addFile(u":/resources/resources/MenuRight.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Spikeling_rightMenuSubContainer_pushButton.setIcon(icon17)
        self.Spikeling_rightMenuSubContainer_pushButton.setIconSize(QSize(30, 30))

        self.horizontalLayout_79.addWidget(self.Spikeling_rightMenuSubContainer_pushButton)


        self.verticalLayout_55.addWidget(self.Spikeling_rightMenuSubContainer_frame, 0, Qt.AlignTop)

        self.Spikeling_rightMenuParameterContainer_frame = QFrame(self.Spikeling_rightMenuSubContainer)
        self.Spikeling_rightMenuParameterContainer_frame.setObjectName(u"Spikeling_rightMenuParameterContainer_frame")
        self.Spikeling_rightMenuParameterContainer_frame.setFrameShape(QFrame.StyledPanel)
        self.Spikeling_rightMenuParameterContainer_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_56 = QVBoxLayout(self.Spikeling_rightMenuParameterContainer_frame)
        self.verticalLayout_56.setSpacing(0)
        self.verticalLayout_56.setObjectName(u"verticalLayout_56")
        self.verticalLayout_56.setContentsMargins(0, 0, 0, 0)
        self.Spikeling_StimulusParameter_pushButton = QPushButton(self.Spikeling_rightMenuParameterContainer_frame)
        self.Spikeling_StimulusParameter_pushButton.setObjectName(u"Spikeling_StimulusParameter_pushButton")
        self.Spikeling_StimulusParameter_pushButton.setFont(font)
        self.Spikeling_StimulusParameter_pushButton.setIcon(icon4)
        self.Spikeling_StimulusParameter_pushButton.setIconSize(QSize(30, 30))

        self.verticalLayout_56.addWidget(self.Spikeling_StimulusParameter_pushButton)

        self.Spikeling_NeuronParameter_pushButton = QPushButton(self.Spikeling_rightMenuParameterContainer_frame)
        self.Spikeling_NeuronParameter_pushButton.setObjectName(u"Spikeling_NeuronParameter_pushButton")
        self.Spikeling_NeuronParameter_pushButton.setFont(font)
        self.Spikeling_NeuronParameter_pushButton.setIcon(icon1)
        self.Spikeling_NeuronParameter_pushButton.setIconSize(QSize(30, 30))

        self.verticalLayout_56.addWidget(self.Spikeling_NeuronParameter_pushButton)


        self.verticalLayout_55.addWidget(self.Spikeling_rightMenuParameterContainer_frame)

        self.frame = QFrame(self.Spikeling_rightMenuSubContainer)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)

        self.verticalLayout_55.addWidget(self.frame)


        self.verticalLayout_53.addWidget(self.Spikeling_rightMenuSubContainer)


        self.horizontalLayout_34.addWidget(self.Spikeling_rightMenuContainer)

        self.mainbody_stackedWidget.addWidget(self.page_101)
        self.page_102 = QWidget()
        self.page_102.setObjectName(u"page_102")
        self.horizontalLayout_66 = QHBoxLayout(self.page_102)
        self.horizontalLayout_66.setSpacing(0)
        self.horizontalLayout_66.setObjectName(u"horizontalLayout_66")
        self.horizontalLayout_66.setContentsMargins(0, 0, 0, 0)
        self.frame_42 = QFrame(self.page_102)
        self.frame_42.setObjectName(u"frame_42")
        self.frame_42.setFrameShape(QFrame.StyledPanel)
        self.frame_42.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_67 = QHBoxLayout(self.frame_42)
        self.horizontalLayout_67.setObjectName(u"horizontalLayout_67")
        self.label_2 = QLabel(self.frame_42)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setPixmap(QPixmap(u":/resources/resources/under_construction.svg"))
        self.label_2.setScaledContents(True)

        self.horizontalLayout_67.addWidget(self.label_2)


        self.horizontalLayout_66.addWidget(self.frame_42)

        self.mainbody_stackedWidget.addWidget(self.page_102)
        self.page_103 = QWidget()
        self.page_103.setObjectName(u"page_103")
        self.horizontalLayout_68 = QHBoxLayout(self.page_103)
        self.horizontalLayout_68.setSpacing(0)
        self.horizontalLayout_68.setObjectName(u"horizontalLayout_68")
        self.horizontalLayout_68.setContentsMargins(0, 0, 0, 0)
        self.DataAnalysis_frame = QFrame(self.page_103)
        self.DataAnalysis_frame.setObjectName(u"DataAnalysis_frame")
        self.DataAnalysis_frame.setFrameShape(QFrame.StyledPanel)
        self.DataAnalysis_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_61 = QHBoxLayout(self.DataAnalysis_frame)
        self.horizontalLayout_61.setSpacing(0)
        self.horizontalLayout_61.setObjectName(u"horizontalLayout_61")
        self.horizontalLayout_61.setContentsMargins(0, 0, 0, 0)
        self.DataAnalysis_Display_frame = QFrame(self.DataAnalysis_frame)
        self.DataAnalysis_Display_frame.setObjectName(u"DataAnalysis_Display_frame")
        self.DataAnalysis_Display_frame.setFrameShape(QFrame.StyledPanel)
        self.DataAnalysis_Display_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_35 = QVBoxLayout(self.DataAnalysis_Display_frame)
        self.verticalLayout_35.setSpacing(0)
        self.verticalLayout_35.setObjectName(u"verticalLayout_35")
        self.verticalLayout_35.setContentsMargins(0, 0, 0, 0)
        self.DataAnalysis_Display_StackedWidget = QStackedWidget(self.DataAnalysis_Display_frame)
        self.DataAnalysis_Display_StackedWidget.setObjectName(u"DataAnalysis_Display_StackedWidget")
        self.page_103_1_0 = QWidget()
        self.page_103_1_0.setObjectName(u"page_103_1_0")
        self.verticalLayout_39 = QVBoxLayout(self.page_103_1_0)
        self.verticalLayout_39.setSpacing(0)
        self.verticalLayout_39.setObjectName(u"verticalLayout_39")
        self.verticalLayout_39.setContentsMargins(0, 0, 0, 0)
        self.DataAnalysis_Oscilloscope_widget1_0_0 = PlotWidget(self.page_103_1_0)
        self.DataAnalysis_Oscilloscope_widget1_0_0.setObjectName(u"DataAnalysis_Oscilloscope_widget1_0_0")
        sizePolicy2.setHeightForWidth(self.DataAnalysis_Oscilloscope_widget1_0_0.sizePolicy().hasHeightForWidth())
        self.DataAnalysis_Oscilloscope_widget1_0_0.setSizePolicy(sizePolicy2)
        self.DataAnalysis_Oscilloscope_widget1_0_0.setStyleSheet(u"background-color: rgb(0, 30, 38);")

        self.verticalLayout_39.addWidget(self.DataAnalysis_Oscilloscope_widget1_0_0)

        self.line_7 = QFrame(self.page_103_1_0)
        self.line_7.setObjectName(u"line_7")
        self.line_7.setFrameShape(QFrame.HLine)
        self.line_7.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_39.addWidget(self.line_7)

        self.DataAnalysis_Oscilloscope_widget1_0_1 = PlotWidget(self.page_103_1_0)
        self.DataAnalysis_Oscilloscope_widget1_0_1.setObjectName(u"DataAnalysis_Oscilloscope_widget1_0_1")
        sizePolicy2.setHeightForWidth(self.DataAnalysis_Oscilloscope_widget1_0_1.sizePolicy().hasHeightForWidth())
        self.DataAnalysis_Oscilloscope_widget1_0_1.setSizePolicy(sizePolicy2)
        self.DataAnalysis_Oscilloscope_widget1_0_1.setStyleSheet(u"background-color: rgb(0, 30, 38);")

        self.verticalLayout_39.addWidget(self.DataAnalysis_Oscilloscope_widget1_0_1)

        self.line_31 = QFrame(self.page_103_1_0)
        self.line_31.setObjectName(u"line_31")
        self.line_31.setFrameShape(QFrame.HLine)
        self.line_31.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_39.addWidget(self.line_31)

        self.DataAnalysis_Oscilloscope_widget1_0_2 = PlotWidget(self.page_103_1_0)
        self.DataAnalysis_Oscilloscope_widget1_0_2.setObjectName(u"DataAnalysis_Oscilloscope_widget1_0_2")
        sizePolicy1.setHeightForWidth(self.DataAnalysis_Oscilloscope_widget1_0_2.sizePolicy().hasHeightForWidth())
        self.DataAnalysis_Oscilloscope_widget1_0_2.setSizePolicy(sizePolicy1)
        self.DataAnalysis_Oscilloscope_widget1_0_2.setMinimumSize(QSize(0, 100))
        self.DataAnalysis_Oscilloscope_widget1_0_2.setMaximumSize(QSize(16777215, 100))
        self.DataAnalysis_Oscilloscope_widget1_0_2.setStyleSheet(u"background-color: rgb(0, 30, 38);")

        self.verticalLayout_39.addWidget(self.DataAnalysis_Oscilloscope_widget1_0_2)

        self.line_8 = QFrame(self.page_103_1_0)
        self.line_8.setObjectName(u"line_8")
        self.line_8.setFrameShape(QFrame.HLine)
        self.line_8.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_39.addWidget(self.line_8)

        self.DataAnalysis_Oscilloscope_widget1_0_3 = PlotWidget(self.page_103_1_0)
        self.DataAnalysis_Oscilloscope_widget1_0_3.setObjectName(u"DataAnalysis_Oscilloscope_widget1_0_3")
        sizePolicy1.setHeightForWidth(self.DataAnalysis_Oscilloscope_widget1_0_3.sizePolicy().hasHeightForWidth())
        self.DataAnalysis_Oscilloscope_widget1_0_3.setSizePolicy(sizePolicy1)
        self.DataAnalysis_Oscilloscope_widget1_0_3.setMinimumSize(QSize(0, 150))
        self.DataAnalysis_Oscilloscope_widget1_0_3.setMaximumSize(QSize(16777215, 150))
        self.DataAnalysis_Oscilloscope_widget1_0_3.setStyleSheet(u"background-color: rgb(0, 30, 38);")

        self.verticalLayout_39.addWidget(self.DataAnalysis_Oscilloscope_widget1_0_3)

        self.line_32 = QFrame(self.page_103_1_0)
        self.line_32.setObjectName(u"line_32")
        self.line_32.setFrameShape(QFrame.HLine)
        self.line_32.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_39.addWidget(self.line_32)

        self.DataAnalysis_Neurons_pushButton10_frame = QFrame(self.page_103_1_0)
        self.DataAnalysis_Neurons_pushButton10_frame.setObjectName(u"DataAnalysis_Neurons_pushButton10_frame")
        sizePolicy3.setHeightForWidth(self.DataAnalysis_Neurons_pushButton10_frame.sizePolicy().hasHeightForWidth())
        self.DataAnalysis_Neurons_pushButton10_frame.setSizePolicy(sizePolicy3)
        self.DataAnalysis_Neurons_pushButton10_frame.setMinimumSize(QSize(0, 25))
        self.DataAnalysis_Neurons_pushButton10_frame.setFrameShape(QFrame.StyledPanel)
        self.DataAnalysis_Neurons_pushButton10_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_80 = QHBoxLayout(self.DataAnalysis_Neurons_pushButton10_frame)
        self.horizontalLayout_80.setSpacing(5)
        self.horizontalLayout_80.setObjectName(u"horizontalLayout_80")
        self.horizontalLayout_80.setContentsMargins(5, 0, 5, 0)
        self.DataAnalysis_Neuron0Vm_pushButton10 = QPushButton(self.DataAnalysis_Neurons_pushButton10_frame)
        self.DataAnalysis_Neuron0Vm_pushButton10.setObjectName(u"DataAnalysis_Neuron0Vm_pushButton10")
        self.DataAnalysis_Neuron0Vm_pushButton10.setMinimumSize(QSize(25, 0))
        self.DataAnalysis_Neuron0Vm_pushButton10.setMaximumSize(QSize(16777215, 25))
        self.DataAnalysis_Neuron0Vm_pushButton10.setFont(font1)
        self.DataAnalysis_Neuron0Vm_pushButton10.setStyleSheet(u"color: rgb(220, 50, 47);")

        self.horizontalLayout_80.addWidget(self.DataAnalysis_Neuron0Vm_pushButton10)

        self.DataAnalysis_Neuron1Vm_pushButton10 = QPushButton(self.DataAnalysis_Neurons_pushButton10_frame)
        self.DataAnalysis_Neuron1Vm_pushButton10.setObjectName(u"DataAnalysis_Neuron1Vm_pushButton10")
        self.DataAnalysis_Neuron1Vm_pushButton10.setMinimumSize(QSize(0, 25))
        self.DataAnalysis_Neuron1Vm_pushButton10.setMaximumSize(QSize(16777215, 25))
        self.DataAnalysis_Neuron1Vm_pushButton10.setFont(font1)
        self.DataAnalysis_Neuron1Vm_pushButton10.setStyleSheet(u"color: rgb(203, 75, 22);")

        self.horizontalLayout_80.addWidget(self.DataAnalysis_Neuron1Vm_pushButton10)

        self.DataAnalysis_Neuron2Vm_pushButton10 = QPushButton(self.DataAnalysis_Neurons_pushButton10_frame)
        self.DataAnalysis_Neuron2Vm_pushButton10.setObjectName(u"DataAnalysis_Neuron2Vm_pushButton10")
        sizePolicy7 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(25)
        sizePolicy7.setHeightForWidth(self.DataAnalysis_Neuron2Vm_pushButton10.sizePolicy().hasHeightForWidth())
        self.DataAnalysis_Neuron2Vm_pushButton10.setSizePolicy(sizePolicy7)
        self.DataAnalysis_Neuron2Vm_pushButton10.setMinimumSize(QSize(0, 25))
        self.DataAnalysis_Neuron2Vm_pushButton10.setMaximumSize(QSize(16777215, 25))
        self.DataAnalysis_Neuron2Vm_pushButton10.setFont(font1)
        self.DataAnalysis_Neuron2Vm_pushButton10.setStyleSheet(u"color: rgb(181, 137, 0);")

        self.horizontalLayout_80.addWidget(self.DataAnalysis_Neuron2Vm_pushButton10)


        self.verticalLayout_39.addWidget(self.DataAnalysis_Neurons_pushButton10_frame)

        self.DataAnalysis_Display_StackedWidget.addWidget(self.page_103_1_0)
        self.page_103_1_1 = QWidget()
        self.page_103_1_1.setObjectName(u"page_103_1_1")
        self.verticalLayout_48 = QVBoxLayout(self.page_103_1_1)
        self.verticalLayout_48.setSpacing(0)
        self.verticalLayout_48.setObjectName(u"verticalLayout_48")
        self.verticalLayout_48.setContentsMargins(0, 0, 0, 0)
        self.DataAnalysis_Oscilloscope_widget1_1_0 = PlotWidget(self.page_103_1_1)
        self.DataAnalysis_Oscilloscope_widget1_1_0.setObjectName(u"DataAnalysis_Oscilloscope_widget1_1_0")
        sizePolicy2.setHeightForWidth(self.DataAnalysis_Oscilloscope_widget1_1_0.sizePolicy().hasHeightForWidth())
        self.DataAnalysis_Oscilloscope_widget1_1_0.setSizePolicy(sizePolicy2)
        self.DataAnalysis_Oscilloscope_widget1_1_0.setStyleSheet(u"background-color: rgb(0, 30, 38);")

        self.verticalLayout_48.addWidget(self.DataAnalysis_Oscilloscope_widget1_1_0)

        self.line_10 = QFrame(self.page_103_1_1)
        self.line_10.setObjectName(u"line_10")
        self.line_10.setFrameShape(QFrame.HLine)
        self.line_10.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_48.addWidget(self.line_10)

        self.DataAnalysis_Oscilloscope_widget1_1_1 = PlotWidget(self.page_103_1_1)
        self.DataAnalysis_Oscilloscope_widget1_1_1.setObjectName(u"DataAnalysis_Oscilloscope_widget1_1_1")
        sizePolicy2.setHeightForWidth(self.DataAnalysis_Oscilloscope_widget1_1_1.sizePolicy().hasHeightForWidth())
        self.DataAnalysis_Oscilloscope_widget1_1_1.setSizePolicy(sizePolicy2)
        self.DataAnalysis_Oscilloscope_widget1_1_1.setStyleSheet(u"background-color: rgb(0, 30, 38);")

        self.verticalLayout_48.addWidget(self.DataAnalysis_Oscilloscope_widget1_1_1)

        self.line_9 = QFrame(self.page_103_1_1)
        self.line_9.setObjectName(u"line_9")
        self.line_9.setFrameShape(QFrame.HLine)
        self.line_9.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_48.addWidget(self.line_9)

        self.DataAnalysis_Oscilloscope_widget1_1_2 = PlotWidget(self.page_103_1_1)
        self.DataAnalysis_Oscilloscope_widget1_1_2.setObjectName(u"DataAnalysis_Oscilloscope_widget1_1_2")
        sizePolicy1.setHeightForWidth(self.DataAnalysis_Oscilloscope_widget1_1_2.sizePolicy().hasHeightForWidth())
        self.DataAnalysis_Oscilloscope_widget1_1_2.setSizePolicy(sizePolicy1)
        self.DataAnalysis_Oscilloscope_widget1_1_2.setMinimumSize(QSize(0, 150))
        self.DataAnalysis_Oscilloscope_widget1_1_2.setMaximumSize(QSize(16777215, 150))
        self.DataAnalysis_Oscilloscope_widget1_1_2.setStyleSheet(u"background-color: rgb(0, 30, 38);")

        self.verticalLayout_48.addWidget(self.DataAnalysis_Oscilloscope_widget1_1_2)

        self.line_33 = QFrame(self.page_103_1_1)
        self.line_33.setObjectName(u"line_33")
        self.line_33.setFrameShape(QFrame.HLine)
        self.line_33.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_48.addWidget(self.line_33)

        self.DataAnalysis_Neurons_pushButton11_frame = QFrame(self.page_103_1_1)
        self.DataAnalysis_Neurons_pushButton11_frame.setObjectName(u"DataAnalysis_Neurons_pushButton11_frame")
        sizePolicy3.setHeightForWidth(self.DataAnalysis_Neurons_pushButton11_frame.sizePolicy().hasHeightForWidth())
        self.DataAnalysis_Neurons_pushButton11_frame.setSizePolicy(sizePolicy3)
        self.DataAnalysis_Neurons_pushButton11_frame.setMinimumSize(QSize(0, 25))
        self.DataAnalysis_Neurons_pushButton11_frame.setFrameShape(QFrame.StyledPanel)
        self.DataAnalysis_Neurons_pushButton11_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_101 = QHBoxLayout(self.DataAnalysis_Neurons_pushButton11_frame)
        self.horizontalLayout_101.setSpacing(5)
        self.horizontalLayout_101.setObjectName(u"horizontalLayout_101")
        self.horizontalLayout_101.setContentsMargins(5, 0, 5, 0)
        self.DataAnalysis_Neuron0Vm_pushButton11 = QPushButton(self.DataAnalysis_Neurons_pushButton11_frame)
        self.DataAnalysis_Neuron0Vm_pushButton11.setObjectName(u"DataAnalysis_Neuron0Vm_pushButton11")
        self.DataAnalysis_Neuron0Vm_pushButton11.setMinimumSize(QSize(25, 0))
        self.DataAnalysis_Neuron0Vm_pushButton11.setMaximumSize(QSize(16777215, 25))
        self.DataAnalysis_Neuron0Vm_pushButton11.setFont(font1)
        self.DataAnalysis_Neuron0Vm_pushButton11.setStyleSheet(u"color: rgb(220, 50, 47);")

        self.horizontalLayout_101.addWidget(self.DataAnalysis_Neuron0Vm_pushButton11)

        self.DataAnalysis_Neuron1Vm_pushButton11 = QPushButton(self.DataAnalysis_Neurons_pushButton11_frame)
        self.DataAnalysis_Neuron1Vm_pushButton11.setObjectName(u"DataAnalysis_Neuron1Vm_pushButton11")
        self.DataAnalysis_Neuron1Vm_pushButton11.setMinimumSize(QSize(0, 25))
        self.DataAnalysis_Neuron1Vm_pushButton11.setMaximumSize(QSize(16777215, 25))
        self.DataAnalysis_Neuron1Vm_pushButton11.setFont(font1)
        self.DataAnalysis_Neuron1Vm_pushButton11.setStyleSheet(u"color: rgb(203, 75, 22);")

        self.horizontalLayout_101.addWidget(self.DataAnalysis_Neuron1Vm_pushButton11)

        self.DataAnalysis_Neuron2Vm_pushButton11 = QPushButton(self.DataAnalysis_Neurons_pushButton11_frame)
        self.DataAnalysis_Neuron2Vm_pushButton11.setObjectName(u"DataAnalysis_Neuron2Vm_pushButton11")
        sizePolicy7.setHeightForWidth(self.DataAnalysis_Neuron2Vm_pushButton11.sizePolicy().hasHeightForWidth())
        self.DataAnalysis_Neuron2Vm_pushButton11.setSizePolicy(sizePolicy7)
        self.DataAnalysis_Neuron2Vm_pushButton11.setMinimumSize(QSize(0, 25))
        self.DataAnalysis_Neuron2Vm_pushButton11.setMaximumSize(QSize(16777215, 25))
        self.DataAnalysis_Neuron2Vm_pushButton11.setFont(font1)
        self.DataAnalysis_Neuron2Vm_pushButton11.setStyleSheet(u"color: rgb(181, 137, 0);")

        self.horizontalLayout_101.addWidget(self.DataAnalysis_Neuron2Vm_pushButton11)


        self.verticalLayout_48.addWidget(self.DataAnalysis_Neurons_pushButton11_frame)

        self.DataAnalysis_Display_StackedWidget.addWidget(self.page_103_1_1)
        self.page_103_1_2 = QWidget()
        self.page_103_1_2.setObjectName(u"page_103_1_2")
        self.verticalLayout_49 = QVBoxLayout(self.page_103_1_2)
        self.verticalLayout_49.setSpacing(0)
        self.verticalLayout_49.setObjectName(u"verticalLayout_49")
        self.verticalLayout_49.setContentsMargins(0, 0, 0, 0)
        self.DataAnalysis_Oscilloscope_widget1_2_0 = PlotWidget(self.page_103_1_2)
        self.DataAnalysis_Oscilloscope_widget1_2_0.setObjectName(u"DataAnalysis_Oscilloscope_widget1_2_0")
        sizePolicy2.setHeightForWidth(self.DataAnalysis_Oscilloscope_widget1_2_0.sizePolicy().hasHeightForWidth())
        self.DataAnalysis_Oscilloscope_widget1_2_0.setSizePolicy(sizePolicy2)
        self.DataAnalysis_Oscilloscope_widget1_2_0.setStyleSheet(u"background-color: rgb(0, 30, 38);")

        self.verticalLayout_49.addWidget(self.DataAnalysis_Oscilloscope_widget1_2_0)

        self.line_30 = QFrame(self.page_103_1_2)
        self.line_30.setObjectName(u"line_30")
        self.line_30.setFrameShape(QFrame.HLine)
        self.line_30.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_49.addWidget(self.line_30)

        self.DataAnalysis_Oscilloscope_widget1_2_1 = PlotWidget(self.page_103_1_2)
        self.DataAnalysis_Oscilloscope_widget1_2_1.setObjectName(u"DataAnalysis_Oscilloscope_widget1_2_1")
        sizePolicy2.setHeightForWidth(self.DataAnalysis_Oscilloscope_widget1_2_1.sizePolicy().hasHeightForWidth())
        self.DataAnalysis_Oscilloscope_widget1_2_1.setSizePolicy(sizePolicy2)
        self.DataAnalysis_Oscilloscope_widget1_2_1.setMinimumSize(QSize(0, 0))
        self.DataAnalysis_Oscilloscope_widget1_2_1.setMaximumSize(QSize(16777215, 16777215))
        self.DataAnalysis_Oscilloscope_widget1_2_1.setStyleSheet(u"background-color: rgb(0, 30, 38);")

        self.verticalLayout_49.addWidget(self.DataAnalysis_Oscilloscope_widget1_2_1)

        self.line_29 = QFrame(self.page_103_1_2)
        self.line_29.setObjectName(u"line_29")
        self.line_29.setFrameShape(QFrame.HLine)
        self.line_29.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_49.addWidget(self.line_29)

        self.DataAnalysis_Oscilloscope_widget1_2_2 = PlotWidget(self.page_103_1_2)
        self.DataAnalysis_Oscilloscope_widget1_2_2.setObjectName(u"DataAnalysis_Oscilloscope_widget1_2_2")
        sizePolicy1.setHeightForWidth(self.DataAnalysis_Oscilloscope_widget1_2_2.sizePolicy().hasHeightForWidth())
        self.DataAnalysis_Oscilloscope_widget1_2_2.setSizePolicy(sizePolicy1)
        self.DataAnalysis_Oscilloscope_widget1_2_2.setMinimumSize(QSize(0, 150))
        self.DataAnalysis_Oscilloscope_widget1_2_2.setMaximumSize(QSize(16777215, 150))
        font5 = QFont()
        font5.setPointSize(11)
        self.DataAnalysis_Oscilloscope_widget1_2_2.setFont(font5)
        self.DataAnalysis_Oscilloscope_widget1_2_2.setStyleSheet(u"background-color: rgb(0, 30, 38);")

        self.verticalLayout_49.addWidget(self.DataAnalysis_Oscilloscope_widget1_2_2)

        self.line_34 = QFrame(self.page_103_1_2)
        self.line_34.setObjectName(u"line_34")
        self.line_34.setFrameShape(QFrame.HLine)
        self.line_34.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_49.addWidget(self.line_34)

        self.DataAnalysis_Neurons_pushButton12_frame = QFrame(self.page_103_1_2)
        self.DataAnalysis_Neurons_pushButton12_frame.setObjectName(u"DataAnalysis_Neurons_pushButton12_frame")
        sizePolicy3.setHeightForWidth(self.DataAnalysis_Neurons_pushButton12_frame.sizePolicy().hasHeightForWidth())
        self.DataAnalysis_Neurons_pushButton12_frame.setSizePolicy(sizePolicy3)
        self.DataAnalysis_Neurons_pushButton12_frame.setMinimumSize(QSize(0, 25))
        self.DataAnalysis_Neurons_pushButton12_frame.setFrameShape(QFrame.StyledPanel)
        self.DataAnalysis_Neurons_pushButton12_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_103 = QHBoxLayout(self.DataAnalysis_Neurons_pushButton12_frame)
        self.horizontalLayout_103.setSpacing(5)
        self.horizontalLayout_103.setObjectName(u"horizontalLayout_103")
        self.horizontalLayout_103.setContentsMargins(5, 0, 5, 0)
        self.DataAnalysis_Neuron0Vm_pushButton12 = QPushButton(self.DataAnalysis_Neurons_pushButton12_frame)
        self.DataAnalysis_Neuron0Vm_pushButton12.setObjectName(u"DataAnalysis_Neuron0Vm_pushButton12")
        self.DataAnalysis_Neuron0Vm_pushButton12.setMinimumSize(QSize(25, 0))
        self.DataAnalysis_Neuron0Vm_pushButton12.setMaximumSize(QSize(16777215, 25))
        self.DataAnalysis_Neuron0Vm_pushButton12.setFont(font1)
        self.DataAnalysis_Neuron0Vm_pushButton12.setStyleSheet(u"color: rgb(220, 50, 47);")

        self.horizontalLayout_103.addWidget(self.DataAnalysis_Neuron0Vm_pushButton12)

        self.DataAnalysis_Neuron1Vm_pushButton12 = QPushButton(self.DataAnalysis_Neurons_pushButton12_frame)
        self.DataAnalysis_Neuron1Vm_pushButton12.setObjectName(u"DataAnalysis_Neuron1Vm_pushButton12")
        self.DataAnalysis_Neuron1Vm_pushButton12.setMinimumSize(QSize(0, 25))
        self.DataAnalysis_Neuron1Vm_pushButton12.setMaximumSize(QSize(16777215, 25))
        self.DataAnalysis_Neuron1Vm_pushButton12.setFont(font1)
        self.DataAnalysis_Neuron1Vm_pushButton12.setStyleSheet(u"color: rgb(203, 75, 22);")

        self.horizontalLayout_103.addWidget(self.DataAnalysis_Neuron1Vm_pushButton12)

        self.DataAnalysis_Neuron2Vm_pushButton12 = QPushButton(self.DataAnalysis_Neurons_pushButton12_frame)
        self.DataAnalysis_Neuron2Vm_pushButton12.setObjectName(u"DataAnalysis_Neuron2Vm_pushButton12")
        sizePolicy7.setHeightForWidth(self.DataAnalysis_Neuron2Vm_pushButton12.sizePolicy().hasHeightForWidth())
        self.DataAnalysis_Neuron2Vm_pushButton12.setSizePolicy(sizePolicy7)
        self.DataAnalysis_Neuron2Vm_pushButton12.setMinimumSize(QSize(0, 25))
        self.DataAnalysis_Neuron2Vm_pushButton12.setMaximumSize(QSize(16777215, 25))
        self.DataAnalysis_Neuron2Vm_pushButton12.setFont(font1)
        self.DataAnalysis_Neuron2Vm_pushButton12.setStyleSheet(u"color: rgb(181, 137, 0);")

        self.horizontalLayout_103.addWidget(self.DataAnalysis_Neuron2Vm_pushButton12)


        self.verticalLayout_49.addWidget(self.DataAnalysis_Neurons_pushButton12_frame)

        self.DataAnalysis_Display_StackedWidget.addWidget(self.page_103_1_2)
        self.page_103_2_0 = QWidget()
        self.page_103_2_0.setObjectName(u"page_103_2_0")
        self.verticalLayout_42 = QVBoxLayout(self.page_103_2_0)
        self.verticalLayout_42.setSpacing(0)
        self.verticalLayout_42.setObjectName(u"verticalLayout_42")
        self.verticalLayout_42.setContentsMargins(0, 0, 0, 0)
        self.DataAnalysis_Oscilloscope_widget2_0_0 = PlotWidget(self.page_103_2_0)
        self.DataAnalysis_Oscilloscope_widget2_0_0.setObjectName(u"DataAnalysis_Oscilloscope_widget2_0_0")
        sizePolicy2.setHeightForWidth(self.DataAnalysis_Oscilloscope_widget2_0_0.sizePolicy().hasHeightForWidth())
        self.DataAnalysis_Oscilloscope_widget2_0_0.setSizePolicy(sizePolicy2)
        self.DataAnalysis_Oscilloscope_widget2_0_0.setStyleSheet(u"background-color: rgb(0, 30, 38);")

        self.verticalLayout_42.addWidget(self.DataAnalysis_Oscilloscope_widget2_0_0)

        self.line_14 = QFrame(self.page_103_2_0)
        self.line_14.setObjectName(u"line_14")
        self.line_14.setFrameShape(QFrame.HLine)
        self.line_14.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_42.addWidget(self.line_14)

        self.DataAnalysis_Oscilloscope_widget2_0_1 = PlotWidget(self.page_103_2_0)
        self.DataAnalysis_Oscilloscope_widget2_0_1.setObjectName(u"DataAnalysis_Oscilloscope_widget2_0_1")
        sizePolicy2.setHeightForWidth(self.DataAnalysis_Oscilloscope_widget2_0_1.sizePolicy().hasHeightForWidth())
        self.DataAnalysis_Oscilloscope_widget2_0_1.setSizePolicy(sizePolicy2)
        self.DataAnalysis_Oscilloscope_widget2_0_1.setStyleSheet(u"background-color: rgb(0, 30, 38);")

        self.verticalLayout_42.addWidget(self.DataAnalysis_Oscilloscope_widget2_0_1)

        self.line_13 = QFrame(self.page_103_2_0)
        self.line_13.setObjectName(u"line_13")
        self.line_13.setFrameShape(QFrame.HLine)
        self.line_13.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_42.addWidget(self.line_13)

        self.DataAnalysis_Oscilloscope_widget2_0_2 = PlotWidget(self.page_103_2_0)
        self.DataAnalysis_Oscilloscope_widget2_0_2.setObjectName(u"DataAnalysis_Oscilloscope_widget2_0_2")
        sizePolicy2.setHeightForWidth(self.DataAnalysis_Oscilloscope_widget2_0_2.sizePolicy().hasHeightForWidth())
        self.DataAnalysis_Oscilloscope_widget2_0_2.setSizePolicy(sizePolicy2)
        self.DataAnalysis_Oscilloscope_widget2_0_2.setStyleSheet(u"background-color: rgb(0, 30, 38);")

        self.verticalLayout_42.addWidget(self.DataAnalysis_Oscilloscope_widget2_0_2)

        self.line_11 = QFrame(self.page_103_2_0)
        self.line_11.setObjectName(u"line_11")
        self.line_11.setFrameShape(QFrame.HLine)
        self.line_11.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_42.addWidget(self.line_11)

        self.DataAnalysis_Oscilloscope_widget2_0_3 = PlotWidget(self.page_103_2_0)
        self.DataAnalysis_Oscilloscope_widget2_0_3.setObjectName(u"DataAnalysis_Oscilloscope_widget2_0_3")
        sizePolicy1.setHeightForWidth(self.DataAnalysis_Oscilloscope_widget2_0_3.sizePolicy().hasHeightForWidth())
        self.DataAnalysis_Oscilloscope_widget2_0_3.setSizePolicy(sizePolicy1)
        self.DataAnalysis_Oscilloscope_widget2_0_3.setMinimumSize(QSize(0, 100))
        self.DataAnalysis_Oscilloscope_widget2_0_3.setMaximumSize(QSize(16777215, 100))
        self.DataAnalysis_Oscilloscope_widget2_0_3.setStyleSheet(u"background-color: rgb(0, 30, 38);\n"
"")

        self.verticalLayout_42.addWidget(self.DataAnalysis_Oscilloscope_widget2_0_3)

        self.line_35 = QFrame(self.page_103_2_0)
        self.line_35.setObjectName(u"line_35")
        self.line_35.setFrameShape(QFrame.HLine)
        self.line_35.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_42.addWidget(self.line_35)

        self.DataAnalysis_Neurons_pushButton20_frame = QFrame(self.page_103_2_0)
        self.DataAnalysis_Neurons_pushButton20_frame.setObjectName(u"DataAnalysis_Neurons_pushButton20_frame")
        sizePolicy3.setHeightForWidth(self.DataAnalysis_Neurons_pushButton20_frame.sizePolicy().hasHeightForWidth())
        self.DataAnalysis_Neurons_pushButton20_frame.setSizePolicy(sizePolicy3)
        self.DataAnalysis_Neurons_pushButton20_frame.setMinimumSize(QSize(0, 25))
        self.DataAnalysis_Neurons_pushButton20_frame.setFrameShape(QFrame.StyledPanel)
        self.DataAnalysis_Neurons_pushButton20_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_105 = QHBoxLayout(self.DataAnalysis_Neurons_pushButton20_frame)
        self.horizontalLayout_105.setSpacing(5)
        self.horizontalLayout_105.setObjectName(u"horizontalLayout_105")
        self.horizontalLayout_105.setContentsMargins(5, 0, 5, 0)
        self.DataAnalysis_Neuron0Vm_pushButton20 = QPushButton(self.DataAnalysis_Neurons_pushButton20_frame)
        self.DataAnalysis_Neuron0Vm_pushButton20.setObjectName(u"DataAnalysis_Neuron0Vm_pushButton20")
        self.DataAnalysis_Neuron0Vm_pushButton20.setMinimumSize(QSize(25, 0))
        self.DataAnalysis_Neuron0Vm_pushButton20.setMaximumSize(QSize(16777215, 25))
        self.DataAnalysis_Neuron0Vm_pushButton20.setFont(font1)
        self.DataAnalysis_Neuron0Vm_pushButton20.setStyleSheet(u"color: rgb(220, 50, 47);")

        self.horizontalLayout_105.addWidget(self.DataAnalysis_Neuron0Vm_pushButton20)

        self.DataAnalysis_Neuron1Vm_pushButton20 = QPushButton(self.DataAnalysis_Neurons_pushButton20_frame)
        self.DataAnalysis_Neuron1Vm_pushButton20.setObjectName(u"DataAnalysis_Neuron1Vm_pushButton20")
        self.DataAnalysis_Neuron1Vm_pushButton20.setMinimumSize(QSize(0, 25))
        self.DataAnalysis_Neuron1Vm_pushButton20.setMaximumSize(QSize(16777215, 25))
        self.DataAnalysis_Neuron1Vm_pushButton20.setFont(font1)
        self.DataAnalysis_Neuron1Vm_pushButton20.setStyleSheet(u"color: rgb(203, 75, 22);")

        self.horizontalLayout_105.addWidget(self.DataAnalysis_Neuron1Vm_pushButton20)

        self.DataAnalysis_Neuron2Vm_pushButton20 = QPushButton(self.DataAnalysis_Neurons_pushButton20_frame)
        self.DataAnalysis_Neuron2Vm_pushButton20.setObjectName(u"DataAnalysis_Neuron2Vm_pushButton20")
        sizePolicy7.setHeightForWidth(self.DataAnalysis_Neuron2Vm_pushButton20.sizePolicy().hasHeightForWidth())
        self.DataAnalysis_Neuron2Vm_pushButton20.setSizePolicy(sizePolicy7)
        self.DataAnalysis_Neuron2Vm_pushButton20.setMinimumSize(QSize(0, 25))
        self.DataAnalysis_Neuron2Vm_pushButton20.setMaximumSize(QSize(16777215, 25))
        self.DataAnalysis_Neuron2Vm_pushButton20.setFont(font1)
        self.DataAnalysis_Neuron2Vm_pushButton20.setStyleSheet(u"color: rgb(181, 137, 0);")

        self.horizontalLayout_105.addWidget(self.DataAnalysis_Neuron2Vm_pushButton20)


        self.verticalLayout_42.addWidget(self.DataAnalysis_Neurons_pushButton20_frame)

        self.DataAnalysis_Display_StackedWidget.addWidget(self.page_103_2_0)
        self.page_103_2_1 = QWidget()
        self.page_103_2_1.setObjectName(u"page_103_2_1")
        self.verticalLayout_43 = QVBoxLayout(self.page_103_2_1)
        self.verticalLayout_43.setSpacing(0)
        self.verticalLayout_43.setObjectName(u"verticalLayout_43")
        self.verticalLayout_43.setContentsMargins(0, 0, 0, 0)
        self.DataAnalysis_Oscilloscope_widget2_1_0 = PlotWidget(self.page_103_2_1)
        self.DataAnalysis_Oscilloscope_widget2_1_0.setObjectName(u"DataAnalysis_Oscilloscope_widget2_1_0")
        sizePolicy2.setHeightForWidth(self.DataAnalysis_Oscilloscope_widget2_1_0.sizePolicy().hasHeightForWidth())
        self.DataAnalysis_Oscilloscope_widget2_1_0.setSizePolicy(sizePolicy2)
        self.DataAnalysis_Oscilloscope_widget2_1_0.setStyleSheet(u"background-color: rgb(0, 30, 38);")

        self.verticalLayout_43.addWidget(self.DataAnalysis_Oscilloscope_widget2_1_0)

        self.line_16 = QFrame(self.page_103_2_1)
        self.line_16.setObjectName(u"line_16")
        self.line_16.setFrameShape(QFrame.HLine)
        self.line_16.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_43.addWidget(self.line_16)

        self.DataAnalysis_Oscilloscope_widget2_1_1 = PlotWidget(self.page_103_2_1)
        self.DataAnalysis_Oscilloscope_widget2_1_1.setObjectName(u"DataAnalysis_Oscilloscope_widget2_1_1")
        sizePolicy2.setHeightForWidth(self.DataAnalysis_Oscilloscope_widget2_1_1.sizePolicy().hasHeightForWidth())
        self.DataAnalysis_Oscilloscope_widget2_1_1.setSizePolicy(sizePolicy2)
        self.DataAnalysis_Oscilloscope_widget2_1_1.setStyleSheet(u"background-color: rgb(0, 30, 38);")

        self.verticalLayout_43.addWidget(self.DataAnalysis_Oscilloscope_widget2_1_1)

        self.line_15 = QFrame(self.page_103_2_1)
        self.line_15.setObjectName(u"line_15")
        self.line_15.setFrameShape(QFrame.HLine)
        self.line_15.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_43.addWidget(self.line_15)

        self.DataAnalysis_Oscilloscope_widget2_1_2 = PlotWidget(self.page_103_2_1)
        self.DataAnalysis_Oscilloscope_widget2_1_2.setObjectName(u"DataAnalysis_Oscilloscope_widget2_1_2")
        sizePolicy2.setHeightForWidth(self.DataAnalysis_Oscilloscope_widget2_1_2.sizePolicy().hasHeightForWidth())
        self.DataAnalysis_Oscilloscope_widget2_1_2.setSizePolicy(sizePolicy2)
        self.DataAnalysis_Oscilloscope_widget2_1_2.setStyleSheet(u"background-color: rgb(0, 30, 38);")

        self.verticalLayout_43.addWidget(self.DataAnalysis_Oscilloscope_widget2_1_2)

        self.line_12 = QFrame(self.page_103_2_1)
        self.line_12.setObjectName(u"line_12")
        self.line_12.setFrameShape(QFrame.HLine)
        self.line_12.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_43.addWidget(self.line_12)

        self.DataAnalysis_Oscilloscope_widget2_1_3 = PlotWidget(self.page_103_2_1)
        self.DataAnalysis_Oscilloscope_widget2_1_3.setObjectName(u"DataAnalysis_Oscilloscope_widget2_1_3")
        sizePolicy1.setHeightForWidth(self.DataAnalysis_Oscilloscope_widget2_1_3.sizePolicy().hasHeightForWidth())
        self.DataAnalysis_Oscilloscope_widget2_1_3.setSizePolicy(sizePolicy1)
        self.DataAnalysis_Oscilloscope_widget2_1_3.setMinimumSize(QSize(0, 100))
        self.DataAnalysis_Oscilloscope_widget2_1_3.setMaximumSize(QSize(16777215, 100))
        self.DataAnalysis_Oscilloscope_widget2_1_3.setStyleSheet(u"background-color: rgb(0, 30, 38);\n"
"")

        self.verticalLayout_43.addWidget(self.DataAnalysis_Oscilloscope_widget2_1_3)

        self.line_36 = QFrame(self.page_103_2_1)
        self.line_36.setObjectName(u"line_36")
        self.line_36.setFrameShape(QFrame.HLine)
        self.line_36.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_43.addWidget(self.line_36)

        self.DataAnalysis_Neurons_pushButton21_frame = QFrame(self.page_103_2_1)
        self.DataAnalysis_Neurons_pushButton21_frame.setObjectName(u"DataAnalysis_Neurons_pushButton21_frame")
        sizePolicy3.setHeightForWidth(self.DataAnalysis_Neurons_pushButton21_frame.sizePolicy().hasHeightForWidth())
        self.DataAnalysis_Neurons_pushButton21_frame.setSizePolicy(sizePolicy3)
        self.DataAnalysis_Neurons_pushButton21_frame.setMinimumSize(QSize(0, 25))
        self.DataAnalysis_Neurons_pushButton21_frame.setFrameShape(QFrame.StyledPanel)
        self.DataAnalysis_Neurons_pushButton21_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_107 = QHBoxLayout(self.DataAnalysis_Neurons_pushButton21_frame)
        self.horizontalLayout_107.setSpacing(5)
        self.horizontalLayout_107.setObjectName(u"horizontalLayout_107")
        self.horizontalLayout_107.setContentsMargins(5, 0, 5, 0)
        self.DataAnalysis_Neuron0Vm_pushButton21 = QPushButton(self.DataAnalysis_Neurons_pushButton21_frame)
        self.DataAnalysis_Neuron0Vm_pushButton21.setObjectName(u"DataAnalysis_Neuron0Vm_pushButton21")
        self.DataAnalysis_Neuron0Vm_pushButton21.setMinimumSize(QSize(25, 0))
        self.DataAnalysis_Neuron0Vm_pushButton21.setMaximumSize(QSize(16777215, 25))
        self.DataAnalysis_Neuron0Vm_pushButton21.setFont(font1)
        self.DataAnalysis_Neuron0Vm_pushButton21.setStyleSheet(u"color: rgb(220, 50, 47);")

        self.horizontalLayout_107.addWidget(self.DataAnalysis_Neuron0Vm_pushButton21)

        self.DataAnalysis_Neuron1Vm_pushButton21 = QPushButton(self.DataAnalysis_Neurons_pushButton21_frame)
        self.DataAnalysis_Neuron1Vm_pushButton21.setObjectName(u"DataAnalysis_Neuron1Vm_pushButton21")
        self.DataAnalysis_Neuron1Vm_pushButton21.setMinimumSize(QSize(0, 25))
        self.DataAnalysis_Neuron1Vm_pushButton21.setMaximumSize(QSize(16777215, 25))
        self.DataAnalysis_Neuron1Vm_pushButton21.setFont(font1)
        self.DataAnalysis_Neuron1Vm_pushButton21.setStyleSheet(u"color: rgb(203, 75, 22);")

        self.horizontalLayout_107.addWidget(self.DataAnalysis_Neuron1Vm_pushButton21)

        self.DataAnalysis_Neuron2Vm_pushButton21 = QPushButton(self.DataAnalysis_Neurons_pushButton21_frame)
        self.DataAnalysis_Neuron2Vm_pushButton21.setObjectName(u"DataAnalysis_Neuron2Vm_pushButton21")
        sizePolicy7.setHeightForWidth(self.DataAnalysis_Neuron2Vm_pushButton21.sizePolicy().hasHeightForWidth())
        self.DataAnalysis_Neuron2Vm_pushButton21.setSizePolicy(sizePolicy7)
        self.DataAnalysis_Neuron2Vm_pushButton21.setMinimumSize(QSize(0, 25))
        self.DataAnalysis_Neuron2Vm_pushButton21.setMaximumSize(QSize(16777215, 25))
        self.DataAnalysis_Neuron2Vm_pushButton21.setFont(font1)
        self.DataAnalysis_Neuron2Vm_pushButton21.setStyleSheet(u"color: rgb(181, 137, 0);")

        self.horizontalLayout_107.addWidget(self.DataAnalysis_Neuron2Vm_pushButton21)


        self.verticalLayout_43.addWidget(self.DataAnalysis_Neurons_pushButton21_frame)

        self.DataAnalysis_Display_StackedWidget.addWidget(self.page_103_2_1)
        self.page_103_2_2 = QWidget()
        self.page_103_2_2.setObjectName(u"page_103_2_2")
        self.verticalLayout_44 = QVBoxLayout(self.page_103_2_2)
        self.verticalLayout_44.setSpacing(0)
        self.verticalLayout_44.setObjectName(u"verticalLayout_44")
        self.verticalLayout_44.setContentsMargins(0, 0, 0, 0)
        self.DataAnalysis_Oscilloscope_widget2_2_0 = PlotWidget(self.page_103_2_2)
        self.DataAnalysis_Oscilloscope_widget2_2_0.setObjectName(u"DataAnalysis_Oscilloscope_widget2_2_0")
        sizePolicy2.setHeightForWidth(self.DataAnalysis_Oscilloscope_widget2_2_0.sizePolicy().hasHeightForWidth())
        self.DataAnalysis_Oscilloscope_widget2_2_0.setSizePolicy(sizePolicy2)
        self.DataAnalysis_Oscilloscope_widget2_2_0.setStyleSheet(u"background-color: rgb(0, 30, 38);")

        self.verticalLayout_44.addWidget(self.DataAnalysis_Oscilloscope_widget2_2_0)

        self.line_18 = QFrame(self.page_103_2_2)
        self.line_18.setObjectName(u"line_18")
        self.line_18.setFrameShape(QFrame.HLine)
        self.line_18.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_44.addWidget(self.line_18)

        self.DataAnalysis_Oscilloscope_widget2_2_1 = PlotWidget(self.page_103_2_2)
        self.DataAnalysis_Oscilloscope_widget2_2_1.setObjectName(u"DataAnalysis_Oscilloscope_widget2_2_1")
        sizePolicy2.setHeightForWidth(self.DataAnalysis_Oscilloscope_widget2_2_1.sizePolicy().hasHeightForWidth())
        self.DataAnalysis_Oscilloscope_widget2_2_1.setSizePolicy(sizePolicy2)
        self.DataAnalysis_Oscilloscope_widget2_2_1.setStyleSheet(u"background-color: rgb(0, 30, 38);")

        self.verticalLayout_44.addWidget(self.DataAnalysis_Oscilloscope_widget2_2_1)

        self.line_17 = QFrame(self.page_103_2_2)
        self.line_17.setObjectName(u"line_17")
        self.line_17.setFrameShape(QFrame.HLine)
        self.line_17.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_44.addWidget(self.line_17)

        self.DataAnalysis_Oscilloscope_widget2_2_2 = PlotWidget(self.page_103_2_2)
        self.DataAnalysis_Oscilloscope_widget2_2_2.setObjectName(u"DataAnalysis_Oscilloscope_widget2_2_2")
        sizePolicy2.setHeightForWidth(self.DataAnalysis_Oscilloscope_widget2_2_2.sizePolicy().hasHeightForWidth())
        self.DataAnalysis_Oscilloscope_widget2_2_2.setSizePolicy(sizePolicy2)
        self.DataAnalysis_Oscilloscope_widget2_2_2.setStyleSheet(u"background-color: rgb(0, 30, 38);")

        self.verticalLayout_44.addWidget(self.DataAnalysis_Oscilloscope_widget2_2_2)

        self.line_19 = QFrame(self.page_103_2_2)
        self.line_19.setObjectName(u"line_19")
        self.line_19.setFrameShape(QFrame.HLine)
        self.line_19.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_44.addWidget(self.line_19)

        self.DataAnalysis_Oscilloscope_widget2_2_3 = PlotWidget(self.page_103_2_2)
        self.DataAnalysis_Oscilloscope_widget2_2_3.setObjectName(u"DataAnalysis_Oscilloscope_widget2_2_3")
        sizePolicy1.setHeightForWidth(self.DataAnalysis_Oscilloscope_widget2_2_3.sizePolicy().hasHeightForWidth())
        self.DataAnalysis_Oscilloscope_widget2_2_3.setSizePolicy(sizePolicy1)
        self.DataAnalysis_Oscilloscope_widget2_2_3.setMinimumSize(QSize(0, 100))
        self.DataAnalysis_Oscilloscope_widget2_2_3.setMaximumSize(QSize(16777215, 100))
        self.DataAnalysis_Oscilloscope_widget2_2_3.setStyleSheet(u"background-color: rgb(0, 30, 38);")

        self.verticalLayout_44.addWidget(self.DataAnalysis_Oscilloscope_widget2_2_3)

        self.line_37 = QFrame(self.page_103_2_2)
        self.line_37.setObjectName(u"line_37")
        self.line_37.setFrameShape(QFrame.HLine)
        self.line_37.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_44.addWidget(self.line_37)

        self.DataAnalysis_Neurons_pushButton22_frame = QFrame(self.page_103_2_2)
        self.DataAnalysis_Neurons_pushButton22_frame.setObjectName(u"DataAnalysis_Neurons_pushButton22_frame")
        sizePolicy3.setHeightForWidth(self.DataAnalysis_Neurons_pushButton22_frame.sizePolicy().hasHeightForWidth())
        self.DataAnalysis_Neurons_pushButton22_frame.setSizePolicy(sizePolicy3)
        self.DataAnalysis_Neurons_pushButton22_frame.setMinimumSize(QSize(0, 25))
        self.DataAnalysis_Neurons_pushButton22_frame.setFrameShape(QFrame.StyledPanel)
        self.DataAnalysis_Neurons_pushButton22_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_108 = QHBoxLayout(self.DataAnalysis_Neurons_pushButton22_frame)
        self.horizontalLayout_108.setSpacing(5)
        self.horizontalLayout_108.setObjectName(u"horizontalLayout_108")
        self.horizontalLayout_108.setContentsMargins(5, 0, 5, 0)
        self.DataAnalysis_Neuron0Vm_pushButton22 = QPushButton(self.DataAnalysis_Neurons_pushButton22_frame)
        self.DataAnalysis_Neuron0Vm_pushButton22.setObjectName(u"DataAnalysis_Neuron0Vm_pushButton22")
        self.DataAnalysis_Neuron0Vm_pushButton22.setMinimumSize(QSize(25, 0))
        self.DataAnalysis_Neuron0Vm_pushButton22.setMaximumSize(QSize(16777215, 25))
        self.DataAnalysis_Neuron0Vm_pushButton22.setFont(font1)
        self.DataAnalysis_Neuron0Vm_pushButton22.setStyleSheet(u"color: rgb(220, 50, 47);")

        self.horizontalLayout_108.addWidget(self.DataAnalysis_Neuron0Vm_pushButton22)

        self.DataAnalysis_Neuron1Vm_pushButton22 = QPushButton(self.DataAnalysis_Neurons_pushButton22_frame)
        self.DataAnalysis_Neuron1Vm_pushButton22.setObjectName(u"DataAnalysis_Neuron1Vm_pushButton22")
        self.DataAnalysis_Neuron1Vm_pushButton22.setMinimumSize(QSize(0, 25))
        self.DataAnalysis_Neuron1Vm_pushButton22.setMaximumSize(QSize(16777215, 25))
        self.DataAnalysis_Neuron1Vm_pushButton22.setFont(font1)
        self.DataAnalysis_Neuron1Vm_pushButton22.setStyleSheet(u"color: rgb(203, 75, 22);")

        self.horizontalLayout_108.addWidget(self.DataAnalysis_Neuron1Vm_pushButton22)

        self.DataAnalysis_Neuron2Vm_pushButton22 = QPushButton(self.DataAnalysis_Neurons_pushButton22_frame)
        self.DataAnalysis_Neuron2Vm_pushButton22.setObjectName(u"DataAnalysis_Neuron2Vm_pushButton22")
        sizePolicy7.setHeightForWidth(self.DataAnalysis_Neuron2Vm_pushButton22.sizePolicy().hasHeightForWidth())
        self.DataAnalysis_Neuron2Vm_pushButton22.setSizePolicy(sizePolicy7)
        self.DataAnalysis_Neuron2Vm_pushButton22.setMinimumSize(QSize(0, 25))
        self.DataAnalysis_Neuron2Vm_pushButton22.setMaximumSize(QSize(16777215, 25))
        self.DataAnalysis_Neuron2Vm_pushButton22.setFont(font1)
        self.DataAnalysis_Neuron2Vm_pushButton22.setStyleSheet(u"color: rgb(181, 137, 0);")

        self.horizontalLayout_108.addWidget(self.DataAnalysis_Neuron2Vm_pushButton22)


        self.verticalLayout_44.addWidget(self.DataAnalysis_Neurons_pushButton22_frame)

        self.DataAnalysis_Display_StackedWidget.addWidget(self.page_103_2_2)
        self.page_103_3_0 = QWidget()
        self.page_103_3_0.setObjectName(u"page_103_3_0")
        self.verticalLayout_45 = QVBoxLayout(self.page_103_3_0)
        self.verticalLayout_45.setSpacing(0)
        self.verticalLayout_45.setObjectName(u"verticalLayout_45")
        self.verticalLayout_45.setContentsMargins(0, 0, 0, 0)
        self.DataAnalysis_Oscilloscope_widget3_0_0 = PlotWidget(self.page_103_3_0)
        self.DataAnalysis_Oscilloscope_widget3_0_0.setObjectName(u"DataAnalysis_Oscilloscope_widget3_0_0")
        sizePolicy2.setHeightForWidth(self.DataAnalysis_Oscilloscope_widget3_0_0.sizePolicy().hasHeightForWidth())
        self.DataAnalysis_Oscilloscope_widget3_0_0.setSizePolicy(sizePolicy2)
        self.DataAnalysis_Oscilloscope_widget3_0_0.setStyleSheet(u"background-color: rgb(0, 30, 38);")

        self.verticalLayout_45.addWidget(self.DataAnalysis_Oscilloscope_widget3_0_0)

        self.line_20 = QFrame(self.page_103_3_0)
        self.line_20.setObjectName(u"line_20")
        self.line_20.setFrameShape(QFrame.HLine)
        self.line_20.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_45.addWidget(self.line_20)

        self.DataAnalysis_Oscilloscope_widget3_0_1 = PlotWidget(self.page_103_3_0)
        self.DataAnalysis_Oscilloscope_widget3_0_1.setObjectName(u"DataAnalysis_Oscilloscope_widget3_0_1")
        sizePolicy3.setHeightForWidth(self.DataAnalysis_Oscilloscope_widget3_0_1.sizePolicy().hasHeightForWidth())
        self.DataAnalysis_Oscilloscope_widget3_0_1.setSizePolicy(sizePolicy3)
        self.DataAnalysis_Oscilloscope_widget3_0_1.setStyleSheet(u"background-color: rgb(0, 30, 38);")

        self.verticalLayout_45.addWidget(self.DataAnalysis_Oscilloscope_widget3_0_1)

        self.line_22 = QFrame(self.page_103_3_0)
        self.line_22.setObjectName(u"line_22")
        self.line_22.setFrameShape(QFrame.HLine)
        self.line_22.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_45.addWidget(self.line_22)

        self.DataAnalysis_Oscilloscope_widget3_0_2 = PlotWidget(self.page_103_3_0)
        self.DataAnalysis_Oscilloscope_widget3_0_2.setObjectName(u"DataAnalysis_Oscilloscope_widget3_0_2")
        sizePolicy2.setHeightForWidth(self.DataAnalysis_Oscilloscope_widget3_0_2.sizePolicy().hasHeightForWidth())
        self.DataAnalysis_Oscilloscope_widget3_0_2.setSizePolicy(sizePolicy2)
        self.DataAnalysis_Oscilloscope_widget3_0_2.setStyleSheet(u"background-color: rgb(0, 30, 38);")

        self.verticalLayout_45.addWidget(self.DataAnalysis_Oscilloscope_widget3_0_2)

        self.line_21 = QFrame(self.page_103_3_0)
        self.line_21.setObjectName(u"line_21")
        self.line_21.setFrameShape(QFrame.HLine)
        self.line_21.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_45.addWidget(self.line_21)

        self.DataAnalysis_Oscilloscope_widget3_0_3 = PlotWidget(self.page_103_3_0)
        self.DataAnalysis_Oscilloscope_widget3_0_3.setObjectName(u"DataAnalysis_Oscilloscope_widget3_0_3")
        sizePolicy2.setHeightForWidth(self.DataAnalysis_Oscilloscope_widget3_0_3.sizePolicy().hasHeightForWidth())
        self.DataAnalysis_Oscilloscope_widget3_0_3.setSizePolicy(sizePolicy2)
        self.DataAnalysis_Oscilloscope_widget3_0_3.setStyleSheet(u"background-color: rgb(0, 30, 38);")

        self.verticalLayout_45.addWidget(self.DataAnalysis_Oscilloscope_widget3_0_3)

        self.line_38 = QFrame(self.page_103_3_0)
        self.line_38.setObjectName(u"line_38")
        self.line_38.setFrameShape(QFrame.HLine)
        self.line_38.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_45.addWidget(self.line_38)

        self.DataAnalysis_Neurons_pushButton30_frame = QFrame(self.page_103_3_0)
        self.DataAnalysis_Neurons_pushButton30_frame.setObjectName(u"DataAnalysis_Neurons_pushButton30_frame")
        sizePolicy3.setHeightForWidth(self.DataAnalysis_Neurons_pushButton30_frame.sizePolicy().hasHeightForWidth())
        self.DataAnalysis_Neurons_pushButton30_frame.setSizePolicy(sizePolicy3)
        self.DataAnalysis_Neurons_pushButton30_frame.setMinimumSize(QSize(0, 25))
        self.DataAnalysis_Neurons_pushButton30_frame.setFrameShape(QFrame.StyledPanel)
        self.DataAnalysis_Neurons_pushButton30_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_109 = QHBoxLayout(self.DataAnalysis_Neurons_pushButton30_frame)
        self.horizontalLayout_109.setSpacing(5)
        self.horizontalLayout_109.setObjectName(u"horizontalLayout_109")
        self.horizontalLayout_109.setContentsMargins(5, 0, 5, 0)
        self.DataAnalysis_Neuron0Vm_pushButton30 = QPushButton(self.DataAnalysis_Neurons_pushButton30_frame)
        self.DataAnalysis_Neuron0Vm_pushButton30.setObjectName(u"DataAnalysis_Neuron0Vm_pushButton30")
        self.DataAnalysis_Neuron0Vm_pushButton30.setMinimumSize(QSize(25, 0))
        self.DataAnalysis_Neuron0Vm_pushButton30.setMaximumSize(QSize(16777215, 25))
        self.DataAnalysis_Neuron0Vm_pushButton30.setFont(font1)
        self.DataAnalysis_Neuron0Vm_pushButton30.setStyleSheet(u"color: rgb(220, 50, 47);")

        self.horizontalLayout_109.addWidget(self.DataAnalysis_Neuron0Vm_pushButton30)

        self.DataAnalysis_Neuron1Vm_pushButton30 = QPushButton(self.DataAnalysis_Neurons_pushButton30_frame)
        self.DataAnalysis_Neuron1Vm_pushButton30.setObjectName(u"DataAnalysis_Neuron1Vm_pushButton30")
        self.DataAnalysis_Neuron1Vm_pushButton30.setMinimumSize(QSize(0, 25))
        self.DataAnalysis_Neuron1Vm_pushButton30.setMaximumSize(QSize(16777215, 25))
        self.DataAnalysis_Neuron1Vm_pushButton30.setFont(font1)
        self.DataAnalysis_Neuron1Vm_pushButton30.setStyleSheet(u"color: rgb(203, 75, 22);")

        self.horizontalLayout_109.addWidget(self.DataAnalysis_Neuron1Vm_pushButton30)

        self.DataAnalysis_Neuron2Vm_pushButton30 = QPushButton(self.DataAnalysis_Neurons_pushButton30_frame)
        self.DataAnalysis_Neuron2Vm_pushButton30.setObjectName(u"DataAnalysis_Neuron2Vm_pushButton30")
        sizePolicy7.setHeightForWidth(self.DataAnalysis_Neuron2Vm_pushButton30.sizePolicy().hasHeightForWidth())
        self.DataAnalysis_Neuron2Vm_pushButton30.setSizePolicy(sizePolicy7)
        self.DataAnalysis_Neuron2Vm_pushButton30.setMinimumSize(QSize(0, 25))
        self.DataAnalysis_Neuron2Vm_pushButton30.setMaximumSize(QSize(16777215, 25))
        self.DataAnalysis_Neuron2Vm_pushButton30.setFont(font1)
        self.DataAnalysis_Neuron2Vm_pushButton30.setStyleSheet(u"color: rgb(181, 137, 0);")

        self.horizontalLayout_109.addWidget(self.DataAnalysis_Neuron2Vm_pushButton30)


        self.verticalLayout_45.addWidget(self.DataAnalysis_Neurons_pushButton30_frame)

        self.DataAnalysis_Display_StackedWidget.addWidget(self.page_103_3_0)
        self.page_103_3_1 = QWidget()
        self.page_103_3_1.setObjectName(u"page_103_3_1")
        self.verticalLayout_46 = QVBoxLayout(self.page_103_3_1)
        self.verticalLayout_46.setSpacing(0)
        self.verticalLayout_46.setObjectName(u"verticalLayout_46")
        self.verticalLayout_46.setContentsMargins(0, 0, 0, 0)
        self.DataAnalysis_Oscilloscope_widget3_1_0 = PlotWidget(self.page_103_3_1)
        self.DataAnalysis_Oscilloscope_widget3_1_0.setObjectName(u"DataAnalysis_Oscilloscope_widget3_1_0")
        sizePolicy2.setHeightForWidth(self.DataAnalysis_Oscilloscope_widget3_1_0.sizePolicy().hasHeightForWidth())
        self.DataAnalysis_Oscilloscope_widget3_1_0.setSizePolicy(sizePolicy2)
        self.DataAnalysis_Oscilloscope_widget3_1_0.setStyleSheet(u"background-color: rgb(0, 30, 38);")

        self.verticalLayout_46.addWidget(self.DataAnalysis_Oscilloscope_widget3_1_0)

        self.line_23 = QFrame(self.page_103_3_1)
        self.line_23.setObjectName(u"line_23")
        self.line_23.setFrameShape(QFrame.HLine)
        self.line_23.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_46.addWidget(self.line_23)

        self.DataAnalysis_Oscilloscope_widget3_1_1 = PlotWidget(self.page_103_3_1)
        self.DataAnalysis_Oscilloscope_widget3_1_1.setObjectName(u"DataAnalysis_Oscilloscope_widget3_1_1")
        sizePolicy2.setHeightForWidth(self.DataAnalysis_Oscilloscope_widget3_1_1.sizePolicy().hasHeightForWidth())
        self.DataAnalysis_Oscilloscope_widget3_1_1.setSizePolicy(sizePolicy2)
        self.DataAnalysis_Oscilloscope_widget3_1_1.setStyleSheet(u"background-color: rgb(0, 30, 38);")

        self.verticalLayout_46.addWidget(self.DataAnalysis_Oscilloscope_widget3_1_1)

        self.line_25 = QFrame(self.page_103_3_1)
        self.line_25.setObjectName(u"line_25")
        self.line_25.setFrameShape(QFrame.HLine)
        self.line_25.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_46.addWidget(self.line_25)

        self.DataAnalysis_Oscilloscope_widget3_1_2 = PlotWidget(self.page_103_3_1)
        self.DataAnalysis_Oscilloscope_widget3_1_2.setObjectName(u"DataAnalysis_Oscilloscope_widget3_1_2")
        sizePolicy2.setHeightForWidth(self.DataAnalysis_Oscilloscope_widget3_1_2.sizePolicy().hasHeightForWidth())
        self.DataAnalysis_Oscilloscope_widget3_1_2.setSizePolicy(sizePolicy2)
        self.DataAnalysis_Oscilloscope_widget3_1_2.setStyleSheet(u"background-color: rgb(0, 30, 38);")

        self.verticalLayout_46.addWidget(self.DataAnalysis_Oscilloscope_widget3_1_2)

        self.line_24 = QFrame(self.page_103_3_1)
        self.line_24.setObjectName(u"line_24")
        self.line_24.setFrameShape(QFrame.HLine)
        self.line_24.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_46.addWidget(self.line_24)

        self.DataAnalysis_Oscilloscope_widget3_1_3 = PlotWidget(self.page_103_3_1)
        self.DataAnalysis_Oscilloscope_widget3_1_3.setObjectName(u"DataAnalysis_Oscilloscope_widget3_1_3")
        sizePolicy2.setHeightForWidth(self.DataAnalysis_Oscilloscope_widget3_1_3.sizePolicy().hasHeightForWidth())
        self.DataAnalysis_Oscilloscope_widget3_1_3.setSizePolicy(sizePolicy2)
        self.DataAnalysis_Oscilloscope_widget3_1_3.setStyleSheet(u"background-color: rgb(0, 30, 38);")

        self.verticalLayout_46.addWidget(self.DataAnalysis_Oscilloscope_widget3_1_3)

        self.line_39 = QFrame(self.page_103_3_1)
        self.line_39.setObjectName(u"line_39")
        self.line_39.setFrameShape(QFrame.HLine)
        self.line_39.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_46.addWidget(self.line_39)

        self.DataAnalysis_Neurons_pushButton31_frame = QFrame(self.page_103_3_1)
        self.DataAnalysis_Neurons_pushButton31_frame.setObjectName(u"DataAnalysis_Neurons_pushButton31_frame")
        sizePolicy3.setHeightForWidth(self.DataAnalysis_Neurons_pushButton31_frame.sizePolicy().hasHeightForWidth())
        self.DataAnalysis_Neurons_pushButton31_frame.setSizePolicy(sizePolicy3)
        self.DataAnalysis_Neurons_pushButton31_frame.setMinimumSize(QSize(0, 25))
        self.DataAnalysis_Neurons_pushButton31_frame.setFrameShape(QFrame.StyledPanel)
        self.DataAnalysis_Neurons_pushButton31_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_110 = QHBoxLayout(self.DataAnalysis_Neurons_pushButton31_frame)
        self.horizontalLayout_110.setSpacing(5)
        self.horizontalLayout_110.setObjectName(u"horizontalLayout_110")
        self.horizontalLayout_110.setContentsMargins(5, 0, 5, 0)
        self.DataAnalysis_Neuron0Vm_pushButton31 = QPushButton(self.DataAnalysis_Neurons_pushButton31_frame)
        self.DataAnalysis_Neuron0Vm_pushButton31.setObjectName(u"DataAnalysis_Neuron0Vm_pushButton31")
        self.DataAnalysis_Neuron0Vm_pushButton31.setMinimumSize(QSize(25, 0))
        self.DataAnalysis_Neuron0Vm_pushButton31.setMaximumSize(QSize(16777215, 25))
        self.DataAnalysis_Neuron0Vm_pushButton31.setFont(font1)
        self.DataAnalysis_Neuron0Vm_pushButton31.setStyleSheet(u"color: rgb(220, 50, 47);")

        self.horizontalLayout_110.addWidget(self.DataAnalysis_Neuron0Vm_pushButton31)

        self.DataAnalysis_Neuron1Vm_pushButton31 = QPushButton(self.DataAnalysis_Neurons_pushButton31_frame)
        self.DataAnalysis_Neuron1Vm_pushButton31.setObjectName(u"DataAnalysis_Neuron1Vm_pushButton31")
        self.DataAnalysis_Neuron1Vm_pushButton31.setMinimumSize(QSize(0, 25))
        self.DataAnalysis_Neuron1Vm_pushButton31.setMaximumSize(QSize(16777215, 25))
        self.DataAnalysis_Neuron1Vm_pushButton31.setFont(font1)
        self.DataAnalysis_Neuron1Vm_pushButton31.setStyleSheet(u"color: rgb(203, 75, 22);")

        self.horizontalLayout_110.addWidget(self.DataAnalysis_Neuron1Vm_pushButton31)

        self.DataAnalysis_Neuron2Vm_pushButton31 = QPushButton(self.DataAnalysis_Neurons_pushButton31_frame)
        self.DataAnalysis_Neuron2Vm_pushButton31.setObjectName(u"DataAnalysis_Neuron2Vm_pushButton31")
        sizePolicy7.setHeightForWidth(self.DataAnalysis_Neuron2Vm_pushButton31.sizePolicy().hasHeightForWidth())
        self.DataAnalysis_Neuron2Vm_pushButton31.setSizePolicy(sizePolicy7)
        self.DataAnalysis_Neuron2Vm_pushButton31.setMinimumSize(QSize(0, 25))
        self.DataAnalysis_Neuron2Vm_pushButton31.setMaximumSize(QSize(16777215, 25))
        self.DataAnalysis_Neuron2Vm_pushButton31.setFont(font1)
        self.DataAnalysis_Neuron2Vm_pushButton31.setStyleSheet(u"color: rgb(181, 137, 0);")

        self.horizontalLayout_110.addWidget(self.DataAnalysis_Neuron2Vm_pushButton31)


        self.verticalLayout_46.addWidget(self.DataAnalysis_Neurons_pushButton31_frame)

        self.DataAnalysis_Display_StackedWidget.addWidget(self.page_103_3_1)
        self.page_103_3_2 = QWidget()
        self.page_103_3_2.setObjectName(u"page_103_3_2")
        self.verticalLayout_47 = QVBoxLayout(self.page_103_3_2)
        self.verticalLayout_47.setSpacing(0)
        self.verticalLayout_47.setObjectName(u"verticalLayout_47")
        self.verticalLayout_47.setContentsMargins(0, 0, 0, 0)
        self.DataAnalysis_Oscilloscope_widget3_2_0 = PlotWidget(self.page_103_3_2)
        self.DataAnalysis_Oscilloscope_widget3_2_0.setObjectName(u"DataAnalysis_Oscilloscope_widget3_2_0")
        sizePolicy2.setHeightForWidth(self.DataAnalysis_Oscilloscope_widget3_2_0.sizePolicy().hasHeightForWidth())
        self.DataAnalysis_Oscilloscope_widget3_2_0.setSizePolicy(sizePolicy2)
        self.DataAnalysis_Oscilloscope_widget3_2_0.setStyleSheet(u"background-color: rgb(0, 30, 38);")

        self.verticalLayout_47.addWidget(self.DataAnalysis_Oscilloscope_widget3_2_0)

        self.line_26 = QFrame(self.page_103_3_2)
        self.line_26.setObjectName(u"line_26")
        self.line_26.setFrameShape(QFrame.HLine)
        self.line_26.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_47.addWidget(self.line_26)

        self.DataAnalysis_Oscilloscope_widget3_2_1 = PlotWidget(self.page_103_3_2)
        self.DataAnalysis_Oscilloscope_widget3_2_1.setObjectName(u"DataAnalysis_Oscilloscope_widget3_2_1")
        sizePolicy2.setHeightForWidth(self.DataAnalysis_Oscilloscope_widget3_2_1.sizePolicy().hasHeightForWidth())
        self.DataAnalysis_Oscilloscope_widget3_2_1.setSizePolicy(sizePolicy2)
        self.DataAnalysis_Oscilloscope_widget3_2_1.setStyleSheet(u"background-color: rgb(0, 30, 38);")

        self.verticalLayout_47.addWidget(self.DataAnalysis_Oscilloscope_widget3_2_1)

        self.line_28 = QFrame(self.page_103_3_2)
        self.line_28.setObjectName(u"line_28")
        self.line_28.setFrameShape(QFrame.HLine)
        self.line_28.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_47.addWidget(self.line_28)

        self.DataAnalysis_Oscilloscope_widget3_2_2 = PlotWidget(self.page_103_3_2)
        self.DataAnalysis_Oscilloscope_widget3_2_2.setObjectName(u"DataAnalysis_Oscilloscope_widget3_2_2")
        sizePolicy2.setHeightForWidth(self.DataAnalysis_Oscilloscope_widget3_2_2.sizePolicy().hasHeightForWidth())
        self.DataAnalysis_Oscilloscope_widget3_2_2.setSizePolicy(sizePolicy2)
        self.DataAnalysis_Oscilloscope_widget3_2_2.setStyleSheet(u"background-color: rgb(0, 30, 38);")

        self.verticalLayout_47.addWidget(self.DataAnalysis_Oscilloscope_widget3_2_2)

        self.line_27 = QFrame(self.page_103_3_2)
        self.line_27.setObjectName(u"line_27")
        self.line_27.setFrameShape(QFrame.HLine)
        self.line_27.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_47.addWidget(self.line_27)

        self.DataAnalysis_Oscilloscope_widget3_2_3 = PlotWidget(self.page_103_3_2)
        self.DataAnalysis_Oscilloscope_widget3_2_3.setObjectName(u"DataAnalysis_Oscilloscope_widget3_2_3")
        sizePolicy2.setHeightForWidth(self.DataAnalysis_Oscilloscope_widget3_2_3.sizePolicy().hasHeightForWidth())
        self.DataAnalysis_Oscilloscope_widget3_2_3.setSizePolicy(sizePolicy2)
        self.DataAnalysis_Oscilloscope_widget3_2_3.setStyleSheet(u"background-color: rgb(0, 30, 38);")

        self.verticalLayout_47.addWidget(self.DataAnalysis_Oscilloscope_widget3_2_3)

        self.line_40 = QFrame(self.page_103_3_2)
        self.line_40.setObjectName(u"line_40")
        self.line_40.setFrameShape(QFrame.HLine)
        self.line_40.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_47.addWidget(self.line_40)

        self.DataAnalysis_Neurons_pushButton32_frame = QFrame(self.page_103_3_2)
        self.DataAnalysis_Neurons_pushButton32_frame.setObjectName(u"DataAnalysis_Neurons_pushButton32_frame")
        sizePolicy3.setHeightForWidth(self.DataAnalysis_Neurons_pushButton32_frame.sizePolicy().hasHeightForWidth())
        self.DataAnalysis_Neurons_pushButton32_frame.setSizePolicy(sizePolicy3)
        self.DataAnalysis_Neurons_pushButton32_frame.setMinimumSize(QSize(0, 25))
        self.DataAnalysis_Neurons_pushButton32_frame.setFrameShape(QFrame.StyledPanel)
        self.DataAnalysis_Neurons_pushButton32_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_111 = QHBoxLayout(self.DataAnalysis_Neurons_pushButton32_frame)
        self.horizontalLayout_111.setSpacing(5)
        self.horizontalLayout_111.setObjectName(u"horizontalLayout_111")
        self.horizontalLayout_111.setContentsMargins(5, 0, 5, 0)
        self.DataAnalysis_Neuron0Vm_pushButton32 = QPushButton(self.DataAnalysis_Neurons_pushButton32_frame)
        self.DataAnalysis_Neuron0Vm_pushButton32.setObjectName(u"DataAnalysis_Neuron0Vm_pushButton32")
        self.DataAnalysis_Neuron0Vm_pushButton32.setMinimumSize(QSize(25, 0))
        self.DataAnalysis_Neuron0Vm_pushButton32.setMaximumSize(QSize(16777215, 25))
        self.DataAnalysis_Neuron0Vm_pushButton32.setFont(font1)
        self.DataAnalysis_Neuron0Vm_pushButton32.setStyleSheet(u"color: rgb(220, 50, 47);")

        self.horizontalLayout_111.addWidget(self.DataAnalysis_Neuron0Vm_pushButton32)

        self.DataAnalysis_Neuron1Vm_pushButton32 = QPushButton(self.DataAnalysis_Neurons_pushButton32_frame)
        self.DataAnalysis_Neuron1Vm_pushButton32.setObjectName(u"DataAnalysis_Neuron1Vm_pushButton32")
        self.DataAnalysis_Neuron1Vm_pushButton32.setMinimumSize(QSize(0, 25))
        self.DataAnalysis_Neuron1Vm_pushButton32.setMaximumSize(QSize(16777215, 25))
        self.DataAnalysis_Neuron1Vm_pushButton32.setFont(font1)
        self.DataAnalysis_Neuron1Vm_pushButton32.setStyleSheet(u"color: rgb(203, 75, 22);")

        self.horizontalLayout_111.addWidget(self.DataAnalysis_Neuron1Vm_pushButton32)

        self.DataAnalysis_Neuron2Vm_pushButton32 = QPushButton(self.DataAnalysis_Neurons_pushButton32_frame)
        self.DataAnalysis_Neuron2Vm_pushButton32.setObjectName(u"DataAnalysis_Neuron2Vm_pushButton32")
        sizePolicy7.setHeightForWidth(self.DataAnalysis_Neuron2Vm_pushButton32.sizePolicy().hasHeightForWidth())
        self.DataAnalysis_Neuron2Vm_pushButton32.setSizePolicy(sizePolicy7)
        self.DataAnalysis_Neuron2Vm_pushButton32.setMinimumSize(QSize(0, 25))
        self.DataAnalysis_Neuron2Vm_pushButton32.setMaximumSize(QSize(16777215, 25))
        self.DataAnalysis_Neuron2Vm_pushButton32.setFont(font1)
        self.DataAnalysis_Neuron2Vm_pushButton32.setStyleSheet(u"color: rgb(181, 137, 0);")

        self.horizontalLayout_111.addWidget(self.DataAnalysis_Neuron2Vm_pushButton32)


        self.verticalLayout_47.addWidget(self.DataAnalysis_Neurons_pushButton32_frame)

        self.DataAnalysis_Display_StackedWidget.addWidget(self.page_103_3_2)

        self.verticalLayout_35.addWidget(self.DataAnalysis_Display_StackedWidget)


        self.horizontalLayout_61.addWidget(self.DataAnalysis_Display_frame)

        self.DataAnalysis_groupBox = QGroupBox(self.DataAnalysis_frame)
        self.DataAnalysis_groupBox.setObjectName(u"DataAnalysis_groupBox")
        sizePolicy.setHeightForWidth(self.DataAnalysis_groupBox.sizePolicy().hasHeightForWidth())
        self.DataAnalysis_groupBox.setSizePolicy(sizePolicy)
        self.DataAnalysis_groupBox.setMinimumSize(QSize(250, 0))
        self.DataAnalysis_groupBox.setMaximumSize(QSize(250, 16777215))
        self.DataAnalysis_groupBox.setStyleSheet(u"")
        self.verticalLayout_34 = QVBoxLayout(self.DataAnalysis_groupBox)
        self.verticalLayout_34.setSpacing(0)
        self.verticalLayout_34.setObjectName(u"verticalLayout_34")
        self.verticalLayout_34.setContentsMargins(0, 0, 0, 1)
        self.DataAnalysis_LoadData_frame = QFrame(self.DataAnalysis_groupBox)
        self.DataAnalysis_LoadData_frame.setObjectName(u"DataAnalysis_LoadData_frame")
        self.DataAnalysis_LoadData_frame.setFrameShape(QFrame.StyledPanel)
        self.DataAnalysis_LoadData_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_36 = QVBoxLayout(self.DataAnalysis_LoadData_frame)
        self.verticalLayout_36.setObjectName(u"verticalLayout_36")
        self.DataAnalysis_LoadData_subframe = QFrame(self.DataAnalysis_LoadData_frame)
        self.DataAnalysis_LoadData_subframe.setObjectName(u"DataAnalysis_LoadData_subframe")
        self.DataAnalysis_LoadData_subframe.setFrameShape(QFrame.StyledPanel)
        self.DataAnalysis_LoadData_subframe.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_62 = QHBoxLayout(self.DataAnalysis_LoadData_subframe)
        self.horizontalLayout_62.setSpacing(0)
        self.horizontalLayout_62.setObjectName(u"horizontalLayout_62")
        self.horizontalLayout_62.setContentsMargins(0, 0, 0, 0)
        self.DataAnalysis_LoadData_label = QLabel(self.DataAnalysis_LoadData_subframe)
        self.DataAnalysis_LoadData_label.setObjectName(u"DataAnalysis_LoadData_label")
        sizePolicy4.setHeightForWidth(self.DataAnalysis_LoadData_label.sizePolicy().hasHeightForWidth())
        self.DataAnalysis_LoadData_label.setSizePolicy(sizePolicy4)
        self.DataAnalysis_LoadData_label.setWordWrap(True)

        self.horizontalLayout_62.addWidget(self.DataAnalysis_LoadData_label)

        self.DataAnalysis_LoadData_pushButton = QPushButton(self.DataAnalysis_LoadData_subframe)
        self.DataAnalysis_LoadData_pushButton.setObjectName(u"DataAnalysis_LoadData_pushButton")

        self.horizontalLayout_62.addWidget(self.DataAnalysis_LoadData_pushButton)


        self.verticalLayout_36.addWidget(self.DataAnalysis_LoadData_subframe)

        self.DataAnalysis_LoadData_Display_pushButton = QPushButton(self.DataAnalysis_LoadData_frame)
        self.DataAnalysis_LoadData_Display_pushButton.setObjectName(u"DataAnalysis_LoadData_Display_pushButton")

        self.verticalLayout_36.addWidget(self.DataAnalysis_LoadData_Display_pushButton)

        self.DataAnalysis_SaveImage_pushButton = QPushButton(self.DataAnalysis_LoadData_frame)
        self.DataAnalysis_SaveImage_pushButton.setObjectName(u"DataAnalysis_SaveImage_pushButton")

        self.verticalLayout_36.addWidget(self.DataAnalysis_SaveImage_pushButton)


        self.verticalLayout_34.addWidget(self.DataAnalysis_LoadData_frame)

        self.DataAnalysis_LoadData_line = QFrame(self.DataAnalysis_groupBox)
        self.DataAnalysis_LoadData_line.setObjectName(u"DataAnalysis_LoadData_line")
        self.DataAnalysis_LoadData_line.setFrameShape(QFrame.HLine)
        self.DataAnalysis_LoadData_line.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_34.addWidget(self.DataAnalysis_LoadData_line)

        self.DataAnalysis_Spike_frame = QFrame(self.DataAnalysis_groupBox)
        self.DataAnalysis_Spike_frame.setObjectName(u"DataAnalysis_Spike_frame")
        self.DataAnalysis_Spike_frame.setStyleSheet(u"background-color: rgb(47,60,63);\n"
"")
        self.DataAnalysis_Spike_frame.setFrameShape(QFrame.StyledPanel)
        self.DataAnalysis_Spike_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_41 = QVBoxLayout(self.DataAnalysis_Spike_frame)
        self.verticalLayout_41.setObjectName(u"verticalLayout_41")
        self.DataAnalysis_Spike_label = QLabel(self.DataAnalysis_Spike_frame)
        self.DataAnalysis_Spike_label.setObjectName(u"DataAnalysis_Spike_label")

        self.verticalLayout_41.addWidget(self.DataAnalysis_Spike_label, 0, Qt.AlignHCenter)

        self.DataAnalysis_Spike_subframe = QFrame(self.DataAnalysis_Spike_frame)
        self.DataAnalysis_Spike_subframe.setObjectName(u"DataAnalysis_Spike_subframe")
        self.DataAnalysis_Spike_subframe.setFrameShape(QFrame.StyledPanel)
        self.DataAnalysis_Spike_subframe.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_69 = QHBoxLayout(self.DataAnalysis_Spike_subframe)
        self.horizontalLayout_69.setSpacing(5)
        self.horizontalLayout_69.setObjectName(u"horizontalLayout_69")
        self.horizontalLayout_69.setContentsMargins(0, 0, 0, 0)
        self.DataAnalysis_Spike_threshold_label = QLabel(self.DataAnalysis_Spike_subframe)
        self.DataAnalysis_Spike_threshold_label.setObjectName(u"DataAnalysis_Spike_threshold_label")
        sizePolicy4.setHeightForWidth(self.DataAnalysis_Spike_threshold_label.sizePolicy().hasHeightForWidth())
        self.DataAnalysis_Spike_threshold_label.setSizePolicy(sizePolicy4)

        self.horizontalLayout_69.addWidget(self.DataAnalysis_Spike_threshold_label)

        self.DataAnalysis_Spike_lineEdit = QLineEdit(self.DataAnalysis_Spike_subframe)
        self.DataAnalysis_Spike_lineEdit.setObjectName(u"DataAnalysis_Spike_lineEdit")
        self.DataAnalysis_Spike_lineEdit.setEnabled(False)
        sizePolicy6.setHeightForWidth(self.DataAnalysis_Spike_lineEdit.sizePolicy().hasHeightForWidth())
        self.DataAnalysis_Spike_lineEdit.setSizePolicy(sizePolicy6)
        self.DataAnalysis_Spike_lineEdit.setMinimumSize(QSize(50, 0))
        self.DataAnalysis_Spike_lineEdit.setMaximumSize(QSize(50, 16777215))
        self.DataAnalysis_Spike_lineEdit.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_69.addWidget(self.DataAnalysis_Spike_lineEdit, 0, Qt.AlignRight)

        self.DataAnalysis_Spike_mV_label = QLabel(self.DataAnalysis_Spike_subframe)
        self.DataAnalysis_Spike_mV_label.setObjectName(u"DataAnalysis_Spike_mV_label")

        self.horizontalLayout_69.addWidget(self.DataAnalysis_Spike_mV_label, 0, Qt.AlignRight)


        self.verticalLayout_41.addWidget(self.DataAnalysis_Spike_subframe)

        self.DataAnalysis_Spike_result_label = QLabel(self.DataAnalysis_Spike_frame)
        self.DataAnalysis_Spike_result_label.setObjectName(u"DataAnalysis_Spike_result_label")
        self.DataAnalysis_Spike_result_label.setFont(font3)
        self.DataAnalysis_Spike_result_label.setStyleSheet(u"")
        self.DataAnalysis_Spike_result_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_41.addWidget(self.DataAnalysis_Spike_result_label)

        self.DataAnalysis_Spike_Display_pushButton = QPushButton(self.DataAnalysis_Spike_frame)
        self.DataAnalysis_Spike_Display_pushButton.setObjectName(u"DataAnalysis_Spike_Display_pushButton")
        self.DataAnalysis_Spike_Display_pushButton.setEnabled(False)

        self.verticalLayout_41.addWidget(self.DataAnalysis_Spike_Display_pushButton)

        self.DataAnalysis_Spike_SaveImage_pushButton = QPushButton(self.DataAnalysis_Spike_frame)
        self.DataAnalysis_Spike_SaveImage_pushButton.setObjectName(u"DataAnalysis_Spike_SaveImage_pushButton")

        self.verticalLayout_41.addWidget(self.DataAnalysis_Spike_SaveImage_pushButton)

        self.DataAnalysis_Spike_Export_pushButton = QPushButton(self.DataAnalysis_Spike_frame)
        self.DataAnalysis_Spike_Export_pushButton.setObjectName(u"DataAnalysis_Spike_Export_pushButton")

        self.verticalLayout_41.addWidget(self.DataAnalysis_Spike_Export_pushButton)


        self.verticalLayout_34.addWidget(self.DataAnalysis_Spike_frame)

        self.DataAnalysis_Average_frame = QFrame(self.DataAnalysis_groupBox)
        self.DataAnalysis_Average_frame.setObjectName(u"DataAnalysis_Average_frame")
        self.DataAnalysis_Average_frame.setStyleSheet(u"background-color: rgb(47,60,63);\n"
"")
        self.DataAnalysis_Average_frame.setFrameShape(QFrame.StyledPanel)
        self.DataAnalysis_Average_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_40 = QVBoxLayout(self.DataAnalysis_Average_frame)
        self.verticalLayout_40.setSpacing(5)
        self.verticalLayout_40.setObjectName(u"verticalLayout_40")
        self.verticalLayout_40.setContentsMargins(0, 0, 0, 5)
        self.DataAnalysis_Spike_line = QFrame(self.DataAnalysis_Average_frame)
        self.DataAnalysis_Spike_line.setObjectName(u"DataAnalysis_Spike_line")
        self.DataAnalysis_Spike_line.setFrameShape(QFrame.HLine)
        self.DataAnalysis_Spike_line.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_40.addWidget(self.DataAnalysis_Spike_line)

        self.DataAnalysis_Average_result_label = QLabel(self.DataAnalysis_Average_frame)
        self.DataAnalysis_Average_result_label.setObjectName(u"DataAnalysis_Average_result_label")

        self.verticalLayout_40.addWidget(self.DataAnalysis_Average_result_label, 0, Qt.AlignHCenter)

        self.DataAnalysis_Average_label = QLabel(self.DataAnalysis_Average_frame)
        self.DataAnalysis_Average_label.setObjectName(u"DataAnalysis_Average_label")
        self.DataAnalysis_Average_label.setFont(font3)
        self.DataAnalysis_Average_label.setStyleSheet(u"")
        self.DataAnalysis_Average_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_40.addWidget(self.DataAnalysis_Average_label)

        self.DataAnalysis_Average_Display_pushButton = QPushButton(self.DataAnalysis_Average_frame)
        self.DataAnalysis_Average_Display_pushButton.setObjectName(u"DataAnalysis_Average_Display_pushButton")
        self.DataAnalysis_Average_Display_pushButton.setEnabled(False)

        self.verticalLayout_40.addWidget(self.DataAnalysis_Average_Display_pushButton)

        self.DataAnalysis_Average_SaveImage_pushButton = QPushButton(self.DataAnalysis_Average_frame)
        self.DataAnalysis_Average_SaveImage_pushButton.setObjectName(u"DataAnalysis_Average_SaveImage_pushButton")

        self.verticalLayout_40.addWidget(self.DataAnalysis_Average_SaveImage_pushButton)

        self.DataAnalysis_Average_Save_pushButton = QPushButton(self.DataAnalysis_Average_frame)
        self.DataAnalysis_Average_Save_pushButton.setObjectName(u"DataAnalysis_Average_Save_pushButton")
        self.DataAnalysis_Average_Save_pushButton.setEnabled(False)

        self.verticalLayout_40.addWidget(self.DataAnalysis_Average_Save_pushButton)


        self.verticalLayout_34.addWidget(self.DataAnalysis_Average_frame)


        self.horizontalLayout_61.addWidget(self.DataAnalysis_groupBox)


        self.horizontalLayout_68.addWidget(self.DataAnalysis_frame)

        self.mainbody_stackedWidget.addWidget(self.page_103)
        self.page_201 = QWidget()
        self.page_201.setObjectName(u"page_201")
        self.horizontalLayout_70 = QHBoxLayout(self.page_201)
        self.horizontalLayout_70.setSpacing(0)
        self.horizontalLayout_70.setObjectName(u"horizontalLayout_70")
        self.horizontalLayout_70.setContentsMargins(0, 0, 0, 0)
        self.frame_44 = QFrame(self.page_201)
        self.frame_44.setObjectName(u"frame_44")
        self.frame_44.setFrameShape(QFrame.StyledPanel)
        self.frame_44.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_71 = QHBoxLayout(self.frame_44)
        self.horizontalLayout_71.setSpacing(0)
        self.horizontalLayout_71.setObjectName(u"horizontalLayout_71")
        self.horizontalLayout_71.setContentsMargins(0, 0, 0, 0)
        self.label_4 = QLabel(self.frame_44)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setPixmap(QPixmap(u":/resources/resources/under_construction.svg"))
        self.label_4.setScaledContents(True)

        self.horizontalLayout_71.addWidget(self.label_4)


        self.horizontalLayout_70.addWidget(self.frame_44)

        self.mainbody_stackedWidget.addWidget(self.page_201)
        self.page_202 = QWidget()
        self.page_202.setObjectName(u"page_202")
        self.horizontalLayout_72 = QHBoxLayout(self.page_202)
        self.horizontalLayout_72.setSpacing(0)
        self.horizontalLayout_72.setObjectName(u"horizontalLayout_72")
        self.horizontalLayout_72.setContentsMargins(0, 0, 0, 0)
        self.frame_45 = QFrame(self.page_202)
        self.frame_45.setObjectName(u"frame_45")
        self.frame_45.setFrameShape(QFrame.StyledPanel)
        self.frame_45.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_73 = QHBoxLayout(self.frame_45)
        self.horizontalLayout_73.setObjectName(u"horizontalLayout_73")
        self.label_5 = QLabel(self.frame_45)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setPixmap(QPixmap(u":/resources/resources/under_construction.svg"))
        self.label_5.setScaledContents(True)

        self.horizontalLayout_73.addWidget(self.label_5)


        self.horizontalLayout_72.addWidget(self.frame_45)

        self.mainbody_stackedWidget.addWidget(self.page_202)
        self.page_203 = QWidget()
        self.page_203.setObjectName(u"page_203")
        self.horizontalLayout_75 = QHBoxLayout(self.page_203)
        self.horizontalLayout_75.setSpacing(0)
        self.horizontalLayout_75.setObjectName(u"horizontalLayout_75")
        self.horizontalLayout_75.setContentsMargins(0, 0, 0, 0)
        self.frame_46 = QFrame(self.page_203)
        self.frame_46.setObjectName(u"frame_46")
        self.frame_46.setFrameShape(QFrame.StyledPanel)
        self.frame_46.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_74 = QHBoxLayout(self.frame_46)
        self.horizontalLayout_74.setObjectName(u"horizontalLayout_74")
        self.label_7 = QLabel(self.frame_46)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setPixmap(QPixmap(u":/resources/resources/under_construction.svg"))
        self.label_7.setScaledContents(True)

        self.horizontalLayout_74.addWidget(self.label_7)


        self.horizontalLayout_75.addWidget(self.frame_46)

        self.mainbody_stackedWidget.addWidget(self.page_203)
        self.page_301 = QWidget()
        self.page_301.setObjectName(u"page_301")
        self.page_301.setStyleSheet(u"")
        self.horizontalLayout_9 = QHBoxLayout(self.page_301)
        self.horizontalLayout_9.setSpacing(5)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(20, 9, 9, 9)
        self.NeuronGenerator_widget = QWidget(self.page_301)
        self.NeuronGenerator_widget.setObjectName(u"NeuronGenerator_widget")
        self.NeuronGenerator_widget.setStyleSheet(u"")
        self.horizontalLayout_10 = QHBoxLayout(self.NeuronGenerator_widget)
        self.horizontalLayout_10.setSpacing(15)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.NeuronGenerator_subwidget1 = QWidget(self.NeuronGenerator_widget)
        self.NeuronGenerator_subwidget1.setObjectName(u"NeuronGenerator_subwidget1")
        self.verticalLayout_12 = QVBoxLayout(self.NeuronGenerator_subwidget1)
        self.verticalLayout_12.setSpacing(5)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.NeuronGenerator_subframe1_top_frame = QFrame(self.NeuronGenerator_subwidget1)
        self.NeuronGenerator_subframe1_top_frame.setObjectName(u"NeuronGenerator_subframe1_top_frame")
        self.NeuronGenerator_subframe1_top_frame.setFrameShape(QFrame.StyledPanel)
        self.NeuronGenerator_subframe1_top_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.NeuronGenerator_subframe1_top_frame)
        self.verticalLayout_13.setSpacing(0)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.NeuronGenerator_subframe1_title_frame = QFrame(self.NeuronGenerator_subframe1_top_frame)
        self.NeuronGenerator_subframe1_title_frame.setObjectName(u"NeuronGenerator_subframe1_title_frame")
        self.NeuronGenerator_subframe1_title_frame.setFrameShape(QFrame.StyledPanel)
        self.NeuronGenerator_subframe1_title_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_14 = QHBoxLayout(self.NeuronGenerator_subframe1_title_frame)
        self.horizontalLayout_14.setSpacing(0)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalLayout_14.setContentsMargins(-1, 0, 0, 0)
        self.NeuronGenerator_subframe1_title_label = QLabel(self.NeuronGenerator_subframe1_title_frame)
        self.NeuronGenerator_subframe1_title_label.setObjectName(u"NeuronGenerator_subframe1_title_label")
        sizePolicy1.setHeightForWidth(self.NeuronGenerator_subframe1_title_label.sizePolicy().hasHeightForWidth())
        self.NeuronGenerator_subframe1_title_label.setSizePolicy(sizePolicy1)
        self.NeuronGenerator_subframe1_title_label.setMaximumSize(QSize(16777215, 30))
        self.NeuronGenerator_subframe1_title_label.setStyleSheet(u"")

        self.horizontalLayout_14.addWidget(self.NeuronGenerator_subframe1_title_label, 0, Qt.AlignLeft)


        self.verticalLayout_13.addWidget(self.NeuronGenerator_subframe1_title_frame, 0, Qt.AlignTop)

        self.NeuronGenerator_subframe1_Izhik_frame = QFrame(self.NeuronGenerator_subframe1_top_frame)
        self.NeuronGenerator_subframe1_Izhik_frame.setObjectName(u"NeuronGenerator_subframe1_Izhik_frame")
        sizePolicy1.setHeightForWidth(self.NeuronGenerator_subframe1_Izhik_frame.sizePolicy().hasHeightForWidth())
        self.NeuronGenerator_subframe1_Izhik_frame.setSizePolicy(sizePolicy1)
        self.NeuronGenerator_subframe1_Izhik_frame.setMaximumSize(QSize(16777215, 240))
        self.NeuronGenerator_subframe1_Izhik_frame.setFrameShape(QFrame.StyledPanel)
        self.NeuronGenerator_subframe1_Izhik_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_13 = QHBoxLayout(self.NeuronGenerator_subframe1_Izhik_frame)
        self.horizontalLayout_13.setSpacing(5)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.NeuronGenerator_subframe1_Izhik_subframe1 = QFrame(self.NeuronGenerator_subframe1_Izhik_frame)
        self.NeuronGenerator_subframe1_Izhik_subframe1.setObjectName(u"NeuronGenerator_subframe1_Izhik_subframe1")
        self.NeuronGenerator_subframe1_Izhik_subframe1.setFrameShape(QFrame.StyledPanel)
        self.NeuronGenerator_subframe1_Izhik_subframe1.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_16 = QHBoxLayout(self.NeuronGenerator_subframe1_Izhik_subframe1)
        self.horizontalLayout_16.setSpacing(0)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.horizontalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.NeuronGenerator_subframe1_Izhik_textbrowser = QTextBrowser(self.NeuronGenerator_subframe1_Izhik_subframe1)
        self.NeuronGenerator_subframe1_Izhik_textbrowser.setObjectName(u"NeuronGenerator_subframe1_Izhik_textbrowser")
        sizePolicy8 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy8.setHorizontalStretch(0)
        sizePolicy8.setVerticalStretch(0)
        sizePolicy8.setHeightForWidth(self.NeuronGenerator_subframe1_Izhik_textbrowser.sizePolicy().hasHeightForWidth())
        self.NeuronGenerator_subframe1_Izhik_textbrowser.setSizePolicy(sizePolicy8)
        self.NeuronGenerator_subframe1_Izhik_textbrowser.setMinimumSize(QSize(0, 240))
        self.NeuronGenerator_subframe1_Izhik_textbrowser.setMaximumSize(QSize(16777215, 200))
        self.NeuronGenerator_subframe1_Izhik_textbrowser.setStyleSheet(u"")

        self.horizontalLayout_16.addWidget(self.NeuronGenerator_subframe1_Izhik_textbrowser, 0, Qt.AlignTop)


        self.horizontalLayout_13.addWidget(self.NeuronGenerator_subframe1_Izhik_subframe1, 0, Qt.AlignTop)

        self.NeuronGenerator_subframe1_Izhik_subframe2 = QFrame(self.NeuronGenerator_subframe1_Izhik_frame)
        self.NeuronGenerator_subframe1_Izhik_subframe2.setObjectName(u"NeuronGenerator_subframe1_Izhik_subframe2")
        self.NeuronGenerator_subframe1_Izhik_subframe2.setFrameShape(QFrame.StyledPanel)
        self.NeuronGenerator_subframe1_Izhik_subframe2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_15 = QHBoxLayout(self.NeuronGenerator_subframe1_Izhik_subframe2)
        self.horizontalLayout_15.setSpacing(0)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalLayout_15.setContentsMargins(0, 0, 0, 0)

        self.horizontalLayout_13.addWidget(self.NeuronGenerator_subframe1_Izhik_subframe2, 0, Qt.AlignRight|Qt.AlignVCenter)


        self.verticalLayout_13.addWidget(self.NeuronGenerator_subframe1_Izhik_frame, 0, Qt.AlignTop)


        self.verticalLayout_12.addWidget(self.NeuronGenerator_subframe1_top_frame, 0, Qt.AlignTop)

        self.NeuronGenerator_subframe1_middle_frame = QFrame(self.NeuronGenerator_subwidget1)
        self.NeuronGenerator_subframe1_middle_frame.setObjectName(u"NeuronGenerator_subframe1_middle_frame")
        self.NeuronGenerator_subframe1_middle_frame.setFrameShape(QFrame.StyledPanel)
        self.NeuronGenerator_subframe1_middle_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.NeuronGenerator_subframe1_middle_frame)
        self.horizontalLayout_12.setSpacing(0)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.NeuronGenerator_subframe1_Oscilloscope_widget = PlotWidget(self.NeuronGenerator_subframe1_middle_frame)
        self.NeuronGenerator_subframe1_Oscilloscope_widget.setObjectName(u"NeuronGenerator_subframe1_Oscilloscope_widget")
        sizePolicy5.setHeightForWidth(self.NeuronGenerator_subframe1_Oscilloscope_widget.sizePolicy().hasHeightForWidth())
        self.NeuronGenerator_subframe1_Oscilloscope_widget.setSizePolicy(sizePolicy5)
        self.NeuronGenerator_subframe1_Oscilloscope_widget.setStyleSheet(u"")
        self.NeuronGenerator_subframe1_Oscilloscope_widget_stimulus_checkbox = QCheckBox(self.NeuronGenerator_subframe1_Oscilloscope_widget)
        self.NeuronGenerator_subframe1_Oscilloscope_widget_stimulus_checkbox.setObjectName(u"NeuronGenerator_subframe1_Oscilloscope_widget_stimulus_checkbox")
        self.NeuronGenerator_subframe1_Oscilloscope_widget_stimulus_checkbox.setEnabled(False)
        self.NeuronGenerator_subframe1_Oscilloscope_widget_stimulus_checkbox.setGeometry(QRect(120, 0, 100, 20))
        self.NeuronGenerator_subframe1_Oscilloscope_widget_stimulus_checkbox.setAutoFillBackground(False)
        self.NeuronGenerator_subframe1_Oscilloscope_widget_stimulus_checkbox.setStyleSheet(u"color: rgb(133, 153, 0);")
        self.NeuronGenerator_subframe1_Oscilloscope_widget_stimulus_checkbox.setChecked(True)
        self.NeuronGenerator_subframe1_Oscilloscope_widget_Vm_checkbox = QCheckBox(self.NeuronGenerator_subframe1_Oscilloscope_widget)
        self.NeuronGenerator_subframe1_Oscilloscope_widget_Vm_checkbox.setObjectName(u"NeuronGenerator_subframe1_Oscilloscope_widget_Vm_checkbox")
        self.NeuronGenerator_subframe1_Oscilloscope_widget_Vm_checkbox.setEnabled(False)
        self.NeuronGenerator_subframe1_Oscilloscope_widget_Vm_checkbox.setGeometry(QRect(70, 0, 100, 20))
        self.NeuronGenerator_subframe1_Oscilloscope_widget_Vm_checkbox.setAutoFillBackground(False)
        self.NeuronGenerator_subframe1_Oscilloscope_widget_Vm_checkbox.setStyleSheet(u"color: rgb(220, 50, 47);")
        self.NeuronGenerator_subframe1_Oscilloscope_widget_Vm_checkbox.setChecked(True)
        self.NeuronGenerator_subframe1_Oscilloscope_widget_Vm_checkbox.raise_()
        self.NeuronGenerator_subframe1_Oscilloscope_widget_stimulus_checkbox.raise_()

        self.horizontalLayout_12.addWidget(self.NeuronGenerator_subframe1_Oscilloscope_widget)


        self.verticalLayout_12.addWidget(self.NeuronGenerator_subframe1_middle_frame)

        self.NeuronGenerator_subframe1_bottom_frame = QFrame(self.NeuronGenerator_subwidget1)
        self.NeuronGenerator_subframe1_bottom_frame.setObjectName(u"NeuronGenerator_subframe1_bottom_frame")
        sizePolicy1.setHeightForWidth(self.NeuronGenerator_subframe1_bottom_frame.sizePolicy().hasHeightForWidth())
        self.NeuronGenerator_subframe1_bottom_frame.setSizePolicy(sizePolicy1)
        self.NeuronGenerator_subframe1_bottom_frame.setMinimumSize(QSize(0, 35))
        self.NeuronGenerator_subframe1_bottom_frame.setMaximumSize(QSize(16777215, 35))
        self.NeuronGenerator_subframe1_bottom_frame.setFrameShape(QFrame.StyledPanel)
        self.NeuronGenerator_subframe1_bottom_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.NeuronGenerator_subframe1_bottom_frame)
        self.horizontalLayout_11.setSpacing(0)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.NeuronGenerator_subframe1_bottom_label = QLabel(self.NeuronGenerator_subframe1_bottom_frame)
        self.NeuronGenerator_subframe1_bottom_label.setObjectName(u"NeuronGenerator_subframe1_bottom_label")
        sizePolicy4.setHeightForWidth(self.NeuronGenerator_subframe1_bottom_label.sizePolicy().hasHeightForWidth())
        self.NeuronGenerator_subframe1_bottom_label.setSizePolicy(sizePolicy4)
        self.NeuronGenerator_subframe1_bottom_label.setWordWrap(True)

        self.horizontalLayout_11.addWidget(self.NeuronGenerator_subframe1_bottom_label, 0, Qt.AlignTop)


        self.verticalLayout_12.addWidget(self.NeuronGenerator_subframe1_bottom_frame, 0, Qt.AlignBottom)


        self.horizontalLayout_10.addWidget(self.NeuronGenerator_subwidget1)

        self.NeuronGenerator_subgroupBox2 = QGroupBox(self.NeuronGenerator_widget)
        self.NeuronGenerator_subgroupBox2.setObjectName(u"NeuronGenerator_subgroupBox2")
        self.NeuronGenerator_subgroupBox2.setEnabled(True)
        sizePolicy.setHeightForWidth(self.NeuronGenerator_subgroupBox2.sizePolicy().hasHeightForWidth())
        self.NeuronGenerator_subgroupBox2.setSizePolicy(sizePolicy)
        self.NeuronGenerator_subgroupBox2.setMinimumSize(QSize(400, 0))
        self.NeuronGenerator_subgroupBox2.setMaximumSize(QSize(400, 16777215))
        self.NeuronGenerator_subgroupBox2.setStyleSheet(u"")
        self.verticalLayout_9 = QVBoxLayout(self.NeuronGenerator_subgroupBox2)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.NeuronGenerator_subframe2 = QFrame(self.NeuronGenerator_subgroupBox2)
        self.NeuronGenerator_subframe2.setObjectName(u"NeuronGenerator_subframe2")
        self.NeuronGenerator_subframe2.setEnabled(True)
        self.NeuronGenerator_subframe2.setFrameShape(QFrame.StyledPanel)
        self.NeuronGenerator_subframe2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_14 = QVBoxLayout(self.NeuronGenerator_subframe2)
        self.verticalLayout_14.setSpacing(0)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.izhik_image = QFrame(self.NeuronGenerator_subframe2)
        self.izhik_image.setObjectName(u"izhik_image")
        sizePolicy1.setHeightForWidth(self.izhik_image.sizePolicy().hasHeightForWidth())
        self.izhik_image.setSizePolicy(sizePolicy1)
        self.izhik_image.setMinimumSize(QSize(0, 150))
        self.izhik_image.setMaximumSize(QSize(16777215, 200))
        self.izhik_image.setFrameShape(QFrame.StyledPanel)
        self.izhik_image.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_17 = QHBoxLayout(self.izhik_image)
        self.horizontalLayout_17.setSpacing(0)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.horizontalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.NeuronGenerator_subframe1_Izhik_image = QLabel(self.izhik_image)
        self.NeuronGenerator_subframe1_Izhik_image.setObjectName(u"NeuronGenerator_subframe1_Izhik_image")
        sizePolicy4.setHeightForWidth(self.NeuronGenerator_subframe1_Izhik_image.sizePolicy().hasHeightForWidth())
        self.NeuronGenerator_subframe1_Izhik_image.setSizePolicy(sizePolicy4)
        self.NeuronGenerator_subframe1_Izhik_image.setMinimumSize(QSize(225, 150))
        self.NeuronGenerator_subframe1_Izhik_image.setMaximumSize(QSize(225, 140))
        self.NeuronGenerator_subframe1_Izhik_image.setPixmap(QPixmap(u":/resources/resources/izhik.png"))
        self.NeuronGenerator_subframe1_Izhik_image.setScaledContents(True)

        self.horizontalLayout_17.addWidget(self.NeuronGenerator_subframe1_Izhik_image, 0, Qt.AlignTop)


        self.verticalLayout_14.addWidget(self.izhik_image)

        self.line = QFrame(self.NeuronGenerator_subframe2)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_14.addWidget(self.line)

        self.a_Izhik_frame = QFrame(self.NeuronGenerator_subframe2)
        self.a_Izhik_frame.setObjectName(u"a_Izhik_frame")
        self.a_Izhik_frame.setFrameShape(QFrame.StyledPanel)
        self.a_Izhik_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_18 = QHBoxLayout(self.a_Izhik_frame)
        self.horizontalLayout_18.setSpacing(15)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.horizontalLayout_18.setContentsMargins(0, 0, 0, 0)
        self.a_value_frame = QFrame(self.a_Izhik_frame)
        self.a_value_frame.setObjectName(u"a_value_frame")
        self.a_value_frame.setFrameShape(QFrame.StyledPanel)
        self.a_value_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_20 = QHBoxLayout(self.a_value_frame)
        self.horizontalLayout_20.setSpacing(0)
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.horizontalLayout_20.setContentsMargins(0, 0, 0, 0)
        self.a_value = QLineEdit(self.a_value_frame)
        self.a_value.setObjectName(u"a_value")
        sizePolicy6.setHeightForWidth(self.a_value.sizePolicy().hasHeightForWidth())
        self.a_value.setSizePolicy(sizePolicy6)
        self.a_value.setMinimumSize(QSize(75, 0))
        self.a_value.setMaximumSize(QSize(50, 16777215))
        self.a_value.setFont(font4)
        self.a_value.setStyleSheet(u"")
        self.a_value.setFrame(True)
        self.a_value.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_20.addWidget(self.a_value)


        self.horizontalLayout_18.addWidget(self.a_value_frame, 0, Qt.AlignLeft)

        self.a_text_frame = QFrame(self.a_Izhik_frame)
        self.a_text_frame.setObjectName(u"a_text_frame")
        self.a_text_frame.setFrameShape(QFrame.StyledPanel)
        self.a_text_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_19 = QHBoxLayout(self.a_text_frame)
        self.horizontalLayout_19.setSpacing(0)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.horizontalLayout_19.setContentsMargins(0, 0, 0, 0)
        self.a_text = QLabel(self.a_text_frame)
        self.a_text.setObjectName(u"a_text")
        sizePolicy4.setHeightForWidth(self.a_text.sizePolicy().hasHeightForWidth())
        self.a_text.setSizePolicy(sizePolicy4)
        self.a_text.setScaledContents(False)
        self.a_text.setAlignment(Qt.AlignBottom|Qt.AlignJustify)
        self.a_text.setWordWrap(True)

        self.horizontalLayout_19.addWidget(self.a_text)


        self.horizontalLayout_18.addWidget(self.a_text_frame)


        self.verticalLayout_14.addWidget(self.a_Izhik_frame)

        self.line_2 = QFrame(self.NeuronGenerator_subframe2)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_14.addWidget(self.line_2)

        self.b_Izhik_frame = QFrame(self.NeuronGenerator_subframe2)
        self.b_Izhik_frame.setObjectName(u"b_Izhik_frame")
        self.b_Izhik_frame.setFrameShape(QFrame.StyledPanel)
        self.b_Izhik_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_21 = QHBoxLayout(self.b_Izhik_frame)
        self.horizontalLayout_21.setSpacing(15)
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.horizontalLayout_21.setContentsMargins(0, 0, 0, 0)
        self.b_value_frame = QFrame(self.b_Izhik_frame)
        self.b_value_frame.setObjectName(u"b_value_frame")
        self.b_value_frame.setFrameShape(QFrame.StyledPanel)
        self.b_value_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_23 = QHBoxLayout(self.b_value_frame)
        self.horizontalLayout_23.setSpacing(0)
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.horizontalLayout_23.setContentsMargins(0, 0, 0, 0)
        self.b_value = QLineEdit(self.b_value_frame)
        self.b_value.setObjectName(u"b_value")
        sizePolicy6.setHeightForWidth(self.b_value.sizePolicy().hasHeightForWidth())
        self.b_value.setSizePolicy(sizePolicy6)
        self.b_value.setMinimumSize(QSize(75, 0))
        self.b_value.setMaximumSize(QSize(75, 16777215))
        self.b_value.setFont(font4)
        self.b_value.setStyleSheet(u"")
        self.b_value.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_23.addWidget(self.b_value)


        self.horizontalLayout_21.addWidget(self.b_value_frame, 0, Qt.AlignLeft)

        self.b_text_frame = QFrame(self.b_Izhik_frame)
        self.b_text_frame.setObjectName(u"b_text_frame")
        sizePolicy4.setHeightForWidth(self.b_text_frame.sizePolicy().hasHeightForWidth())
        self.b_text_frame.setSizePolicy(sizePolicy4)
        self.b_text_frame.setFrameShape(QFrame.StyledPanel)
        self.b_text_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_22 = QHBoxLayout(self.b_text_frame)
        self.horizontalLayout_22.setSpacing(0)
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.horizontalLayout_22.setContentsMargins(0, 0, 0, 0)
        self.b_text = QLabel(self.b_text_frame)
        self.b_text.setObjectName(u"b_text")
        self.b_text.setAlignment(Qt.AlignBottom|Qt.AlignJustify)
        self.b_text.setWordWrap(True)

        self.horizontalLayout_22.addWidget(self.b_text)


        self.horizontalLayout_21.addWidget(self.b_text_frame)


        self.verticalLayout_14.addWidget(self.b_Izhik_frame)

        self.line_3 = QFrame(self.NeuronGenerator_subframe2)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFrameShape(QFrame.HLine)
        self.line_3.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_14.addWidget(self.line_3)

        self.c_Izhik_frame = QFrame(self.NeuronGenerator_subframe2)
        self.c_Izhik_frame.setObjectName(u"c_Izhik_frame")
        self.c_Izhik_frame.setFrameShape(QFrame.StyledPanel)
        self.c_Izhik_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_24 = QHBoxLayout(self.c_Izhik_frame)
        self.horizontalLayout_24.setSpacing(15)
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.horizontalLayout_24.setContentsMargins(0, 0, 0, 0)
        self.c_value_frame = QFrame(self.c_Izhik_frame)
        self.c_value_frame.setObjectName(u"c_value_frame")
        self.c_value_frame.setFrameShape(QFrame.StyledPanel)
        self.c_value_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_25 = QHBoxLayout(self.c_value_frame)
        self.horizontalLayout_25.setSpacing(0)
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.horizontalLayout_25.setContentsMargins(0, 0, 0, 0)
        self.c_value = QLineEdit(self.c_value_frame)
        self.c_value.setObjectName(u"c_value")
        sizePolicy6.setHeightForWidth(self.c_value.sizePolicy().hasHeightForWidth())
        self.c_value.setSizePolicy(sizePolicy6)
        self.c_value.setMinimumSize(QSize(75, 0))
        self.c_value.setMaximumSize(QSize(75, 16777215))
        self.c_value.setFont(font4)
        self.c_value.setStyleSheet(u"")
        self.c_value.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_25.addWidget(self.c_value)


        self.horizontalLayout_24.addWidget(self.c_value_frame)

        self.c_text_frame = QFrame(self.c_Izhik_frame)
        self.c_text_frame.setObjectName(u"c_text_frame")
        sizePolicy4.setHeightForWidth(self.c_text_frame.sizePolicy().hasHeightForWidth())
        self.c_text_frame.setSizePolicy(sizePolicy4)
        self.c_text_frame.setFrameShape(QFrame.StyledPanel)
        self.c_text_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_26 = QHBoxLayout(self.c_text_frame)
        self.horizontalLayout_26.setSpacing(0)
        self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")
        self.horizontalLayout_26.setContentsMargins(0, 0, 0, 0)
        self.c_text = QLabel(self.c_text_frame)
        self.c_text.setObjectName(u"c_text")
        self.c_text.setAlignment(Qt.AlignBottom|Qt.AlignJustify)
        self.c_text.setWordWrap(True)

        self.horizontalLayout_26.addWidget(self.c_text)


        self.horizontalLayout_24.addWidget(self.c_text_frame)


        self.verticalLayout_14.addWidget(self.c_Izhik_frame)

        self.line_4 = QFrame(self.NeuronGenerator_subframe2)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setFrameShape(QFrame.HLine)
        self.line_4.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_14.addWidget(self.line_4)

        self.d_Izhik_frame = QFrame(self.NeuronGenerator_subframe2)
        self.d_Izhik_frame.setObjectName(u"d_Izhik_frame")
        self.d_Izhik_frame.setFrameShape(QFrame.StyledPanel)
        self.d_Izhik_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_27 = QHBoxLayout(self.d_Izhik_frame)
        self.horizontalLayout_27.setSpacing(15)
        self.horizontalLayout_27.setObjectName(u"horizontalLayout_27")
        self.horizontalLayout_27.setContentsMargins(0, 0, 0, 0)
        self.d_value_frame = QFrame(self.d_Izhik_frame)
        self.d_value_frame.setObjectName(u"d_value_frame")
        self.d_value_frame.setFrameShape(QFrame.StyledPanel)
        self.d_value_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_28 = QHBoxLayout(self.d_value_frame)
        self.horizontalLayout_28.setSpacing(0)
        self.horizontalLayout_28.setObjectName(u"horizontalLayout_28")
        self.horizontalLayout_28.setContentsMargins(0, 0, 0, 0)
        self.d_value = QLineEdit(self.d_value_frame)
        self.d_value.setObjectName(u"d_value")
        sizePolicy6.setHeightForWidth(self.d_value.sizePolicy().hasHeightForWidth())
        self.d_value.setSizePolicy(sizePolicy6)
        self.d_value.setMinimumSize(QSize(75, 0))
        self.d_value.setMaximumSize(QSize(75, 16777215))
        self.d_value.setFont(font4)
        self.d_value.setStyleSheet(u"")
        self.d_value.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_28.addWidget(self.d_value)


        self.horizontalLayout_27.addWidget(self.d_value_frame, 0, Qt.AlignLeft)

        self.d_text_frame = QFrame(self.d_Izhik_frame)
        self.d_text_frame.setObjectName(u"d_text_frame")
        self.d_text_frame.setFrameShape(QFrame.StyledPanel)
        self.d_text_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_29 = QHBoxLayout(self.d_text_frame)
        self.horizontalLayout_29.setSpacing(0)
        self.horizontalLayout_29.setObjectName(u"horizontalLayout_29")
        self.horizontalLayout_29.setContentsMargins(0, 0, 0, 0)
        self.d_text = QLabel(self.d_text_frame)
        self.d_text.setObjectName(u"d_text")
        sizePolicy4.setHeightForWidth(self.d_text.sizePolicy().hasHeightForWidth())
        self.d_text.setSizePolicy(sizePolicy4)
        self.d_text.setAlignment(Qt.AlignBottom|Qt.AlignJustify)
        self.d_text.setWordWrap(True)

        self.horizontalLayout_29.addWidget(self.d_text)


        self.horizontalLayout_27.addWidget(self.d_text_frame)


        self.verticalLayout_14.addWidget(self.d_Izhik_frame)

        self.line_5 = QFrame(self.NeuronGenerator_subframe2)
        self.line_5.setObjectName(u"line_5")
        self.line_5.setFrameShape(QFrame.HLine)
        self.line_5.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_14.addWidget(self.line_5)

        self.Izhik_button_frame = QFrame(self.NeuronGenerator_subframe2)
        self.Izhik_button_frame.setObjectName(u"Izhik_button_frame")
        self.Izhik_button_frame.setFrameShape(QFrame.StyledPanel)
        self.Izhik_button_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_30 = QHBoxLayout(self.Izhik_button_frame)
        self.horizontalLayout_30.setSpacing(0)
        self.horizontalLayout_30.setObjectName(u"horizontalLayout_30")
        self.horizontalLayout_30.setContentsMargins(0, 0, 0, 0)
        self.DisplayNeuron_frame = QFrame(self.Izhik_button_frame)
        self.DisplayNeuron_frame.setObjectName(u"DisplayNeuron_frame")
        self.DisplayNeuron_frame.setFrameShape(QFrame.StyledPanel)
        self.DisplayNeuron_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_31 = QHBoxLayout(self.DisplayNeuron_frame)
        self.horizontalLayout_31.setObjectName(u"horizontalLayout_31")
        self.horizontalLayout_31.setContentsMargins(-1, 0, -1, 0)
        self.DisplayNeuronPushButton = QPushButton(self.DisplayNeuron_frame)
        self.DisplayNeuronPushButton.setObjectName(u"DisplayNeuronPushButton")
        self.DisplayNeuronPushButton.setEnabled(True)
        self.DisplayNeuronPushButton.setFont(font3)
        self.DisplayNeuronPushButton.setMouseTracking(True)
        self.DisplayNeuronPushButton.setFocusPolicy(Qt.NoFocus)
        self.DisplayNeuronPushButton.setAutoFillBackground(False)
        self.DisplayNeuronPushButton.setStyleSheet(u"color: rgb(147, 161, 161);")
        self.DisplayNeuronPushButton.setCheckable(False)
        self.DisplayNeuronPushButton.setAutoRepeat(False)

        self.horizontalLayout_31.addWidget(self.DisplayNeuronPushButton)


        self.horizontalLayout_30.addWidget(self.DisplayNeuron_frame)

        self.SaveNeuron_frame = QFrame(self.Izhik_button_frame)
        self.SaveNeuron_frame.setObjectName(u"SaveNeuron_frame")
        self.SaveNeuron_frame.setFrameShape(QFrame.StyledPanel)
        self.SaveNeuron_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_32 = QHBoxLayout(self.SaveNeuron_frame)
        self.horizontalLayout_32.setObjectName(u"horizontalLayout_32")
        self.horizontalLayout_32.setContentsMargins(-1, 0, -1, 0)
        self.SaveNeuronPushButton = QPushButton(self.SaveNeuron_frame)
        self.SaveNeuronPushButton.setObjectName(u"SaveNeuronPushButton")
        self.SaveNeuronPushButton.setEnabled(True)
        font6 = QFont()
        font6.setPointSize(10)
        font6.setBold(True)
        font6.setStrikeOut(False)
        self.SaveNeuronPushButton.setFont(font6)
        self.SaveNeuronPushButton.setStyleSheet(u"color: rgb(147, 161, 161);")
        self.SaveNeuronPushButton.setCheckable(False)

        self.horizontalLayout_32.addWidget(self.SaveNeuronPushButton)


        self.horizontalLayout_30.addWidget(self.SaveNeuron_frame)


        self.verticalLayout_14.addWidget(self.Izhik_button_frame, 0, Qt.AlignVCenter)


        self.verticalLayout_9.addWidget(self.NeuronGenerator_subframe2)


        self.horizontalLayout_10.addWidget(self.NeuronGenerator_subgroupBox2)


        self.horizontalLayout_9.addWidget(self.NeuronGenerator_widget)

        self.mainbody_stackedWidget.addWidget(self.page_301)

        self.horizontalLayout_7.addWidget(self.mainbody_stackedWidget)


        self.verticalLayout_2.addWidget(self.mainBodyContainer)

        self.footer_widget = QWidget(self.main_window)
        self.footer_widget.setObjectName(u"footer_widget")
        self.footer_widget.setMinimumSize(QSize(0, 30))
        self.footer_widget.setMaximumSize(QSize(16777215, 30))
        self.footer_widget.setStyleSheet(u"")
        self.horizontalLayout_3 = QHBoxLayout(self.footer_widget)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.license_frame = QFrame(self.footer_widget)
        self.license_frame.setObjectName(u"license_frame")
        self.license_frame.setFrameShape(QFrame.StyledPanel)
        self.license_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.license_frame)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.line_6 = QFrame(self.license_frame)
        self.line_6.setObjectName(u"line_6")
        sizePolicy8.setHeightForWidth(self.line_6.sizePolicy().hasHeightForWidth())
        self.line_6.setSizePolicy(sizePolicy8)
        self.line_6.setFrameShape(QFrame.HLine)
        self.line_6.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_3.addWidget(self.line_6)

        self.license_label = QLabel(self.license_frame)
        self.license_label.setObjectName(u"license_label")

        self.verticalLayout_3.addWidget(self.license_label)


        self.horizontalLayout_3.addWidget(self.license_frame)

        self.logo_frame = QFrame(self.footer_widget)
        self.logo_frame.setObjectName(u"logo_frame")
        self.logo_frame.setMaximumSize(QSize(16777215, 20))
        self.horizontalLayout_8 = QHBoxLayout(self.logo_frame)
        self.horizontalLayout_8.setSpacing(5)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.badenlab_logo = QLabel(self.logo_frame)
        self.badenlab_logo.setObjectName(u"badenlab_logo")
        self.badenlab_logo.setMinimumSize(QSize(0, 0))
        self.badenlab_logo.setMaximumSize(QSize(125, 30))
        self.badenlab_logo.setPixmap(QPixmap(u":/resources/resources/Baden-Logo.png"))
        self.badenlab_logo.setScaledContents(True)
        self.badenlab_logo.setWordWrap(False)

        self.horizontalLayout_8.addWidget(self.badenlab_logo)

        self.ON_logo = QLabel(self.logo_frame)
        self.ON_logo.setObjectName(u"ON_logo")
        sizePolicy3.setHeightForWidth(self.ON_logo.sizePolicy().hasHeightForWidth())
        self.ON_logo.setSizePolicy(sizePolicy3)
        self.ON_logo.setMaximumSize(QSize(160, 30))
        self.ON_logo.setPixmap(QPixmap(u":/resources/resources/ON-Logo.png"))
        self.ON_logo.setScaledContents(True)

        self.horizontalLayout_8.addWidget(self.ON_logo)

        self.trend_logo = QLabel(self.logo_frame)
        self.trend_logo.setObjectName(u"trend_logo")
        sizePolicy3.setHeightForWidth(self.trend_logo.sizePolicy().hasHeightForWidth())
        self.trend_logo.setSizePolicy(sizePolicy3)
        self.trend_logo.setMaximumSize(QSize(40, 16777215))
        self.trend_logo.setPixmap(QPixmap(u":/resources/resources/TReND-Logo.png"))
        self.trend_logo.setScaledContents(True)

        self.horizontalLayout_8.addWidget(self.trend_logo)


        self.horizontalLayout_3.addWidget(self.logo_frame, 0, Qt.AlignRight)

        self.sizegrip = QFrame(self.footer_widget)
        self.sizegrip.setObjectName(u"sizegrip")
        self.sizegrip.setFrameShape(QFrame.StyledPanel)
        self.sizegrip.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_3.addWidget(self.sizegrip)


        self.verticalLayout_2.addWidget(self.footer_widget)

        self.footer_widget.raise_()
        self.header_widget.raise_()
        self.mainBodyContainer.raise_()

        self.horizontalLayout.addWidget(self.main_window)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.centerMenuSubContainer_menu_stackedwidget.setCurrentIndex(2)
        self.mainbody_stackedWidget.setCurrentIndex(7)
        self.Spikeling_parameter_stackedwidget.setCurrentIndex(0)
        self.DataAnalysis_Display_StackedWidget.setCurrentIndex(3)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.menu_pushButton.setText("")
        self.SpikelingMenu_pushButton.setText(QCoreApplication.translate("MainWindow", u"Spikeling", None))
        self.ImagingMenu_pushButton.setText(QCoreApplication.translate("MainWindow", u"Imaging", None))
        self.NeuronGeneratorMenu_pushButton.setText(QCoreApplication.translate("MainWindow", u"Neuron Generator", None))
        self.StimuluGeneratorMenu_pushButton.setText(QCoreApplication.translate("MainWindow", u"Stimulus Generator", None))
        self.ExercisesMenu_pushButton.setText(QCoreApplication.translate("MainWindow", u"Exercises", None))
        self.SettingsMenu_pushButton.setText(QCoreApplication.translate("MainWindow", u"Settings", None))
        self.AboutMenu_pushButton.setText(QCoreApplication.translate("MainWindow", u"About", None))
        self.HelpMenu_pushButton.setText(QCoreApplication.translate("MainWindow", u"Help", None))
        self.GitHubMenu_pushButton.setText(QCoreApplication.translate("MainWindow", u"GitHub", None))
        self.centerMenuSubContainer_exit_label.setText(QCoreApplication.translate("MainWindow", u"Sub-menus", None))
        self.centerMenuSubContainer_exit_pushButton.setText("")
        self.Spikeling_SubMenu_label.setText(QCoreApplication.translate("MainWindow", u"Spikeling Neuron Interface", None))
        self.Neuron_pushButton.setText(QCoreApplication.translate("MainWindow", u"Neuron Interface", None))
        self.NeuronTutorial_pushButton.setText(QCoreApplication.translate("MainWindow", u"Tutorial", None))
        self.NeuronDataAnalysis_pushButton.setText(QCoreApplication.translate("MainWindow", u"Data Analysis", None))
        self.Imaging_SubMenu_label.setText(QCoreApplication.translate("MainWindow", u"Spikeling Imaging Stimulation", None))
        self.ImagingIdeal_pushButton.setText(QCoreApplication.translate("MainWindow", u"Ideal Imaging", None))
        self.ImagingStimulation_pushButton.setText(QCoreApplication.translate("MainWindow", u"Imaging Stimulation", None))
        self.ImagingTutorial_pushButton.setText(QCoreApplication.translate("MainWindow", u"Tutorial", None))
        self.ImagingDataAnalysis_pushButton.setText(QCoreApplication.translate("MainWindow", u"Data Analysis", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Neuron Generator", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Stimulus Generator", None))
        self.Exercices_SubMenu_label.setText(QCoreApplication.translate("MainWindow", u"Suggested Exercices", None))
        self.Exercice101_pushButton.setText(QCoreApplication.translate("MainWindow", u"1.1 Introduction to Spikeling", None))
        self.Exercice102_pushButton.setText(QCoreApplication.translate("MainWindow", u"1.2 Spikes", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Settings", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"About", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Help", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"GitHub", None))
        self.appTitle_pushButton.setText("")
        self.appTitle_label.setText(QCoreApplication.translate("MainWindow", u"Spikeling V2.2 GUI", None))
        self.reduce_pushButton.setText("")
        self.expand_pushButton.setText("")
        self.exit_pushButton.setText("")
        self.mainbody_header_text.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:48pt; color:#eee8d5;\">Spikeling</span></p><p align=\"center\"><span style=\" font-size:10pt;\">A hardware implementation of a spiking neuron for neursocience teaching and outreach</span></p><p align=\"right\"><span style=\" font-size:8pt;\">Conceived and developed by  M.J.Y. Zimmermann, A.M. Chagas, T. Baden</span></p></body></html>", None))
        self.mainbody_content_text.setText(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:700;\">Spikeling</span><span style=\" font-size:12pt;\"> is an educational tool for neuroscience students and enthusiasts!</span></p>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">It is an artificial neuron that can receive different inputs, integrate them and outputs its computation, just like a spiking neuron would!</span></p>\n"
"<p align=\"ju"
                        "stify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">Technically, it consists on a microcontroller (an ESP32) running the computationally efficient Izhikevich model of a spiking neuron.</span></p>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\"><br /></span></p>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; color:#268bd2;\">This project is licensed under the </span><span style=\" font-size:10pt; font-weight:700; color:#268bd2;\">GNU General Public License v3.0</span></p>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; color"
                        ":#268bd2;\">The hardware is licensed under the </span><span style=\" font-size:10pt; font-weight:700; color:#268bd2;\">CERN OHL v1.2</span></p>\n"
"<p align=\"justify\" style=\"-qt-paragraph-type:empty; margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:10pt; font-weight:700; color:#268bd2;\"><br /></p>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#268bd2;\">https://github.com/MaxZimmer/Spikeling-V2</span></p></body></html>", None))
        self.mainbody_content_SpikelingGif.setText("")
        self.mainbody_footer_text.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"justify\"><span style=\" font-size:8pt;\">Understanding how neurons encode and compute information is fundamental to our study of the brain, but opportunities for hands-on experience with neurophysiological techniques on live neurons are scarce in science education.</span></p><p align=\"justify\"><span style=\" font-size:8pt;\">Originally developped in the Baden Lab at the University of Sussex, Spikeling is an </span><span style=\" font-size:8pt; font-style:italic;\">in-silico</span><span style=\" font-size:8pt;\"> neuron that mimics a wide range of neuronal behaviours for classroom education and public neuroscience outreach. The current version is the result of a collective work from on-field teaching experience, both in the UK and on the African continent and from users and students feedback.</span></p><p align=\"justify\"><span style=\" font-size:8pt;\">The GUI presented here proposed a full and didactic interaction with the neuronal model. It also contains various exercices wh"
                        "ich can be linked to classical neuroscience teachings from early to advanced degree students. Futhermore it offers the opportunity to teachers to prepare practical on: programming, data analysis scipting, methodology and protocol design. All very important skills for modern neuroscience academics but which is unfortunately widely lacking from neuroscience degrees education.</span></p></body></html>", None))
        self.Spikeling_SelectPortLabel.setText(QCoreApplication.translate("MainWindow", u"Select Port :", None))
        self.Spikeling_SelectPortComboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Select a COM port:", None))

        self.Spikeling_ConnectButton.setText(QCoreApplication.translate("MainWindow", u"Connected", None))
        self.Spikeling_NeuronModeLabel.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:18pt; font-weight:700;\">Neuron Mode</span></p></body></html>", None))
        self.Spikeling_NeuronModeComboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Select Neuron Mode", None))
        self.Spikeling_NeuronModeComboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"Tonic Spiking", None))
        self.Spikeling_NeuronModeComboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"Phasic Spiking", None))
        self.Spikeling_NeuronModeComboBox.setItemText(3, QCoreApplication.translate("MainWindow", u"Tonic Bursting", None))
        self.Spikeling_NeuronModeComboBox.setItemText(4, QCoreApplication.translate("MainWindow", u"Phasic Bursting", None))
        self.Spikeling_NeuronModeComboBox.setItemText(5, QCoreApplication.translate("MainWindow", u"Mixed Mode", None))
        self.Spikeling_NeuronModeComboBox.setItemText(6, QCoreApplication.translate("MainWindow", u"Spike Frequency Adaptation", None))
        self.Spikeling_NeuronModeComboBox.setItemText(7, QCoreApplication.translate("MainWindow", u"Class 1 Excitable", None))
        self.Spikeling_NeuronModeComboBox.setItemText(8, QCoreApplication.translate("MainWindow", u"Class 2 Excitable", None))
        self.Spikeling_NeuronModeComboBox.setItemText(9, QCoreApplication.translate("MainWindow", u"Spike Latency", None))
        self.Spikeling_NeuronModeComboBox.setItemText(10, QCoreApplication.translate("MainWindow", u"Subthreshold Oscillations", None))
        self.Spikeling_NeuronModeComboBox.setItemText(11, QCoreApplication.translate("MainWindow", u"Resonator", None))
        self.Spikeling_NeuronModeComboBox.setItemText(12, QCoreApplication.translate("MainWindow", u"Integrator", None))

        self.Spikeling_NeuronBrowsePushButton.setText(QCoreApplication.translate("MainWindow", u"Browse", None))
        self.Spikeling_Syn2InputCheckbox.setText(QCoreApplication.translate("MainWindow", u"Synapse 2 Input", None))
        self.Spikeling_Syn2VmCheckbox.setText(QCoreApplication.translate("MainWindow", u"Synapse 2 Vm", None))
        self.Spikeling_Syn1InputCheckbox.setText(QCoreApplication.translate("MainWindow", u"Synapse 1 Input", None))
        self.Spikeling_Syn1VmCheckbox.setText(QCoreApplication.translate("MainWindow", u"Synapse 1 Vm", None))
        self.Spikeling_StimulusCheckbox.setText(QCoreApplication.translate("MainWindow", u"Stimulus", None))
        self.Spikeling_InputCurrentCheckbox.setText(QCoreApplication.translate("MainWindow", u"Input Current", None))
        self.Spikeling_VmCheckbox.setText(QCoreApplication.translate("MainWindow", u"Vm", None))
        self.Spikeling_DataRecording_box.setTitle(QCoreApplication.translate("MainWindow", u"Data Recording", None))
        self.Spikeling_DataRecording_ComboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Live ", None))
        self.Spikeling_DataRecording_ComboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"Loop", None))

        self.Spikeling_DataRecording_NumberOfLoops_abel.setText(QCoreApplication.translate("MainWindow", u"Number of loops :", None))
        self.Spikeling_DataRecording_NumberOfLoops_value.setText("")
        self.Spikeling_DataRecording_SelectRecordFolder_label.setText(QCoreApplication.translate("MainWindow", u"Data Logging: Filename", None))
        self.Spikeling_DataRecording_RecordFolder_value.setText("")
        self.Spikeling_DataRecording_RecordFolderDir_pushButton.setText(QCoreApplication.translate("MainWindow", u"Dir.", None))
        self.Spikeling_SelectedFolderLabel.setText("")
        self.Spikeling_DataRecording_Record_pushButton.setText(QCoreApplication.translate("MainWindow", u"Record", None))
        self.Spikeling_parameter_exit_pushButton.setText("")
        self.Spikeling_parameter_exit_label.setText(QCoreApplication.translate("MainWindow", u"Parameters", None))
        self.StimulusLabel.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:700;\">Stimulus</span></p></body></html>", None))
        self.Spikeling_StimFre_checkBox.setText(QCoreApplication.translate("MainWindow", u"Stimulus Frequency (Hz)", None))
        self.Spikeling_StimFre_values_min.setText(QCoreApplication.translate("MainWindow", u"2.5", None))
        self.Spikeling_StimFre_values_0.setText(QCoreApplication.translate("MainWindow", u"5", None))
        self.Spikeling_StimFre_values_max.setText(QCoreApplication.translate("MainWindow", u"100", None))
        self.Spikeling_StimFre_image.setText("")
        self.Spikeling_StimStr_checkBox.setText(QCoreApplication.translate("MainWindow", u"Stimulus Strenght (%)", None))
        self.Spikeling_StimStr_values_min.setText(QCoreApplication.translate("MainWindow", u"-100", None))
        self.Spikeling_StimStr_values_0.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.Spikeling_StimStr_values_max.setText(QCoreApplication.translate("MainWindow", u"100", None))
        self.Spikeling_StimStr_image.setText("")
        self.Spikeling_CustomStimulus_checkBox.setText(QCoreApplication.translate("MainWindow", u"Custom Stimulus", None))
        self.Spikeling_PR_label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:700;\">Photo-Receptor</span></p></body></html>", None))
        self.Spikeling_PR_PhotoGain_checkBox.setText(QCoreApplication.translate("MainWindow", u"Photo-Gain (%)", None))
        self.Spikeling_PR_PhotoGain_values_min.setText(QCoreApplication.translate("MainWindow", u"-100", None))
        self.Spikeling_PR_PhotoGain_values_0.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.Spikeling_PR_PhotoGain_values_max.setText(QCoreApplication.translate("MainWindow", u"100", None))
        self.Spikeling_PR_Decay_checkBox.setText(QCoreApplication.translate("MainWindow", u"Decay", None))
        self.Spikeling_PR_Decay_value.setText(QCoreApplication.translate("MainWindow", u"0.001", None))
        self.Spikeling_PR_Recovery_checkBox.setText(QCoreApplication.translate("MainWindow", u"Recovery", None))
        self.Spikeling_PR_Recovery_value.setText(QCoreApplication.translate("MainWindow", u"0.025", None))
        self.Spikeling_PatchClamp_label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:700;\">Patch Clamp</span></p></body></html>", None))
        self.Spikeling_PatchClamp_checkBox.setText(QCoreApplication.translate("MainWindow", u"Injected Current (a.u.)", None))
        self.Spikeling_PatchClamp_values_min.setText(QCoreApplication.translate("MainWindow", u"-100", None))
        self.Spikeling_PatchClamp_values_0.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.Spikeling_PatchClamp_values_max.setText(QCoreApplication.translate("MainWindow", u"100", None))
        self.Spikeling_Noise_label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:700;\">Noise</span></p></body></html>", None))
        self.Spikeling_Noise_checkBox.setText(QCoreApplication.translate("MainWindow", u"Noise Level", None))
        self.Spikeling_Noise_0_value.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.Spikeling_Noise_max_value.setText(QCoreApplication.translate("MainWindow", u"max", None))
        self.Spikeling_Synapse1_label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:700;\">Synapse 1</span></p></body></html>", None))
        self.Spikeling_Synapse1_checkBox.setText(QCoreApplication.translate("MainWindow", u"Synaptic Gain (%)", None))
        self.Spikeling_Synapse1_min.setText(QCoreApplication.translate("MainWindow", u"-100", None))
        self.Spikeling_Synapse1_0.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.Spikeling_Synapse1_max.setText(QCoreApplication.translate("MainWindow", u"100", None))
        self.Spikeling_Synapse1_Decay_checkBox.setText(QCoreApplication.translate("MainWindow", u"Decay", None))
        self.Spikeling_Synapse1_Decay_value.setText(QCoreApplication.translate("MainWindow", u"0.995", None))
        self.Spikeling_Synapse2_label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:700;\">Synapse 2</span></p></body></html>", None))
        self.Spikeling_Synapse2_checkBox.setText(QCoreApplication.translate("MainWindow", u"Synaptic Gain (%)", None))
        self.Spikeling_Synapse2_min.setText(QCoreApplication.translate("MainWindow", u"-100", None))
        self.Spikeling_Synapse2_0.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.Spikeling_Synapse2_max.setText(QCoreApplication.translate("MainWindow", u"100", None))
        self.Spikeling_Synapse2_Decay_checkBox.setText(QCoreApplication.translate("MainWindow", u"Decay", None))
        self.Spikeling_Synapse2_Decay_value.setText(QCoreApplication.translate("MainWindow", u"0.990", None))
        self.Spikeling_rightMenuSubContainer_pushButton.setText("")
        self.Spikeling_StimulusParameter_pushButton.setText(QCoreApplication.translate("MainWindow", u"Stimulus Parameters", None))
        self.Spikeling_NeuronParameter_pushButton.setText(QCoreApplication.translate("MainWindow", u"Neuron Parameters", None))
        self.label_2.setText("")
        self.DataAnalysis_Neuron0Vm_pushButton10.setText(QCoreApplication.translate("MainWindow", u"Spikeling Neuron", None))
        self.DataAnalysis_Neuron1Vm_pushButton10.setText(QCoreApplication.translate("MainWindow", u"Aux Neuron 1", None))
        self.DataAnalysis_Neuron2Vm_pushButton10.setText(QCoreApplication.translate("MainWindow", u"Aux Neuron 2", None))
        self.DataAnalysis_Neuron0Vm_pushButton11.setText(QCoreApplication.translate("MainWindow", u"Spikeling Neuron", None))
        self.DataAnalysis_Neuron1Vm_pushButton11.setText(QCoreApplication.translate("MainWindow", u"Aux Neuron 1", None))
        self.DataAnalysis_Neuron2Vm_pushButton11.setText(QCoreApplication.translate("MainWindow", u"Aux Neuron 2", None))
        self.DataAnalysis_Neuron0Vm_pushButton12.setText(QCoreApplication.translate("MainWindow", u"Spikeling Neuron", None))
        self.DataAnalysis_Neuron1Vm_pushButton12.setText(QCoreApplication.translate("MainWindow", u"Aux Neuron 1", None))
        self.DataAnalysis_Neuron2Vm_pushButton12.setText(QCoreApplication.translate("MainWindow", u"Aux Neuron 2", None))
        self.DataAnalysis_Neuron0Vm_pushButton20.setText(QCoreApplication.translate("MainWindow", u"Spikeling Neuron", None))
        self.DataAnalysis_Neuron1Vm_pushButton20.setText(QCoreApplication.translate("MainWindow", u"Aux Neuron 1", None))
        self.DataAnalysis_Neuron2Vm_pushButton20.setText(QCoreApplication.translate("MainWindow", u"Aux Neuron 2", None))
        self.DataAnalysis_Neuron0Vm_pushButton21.setText(QCoreApplication.translate("MainWindow", u"Spikeling Neuron", None))
        self.DataAnalysis_Neuron1Vm_pushButton21.setText(QCoreApplication.translate("MainWindow", u"Aux Neuron 1", None))
        self.DataAnalysis_Neuron2Vm_pushButton21.setText(QCoreApplication.translate("MainWindow", u"Aux Neuron 2", None))
        self.DataAnalysis_Neuron0Vm_pushButton22.setText(QCoreApplication.translate("MainWindow", u"Spikeling Neuron", None))
        self.DataAnalysis_Neuron1Vm_pushButton22.setText(QCoreApplication.translate("MainWindow", u"Aux Neuron 1", None))
        self.DataAnalysis_Neuron2Vm_pushButton22.setText(QCoreApplication.translate("MainWindow", u"Aux Neuron 2", None))
        self.DataAnalysis_Neuron0Vm_pushButton30.setText(QCoreApplication.translate("MainWindow", u"Spikeling Neuron", None))
        self.DataAnalysis_Neuron1Vm_pushButton30.setText(QCoreApplication.translate("MainWindow", u"Aux Neuron 1", None))
        self.DataAnalysis_Neuron2Vm_pushButton30.setText(QCoreApplication.translate("MainWindow", u"Aux Neuron 2", None))
        self.DataAnalysis_Neuron0Vm_pushButton31.setText(QCoreApplication.translate("MainWindow", u"Spikeling Neuron", None))
        self.DataAnalysis_Neuron1Vm_pushButton31.setText(QCoreApplication.translate("MainWindow", u"Aux Neuron 1", None))
        self.DataAnalysis_Neuron2Vm_pushButton31.setText(QCoreApplication.translate("MainWindow", u"Aux Neuron 2", None))
        self.DataAnalysis_Neuron0Vm_pushButton32.setText(QCoreApplication.translate("MainWindow", u"Spikeling Neuron", None))
        self.DataAnalysis_Neuron1Vm_pushButton32.setText(QCoreApplication.translate("MainWindow", u"Aux Neuron 1", None))
        self.DataAnalysis_Neuron2Vm_pushButton32.setText(QCoreApplication.translate("MainWindow", u"Aux Neuron 2", None))
        self.DataAnalysis_LoadData_label.setText("")
        self.DataAnalysis_LoadData_pushButton.setText(QCoreApplication.translate("MainWindow", u"Load Data", None))
        self.DataAnalysis_LoadData_Display_pushButton.setText(QCoreApplication.translate("MainWindow", u"Display Raw Data", None))
        self.DataAnalysis_SaveImage_pushButton.setText(QCoreApplication.translate("MainWindow", u"Save Image", None))
        self.DataAnalysis_Spike_label.setText(QCoreApplication.translate("MainWindow", u"Find Spikes along the Vm trace(s)", None))
        self.DataAnalysis_Spike_threshold_label.setText(QCoreApplication.translate("MainWindow", u"Spike Threshold: ", None))
        self.DataAnalysis_Spike_lineEdit.setText(QCoreApplication.translate("MainWindow", u"-20", None))
        self.DataAnalysis_Spike_mV_label.setText(QCoreApplication.translate("MainWindow", u"mV", None))
        self.DataAnalysis_Spike_result_label.setText("")
        self.DataAnalysis_Spike_Display_pushButton.setText(QCoreApplication.translate("MainWindow", u"Display Spike events", None))
        self.DataAnalysis_Spike_SaveImage_pushButton.setText(QCoreApplication.translate("MainWindow", u"Save Image", None))
        self.DataAnalysis_Spike_Export_pushButton.setText(QCoreApplication.translate("MainWindow", u"Export .csv", None))
        self.DataAnalysis_Average_result_label.setText(QCoreApplication.translate("MainWindow", u"Average traces based on stimulus cycles", None))
        self.DataAnalysis_Average_label.setText("")
        self.DataAnalysis_Average_Display_pushButton.setText(QCoreApplication.translate("MainWindow", u"Display Average traces", None))
        self.DataAnalysis_Average_SaveImage_pushButton.setText(QCoreApplication.translate("MainWindow", u"Save Image", None))
        self.DataAnalysis_Average_Save_pushButton.setText(QCoreApplication.translate("MainWindow", u"Export .csv", None))
        self.label_4.setText("")
        self.label_5.setText("")
        self.label_7.setText("")
        self.NeuronGenerator_subframe1_title_label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:18pt; font-weight:700;\">Spikeling is built on the Izhikevich model</span></p></body></html>", None))
        self.NeuronGenerator_subframe1_Izhik_textbrowser.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">Bifurcation methodologies enable us to reduce many biophysically accurate Hodgkin\u2013Huxley-type neuronal models to a two-dimensional (2-D) system of ordinary differential equations of the form:</span></p>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt; font-weight:696;\">v' = 0.04v</span><span style=\" font-size:11pt; font-weight:696; vertical-align:super;\">"
                        "2</span><span style=\" font-size:11pt; font-weight:696;\"> + 5v + 140 - u + I                    </span><span style=\" font-size:11pt;\">&amp;</span><span style=\" font-size:11pt; font-weight:696;\">                    u' = a(bv - u)</span></p>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">with the auxiliary after-spike resetting:   if </span><span style=\" font-size:11pt; font-weight:696;\">v &gt;= 30 mV</span><span style=\" font-size:10pt;\">, then </span><span style=\" font-size:11pt; font-weight:696;\">v = c</span><span style=\" font-size:10pt;\"> and</span><span style=\" font-size:11pt;\"> </span><span style=\" font-size:11pt; font-weight:696;\">u = u + d</span></p>\n"
"<p align=\"justify\" style=\"-qt-paragraph-type:empty; margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:11pt; font-weight:696;\"><br /></p>"
                        "\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">Here, </span><span style=\" font-size:11pt; font-weight:696;\">v</span><span style=\" font-size:10pt;\"> and </span><span style=\" font-size:11pt; font-weight:696;\">u</span><span style=\" font-size:10pt;\"> are dimensionless variables, and </span><span style=\" font-size:11pt; font-weight:696;\">a</span><span style=\" font-size:10pt;\">, </span><span style=\" font-size:11pt; font-weight:696;\">b</span><span style=\" font-size:10pt;\">, </span><span style=\" font-size:11pt; font-weight:696;\">c</span><span style=\" font-size:10pt;\">, and </span><span style=\" font-size:11pt; font-weight:696;\">d</span><span style=\" font-size:10pt;\"> are dimensionless parameters, and </span><span style=\" font-size:11pt; font-weight:696;\">'= d/dt</span><span style=\" font-size:10pt;\">, where </span><span style=\" font-size:11pt; font-weight:696;\""
                        ">t</span><span style=\" font-size:10pt;\"> is the time. </span></p>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">The variable v represents the membrane potential of the neuron and </span><span style=\" font-size:11pt; font-weight:696;\">u</span><span style=\" font-size:10pt;\"> represents a membrane recovery variable, which accounts for the activation of K+ ionic currents and inactivation of Na+ ionic currents, and it provides negative feedback to </span><span style=\" font-size:11pt; font-weight:696;\">v</span><span style=\" font-size:10pt;\">. </span></p>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">After the spike reaches its apex (+30 mV), the membrane voltage and the recovery variable are reset. </span></p>\n"
"<p align=\"justify\" style=\" mar"
                        "gin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">Synaptic currents or injected DC-currents are delivered via the variable</span><span style=\" font-size:10pt; font-weight:696;\"> </span><span style=\" font-size:11pt; font-weight:696;\">I</span><span style=\" font-size:10pt;\">.</span></p></body></html>", None))
        self.NeuronGenerator_subframe1_Oscilloscope_widget_stimulus_checkbox.setText(QCoreApplication.translate("MainWindow", u"Current Input", None))
        self.NeuronGenerator_subframe1_Oscilloscope_widget_Vm_checkbox.setText(QCoreApplication.translate("MainWindow", u"Vm", None))
        self.NeuronGenerator_subframe1_bottom_label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>As most real neurons, the model does not have a fixed threshold: Depending on the history of the membrane potential prior to the spike, the threshold potential can be as low as -55 mV or as high as -40mV</p></body></html>", None))
        self.NeuronGenerator_subframe1_Izhik_image.setText("")
        self.a_value.setText(QCoreApplication.translate("MainWindow", u"0.02", None))
        self.a_text.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:9pt;\">The parameter </span><span style=\" font-size:12pt; font-weight:600;\">a</span><span style=\" font-size:9pt;\"> describes the time scale of the recovery variable </span><span style=\" font-size:9pt; font-weight:600;\">u</span><span style=\" font-size:9pt;\">. Smaller values result in slower recovery. </span></p><p><span style=\" font-size:9pt; text-decoration: underline;\">A typical value is </span><span style=\" font-size:9pt; font-weight:600; text-decoration: underline;\">a</span><span style=\" font-size:9pt; text-decoration: underline;\"> = 0.02.</span></p></body></html>", None))
        self.b_value.setText(QCoreApplication.translate("MainWindow", u"0.2", None))
        self.b_text.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>The parameter <span style=\" font-size:12pt; font-weight:600;\">b</span> describes the sensitivity of the recovery variable <span style=\" font-weight:600;\">u </span>to the subthreshold fluctuations of the membrane potential v. Greater values couple<span style=\" font-weight:600;\"> v</span> and<span style=\" font-weight:600;\"> u</span> more strongly resulting in possible sub-threshold oscillations and low-threshold spiking dynamics. </p><p><span style=\" text-decoration: underline;\">A typical value is </span><span style=\" font-weight:600; text-decoration: underline;\">b </span><span style=\" text-decoration: underline;\">= 0.2</span>. </p><p>The case <span style=\" font-weight:600;\">b</span> &lt; <span style=\" font-weight:600;\">a</span>(<span style=\" font-weight:600;\">b</span> &gt; <span style=\" font-weight:600;\">a</span>) corresponds to saddle-node (Andronov\u2013Hopf) bifurcation of the resting state.</p></body></html>", None))
        self.c_value.setText(QCoreApplication.translate("MainWindow", u"-65", None))
        self.c_text.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:9pt;\">The parameter</span><span style=\" font-size:12pt; font-weight:600;\"> c</span><span style=\" font-size:9pt;\"> describes the after-spike reset value of the membrane potential v caused by the fast high-threshold K+ conductances. </span></p><p><span style=\" font-size:9pt; text-decoration: underline;\">A typical value is </span><span style=\" font-size:9pt; font-weight:600; text-decoration: underline;\">c</span><span style=\" font-size:9pt; text-decoration: underline;\"> = -65 (mV)</span><span style=\" font-size:9pt;\">.</span></p></body></html>", None))
        self.d_value.setText(QCoreApplication.translate("MainWindow", u"2", None))
        self.d_text.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:9pt;\">The parameter </span><span style=\" font-size:12pt; font-weight:600;\">d</span><span style=\" font-size:9pt;\"> describes after-spike reset of the recovery variable </span><span style=\" font-size:9pt; font-weight:600;\">u</span><span style=\" font-size:9pt;\"> caused by slow high-threshold Na+ and K+ conductances.</span></p><p><span style=\" font-size:9pt; text-decoration: underline;\">A typical value is </span><span style=\" font-size:9pt; font-weight:600; text-decoration: underline;\">d</span><span style=\" font-size:9pt; text-decoration: underline;\"> = 2</span><span style=\" font-size:9pt;\">.</span></p></body></html>", None))
        self.DisplayNeuronPushButton.setText(QCoreApplication.translate("MainWindow", u"Display Neuron", None))
        self.SaveNeuronPushButton.setText(QCoreApplication.translate("MainWindow", u"Save Neuron", None))
        self.license_label.setText(QCoreApplication.translate("MainWindow", u"This project is licensed under the GNU General Public License v3.0", None))
        self.badenlab_logo.setText("")
        self.ON_logo.setText("")
        self.trend_logo.setText("")
    # retranslateUi

