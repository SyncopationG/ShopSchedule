# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 520)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/pic/pic/logo.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.groupBox_3 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_3.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox_3.setObjectName("groupBox_3")
        self.gridLayout.addWidget(self.groupBox_3, 1, 0, 1, 1)
        self.groupBox_4 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_4.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox_4.setObjectName("groupBox_4")
        self.gridLayout.addWidget(self.groupBox_4, 1, 1, 1, 1)
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout.addWidget(self.groupBox_2, 0, 1, 1, 1)
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.gridLayout_3.addWidget(self.label_3, 4, 0, 1, 1)
        self.gridLayout_4 = QtWidgets.QGridLayout()
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.checkBoxMakespan = QtWidgets.QCheckBox(self.groupBox)
        self.checkBoxMakespan.setChecked(True)
        self.checkBoxMakespan.setObjectName("checkBoxMakespan")
        self.gridLayout_4.addWidget(self.checkBoxMakespan, 0, 0, 1, 1)
        self.checkBoxTotalMakespan = QtWidgets.QCheckBox(self.groupBox)
        self.checkBoxTotalMakespan.setObjectName("checkBoxTotalMakespan")
        self.gridLayout_4.addWidget(self.checkBoxTotalMakespan, 0, 1, 1, 1)
        self.checkBoxTotalFlowTime = QtWidgets.QCheckBox(self.groupBox)
        self.checkBoxTotalFlowTime.setObjectName("checkBoxTotalFlowTime")
        self.gridLayout_4.addWidget(self.checkBoxTotalFlowTime, 0, 2, 1, 1)
        self.checkBoxEarliness = QtWidgets.QCheckBox(self.groupBox)
        self.checkBoxEarliness.setObjectName("checkBoxEarliness")
        self.gridLayout_4.addWidget(self.checkBoxEarliness, 1, 2, 1, 1)
        self.checkBoxTardiness = QtWidgets.QCheckBox(self.groupBox)
        self.checkBoxTardiness.setObjectName("checkBoxTardiness")
        self.gridLayout_4.addWidget(self.checkBoxTardiness, 1, 1, 1, 1)
        self.checkBoxNTardiness = QtWidgets.QCheckBox(self.groupBox)
        self.checkBoxNTardiness.setObjectName("checkBoxNTardiness")
        self.gridLayout_4.addWidget(self.checkBoxNTardiness, 1, 0, 1, 1)
        self.gridLayout_3.addLayout(self.gridLayout_4, 4, 1, 1, 1)
        self.gridLayout_5 = QtWidgets.QGridLayout()
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.checkBoxBasic = QtWidgets.QCheckBox(self.groupBox)
        self.checkBoxBasic.setEnabled(False)
        self.checkBoxBasic.setChecked(True)
        self.checkBoxBasic.setObjectName("checkBoxBasic")
        self.gridLayout_5.addWidget(self.checkBoxBasic, 0, 0, 1, 1)
        self.checkBoxWorkTimetable = QtWidgets.QCheckBox(self.groupBox)
        self.checkBoxWorkTimetable.setObjectName("checkBoxWorkTimetable")
        self.gridLayout_5.addWidget(self.checkBoxWorkTimetable, 0, 1, 1, 1)
        self.checkBoxNoWait = QtWidgets.QCheckBox(self.groupBox)
        self.checkBoxNoWait.setObjectName("checkBoxNoWait")
        self.gridLayout_5.addWidget(self.checkBoxNoWait, 1, 0, 1, 1)
        self.checkBoxLimitedWait = QtWidgets.QCheckBox(self.groupBox)
        self.checkBoxLimitedWait.setObjectName("checkBoxLimitedWait")
        self.gridLayout_5.addWidget(self.checkBoxLimitedWait, 1, 1, 1, 1)
        self.gridLayout_3.addLayout(self.gridLayout_5, 2, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout_3.addWidget(self.label_2, 1, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.gridLayout_3.addWidget(self.label_4, 2, 0, 1, 1)
        self.comboBoxShopType = QtWidgets.QComboBox(self.groupBox)
        self.comboBoxShopType.setObjectName("comboBoxShopType")
        self.comboBoxShopType.addItem("")
        self.comboBoxShopType.addItem("")
        self.comboBoxShopType.addItem("")
        self.comboBoxShopType.addItem("")
        self.comboBoxShopType.addItem("")
        self.comboBoxShopType.addItem("")
        self.comboBoxShopType.addItem("")
        self.gridLayout_3.addWidget(self.comboBoxShopType, 0, 1, 1, 1)
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout_3.addWidget(self.label, 0, 0, 1, 1)
        self.comboBoxDataSource = QtWidgets.QComboBox(self.groupBox)
        self.comboBoxDataSource.setObjectName("comboBoxDataSource")
        self.comboBoxDataSource.addItem("")
        self.comboBoxDataSource.addItem("")
        self.gridLayout_3.addWidget(self.comboBoxDataSource, 1, 1, 1, 1)
        self.line = QtWidgets.QFrame(self.groupBox)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout_3.addWidget(self.line, 3, 1, 1, 1)
        self.gridLayout.addWidget(self.groupBox, 0, 0, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 800, 23))
        self.menuBar.setObjectName("menuBar")
        self.menufile = QtWidgets.QMenu(self.menuBar)
        self.menufile.setObjectName("menufile")
        self.menuHelp = QtWidgets.QMenu(self.menuBar)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menuBar)
        self.actionJSP = QtWidgets.QAction(MainWindow)
        self.actionJSP.setObjectName("actionJSP")
        self.actionFJSP = QtWidgets.QAction(MainWindow)
        self.actionFJSP.setObjectName("actionFJSP")
        self.actionFSP = QtWidgets.QAction(MainWindow)
        self.actionFSP.setObjectName("actionFSP")
        self.actionHFSP = QtWidgets.QAction(MainWindow)
        self.actionHFSP.setObjectName("actionHFSP")
        self.actionClassic = QtWidgets.QAction(MainWindow)
        self.actionClassic.setObjectName("actionClassic")
        self.actionTimetable = QtWidgets.QAction(MainWindow)
        self.actionTimetable.setObjectName("actionTimetable")
        self.actionNew = QtWidgets.QAction(MainWindow)
        self.actionNew.setObjectName("actionNew")
        self.actionOpen = QtWidgets.QAction(MainWindow)
        self.actionOpen.setObjectName("actionOpen")
        self.actionEdit = QtWidgets.QAction(MainWindow)
        self.actionEdit.setObjectName("actionEdit")
        self.actionSave = QtWidgets.QAction(MainWindow)
        self.actionSave.setObjectName("actionSave")
        self.actionSave_as = QtWidgets.QAction(MainWindow)
        self.actionSave_as.setObjectName("actionSave_as")
        self.actionAbout = QtWidgets.QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.menufile.addAction(self.actionNew)
        self.menufile.addAction(self.actionOpen)
        self.menuHelp.addAction(self.actionAbout)
        self.menuBar.addAction(self.menufile.menuAction())
        self.menuBar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "制造车间作业优化调度系统"))
        self.groupBox_3.setTitle(_translate("MainWindow", "优化算法"))
        self.groupBox_4.setTitle(_translate("MainWindow", "结果分析"))
        self.groupBox_2.setTitle(_translate("MainWindow", "调度数据"))
        self.groupBox.setTitle(_translate("MainWindow", "调度类型"))
        self.label_3.setText(_translate("MainWindow", "优化目标"))
        self.checkBoxMakespan.setText(_translate("MainWindow", "工期"))
        self.checkBoxTotalMakespan.setText(_translate("MainWindow", "工期之和"))
        self.checkBoxTotalFlowTime.setText(_translate("MainWindow", "总流程时间"))
        self.checkBoxEarliness.setText(_translate("MainWindow", "总提前期"))
        self.checkBoxTardiness.setText(_translate("MainWindow", "总拖期"))
        self.checkBoxNTardiness.setText(_translate("MainWindow", "拖期工件数"))
        self.checkBoxBasic.setText(_translate("MainWindow", "基本约束"))
        self.checkBoxWorkTimetable.setText(_translate("MainWindow", "工作时间表"))
        self.checkBoxNoWait.setText(_translate("MainWindow", "无等待"))
        self.checkBoxLimitedWait.setText(_translate("MainWindow", "等待时间有限"))
        self.label_2.setText(_translate("MainWindow", "数据来源"))
        self.label_4.setText(_translate("MainWindow", "约束条件"))
        self.comboBoxShopType.setItemText(0, _translate("MainWindow", "作业车间"))
        self.comboBoxShopType.setItemText(1, _translate("MainWindow", "柔性作业车间"))
        self.comboBoxShopType.setItemText(2, _translate("MainWindow", "流水车间"))
        self.comboBoxShopType.setItemText(3, _translate("MainWindow", "混合流水车间"))
        self.comboBoxShopType.setItemText(4, _translate("MainWindow", "多加工路径作业车间"))
        self.comboBoxShopType.setItemText(5, _translate("MainWindow", "多加工路径柔性作业车间"))
        self.comboBoxShopType.setItemText(6, _translate("MainWindow", "考虑工人的柔性作业车间"))
        self.label.setText(_translate("MainWindow", "车间类型"))
        self.comboBoxDataSource.setItemText(0, _translate("MainWindow", "输入数据"))
        self.comboBoxDataSource.setItemText(1, _translate("MainWindow", "标准算例"))
        self.menufile.setTitle(_translate("MainWindow", "文件"))
        self.menuHelp.setTitle(_translate("MainWindow", "帮助"))
        self.actionJSP.setText(_translate("MainWindow", "静态作业车间"))
        self.actionJSP.setToolTip(_translate("MainWindow", "静态作业车间"))
        self.actionFJSP.setText(_translate("MainWindow", "静态柔性作业车间"))
        self.actionFSP.setText(_translate("MainWindow", "静态流水车间"))
        self.actionHFSP.setText(_translate("MainWindow", "静态混合流水车间"))
        self.actionClassic.setText(_translate("MainWindow", "Classic"))
        self.actionTimetable.setText(_translate("MainWindow", "Timetable"))
        self.actionNew.setText(_translate("MainWindow", "新建"))
        self.actionNew.setIconText(_translate("MainWindow", "新建"))
        self.actionOpen.setText(_translate("MainWindow", "打开"))
        self.actionEdit.setText(_translate("MainWindow", "编辑"))
        self.actionSave.setText(_translate("MainWindow", "保存"))
        self.actionSave_as.setText(_translate("MainWindow", "Save as"))
        self.actionAbout.setText(_translate("MainWindow", "关于"))


from . import apprcc_rc