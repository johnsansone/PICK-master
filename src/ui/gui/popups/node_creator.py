# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'node_creator.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets 
from PyQt5.QtWidgets import QMainWindow, QVBoxLayout

import sys

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Create Node")
        Form.resize(539, 300)
        self.formLayoutWidget = QtWidgets.QWidget(Form)
        self.formLayoutWidget.setGeometry(QtCore.QRect(10, -16, 521, 241))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(self.formLayoutWidget)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.nodeIDLabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.nodeIDLabel.setObjectName("nodeIDLabel")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.nodeIDLabel)
        self.nodeIDLineEdit = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.nodeIDLineEdit.setObjectName("nodeIDLineEdit")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.nodeIDLineEdit)
        self.logNameLabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.logNameLabel.setObjectName("logNameLabel")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.logNameLabel)
        self.logNameLineEdit = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.logNameLineEdit.setObjectName("logNameLineEdit")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.logNameLineEdit)
        self.timestampLabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.timestampLabel.setObjectName("timestampLabel")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.timestampLabel)
        self.timestampLineEdit = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.timestampLineEdit.setObjectName("timestampLineEdit")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.timestampLineEdit)
        self.descriptionLabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.descriptionLabel.setObjectName("descriptionLabel")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.descriptionLabel)
        self.descriptionLineEdit = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.descriptionLineEdit.setObjectName("descriptionLineEdit")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.descriptionLineEdit)
        self.creatorTeamLabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.creatorTeamLabel.setObjectName("creatorTeamLabel")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.creatorTeamLabel)
        self.creatorTeamLineEdit = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.creatorTeamLineEdit.setObjectName("creatorTeamLineEdit")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.creatorTeamLineEdit)
        self.eventTeamLabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.eventTeamLabel.setObjectName("eventTeamLabel")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.eventTeamLabel)
        self.eventTeamLineEdit = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.eventTeamLineEdit.setObjectName("eventTeamLineEdit")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.eventTeamLineEdit)
        self.iconLabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.iconLabel.setObjectName("iconLabel")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.LabelRole, self.iconLabel)
        self.comboBox = QtWidgets.QComboBox(self.formLayoutWidget)
        self.comboBox.setObjectName("comboBox")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.FieldRole, self.comboBox)
        self.label_3 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(8, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.label_2 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(9, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.iconLineEdit = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.iconLineEdit.setObjectName("iconLineEdit")
        self.formLayout.setWidget(9, QtWidgets.QFormLayout.FieldRole, self.iconLineEdit)
        self.linkedNodeLabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.linkedNodeLabel.setObjectName("linkedNodeLabel")
        self.formLayout.setWidget(10, QtWidgets.QFormLayout.LabelRole, self.linkedNodeLabel)
        self.linkedNodeLineEdit = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.linkedNodeLineEdit.setObjectName("linkedNodeLineEdit")
        self.formLayout.setWidget(10, QtWidgets.QFormLayout.FieldRole, self.linkedNodeLineEdit)
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(230, 240, 56, 17))
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "TextLabel"))
        self.nodeIDLabel.setText(_translate("Form", "NodeID"))
        self.logNameLabel.setText(_translate("Form", "Log Name"))
        self.timestampLabel.setText(_translate("Form", "Timestamp"))
        self.descriptionLabel.setText(_translate("Form", "Description"))
        self.creatorTeamLabel.setText(_translate("Form", "Creator Team"))
        self.eventTeamLabel.setText(_translate("Form", "Event Team"))
        self.iconLabel.setText(_translate("Form", "Icon"))
        self.label_3.setText(_translate("Form", "or"))
        self.label_2.setText(_translate("Form", "Location"))
        self.linkedNodeLabel.setText(_translate("Form", "Linked Node"))
        self.pushButton.setText(_translate("Form", "Create"))
       

class OpenNodeCreatePopup(QMainWindow):
    
    def __init__(self):
        super().__init__()
        
        self.initUI()
    
    def initUI(self):    
        layout = QVBoxLayout()
        self.Dialog = QtWidgets.QDialog()
        self.ui = Ui_Form()
        self.ui.setupUi(self.Dialog)
        layout.addWidget(self.Dialog)
        self.setLayout(layout)
        self.Dialog.show()
        #sys.exit(app1.exec_())