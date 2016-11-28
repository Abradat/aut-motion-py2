# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'motion.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
from API import motors
import thread, time
try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(800, 600)
        MainWindow.setMinimumSize(QtCore.QSize(800, 600))
        MainWindow.setMaximumSize(QtCore.QSize(800, 647))
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setMinimumSize(QtCore.QSize(800, 600))
        self.centralwidget.setMaximumSize(QtCore.QSize(800, 600))
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.stackedWidget = QtGui.QStackedWidget(self.centralwidget)
        self.stackedWidget.setGeometry(QtCore.QRect(0, 0, 800, 560))
        self.stackedWidget.setMinimumSize(QtCore.QSize(800, 560))
        self.stackedWidget.setMaximumSize(QtCore.QSize(800, 560))
        self.stackedWidget.setObjectName(_fromUtf8("stackedWidget"))
        self.mainPage = QtGui.QWidget()
        self.mainPage.setMinimumSize(QtCore.QSize(800, 600))
        self.mainPage.setMaximumSize(QtCore.QSize(800, 600))
        self.mainPage.setObjectName(_fromUtf8("mainPage"))
        self.mPageMFrame = QtGui.QFrame(self.mainPage)
        self.mPageMFrame.setGeometry(QtCore.QRect(10, 20, 541, 531))
        self.mPageMFrame.setStyleSheet(_fromUtf8("border : 1px solid rgb(113, 0, 0);\n"
""))
        self.mPageMFrame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.mPageMFrame.setFrameShadow(QtGui.QFrame.Raised)
        self.mPageMFrame.setObjectName(_fromUtf8("mPageMFrame"))
        self.mId = QtGui.QLabel(self.mPageMFrame)
        self.mId.setGeometry(QtCore.QRect(30, 20, 31, 21))
        self.mId.setStyleSheet(_fromUtf8("font: 63 14pt \"KacstArt\";\n"
"border : none;\n"
""))
        self.mId.setObjectName(_fromUtf8("mId"))
        self.mAngle = QtGui.QLabel(self.mPageMFrame)
        self.mAngle.setGeometry(QtCore.QRect(90, 20, 61, 21))
        self.mAngle.setStyleSheet(_fromUtf8("font: 63 14pt \"KacstArt\";\n"
"border : none;\n"
"\n"
""))
        self.mAngle.setObjectName(_fromUtf8("mAngle"))
        self.mPos = QtGui.QLabel(self.mPageMFrame)
        self.mPos.setGeometry(QtCore.QRect(180, 20, 81, 21))
        self.mPos.setStyleSheet(_fromUtf8("font: 63 14pt \"KacstArt\";\n"
"border : none;\n"
"\n"
""))
        self.mPos.setObjectName(_fromUtf8("mPos"))
        self.m1Frame = QtGui.QFrame(self.mPageMFrame)
        self.m1Frame.setGeometry(QtCore.QRect(20, 50, 501, 31))
        self.m1Frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.m1Frame.setFrameShadow(QtGui.QFrame.Raised)
        self.m1Frame.setObjectName(_fromUtf8("m1Frame"))
        self.m1 = QtGui.QLabel(self.m1Frame)
        self.m1.setGeometry(QtCore.QRect(10, 0, 16, 31))
        self.m1.setStyleSheet(_fromUtf8("font: 63 14pt \"KacstArt\";\n"
"border : none;\n"
""))
        self.m1.setObjectName(_fromUtf8("m1"))
        self.m1Ang = QtGui.QLabel(self.m1Frame)
        self.m1Ang.setGeometry(QtCore.QRect(70, 10, 51, 17))
        self.m1Ang.setStyleSheet(_fromUtf8("font: 63 14pt \"KacstArt\";\n"
"border : none;\n"
"        "))
        self.m1Ang.setObjectName(_fromUtf8("m1Ang"))
        self.m1Pos = QtGui.QLabel(self.m1Frame)
        self.m1Pos.setGeometry(QtCore.QRect(170, 10, 51, 17))
        self.m1Pos.setStyleSheet(_fromUtf8("font: 63 14pt \"KacstArt\";\n"
"border : none;\n"
"        "))
        self.m1Pos.setObjectName(_fromUtf8("m1Pos"))
        self.m10 = QtGui.QLabel(self.m1Frame)
        self.m10.setGeometry(QtCore.QRect(270, 0, 31, 31))
        self.m10.setStyleSheet(_fromUtf8("font: 63 14pt \"KacstArt\";\n"
"border : none;\n"
""))
        self.m10.setObjectName(_fromUtf8("m10"))
        self.m10Ang = QtGui.QLabel(self.m1Frame)
        self.m10Ang.setGeometry(QtCore.QRect(340, 10, 51, 17))
        self.m10Ang.setStyleSheet(_fromUtf8("font: 63 14pt \"KacstArt\";\n"
"border : none;\n"
"        "))
        self.m10Ang.setObjectName(_fromUtf8("m10Ang"))
        self.m10Pos = QtGui.QLabel(self.m1Frame)
        self.m10Pos.setGeometry(QtCore.QRect(430, 10, 51, 17))
        self.m10Pos.setStyleSheet(_fromUtf8("font: 63 14pt \"KacstArt\";\n"
"border : none;\n"
"        "))
        self.m10Pos.setObjectName(_fromUtf8("m10Pos"))
        self.m2Frame = QtGui.QFrame(self.mPageMFrame)
        self.m2Frame.setGeometry(QtCore.QRect(20, 100, 501, 31))
        self.m2Frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.m2Frame.setFrameShadow(QtGui.QFrame.Raised)
        self.m2Frame.setObjectName(_fromUtf8("m2Frame"))
        self.m2 = QtGui.QLabel(self.m2Frame)
        self.m2.setGeometry(QtCore.QRect(10, 0, 16, 31))
        self.m2.setStyleSheet(_fromUtf8("font: 63 14pt \"KacstArt\";\n"
"border : none;\n"
""))
        self.m2.setObjectName(_fromUtf8("m2"))
        self.m2Ang = QtGui.QLabel(self.m2Frame)
        self.m2Ang.setGeometry(QtCore.QRect(70, 10, 51, 17))
        self.m2Ang.setStyleSheet(_fromUtf8("font: 63 14pt \"KacstArt\";\n"
"border : none;\n"
"        "))
        self.m2Ang.setObjectName(_fromUtf8("m2Ang"))
        self.label_4 = QtGui.QLabel(self.m2Frame)
        self.label_4.setGeometry(QtCore.QRect(250, 30, 51, 17))
        self.label_4.setStyleSheet(_fromUtf8("font: 63 14pt \"KacstArt\";\n"
"border : none;\n"
"        "))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.m2Pos = QtGui.QLabel(self.m2Frame)
        self.m2Pos.setGeometry(QtCore.QRect(170, 10, 51, 17))
        self.m2Pos.setStyleSheet(_fromUtf8("font: 63 14pt \"KacstArt\";\n"
"border : none;\n"
"        "))
        self.m2Pos.setObjectName(_fromUtf8("m2Pos"))
        self.m11 = QtGui.QLabel(self.m2Frame)
        self.m11.setGeometry(QtCore.QRect(270, 0, 21, 31))
        self.m11.setStyleSheet(_fromUtf8("font: 63 14pt \"KacstArt\";\n"
"border : none;\n"
""))
        self.m11.setObjectName(_fromUtf8("m11"))
        self.m11Pos = QtGui.QLabel(self.m2Frame)
        self.m11Pos.setGeometry(QtCore.QRect(430, 10, 51, 17))
        self.m11Pos.setStyleSheet(_fromUtf8("font: 63 14pt \"KacstArt\";\n"
"border : none;\n"
"        "))
        self.m11Pos.setObjectName(_fromUtf8("m11Pos"))
        self.m11Ang = QtGui.QLabel(self.m2Frame)
        self.m11Ang.setGeometry(QtCore.QRect(340, 10, 51, 17))
        self.m11Ang.setStyleSheet(_fromUtf8("font: 63 14pt \"KacstArt\";\n"
"border : none;\n"
"        "))
        self.m11Ang.setObjectName(_fromUtf8("m11Ang"))
        self.m3Frame = QtGui.QFrame(self.mPageMFrame)
        self.m3Frame.setGeometry(QtCore.QRect(20, 150, 501, 31))
        self.m3Frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.m3Frame.setFrameShadow(QtGui.QFrame.Raised)
        self.m3Frame.setObjectName(_fromUtf8("m3Frame"))
        self.m3Ang = QtGui.QLabel(self.m3Frame)
        self.m3Ang.setGeometry(QtCore.QRect(70, 10, 51, 17))
        self.m3Ang.setStyleSheet(_fromUtf8("font: 63 14pt \"KacstArt\";\n"
"border : none;\n"
"        "))
        self.m3Ang.setObjectName(_fromUtf8("m3Ang"))
        self.m3Pos = QtGui.QLabel(self.m3Frame)
        self.m3Pos.setGeometry(QtCore.QRect(170, 10, 51, 17))
        self.m3Pos.setStyleSheet(_fromUtf8("font: 63 14pt \"KacstArt\";\n"
"border : none;\n"
"        "))
        self.m3Pos.setObjectName(_fromUtf8("m3Pos"))
        self.label_8 = QtGui.QLabel(self.m3Frame)
        self.label_8.setGeometry(QtCore.QRect(270, 50, 51, 17))
        self.label_8.setStyleSheet(_fromUtf8("font: 63 14pt \"KacstArt\";\n"
"border : none;\n"
"        "))
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.m3 = QtGui.QLabel(self.m3Frame)
        self.m3.setGeometry(QtCore.QRect(10, 0, 21, 31))
        self.m3.setStyleSheet(_fromUtf8("font: 63 14pt \"KacstArt\";\n"
"border : none;\n"
""))
        self.m3.setObjectName(_fromUtf8("m3"))
        self.m12 = QtGui.QLabel(self.m3Frame)
        self.m12.setGeometry(QtCore.QRect(270, 0, 31, 31))
        self.m12.setStyleSheet(_fromUtf8("font: 63 14pt \"KacstArt\";\n"
"border : none;\n"
""))
        self.m12.setObjectName(_fromUtf8("m12"))
        self.m12Pos = QtGui.QLabel(self.m3Frame)
        self.m12Pos.setGeometry(QtCore.QRect(430, 10, 51, 17))
        self.m12Pos.setStyleSheet(_fromUtf8("font: 63 14pt \"KacstArt\";\n"
"border : none;\n"
"        "))
        self.m12Pos.setObjectName(_fromUtf8("m12Pos"))
        self.m12Ang = QtGui.QLabel(self.m3Frame)
        self.m12Ang.setGeometry(QtCore.QRect(340, 10, 51, 17))
        self.m12Ang.setStyleSheet(_fromUtf8("font: 63 14pt \"KacstArt\";\n"
"border : none;\n"
"        "))
        self.m12Ang.setObjectName(_fromUtf8("m12Ang"))
        self.m4Frame = QtGui.QFrame(self.mPageMFrame)
        self.m4Frame.setGeometry(QtCore.QRect(20, 200, 501, 31))
        self.m4Frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.m4Frame.setFrameShadow(QtGui.QFrame.Raised)
        self.m4Frame.setObjectName(_fromUtf8("m4Frame"))
        self.m4Ang = QtGui.QLabel(self.m4Frame)
        self.m4Ang.setGeometry(QtCore.QRect(70, 10, 51, 17))
        self.m4Ang.setStyleSheet(_fromUtf8("font: 63 14pt \"KacstArt\";\n"
"border : none;\n"
"        "))
        self.m4Ang.setObjectName(_fromUtf8("m4Ang"))
        self.m4Pos = QtGui.QLabel(self.m4Frame)
        self.m4Pos.setGeometry(QtCore.QRect(170, 10, 51, 17))
        self.m4Pos.setStyleSheet(_fromUtf8("font: 63 14pt \"KacstArt\";\n"
"border : none;\n"
"        "))
        self.m4Pos.setObjectName(_fromUtf8("m4Pos"))
        self.m4 = QtGui.QLabel(self.m4Frame)
        self.m4.setGeometry(QtCore.QRect(10, 0, 21, 31))
        self.m4.setStyleSheet(_fromUtf8("font: 63 14pt \"KacstArt\";\n"
"border : none;\n"
""))
        self.m4.setObjectName(_fromUtf8("m4"))
        self.m13 = QtGui.QLabel(self.m4Frame)
        self.m13.setGeometry(QtCore.QRect(270, 0, 31, 31))
        self.m13.setStyleSheet(_fromUtf8("font: 63 14pt \"KacstArt\";\n"
"border : none;\n"
""))
        self.m13.setObjectName(_fromUtf8("m13"))
        self.m13Pos = QtGui.QLabel(self.m4Frame)
        self.m13Pos.setGeometry(QtCore.QRect(430, 10, 51, 17))
        self.m13Pos.setStyleSheet(_fromUtf8("font: 63 14pt \"KacstArt\";\n"
"border : none;\n"
"        "))
        self.m13Pos.setObjectName(_fromUtf8("m13Pos"))
        self.m13Ang = QtGui.QLabel(self.m4Frame)
        self.m13Ang.setGeometry(QtCore.QRect(340, 10, 51, 17))
        self.m13Ang.setStyleSheet(_fromUtf8("font: 63 14pt \"KacstArt\";\n"
"border : none;\n"
"        "))
        self.m13Ang.setObjectName(_fromUtf8("m13Ang"))
        self.m5Frame = QtGui.QFrame(self.mPageMFrame)
        self.m5Frame.setGeometry(QtCore.QRect(20, 250, 501, 31))
        self.m5Frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.m5Frame.setFrameShadow(QtGui.QFrame.Raised)
        self.m5Frame.setObjectName(_fromUtf8("m5Frame"))
        self.m5 = QtGui.QLabel(self.m5Frame)
        self.m5.setGeometry(QtCore.QRect(10, 0, 16, 31))
        self.m5.setStyleSheet(_fromUtf8("font: 63 14pt \"KacstArt\";\n"
"border : none;\n"
""))
        self.m5.setObjectName(_fromUtf8("m5"))
        self.m5Ang = QtGui.QLabel(self.m5Frame)
        self.m5Ang.setGeometry(QtCore.QRect(70, 10, 51, 17))
        self.m5Ang.setStyleSheet(_fromUtf8("font: 63 14pt \"KacstArt\";\n"
"border : none;\n"
"        "))
        self.m5Ang.setObjectName(_fromUtf8("m5Ang"))
        self.m5Pos = QtGui.QLabel(self.m5Frame)
        self.m5Pos.setGeometry(QtCore.QRect(170, 10, 51, 17))
        self.m5Pos.setStyleSheet(_fromUtf8("font: 63 14pt \"KacstArt\";\n"
"border : none;\n"
"        "))
        self.m5Pos.setObjectName(_fromUtf8("m5Pos"))
        self.m14 = QtGui.QLabel(self.m5Frame)
        self.m14.setGeometry(QtCore.QRect(270, 0, 31, 31))
        self.m14.setStyleSheet(_fromUtf8("font: 63 14pt \"KacstArt\";\n"
"border : none;\n"
""))
        self.m14.setObjectName(_fromUtf8("m14"))
        self.m14Pos = QtGui.QLabel(self.m5Frame)
        self.m14Pos.setGeometry(QtCore.QRect(430, 10, 51, 17))
        self.m14Pos.setStyleSheet(_fromUtf8("font: 63 14pt \"KacstArt\";\n"
"border : none;\n"
"        "))
        self.m14Pos.setObjectName(_fromUtf8("m14Pos"))
        self.m14Ang = QtGui.QLabel(self.m5Frame)
        self.m14Ang.setGeometry(QtCore.QRect(340, 10, 51, 17))
        self.m14Ang.setStyleSheet(_fromUtf8("font: 63 14pt \"KacstArt\";\n"
"border : none;\n"
"        "))
        self.m14Ang.setObjectName(_fromUtf8("m14Ang"))
        self.m6Frame = QtGui.QFrame(self.mPageMFrame)
        self.m6Frame.setGeometry(QtCore.QRect(20, 300, 501, 31))
        self.m6Frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.m6Frame.setFrameShadow(QtGui.QFrame.Raised)
        self.m6Frame.setObjectName(_fromUtf8("m6Frame"))
        self.m6 = QtGui.QLabel(self.m6Frame)
        self.m6.setGeometry(QtCore.QRect(10, 0, 21, 31))
        self.m6.setStyleSheet(_fromUtf8("font: 63 14pt \"KacstArt\";\n"
"border : none;\n"
""))
        self.m6.setObjectName(_fromUtf8("m6"))
        self.m6Ang = QtGui.QLabel(self.m6Frame)
        self.m6Ang.setGeometry(QtCore.QRect(70, 10, 51, 17))
        self.m6Ang.setStyleSheet(_fromUtf8("font: 63 14pt \"KacstArt\";\n"
"border : none;\n"
"        "))
        self.m6Ang.setObjectName(_fromUtf8("m6Ang"))
        self.m6Pos = QtGui.QLabel(self.m6Frame)
        self.m6Pos.setGeometry(QtCore.QRect(170, 10, 51, 17))
        self.m6Pos.setStyleSheet(_fromUtf8("font: 63 14pt \"KacstArt\";\n"
"border : none;\n"
"        "))
        self.m6Pos.setObjectName(_fromUtf8("m6Pos"))
        self.m15 = QtGui.QLabel(self.m6Frame)
        self.m15.setGeometry(QtCore.QRect(270, 0, 31, 31))
        self.m15.setStyleSheet(_fromUtf8("font: 63 14pt \"KacstArt\";\n"
"border : none;\n"
""))
        self.m15.setObjectName(_fromUtf8("m15"))
        self.m15Pos = QtGui.QLabel(self.m6Frame)
        self.m15Pos.setGeometry(QtCore.QRect(430, 10, 51, 17))
        self.m15Pos.setStyleSheet(_fromUtf8("font: 63 14pt \"KacstArt\";\n"
"border : none;\n"
"        "))
        self.m15Pos.setObjectName(_fromUtf8("m15Pos"))
        self.m15Ang = QtGui.QLabel(self.m6Frame)
        self.m15Ang.setGeometry(QtCore.QRect(340, 10, 51, 17))
        self.m15Ang.setStyleSheet(_fromUtf8("font: 63 14pt \"KacstArt\";\n"
"border : none;\n"
"        "))
        self.m15Ang.setObjectName(_fromUtf8("m15Ang"))
        self.m7Frame = QtGui.QFrame(self.mPageMFrame)
        self.m7Frame.setGeometry(QtCore.QRect(20, 350, 501, 31))
        self.m7Frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.m7Frame.setFrameShadow(QtGui.QFrame.Raised)
        self.m7Frame.setObjectName(_fromUtf8("m7Frame"))
        self.m7 = QtGui.QLabel(self.m7Frame)
        self.m7.setGeometry(QtCore.QRect(10, 0, 16, 31))
        self.m7.setStyleSheet(_fromUtf8("font: 63 14pt \"KacstArt\";\n"
"border : none;\n"
""))
        self.m7.setObjectName(_fromUtf8("m7"))
        self.m7Ang = QtGui.QLabel(self.m7Frame)
        self.m7Ang.setGeometry(QtCore.QRect(70, 10, 51, 17))
        self.m7Ang.setStyleSheet(_fromUtf8("font: 63 14pt \"KacstArt\";\n"
"border : none;\n"
"        "))
        self.m7Ang.setObjectName(_fromUtf8("m7Ang"))
        self.m7Pos = QtGui.QLabel(self.m7Frame)
        self.m7Pos.setGeometry(QtCore.QRect(170, 10, 51, 17))
        self.m7Pos.setStyleSheet(_fromUtf8("font: 63 14pt \"KacstArt\";\n"
"border : none;\n"
"        "))
        self.m7Pos.setObjectName(_fromUtf8("m7Pos"))
        self.m16 = QtGui.QLabel(self.m7Frame)
        self.m16.setGeometry(QtCore.QRect(270, 0, 31, 31))
        self.m16.setStyleSheet(_fromUtf8("font: 63 14pt \"KacstArt\";\n"
"border : none;\n"
""))
        self.m16.setObjectName(_fromUtf8("m16"))
        self.m16Pos = QtGui.QLabel(self.m7Frame)
        self.m16Pos.setGeometry(QtCore.QRect(430, 10, 51, 17))
        self.m16Pos.setStyleSheet(_fromUtf8("font: 63 14pt \"KacstArt\";\n"
"border : none;\n"
"        "))
        self.m16Pos.setObjectName(_fromUtf8("m16Pos"))
        self.m16Ang = QtGui.QLabel(self.m7Frame)
        self.m16Ang.setGeometry(QtCore.QRect(340, 10, 51, 17))
        self.m16Ang.setStyleSheet(_fromUtf8("font: 63 14pt \"KacstArt\";\n"
"border : none;\n"
"        "))
        self.m16Ang.setObjectName(_fromUtf8("m16Ang"))
        self.m8Frame = QtGui.QFrame(self.mPageMFrame)
        self.m8Frame.setGeometry(QtCore.QRect(20, 400, 501, 31))
        self.m8Frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.m8Frame.setFrameShadow(QtGui.QFrame.Raised)
        self.m8Frame.setObjectName(_fromUtf8("m8Frame"))
        self.m8 = QtGui.QLabel(self.m8Frame)
        self.m8.setGeometry(QtCore.QRect(10, 0, 21, 31))
        self.m8.setStyleSheet(_fromUtf8("font: 63 14pt \"KacstArt\";\n"
"border : none;\n"
""))
        self.m8.setObjectName(_fromUtf8("m8"))
        self.m8Ang = QtGui.QLabel(self.m8Frame)
        self.m8Ang.setGeometry(QtCore.QRect(70, 10, 51, 17))
        self.m8Ang.setStyleSheet(_fromUtf8("font: 63 14pt \"KacstArt\";\n"
"border : none;\n"
"        "))
        self.m8Ang.setObjectName(_fromUtf8("m8Ang"))
        self.m8Pos = QtGui.QLabel(self.m8Frame)
        self.m8Pos.setGeometry(QtCore.QRect(170, 10, 51, 17))
        self.m8Pos.setStyleSheet(_fromUtf8("font: 63 14pt \"KacstArt\";\n"
"border : none;\n"
"        "))
        self.m8Pos.setObjectName(_fromUtf8("m8Pos"))
        self.m17 = QtGui.QLabel(self.m8Frame)
        self.m17.setGeometry(QtCore.QRect(270, 0, 31, 31))
        self.m17.setStyleSheet(_fromUtf8("font: 63 14pt \"KacstArt\";\n"
"border : none;\n"
""))
        self.m17.setObjectName(_fromUtf8("m17"))
        self.m17Pos = QtGui.QLabel(self.m8Frame)
        self.m17Pos.setGeometry(QtCore.QRect(430, 10, 51, 17))
        self.m17Pos.setStyleSheet(_fromUtf8("font: 63 14pt \"KacstArt\";\n"
"border : none;\n"
"        "))
        self.m17Pos.setObjectName(_fromUtf8("m17Pos"))
        self.m17Ang = QtGui.QLabel(self.m8Frame)
        self.m17Ang.setGeometry(QtCore.QRect(340, 10, 51, 17))
        self.m17Ang.setStyleSheet(_fromUtf8("font: 63 14pt \"KacstArt\";\n"
"border : none;\n"
"        "))
        self.m17Ang.setObjectName(_fromUtf8("m17Ang"))
        self.recSavedLabel = QtGui.QLabel(self.mPageMFrame)
        self.recSavedLabel.setGeometry(QtCore.QRect(280, 500, 151, 20))
        self.recSavedLabel.setStyleSheet(_fromUtf8("font: 63 14pt \"KacstArt\";\n"
"border : none;\n"
"\n"
""))
        self.recSavedLabel.setObjectName(_fromUtf8("recSavedLabel"))
        self.recNumLabel = QtGui.QLabel(self.mPageMFrame)
        self.recNumLabel.setGeometry(QtCore.QRect(450, 500, 16, 31))
        self.recNumLabel.setStyleSheet(_fromUtf8("font: 63 14pt \"KacstArt\";\n"
"border : none;\n"
""))
        self.recNumLabel.setObjectName(_fromUtf8("recNumLabel"))
        self.mUpdateBtn = QtGui.QPushButton(self.mPageMFrame)
        self.mUpdateBtn.setGeometry(QtCore.QRect(20, 490, 171, 31))
        self.mUpdateBtn.setAutoFillBackground(False)
        self.mUpdateBtn.setStyleSheet(_fromUtf8("QPushButton\n"
"{font: 63 14pt \"KacstArt\";\n"
"border : 2px solid black;\n"
"}\n"
"QPushButton:pressed\n"
"{    \n"
"    background-color : rgb(209,209,224);\n"
"}\n"
"\n"
"        "))
        self.mUpdateBtn.setAutoDefault(False)
        self.mUpdateBtn.setDefault(False)
        self.mUpdateBtn.setFlat(False)
        self.mUpdateBtn.setObjectName(_fromUtf8("mUpdateBtn"))
        self.m8Frame_2 = QtGui.QFrame(self.mPageMFrame)
        self.m8Frame_2.setGeometry(QtCore.QRect(20, 450, 501, 31))
        self.m8Frame_2.setFrameShape(QtGui.QFrame.StyledPanel)
        self.m8Frame_2.setFrameShadow(QtGui.QFrame.Raised)
        self.m8Frame_2.setObjectName(_fromUtf8("m8Frame_2"))
        self.m9 = QtGui.QLabel(self.m8Frame_2)
        self.m9.setGeometry(QtCore.QRect(10, 0, 21, 31))
        self.m9.setStyleSheet(_fromUtf8("font: 63 14pt \"KacstArt\";\n"
"border : none;\n"
""))
        self.m9.setObjectName(_fromUtf8("m9"))
        self.m9Ang = QtGui.QLabel(self.m8Frame_2)
        self.m9Ang.setGeometry(QtCore.QRect(70, 10, 51, 17))
        self.m9Ang.setStyleSheet(_fromUtf8("font: 63 14pt \"KacstArt\";\n"
"border : none;\n"
"        "))
        self.m9Ang.setObjectName(_fromUtf8("m9Ang"))
        self.m9Pos = QtGui.QLabel(self.m8Frame_2)
        self.m9Pos.setGeometry(QtCore.QRect(170, 10, 51, 17))
        self.m9Pos.setStyleSheet(_fromUtf8("font: 63 14pt \"KacstArt\";\n"
"border : none;\n"
"        "))
        self.m9Pos.setObjectName(_fromUtf8("m9Pos"))
        self.m18 = QtGui.QLabel(self.m8Frame_2)
        self.m18.setGeometry(QtCore.QRect(270, 0, 31, 31))
        self.m18.setStyleSheet(_fromUtf8("font: 63 14pt \"KacstArt\";\n"
"border : none;\n"
""))
        self.m18.setObjectName(_fromUtf8("m18"))
        self.m18Pos = QtGui.QLabel(self.m8Frame_2)
        self.m18Pos.setGeometry(QtCore.QRect(430, 10, 51, 17))
        self.m18Pos.setStyleSheet(_fromUtf8("font: 63 14pt \"KacstArt\";\n"
"border : none;\n"
"        "))
        self.m18Pos.setObjectName(_fromUtf8("m18Pos"))
        self.m18Ang = QtGui.QLabel(self.m8Frame_2)
        self.m18Ang.setGeometry(QtCore.QRect(340, 10, 51, 17))
        self.m18Ang.setStyleSheet(_fromUtf8("font: 63 14pt \"KacstArt\";\n"
"border : none;\n"
"        "))
        self.m18Ang.setObjectName(_fromUtf8("m18Ang"))
        self.mId_2 = QtGui.QLabel(self.mPageMFrame)
        self.mId_2.setGeometry(QtCore.QRect(290, 20, 31, 21))
        self.mId_2.setStyleSheet(_fromUtf8("font: 63 14pt \"KacstArt\";\n"
"border : none;\n"
""))
        self.mId_2.setObjectName(_fromUtf8("mId_2"))
        self.mAngle_2 = QtGui.QLabel(self.mPageMFrame)
        self.mAngle_2.setGeometry(QtCore.QRect(360, 20, 61, 21))
        self.mAngle_2.setStyleSheet(_fromUtf8("font: 63 14pt \"KacstArt\";\n"
"border : none;\n"
"\n"
""))
        self.mAngle_2.setObjectName(_fromUtf8("mAngle_2"))
        self.mPos_2 = QtGui.QLabel(self.mPageMFrame)
        self.mPos_2.setGeometry(QtCore.QRect(440, 20, 81, 21))
        self.mPos_2.setStyleSheet(_fromUtf8("font: 63 14pt \"KacstArt\";\n"
"border : none;\n"
"\n"
""))
        self.mPos_2.setObjectName(_fromUtf8("mPos_2"))
        self.mPageSFrame = QtGui.QFrame(self.mainPage)
        self.mPageSFrame.setGeometry(QtCore.QRect(560, 20, 231, 531))
        self.mPageSFrame.setStyleSheet(_fromUtf8("border : 1px solid rgb(113, 0, 0);\n"
""))
        self.mPageSFrame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.mPageSFrame.setFrameShadow(QtGui.QFrame.Raised)
        self.mPageSFrame.setObjectName(_fromUtf8("mPageSFrame"))
        self.inRecBtn = QtGui.QPushButton(self.mPageSFrame)
        self.inRecBtn.setGeometry(QtCore.QRect(30, 20, 171, 61))
        self.inRecBtn.setStyleSheet(_fromUtf8("QPushButton\n"
"{font: 63 14pt \"KacstArt\";\n"
"border : 2px solid black;\n"
"}\n"
"QPushButton:pressed\n"
"{    \n"
"    background-color : rgb(209,209,224);\n"
"}\n"
"\n"
"        "))
        self.inRecBtn.setObjectName(_fromUtf8("inRecBtn"))
        self.saveRecBtn = QtGui.QPushButton(self.mPageSFrame)
        self.saveRecBtn.setGeometry(QtCore.QRect(30, 150, 171, 61))
        self.saveRecBtn.setStyleSheet(_fromUtf8("QPushButton\n"
"{font: 63 14pt \"KacstArt\";\n"
"border : 2px solid black;\n"
"}\n"
"QPushButton:pressed\n"
"{    \n"
"    background-color : rgb(209,209,224);\n"
"}\n"
"\n"
"        "))
        self.saveRecBtn.setObjectName(_fromUtf8("saveRecBtn"))
        self.recNameInput = QtGui.QLineEdit(self.mPageSFrame)
        self.recNameInput.setGeometry(QtCore.QRect(30, 110, 171, 27))
        self.recNameInput.setObjectName(_fromUtf8("recNameInput"))
        self.saveStatusLabel = QtGui.QLabel(self.mPageSFrame)
        self.saveStatusLabel.setGeometry(QtCore.QRect(70, 230, 101, 21))
        self.saveStatusLabel.setStyleSheet(_fromUtf8("font: 63 14pt \"KacstArt\";\n"
"border : none;\n"
"\n"
""))
        self.saveStatusLabel.setObjectName(_fromUtf8("saveStatusLabel"))
        self.newRecBtn = QtGui.QPushButton(self.mPageSFrame)
        self.newRecBtn.setGeometry(QtCore.QRect(30, 430, 171, 61))
        self.newRecBtn.setStyleSheet(_fromUtf8("QPushButton\n"
"{font: 63 14pt \"KacstArt\";\n"
"border : 2px solid black;\n"
"}\n"
"QPushButton:pressed\n"
"{    \n"
"    background-color : rgb(209,209,224);\n"
"}\n"
"\n"
"        "))
        self.newRecBtn.setObjectName(_fromUtf8("newRecBtn"))
        self.mSelect = QtGui.QComboBox(self.mPageSFrame)
        self.mSelect.setGeometry(QtCore.QRect(30, 280, 171, 27))
        self.mSelect.setObjectName(_fromUtf8("mSelect"))
        self.mSelect.addItem(_fromUtf8(""))
        self.mSelect.addItem(_fromUtf8(""))
        self.mSelect.addItem(_fromUtf8(""))
        self.mSelect.addItem(_fromUtf8(""))
        self.mSelect.addItem(_fromUtf8(""))
        self.mSelect.addItem(_fromUtf8(""))
        self.mSelect.addItem(_fromUtf8(""))
        self.mSelect.addItem(_fromUtf8(""))
        self.mSelect.addItem(_fromUtf8(""))
        self.mSelect.addItem(_fromUtf8(""))
        self.mSelect.addItem(_fromUtf8(""))
        self.mSelect.addItem(_fromUtf8(""))
        self.mSelect.addItem(_fromUtf8(""))
        self.mSelect.addItem(_fromUtf8(""))
        self.mSelect.addItem(_fromUtf8(""))
        self.mSelect.addItem(_fromUtf8(""))
        self.mSelect.addItem(_fromUtf8(""))
        self.mSelect.addItem(_fromUtf8(""))
        self.mGoBtn = QtGui.QPushButton(self.mPageSFrame)
        self.mGoBtn.setGeometry(QtCore.QRect(30, 320, 171, 31))
        self.mGoBtn.setStyleSheet(_fromUtf8("QPushButton\n"
"{font: 63 14pt \"KacstArt\";\n"
"border : 2px solid black;\n"
"}\n"
"QPushButton:pressed\n"
"{    \n"
"    background-color : rgb(209,209,224);\n"
"}\n"
"\n"
"        "))
        self.mGoBtn.setObjectName(_fromUtf8("mGoBtn"))
        self.stackedWidget.addWidget(self.mainPage)
        self.m1Page = QtGui.QWidget()
        self.m1Page.setObjectName(_fromUtf8("m1Page"))
        self.m1Label = QtGui.QLabel(self.m1Page)
        self.m1Label.setGeometry(QtCore.QRect(340, 10, 91, 21))
        self.m1Label.setStyleSheet(_fromUtf8("font: 63 16pt \"KacstArt\";\n"
"border : none;"))
        self.m1Label.setObjectName(_fromUtf8("m1Label"))
        self.m1SFrame = QtGui.QFrame(self.m1Page)
        self.m1SFrame.setGeometry(QtCore.QRect(10, 40, 561, 501))
        self.m1SFrame.setStyleSheet(_fromUtf8("border : 1px solid rgb(113, 0, 0);\n"
""))
        self.m1SFrame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.m1SFrame.setFrameShadow(QtGui.QFrame.Raised)
        self.m1SFrame.setObjectName(_fromUtf8("m1SFrame"))
        self.m1AngLabel = QtGui.QLabel(self.m1SFrame)
        self.m1AngLabel.setGeometry(QtCore.QRect(120, 40, 61, 21))
        self.m1AngLabel.setStyleSheet(_fromUtf8("font: 63 16pt \"KacstArt\";\n"
"border : none;"))
        self.m1AngLabel.setObjectName(_fromUtf8("m1AngLabel"))
        self.m1PosLabel = QtGui.QLabel(self.m1SFrame)
        self.m1PosLabel.setGeometry(QtCore.QRect(390, 40, 91, 21))
        self.m1PosLabel.setStyleSheet(_fromUtf8("font: 63 16pt \"KacstArt\";\n"
"border : none;"))
        self.m1PosLabel.setObjectName(_fromUtf8("m1PosLabel"))
        self.m1TorqueLabel = QtGui.QLabel(self.m1SFrame)
        self.m1TorqueLabel.setGeometry(QtCore.QRect(80, 270, 141, 21))
        self.m1TorqueLabel.setStyleSheet(_fromUtf8("font: 63 16pt \"KacstArt\";\n"
"border : none;"))
        self.m1TorqueLabel.setObjectName(_fromUtf8("m1TorqueLabel"))
        self.m1TempLabel = QtGui.QLabel(self.m1SFrame)
        self.m1TempLabel.setGeometry(QtCore.QRect(370, 270, 131, 21))
        self.m1TempLabel.setStyleSheet(_fromUtf8("font: 63 16pt \"KacstArt\";\n"
"border : none;"))
        self.m1TempLabel.setObjectName(_fromUtf8("m1TempLabel"))
        self.m1ErrLabel = QtGui.QLabel(self.m1SFrame)
        self.m1ErrLabel.setGeometry(QtCore.QRect(260, 390, 61, 21))
        self.m1ErrLabel.setStyleSheet(_fromUtf8("font: 63 16pt \"KacstArt\";\n"
"border : none;"))
        self.m1ErrLabel.setObjectName(_fromUtf8("m1ErrLabel"))
        self.m1AngDial = QtGui.QDial(self.m1SFrame)
        self.m1AngDial.setGeometry(QtCore.QRect(100, 80, 91, 81))
        self.m1AngDial.setMinimum(-150)
        self.m1AngDial.setMaximum(150)
        self.m1AngDial.setTracking(True)
        self.m1AngDial.setWrapping(False)
        self.m1AngDial.setNotchTarget(50.0)
        self.m1AngDial.setNotchesVisible(True)
        self.m1AngDial.setObjectName(_fromUtf8("m1AngDial"))
        self.m1PosDial = QtGui.QDial(self.m1SFrame)
        self.m1PosDial.setGeometry(QtCore.QRect(380, 80, 91, 81))
        self.m1PosDial.setMinimum(0)
        self.m1PosDial.setMaximum(1023)
        self.m1PosDial.setTracking(True)
        self.m1PosDial.setWrapping(False)
        self.m1PosDial.setNotchTarget(100.0)
        self.m1PosDial.setNotchesVisible(True)
        self.m1PosDial.setObjectName(_fromUtf8("m1PosDial"))
        self.m1AngNum = QtGui.QLabel(self.m1SFrame)
        self.m1AngNum.setGeometry(QtCore.QRect(120, 200, 61, 21))
        self.m1AngNum.setStyleSheet(_fromUtf8("font: 63 16pt \"KacstArt\";\n"
"border : none;"))
        self.m1AngNum.setObjectName(_fromUtf8("m1AngNum"))
        self.m1PosNum = QtGui.QLabel(self.m1SFrame)
        self.m1PosNum.setGeometry(QtCore.QRect(400, 200, 61, 21))
        self.m1PosNum.setStyleSheet(_fromUtf8("font: 63 16pt \"KacstArt\";\n"
"border : none;"))
        self.m1PosNum.setObjectName(_fromUtf8("m1PosNum"))
        self.m1TorqueNum = QtGui.QLabel(self.m1SFrame)
        self.m1TorqueNum.setGeometry(QtCore.QRect(120, 320, 61, 21))
        self.m1TorqueNum.setStyleSheet(_fromUtf8("font: 63 16pt \"KacstArt\";\n"
"border : none;"))
        self.m1TorqueNum.setObjectName(_fromUtf8("m1TorqueNum"))
        self.m1ErrNum = QtGui.QLabel(self.m1SFrame)
        self.m1ErrNum.setGeometry(QtCore.QRect(260, 440, 61, 21))
        self.m1ErrNum.setStyleSheet(_fromUtf8("font: 63 16pt \"KacstArt\";\n"
"border : none;"))
        self.m1ErrNum.setObjectName(_fromUtf8("m1ErrNum"))
        self.m1TempNum = QtGui.QLabel(self.m1SFrame)
        self.m1TempNum.setGeometry(QtCore.QRect(400, 320, 61, 21))
        self.m1TempNum.setStyleSheet(_fromUtf8("font: 63 16pt \"KacstArt\";\n"
"border : none;"))
        self.m1TempNum.setObjectName(_fromUtf8("m1TempNum"))
        self.m1CFrame = QtGui.QFrame(self.m1Page)
        self.m1CFrame.setGeometry(QtCore.QRect(580, 40, 211, 501))
        self.m1CFrame.setStyleSheet(_fromUtf8("border : 1px solid rgb(113, 0, 0);\n"
""))
        self.m1CFrame.setObjectName(_fromUtf8("m1CFrame"))
        self.m1GoalTSpin = QtGui.QSpinBox(self.m1CFrame)
        self.m1GoalTSpin.setGeometry(QtCore.QRect(30, 40, 151, 21))
        self.m1GoalTSpin.setStyleSheet(_fromUtf8("font: 63 13pt \"KacstArt\";"))
        self.m1GoalTSpin.setWrapping(False)
        self.m1GoalTSpin.setAccelerated(False)
        self.m1GoalTSpin.setObjectName(_fromUtf8("m1GoalTSpin"))
        self.m1GoalTLabel = QtGui.QLabel(self.m1CFrame)
        self.m1GoalTLabel.setGeometry(QtCore.QRect(60, 10, 111, 21))
        self.m1GoalTLabel.setStyleSheet(_fromUtf8("font: 63 14pt \"KacstArt\";\n"
"border : none;"))
        self.m1GoalTLabel.setObjectName(_fromUtf8("m1GoalTLabel"))
        self.m1UpdateBtn = QtGui.QPushButton(self.m1CFrame)
        self.m1UpdateBtn.setGeometry(QtCore.QRect(20, 290, 171, 41))
        self.m1UpdateBtn.setAutoFillBackground(False)
        self.m1UpdateBtn.setStyleSheet(_fromUtf8("QPushButton\n"
"{font: 63 14pt \"KacstArt\";\n"
"border : 2px solid black;\n"
"}\n"
"QPushButton:pressed\n"
"{    \n"
"    background-color : rgb(209,209,224);\n"
"}\n"
"\n"
"        "))
        self.m1UpdateBtn.setAutoDefault(False)
        self.m1UpdateBtn.setDefault(False)
        self.m1UpdateBtn.setFlat(False)
        self.m1UpdateBtn.setObjectName(_fromUtf8("m1UpdateBtn"))
        self.m1AngleLabel = QtGui.QLabel(self.m1CFrame)
        self.m1AngleLabel.setGeometry(QtCore.QRect(80, 70, 61, 21))
        self.m1AngleLabel.setStyleSheet(_fromUtf8("font: 63 14pt \"KacstArt\";\n"
"border : none;"))
        self.m1AngleLabel.setObjectName(_fromUtf8("m1AngleLabel"))
        self.m1AngleSpin = QtGui.QSpinBox(self.m1CFrame)
        self.m1AngleSpin.setGeometry(QtCore.QRect(30, 100, 151, 21))
        self.m1AngleSpin.setStyleSheet(_fromUtf8("font: 63 13pt \"KacstArt\";"))
        self.m1AngleSpin.setWrapping(False)
        self.m1AngleSpin.setAccelerated(False)
        self.m1AngleSpin.setMinimum(-150)
        self.m1AngleSpin.setMaximum(150)
        self.m1AngleSpin.setObjectName(_fromUtf8("m1AngleSpin"))
        self.m1PositionSpin = QtGui.QSpinBox(self.m1CFrame)
        self.m1PositionSpin.setGeometry(QtCore.QRect(30, 190, 151, 21))
        self.m1PositionSpin.setStyleSheet(_fromUtf8("font: 63 13pt \"KacstArt\";"))
        self.m1PositionSpin.setWrapping(False)
        self.m1PositionSpin.setAccelerated(False)
        self.m1PositionSpin.setMaximum(1023)
        self.m1PositionSpin.setObjectName(_fromUtf8("m1PositionSpin"))
        self.m1PositionLabel = QtGui.QLabel(self.m1CFrame)
        self.m1PositionLabel.setGeometry(QtCore.QRect(70, 170, 81, 21))
        self.m1PositionLabel.setStyleSheet(_fromUtf8("font: 63 14pt \"KacstArt\";\n"
"border : none;"))
        self.m1PositionLabel.setObjectName(_fromUtf8("m1PositionLabel"))
        self.m1AngleBtn = QtGui.QPushButton(self.m1CFrame)
        self.m1AngleBtn.setGeometry(QtCore.QRect(30, 130, 151, 21))
        self.m1AngleBtn.setStyleSheet(_fromUtf8("QPushButton\n"
"{font: 63 12pt \"KacstArt\";\n"
"border : 2px solid black;\n"
"}\n"
"QPushButton:pressed\n"
"{    \n"
"    background-color : rgb(209,209,224);\n"
"}\n"
"\n"
"        "))
        self.m1AngleBtn.setObjectName(_fromUtf8("m1AngleBtn"))
        self.m1PositionBtn = QtGui.QPushButton(self.m1CFrame)
        self.m1PositionBtn.setGeometry(QtCore.QRect(30, 220, 151, 21))
        self.m1PositionBtn.setStyleSheet(_fromUtf8("QPushButton\n"
"{font: 63 12pt \"KacstArt\";\n"
"border : 2px solid black;\n"
"}\n"
"QPushButton:pressed\n"
"{    \n"
"    background-color : rgb(209,209,224);\n"
"}\n"
"\n"
"        "))
        self.m1PositionBtn.setObjectName(_fromUtf8("m1PositionBtn"))
        self.m1HomeBtn = QtGui.QPushButton(self.m1CFrame)
        self.m1HomeBtn.setGeometry(QtCore.QRect(20, 370, 171, 61))
        self.m1HomeBtn.setStyleSheet(_fromUtf8("QPushButton\n"
"{font: 63 14pt \"KacstArt\";\n"
"border : 2px solid black;\n"
"}\n"
"QPushButton:pressed\n"
"{    \n"
"    background-color : rgb(209,209,224);\n"
"}\n"
"\n"
"        "))
        self.m1HomeBtn.setObjectName(_fromUtf8("m1HomeBtn"))
        self.stackedWidget.addWidget(self.m1Page)
        self.m2Page = QtGui.QWidget()
        self.m2Page.setObjectName(_fromUtf8("m2Page"))
        self.m2SFrame = QtGui.QFrame(self.m2Page)
        self.m2SFrame.setGeometry(QtCore.QRect(10, 40, 561, 501))
        self.m2SFrame.setStyleSheet(_fromUtf8("border : 1px solid rgb(113, 0, 0);\n"
""))
        self.m2SFrame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.m2SFrame.setFrameShadow(QtGui.QFrame.Raised)
        self.m2SFrame.setObjectName(_fromUtf8("m2SFrame"))
        self.m2AngLabel = QtGui.QLabel(self.m2SFrame)
        self.m2AngLabel.setGeometry(QtCore.QRect(120, 40, 61, 21))
        self.m2AngLabel.setStyleSheet(_fromUtf8("font: 63 16pt \"KacstArt\";\n"
"border : none;"))
        self.m2AngLabel.setObjectName(_fromUtf8("m2AngLabel"))
        self.m2PosLabel = QtGui.QLabel(self.m2SFrame)
        self.m2PosLabel.setGeometry(QtCore.QRect(390, 40, 91, 21))
        self.m2PosLabel.setStyleSheet(_fromUtf8("font: 63 16pt \"KacstArt\";\n"
"border : none;"))
        self.m2PosLabel.setObjectName(_fromUtf8("m2PosLabel"))
        self.m2TorqueLabel = QtGui.QLabel(self.m2SFrame)
        self.m2TorqueLabel.setGeometry(QtCore.QRect(80, 270, 141, 21))
        self.m2TorqueLabel.setStyleSheet(_fromUtf8("font: 63 16pt \"KacstArt\";\n"
"border : none;"))
        self.m2TorqueLabel.setObjectName(_fromUtf8("m2TorqueLabel"))
        self.m2TempLabel = QtGui.QLabel(self.m2SFrame)
        self.m2TempLabel.setGeometry(QtCore.QRect(370, 270, 131, 21))
        self.m2TempLabel.setStyleSheet(_fromUtf8("font: 63 16pt \"KacstArt\";\n"
"border : none;"))
        self.m2TempLabel.setObjectName(_fromUtf8("m2TempLabel"))
        self.m2ErrLabel = QtGui.QLabel(self.m2SFrame)
        self.m2ErrLabel.setGeometry(QtCore.QRect(260, 390, 61, 21))
        self.m2ErrLabel.setStyleSheet(_fromUtf8("font: 63 16pt \"KacstArt\";\n"
"border : none;"))
        self.m2ErrLabel.setObjectName(_fromUtf8("m2ErrLabel"))
        self.m2AngDial = QtGui.QDial(self.m2SFrame)
        self.m2AngDial.setGeometry(QtCore.QRect(100, 80, 91, 81))
        self.m2AngDial.setMinimum(-150)
        self.m2AngDial.setMaximum(150)
        self.m2AngDial.setTracking(True)
        self.m2AngDial.setWrapping(False)
        self.m2AngDial.setNotchTarget(50.0)
        self.m2AngDial.setNotchesVisible(True)
        self.m2AngDial.setObjectName(_fromUtf8("m2AngDial"))
        self.m2PosDial = QtGui.QDial(self.m2SFrame)
        self.m2PosDial.setGeometry(QtCore.QRect(380, 80, 91, 81))
        self.m2PosDial.setMinimum(0)
        self.m2PosDial.setMaximum(1023)
        self.m2PosDial.setTracking(True)
        self.m2PosDial.setWrapping(False)
        self.m2PosDial.setNotchTarget(100.0)
        self.m2PosDial.setNotchesVisible(True)
        self.m2PosDial.setObjectName(_fromUtf8("m2PosDial"))
        self.m2AngNum = QtGui.QLabel(self.m2SFrame)
        self.m2AngNum.setGeometry(QtCore.QRect(120, 200, 61, 21))
        self.m2AngNum.setStyleSheet(_fromUtf8("font: 63 16pt \"KacstArt\";\n"
"border : none;"))
        self.m2AngNum.setObjectName(_fromUtf8("m2AngNum"))
        self.m2PosNum = QtGui.QLabel(self.m2SFrame)
        self.m2PosNum.setGeometry(QtCore.QRect(400, 200, 61, 21))
        self.m2PosNum.setStyleSheet(_fromUtf8("font: 63 16pt \"KacstArt\";\n"
"border : none;"))
        self.m2PosNum.setObjectName(_fromUtf8("m2PosNum"))
        self.m2TorqueNum = QtGui.QLabel(self.m2SFrame)
        self.m2TorqueNum.setGeometry(QtCore.QRect(120, 320, 61, 21))
        self.m2TorqueNum.setStyleSheet(_fromUtf8("font: 63 16pt \"KacstArt\";\n"
"border : none;"))
        self.m2TorqueNum.setObjectName(_fromUtf8("m2TorqueNum"))
        self.m2ErrNum = QtGui.QLabel(self.m2SFrame)
        self.m2ErrNum.setGeometry(QtCore.QRect(260, 440, 61, 21))
        self.m2ErrNum.setStyleSheet(_fromUtf8("font: 63 16pt \"KacstArt\";\n"
"border : none;"))
        self.m2ErrNum.setObjectName(_fromUtf8("m2ErrNum"))
        self.m2TempNum = QtGui.QLabel(self.m2SFrame)
        self.m2TempNum.setGeometry(QtCore.QRect(400, 320, 61, 21))
        self.m2TempNum.setStyleSheet(_fromUtf8("font: 63 16pt \"KacstArt\";\n"
"border : none;"))
        self.m2TempNum.setObjectName(_fromUtf8("m2TempNum"))
        self.m2CFrame = QtGui.QFrame(self.m2Page)
        self.m2CFrame.setGeometry(QtCore.QRect(580, 40, 211, 501))
        self.m2CFrame.setStyleSheet(_fromUtf8("border : 1px solid rgb(113, 0, 0);\n"
""))
        self.m2CFrame.setObjectName(_fromUtf8("m2CFrame"))
        self.m2GoalTSpin = QtGui.QSpinBox(self.m2CFrame)
        self.m2GoalTSpin.setGeometry(QtCore.QRect(30, 40, 151, 21))
        self.m2GoalTSpin.setStyleSheet(_fromUtf8("font: 63 13pt \"KacstArt\";"))
        self.m2GoalTSpin.setWrapping(False)
        self.m2GoalTSpin.setAccelerated(False)
        self.m2GoalTSpin.setObjectName(_fromUtf8("m2GoalTSpin"))
        self.m2GoalTLabel = QtGui.QLabel(self.m2CFrame)
        self.m2GoalTLabel.setGeometry(QtCore.QRect(60, 10, 111, 21))
        self.m2GoalTLabel.setStyleSheet(_fromUtf8("font: 63 14pt \"KacstArt\";\n"
"border : none;"))
        self.m2GoalTLabel.setObjectName(_fromUtf8("m2GoalTLabel"))
        self.m2UpdateBtn = QtGui.QPushButton(self.m2CFrame)
        self.m2UpdateBtn.setGeometry(QtCore.QRect(20, 290, 171, 41))
        self.m2UpdateBtn.setAutoFillBackground(False)
        self.m2UpdateBtn.setStyleSheet(_fromUtf8("QPushButton\n"
"{font: 63 14pt \"KacstArt\";\n"
"border : 2px solid black;\n"
"}\n"
"QPushButton:pressed\n"
"{    \n"
"    background-color : rgb(209,209,224);\n"
"}\n"
"\n"
"        "))
        self.m2UpdateBtn.setAutoDefault(False)
        self.m2UpdateBtn.setDefault(False)
        self.m2UpdateBtn.setFlat(False)
        self.m2UpdateBtn.setObjectName(_fromUtf8("m2UpdateBtn"))
        self.m2AngleLabel = QtGui.QLabel(self.m2CFrame)
        self.m2AngleLabel.setGeometry(QtCore.QRect(80, 70, 61, 21))
        self.m2AngleLabel.setStyleSheet(_fromUtf8("font: 63 14pt \"KacstArt\";\n"
"border : none;"))
        self.m2AngleLabel.setObjectName(_fromUtf8("m2AngleLabel"))
        self.m2AngleSpin = QtGui.QSpinBox(self.m2CFrame)
        self.m2AngleSpin.setGeometry(QtCore.QRect(30, 100, 151, 21))
        self.m2AngleSpin.setStyleSheet(_fromUtf8("font: 63 13pt \"KacstArt\";"))
        self.m2AngleSpin.setWrapping(False)
        self.m2AngleSpin.setAccelerated(False)
        self.m2AngleSpin.setMinimum(-150)
        self.m2AngleSpin.setMaximum(150)
        self.m2AngleSpin.setObjectName(_fromUtf8("m2AngleSpin"))
        self.m2PositionSpin = QtGui.QSpinBox(self.m2CFrame)
        self.m2PositionSpin.setGeometry(QtCore.QRect(30, 190, 151, 21))
        self.m2PositionSpin.setStyleSheet(_fromUtf8("font: 63 13pt \"KacstArt\";"))
        self.m2PositionSpin.setWrapping(False)
        self.m2PositionSpin.setAccelerated(False)
        self.m2PositionSpin.setMaximum(1023)
        self.m2PositionSpin.setObjectName(_fromUtf8("m2PositionSpin"))
        self.m2PositionLabel = QtGui.QLabel(self.m2CFrame)
        self.m2PositionLabel.setGeometry(QtCore.QRect(70, 170, 81, 21))
        self.m2PositionLabel.setStyleSheet(_fromUtf8("font: 63 14pt \"KacstArt\";\n"
"border : none;"))
        self.m2PositionLabel.setObjectName(_fromUtf8("m2PositionLabel"))
        self.m2AngleBtn = QtGui.QPushButton(self.m2CFrame)
        self.m2AngleBtn.setGeometry(QtCore.QRect(30, 130, 151, 21))
        self.m2AngleBtn.setStyleSheet(_fromUtf8("QPushButton\n"
"{font: 63 12pt \"KacstArt\";\n"
"border : 2px solid black;\n"
"}\n"
"QPushButton:pressed\n"
"{    \n"
"    background-color : rgb(209,209,224);\n"
"}\n"
"\n"
"        "))
        self.m2AngleBtn.setObjectName(_fromUtf8("m2AngleBtn"))
        self.m2PositionBtn = QtGui.QPushButton(self.m2CFrame)
        self.m2PositionBtn.setGeometry(QtCore.QRect(30, 220, 151, 21))
        self.m2PositionBtn.setStyleSheet(_fromUtf8("QPushButton\n"
"{font: 63 12pt \"KacstArt\";\n"
"border : 2px solid black;\n"
"}\n"
"QPushButton:pressed\n"
"{    \n"
"    background-color : rgb(209,209,224);\n"
"}\n"
"\n"
"        "))
        self.m2PositionBtn.setObjectName(_fromUtf8("m2PositionBtn"))
        self.m2HomeBtn = QtGui.QPushButton(self.m2CFrame)
        self.m2HomeBtn.setGeometry(QtCore.QRect(20, 370, 171, 61))
        self.m2HomeBtn.setStyleSheet(_fromUtf8("QPushButton\n"
"{font: 63 14pt \"KacstArt\";\n"
"border : 2px solid black;\n"
"}\n"
"QPushButton:pressed\n"
"{    \n"
"    background-color : rgb(209,209,224);\n"
"}\n"
"\n"
"        "))
        self.m2HomeBtn.setObjectName(_fromUtf8("m2HomeBtn"))
        self.m2Label = QtGui.QLabel(self.m2Page)
        self.m2Label.setGeometry(QtCore.QRect(340, 10, 91, 21))
        self.m2Label.setStyleSheet(_fromUtf8("font: 63 16pt \"KacstArt\";\n"
"border : none;"))
        self.m2Label.setObjectName(_fromUtf8("m2Label"))
        self.stackedWidget.addWidget(self.m2Page)
        self.m3Page = QtGui.QWidget()
        self.m3Page.setObjectName(_fromUtf8("m3Page"))
        self.m3SFrame = QtGui.QFrame(self.m3Page)
        self.m3SFrame.setGeometry(QtCore.QRect(10, 40, 561, 501))
        self.m3SFrame.setStyleSheet(_fromUtf8("border : 1px solid rgb(113, 0, 0);\n"
""))
        self.m3SFrame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.m3SFrame.setFrameShadow(QtGui.QFrame.Raised)
        self.m3SFrame.setObjectName(_fromUtf8("m3SFrame"))
        self.m3AngLabel = QtGui.QLabel(self.m3SFrame)
        self.m3AngLabel.setGeometry(QtCore.QRect(120, 40, 61, 21))
        self.m3AngLabel.setStyleSheet(_fromUtf8("font: 63 16pt \"KacstArt\";\n"
"border : none;"))
        self.m3AngLabel.setObjectName(_fromUtf8("m3AngLabel"))
        self.m3PosLabel = QtGui.QLabel(self.m3SFrame)
        self.m3PosLabel.setGeometry(QtCore.QRect(390, 40, 91, 21))
        self.m3PosLabel.setStyleSheet(_fromUtf8("font: 63 16pt \"KacstArt\";\n"
"border : none;"))
        self.m3PosLabel.setObjectName(_fromUtf8("m3PosLabel"))
        self.m3TorqueLabel = QtGui.QLabel(self.m3SFrame)
        self.m3TorqueLabel.setGeometry(QtCore.QRect(80, 270, 141, 21))
        self.m3TorqueLabel.setStyleSheet(_fromUtf8("font: 63 16pt \"KacstArt\";\n"
"border : none;"))
        self.m3TorqueLabel.setObjectName(_fromUtf8("m3TorqueLabel"))
        self.m3TempLabel = QtGui.QLabel(self.m3SFrame)
        self.m3TempLabel.setGeometry(QtCore.QRect(370, 270, 131, 21))
        self.m3TempLabel.setStyleSheet(_fromUtf8("font: 63 16pt \"KacstArt\";\n"
"border : none;"))
        self.m3TempLabel.setObjectName(_fromUtf8("m3TempLabel"))
        self.m3ErrLabel = QtGui.QLabel(self.m3SFrame)
        self.m3ErrLabel.setGeometry(QtCore.QRect(260, 390, 61, 21))
        self.m3ErrLabel.setStyleSheet(_fromUtf8("font: 63 16pt \"KacstArt\";\n"
"border : none;"))
        self.m3ErrLabel.setObjectName(_fromUtf8("m3ErrLabel"))
        self.m3AngDial = QtGui.QDial(self.m3SFrame)
        self.m3AngDial.setGeometry(QtCore.QRect(100, 80, 91, 81))
        self.m3AngDial.setMinimum(-150)
        self.m3AngDial.setMaximum(150)
        self.m3AngDial.setTracking(True)
        self.m3AngDial.setWrapping(False)
        self.m3AngDial.setNotchTarget(50.0)
        self.m3AngDial.setNotchesVisible(True)
        self.m3AngDial.setObjectName(_fromUtf8("m3AngDial"))
        self.m3PosDial = QtGui.QDial(self.m3SFrame)
        self.m3PosDial.setGeometry(QtCore.QRect(380, 80, 91, 81))
        self.m3PosDial.setMinimum(0)
        self.m3PosDial.setMaximum(1023)
        self.m3PosDial.setTracking(True)
        self.m3PosDial.setWrapping(False)
        self.m3PosDial.setNotchTarget(100.0)
        self.m3PosDial.setNotchesVisible(True)
        self.m3PosDial.setObjectName(_fromUtf8("m3PosDial"))
        self.m3AngNum = QtGui.QLabel(self.m3SFrame)
        self.m3AngNum.setGeometry(QtCore.QRect(120, 200, 61, 21))
        self.m3AngNum.setStyleSheet(_fromUtf8("font: 63 16pt \"KacstArt\";\n"
"border : none;"))
        self.m3AngNum.setObjectName(_fromUtf8("m3AngNum"))
        self.m3PosNum = QtGui.QLabel(self.m3SFrame)
        self.m3PosNum.setGeometry(QtCore.QRect(400, 200, 61, 21))
        self.m3PosNum.setStyleSheet(_fromUtf8("font: 63 16pt \"KacstArt\";\n"
"border : none;"))
        self.m3PosNum.setObjectName(_fromUtf8("m3PosNum"))
        self.m3TorqueNum = QtGui.QLabel(self.m3SFrame)
        self.m3TorqueNum.setGeometry(QtCore.QRect(120, 320, 61, 21))
        self.m3TorqueNum.setStyleSheet(_fromUtf8("font: 63 16pt \"KacstArt\";\n"
"border : none;"))
        self.m3TorqueNum.setObjectName(_fromUtf8("m3TorqueNum"))
        self.m3ErrNum = QtGui.QLabel(self.m3SFrame)
        self.m3ErrNum.setGeometry(QtCore.QRect(260, 440, 61, 21))
        self.m3ErrNum.setStyleSheet(_fromUtf8("font: 63 16pt \"KacstArt\";\n"
"border : none;"))
        self.m3ErrNum.setObjectName(_fromUtf8("m3ErrNum"))
        self.m3TempNum = QtGui.QLabel(self.m3SFrame)
        self.m3TempNum.setGeometry(QtCore.QRect(400, 320, 61, 21))
        self.m3TempNum.setStyleSheet(_fromUtf8("font: 63 16pt \"KacstArt\";\n"
"border : none;"))
        self.m3TempNum.setObjectName(_fromUtf8("m3TempNum"))
        self.m3CFrame = QtGui.QFrame(self.m3Page)
        self.m3CFrame.setGeometry(QtCore.QRect(580, 40, 211, 501))
        self.m3CFrame.setStyleSheet(_fromUtf8("border : 1px solid rgb(113, 0, 0);\n"
""))
        self.m3CFrame.setObjectName(_fromUtf8("m3CFrame"))
        self.m3GoalTSpin = QtGui.QSpinBox(self.m3CFrame)
        self.m3GoalTSpin.setGeometry(QtCore.QRect(30, 40, 151, 21))
        self.m3GoalTSpin.setStyleSheet(_fromUtf8("font: 63 13pt \"KacstArt\";"))
        self.m3GoalTSpin.setWrapping(False)
        self.m3GoalTSpin.setAccelerated(False)
        self.m3GoalTSpin.setObjectName(_fromUtf8("m3GoalTSpin"))
        self.m3GoalTLabel = QtGui.QLabel(self.m3CFrame)
        self.m3GoalTLabel.setGeometry(QtCore.QRect(60, 10, 111, 21))
        self.m3GoalTLabel.setStyleSheet(_fromUtf8("font: 63 14pt \"KacstArt\";\n"
"border : none;"))
        self.m3GoalTLabel.setObjectName(_fromUtf8("m3GoalTLabel"))
        self.m3UpdateBtn = QtGui.QPushButton(self.m3CFrame)
        self.m3UpdateBtn.setGeometry(QtCore.QRect(20, 290, 171, 41))
        self.m3UpdateBtn.setAutoFillBackground(False)
        self.m3UpdateBtn.setStyleSheet(_fromUtf8("QPushButton\n"
"{font: 63 14pt \"KacstArt\";\n"
"border : 2px solid black;\n"
"}\n"
"QPushButton:pressed\n"
"{    \n"
"    background-color : rgb(209,209,224);\n"
"}\n"
"\n"
"        "))
        self.m3UpdateBtn.setAutoDefault(False)
        self.m3UpdateBtn.setDefault(False)
        self.m3UpdateBtn.setFlat(False)
        self.m3UpdateBtn.setObjectName(_fromUtf8("m3UpdateBtn"))
        self.m3AngleLabel = QtGui.QLabel(self.m3CFrame)
        self.m3AngleLabel.setGeometry(QtCore.QRect(80, 70, 61, 21))
        self.m3AngleLabel.setStyleSheet(_fromUtf8("font: 63 14pt \"KacstArt\";\n"
"border : none;"))
        self.m3AngleLabel.setObjectName(_fromUtf8("m3AngleLabel"))
        self.m3AngleSpin = QtGui.QSpinBox(self.m3CFrame)
        self.m3AngleSpin.setGeometry(QtCore.QRect(30, 100, 151, 21))
        self.m3AngleSpin.setStyleSheet(_fromUtf8("font: 63 13pt \"KacstArt\";"))
        self.m3AngleSpin.setWrapping(False)
        self.m3AngleSpin.setAccelerated(False)
        self.m3AngleSpin.setMinimum(-150)
        self.m3AngleSpin.setMaximum(150)
        self.m3AngleSpin.setObjectName(_fromUtf8("m3AngleSpin"))
        self.m3PositionSpin = QtGui.QSpinBox(self.m3CFrame)
        self.m3PositionSpin.setGeometry(QtCore.QRect(30, 190, 151, 21))
        self.m3PositionSpin.setStyleSheet(_fromUtf8("font: 63 13pt \"KacstArt\";"))
        self.m3PositionSpin.setWrapping(False)
        self.m3PositionSpin.setAccelerated(False)
        self.m3PositionSpin.setMaximum(1023)
        self.m3PositionSpin.setObjectName(_fromUtf8("m3PositionSpin"))
        self.m3PositionLabel = QtGui.QLabel(self.m3CFrame)
        self.m3PositionLabel.setGeometry(QtCore.QRect(70, 170, 81, 21))
        self.m3PositionLabel.setStyleSheet(_fromUtf8("font: 63 14pt \"KacstArt\";\n"
"border : none;"))
        self.m3PositionLabel.setObjectName(_fromUtf8("m3PositionLabel"))
        self.m3AngleBtn = QtGui.QPushButton(self.m3CFrame)
        self.m3AngleBtn.setGeometry(QtCore.QRect(30, 130, 151, 21))
        self.m3AngleBtn.setStyleSheet(_fromUtf8("QPushButton\n"
"{font: 63 12pt \"KacstArt\";\n"
"border : 2px solid black;\n"
"}\n"
"QPushButton:pressed\n"
"{    \n"
"    background-color : rgb(209,209,224);\n"
"}\n"
"\n"
"        "))
        self.m3AngleBtn.setObjectName(_fromUtf8("m3AngleBtn"))
        self.m3PositionBtn = QtGui.QPushButton(self.m3CFrame)
        self.m3PositionBtn.setGeometry(QtCore.QRect(30, 220, 151, 21))
        self.m3PositionBtn.setStyleSheet(_fromUtf8("QPushButton\n"
"{font: 63 12pt \"KacstArt\";\n"
"border : 2px solid black;\n"
"}\n"
"QPushButton:pressed\n"
"{    \n"
"    background-color : rgb(209,209,224);\n"
"}\n"
"\n"
"        "))
        self.m3PositionBtn.setObjectName(_fromUtf8("m3PositionBtn"))
        self.m3HomeBtn = QtGui.QPushButton(self.m3CFrame)
        self.m3HomeBtn.setGeometry(QtCore.QRect(20, 370, 171, 61))
        self.m3HomeBtn.setStyleSheet(_fromUtf8("QPushButton\n"
"{font: 63 14pt \"KacstArt\";\n"
"border : 2px solid black;\n"
"}\n"
"QPushButton:pressed\n"
"{    \n"
"    background-color : rgb(209,209,224);\n"
"}\n"
"\n"
"        "))
        self.m3HomeBtn.setObjectName(_fromUtf8("m3HomeBtn"))
        self.m3Label = QtGui.QLabel(self.m3Page)
        self.m3Label.setGeometry(QtCore.QRect(340, 10, 91, 21))
        self.m3Label.setStyleSheet(_fromUtf8("font: 63 16pt \"KacstArt\";\n"
"border : none;"))
        self.m3Label.setObjectName(_fromUtf8("m3Label"))
        self.stackedWidget.addWidget(self.m3Page)
        self.m4Page = QtGui.QWidget()
        self.m4Page.setObjectName(_fromUtf8("m4Page"))
        self.m4SFrame = QtGui.QFrame(self.m4Page)
        self.m4SFrame.setGeometry(QtCore.QRect(10, 40, 561, 501))
        self.m4SFrame.setStyleSheet(_fromUtf8("border : 1px solid rgb(113, 0, 0);\n"
""))
        self.m4SFrame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.m4SFrame.setFrameShadow(QtGui.QFrame.Raised)
        self.m4SFrame.setObjectName(_fromUtf8("m4SFrame"))
        self.m4AngLabel = QtGui.QLabel(self.m4SFrame)
        self.m4AngLabel.setGeometry(QtCore.QRect(120, 40, 61, 21))
        self.m4AngLabel.setStyleSheet(_fromUtf8("font: 63 16pt \"KacstArt\";\n"
"border : none;"))
        self.m4AngLabel.setObjectName(_fromUtf8("m4AngLabel"))
        self.m4PosLabel = QtGui.QLabel(self.m4SFrame)
        self.m4PosLabel.setGeometry(QtCore.QRect(390, 40, 91, 21))
        self.m4PosLabel.setStyleSheet(_fromUtf8("font: 63 16pt \"KacstArt\";\n"
"border : none;"))
        self.m4PosLabel.setObjectName(_fromUtf8("m4PosLabel"))
        self.m4TorqueLabel = QtGui.QLabel(self.m4SFrame)
        self.m4TorqueLabel.setGeometry(QtCore.QRect(80, 270, 141, 21))
        self.m4TorqueLabel.setStyleSheet(_fromUtf8("font: 63 16pt \"KacstArt\";\n"
"border : none;"))
        self.m4TorqueLabel.setObjectName(_fromUtf8("m4TorqueLabel"))
        self.m4TempLabel = QtGui.QLabel(self.m4SFrame)
        self.m4TempLabel.setGeometry(QtCore.QRect(370, 270, 131, 21))
        self.m4TempLabel.setStyleSheet(_fromUtf8("font: 63 16pt \"KacstArt\";\n"
"border : none;"))
        self.m4TempLabel.setObjectName(_fromUtf8("m4TempLabel"))
        self.m4ErrLabel = QtGui.QLabel(self.m4SFrame)
        self.m4ErrLabel.setGeometry(QtCore.QRect(260, 390, 61, 21))
        self.m4ErrLabel.setStyleSheet(_fromUtf8("font: 63 16pt \"KacstArt\";\n"
"border : none;"))
        self.m4ErrLabel.setObjectName(_fromUtf8("m4ErrLabel"))
        self.m4AngDial = QtGui.QDial(self.m4SFrame)
        self.m4AngDial.setGeometry(QtCore.QRect(100, 80, 91, 81))
        self.m4AngDial.setMinimum(-150)
        self.m4AngDial.setMaximum(150)
        self.m4AngDial.setTracking(True)
        self.m4AngDial.setWrapping(False)
        self.m4AngDial.setNotchTarget(50.0)
        self.m4AngDial.setNotchesVisible(True)
        self.m4AngDial.setObjectName(_fromUtf8("m4AngDial"))
        self.m4PosDial = QtGui.QDial(self.m4SFrame)
        self.m4PosDial.setGeometry(QtCore.QRect(380, 80, 91, 81))
        self.m4PosDial.setMinimum(0)
        self.m4PosDial.setMaximum(1023)
        self.m4PosDial.setTracking(True)
        self.m4PosDial.setWrapping(False)
        self.m4PosDial.setNotchTarget(100.0)
        self.m4PosDial.setNotchesVisible(True)
        self.m4PosDial.setObjectName(_fromUtf8("m4PosDial"))
        self.m4AngNum = QtGui.QLabel(self.m4SFrame)
        self.m4AngNum.setGeometry(QtCore.QRect(120, 200, 61, 21))
        self.m4AngNum.setStyleSheet(_fromUtf8("font: 63 16pt \"KacstArt\";\n"
"border : none;"))
        self.m4AngNum.setObjectName(_fromUtf8("m4AngNum"))
        self.m4PosNum = QtGui.QLabel(self.m4SFrame)
        self.m4PosNum.setGeometry(QtCore.QRect(400, 200, 61, 21))
        self.m4PosNum.setStyleSheet(_fromUtf8("font: 63 16pt \"KacstArt\";\n"
"border : none;"))
        self.m4PosNum.setObjectName(_fromUtf8("m4PosNum"))
        self.m4TorqueNum = QtGui.QLabel(self.m4SFrame)
        self.m4TorqueNum.setGeometry(QtCore.QRect(120, 320, 61, 21))
        self.m4TorqueNum.setStyleSheet(_fromUtf8("font: 63 16pt \"KacstArt\";\n"
"border : none;"))
        self.m4TorqueNum.setObjectName(_fromUtf8("m4TorqueNum"))
        self.m4ErrNum = QtGui.QLabel(self.m4SFrame)
        self.m4ErrNum.setGeometry(QtCore.QRect(260, 440, 61, 21))
        self.m4ErrNum.setStyleSheet(_fromUtf8("font: 63 16pt \"KacstArt\";\n"
"border : none;"))
        self.m4ErrNum.setObjectName(_fromUtf8("m4ErrNum"))
        self.m4TempNum = QtGui.QLabel(self.m4SFrame)
        self.m4TempNum.setGeometry(QtCore.QRect(400, 320, 61, 21))
        self.m4TempNum.setStyleSheet(_fromUtf8("font: 63 16pt \"KacstArt\";\n"
"border : none;"))
        self.m4TempNum.setObjectName(_fromUtf8("m4TempNum"))
        self.m4CFrame = QtGui.QFrame(self.m4Page)
        self.m4CFrame.setGeometry(QtCore.QRect(580, 40, 211, 501))
        self.m4CFrame.setStyleSheet(_fromUtf8("border : 1px solid rgb(113, 0, 0);\n"
""))
        self.m4CFrame.setObjectName(_fromUtf8("m4CFrame"))
        self.m4GoalTSpin = QtGui.QSpinBox(self.m4CFrame)
        self.m4GoalTSpin.setGeometry(QtCore.QRect(30, 40, 151, 21))
        self.m4GoalTSpin.setStyleSheet(_fromUtf8("font: 63 13pt \"KacstArt\";"))
        self.m4GoalTSpin.setWrapping(False)
        self.m4GoalTSpin.setAccelerated(False)
        self.m4GoalTSpin.setObjectName(_fromUtf8("m4GoalTSpin"))
        self.m4GoalTLabel = QtGui.QLabel(self.m4CFrame)
        self.m4GoalTLabel.setGeometry(QtCore.QRect(60, 10, 111, 21))
        self.m4GoalTLabel.setStyleSheet(_fromUtf8("font: 63 14pt \"KacstArt\";\n"
"border : none;"))
        self.m4GoalTLabel.setObjectName(_fromUtf8("m4GoalTLabel"))
        self.m4UpdateBtn = QtGui.QPushButton(self.m4CFrame)
        self.m4UpdateBtn.setGeometry(QtCore.QRect(20, 290, 171, 41))
        self.m4UpdateBtn.setAutoFillBackground(False)
        self.m4UpdateBtn.setStyleSheet(_fromUtf8("QPushButton\n"
"{font: 63 14pt \"KacstArt\";\n"
"border : 2px solid black;\n"
"}\n"
"QPushButton:pressed\n"
"{    \n"
"    background-color : rgb(209,209,224);\n"
"}\n"
"\n"
"        "))
        self.m4UpdateBtn.setAutoDefault(False)
        self.m4UpdateBtn.setDefault(False)
        self.m4UpdateBtn.setFlat(False)
        self.m4UpdateBtn.setObjectName(_fromUtf8("m4UpdateBtn"))
        self.m4AngleLabel = QtGui.QLabel(self.m4CFrame)
        self.m4AngleLabel.setGeometry(QtCore.QRect(80, 70, 61, 21))
        self.m4AngleLabel.setStyleSheet(_fromUtf8("font: 63 14pt \"KacstArt\";\n"
"border : none;"))
        self.m4AngleLabel.setObjectName(_fromUtf8("m4AngleLabel"))
        self.m4AngleSpin = QtGui.QSpinBox(self.m4CFrame)
        self.m4AngleSpin.setGeometry(QtCore.QRect(30, 100, 151, 21))
        self.m4AngleSpin.setStyleSheet(_fromUtf8("font: 63 13pt \"KacstArt\";"))
        self.m4AngleSpin.setWrapping(False)
        self.m4AngleSpin.setAccelerated(False)
        self.m4AngleSpin.setMinimum(-150)
        self.m4AngleSpin.setMaximum(150)
        self.m4AngleSpin.setObjectName(_fromUtf8("m4AngleSpin"))
        self.m4PositionSpin = QtGui.QSpinBox(self.m4CFrame)
        self.m4PositionSpin.setGeometry(QtCore.QRect(30, 190, 151, 21))
        self.m4PositionSpin.setStyleSheet(_fromUtf8("font: 63 13pt \"KacstArt\";"))
        self.m4PositionSpin.setWrapping(False)
        self.m4PositionSpin.setAccelerated(False)
        self.m4PositionSpin.setMaximum(1023)
        self.m4PositionSpin.setObjectName(_fromUtf8("m4PositionSpin"))
        self.m4PositionLabel = QtGui.QLabel(self.m4CFrame)
        self.m4PositionLabel.setGeometry(QtCore.QRect(70, 170, 81, 21))
        self.m4PositionLabel.setStyleSheet(_fromUtf8("font: 63 14pt \"KacstArt\";\n"
"border : none;"))
        self.m4PositionLabel.setObjectName(_fromUtf8("m4PositionLabel"))
        self.m4AngleBtn = QtGui.QPushButton(self.m4CFrame)
        self.m4AngleBtn.setGeometry(QtCore.QRect(30, 130, 151, 21))
        self.m4AngleBtn.setStyleSheet(_fromUtf8("QPushButton\n"
"{font: 63 12pt \"KacstArt\";\n"
"border : 2px solid black;\n"
"}\n"
"QPushButton:pressed\n"
"{    \n"
"    background-color : rgb(209,209,224);\n"
"}\n"
"\n"
"        "))
        self.m4AngleBtn.setObjectName(_fromUtf8("m4AngleBtn"))
        self.m4PositionBtn = QtGui.QPushButton(self.m4CFrame)
        self.m4PositionBtn.setGeometry(QtCore.QRect(30, 220, 151, 21))
        self.m4PositionBtn.setStyleSheet(_fromUtf8("QPushButton\n"
"{font: 63 12pt \"KacstArt\";\n"
"border : 2px solid black;\n"
"}\n"
"QPushButton:pressed\n"
"{    \n"
"    background-color : rgb(209,209,224);\n"
"}\n"
"\n"
"        "))
        self.m4PositionBtn.setObjectName(_fromUtf8("m4PositionBtn"))
        self.m4HomeBtn = QtGui.QPushButton(self.m4CFrame)
        self.m4HomeBtn.setGeometry(QtCore.QRect(20, 370, 171, 61))
        self.m4HomeBtn.setStyleSheet(_fromUtf8("QPushButton\n"
"{font: 63 14pt \"KacstArt\";\n"
"border : 2px solid black;\n"
"}\n"
"QPushButton:pressed\n"
"{    \n"
"    background-color : rgb(209,209,224);\n"
"}\n"
"\n"
"        "))
        self.m4HomeBtn.setObjectName(_fromUtf8("m4HomeBtn"))
        self.m4Label = QtGui.QLabel(self.m4Page)
        self.m4Label.setGeometry(QtCore.QRect(340, 10, 91, 21))
        self.m4Label.setStyleSheet(_fromUtf8("font: 63 16pt \"KacstArt\";\n"
"border : none;"))
        self.m4Label.setObjectName(_fromUtf8("m4Label"))
        self.stackedWidget.addWidget(self.m4Page)
        self.m5Page = QtGui.QWidget()
        self.m5Page.setObjectName(_fromUtf8("m5Page"))
        self.m5SFrame = QtGui.QFrame(self.m5Page)
        self.m5SFrame.setGeometry(QtCore.QRect(10, 40, 561, 501))
        self.m5SFrame.setStyleSheet(_fromUtf8("border : 1px solid rgb(113, 0, 0);\n"
""))
        self.m5SFrame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.m5SFrame.setFrameShadow(QtGui.QFrame.Raised)
        self.m5SFrame.setObjectName(_fromUtf8("m5SFrame"))
        self.m5AngLabel = QtGui.QLabel(self.m5SFrame)
        self.m5AngLabel.setGeometry(QtCore.QRect(120, 40, 61, 21))
        self.m5AngLabel.setStyleSheet(_fromUtf8("font: 63 16pt \"KacstArt\";\n"
"border : none;"))
        self.m5AngLabel.setObjectName(_fromUtf8("m5AngLabel"))
        self.m5PosLabel = QtGui.QLabel(self.m5SFrame)
        self.m5PosLabel.setGeometry(QtCore.QRect(390, 40, 91, 21))
        self.m5PosLabel.setStyleSheet(_fromUtf8("font: 63 16pt \"KacstArt\";\n"
"border : none;"))
        self.m5PosLabel.setObjectName(_fromUtf8("m5PosLabel"))
        self.m5TorqueLabel = QtGui.QLabel(self.m5SFrame)
        self.m5TorqueLabel.setGeometry(QtCore.QRect(80, 270, 141, 21))
        self.m5TorqueLabel.setStyleSheet(_fromUtf8("font: 63 16pt \"KacstArt\";\n"
"border : none;"))
        self.m5TorqueLabel.setObjectName(_fromUtf8("m5TorqueLabel"))
        self.m5TempLabel = QtGui.QLabel(self.m5SFrame)
        self.m5TempLabel.setGeometry(QtCore.QRect(370, 270, 131, 21))
        self.m5TempLabel.setStyleSheet(_fromUtf8("font: 63 16pt \"KacstArt\";\n"
"border : none;"))
        self.m5TempLabel.setObjectName(_fromUtf8("m5TempLabel"))
        self.m5ErrLabel = QtGui.QLabel(self.m5SFrame)
        self.m5ErrLabel.setGeometry(QtCore.QRect(260, 390, 61, 21))
        self.m5ErrLabel.setStyleSheet(_fromUtf8("font: 63 16pt \"KacstArt\";\n"
"border : none;"))
        self.m5ErrLabel.setObjectName(_fromUtf8("m5ErrLabel"))
        self.m5AngDial = QtGui.QDial(self.m5SFrame)
        self.m5AngDial.setGeometry(QtCore.QRect(100, 80, 91, 81))
        self.m5AngDial.setMinimum(-150)
        self.m5AngDial.setMaximum(150)
        self.m5AngDial.setTracking(True)
        self.m5AngDial.setWrapping(False)
        self.m5AngDial.setNotchTarget(50.0)
        self.m5AngDial.setNotchesVisible(True)
        self.m5AngDial.setObjectName(_fromUtf8("m5AngDial"))
        self.m5PosDial = QtGui.QDial(self.m5SFrame)
        self.m5PosDial.setGeometry(QtCore.QRect(380, 80, 91, 81))
        self.m5PosDial.setMinimum(0)
        self.m5PosDial.setMaximum(1023)
        self.m5PosDial.setTracking(True)
        self.m5PosDial.setWrapping(False)
        self.m5PosDial.setNotchTarget(100.0)
        self.m5PosDial.setNotchesVisible(True)
        self.m5PosDial.setObjectName(_fromUtf8("m5PosDial"))
        self.m5AngNum = QtGui.QLabel(self.m5SFrame)
        self.m5AngNum.setGeometry(QtCore.QRect(120, 200, 61, 21))
        self.m5AngNum.setStyleSheet(_fromUtf8("font: 63 16pt \"KacstArt\";\n"
"border : none;"))
        self.m5AngNum.setObjectName(_fromUtf8("m5AngNum"))
        self.m5PosNum = QtGui.QLabel(self.m5SFrame)
        self.m5PosNum.setGeometry(QtCore.QRect(400, 200, 61, 21))
        self.m5PosNum.setStyleSheet(_fromUtf8("font: 63 16pt \"KacstArt\";\n"
"border : none;"))
        self.m5PosNum.setObjectName(_fromUtf8("m5PosNum"))
        self.m5TorqueNum = QtGui.QLabel(self.m5SFrame)
        self.m5TorqueNum.setGeometry(QtCore.QRect(120, 320, 61, 21))
        self.m5TorqueNum.setStyleSheet(_fromUtf8("font: 63 16pt \"KacstArt\";\n"
"border : none;"))
        self.m5TorqueNum.setObjectName(_fromUtf8("m5TorqueNum"))
        self.m5ErrNum = QtGui.QLabel(self.m5SFrame)
        self.m5ErrNum.setGeometry(QtCore.QRect(260, 440, 61, 21))
        self.m5ErrNum.setStyleSheet(_fromUtf8("font: 63 16pt \"KacstArt\";\n"
"border : none;"))
        self.m5ErrNum.setObjectName(_fromUtf8("m5ErrNum"))
        self.m5TempNum = QtGui.QLabel(self.m5SFrame)
        self.m5TempNum.setGeometry(QtCore.QRect(400, 320, 61, 21))
        self.m5TempNum.setStyleSheet(_fromUtf8("font: 63 16pt \"KacstArt\";\n"
"border : none;"))
        self.m5TempNum.setObjectName(_fromUtf8("m5TempNum"))
        self.m5CFrame = QtGui.QFrame(self.m5Page)
        self.m5CFrame.setGeometry(QtCore.QRect(580, 40, 211, 501))
        self.m5CFrame.setStyleSheet(_fromUtf8("border : 1px solid rgb(113, 0, 0);\n"
""))
        self.m5CFrame.setObjectName(_fromUtf8("m5CFrame"))
        self.m5GoalTSpin = QtGui.QSpinBox(self.m5CFrame)
        self.m5GoalTSpin.setGeometry(QtCore.QRect(30, 40, 151, 21))
        self.m5GoalTSpin.setStyleSheet(_fromUtf8("font: 63 13pt \"KacstArt\";"))
        self.m5GoalTSpin.setWrapping(False)
        self.m5GoalTSpin.setAccelerated(False)
        self.m5GoalTSpin.setObjectName(_fromUtf8("m5GoalTSpin"))
        self.m5GoalTLabel = QtGui.QLabel(self.m5CFrame)
        self.m5GoalTLabel.setGeometry(QtCore.QRect(60, 10, 111, 21))
        self.m5GoalTLabel.setStyleSheet(_fromUtf8("font: 63 14pt \"KacstArt\";\n"
"border : none;"))
        self.m5GoalTLabel.setObjectName(_fromUtf8("m5GoalTLabel"))
        self.m5UpdateBtn = QtGui.QPushButton(self.m5CFrame)
        self.m5UpdateBtn.setGeometry(QtCore.QRect(20, 290, 171, 41))
        self.m5UpdateBtn.setAutoFillBackground(False)
        self.m5UpdateBtn.setStyleSheet(_fromUtf8("QPushButton\n"
"{font: 63 14pt \"KacstArt\";\n"
"border : 2px solid black;\n"
"}\n"
"QPushButton:pressed\n"
"{    \n"
"    background-color : rgb(209,209,224);\n"
"}\n"
"\n"
"        "))
        self.m5UpdateBtn.setAutoDefault(False)
        self.m5UpdateBtn.setDefault(False)
        self.m5UpdateBtn.setFlat(False)
        self.m5UpdateBtn.setObjectName(_fromUtf8("m5UpdateBtn"))
        self.m5AngleLabel = QtGui.QLabel(self.m5CFrame)
        self.m5AngleLabel.setGeometry(QtCore.QRect(80, 70, 61, 21))
        self.m5AngleLabel.setStyleSheet(_fromUtf8("font: 63 14pt \"KacstArt\";\n"
"border : none;"))
        self.m5AngleLabel.setObjectName(_fromUtf8("m5AngleLabel"))
        self.m5AngleSpin = QtGui.QSpinBox(self.m5CFrame)
        self.m5AngleSpin.setGeometry(QtCore.QRect(30, 100, 151, 21))
        self.m5AngleSpin.setStyleSheet(_fromUtf8("font: 63 13pt \"KacstArt\";"))
        self.m5AngleSpin.setWrapping(False)
        self.m5AngleSpin.setAccelerated(False)
        self.m5AngleSpin.setMinimum(-150)
        self.m5AngleSpin.setMaximum(150)
        self.m5AngleSpin.setObjectName(_fromUtf8("m5AngleSpin"))
        self.m5PositionSpin = QtGui.QSpinBox(self.m5CFrame)
        self.m5PositionSpin.setGeometry(QtCore.QRect(30, 190, 151, 21))
        self.m5PositionSpin.setStyleSheet(_fromUtf8("font: 63 13pt \"KacstArt\";"))
        self.m5PositionSpin.setWrapping(False)
        self.m5PositionSpin.setAccelerated(False)
        self.m5PositionSpin.setMaximum(1023)
        self.m5PositionSpin.setObjectName(_fromUtf8("m5PositionSpin"))
        self.m5PositionLabel = QtGui.QLabel(self.m5CFrame)
        self.m5PositionLabel.setGeometry(QtCore.QRect(70, 170, 81, 21))
        self.m5PositionLabel.setStyleSheet(_fromUtf8("font: 63 14pt \"KacstArt\";\n"
"border : none;"))
        self.m5PositionLabel.setObjectName(_fromUtf8("m5PositionLabel"))
        self.m5AngleBtn = QtGui.QPushButton(self.m5CFrame)
        self.m5AngleBtn.setGeometry(QtCore.QRect(30, 130, 151, 21))
        self.m5AngleBtn.setStyleSheet(_fromUtf8("QPushButton\n"
"{font: 63 12pt \"KacstArt\";\n"
"border : 2px solid black;\n"
"}\n"
"QPushButton:pressed\n"
"{    \n"
"    background-color : rgb(209,209,224);\n"
"}\n"
"\n"
"        "))
        self.m5AngleBtn.setObjectName(_fromUtf8("m5AngleBtn"))
        self.m5PositionBtn = QtGui.QPushButton(self.m5CFrame)
        self.m5PositionBtn.setGeometry(QtCore.QRect(30, 220, 151, 21))
        self.m5PositionBtn.setStyleSheet(_fromUtf8("QPushButton\n"
"{font: 63 12pt \"KacstArt\";\n"
"border : 2px solid black;\n"
"}\n"
"QPushButton:pressed\n"
"{    \n"
"    background-color : rgb(209,209,224);\n"
"}\n"
"\n"
"        "))
        self.m5PositionBtn.setObjectName(_fromUtf8("m5PositionBtn"))
        self.m5HomeBtn = QtGui.QPushButton(self.m5CFrame)
        self.m5HomeBtn.setGeometry(QtCore.QRect(20, 370, 171, 61))
        self.m5HomeBtn.setStyleSheet(_fromUtf8("QPushButton\n"
"{font: 63 14pt \"KacstArt\";\n"
"border : 2px solid black;\n"
"}\n"
"QPushButton:pressed\n"
"{    \n"
"    background-color : rgb(209,209,224);\n"
"}\n"
"\n"
"        "))
        self.m5HomeBtn.setObjectName(_fromUtf8("m5HomeBtn"))
        self.m5Label = QtGui.QLabel(self.m5Page)
        self.m5Label.setGeometry(QtCore.QRect(340, 10, 91, 21))
        self.m5Label.setStyleSheet(_fromUtf8("font: 63 16pt \"KacstArt\";\n"
"border : none;"))
        self.m5Label.setObjectName(_fromUtf8("m5Label"))
        self.stackedWidget.addWidget(self.m5Page)
        self.m6Page = QtGui.QWidget()
        self.m6Page.setObjectName(_fromUtf8("m6Page"))
        self.m6Label = QtGui.QLabel(self.m6Page)
        self.m6Label.setGeometry(QtCore.QRect(340, 10, 91, 21))
        self.m6Label.setStyleSheet(_fromUtf8("font: 63 16pt \"KacstArt\";\n"
"border : none;"))
        self.m6Label.setObjectName(_fromUtf8("m6Label"))
        self.m6CFrame = QtGui.QFrame(self.m6Page)
        self.m6CFrame.setGeometry(QtCore.QRect(580, 40, 211, 501))
        self.m6CFrame.setStyleSheet(_fromUtf8("border : 1px solid rgb(113, 0, 0);\n"
"\n"
"\n"
"        "))
        self.m6CFrame.setObjectName(_fromUtf8("m6CFrame"))
        self.m6GoalTSpin = QtGui.QSpinBox(self.m6CFrame)
        self.m6GoalTSpin.setGeometry(QtCore.QRect(30, 40, 151, 21))
        self.m6GoalTSpin.setStyleSheet(_fromUtf8("font: 63 13pt \"KacstArt\";"))
        self.m6GoalTSpin.setWrapping(False)
        self.m6GoalTSpin.setAccelerated(False)
        self.m6GoalTSpin.setObjectName(_fromUtf8("m6GoalTSpin"))
        self.m6GoalTLabel = QtGui.QLabel(self.m6CFrame)
        self.m6GoalTLabel.setGeometry(QtCore.QRect(60, 10, 111, 21))
        self.m6GoalTLabel.setStyleSheet(_fromUtf8("font: 63 14pt \"KacstArt\";\n"
"border : none;"))
        self.m6GoalTLabel.setObjectName(_fromUtf8("m6GoalTLabel"))
        self.m6UpdateBtn = QtGui.QPushButton(self.m6CFrame)
        self.m6UpdateBtn.setGeometry(QtCore.QRect(20, 290, 171, 41))
        self.m6UpdateBtn.setAutoFillBackground(False)
        self.m6UpdateBtn.setStyleSheet(_fromUtf8("QPushButton\n"
"{font: 63 14pt \"KacstArt\";\n"
"border : 2px solid black;\n"
"}\n"
"QPushButton:pressed\n"
"{    \n"
"    background-color : rgb(209,209,224);\n"
"}\n"
"\n"
"        "))
        self.m6UpdateBtn.setAutoDefault(False)
        self.m6UpdateBtn.setDefault(False)
        self.m6UpdateBtn.setFlat(False)
        self.m6UpdateBtn.setObjectName(_fromUtf8("m6UpdateBtn"))
        self.m6AngleLabel = QtGui.QLabel(self.m6CFrame)
        self.m6AngleLabel.setGeometry(QtCore.QRect(80, 70, 61, 21))
        self.m6AngleLabel.setStyleSheet(_fromUtf8("font: 63 14pt \"KacstArt\";\n"
"border : none;"))
        self.m6AngleLabel.setObjectName(_fromUtf8("m6AngleLabel"))
        self.m6AngleSpin = QtGui.QSpinBox(self.m6CFrame)
        self.m6AngleSpin.setGeometry(QtCore.QRect(30, 100, 151, 21))
        self.m6AngleSpin.setStyleSheet(_fromUtf8("font: 63 13pt \"KacstArt\";"))
        self.m6AngleSpin.setWrapping(False)
        self.m6AngleSpin.setAccelerated(False)
        self.m6AngleSpin.setMinimum(-150)
        self.m6AngleSpin.setMaximum(150)
        self.m6AngleSpin.setObjectName(_fromUtf8("m6AngleSpin"))
        self.m6PositionSpin = QtGui.QSpinBox(self.m6CFrame)
        self.m6PositionSpin.setGeometry(QtCore.QRect(30, 190, 151, 21))
        self.m6PositionSpin.setStyleSheet(_fromUtf8("font: 63 13pt \"KacstArt\";"))
        self.m6PositionSpin.setWrapping(False)
        self.m6PositionSpin.setAccelerated(False)
        self.m6PositionSpin.setMaximum(1023)
        self.m6PositionSpin.setObjectName(_fromUtf8("m6PositionSpin"))
        self.m6PositionLabel = QtGui.QLabel(self.m6CFrame)
        self.m6PositionLabel.setGeometry(QtCore.QRect(70, 170, 81, 21))
        self.m6PositionLabel.setStyleSheet(_fromUtf8("font: 63 14pt \"KacstArt\";\n"
"border : none;"))
        self.m6PositionLabel.setObjectName(_fromUtf8("m6PositionLabel"))
        self.m6AngleBtn = QtGui.QPushButton(self.m6CFrame)
        self.m6AngleBtn.setGeometry(QtCore.QRect(30, 130, 151, 21))
        self.m6AngleBtn.setStyleSheet(_fromUtf8("QPushButton\n"
"{font: 63 12pt \"KacstArt\";\n"
"border : 2px solid black;\n"
"}\n"
"QPushButton:pressed\n"
"{    \n"
"    background-color : rgb(209,209,224);\n"
"}\n"
"\n"
"        "))
        self.m6AngleBtn.setObjectName(_fromUtf8("m6AngleBtn"))
        self.m6PositionBtn = QtGui.QPushButton(self.m6CFrame)
        self.m6PositionBtn.setGeometry(QtCore.QRect(30, 220, 151, 21))
        self.m6PositionBtn.setStyleSheet(_fromUtf8("QPushButton\n"
"{font: 63 12pt \"KacstArt\";\n"
"border : 2px solid black;\n"
"}\n"
"QPushButton:pressed\n"
"{    \n"
"    background-color : rgb(209,209,224);\n"
"}\n"
"\n"
"        "))
        self.m6PositionBtn.setObjectName(_fromUtf8("m6PositionBtn"))
        self.m6HomeBtn = QtGui.QPushButton(self.m6CFrame)
        self.m6HomeBtn.setGeometry(QtCore.QRect(20, 370, 171, 61))
        self.m6HomeBtn.setStyleSheet(_fromUtf8("QPushButton\n"
"{font: 63 14pt \"KacstArt\";\n"
"border : 2px solid black;\n"
"}\n"
"QPushButton:pressed\n"
"{    \n"
"    background-color : rgb(209,209,224);\n"
"}\n"
"\n"
"        "))
        self.m6HomeBtn.setObjectName(_fromUtf8("m6HomeBtn"))
        self.m6SFrame = QtGui.QFrame(self.m6Page)
        self.m6SFrame.setGeometry(QtCore.QRect(10, 40, 561, 501))
        self.m6SFrame.setStyleSheet(_fromUtf8("border : 1px solid rgb(113, 0, 0);\n"
""))
        self.m6SFrame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.m6SFrame.setFrameShadow(QtGui.QFrame.Raised)
        self.m6SFrame.setObjectName(_fromUtf8("m6SFrame"))
        self.m6AngLabel = QtGui.QLabel(self.m6SFrame)
        self.m6AngLabel.setGeometry(QtCore.QRect(120, 40, 61, 21))
        self.m6AngLabel.setStyleSheet(_fromUtf8("font: 63 16pt \"KacstArt\";\n"
"border : none;"))
        self.m6AngLabel.setObjectName(_fromUtf8("m6AngLabel"))
        self.m6PosLabel = QtGui.QLabel(self.m6SFrame)
        self.m6PosLabel.setGeometry(QtCore.QRect(390, 40, 91, 21))
        self.m6PosLabel.setStyleSheet(_fromUtf8("font: 63 16pt \"KacstArt\";\n"
"border : none;"))
        self.m6PosLabel.setObjectName(_fromUtf8("m6PosLabel"))
        self.m6TorqueLabel = QtGui.QLabel(self.m6SFrame)
        self.m6TorqueLabel.setGeometry(QtCore.QRect(80, 270, 141, 21))
        self.m6TorqueLabel.setStyleSheet(_fromUtf8("font: 63 16pt \"KacstArt\";\n"
"border : none;"))
        self.m6TorqueLabel.setObjectName(_fromUtf8("m6TorqueLabel"))
        self.m6TempLabel = QtGui.QLabel(self.m6SFrame)
        self.m6TempLabel.setGeometry(QtCore.QRect(370, 270, 131, 21))
        self.m6TempLabel.setStyleSheet(_fromUtf8("font: 63 16pt \"KacstArt\";\n"
"border : none;"))
        self.m6TempLabel.setObjectName(_fromUtf8("m6TempLabel"))
        self.m6ErrLabel = QtGui.QLabel(self.m6SFrame)
        self.m6ErrLabel.setGeometry(QtCore.QRect(260, 390, 61, 21))
        self.m6ErrLabel.setStyleSheet(_fromUtf8("font: 63 16pt \"KacstArt\";\n"
"border : none;"))
        self.m6ErrLabel.setObjectName(_fromUtf8("m6ErrLabel"))
        self.m6AngDial = QtGui.QDial(self.m6SFrame)
        self.m6AngDial.setGeometry(QtCore.QRect(100, 80, 91, 81))
        self.m6AngDial.setMinimum(-150)
        self.m6AngDial.setMaximum(150)
        self.m6AngDial.setTracking(True)
        self.m6AngDial.setWrapping(False)
        self.m6AngDial.setNotchTarget(50.0)
        self.m6AngDial.setNotchesVisible(True)
        self.m6AngDial.setObjectName(_fromUtf8("m6AngDial"))
        self.m6PosDial = QtGui.QDial(self.m6SFrame)
        self.m6PosDial.setGeometry(QtCore.QRect(380, 80, 91, 81))
        self.m6PosDial.setMinimum(0)
        self.m6PosDial.setMaximum(1023)
        self.m6PosDial.setTracking(True)
        self.m6PosDial.setWrapping(False)
        self.m6PosDial.setNotchTarget(100.0)
        self.m6PosDial.setNotchesVisible(True)
        self.m6PosDial.setObjectName(_fromUtf8("m6PosDial"))
        self.m6AngNum = QtGui.QLabel(self.m6SFrame)
        self.m6AngNum.setGeometry(QtCore.QRect(120, 200, 61, 21))
        self.m6AngNum.setStyleSheet(_fromUtf8("font: 63 16pt \"KacstArt\";\n"
"border : none;"))
        self.m6AngNum.setObjectName(_fromUtf8("m6AngNum"))
        self.m6PosNum = QtGui.QLabel(self.m6SFrame)
        self.m6PosNum.setGeometry(QtCore.QRect(400, 200, 61, 21))
        self.m6PosNum.setStyleSheet(_fromUtf8("font: 63 16pt \"KacstArt\";\n"
"border : none;"))
        self.m6PosNum.setObjectName(_fromUtf8("m6PosNum"))
        self.m6TorqueNum = QtGui.QLabel(self.m6SFrame)
        self.m6TorqueNum.setGeometry(QtCore.QRect(120, 320, 61, 21))
        self.m6TorqueNum.setStyleSheet(_fromUtf8("font: 63 16pt \"KacstArt\";\n"
"border : none;"))
        self.m6TorqueNum.setObjectName(_fromUtf8("m6TorqueNum"))
        self.m6ErrNum = QtGui.QLabel(self.m6SFrame)
        self.m6ErrNum.setGeometry(QtCore.QRect(260, 440, 61, 21))
        self.m6ErrNum.setStyleSheet(_fromUtf8("font: 63 16pt \"KacstArt\";\n"
"border : none;"))
        self.m6ErrNum.setObjectName(_fromUtf8("m6ErrNum"))
        self.m6TempNum = QtGui.QLabel(self.m6SFrame)
        self.m6TempNum.setGeometry(QtCore.QRect(400, 320, 61, 21))
        self.m6TempNum.setStyleSheet(_fromUtf8("font: 63 16pt \"KacstArt\";\n"
"border : none;"))
        self.m6TempNum.setObjectName(_fromUtf8("m6TempNum"))
        self.stackedWidget.addWidget(self.m6Page)
        self.m7Page = QtGui.QWidget()
        self.m7Page.setObjectName(_fromUtf8("m7Page"))
        self.m7Label = QtGui.QLabel(self.m7Page)
        self.m7Label.setGeometry(QtCore.QRect(340, 10, 91, 21))
        self.m7Label.setStyleSheet(_fromUtf8("font: 63 16pt \"KacstArt\";\n"
"border : none;"))
        self.m7Label.setObjectName(_fromUtf8("m7Label"))
        self.m7CFrame = QtGui.QFrame(self.m7Page)
        self.m7CFrame.setGeometry(QtCore.QRect(580, 40, 211, 501))
        self.m7CFrame.setStyleSheet(_fromUtf8("border : 1px solid rgb(113, 0, 0);\n"
""))
        self.m7CFrame.setObjectName(_fromUtf8("m7CFrame"))
        self.m7GoalTSpin = QtGui.QSpinBox(self.m7CFrame)
        self.m7GoalTSpin.setGeometry(QtCore.QRect(30, 40, 151, 21))
        self.m7GoalTSpin.setStyleSheet(_fromUtf8("font: 63 13pt \"KacstArt\";"))
        self.m7GoalTSpin.setWrapping(False)
        self.m7GoalTSpin.setAccelerated(False)
        self.m7GoalTSpin.setObjectName(_fromUtf8("m7GoalTSpin"))
        self.m7GoalTLabel = QtGui.QLabel(self.m7CFrame)
        self.m7GoalTLabel.setGeometry(QtCore.QRect(60, 10, 111, 21))
        self.m7GoalTLabel.setStyleSheet(_fromUtf8("font: 63 14pt \"KacstArt\";\n"
"border : none;"))
        self.m7GoalTLabel.setObjectName(_fromUtf8("m7GoalTLabel"))
        self.m7UpdateBtn = QtGui.QPushButton(self.m7CFrame)
        self.m7UpdateBtn.setGeometry(QtCore.QRect(20, 290, 171, 41))
        self.m7UpdateBtn.setAutoFillBackground(False)
        self.m7UpdateBtn.setStyleSheet(_fromUtf8("QPushButton\n"
"{font: 63 14pt \"KacstArt\";\n"
"border : 2px solid black;\n"
"}\n"
"QPushButton:pressed\n"
"{    \n"
"    background-color : rgb(209,209,224);\n"
"}\n"
"\n"
"        "))
        self.m7UpdateBtn.setAutoDefault(False)
        self.m7UpdateBtn.setDefault(False)
        self.m7UpdateBtn.setFlat(False)
        self.m7UpdateBtn.setObjectName(_fromUtf8("m7UpdateBtn"))
        self.m7AngleLabel = QtGui.QLabel(self.m7CFrame)
        self.m7AngleLabel.setGeometry(QtCore.QRect(80, 70, 61, 21))
        self.m7AngleLabel.setStyleSheet(_fromUtf8("font: 63 14pt \"KacstArt\";\n"
"border : none;"))
        self.m7AngleLabel.setObjectName(_fromUtf8("m7AngleLabel"))
        self.m7AngleSpin = QtGui.QSpinBox(self.m7CFrame)
        self.m7AngleSpin.setGeometry(QtCore.QRect(30, 100, 151, 21))
        self.m7AngleSpin.setStyleSheet(_fromUtf8("font: 63 13pt \"KacstArt\";"))
        self.m7AngleSpin.setWrapping(False)
        self.m7AngleSpin.setAccelerated(False)
        self.m7AngleSpin.setMinimum(-150)
        self.m7AngleSpin.setMaximum(150)
        self.m7AngleSpin.setObjectName(_fromUtf8("m7AngleSpin"))
        self.m7PositionSpin = QtGui.QSpinBox(self.m7CFrame)
        self.m7PositionSpin.setGeometry(QtCore.QRect(30, 190, 151, 21))
        self.m7PositionSpin.setStyleSheet(_fromUtf8("font: 63 13pt \"KacstArt\";"))
        self.m7PositionSpin.setWrapping(False)
        self.m7PositionSpin.setAccelerated(False)
        self.m7PositionSpin.setMaximum(1023)
        self.m7PositionSpin.setObjectName(_fromUtf8("m7PositionSpin"))
        self.m7PositionLabel = QtGui.QLabel(self.m7CFrame)
        self.m7PositionLabel.setGeometry(QtCore.QRect(70, 170, 81, 21))
        self.m7PositionLabel.setStyleSheet(_fromUtf8("font: 63 14pt \"KacstArt\";\n"
"border : none;"))
        self.m7PositionLabel.setObjectName(_fromUtf8("m7PositionLabel"))
        self.m7AngleBtn = QtGui.QPushButton(self.m7CFrame)
        self.m7AngleBtn.setGeometry(QtCore.QRect(30, 130, 151, 21))
        self.m7AngleBtn.setStyleSheet(_fromUtf8("QPushButton\n"
"{font: 63 12pt \"KacstArt\";\n"
"border : 2px solid black;\n"
"}\n"
"QPushButton:pressed\n"
"{    \n"
"    background-color : rgb(209,209,224);\n"
"}\n"
"\n"
"        "))
        self.m7AngleBtn.setObjectName(_fromUtf8("m7AngleBtn"))
        self.m7PositionBtn = QtGui.QPushButton(self.m7CFrame)
        self.m7PositionBtn.setGeometry(QtCore.QRect(30, 220, 151, 21))
        self.m7PositionBtn.setStyleSheet(_fromUtf8("QPushButton\n"
"{font: 63 12pt \"KacstArt\";\n"
"border : 2px solid black;\n"
"}\n"
"QPushButton:pressed\n"
"{    \n"
"    background-color : rgb(209,209,224);\n"
"}\n"
"\n"
"        "))
        self.m7PositionBtn.setObjectName(_fromUtf8("m7PositionBtn"))
        self.m7HomeBtn = QtGui.QPushButton(self.m7CFrame)
        self.m7HomeBtn.setGeometry(QtCore.QRect(20, 370, 171, 61))
        self.m7HomeBtn.setStyleSheet(_fromUtf8("QPushButton\n"
"{font: 63 14pt \"KacstArt\";\n"
"border : 2px solid black;\n"
"}\n"
"QPushButton:pressed\n"
"{    \n"
"    background-color : rgb(209,209,224);\n"
"}\n"
"\n"
"        "))
        self.m7HomeBtn.setObjectName(_fromUtf8("m7HomeBtn"))
        self.m7SFrame = QtGui.QFrame(self.m7Page)
        self.m7SFrame.setGeometry(QtCore.QRect(10, 40, 561, 501))
        self.m7SFrame.setStyleSheet(_fromUtf8("border : 1px solid rgb(113, 0, 0);\n"
""))
        self.m7SFrame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.m7SFrame.setFrameShadow(QtGui.QFrame.Raised)
        self.m7SFrame.setObjectName(_fromUtf8("m7SFrame"))
        self.m7AngLabel = QtGui.QLabel(self.m7SFrame)
        self.m7AngLabel.setGeometry(QtCore.QRect(120, 40, 61, 21))
        self.m7AngLabel.setStyleSheet(_fromUtf8("font: 63 16pt \"KacstArt\";\n"
"border : none;"))
        self.m7AngLabel.setObjectName(_fromUtf8("m7AngLabel"))
        self.m7PosLabel = QtGui.QLabel(self.m7SFrame)
        self.m7PosLabel.setGeometry(QtCore.QRect(390, 40, 91, 21))
        self.m7PosLabel.setStyleSheet(_fromUtf8("font: 63 16pt \"KacstArt\";\n"
"border : none;"))
        self.m7PosLabel.setObjectName(_fromUtf8("m7PosLabel"))
        self.m7TorqueLabel = QtGui.QLabel(self.m7SFrame)
        self.m7TorqueLabel.setGeometry(QtCore.QRect(80, 270, 141, 21))
        self.m7TorqueLabel.setStyleSheet(_fromUtf8("font: 63 16pt \"KacstArt\";\n"
"border : none;"))
        self.m7TorqueLabel.setObjectName(_fromUtf8("m7TorqueLabel"))
        self.m7TempLabel = QtGui.QLabel(self.m7SFrame)
        self.m7TempLabel.setGeometry(QtCore.QRect(370, 270, 131, 21))
        self.m7TempLabel.setStyleSheet(_fromUtf8("font: 63 16pt \"KacstArt\";\n"
"border : none;"))
        self.m7TempLabel.setObjectName(_fromUtf8("m7TempLabel"))
        self.m7ErrLabel = QtGui.QLabel(self.m7SFrame)
        self.m7ErrLabel.setGeometry(QtCore.QRect(260, 390, 61, 21))
        self.m7ErrLabel.setStyleSheet(_fromUtf8("font: 63 16pt \"KacstArt\";\n"
"border : none;"))
        self.m7ErrLabel.setObjectName(_fromUtf8("m7ErrLabel"))
        self.m7AngDial = QtGui.QDial(self.m7SFrame)
        self.m7AngDial.setGeometry(QtCore.QRect(100, 80, 91, 81))
        self.m7AngDial.setMinimum(-150)
        self.m7AngDial.setMaximum(150)
        self.m7AngDial.setTracking(True)
        self.m7AngDial.setWrapping(False)
        self.m7AngDial.setNotchTarget(50.0)
        self.m7AngDial.setNotchesVisible(True)
        self.m7AngDial.setObjectName(_fromUtf8("m7AngDial"))
        self.m7PosDial = QtGui.QDial(self.m7SFrame)
        self.m7PosDial.setGeometry(QtCore.QRect(380, 80, 91, 81))
        self.m7PosDial.setMinimum(0)
        self.m7PosDial.setMaximum(1023)
        self.m7PosDial.setTracking(True)
        self.m7PosDial.setWrapping(False)
        self.m7PosDial.setNotchTarget(100.0)
        self.m7PosDial.setNotchesVisible(True)
        self.m7PosDial.setObjectName(_fromUtf8("m7PosDial"))
        self.m7AngNum = QtGui.QLabel(self.m7SFrame)
        self.m7AngNum.setGeometry(QtCore.QRect(120, 200, 61, 21))
        self.m7AngNum.setStyleSheet(_fromUtf8("font: 63 16pt \"KacstArt\";\n"
"border : none;"))
        self.m7AngNum.setObjectName(_fromUtf8("m7AngNum"))
        self.m7PosNum = QtGui.QLabel(self.m7SFrame)
        self.m7PosNum.setGeometry(QtCore.QRect(400, 200, 61, 21))
        self.m7PosNum.setStyleSheet(_fromUtf8("font: 63 16pt \"KacstArt\";\n"
"border : none;"))
        self.m7PosNum.setObjectName(_fromUtf8("m7PosNum"))
        self.m7TorqueNum = QtGui.QLabel(self.m7SFrame)
        self.m7TorqueNum.setGeometry(QtCore.QRect(120, 320, 61, 21))
        self.m7TorqueNum.setStyleSheet(_fromUtf8("font: 63 16pt \"KacstArt\";\n"
"border : none;"))
        self.m7TorqueNum.setObjectName(_fromUtf8("m7TorqueNum"))
        self.m7ErrNum = QtGui.QLabel(self.m7SFrame)
        self.m7ErrNum.setGeometry(QtCore.QRect(260, 440, 61, 21))
        self.m7ErrNum.setStyleSheet(_fromUtf8("font: 63 16pt \"KacstArt\";\n"
"border : none;"))
        self.m7ErrNum.setObjectName(_fromUtf8("m7ErrNum"))
        self.m7TempNum = QtGui.QLabel(self.m7SFrame)
        self.m7TempNum.setGeometry(QtCore.QRect(400, 320, 61, 21))
        self.m7TempNum.setStyleSheet(_fromUtf8("font: 63 16pt \"KacstArt\";\n"
"border : none;"))
        self.m7TempNum.setObjectName(_fromUtf8("m7TempNum"))
        self.stackedWidget.addWidget(self.m7Page)
        self.m8Page = QtGui.QWidget()
        self.m8Page.setObjectName(_fromUtf8("m8Page"))
        self.m8SFrame = QtGui.QFrame(self.m8Page)
        self.m8SFrame.setGeometry(QtCore.QRect(10, 40, 561, 501))
        self.m8SFrame.setStyleSheet(_fromUtf8("border : 1px solid rgb(113, 0, 0);\n"
""))
        self.m8SFrame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.m8SFrame.setFrameShadow(QtGui.QFrame.Raised)
        self.m8SFrame.setObjectName(_fromUtf8("m8SFrame"))
        self.m8AngLabel = QtGui.QLabel(self.m8SFrame)
        self.m8AngLabel.setGeometry(QtCore.QRect(120, 40, 61, 21))
        self.m8AngLabel.setStyleSheet(_fromUtf8("font: 63 16pt \"KacstArt\";\n"
"border : none;"))
        self.m8AngLabel.setObjectName(_fromUtf8("m8AngLabel"))
        self.m8PosLabel = QtGui.QLabel(self.m8SFrame)
        self.m8PosLabel.setGeometry(QtCore.QRect(390, 40, 91, 21))
        self.m8PosLabel.setStyleSheet(_fromUtf8("font: 63 16pt \"KacstArt\";\n"
"border : none;"))
        self.m8PosLabel.setObjectName(_fromUtf8("m8PosLabel"))
        self.m8TorqueLabel = QtGui.QLabel(self.m8SFrame)
        self.m8TorqueLabel.setGeometry(QtCore.QRect(80, 270, 141, 21))
        self.m8TorqueLabel.setStyleSheet(_fromUtf8("font: 63 16pt \"KacstArt\";\n"
"border : none;"))
        self.m8TorqueLabel.setObjectName(_fromUtf8("m8TorqueLabel"))
        self.m8TempLabel = QtGui.QLabel(self.m8SFrame)
        self.m8TempLabel.setGeometry(QtCore.QRect(370, 270, 131, 21))
        self.m8TempLabel.setStyleSheet(_fromUtf8("font: 63 16pt \"KacstArt\";\n"
"border : none;"))
        self.m8TempLabel.setObjectName(_fromUtf8("m8TempLabel"))
        self.m8ErrLabel = QtGui.QLabel(self.m8SFrame)
        self.m8ErrLabel.setGeometry(QtCore.QRect(260, 390, 61, 21))
        self.m8ErrLabel.setStyleSheet(_fromUtf8("font: 63 16pt \"KacstArt\";\n"
"border : none;"))
        self.m8ErrLabel.setObjectName(_fromUtf8("m8ErrLabel"))
        self.m8AngDial = QtGui.QDial(self.m8SFrame)
        self.m8AngDial.setGeometry(QtCore.QRect(100, 80, 91, 81))
        self.m8AngDial.setMinimum(-150)
        self.m8AngDial.setMaximum(150)
        self.m8AngDial.setTracking(True)
        self.m8AngDial.setWrapping(False)
        self.m8AngDial.setNotchTarget(50.0)
        self.m8AngDial.setNotchesVisible(True)
        self.m8AngDial.setObjectName(_fromUtf8("m8AngDial"))
        self.m8PosDial = QtGui.QDial(self.m8SFrame)
        self.m8PosDial.setGeometry(QtCore.QRect(380, 80, 91, 81))
        self.m8PosDial.setMinimum(0)
        self.m8PosDial.setMaximum(1023)
        self.m8PosDial.setTracking(True)
        self.m8PosDial.setWrapping(False)
        self.m8PosDial.setNotchTarget(100.0)
        self.m8PosDial.setNotchesVisible(True)
        self.m8PosDial.setObjectName(_fromUtf8("m8PosDial"))
        self.m8AngNum = QtGui.QLabel(self.m8SFrame)
        self.m8AngNum.setGeometry(QtCore.QRect(120, 200, 61, 21))
        self.m8AngNum.setStyleSheet(_fromUtf8("font: 63 16pt \"KacstArt\";\n"
"border : none;"))
        self.m8AngNum.setObjectName(_fromUtf8("m8AngNum"))
        self.m8PosNum = QtGui.QLabel(self.m8SFrame)
        self.m8PosNum.setGeometry(QtCore.QRect(400, 200, 61, 21))
        self.m8PosNum.setStyleSheet(_fromUtf8("font: 63 16pt \"KacstArt\";\n"
"border : none;"))
        self.m8PosNum.setObjectName(_fromUtf8("m8PosNum"))
        self.m8TorqueNum = QtGui.QLabel(self.m8SFrame)
        self.m8TorqueNum.setGeometry(QtCore.QRect(120, 320, 61, 21))
        self.m8TorqueNum.setStyleSheet(_fromUtf8("font: 63 16pt \"KacstArt\";\n"
"border : none;"))
        self.m8TorqueNum.setObjectName(_fromUtf8("m8TorqueNum"))
        self.m8ErrNum = QtGui.QLabel(self.m8SFrame)
        self.m8ErrNum.setGeometry(QtCore.QRect(260, 440, 61, 21))
        self.m8ErrNum.setStyleSheet(_fromUtf8("font: 63 16pt \"KacstArt\";\n"
"border : none;"))
        self.m8ErrNum.setObjectName(_fromUtf8("m8ErrNum"))
        self.m8TempNum = QtGui.QLabel(self.m8SFrame)
        self.m8TempNum.setGeometry(QtCore.QRect(400, 320, 61, 21))
        self.m8TempNum.setStyleSheet(_fromUtf8("font: 63 16pt \"KacstArt\";\n"
"border : none;"))
        self.m8TempNum.setObjectName(_fromUtf8("m8TempNum"))
        self.m8Label = QtGui.QLabel(self.m8Page)
        self.m8Label.setGeometry(QtCore.QRect(340, 10, 91, 21))
        self.m8Label.setStyleSheet(_fromUtf8("font: 63 16pt \"KacstArt\";\n"
"border : none;"))
        self.m8Label.setObjectName(_fromUtf8("m8Label"))
        self.m8CFrame = QtGui.QFrame(self.m8Page)
        self.m8CFrame.setGeometry(QtCore.QRect(580, 40, 211, 501))
        self.m8CFrame.setStyleSheet(_fromUtf8("border : 1px solid rgb(113, 0, 0);\n"
""))
        self.m8CFrame.setObjectName(_fromUtf8("m8CFrame"))
        self.m8GoalTSpin = QtGui.QSpinBox(self.m8CFrame)
        self.m8GoalTSpin.setGeometry(QtCore.QRect(30, 40, 151, 21))
        self.m8GoalTSpin.setStyleSheet(_fromUtf8("font: 63 13pt \"KacstArt\";"))
        self.m8GoalTSpin.setWrapping(False)
        self.m8GoalTSpin.setAccelerated(False)
        self.m8GoalTSpin.setObjectName(_fromUtf8("m8GoalTSpin"))
        self.m8GoalTLabel = QtGui.QLabel(self.m8CFrame)
        self.m8GoalTLabel.setGeometry(QtCore.QRect(60, 10, 111, 21))
        self.m8GoalTLabel.setStyleSheet(_fromUtf8("font: 63 14pt \"KacstArt\";\n"
"border : none;"))
        self.m8GoalTLabel.setObjectName(_fromUtf8("m8GoalTLabel"))
        self.m8UpdateBtn = QtGui.QPushButton(self.m8CFrame)
        self.m8UpdateBtn.setGeometry(QtCore.QRect(20, 290, 171, 41))
        self.m8UpdateBtn.setAutoFillBackground(False)
        self.m8UpdateBtn.setStyleSheet(_fromUtf8("QPushButton\n"
"{font: 63 14pt \"KacstArt\";\n"
"border : 2px solid black;\n"
"}\n"
"QPushButton:pressed\n"
"{    \n"
"    background-color : rgb(209,209,224);\n"
"}\n"
"\n"
"        "))
        self.m8UpdateBtn.setAutoDefault(False)
        self.m8UpdateBtn.setDefault(False)
        self.m8UpdateBtn.setFlat(False)
        self.m8UpdateBtn.setObjectName(_fromUtf8("m8UpdateBtn"))
        self.m8AngleLabel = QtGui.QLabel(self.m8CFrame)
        self.m8AngleLabel.setGeometry(QtCore.QRect(80, 70, 61, 21))
        self.m8AngleLabel.setStyleSheet(_fromUtf8("font: 63 14pt \"KacstArt\";\n"
"border : none;"))
        self.m8AngleLabel.setObjectName(_fromUtf8("m8AngleLabel"))
        self.m8AngleSpin = QtGui.QSpinBox(self.m8CFrame)
        self.m8AngleSpin.setGeometry(QtCore.QRect(30, 100, 151, 21))
        self.m8AngleSpin.setStyleSheet(_fromUtf8("font: 63 13pt \"KacstArt\";"))
        self.m8AngleSpin.setWrapping(False)
        self.m8AngleSpin.setAccelerated(False)
        self.m8AngleSpin.setMinimum(-150)
        self.m8AngleSpin.setMaximum(150)
        self.m8AngleSpin.setObjectName(_fromUtf8("m8AngleSpin"))
        self.m8PositionSpin = QtGui.QSpinBox(self.m8CFrame)
        self.m8PositionSpin.setGeometry(QtCore.QRect(30, 190, 151, 21))
        self.m8PositionSpin.setStyleSheet(_fromUtf8("font: 63 13pt \"KacstArt\";"))
        self.m8PositionSpin.setWrapping(False)
        self.m8PositionSpin.setAccelerated(False)
        self.m8PositionSpin.setMaximum(1023)
        self.m8PositionSpin.setObjectName(_fromUtf8("m8PositionSpin"))
        self.m8PositionLabel = QtGui.QLabel(self.m8CFrame)
        self.m8PositionLabel.setGeometry(QtCore.QRect(70, 170, 81, 21))
        self.m8PositionLabel.setStyleSheet(_fromUtf8("font: 63 14pt \"KacstArt\";\n"
"border : none;"))
        self.m8PositionLabel.setObjectName(_fromUtf8("m8PositionLabel"))
        self.m8AngleBtn = QtGui.QPushButton(self.m8CFrame)
        self.m8AngleBtn.setGeometry(QtCore.QRect(30, 130, 151, 21))
        self.m8AngleBtn.setStyleSheet(_fromUtf8("QPushButton\n"
"{font: 63 12pt \"KacstArt\";\n"
"border : 2px solid black;\n"
"}\n"
"QPushButton:pressed\n"
"{    \n"
"    background-color : rgb(209,209,224);\n"
"}\n"
"\n"
"        "))
        self.m8AngleBtn.setObjectName(_fromUtf8("m8AngleBtn"))
        self.m8PositionBtn = QtGui.QPushButton(self.m8CFrame)
        self.m8PositionBtn.setGeometry(QtCore.QRect(30, 220, 151, 21))
        self.m8PositionBtn.setStyleSheet(_fromUtf8("QPushButton\n"
"{font: 63 12pt \"KacstArt\";\n"
"border : 2px solid black;\n"
"}\n"
"QPushButton:pressed\n"
"{    \n"
"    background-color : rgb(209,209,224);\n"
"}\n"
"\n"
"        "))
        self.m8PositionBtn.setObjectName(_fromUtf8("m8PositionBtn"))
        self.m8HomeBtn = QtGui.QPushButton(self.m8CFrame)
        self.m8HomeBtn.setGeometry(QtCore.QRect(20, 370, 171, 61))
        self.m8HomeBtn.setStyleSheet(_fromUtf8("QPushButton\n"
"{font: 63 14pt \"KacstArt\";\n"
"border : 2px solid black;\n"
"}\n"
"QPushButton:pressed\n"
"{    \n"
"    background-color : rgb(209,209,224);\n"
"}\n"
"\n"
"        "))
        self.m8HomeBtn.setObjectName(_fromUtf8("m8HomeBtn"))
        self.stackedWidget.addWidget(self.m8Page)
        self.m9Page = QtGui.QWidget()
        self.m9Page.setObjectName(_fromUtf8("m9Page"))
        self.m9Label = QtGui.QLabel(self.m9Page)
        self.m9Label.setGeometry(QtCore.QRect(340, 10, 91, 21))
        self.m9Label.setStyleSheet(_fromUtf8("font: 63 16pt \"KacstArt\";\n"
"border : none;"))
        self.m9Label.setObjectName(_fromUtf8("m9Label"))
        self.m9CFrame = QtGui.QFrame(self.m9Page)
        self.m9CFrame.setGeometry(QtCore.QRect(580, 40, 211, 501))
        self.m9CFrame.setStyleSheet(_fromUtf8("border : 1px solid rgb(113, 0, 0);\n"
""))
        self.m9CFrame.setObjectName(_fromUtf8("m9CFrame"))
        self.m9GoalTSpin = QtGui.QSpinBox(self.m9CFrame)
        self.m9GoalTSpin.setGeometry(QtCore.QRect(30, 40, 151, 21))
        self.m9GoalTSpin.setStyleSheet(_fromUtf8("font: 63 13pt \"KacstArt\";"))
        self.m9GoalTSpin.setWrapping(False)
        self.m9GoalTSpin.setAccelerated(False)
        self.m9GoalTSpin.setObjectName(_fromUtf8("m9GoalTSpin"))
        self.m9GoalTLabel = QtGui.QLabel(self.m9CFrame)
        self.m9GoalTLabel.setGeometry(QtCore.QRect(60, 10, 111, 21))
        self.m9GoalTLabel.setStyleSheet(_fromUtf8("font: 63 14pt \"KacstArt\";\n"
"border : none;"))
        self.m9GoalTLabel.setObjectName(_fromUtf8("m9GoalTLabel"))
        self.m9UpdateBtn = QtGui.QPushButton(self.m9CFrame)
        self.m9UpdateBtn.setGeometry(QtCore.QRect(20, 290, 171, 41))
        self.m9UpdateBtn.setAutoFillBackground(False)
        self.m9UpdateBtn.setStyleSheet(_fromUtf8("QPushButton\n"
"{font: 63 14pt \"KacstArt\";\n"
"border : 2px solid black;\n"
"}\n"
"QPushButton:pressed\n"
"{    \n"
"    background-color : rgb(209,209,224);\n"
"}\n"
"\n"
"        "))
        self.m9UpdateBtn.setAutoDefault(False)
        self.m9UpdateBtn.setDefault(False)
        self.m9UpdateBtn.setFlat(False)
        self.m9UpdateBtn.setObjectName(_fromUtf8("m9UpdateBtn"))
        self.m9AngleLabel = QtGui.QLabel(self.m9CFrame)
        self.m9AngleLabel.setGeometry(QtCore.QRect(80, 70, 61, 21))
        self.m9AngleLabel.setStyleSheet(_fromUtf8("font: 63 14pt \"KacstArt\";\n"
"border : none;"))
        self.m9AngleLabel.setObjectName(_fromUtf8("m9AngleLabel"))
        self.m9AngleSpin = QtGui.QSpinBox(self.m9CFrame)
        self.m9AngleSpin.setGeometry(QtCore.QRect(30, 100, 151, 21))
        self.m9AngleSpin.setStyleSheet(_fromUtf8("font: 63 13pt \"KacstArt\";"))
        self.m9AngleSpin.setWrapping(False)
        self.m9AngleSpin.setAccelerated(False)
        self.m9AngleSpin.setMinimum(-150)
        self.m9AngleSpin.setMaximum(150)
        self.m9AngleSpin.setObjectName(_fromUtf8("m9AngleSpin"))
        self.m9PositionSpin = QtGui.QSpinBox(self.m9CFrame)
        self.m9PositionSpin.setGeometry(QtCore.QRect(30, 190, 151, 21))
        self.m9PositionSpin.setStyleSheet(_fromUtf8("font: 63 13pt \"KacstArt\";"))
        self.m9PositionSpin.setWrapping(False)
        self.m9PositionSpin.setAccelerated(False)
        self.m9PositionSpin.setMaximum(1023)
        self.m9PositionSpin.setObjectName(_fromUtf8("m9PositionSpin"))
        self.m9PositionLabel = QtGui.QLabel(self.m9CFrame)
        self.m9PositionLabel.setGeometry(QtCore.QRect(70, 170, 81, 21))
        self.m9PositionLabel.setStyleSheet(_fromUtf8("font: 63 14pt \"KacstArt\";\n"
"border : none;"))
        self.m9PositionLabel.setObjectName(_fromUtf8("m9PositionLabel"))
        self.m9AngleBtn = QtGui.QPushButton(self.m9CFrame)
        self.m9AngleBtn.setGeometry(QtCore.QRect(30, 130, 151, 21))
        self.m9AngleBtn.setStyleSheet(_fromUtf8("QPushButton\n"
"{font: 63 12pt \"KacstArt\";\n"
"border : 2px solid black;\n"
"}\n"
"QPushButton:pressed\n"
"{    \n"
"    background-color : rgb(209,209,224);\n"
"}\n"
"\n"
"        "))
        self.m9AngleBtn.setObjectName(_fromUtf8("m9AngleBtn"))
        self.m9PositionBtn = QtGui.QPushButton(self.m9CFrame)
        self.m9PositionBtn.setGeometry(QtCore.QRect(30, 220, 151, 21))
        self.m9PositionBtn.setStyleSheet(_fromUtf8("QPushButton\n"
"{font: 63 12pt \"KacstArt\";\n"
"border : 2px solid black;\n"
"}\n"
"QPushButton:pressed\n"
"{    \n"
"    background-color : rgb(209,209,224);\n"
"}\n"
"\n"
"        "))
        self.m9PositionBtn.setObjectName(_fromUtf8("m9PositionBtn"))
        self.m9HomeBtn = QtGui.QPushButton(self.m9CFrame)
        self.m9HomeBtn.setGeometry(QtCore.QRect(20, 370, 171, 61))
        self.m9HomeBtn.setStyleSheet(_fromUtf8("QPushButton\n"
"{font: 63 14pt \"KacstArt\";\n"
"border : 2px solid black;\n"
"}\n"
"QPushButton:pressed\n"
"{    \n"
"    background-color : rgb(209,209,224);\n"
"}\n"
"\n"
"        "))
        self.m9HomeBtn.setObjectName(_fromUtf8("m9HomeBtn"))
        self.m9SFrame = QtGui.QFrame(self.m9Page)
        self.m9SFrame.setGeometry(QtCore.QRect(10, 40, 561, 501))
        self.m9SFrame.setStyleSheet(_fromUtf8("border : 1px solid rgb(113, 0, 0);\n"
""))
        self.m9SFrame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.m9SFrame.setFrameShadow(QtGui.QFrame.Raised)
        self.m9SFrame.setObjectName(_fromUtf8("m9SFrame"))
        self.m9AngLabel = QtGui.QLabel(self.m9SFrame)
        self.m9AngLabel.setGeometry(QtCore.QRect(120, 40, 61, 21))
        self.m9AngLabel.setStyleSheet(_fromUtf8("font: 63 16pt \"KacstArt\";\n"
"border : none;"))
        self.m9AngLabel.setObjectName(_fromUtf8("m9AngLabel"))
        self.m9PosLabel = QtGui.QLabel(self.m9SFrame)
        self.m9PosLabel.setGeometry(QtCore.QRect(390, 40, 91, 21))
        self.m9PosLabel.setStyleSheet(_fromUtf8("font: 63 16pt \"KacstArt\";\n"
"border : none;"))
        self.m9PosLabel.setObjectName(_fromUtf8("m9PosLabel"))
        self.m9TorqueLabel = QtGui.QLabel(self.m9SFrame)
        self.m9TorqueLabel.setGeometry(QtCore.QRect(80, 270, 141, 21))
        self.m9TorqueLabel.setStyleSheet(_fromUtf8("font: 63 16pt \"KacstArt\";\n"
"border : none;"))
        self.m9TorqueLabel.setObjectName(_fromUtf8("m9TorqueLabel"))
        self.m9TempLabel = QtGui.QLabel(self.m9SFrame)
        self.m9TempLabel.setGeometry(QtCore.QRect(370, 270, 131, 21))
        self.m9TempLabel.setStyleSheet(_fromUtf8("font: 63 16pt \"KacstArt\";\n"
"border : none;"))
        self.m9TempLabel.setObjectName(_fromUtf8("m9TempLabel"))
        self.m9ErrLabel = QtGui.QLabel(self.m9SFrame)
        self.m9ErrLabel.setGeometry(QtCore.QRect(260, 390, 61, 21))
        self.m9ErrLabel.setStyleSheet(_fromUtf8("font: 63 16pt \"KacstArt\";\n"
"border : none;"))
        self.m9ErrLabel.setObjectName(_fromUtf8("m9ErrLabel"))
        self.m9AngDial = QtGui.QDial(self.m9SFrame)
        self.m9AngDial.setGeometry(QtCore.QRect(100, 80, 91, 81))
        self.m9AngDial.setMinimum(-150)
        self.m9AngDial.setMaximum(150)
        self.m9AngDial.setTracking(True)
        self.m9AngDial.setWrapping(False)
        self.m9AngDial.setNotchTarget(50.0)
        self.m9AngDial.setNotchesVisible(True)
        self.m9AngDial.setObjectName(_fromUtf8("m9AngDial"))
        self.m9PosDial = QtGui.QDial(self.m9SFrame)
        self.m9PosDial.setGeometry(QtCore.QRect(380, 80, 91, 81))
        self.m9PosDial.setMinimum(0)
        self.m9PosDial.setMaximum(1023)
        self.m9PosDial.setTracking(True)
        self.m9PosDial.setWrapping(False)
        self.m9PosDial.setNotchTarget(100.0)
        self.m9PosDial.setNotchesVisible(True)
        self.m9PosDial.setObjectName(_fromUtf8("m9PosDial"))
        self.m9AngNum = QtGui.QLabel(self.m9SFrame)
        self.m9AngNum.setGeometry(QtCore.QRect(120, 200, 61, 21))
        self.m9AngNum.setStyleSheet(_fromUtf8("font: 63 16pt \"KacstArt\";\n"
"border : none;"))
        self.m9AngNum.setObjectName(_fromUtf8("m9AngNum"))
        self.m9PosNum = QtGui.QLabel(self.m9SFrame)
        self.m9PosNum.setGeometry(QtCore.QRect(400, 200, 61, 21))
        self.m9PosNum.setStyleSheet(_fromUtf8("font: 63 16pt \"KacstArt\";\n"
"border : none;"))
        self.m9PosNum.setObjectName(_fromUtf8("m9PosNum"))
        self.m9TorqueNum = QtGui.QLabel(self.m9SFrame)
        self.m9TorqueNum.setGeometry(QtCore.QRect(120, 320, 61, 21))
        self.m9TorqueNum.setStyleSheet(_fromUtf8("font: 63 16pt \"KacstArt\";\n"
"border : none;"))
        self.m9TorqueNum.setObjectName(_fromUtf8("m9TorqueNum"))
        self.m9ErrNum = QtGui.QLabel(self.m9SFrame)
        self.m9ErrNum.setGeometry(QtCore.QRect(260, 440, 61, 21))
        self.m9ErrNum.setStyleSheet(_fromUtf8("font: 63 16pt \"KacstArt\";\n"
"border : none;"))
        self.m9ErrNum.setObjectName(_fromUtf8("m9ErrNum"))
        self.m9TempNum = QtGui.QLabel(self.m9SFrame)
        self.m9TempNum.setGeometry(QtCore.QRect(400, 320, 61, 21))
        self.m9TempNum.setStyleSheet(_fromUtf8("font: 63 16pt \"KacstArt\";\n"
"border : none;"))
        self.m9TempNum.setObjectName(_fromUtf8("m9TempNum"))
        self.stackedWidget.addWidget(self.m9Page)
        self.m10Page = QtGui.QWidget()
        self.m10Page.setObjectName(_fromUtf8("m10Page"))
        self.m10Label = QtGui.QLabel(self.m10Page)
        self.m10Label.setGeometry(QtCore.QRect(340, 10, 91, 21))
        self.m10Label.setStyleSheet(_fromUtf8("font: 63 16pt \"KacstArt\";\n"
"border : none;"))
        self.m10Label.setObjectName(_fromUtf8("m10Label"))
        self.m10CFrame = QtGui.QFrame(self.m10Page)
        self.m10CFrame.setGeometry(QtCore.QRect(580, 40, 211, 501))
        self.m10CFrame.setStyleSheet(_fromUtf8("border : 1px solid rgb(113, 0, 0);\n"
""))
        self.m10CFrame.setObjectName(_fromUtf8("m10CFrame"))
        self.m10GoalTSpin = QtGui.QSpinBox(self.m10CFrame)
        self.m10GoalTSpin.setGeometry(QtCore.QRect(30, 40, 151, 21))
        self.m10GoalTSpin.setStyleSheet(_fromUtf8("font: 63 13pt \"KacstArt\";"))
        self.m10GoalTSpin.setWrapping(False)
        self.m10GoalTSpin.setAccelerated(False)
        self.m10GoalTSpin.setObjectName(_fromUtf8("m10GoalTSpin"))
        self.m10GoalTLabel = QtGui.QLabel(self.m10CFrame)
        self.m10GoalTLabel.setGeometry(QtCore.QRect(60, 10, 111, 21))
        self.m10GoalTLabel.setStyleSheet(_fromUtf8("font: 63 14pt \"KacstArt\";\n"
"border : none;"))
        self.m10GoalTLabel.setObjectName(_fromUtf8("m10GoalTLabel"))
        self.m10UpdateBtn = QtGui.QPushButton(self.m10CFrame)
        self.m10UpdateBtn.setGeometry(QtCore.QRect(20, 290, 171, 41))
        self.m10UpdateBtn.setAutoFillBackground(False)
        self.m10UpdateBtn.setStyleSheet(_fromUtf8("QPushButton\n"
"{font: 63 14pt \"KacstArt\";\n"
"border : 2px solid black;\n"
"}\n"
"QPushButton:pressed\n"
"{    \n"
"    background-color : rgb(209,209,224);\n"
"}\n"
"\n"
"        "))
        self.m10UpdateBtn.setAutoDefault(False)
        self.m10UpdateBtn.setDefault(False)
        self.m10UpdateBtn.setFlat(False)
        self.m10UpdateBtn.setObjectName(_fromUtf8("m10UpdateBtn"))
        self.m10AngleLabel = QtGui.QLabel(self.m10CFrame)
        self.m10AngleLabel.setGeometry(QtCore.QRect(80, 70, 61, 21))
        self.m10AngleLabel.setStyleSheet(_fromUtf8("font: 63 14pt \"KacstArt\";\n"
"border : none;"))
        self.m10AngleLabel.setObjectName(_fromUtf8("m10AngleLabel"))
        self.m10AngleSpin = QtGui.QSpinBox(self.m10CFrame)
        self.m10AngleSpin.setGeometry(QtCore.QRect(30, 100, 151, 21))
        self.m10AngleSpin.setStyleSheet(_fromUtf8("font: 63 13pt \"KacstArt\";"))
        self.m10AngleSpin.setWrapping(False)
        self.m10AngleSpin.setAccelerated(False)
        self.m10AngleSpin.setMinimum(-150)
        self.m10AngleSpin.setMaximum(150)
        self.m10AngleSpin.setObjectName(_fromUtf8("m10AngleSpin"))
        self.m10PositionSpin = QtGui.QSpinBox(self.m10CFrame)
        self.m10PositionSpin.setGeometry(QtCore.QRect(30, 190, 151, 21))
        self.m10PositionSpin.setStyleSheet(_fromUtf8("font: 63 13pt \"KacstArt\";"))
        self.m10PositionSpin.setWrapping(False)
        self.m10PositionSpin.setAccelerated(False)
        self.m10PositionSpin.setMaximum(1023)
        self.m10PositionSpin.setObjectName(_fromUtf8("m10PositionSpin"))
        self.m10PositionLabel = QtGui.QLabel(self.m10CFrame)
        self.m10PositionLabel.setGeometry(QtCore.QRect(70, 170, 81, 21))
        self.m10PositionLabel.setStyleSheet(_fromUtf8("font: 63 14pt \"KacstArt\";\n"
"border : none;"))
        self.m10PositionLabel.setObjectName(_fromUtf8("m10PositionLabel"))
        self.m10AngleBtn = QtGui.QPushButton(self.m10CFrame)
        self.m10AngleBtn.setGeometry(QtCore.QRect(30, 130, 151, 21))
        self.m10AngleBtn.setStyleSheet(_fromUtf8("QPushButton\n"
"{font: 63 12pt \"KacstArt\";\n"
"border : 2px solid black;\n"
"}\n"
"QPushButton:pressed\n"
"{    \n"
"    background-color : rgb(209,209,224);\n"
"}\n"
"\n"
"        "))
        self.m10AngleBtn.setObjectName(_fromUtf8("m10AngleBtn"))
        self.m10PositionBtn = QtGui.QPushButton(self.m10CFrame)
        self.m10PositionBtn.setGeometry(QtCore.QRect(30, 220, 151, 21))
        self.m10PositionBtn.setStyleSheet(_fromUtf8("QPushButton\n"
"{font: 63 12pt \"KacstArt\";\n"
"border : 2px solid black;\n"
"}\n"
"QPushButton:pressed\n"
"{    \n"
"    background-color : rgb(209,209,224);\n"
"}\n"
"\n"
"        "))
        self.m10PositionBtn.setObjectName(_fromUtf8("m10PositionBtn"))
        self.m10HomeBtn = QtGui.QPushButton(self.m10CFrame)
        self.m10HomeBtn.setGeometry(QtCore.QRect(20, 370, 171, 61))
        self.m10HomeBtn.setStyleSheet(_fromUtf8("QPushButton\n"
"{font: 63 14pt \"KacstArt\";\n"
"border : 2px solid black;\n"
"}\n"
"QPushButton:pressed\n"
"{    \n"
"    background-color : rgb(209,209,224);\n"
"}\n"
"\n"
"        "))
        self.m10HomeBtn.setObjectName(_fromUtf8("m10HomeBtn"))
        self.m10SFrame = QtGui.QFrame(self.m10Page)
        self.m10SFrame.setGeometry(QtCore.QRect(10, 40, 561, 501))
        self.m10SFrame.setStyleSheet(_fromUtf8("border : 1px solid rgb(113, 0, 0);\n"
""))
        self.m10SFrame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.m10SFrame.setFrameShadow(QtGui.QFrame.Raised)
        self.m10SFrame.setObjectName(_fromUtf8("m10SFrame"))
        self.m10AngLabel = QtGui.QLabel(self.m10SFrame)
        self.m10AngLabel.setGeometry(QtCore.QRect(120, 40, 61, 21))
        self.m10AngLabel.setStyleSheet(_fromUtf8("font: 63 16pt \"KacstArt\";\n"
"border : none;"))
        self.m10AngLabel.setObjectName(_fromUtf8("m10AngLabel"))
        self.m10PosLabel = QtGui.QLabel(self.m10SFrame)
        self.m10PosLabel.setGeometry(QtCore.QRect(390, 40, 91, 21))
        self.m10PosLabel.setStyleSheet(_fromUtf8("font: 63 16pt \"KacstArt\";\n"
"border : none;"))
        self.m10PosLabel.setObjectName(_fromUtf8("m10PosLabel"))
        self.m10TorqueLabel = QtGui.QLabel(self.m10SFrame)
        self.m10TorqueLabel.setGeometry(QtCore.QRect(80, 270, 141, 21))
        self.m10TorqueLabel.setStyleSheet(_fromUtf8("font: 63 16pt \"KacstArt\";\n"
"border : none;"))
        self.m10TorqueLabel.setObjectName(_fromUtf8("m10TorqueLabel"))
        self.m10TempLabel = QtGui.QLabel(self.m10SFrame)
        self.m10TempLabel.setGeometry(QtCore.QRect(370, 270, 131, 21))
        self.m10TempLabel.setStyleSheet(_fromUtf8("font: 63 16pt \"KacstArt\";\n"
"border : none;"))
        self.m10TempLabel.setObjectName(_fromUtf8("m10TempLabel"))
        self.m10ErrLabel = QtGui.QLabel(self.m10SFrame)
        self.m10ErrLabel.setGeometry(QtCore.QRect(260, 390, 61, 21))
        self.m10ErrLabel.setStyleSheet(_fromUtf8("font: 63 16pt \"KacstArt\";\n"
"border : none;"))
        self.m10ErrLabel.setObjectName(_fromUtf8("m10ErrLabel"))
        self.m10AngDial = QtGui.QDial(self.m10SFrame)
        self.m10AngDial.setGeometry(QtCore.QRect(100, 80, 91, 81))
        self.m10AngDial.setMinimum(-150)
        self.m10AngDial.setMaximum(150)
        self.m10AngDial.setTracking(True)
        self.m10AngDial.setWrapping(False)
        self.m10AngDial.setNotchTarget(50.0)
        self.m10AngDial.setNotchesVisible(True)
        self.m10AngDial.setObjectName(_fromUtf8("m10AngDial"))
        self.m10PosDial = QtGui.QDial(self.m10SFrame)
        self.m10PosDial.setGeometry(QtCore.QRect(380, 80, 91, 81))
        self.m10PosDial.setMinimum(0)
        self.m10PosDial.setMaximum(1023)
        self.m10PosDial.setTracking(True)
        self.m10PosDial.setWrapping(False)
        self.m10PosDial.setNotchTarget(100.0)
        self.m10PosDial.setNotchesVisible(True)
        self.m10PosDial.setObjectName(_fromUtf8("m10PosDial"))
        self.m10AngNum = QtGui.QLabel(self.m10SFrame)
        self.m10AngNum.setGeometry(QtCore.QRect(120, 200, 61, 21))
        self.m10AngNum.setStyleSheet(_fromUtf8("font: 63 16pt \"KacstArt\";\n"
"border : none;"))
        self.m10AngNum.setObjectName(_fromUtf8("m10AngNum"))
        self.m10PosNum = QtGui.QLabel(self.m10SFrame)
        self.m10PosNum.setGeometry(QtCore.QRect(400, 200, 61, 21))
        self.m10PosNum.setStyleSheet(_fromUtf8("font: 63 16pt \"KacstArt\";\n"
"border : none;"))
        self.m10PosNum.setObjectName(_fromUtf8("m10PosNum"))
        self.m10TorqueNum = QtGui.QLabel(self.m10SFrame)
        self.m10TorqueNum.setGeometry(QtCore.QRect(120, 320, 61, 21))
        self.m10TorqueNum.setStyleSheet(_fromUtf8("font: 63 16pt \"KacstArt\";\n"
"border : none;"))
        self.m10TorqueNum.setObjectName(_fromUtf8("m10TorqueNum"))
        self.m10ErrNum = QtGui.QLabel(self.m10SFrame)
        self.m10ErrNum.setGeometry(QtCore.QRect(260, 440, 61, 21))
        self.m10ErrNum.setStyleSheet(_fromUtf8("font: 63 16pt \"KacstArt\";\n"
"border : none;"))
        self.m10ErrNum.setObjectName(_fromUtf8("m10ErrNum"))
        self.m10TempNum = QtGui.QLabel(self.m10SFrame)
        self.m10TempNum.setGeometry(QtCore.QRect(400, 320, 61, 21))
        self.m10TempNum.setStyleSheet(_fromUtf8("font: 63 16pt \"KacstArt\";\n"
"border : none;"))
        self.m10TempNum.setObjectName(_fromUtf8("m10TempNum"))
        self.stackedWidget.addWidget(self.m10Page)
        self.m11Page = QtGui.QWidget()
        self.m11Page.setObjectName(_fromUtf8("m11Page"))
        self.m11Label = QtGui.QLabel(self.m11Page)
        self.m11Label.setGeometry(QtCore.QRect(340, 10, 91, 21))
        self.m11Label.setStyleSheet(_fromUtf8("font: 63 16pt \"KacstArt\";\n"
"border : none;"))
        self.m11Label.setObjectName(_fromUtf8("m11Label"))
        self.m11CFrame = QtGui.QFrame(self.m11Page)
        self.m11CFrame.setGeometry(QtCore.QRect(580, 40, 211, 501))
        self.m11CFrame.setStyleSheet(_fromUtf8("border : 1px solid rgb(113, 0, 0);\n"
""))
        self.m11CFrame.setObjectName(_fromUtf8("m11CFrame"))
        self.m11GoalTSpin = QtGui.QSpinBox(self.m11CFrame)
        self.m11GoalTSpin.setGeometry(QtCore.QRect(30, 40, 151, 21))
        self.m11GoalTSpin.setStyleSheet(_fromUtf8("font: 63 13pt \"KacstArt\";"))
        self.m11GoalTSpin.setWrapping(False)
        self.m11GoalTSpin.setAccelerated(False)
        self.m11GoalTSpin.setObjectName(_fromUtf8("m11GoalTSpin"))
        self.m11GoalTLabel = QtGui.QLabel(self.m11CFrame)
        self.m11GoalTLabel.setGeometry(QtCore.QRect(60, 10, 111, 21))
        self.m11GoalTLabel.setStyleSheet(_fromUtf8("font: 63 14pt \"KacstArt\";\n"
"border : none;"))
        self.m11GoalTLabel.setObjectName(_fromUtf8("m11GoalTLabel"))
        self.m11UpdateBtn = QtGui.QPushButton(self.m11CFrame)
        self.m11UpdateBtn.setGeometry(QtCore.QRect(20, 290, 171, 41))
        self.m11UpdateBtn.setAutoFillBackground(False)
        self.m11UpdateBtn.setStyleSheet(_fromUtf8("QPushButton\n"
"{font: 63 14pt \"KacstArt\";\n"
"border : 2px solid black;\n"
"}\n"
"QPushButton:pressed\n"
"{    \n"
"    background-color : rgb(209,209,224);\n"
"}\n"
"\n"
"        "))
        self.m11UpdateBtn.setAutoDefault(False)
        self.m11UpdateBtn.setDefault(False)
        self.m11UpdateBtn.setFlat(False)
        self.m11UpdateBtn.setObjectName(_fromUtf8("m11UpdateBtn"))
        self.m11AngleLabel = QtGui.QLabel(self.m11CFrame)
        self.m11AngleLabel.setGeometry(QtCore.QRect(80, 70, 61, 21))
        self.m11AngleLabel.setStyleSheet(_fromUtf8("font: 63 14pt \"KacstArt\";\n"
"border : none;"))
        self.m11AngleLabel.setObjectName(_fromUtf8("m11AngleLabel"))
        self.m11AngleSpin = QtGui.QSpinBox(self.m11CFrame)
        self.m11AngleSpin.setGeometry(QtCore.QRect(30, 100, 151, 21))
        self.m11AngleSpin.setStyleSheet(_fromUtf8("font: 63 13pt \"KacstArt\";"))
        self.m11AngleSpin.setWrapping(False)
        self.m11AngleSpin.setAccelerated(False)
        self.m11AngleSpin.setMinimum(-150)
        self.m11AngleSpin.setMaximum(150)
        self.m11AngleSpin.setObjectName(_fromUtf8("m11AngleSpin"))
        self.m11PositionSpin = QtGui.QSpinBox(self.m11CFrame)
        self.m11PositionSpin.setGeometry(QtCore.QRect(30, 190, 151, 21))
        self.m11PositionSpin.setStyleSheet(_fromUtf8("font: 63 13pt \"KacstArt\";"))
        self.m11PositionSpin.setWrapping(False)
        self.m11PositionSpin.setAccelerated(False)
        self.m11PositionSpin.setMaximum(1023)
        self.m11PositionSpin.setObjectName(_fromUtf8("m11PositionSpin"))
        self.m11PositionLabel = QtGui.QLabel(self.m11CFrame)
        self.m11PositionLabel.setGeometry(QtCore.QRect(70, 170, 81, 21))
        self.m11PositionLabel.setStyleSheet(_fromUtf8("font: 63 14pt \"KacstArt\";\n"
"border : none;"))
        self.m11PositionLabel.setObjectName(_fromUtf8("m11PositionLabel"))
        self.m11AngleBtn = QtGui.QPushButton(self.m11CFrame)
        self.m11AngleBtn.setGeometry(QtCore.QRect(30, 130, 151, 21))
        self.m11AngleBtn.setStyleSheet(_fromUtf8("QPushButton\n"
"{font: 63 12pt \"KacstArt\";\n"
"border : 2px solid black;\n"
"}\n"
"QPushButton:pressed\n"
"{    \n"
"    background-color : rgb(209,209,224);\n"
"}\n"
"\n"
"        "))
        self.m11AngleBtn.setObjectName(_fromUtf8("m11AngleBtn"))
        self.m11PositionBtn = QtGui.QPushButton(self.m11CFrame)
        self.m11PositionBtn.setGeometry(QtCore.QRect(30, 220, 151, 21))
        self.m11PositionBtn.setStyleSheet(_fromUtf8("QPushButton\n"
"{font: 63 12pt \"KacstArt\";\n"
"border : 2px solid black;\n"
"}\n"
"QPushButton:pressed\n"
"{    \n"
"    background-color : rgb(209,209,224);\n"
"}\n"
"\n"
"        "))
        self.m11PositionBtn.setObjectName(_fromUtf8("m11PositionBtn"))
        self.m11HomeBtn = QtGui.QPushButton(self.m11CFrame)
        self.m11HomeBtn.setGeometry(QtCore.QRect(20, 370, 171, 61))
        self.m11HomeBtn.setStyleSheet(_fromUtf8("QPushButton\n"
"{font: 63 14pt \"KacstArt\";\n"
"border : 2px solid black;\n"
"}\n"
"QPushButton:pressed\n"
"{    \n"
"    background-color : rgb(209,209,224);\n"
"}\n"
"\n"
"        "))
        self.m11HomeBtn.setObjectName(_fromUtf8("m11HomeBtn"))
        self.m11SFrame = QtGui.QFrame(self.m11Page)
        self.m11SFrame.setGeometry(QtCore.QRect(10, 40, 561, 501))
        self.m11SFrame.setStyleSheet(_fromUtf8("border : 1px solid rgb(113, 0, 0);\n"
""))
        self.m11SFrame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.m11SFrame.setFrameShadow(QtGui.QFrame.Raised)
        self.m11SFrame.setObjectName(_fromUtf8("m11SFrame"))
        self.m11AngLabel = QtGui.QLabel(self.m11SFrame)
        self.m11AngLabel.setGeometry(QtCore.QRect(120, 40, 61, 21))
        self.m11AngLabel.setStyleSheet(_fromUtf8("font: 63 16pt \"KacstArt\";\n"
"border : none;"))
        self.m11AngLabel.setObjectName(_fromUtf8("m11AngLabel"))
        self.m11PosLabel = QtGui.QLabel(self.m11SFrame)
        self.m11PosLabel.setGeometry(QtCore.QRect(390, 40, 91, 21))
        self.m11PosLabel.setStyleSheet(_fromUtf8("font: 63 16pt \"KacstArt\";\n"
"border : none;"))
        self.m11PosLabel.setObjectName(_fromUtf8("m11PosLabel"))
        self.m11TorqueLabel = QtGui.QLabel(self.m11SFrame)
        self.m11TorqueLabel.setGeometry(QtCore.QRect(80, 270, 141, 21))
        self.m11TorqueLabel.setStyleSheet(_fromUtf8("font: 63 16pt \"KacstArt\";\n"
"border : none;"))
        self.m11TorqueLabel.setObjectName(_fromUtf8("m11TorqueLabel"))
        self.m11TempLabel = QtGui.QLabel(self.m11SFrame)
        self.m11TempLabel.setGeometry(QtCore.QRect(370, 270, 131, 21))
        self.m11TempLabel.setStyleSheet(_fromUtf8("font: 63 16pt \"KacstArt\";\n"
"border : none;"))
        self.m11TempLabel.setObjectName(_fromUtf8("m11TempLabel"))
        self.m11ErrLabel = QtGui.QLabel(self.m11SFrame)
        self.m11ErrLabel.setGeometry(QtCore.QRect(260, 390, 61, 21))
        self.m11ErrLabel.setStyleSheet(_fromUtf8("font: 63 16pt \"KacstArt\";\n"
"border : none;"))
        self.m11ErrLabel.setObjectName(_fromUtf8("m11ErrLabel"))
        self.m11AngDial = QtGui.QDial(self.m11SFrame)
        self.m11AngDial.setGeometry(QtCore.QRect(100, 80, 91, 81))
        self.m11AngDial.setMinimum(-150)
        self.m11AngDial.setMaximum(150)
        self.m11AngDial.setTracking(True)
        self.m11AngDial.setWrapping(False)
        self.m11AngDial.setNotchTarget(50.0)
        self.m11AngDial.setNotchesVisible(True)
        self.m11AngDial.setObjectName(_fromUtf8("m11AngDial"))
        self.m11PosDial = QtGui.QDial(self.m11SFrame)
        self.m11PosDial.setGeometry(QtCore.QRect(380, 80, 91, 81))
        self.m11PosDial.setMinimum(0)
        self.m11PosDial.setMaximum(1023)
        self.m11PosDial.setTracking(True)
        self.m11PosDial.setWrapping(False)
        self.m11PosDial.setNotchTarget(100.0)
        self.m11PosDial.setNotchesVisible(True)
        self.m11PosDial.setObjectName(_fromUtf8("m11PosDial"))
        self.m11AngNum = QtGui.QLabel(self.m11SFrame)
        self.m11AngNum.setGeometry(QtCore.QRect(120, 200, 61, 21))
        self.m11AngNum.setStyleSheet(_fromUtf8("font: 63 16pt \"KacstArt\";\n"
"border : none;"))
        self.m11AngNum.setObjectName(_fromUtf8("m11AngNum"))
        self.m11PosNum = QtGui.QLabel(self.m11SFrame)
        self.m11PosNum.setGeometry(QtCore.QRect(400, 200, 61, 21))
        self.m11PosNum.setStyleSheet(_fromUtf8("font: 63 16pt \"KacstArt\";\n"
"border : none;"))
        self.m11PosNum.setObjectName(_fromUtf8("m11PosNum"))
        self.m11TorqueNum = QtGui.QLabel(self.m11SFrame)
        self.m11TorqueNum.setGeometry(QtCore.QRect(120, 320, 61, 21))
        self.m11TorqueNum.setStyleSheet(_fromUtf8("font: 63 16pt \"KacstArt\";\n"
"border : none;"))
        self.m11TorqueNum.setObjectName(_fromUtf8("m11TorqueNum"))
        self.m11ErrNum = QtGui.QLabel(self.m11SFrame)
        self.m11ErrNum.setGeometry(QtCore.QRect(260, 440, 61, 21))
        self.m11ErrNum.setStyleSheet(_fromUtf8("font: 63 16pt \"KacstArt\";\n"
"border : none;"))
        self.m11ErrNum.setObjectName(_fromUtf8("m11ErrNum"))
        self.m11TempNum = QtGui.QLabel(self.m11SFrame)
        self.m11TempNum.setGeometry(QtCore.QRect(400, 320, 61, 21))
        self.m11TempNum.setStyleSheet(_fromUtf8("font: 63 16pt \"KacstArt\";\n"
"border : none;"))
        self.m11TempNum.setObjectName(_fromUtf8("m11TempNum"))
        self.stackedWidget.addWidget(self.m11Page)
        self.m12Page = QtGui.QWidget()
        self.m12Page.setObjectName(_fromUtf8("m12Page"))
        self.m12Label = QtGui.QLabel(self.m12Page)
        self.m12Label.setGeometry(QtCore.QRect(340, 10, 91, 21))
        self.m12Label.setStyleSheet(_fromUtf8("font: 63 16pt \"KacstArt\";\n"
"border : none;"))
        self.m12Label.setObjectName(_fromUtf8("m12Label"))
        self.m1CFrame_2 = QtGui.QFrame(self.m12Page)
        self.m1CFrame_2.setGeometry(QtCore.QRect(580, 40, 211, 501))
        self.m1CFrame_2.setStyleSheet(_fromUtf8("border : 1px solid rgb(113, 0, 0);\n"
""))
        self.m1CFrame_2.setObjectName(_fromUtf8("m1CFrame_2"))
        self.m12GoalTSpin = QtGui.QSpinBox(self.m1CFrame_2)
        self.m12GoalTSpin.setGeometry(QtCore.QRect(30, 40, 151, 21))
        self.m12GoalTSpin.setStyleSheet(_fromUtf8("font: 63 13pt \"KacstArt\";"))
        self.m12GoalTSpin.setWrapping(False)
        self.m12GoalTSpin.setAccelerated(False)
        self.m12GoalTSpin.setObjectName(_fromUtf8("m12GoalTSpin"))
        self.m12GoalTLabel = QtGui.QLabel(self.m1CFrame_2)
        self.m12GoalTLabel.setGeometry(QtCore.QRect(60, 10, 111, 21))
        self.m12GoalTLabel.setStyleSheet(_fromUtf8("font: 63 14pt \"KacstArt\";\n"
"border : none;"))
        self.m12GoalTLabel.setObjectName(_fromUtf8("m12GoalTLabel"))
        self.m12UpdateBtn = QtGui.QPushButton(self.m1CFrame_2)
        self.m12UpdateBtn.setGeometry(QtCore.QRect(20, 290, 171, 41))
        self.m12UpdateBtn.setAutoFillBackground(False)
        self.m12UpdateBtn.setStyleSheet(_fromUtf8("QPushButton\n"
"{font: 63 14pt \"KacstArt\";\n"
"border : 2px solid black;\n"
"}\n"
"QPushButton:pressed\n"
"{    \n"
"    background-color : rgb(209,209,224);\n"
"}\n"
"\n"
"        "))
        self.m12UpdateBtn.setAutoDefault(False)
        self.m12UpdateBtn.setDefault(False)
        self.m12UpdateBtn.setFlat(False)
        self.m12UpdateBtn.setObjectName(_fromUtf8("m12UpdateBtn"))
        self.m12AngleLabel = QtGui.QLabel(self.m1CFrame_2)
        self.m12AngleLabel.setGeometry(QtCore.QRect(80, 70, 61, 21))
        self.m12AngleLabel.setStyleSheet(_fromUtf8("font: 63 14pt \"KacstArt\";\n"
"border : none;"))
        self.m12AngleLabel.setObjectName(_fromUtf8("m12AngleLabel"))
        self.m12AngleSpin = QtGui.QSpinBox(self.m1CFrame_2)
        self.m12AngleSpin.setGeometry(QtCore.QRect(30, 100, 151, 21))
        self.m12AngleSpin.setStyleSheet(_fromUtf8("font: 63 13pt \"KacstArt\";"))
        self.m12AngleSpin.setWrapping(False)
        self.m12AngleSpin.setAccelerated(False)
        self.m12AngleSpin.setMinimum(-150)
        self.m12AngleSpin.setMaximum(150)
        self.m12AngleSpin.setObjectName(_fromUtf8("m12AngleSpin"))
        self.m12PositionSpin = QtGui.QSpinBox(self.m1CFrame_2)
        self.m12PositionSpin.setGeometry(QtCore.QRect(30, 190, 151, 21))
        self.m12PositionSpin.setStyleSheet(_fromUtf8("font: 63 13pt \"KacstArt\";"))
        self.m12PositionSpin.setWrapping(False)
        self.m12PositionSpin.setAccelerated(False)
        self.m12PositionSpin.setMaximum(1023)
        self.m12PositionSpin.setObjectName(_fromUtf8("m12PositionSpin"))
        self.m12PositionLabel = QtGui.QLabel(self.m1CFrame_2)
        self.m12PositionLabel.setGeometry(QtCore.QRect(70, 170, 81, 21))
        self.m12PositionLabel.setStyleSheet(_fromUtf8("font: 63 14pt \"KacstArt\";\n"
"border : none;"))
        self.m12PositionLabel.setObjectName(_fromUtf8("m12PositionLabel"))
        self.m12AngleBtn = QtGui.QPushButton(self.m1CFrame_2)
        self.m12AngleBtn.setGeometry(QtCore.QRect(30, 130, 151, 21))
        self.m12AngleBtn.setStyleSheet(_fromUtf8("QPushButton\n"
"{font: 63 12pt \"KacstArt\";\n"
"border : 2px solid black;\n"
"}\n"
"QPushButton:pressed\n"
"{    \n"
"    background-color : rgb(209,209,224);\n"
"}\n"
"\n"
"        "))
        self.m12AngleBtn.setObjectName(_fromUtf8("m12AngleBtn"))
        self.m12PositionBtn = QtGui.QPushButton(self.m1CFrame_2)
        self.m12PositionBtn.setGeometry(QtCore.QRect(30, 220, 151, 21))
        self.m12PositionBtn.setStyleSheet(_fromUtf8("QPushButton\n"
"{font: 63 12pt \"KacstArt\";\n"
"border : 2px solid black;\n"
"}\n"
"QPushButton:pressed\n"
"{    \n"
"    background-color : rgb(209,209,224);\n"
"}\n"
"\n"
"        "))
        self.m12PositionBtn.setObjectName(_fromUtf8("m12PositionBtn"))
        self.m12HomeBtn = QtGui.QPushButton(self.m1CFrame_2)
        self.m12HomeBtn.setGeometry(QtCore.QRect(20, 370, 171, 61))
        self.m12HomeBtn.setStyleSheet(_fromUtf8("QPushButton\n"
"{font: 63 14pt \"KacstArt\";\n"
"border : 2px solid black;\n"
"}\n"
"QPushButton:pressed\n"
"{    \n"
"    background-color : rgb(209,209,224);\n"
"}\n"
"\n"
"        "))
        self.m12HomeBtn.setObjectName(_fromUtf8("m12HomeBtn"))
        self.m12SFrame = QtGui.QFrame(self.m12Page)
        self.m12SFrame.setGeometry(QtCore.QRect(10, 40, 561, 501))
        self.m12SFrame.setStyleSheet(_fromUtf8("border : 1px solid rgb(113, 0, 0);\n"
""))
        self.m12SFrame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.m12SFrame.setFrameShadow(QtGui.QFrame.Raised)
        self.m12SFrame.setObjectName(_fromUtf8("m12SFrame"))
        self.m12AngLabel = QtGui.QLabel(self.m12SFrame)
        self.m12AngLabel.setGeometry(QtCore.QRect(120, 40, 61, 21))
        self.m12AngLabel.setStyleSheet(_fromUtf8("font: 63 16pt \"KacstArt\";\n"
"border : none;"))
        self.m12AngLabel.setObjectName(_fromUtf8("m12AngLabel"))
        self.m12PosLabel = QtGui.QLabel(self.m12SFrame)
        self.m12PosLabel.setGeometry(QtCore.QRect(390, 40, 91, 21))
        self.m12PosLabel.setStyleSheet(_fromUtf8("font: 63 16pt \"KacstArt\";\n"
"border : none;"))
        self.m12PosLabel.setObjectName(_fromUtf8("m12PosLabel"))
        self.m12TorqueLabel = QtGui.QLabel(self.m12SFrame)
        self.m12TorqueLabel.setGeometry(QtCore.QRect(80, 270, 141, 21))
        self.m12TorqueLabel.setStyleSheet(_fromUtf8("font: 63 16pt \"KacstArt\";\n"
"border : none;"))
        self.m12TorqueLabel.setObjectName(_fromUtf8("m12TorqueLabel"))
        self.m12TempLabel = QtGui.QLabel(self.m12SFrame)
        self.m12TempLabel.setGeometry(QtCore.QRect(370, 270, 131, 21))
        self.m12TempLabel.setStyleSheet(_fromUtf8("font: 63 16pt \"KacstArt\";\n"
"border : none;"))
        self.m12TempLabel.setObjectName(_fromUtf8("m12TempLabel"))
        self.m12ErrLabel = QtGui.QLabel(self.m12SFrame)
        self.m12ErrLabel.setGeometry(QtCore.QRect(260, 390, 61, 21))
        self.m12ErrLabel.setStyleSheet(_fromUtf8("font: 63 16pt \"KacstArt\";\n"
"border : none;"))
        self.m12ErrLabel.setObjectName(_fromUtf8("m12ErrLabel"))
        self.m12AngDial = QtGui.QDial(self.m12SFrame)
        self.m12AngDial.setGeometry(QtCore.QRect(100, 80, 91, 81))
        self.m12AngDial.setMinimum(-150)
        self.m12AngDial.setMaximum(150)
        self.m12AngDial.setTracking(True)
        self.m12AngDial.setWrapping(False)
        self.m12AngDial.setNotchTarget(50.0)
        self.m12AngDial.setNotchesVisible(True)
        self.m12AngDial.setObjectName(_fromUtf8("m12AngDial"))
        self.m12PosDial = QtGui.QDial(self.m12SFrame)
        self.m12PosDial.setGeometry(QtCore.QRect(380, 80, 91, 81))
        self.m12PosDial.setMinimum(0)
        self.m12PosDial.setMaximum(1023)
        self.m12PosDial.setTracking(True)
        self.m12PosDial.setWrapping(False)
        self.m12PosDial.setNotchTarget(100.0)
        self.m12PosDial.setNotchesVisible(True)
        self.m12PosDial.setObjectName(_fromUtf8("m12PosDial"))
        self.m12AngNum = QtGui.QLabel(self.m12SFrame)
        self.m12AngNum.setGeometry(QtCore.QRect(120, 200, 61, 21))
        self.m12AngNum.setStyleSheet(_fromUtf8("font: 63 16pt \"KacstArt\";\n"
"border : none;"))
        self.m12AngNum.setObjectName(_fromUtf8("m12AngNum"))
        self.m12PosNum = QtGui.QLabel(self.m12SFrame)
        self.m12PosNum.setGeometry(QtCore.QRect(400, 200, 61, 21))
        self.m12PosNum.setStyleSheet(_fromUtf8("font: 63 16pt \"KacstArt\";\n"
"border : none;"))
        self.m12PosNum.setObjectName(_fromUtf8("m12PosNum"))
        self.m12TorqueNum = QtGui.QLabel(self.m12SFrame)
        self.m12TorqueNum.setGeometry(QtCore.QRect(120, 320, 61, 21))
        self.m12TorqueNum.setStyleSheet(_fromUtf8("font: 63 16pt \"KacstArt\";\n"
"border : none;"))
        self.m12TorqueNum.setObjectName(_fromUtf8("m12TorqueNum"))
        self.m12ErrNum = QtGui.QLabel(self.m12SFrame)
        self.m12ErrNum.setGeometry(QtCore.QRect(260, 440, 61, 21))
        self.m12ErrNum.setStyleSheet(_fromUtf8("font: 63 16pt \"KacstArt\";\n"
"border : none;"))
        self.m12ErrNum.setObjectName(_fromUtf8("m12ErrNum"))
        self.m12TempNum = QtGui.QLabel(self.m12SFrame)
        self.m12TempNum.setGeometry(QtCore.QRect(400, 320, 61, 21))
        self.m12TempNum.setStyleSheet(_fromUtf8("font: 63 16pt \"KacstArt\";\n"
"border : none;"))
        self.m12TempNum.setObjectName(_fromUtf8("m12TempNum"))
        self.stackedWidget.addWidget(self.m12Page)
        self.m13Page = QtGui.QWidget()
        self.m13Page.setObjectName(_fromUtf8("m13Page"))
        self.m13Label = QtGui.QLabel(self.m13Page)
        self.m13Label.setGeometry(QtCore.QRect(340, 10, 91, 21))
        self.m13Label.setStyleSheet(_fromUtf8("font: 63 16pt \"KacstArt\";\n"
"border : none;"))
        self.m13Label.setObjectName(_fromUtf8("m13Label"))
        self.m13CFrame = QtGui.QFrame(self.m13Page)
        self.m13CFrame.setGeometry(QtCore.QRect(580, 40, 211, 501))
        self.m13CFrame.setStyleSheet(_fromUtf8("border : 1px solid rgb(113, 0, 0);\n"
""))
        self.m13CFrame.setObjectName(_fromUtf8("m13CFrame"))
        self.m13GoalTSpin = QtGui.QSpinBox(self.m13CFrame)
        self.m13GoalTSpin.setGeometry(QtCore.QRect(30, 40, 151, 21))
        self.m13GoalTSpin.setStyleSheet(_fromUtf8("font: 63 13pt \"KacstArt\";"))
        self.m13GoalTSpin.setWrapping(False)
        self.m13GoalTSpin.setAccelerated(False)
        self.m13GoalTSpin.setObjectName(_fromUtf8("m13GoalTSpin"))
        self.m13GoalTLabel = QtGui.QLabel(self.m13CFrame)
        self.m13GoalTLabel.setGeometry(QtCore.QRect(60, 10, 111, 21))
        self.m13GoalTLabel.setStyleSheet(_fromUtf8("font: 63 14pt \"KacstArt\";\n"
"border : none;"))
        self.m13GoalTLabel.setObjectName(_fromUtf8("m13GoalTLabel"))
        self.m13UpdateBtn = QtGui.QPushButton(self.m13CFrame)
        self.m13UpdateBtn.setGeometry(QtCore.QRect(20, 290, 171, 41))
        self.m13UpdateBtn.setAutoFillBackground(False)
        self.m13UpdateBtn.setStyleSheet(_fromUtf8("QPushButton\n"
"{font: 63 14pt \"KacstArt\";\n"
"border : 2px solid black;\n"
"}\n"
"QPushButton:pressed\n"
"{    \n"
"    background-color : rgb(209,209,224);\n"
"}\n"
"\n"
"        "))
        self.m13UpdateBtn.setAutoDefault(False)
        self.m13UpdateBtn.setDefault(False)
        self.m13UpdateBtn.setFlat(False)
        self.m13UpdateBtn.setObjectName(_fromUtf8("m13UpdateBtn"))
        self.m13AngleLabel = QtGui.QLabel(self.m13CFrame)
        self.m13AngleLabel.setGeometry(QtCore.QRect(80, 70, 61, 21))
        self.m13AngleLabel.setStyleSheet(_fromUtf8("font: 63 14pt \"KacstArt\";\n"
"border : none;"))
        self.m13AngleLabel.setObjectName(_fromUtf8("m13AngleLabel"))
        self.m13AngleSpin = QtGui.QSpinBox(self.m13CFrame)
        self.m13AngleSpin.setGeometry(QtCore.QRect(30, 100, 151, 21))
        self.m13AngleSpin.setStyleSheet(_fromUtf8("font: 63 13pt \"KacstArt\";"))
        self.m13AngleSpin.setWrapping(False)
        self.m13AngleSpin.setAccelerated(False)
        self.m13AngleSpin.setMinimum(-150)
        self.m13AngleSpin.setMaximum(150)
        self.m13AngleSpin.setObjectName(_fromUtf8("m13AngleSpin"))
        self.m13PositionSpin = QtGui.QSpinBox(self.m13CFrame)
        self.m13PositionSpin.setGeometry(QtCore.QRect(30, 190, 151, 21))
        self.m13PositionSpin.setStyleSheet(_fromUtf8("font: 63 13pt \"KacstArt\";"))
        self.m13PositionSpin.setWrapping(False)
        self.m13PositionSpin.setAccelerated(False)
        self.m13PositionSpin.setMaximum(1023)
        self.m13PositionSpin.setObjectName(_fromUtf8("m13PositionSpin"))
        self.m13PositionLabel = QtGui.QLabel(self.m13CFrame)
        self.m13PositionLabel.setGeometry(QtCore.QRect(70, 170, 81, 21))
        self.m13PositionLabel.setStyleSheet(_fromUtf8("font: 63 14pt \"KacstArt\";\n"
"border : none;"))
        self.m13PositionLabel.setObjectName(_fromUtf8("m13PositionLabel"))
        self.m13AngleBtn = QtGui.QPushButton(self.m13CFrame)
        self.m13AngleBtn.setGeometry(QtCore.QRect(30, 130, 151, 21))
        self.m13AngleBtn.setStyleSheet(_fromUtf8("QPushButton\n"
"{font: 63 12pt \"KacstArt\";\n"
"border : 2px solid black;\n"
"}\n"
"QPushButton:pressed\n"
"{    \n"
"    background-color : rgb(209,209,224);\n"
"}\n"
"\n"
"        "))
        self.m13AngleBtn.setObjectName(_fromUtf8("m13AngleBtn"))
        self.m13PositionBtn = QtGui.QPushButton(self.m13CFrame)
        self.m13PositionBtn.setGeometry(QtCore.QRect(30, 220, 151, 21))
        self.m13PositionBtn.setStyleSheet(_fromUtf8("QPushButton\n"
"{font: 63 12pt \"KacstArt\";\n"
"border : 2px solid black;\n"
"}\n"
"QPushButton:pressed\n"
"{    \n"
"    background-color : rgb(209,209,224);\n"
"}\n"
"\n"
"        "))
        self.m13PositionBtn.setObjectName(_fromUtf8("m13PositionBtn"))
        self.m13HomeBtn = QtGui.QPushButton(self.m13CFrame)
        self.m13HomeBtn.setGeometry(QtCore.QRect(20, 370, 171, 61))
        self.m13HomeBtn.setStyleSheet(_fromUtf8("QPushButton\n"
"{font: 63 14pt \"KacstArt\";\n"
"border : 2px solid black;\n"
"}\n"
"QPushButton:pressed\n"
"{    \n"
"    background-color : rgb(209,209,224);\n"
"}\n"
"\n"
"        "))
        self.m13HomeBtn.setObjectName(_fromUtf8("m13HomeBtn"))
        self.m13SFrame = QtGui.QFrame(self.m13Page)
        self.m13SFrame.setGeometry(QtCore.QRect(10, 40, 561, 501))
        self.m13SFrame.setStyleSheet(_fromUtf8("border : 1px solid rgb(113, 0, 0);\n"
""))
        self.m13SFrame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.m13SFrame.setFrameShadow(QtGui.QFrame.Raised)
        self.m13SFrame.setObjectName(_fromUtf8("m13SFrame"))
        self.m13AngLabel = QtGui.QLabel(self.m13SFrame)
        self.m13AngLabel.setGeometry(QtCore.QRect(120, 40, 61, 21))
        self.m13AngLabel.setStyleSheet(_fromUtf8("font: 63 16pt \"KacstArt\";\n"
"border : none;"))
        self.m13AngLabel.setObjectName(_fromUtf8("m13AngLabel"))
        self.m13PosLabel = QtGui.QLabel(self.m13SFrame)
        self.m13PosLabel.setGeometry(QtCore.QRect(390, 40, 91, 21))
        self.m13PosLabel.setStyleSheet(_fromUtf8("font: 63 16pt \"KacstArt\";\n"
"border : none;"))
        self.m13PosLabel.setObjectName(_fromUtf8("m13PosLabel"))
        self.m13TorqueLabel = QtGui.QLabel(self.m13SFrame)
        self.m13TorqueLabel.setGeometry(QtCore.QRect(80, 270, 141, 21))
        self.m13TorqueLabel.setStyleSheet(_fromUtf8("font: 63 16pt \"KacstArt\";\n"
"border : none;"))
        self.m13TorqueLabel.setObjectName(_fromUtf8("m13TorqueLabel"))
        self.m13TempLabel = QtGui.QLabel(self.m13SFrame)
        self.m13TempLabel.setGeometry(QtCore.QRect(370, 270, 131, 21))
        self.m13TempLabel.setStyleSheet(_fromUtf8("font: 63 16pt \"KacstArt\";\n"
"border : none;"))
        self.m13TempLabel.setObjectName(_fromUtf8("m13TempLabel"))
        self.m13ErrLabel = QtGui.QLabel(self.m13SFrame)
        self.m13ErrLabel.setGeometry(QtCore.QRect(260, 390, 61, 21))
        self.m13ErrLabel.setStyleSheet(_fromUtf8("font: 63 16pt \"KacstArt\";\n"
"border : none;"))
        self.m13ErrLabel.setObjectName(_fromUtf8("m13ErrLabel"))
        self.m13AngDial = QtGui.QDial(self.m13SFrame)
        self.m13AngDial.setGeometry(QtCore.QRect(100, 80, 91, 81))
        self.m13AngDial.setMinimum(-150)
        self.m13AngDial.setMaximum(150)
        self.m13AngDial.setTracking(True)
        self.m13AngDial.setWrapping(False)
        self.m13AngDial.setNotchTarget(50.0)
        self.m13AngDial.setNotchesVisible(True)
        self.m13AngDial.setObjectName(_fromUtf8("m13AngDial"))
        self.m13PosDial = QtGui.QDial(self.m13SFrame)
        self.m13PosDial.setGeometry(QtCore.QRect(380, 80, 91, 81))
        self.m13PosDial.setMinimum(0)
        self.m13PosDial.setMaximum(1023)
        self.m13PosDial.setTracking(True)
        self.m13PosDial.setWrapping(False)
        self.m13PosDial.setNotchTarget(100.0)
        self.m13PosDial.setNotchesVisible(True)
        self.m13PosDial.setObjectName(_fromUtf8("m13PosDial"))
        self.m13AngNum = QtGui.QLabel(self.m13SFrame)
        self.m13AngNum.setGeometry(QtCore.QRect(120, 200, 61, 21))
        self.m13AngNum.setStyleSheet(_fromUtf8("font: 63 16pt \"KacstArt\";\n"
"border : none;"))
        self.m13AngNum.setObjectName(_fromUtf8("m13AngNum"))
        self.m13PosNum = QtGui.QLabel(self.m13SFrame)
        self.m13PosNum.setGeometry(QtCore.QRect(400, 200, 61, 21))
        self.m13PosNum.setStyleSheet(_fromUtf8("font: 63 16pt \"KacstArt\";\n"
"border : none;"))
        self.m13PosNum.setObjectName(_fromUtf8("m13PosNum"))
        self.m13TorqueNum = QtGui.QLabel(self.m13SFrame)
        self.m13TorqueNum.setGeometry(QtCore.QRect(120, 320, 61, 21))
        self.m13TorqueNum.setStyleSheet(_fromUtf8("font: 63 16pt \"KacstArt\";\n"
"border : none;"))
        self.m13TorqueNum.setObjectName(_fromUtf8("m13TorqueNum"))
        self.m13ErrNum = QtGui.QLabel(self.m13SFrame)
        self.m13ErrNum.setGeometry(QtCore.QRect(260, 440, 61, 21))
        self.m13ErrNum.setStyleSheet(_fromUtf8("font: 63 16pt \"KacstArt\";\n"
"border : none;"))
        self.m13ErrNum.setObjectName(_fromUtf8("m13ErrNum"))
        self.m13TempNum = QtGui.QLabel(self.m13SFrame)
        self.m13TempNum.setGeometry(QtCore.QRect(400, 320, 61, 21))
        self.m13TempNum.setStyleSheet(_fromUtf8("font: 63 16pt \"KacstArt\";\n"
"border : none;"))
        self.m13TempNum.setObjectName(_fromUtf8("m13TempNum"))
        self.stackedWidget.addWidget(self.m13Page)
        self.m14Page = QtGui.QWidget()
        self.m14Page.setObjectName(_fromUtf8("m14Page"))
        self.m14Label = QtGui.QLabel(self.m14Page)
        self.m14Label.setGeometry(QtCore.QRect(340, 10, 91, 21))
        self.m14Label.setStyleSheet(_fromUtf8("font: 63 16pt \"KacstArt\";\n"
"border : none;"))
        self.m14Label.setObjectName(_fromUtf8("m14Label"))
        self.m14CFrame = QtGui.QFrame(self.m14Page)
        self.m14CFrame.setGeometry(QtCore.QRect(580, 40, 211, 501))
        self.m14CFrame.setStyleSheet(_fromUtf8("border : 1px solid rgb(113, 0, 0);\n"
""))
        self.m14CFrame.setObjectName(_fromUtf8("m14CFrame"))
        self.m14GoalTSpin = QtGui.QSpinBox(self.m14CFrame)
        self.m14GoalTSpin.setGeometry(QtCore.QRect(30, 40, 151, 21))
        self.m14GoalTSpin.setStyleSheet(_fromUtf8("font: 63 13pt \"KacstArt\";"))
        self.m14GoalTSpin.setWrapping(False)
        self.m14GoalTSpin.setAccelerated(False)
        self.m14GoalTSpin.setObjectName(_fromUtf8("m14GoalTSpin"))
        self.m14GoalTLabel = QtGui.QLabel(self.m14CFrame)
        self.m14GoalTLabel.setGeometry(QtCore.QRect(60, 10, 111, 21))
        self.m14GoalTLabel.setStyleSheet(_fromUtf8("font: 63 14pt \"KacstArt\";\n"
"border : none;"))
        self.m14GoalTLabel.setObjectName(_fromUtf8("m14GoalTLabel"))
        self.m14UpdateBtn = QtGui.QPushButton(self.m14CFrame)
        self.m14UpdateBtn.setGeometry(QtCore.QRect(20, 290, 171, 41))
        self.m14UpdateBtn.setAutoFillBackground(False)
        self.m14UpdateBtn.setStyleSheet(_fromUtf8("QPushButton\n"
"{font: 63 14pt \"KacstArt\";\n"
"border : 2px solid black;\n"
"}\n"
"QPushButton:pressed\n"
"{    \n"
"    background-color : rgb(209,209,224);\n"
"}\n"
"\n"
"        "))
        self.m14UpdateBtn.setAutoDefault(False)
        self.m14UpdateBtn.setDefault(False)
        self.m14UpdateBtn.setFlat(False)
        self.m14UpdateBtn.setObjectName(_fromUtf8("m14UpdateBtn"))
        self.m14AngleLabel = QtGui.QLabel(self.m14CFrame)
        self.m14AngleLabel.setGeometry(QtCore.QRect(80, 70, 61, 21))
        self.m14AngleLabel.setStyleSheet(_fromUtf8("font: 63 14pt \"KacstArt\";\n"
"border : none;"))
        self.m14AngleLabel.setObjectName(_fromUtf8("m14AngleLabel"))
        self.m14AngleSpin = QtGui.QSpinBox(self.m14CFrame)
        self.m14AngleSpin.setGeometry(QtCore.QRect(30, 100, 151, 21))
        self.m14AngleSpin.setStyleSheet(_fromUtf8("font: 63 13pt \"KacstArt\";"))
        self.m14AngleSpin.setWrapping(False)
        self.m14AngleSpin.setAccelerated(False)
        self.m14AngleSpin.setMinimum(-150)
        self.m14AngleSpin.setMaximum(150)
        self.m14AngleSpin.setObjectName(_fromUtf8("m14AngleSpin"))
        self.m14PositionSpin = QtGui.QSpinBox(self.m14CFrame)
        self.m14PositionSpin.setGeometry(QtCore.QRect(30, 190, 151, 21))
        self.m14PositionSpin.setStyleSheet(_fromUtf8("font: 63 13pt \"KacstArt\";"))
        self.m14PositionSpin.setWrapping(False)
        self.m14PositionSpin.setAccelerated(False)
        self.m14PositionSpin.setMaximum(1023)
        self.m14PositionSpin.setObjectName(_fromUtf8("m14PositionSpin"))
        self.m14PositionLabel = QtGui.QLabel(self.m14CFrame)
        self.m14PositionLabel.setGeometry(QtCore.QRect(70, 170, 81, 21))
        self.m14PositionLabel.setStyleSheet(_fromUtf8("font: 63 14pt \"KacstArt\";\n"
"border : none;"))
        self.m14PositionLabel.setObjectName(_fromUtf8("m14PositionLabel"))
        self.m14AngleBtn = QtGui.QPushButton(self.m14CFrame)
        self.m14AngleBtn.setGeometry(QtCore.QRect(30, 130, 151, 21))
        self.m14AngleBtn.setStyleSheet(_fromUtf8("QPushButton\n"
"{font: 63 12pt \"KacstArt\";\n"
"border : 2px solid black;\n"
"}\n"
"QPushButton:pressed\n"
"{    \n"
"    background-color : rgb(209,209,224);\n"
"}\n"
"\n"
"        "))
        self.m14AngleBtn.setObjectName(_fromUtf8("m14AngleBtn"))
        self.m14PositionBtn = QtGui.QPushButton(self.m14CFrame)
        self.m14PositionBtn.setGeometry(QtCore.QRect(30, 220, 151, 21))
        self.m14PositionBtn.setStyleSheet(_fromUtf8("QPushButton\n"
"{font: 63 12pt \"KacstArt\";\n"
"border : 2px solid black;\n"
"}\n"
"QPushButton:pressed\n"
"{    \n"
"    background-color : rgb(209,209,224);\n"
"}\n"
"\n"
"        "))
        self.m14PositionBtn.setObjectName(_fromUtf8("m14PositionBtn"))
        self.m14HomeBtn = QtGui.QPushButton(self.m14CFrame)
        self.m14HomeBtn.setGeometry(QtCore.QRect(20, 370, 171, 61))
        self.m14HomeBtn.setStyleSheet(_fromUtf8("QPushButton\n"
"{font: 63 14pt \"KacstArt\";\n"
"border : 2px solid black;\n"
"}\n"
"QPushButton:pressed\n"
"{    \n"
"    background-color : rgb(209,209,224);\n"
"}\n"
"\n"
"        "))
        self.m14HomeBtn.setObjectName(_fromUtf8("m14HomeBtn"))
        self.m14SFrame = QtGui.QFrame(self.m14Page)
        self.m14SFrame.setGeometry(QtCore.QRect(10, 40, 561, 501))
        self.m14SFrame.setStyleSheet(_fromUtf8("border : 1px solid rgb(113, 0, 0);\n"
""))
        self.m14SFrame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.m14SFrame.setFrameShadow(QtGui.QFrame.Raised)
        self.m14SFrame.setObjectName(_fromUtf8("m14SFrame"))
        self.m14AngLabel = QtGui.QLabel(self.m14SFrame)
        self.m14AngLabel.setGeometry(QtCore.QRect(120, 40, 61, 21))
        self.m14AngLabel.setStyleSheet(_fromUtf8("font: 63 16pt \"KacstArt\";\n"
"border : none;"))
        self.m14AngLabel.setObjectName(_fromUtf8("m14AngLabel"))
        self.m14PosLabel = QtGui.QLabel(self.m14SFrame)
        self.m14PosLabel.setGeometry(QtCore.QRect(390, 40, 91, 21))
        self.m14PosLabel.setStyleSheet(_fromUtf8("font: 63 16pt \"KacstArt\";\n"
"border : none;"))
        self.m14PosLabel.setObjectName(_fromUtf8("m14PosLabel"))
        self.m14TorqueLabel = QtGui.QLabel(self.m14SFrame)
        self.m14TorqueLabel.setGeometry(QtCore.QRect(80, 270, 141, 21))
        self.m14TorqueLabel.setStyleSheet(_fromUtf8("font: 63 16pt \"KacstArt\";\n"
"border : none;"))
        self.m14TorqueLabel.setObjectName(_fromUtf8("m14TorqueLabel"))
        self.m14TempLabel = QtGui.QLabel(self.m14SFrame)
        self.m14TempLabel.setGeometry(QtCore.QRect(370, 270, 131, 21))
        self.m14TempLabel.setStyleSheet(_fromUtf8("font: 63 16pt \"KacstArt\";\n"
"border : none;"))
        self.m14TempLabel.setObjectName(_fromUtf8("m14TempLabel"))
        self.m14ErrLabel = QtGui.QLabel(self.m14SFrame)
        self.m14ErrLabel.setGeometry(QtCore.QRect(260, 390, 61, 21))
        self.m14ErrLabel.setStyleSheet(_fromUtf8("font: 63 16pt \"KacstArt\";\n"
"border : none;"))
        self.m14ErrLabel.setObjectName(_fromUtf8("m14ErrLabel"))
        self.m14AngDial = QtGui.QDial(self.m14SFrame)
        self.m14AngDial.setGeometry(QtCore.QRect(100, 80, 91, 81))
        self.m14AngDial.setMinimum(-150)
        self.m14AngDial.setMaximum(150)
        self.m14AngDial.setTracking(True)
        self.m14AngDial.setWrapping(False)
        self.m14AngDial.setNotchTarget(50.0)
        self.m14AngDial.setNotchesVisible(True)
        self.m14AngDial.setObjectName(_fromUtf8("m14AngDial"))
        self.m14PosDial = QtGui.QDial(self.m14SFrame)
        self.m14PosDial.setGeometry(QtCore.QRect(380, 80, 91, 81))
        self.m14PosDial.setMinimum(0)
        self.m14PosDial.setMaximum(1023)
        self.m14PosDial.setTracking(True)
        self.m14PosDial.setWrapping(False)
        self.m14PosDial.setNotchTarget(100.0)
        self.m14PosDial.setNotchesVisible(True)
        self.m14PosDial.setObjectName(_fromUtf8("m14PosDial"))
        self.m14AngNum = QtGui.QLabel(self.m14SFrame)
        self.m14AngNum.setGeometry(QtCore.QRect(120, 200, 61, 21))
        self.m14AngNum.setStyleSheet(_fromUtf8("font: 63 16pt \"KacstArt\";\n"
"border : none;"))
        self.m14AngNum.setObjectName(_fromUtf8("m14AngNum"))
        self.m14PosNum = QtGui.QLabel(self.m14SFrame)
        self.m14PosNum.setGeometry(QtCore.QRect(400, 200, 61, 21))
        self.m14PosNum.setStyleSheet(_fromUtf8("font: 63 16pt \"KacstArt\";\n"
"border : none;"))
        self.m14PosNum.setObjectName(_fromUtf8("m14PosNum"))
        self.m14TorqueNum = QtGui.QLabel(self.m14SFrame)
        self.m14TorqueNum.setGeometry(QtCore.QRect(120, 320, 61, 21))
        self.m14TorqueNum.setStyleSheet(_fromUtf8("font: 63 16pt \"KacstArt\";\n"
"border : none;"))
        self.m14TorqueNum.setObjectName(_fromUtf8("m14TorqueNum"))
        self.m14ErrNum = QtGui.QLabel(self.m14SFrame)
        self.m14ErrNum.setGeometry(QtCore.QRect(260, 440, 61, 21))
        self.m14ErrNum.setStyleSheet(_fromUtf8("font: 63 16pt \"KacstArt\";\n"
"border : none;"))
        self.m14ErrNum.setObjectName(_fromUtf8("m14ErrNum"))
        self.m14TempNum = QtGui.QLabel(self.m14SFrame)
        self.m14TempNum.setGeometry(QtCore.QRect(400, 320, 61, 21))
        self.m14TempNum.setStyleSheet(_fromUtf8("font: 63 16pt \"KacstArt\";\n"
"border : none;"))
        self.m14TempNum.setObjectName(_fromUtf8("m14TempNum"))
        self.stackedWidget.addWidget(self.m14Page)
        self.m15Page = QtGui.QWidget()
        self.m15Page.setObjectName(_fromUtf8("m15Page"))
        self.m15Label = QtGui.QLabel(self.m15Page)
        self.m15Label.setGeometry(QtCore.QRect(340, 10, 91, 21))
        self.m15Label.setStyleSheet(_fromUtf8("font: 63 16pt \"KacstArt\";\n"
"border : none;"))
        self.m15Label.setObjectName(_fromUtf8("m15Label"))
        self.m15CFrame = QtGui.QFrame(self.m15Page)
        self.m15CFrame.setGeometry(QtCore.QRect(580, 40, 211, 501))
        self.m15CFrame.setStyleSheet(_fromUtf8("border : 1px solid rgb(113, 0, 0);\n"
""))
        self.m15CFrame.setObjectName(_fromUtf8("m15CFrame"))
        self.m15GoalTSpin = QtGui.QSpinBox(self.m15CFrame)
        self.m15GoalTSpin.setGeometry(QtCore.QRect(30, 40, 151, 21))
        self.m15GoalTSpin.setStyleSheet(_fromUtf8("font: 63 13pt \"KacstArt\";"))
        self.m15GoalTSpin.setWrapping(False)
        self.m15GoalTSpin.setAccelerated(False)
        self.m15GoalTSpin.setObjectName(_fromUtf8("m15GoalTSpin"))
        self.m15GoalTLabel = QtGui.QLabel(self.m15CFrame)
        self.m15GoalTLabel.setGeometry(QtCore.QRect(60, 10, 111, 21))
        self.m15GoalTLabel.setStyleSheet(_fromUtf8("font: 63 14pt \"KacstArt\";\n"
"border : none;"))
        self.m15GoalTLabel.setObjectName(_fromUtf8("m15GoalTLabel"))
        self.m15UpdateBtn = QtGui.QPushButton(self.m15CFrame)
        self.m15UpdateBtn.setGeometry(QtCore.QRect(20, 290, 171, 41))
        self.m15UpdateBtn.setAutoFillBackground(False)
        self.m15UpdateBtn.setStyleSheet(_fromUtf8("QPushButton\n"
"{font: 63 14pt \"KacstArt\";\n"
"border : 2px solid black;\n"
"}\n"
"QPushButton:pressed\n"
"{    \n"
"    background-color : rgb(209,209,224);\n"
"}\n"
"\n"
"        "))
        self.m15UpdateBtn.setAutoDefault(False)
        self.m15UpdateBtn.setDefault(False)
        self.m15UpdateBtn.setFlat(False)
        self.m15UpdateBtn.setObjectName(_fromUtf8("m15UpdateBtn"))
        self.m15AngleLabel = QtGui.QLabel(self.m15CFrame)
        self.m15AngleLabel.setGeometry(QtCore.QRect(80, 70, 61, 21))
        self.m15AngleLabel.setStyleSheet(_fromUtf8("font: 63 14pt \"KacstArt\";\n"
"border : none;"))
        self.m15AngleLabel.setObjectName(_fromUtf8("m15AngleLabel"))
        self.m15AngleSpin = QtGui.QSpinBox(self.m15CFrame)
        self.m15AngleSpin.setGeometry(QtCore.QRect(30, 100, 151, 21))
        self.m15AngleSpin.setStyleSheet(_fromUtf8("font: 63 13pt \"KacstArt\";"))
        self.m15AngleSpin.setWrapping(False)
        self.m15AngleSpin.setAccelerated(False)
        self.m15AngleSpin.setMinimum(-150)
        self.m15AngleSpin.setMaximum(150)
        self.m15AngleSpin.setObjectName(_fromUtf8("m15AngleSpin"))
        self.m15PositionSpin = QtGui.QSpinBox(self.m15CFrame)
        self.m15PositionSpin.setGeometry(QtCore.QRect(30, 190, 151, 21))
        self.m15PositionSpin.setStyleSheet(_fromUtf8("font: 63 13pt \"KacstArt\";"))
        self.m15PositionSpin.setWrapping(False)
        self.m15PositionSpin.setAccelerated(False)
        self.m15PositionSpin.setMaximum(1023)
        self.m15PositionSpin.setObjectName(_fromUtf8("m15PositionSpin"))
        self.m15PositionLabel = QtGui.QLabel(self.m15CFrame)
        self.m15PositionLabel.setGeometry(QtCore.QRect(70, 170, 81, 21))
        self.m15PositionLabel.setStyleSheet(_fromUtf8("font: 63 14pt \"KacstArt\";\n"
"border : none;"))
        self.m15PositionLabel.setObjectName(_fromUtf8("m15PositionLabel"))
        self.m15AngleBtn = QtGui.QPushButton(self.m15CFrame)
        self.m15AngleBtn.setGeometry(QtCore.QRect(30, 130, 151, 21))
        self.m15AngleBtn.setStyleSheet(_fromUtf8("QPushButton\n"
"{font: 63 12pt \"KacstArt\";\n"
"border : 2px solid black;\n"
"}\n"
"QPushButton:pressed\n"
"{    \n"
"    background-color : rgb(209,209,224);\n"
"}\n"
"\n"
"        "))
        self.m15AngleBtn.setObjectName(_fromUtf8("m15AngleBtn"))
        self.m15PositionBtn = QtGui.QPushButton(self.m15CFrame)
        self.m15PositionBtn.setGeometry(QtCore.QRect(30, 220, 151, 21))
        self.m15PositionBtn.setStyleSheet(_fromUtf8("QPushButton\n"
"{font: 63 12pt \"KacstArt\";\n"
"border : 2px solid black;\n"
"}\n"
"QPushButton:pressed\n"
"{    \n"
"    background-color : rgb(209,209,224);\n"
"}\n"
"\n"
"        "))
        self.m15PositionBtn.setObjectName(_fromUtf8("m15PositionBtn"))
        self.m15HomeBtn = QtGui.QPushButton(self.m15CFrame)
        self.m15HomeBtn.setGeometry(QtCore.QRect(20, 370, 171, 61))
        self.m15HomeBtn.setStyleSheet(_fromUtf8("QPushButton\n"
"{font: 63 14pt \"KacstArt\";\n"
"border : 2px solid black;\n"
"}\n"
"QPushButton:pressed\n"
"{    \n"
"    background-color : rgb(209,209,224);\n"
"}\n"
"\n"
"        "))
        self.m15HomeBtn.setObjectName(_fromUtf8("m15HomeBtn"))
        self.m15SFrame = QtGui.QFrame(self.m15Page)
        self.m15SFrame.setGeometry(QtCore.QRect(10, 40, 561, 501))
        self.m15SFrame.setStyleSheet(_fromUtf8("border : 1px solid rgb(113, 0, 0);\n"
""))
        self.m15SFrame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.m15SFrame.setFrameShadow(QtGui.QFrame.Raised)
        self.m15SFrame.setObjectName(_fromUtf8("m15SFrame"))
        self.m15AngLabel = QtGui.QLabel(self.m15SFrame)
        self.m15AngLabel.setGeometry(QtCore.QRect(120, 40, 61, 21))
        self.m15AngLabel.setStyleSheet(_fromUtf8("font: 63 16pt \"KacstArt\";\n"
"border : none;"))
        self.m15AngLabel.setObjectName(_fromUtf8("m15AngLabel"))
        self.m15PosLabel = QtGui.QLabel(self.m15SFrame)
        self.m15PosLabel.setGeometry(QtCore.QRect(390, 40, 91, 21))
        self.m15PosLabel.setStyleSheet(_fromUtf8("font: 63 16pt \"KacstArt\";\n"
"border : none;"))
        self.m15PosLabel.setObjectName(_fromUtf8("m15PosLabel"))
        self.m15TorqueLabel = QtGui.QLabel(self.m15SFrame)
        self.m15TorqueLabel.setGeometry(QtCore.QRect(80, 270, 141, 21))
        self.m15TorqueLabel.setStyleSheet(_fromUtf8("font: 63 16pt \"KacstArt\";\n"
"border : none;"))
        self.m15TorqueLabel.setObjectName(_fromUtf8("m15TorqueLabel"))
        self.m15TempLabel = QtGui.QLabel(self.m15SFrame)
        self.m15TempLabel.setGeometry(QtCore.QRect(370, 270, 131, 21))
        self.m15TempLabel.setStyleSheet(_fromUtf8("font: 63 16pt \"KacstArt\";\n"
"border : none;"))
        self.m15TempLabel.setObjectName(_fromUtf8("m15TempLabel"))
        self.m15ErrLabel = QtGui.QLabel(self.m15SFrame)
        self.m15ErrLabel.setGeometry(QtCore.QRect(260, 390, 61, 21))
        self.m15ErrLabel.setStyleSheet(_fromUtf8("font: 63 16pt \"KacstArt\";\n"
"border : none;"))
        self.m15ErrLabel.setObjectName(_fromUtf8("m15ErrLabel"))
        self.m15AngDial = QtGui.QDial(self.m15SFrame)
        self.m15AngDial.setGeometry(QtCore.QRect(100, 80, 91, 81))
        self.m15AngDial.setMinimum(-150)
        self.m15AngDial.setMaximum(150)
        self.m15AngDial.setTracking(True)
        self.m15AngDial.setWrapping(False)
        self.m15AngDial.setNotchTarget(50.0)
        self.m15AngDial.setNotchesVisible(True)
        self.m15AngDial.setObjectName(_fromUtf8("m15AngDial"))
        self.m15PosDial = QtGui.QDial(self.m15SFrame)
        self.m15PosDial.setGeometry(QtCore.QRect(380, 80, 91, 81))
        self.m15PosDial.setMinimum(0)
        self.m15PosDial.setMaximum(1023)
        self.m15PosDial.setTracking(True)
        self.m15PosDial.setWrapping(False)
        self.m15PosDial.setNotchTarget(100.0)
        self.m15PosDial.setNotchesVisible(True)
        self.m15PosDial.setObjectName(_fromUtf8("m15PosDial"))
        self.m15AngNum = QtGui.QLabel(self.m15SFrame)
        self.m15AngNum.setGeometry(QtCore.QRect(120, 200, 61, 21))
        self.m15AngNum.setStyleSheet(_fromUtf8("font: 63 16pt \"KacstArt\";\n"
"border : none;"))
        self.m15AngNum.setObjectName(_fromUtf8("m15AngNum"))
        self.m15PosNum = QtGui.QLabel(self.m15SFrame)
        self.m15PosNum.setGeometry(QtCore.QRect(400, 200, 61, 21))
        self.m15PosNum.setStyleSheet(_fromUtf8("font: 63 16pt \"KacstArt\";\n"
"border : none;"))
        self.m15PosNum.setObjectName(_fromUtf8("m15PosNum"))
        self.m15TorqueNum = QtGui.QLabel(self.m15SFrame)
        self.m15TorqueNum.setGeometry(QtCore.QRect(120, 330, 61, 21))
        self.m15TorqueNum.setStyleSheet(_fromUtf8("font: 63 16pt \"KacstArt\";\n"
"border : none;"))
        self.m15TorqueNum.setObjectName(_fromUtf8("m15TorqueNum"))
        self.m15ErrNum = QtGui.QLabel(self.m15SFrame)
        self.m15ErrNum.setGeometry(QtCore.QRect(260, 440, 61, 21))
        self.m15ErrNum.setStyleSheet(_fromUtf8("font: 63 16pt \"KacstArt\";\n"
"border : none;"))
        self.m15ErrNum.setObjectName(_fromUtf8("m15ErrNum"))
        self.m15TempNum = QtGui.QLabel(self.m15SFrame)
        self.m15TempNum.setGeometry(QtCore.QRect(400, 320, 61, 21))
        self.m15TempNum.setStyleSheet(_fromUtf8("font: 63 16pt \"KacstArt\";\n"
"border : none;"))
        self.m15TempNum.setObjectName(_fromUtf8("m15TempNum"))
        self.stackedWidget.addWidget(self.m15Page)
        self.m16Page = QtGui.QWidget()
        self.m16Page.setObjectName(_fromUtf8("m16Page"))
        self.m16Label = QtGui.QLabel(self.m16Page)
        self.m16Label.setGeometry(QtCore.QRect(340, 10, 91, 21))
        self.m16Label.setStyleSheet(_fromUtf8("font: 63 16pt \"KacstArt\";\n"
"border : none;"))
        self.m16Label.setObjectName(_fromUtf8("m16Label"))
        self.m16CFrame = QtGui.QFrame(self.m16Page)
        self.m16CFrame.setGeometry(QtCore.QRect(580, 40, 211, 501))
        self.m16CFrame.setStyleSheet(_fromUtf8("border : 1px solid rgb(113, 0, 0);\n"
""))
        self.m16CFrame.setObjectName(_fromUtf8("m16CFrame"))
        self.m16GoalTSpin = QtGui.QSpinBox(self.m16CFrame)
        self.m16GoalTSpin.setGeometry(QtCore.QRect(30, 40, 151, 21))
        self.m16GoalTSpin.setStyleSheet(_fromUtf8("font: 63 13pt \"KacstArt\";"))
        self.m16GoalTSpin.setWrapping(False)
        self.m16GoalTSpin.setAccelerated(False)
        self.m16GoalTSpin.setObjectName(_fromUtf8("m16GoalTSpin"))
        self.m16GoalTLabel = QtGui.QLabel(self.m16CFrame)
        self.m16GoalTLabel.setGeometry(QtCore.QRect(60, 10, 111, 21))
        self.m16GoalTLabel.setStyleSheet(_fromUtf8("font: 63 14pt \"KacstArt\";\n"
"border : none;"))
        self.m16GoalTLabel.setObjectName(_fromUtf8("m16GoalTLabel"))
        self.m16UpdateBtn = QtGui.QPushButton(self.m16CFrame)
        self.m16UpdateBtn.setGeometry(QtCore.QRect(20, 290, 171, 41))
        self.m16UpdateBtn.setAutoFillBackground(False)
        self.m16UpdateBtn.setStyleSheet(_fromUtf8("QPushButton\n"
"{font: 63 14pt \"KacstArt\";\n"
"border : 2px solid black;\n"
"}\n"
"QPushButton:pressed\n"
"{    \n"
"    background-color : rgb(209,209,224);\n"
"}\n"
"\n"
"        "))
        self.m16UpdateBtn.setAutoDefault(False)
        self.m16UpdateBtn.setDefault(False)
        self.m16UpdateBtn.setFlat(False)
        self.m16UpdateBtn.setObjectName(_fromUtf8("m16UpdateBtn"))
        self.m16AngleLabel = QtGui.QLabel(self.m16CFrame)
        self.m16AngleLabel.setGeometry(QtCore.QRect(80, 70, 61, 21))
        self.m16AngleLabel.setStyleSheet(_fromUtf8("font: 63 14pt \"KacstArt\";\n"
"border : none;"))
        self.m16AngleLabel.setObjectName(_fromUtf8("m16AngleLabel"))
        self.m16AngleSpin = QtGui.QSpinBox(self.m16CFrame)
        self.m16AngleSpin.setGeometry(QtCore.QRect(30, 100, 151, 21))
        self.m16AngleSpin.setStyleSheet(_fromUtf8("font: 63 13pt \"KacstArt\";"))
        self.m16AngleSpin.setWrapping(False)
        self.m16AngleSpin.setAccelerated(False)
        self.m16AngleSpin.setMinimum(-150)
        self.m16AngleSpin.setMaximum(150)
        self.m16AngleSpin.setObjectName(_fromUtf8("m16AngleSpin"))
        self.m16PositionSpin = QtGui.QSpinBox(self.m16CFrame)
        self.m16PositionSpin.setGeometry(QtCore.QRect(30, 190, 151, 21))
        self.m16PositionSpin.setStyleSheet(_fromUtf8("font: 63 13pt \"KacstArt\";"))
        self.m16PositionSpin.setWrapping(False)
        self.m16PositionSpin.setAccelerated(False)
        self.m16PositionSpin.setMaximum(1023)
        self.m16PositionSpin.setObjectName(_fromUtf8("m16PositionSpin"))
        self.m16PositionLabel = QtGui.QLabel(self.m16CFrame)
        self.m16PositionLabel.setGeometry(QtCore.QRect(70, 170, 81, 21))
        self.m16PositionLabel.setStyleSheet(_fromUtf8("font: 63 14pt \"KacstArt\";\n"
"border : none;"))
        self.m16PositionLabel.setObjectName(_fromUtf8("m16PositionLabel"))
        self.m16AngleBtn = QtGui.QPushButton(self.m16CFrame)
        self.m16AngleBtn.setGeometry(QtCore.QRect(30, 130, 151, 21))
        self.m16AngleBtn.setStyleSheet(_fromUtf8("QPushButton\n"
"{font: 63 12pt \"KacstArt\";\n"
"border : 2px solid black;\n"
"}\n"
"QPushButton:pressed\n"
"{    \n"
"    background-color : rgb(209,209,224);\n"
"}\n"
"\n"
"        "))
        self.m16AngleBtn.setObjectName(_fromUtf8("m16AngleBtn"))
        self.m16PositionBtn = QtGui.QPushButton(self.m16CFrame)
        self.m16PositionBtn.setGeometry(QtCore.QRect(30, 220, 151, 21))
        self.m16PositionBtn.setStyleSheet(_fromUtf8("QPushButton\n"
"{font: 63 12pt \"KacstArt\";\n"
"border : 2px solid black;\n"
"}\n"
"QPushButton:pressed\n"
"{    \n"
"    background-color : rgb(209,209,224);\n"
"}\n"
"\n"
"        "))
        self.m16PositionBtn.setObjectName(_fromUtf8("m16PositionBtn"))
        self.m16HomeBtn = QtGui.QPushButton(self.m16CFrame)
        self.m16HomeBtn.setGeometry(QtCore.QRect(20, 370, 171, 61))
        self.m16HomeBtn.setStyleSheet(_fromUtf8("QPushButton\n"
"{font: 63 14pt \"KacstArt\";\n"
"border : 2px solid black;\n"
"}\n"
"QPushButton:pressed\n"
"{    \n"
"    background-color : rgb(209,209,224);\n"
"}\n"
"\n"
"        "))
        self.m16HomeBtn.setObjectName(_fromUtf8("m16HomeBtn"))
        self.m16SFrame = QtGui.QFrame(self.m16Page)
        self.m16SFrame.setGeometry(QtCore.QRect(10, 40, 561, 501))
        self.m16SFrame.setStyleSheet(_fromUtf8("border : 1px solid rgb(113, 0, 0);\n"
""))
        self.m16SFrame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.m16SFrame.setFrameShadow(QtGui.QFrame.Raised)
        self.m16SFrame.setObjectName(_fromUtf8("m16SFrame"))
        self.m16AngLabel = QtGui.QLabel(self.m16SFrame)
        self.m16AngLabel.setGeometry(QtCore.QRect(120, 40, 61, 21))
        self.m16AngLabel.setStyleSheet(_fromUtf8("font: 63 16pt \"KacstArt\";\n"
"border : none;"))
        self.m16AngLabel.setObjectName(_fromUtf8("m16AngLabel"))
        self.m16PosLabel = QtGui.QLabel(self.m16SFrame)
        self.m16PosLabel.setGeometry(QtCore.QRect(390, 40, 91, 21))
        self.m16PosLabel.setStyleSheet(_fromUtf8("font: 63 16pt \"KacstArt\";\n"
"border : none;"))
        self.m16PosLabel.setObjectName(_fromUtf8("m16PosLabel"))
        self.m16TorqueLabel = QtGui.QLabel(self.m16SFrame)
        self.m16TorqueLabel.setGeometry(QtCore.QRect(80, 270, 141, 21))
        self.m16TorqueLabel.setStyleSheet(_fromUtf8("font: 63 16pt \"KacstArt\";\n"
"border : none;"))
        self.m16TorqueLabel.setObjectName(_fromUtf8("m16TorqueLabel"))
        self.m16TempLabel = QtGui.QLabel(self.m16SFrame)
        self.m16TempLabel.setGeometry(QtCore.QRect(370, 270, 131, 21))
        self.m16TempLabel.setStyleSheet(_fromUtf8("font: 63 16pt \"KacstArt\";\n"
"border : none;"))
        self.m16TempLabel.setObjectName(_fromUtf8("m16TempLabel"))
        self.m16ErrLabel = QtGui.QLabel(self.m16SFrame)
        self.m16ErrLabel.setGeometry(QtCore.QRect(260, 390, 61, 21))
        self.m16ErrLabel.setStyleSheet(_fromUtf8("font: 63 16pt \"KacstArt\";\n"
"border : none;"))
        self.m16ErrLabel.setObjectName(_fromUtf8("m16ErrLabel"))
        self.m16AngDial = QtGui.QDial(self.m16SFrame)
        self.m16AngDial.setGeometry(QtCore.QRect(100, 80, 91, 81))
        self.m16AngDial.setMinimum(-150)
        self.m16AngDial.setMaximum(150)
        self.m16AngDial.setTracking(True)
        self.m16AngDial.setWrapping(False)
        self.m16AngDial.setNotchTarget(50.0)
        self.m16AngDial.setNotchesVisible(True)
        self.m16AngDial.setObjectName(_fromUtf8("m16AngDial"))
        self.m16PosDial = QtGui.QDial(self.m16SFrame)
        self.m16PosDial.setGeometry(QtCore.QRect(380, 80, 91, 81))
        self.m16PosDial.setMinimum(0)
        self.m16PosDial.setMaximum(1023)
        self.m16PosDial.setTracking(True)
        self.m16PosDial.setWrapping(False)
        self.m16PosDial.setNotchTarget(100.0)
        self.m16PosDial.setNotchesVisible(True)
        self.m16PosDial.setObjectName(_fromUtf8("m16PosDial"))
        self.m16AngNum = QtGui.QLabel(self.m16SFrame)
        self.m16AngNum.setGeometry(QtCore.QRect(120, 200, 61, 21))
        self.m16AngNum.setStyleSheet(_fromUtf8("font: 63 16pt \"KacstArt\";\n"
"border : none;"))
        self.m16AngNum.setObjectName(_fromUtf8("m16AngNum"))
        self.m16PosNum = QtGui.QLabel(self.m16SFrame)
        self.m16PosNum.setGeometry(QtCore.QRect(400, 200, 61, 21))
        self.m16PosNum.setStyleSheet(_fromUtf8("font: 63 16pt \"KacstArt\";\n"
"border : none;"))
        self.m16PosNum.setObjectName(_fromUtf8("m16PosNum"))
        self.m16TorqueNum = QtGui.QLabel(self.m16SFrame)
        self.m16TorqueNum.setGeometry(QtCore.QRect(120, 330, 61, 21))
        self.m16TorqueNum.setStyleSheet(_fromUtf8("font: 63 16pt \"KacstArt\";\n"
"border : none;"))
        self.m16TorqueNum.setObjectName(_fromUtf8("m16TorqueNum"))
        self.m16ErrNum = QtGui.QLabel(self.m16SFrame)
        self.m16ErrNum.setGeometry(QtCore.QRect(260, 440, 61, 21))
        self.m16ErrNum.setStyleSheet(_fromUtf8("font: 63 16pt \"KacstArt\";\n"
"border : none;"))
        self.m16ErrNum.setObjectName(_fromUtf8("m16ErrNum"))
        self.m16TempNum = QtGui.QLabel(self.m16SFrame)
        self.m16TempNum.setGeometry(QtCore.QRect(400, 320, 61, 21))
        self.m16TempNum.setStyleSheet(_fromUtf8("font: 63 16pt \"KacstArt\";\n"
"border : none;"))
        self.m16TempNum.setObjectName(_fromUtf8("m16TempNum"))
        self.stackedWidget.addWidget(self.m16Page)
        self.m17Page = QtGui.QWidget()
        self.m17Page.setObjectName(_fromUtf8("m17Page"))
        self.m17Label = QtGui.QLabel(self.m17Page)
        self.m17Label.setGeometry(QtCore.QRect(340, 10, 91, 21))
        self.m17Label.setStyleSheet(_fromUtf8("font: 63 16pt \"KacstArt\";\n"
"border : none;"))
        self.m17Label.setObjectName(_fromUtf8("m17Label"))
        self.m17CFrame = QtGui.QFrame(self.m17Page)
        self.m17CFrame.setGeometry(QtCore.QRect(580, 40, 211, 501))
        self.m17CFrame.setStyleSheet(_fromUtf8("border : 1px solid rgb(113, 0, 0);\n"
""))
        self.m17CFrame.setObjectName(_fromUtf8("m17CFrame"))
        self.m17GoalTSpin = QtGui.QSpinBox(self.m17CFrame)
        self.m17GoalTSpin.setGeometry(QtCore.QRect(30, 40, 151, 21))
        self.m17GoalTSpin.setStyleSheet(_fromUtf8("font: 63 13pt \"KacstArt\";"))
        self.m17GoalTSpin.setWrapping(False)
        self.m17GoalTSpin.setAccelerated(False)
        self.m17GoalTSpin.setObjectName(_fromUtf8("m17GoalTSpin"))
        self.m17GoalTLabel = QtGui.QLabel(self.m17CFrame)
        self.m17GoalTLabel.setGeometry(QtCore.QRect(60, 10, 111, 21))
        self.m17GoalTLabel.setStyleSheet(_fromUtf8("font: 63 14pt \"KacstArt\";\n"
"border : none;"))
        self.m17GoalTLabel.setObjectName(_fromUtf8("m17GoalTLabel"))
        self.m17UpdateBtn = QtGui.QPushButton(self.m17CFrame)
        self.m17UpdateBtn.setGeometry(QtCore.QRect(20, 290, 171, 41))
        self.m17UpdateBtn.setAutoFillBackground(False)
        self.m17UpdateBtn.setStyleSheet(_fromUtf8("QPushButton\n"
"{font: 63 14pt \"KacstArt\";\n"
"border : 2px solid black;\n"
"}\n"
"QPushButton:pressed\n"
"{    \n"
"    background-color : rgb(209,209,224);\n"
"}\n"
"\n"
"        "))
        self.m17UpdateBtn.setAutoDefault(False)
        self.m17UpdateBtn.setDefault(False)
        self.m17UpdateBtn.setFlat(False)
        self.m17UpdateBtn.setObjectName(_fromUtf8("m17UpdateBtn"))
        self.m17AngleLabel = QtGui.QLabel(self.m17CFrame)
        self.m17AngleLabel.setGeometry(QtCore.QRect(80, 70, 61, 21))
        self.m17AngleLabel.setStyleSheet(_fromUtf8("font: 63 14pt \"KacstArt\";\n"
"border : none;"))
        self.m17AngleLabel.setObjectName(_fromUtf8("m17AngleLabel"))
        self.m17AngleSpin = QtGui.QSpinBox(self.m17CFrame)
        self.m17AngleSpin.setGeometry(QtCore.QRect(30, 100, 151, 21))
        self.m17AngleSpin.setStyleSheet(_fromUtf8("font: 63 13pt \"KacstArt\";"))
        self.m17AngleSpin.setWrapping(False)
        self.m17AngleSpin.setAccelerated(False)
        self.m17AngleSpin.setMinimum(-150)
        self.m17AngleSpin.setMaximum(150)
        self.m17AngleSpin.setObjectName(_fromUtf8("m17AngleSpin"))
        self.m17PositionSpin = QtGui.QSpinBox(self.m17CFrame)
        self.m17PositionSpin.setGeometry(QtCore.QRect(30, 190, 151, 21))
        self.m17PositionSpin.setStyleSheet(_fromUtf8("font: 63 13pt \"KacstArt\";"))
        self.m17PositionSpin.setWrapping(False)
        self.m17PositionSpin.setAccelerated(False)
        self.m17PositionSpin.setMaximum(1023)
        self.m17PositionSpin.setObjectName(_fromUtf8("m17PositionSpin"))
        self.m17PositionLabel = QtGui.QLabel(self.m17CFrame)
        self.m17PositionLabel.setGeometry(QtCore.QRect(70, 170, 81, 21))
        self.m17PositionLabel.setStyleSheet(_fromUtf8("font: 63 14pt \"KacstArt\";\n"
"border : none;"))
        self.m17PositionLabel.setObjectName(_fromUtf8("m17PositionLabel"))
        self.m17AngleBtn = QtGui.QPushButton(self.m17CFrame)
        self.m17AngleBtn.setGeometry(QtCore.QRect(30, 130, 151, 21))
        self.m17AngleBtn.setStyleSheet(_fromUtf8("QPushButton\n"
"{font: 63 12pt \"KacstArt\";\n"
"border : 2px solid black;\n"
"}\n"
"QPushButton:pressed\n"
"{    \n"
"    background-color : rgb(209,209,224);\n"
"}\n"
"\n"
"        "))
        self.m17AngleBtn.setObjectName(_fromUtf8("m17AngleBtn"))
        self.m17PositionBtn = QtGui.QPushButton(self.m17CFrame)
        self.m17PositionBtn.setGeometry(QtCore.QRect(30, 220, 151, 21))
        self.m17PositionBtn.setStyleSheet(_fromUtf8("QPushButton\n"
"{font: 63 12pt \"KacstArt\";\n"
"border : 2px solid black;\n"
"}\n"
"QPushButton:pressed\n"
"{    \n"
"    background-color : rgb(209,209,224);\n"
"}\n"
"\n"
"        "))
        self.m17PositionBtn.setObjectName(_fromUtf8("m17PositionBtn"))
        self.m17HomeBtn = QtGui.QPushButton(self.m17CFrame)
        self.m17HomeBtn.setGeometry(QtCore.QRect(20, 370, 171, 61))
        self.m17HomeBtn.setStyleSheet(_fromUtf8("QPushButton\n"
"{font: 63 14pt \"KacstArt\";\n"
"border : 2px solid black;\n"
"}\n"
"QPushButton:pressed\n"
"{    \n"
"    background-color : rgb(209,209,224);\n"
"}\n"
"\n"
"        "))
        self.m17HomeBtn.setObjectName(_fromUtf8("m17HomeBtn"))
        self.m17SFrame = QtGui.QFrame(self.m17Page)
        self.m17SFrame.setGeometry(QtCore.QRect(10, 40, 561, 501))
        self.m17SFrame.setStyleSheet(_fromUtf8("border : 1px solid rgb(113, 0, 0);\n"
""))
        self.m17SFrame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.m17SFrame.setFrameShadow(QtGui.QFrame.Raised)
        self.m17SFrame.setObjectName(_fromUtf8("m17SFrame"))
        self.m17AngLabel = QtGui.QLabel(self.m17SFrame)
        self.m17AngLabel.setGeometry(QtCore.QRect(120, 40, 61, 21))
        self.m17AngLabel.setStyleSheet(_fromUtf8("font: 63 16pt \"KacstArt\";\n"
"border : none;"))
        self.m17AngLabel.setObjectName(_fromUtf8("m17AngLabel"))
        self.m17PosLabel = QtGui.QLabel(self.m17SFrame)
        self.m17PosLabel.setGeometry(QtCore.QRect(390, 40, 91, 21))
        self.m17PosLabel.setStyleSheet(_fromUtf8("font: 63 16pt \"KacstArt\";\n"
"border : none;"))
        self.m17PosLabel.setObjectName(_fromUtf8("m17PosLabel"))
        self.m17TorqueLabel = QtGui.QLabel(self.m17SFrame)
        self.m17TorqueLabel.setGeometry(QtCore.QRect(80, 270, 141, 21))
        self.m17TorqueLabel.setStyleSheet(_fromUtf8("font: 63 16pt \"KacstArt\";\n"
"border : none;"))
        self.m17TorqueLabel.setObjectName(_fromUtf8("m17TorqueLabel"))
        self.m17TempLabel = QtGui.QLabel(self.m17SFrame)
        self.m17TempLabel.setGeometry(QtCore.QRect(370, 270, 131, 21))
        self.m17TempLabel.setStyleSheet(_fromUtf8("font: 63 16pt \"KacstArt\";\n"
"border : none;"))
        self.m17TempLabel.setObjectName(_fromUtf8("m17TempLabel"))
        self.m17ErrLabel = QtGui.QLabel(self.m17SFrame)
        self.m17ErrLabel.setGeometry(QtCore.QRect(260, 390, 61, 21))
        self.m17ErrLabel.setStyleSheet(_fromUtf8("font: 63 16pt \"KacstArt\";\n"
"border : none;"))
        self.m17ErrLabel.setObjectName(_fromUtf8("m17ErrLabel"))
        self.m17AngDial = QtGui.QDial(self.m17SFrame)
        self.m17AngDial.setGeometry(QtCore.QRect(100, 80, 91, 81))
        self.m17AngDial.setMinimum(-150)
        self.m17AngDial.setMaximum(150)
        self.m17AngDial.setTracking(True)
        self.m17AngDial.setWrapping(False)
        self.m17AngDial.setNotchTarget(50.0)
        self.m17AngDial.setNotchesVisible(True)
        self.m17AngDial.setObjectName(_fromUtf8("m17AngDial"))
        self.m17PosDial = QtGui.QDial(self.m17SFrame)
        self.m17PosDial.setGeometry(QtCore.QRect(380, 80, 91, 81))
        self.m17PosDial.setMinimum(0)
        self.m17PosDial.setMaximum(1023)
        self.m17PosDial.setTracking(True)
        self.m17PosDial.setWrapping(False)
        self.m17PosDial.setNotchTarget(100.0)
        self.m17PosDial.setNotchesVisible(True)
        self.m17PosDial.setObjectName(_fromUtf8("m17PosDial"))
        self.m17AngNum = QtGui.QLabel(self.m17SFrame)
        self.m17AngNum.setGeometry(QtCore.QRect(120, 200, 61, 21))
        self.m17AngNum.setStyleSheet(_fromUtf8("font: 63 16pt \"KacstArt\";\n"
"border : none;"))
        self.m17AngNum.setObjectName(_fromUtf8("m17AngNum"))
        self.m17PosNum = QtGui.QLabel(self.m17SFrame)
        self.m17PosNum.setGeometry(QtCore.QRect(400, 200, 61, 21))
        self.m17PosNum.setStyleSheet(_fromUtf8("font: 63 16pt \"KacstArt\";\n"
"border : none;"))
        self.m17PosNum.setObjectName(_fromUtf8("m17PosNum"))
        self.m17TorqueNum = QtGui.QLabel(self.m17SFrame)
        self.m17TorqueNum.setGeometry(QtCore.QRect(120, 330, 61, 21))
        self.m17TorqueNum.setStyleSheet(_fromUtf8("font: 63 16pt \"KacstArt\";\n"
"border : none;"))
        self.m17TorqueNum.setObjectName(_fromUtf8("m17TorqueNum"))
        self.m17ErrNum = QtGui.QLabel(self.m17SFrame)
        self.m17ErrNum.setGeometry(QtCore.QRect(260, 440, 61, 21))
        self.m17ErrNum.setStyleSheet(_fromUtf8("font: 63 16pt \"KacstArt\";\n"
"border : none;"))
        self.m17ErrNum.setObjectName(_fromUtf8("m17ErrNum"))
        self.m17TempNum = QtGui.QLabel(self.m17SFrame)
        self.m17TempNum.setGeometry(QtCore.QRect(400, 320, 61, 21))
        self.m17TempNum.setStyleSheet(_fromUtf8("font: 63 16pt \"KacstArt\";\n"
"border : none;"))
        self.m17TempNum.setObjectName(_fromUtf8("m17TempNum"))
        self.stackedWidget.addWidget(self.m17Page)
        self.m18Page = QtGui.QWidget()
        self.m18Page.setObjectName(_fromUtf8("m18Page"))
        self.m18Label = QtGui.QLabel(self.m18Page)
        self.m18Label.setGeometry(QtCore.QRect(340, 10, 91, 21))
        self.m18Label.setStyleSheet(_fromUtf8("font: 63 16pt \"KacstArt\";\n"
"border : none;"))
        self.m18Label.setObjectName(_fromUtf8("m18Label"))
        self.m18CFrame = QtGui.QFrame(self.m18Page)
        self.m18CFrame.setGeometry(QtCore.QRect(580, 40, 211, 501))
        self.m18CFrame.setStyleSheet(_fromUtf8("border : 1px solid rgb(113, 0, 0);\n"
""))
        self.m18CFrame.setObjectName(_fromUtf8("m18CFrame"))
        self.m18GoalTSpin = QtGui.QSpinBox(self.m18CFrame)
        self.m18GoalTSpin.setGeometry(QtCore.QRect(30, 40, 151, 21))
        self.m18GoalTSpin.setStyleSheet(_fromUtf8("font: 63 13pt \"KacstArt\";"))
        self.m18GoalTSpin.setWrapping(False)
        self.m18GoalTSpin.setAccelerated(False)
        self.m18GoalTSpin.setObjectName(_fromUtf8("m18GoalTSpin"))
        self.m18GoalTLabel = QtGui.QLabel(self.m18CFrame)
        self.m18GoalTLabel.setGeometry(QtCore.QRect(60, 10, 111, 21))
        self.m18GoalTLabel.setStyleSheet(_fromUtf8("font: 63 14pt \"KacstArt\";\n"
"border : none;"))
        self.m18GoalTLabel.setObjectName(_fromUtf8("m18GoalTLabel"))
        self.m18UpdateBtn = QtGui.QPushButton(self.m18CFrame)
        self.m18UpdateBtn.setGeometry(QtCore.QRect(20, 290, 171, 41))
        self.m18UpdateBtn.setAutoFillBackground(False)
        self.m18UpdateBtn.setStyleSheet(_fromUtf8("QPushButton\n"
"{font: 63 14pt \"KacstArt\";\n"
"border : 2px solid black;\n"
"}\n"
"QPushButton:pressed\n"
"{    \n"
"    background-color : rgb(209,209,224);\n"
"}\n"
"\n"
"        "))
        self.m18UpdateBtn.setAutoDefault(False)
        self.m18UpdateBtn.setDefault(False)
        self.m18UpdateBtn.setFlat(False)
        self.m18UpdateBtn.setObjectName(_fromUtf8("m18UpdateBtn"))
        self.m18AngleLabel = QtGui.QLabel(self.m18CFrame)
        self.m18AngleLabel.setGeometry(QtCore.QRect(80, 70, 61, 21))
        self.m18AngleLabel.setStyleSheet(_fromUtf8("font: 63 14pt \"KacstArt\";\n"
"border : none;"))
        self.m18AngleLabel.setObjectName(_fromUtf8("m18AngleLabel"))
        self.m18AngleSpin = QtGui.QSpinBox(self.m18CFrame)
        self.m18AngleSpin.setGeometry(QtCore.QRect(30, 100, 151, 21))
        self.m18AngleSpin.setStyleSheet(_fromUtf8("font: 63 13pt \"KacstArt\";"))
        self.m18AngleSpin.setWrapping(False)
        self.m18AngleSpin.setAccelerated(False)
        self.m18AngleSpin.setMinimum(-150)
        self.m18AngleSpin.setMaximum(150)
        self.m18AngleSpin.setObjectName(_fromUtf8("m18AngleSpin"))
        self.m18PositionSpin = QtGui.QSpinBox(self.m18CFrame)
        self.m18PositionSpin.setGeometry(QtCore.QRect(30, 190, 151, 21))
        self.m18PositionSpin.setStyleSheet(_fromUtf8("font: 63 13pt \"KacstArt\";"))
        self.m18PositionSpin.setWrapping(False)
        self.m18PositionSpin.setAccelerated(False)
        self.m18PositionSpin.setMaximum(1023)
        self.m18PositionSpin.setObjectName(_fromUtf8("m18PositionSpin"))
        self.m18PositionLabel = QtGui.QLabel(self.m18CFrame)
        self.m18PositionLabel.setGeometry(QtCore.QRect(70, 170, 81, 21))
        self.m18PositionLabel.setStyleSheet(_fromUtf8("font: 63 14pt \"KacstArt\";\n"
"border : none;"))
        self.m18PositionLabel.setObjectName(_fromUtf8("m18PositionLabel"))
        self.m18AngleBtn = QtGui.QPushButton(self.m18CFrame)
        self.m18AngleBtn.setGeometry(QtCore.QRect(30, 130, 151, 21))
        self.m18AngleBtn.setStyleSheet(_fromUtf8("QPushButton\n"
"{font: 63 12pt \"KacstArt\";\n"
"border : 2px solid black;\n"
"}\n"
"QPushButton:pressed\n"
"{    \n"
"    background-color : rgb(209,209,224);\n"
"}\n"
"\n"
"        "))
        self.m18AngleBtn.setObjectName(_fromUtf8("m18AngleBtn"))
        self.m18PositionBtn = QtGui.QPushButton(self.m18CFrame)
        self.m18PositionBtn.setGeometry(QtCore.QRect(30, 220, 151, 21))
        self.m18PositionBtn.setStyleSheet(_fromUtf8("QPushButton\n"
"{font: 63 12pt \"KacstArt\";\n"
"border : 2px solid black;\n"
"}\n"
"QPushButton:pressed\n"
"{    \n"
"    background-color : rgb(209,209,224);\n"
"}\n"
"\n"
"        "))
        self.m18PositionBtn.setObjectName(_fromUtf8("m18PositionBtn"))
        self.m18HomeBtn = QtGui.QPushButton(self.m18CFrame)
        self.m18HomeBtn.setGeometry(QtCore.QRect(20, 370, 171, 61))
        self.m18HomeBtn.setStyleSheet(_fromUtf8("QPushButton\n"
"{font: 63 14pt \"KacstArt\";\n"
"border : 2px solid black;\n"
"}\n"
"QPushButton:pressed\n"
"{    \n"
"    background-color : rgb(209,209,224);\n"
"}\n"
"\n"
"        "))
        self.m18HomeBtn.setObjectName(_fromUtf8("m18HomeBtn"))
        self.m18SFrame = QtGui.QFrame(self.m18Page)
        self.m18SFrame.setGeometry(QtCore.QRect(10, 40, 561, 501))
        self.m18SFrame.setStyleSheet(_fromUtf8("border : 1px solid rgb(113, 0, 0);\n"
""))
        self.m18SFrame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.m18SFrame.setFrameShadow(QtGui.QFrame.Raised)
        self.m18SFrame.setObjectName(_fromUtf8("m18SFrame"))
        self.m18AngLabel = QtGui.QLabel(self.m18SFrame)
        self.m18AngLabel.setGeometry(QtCore.QRect(120, 40, 61, 21))
        self.m18AngLabel.setStyleSheet(_fromUtf8("font: 63 16pt \"KacstArt\";\n"
"border : none;"))
        self.m18AngLabel.setObjectName(_fromUtf8("m18AngLabel"))
        self.m18PosLabel = QtGui.QLabel(self.m18SFrame)
        self.m18PosLabel.setGeometry(QtCore.QRect(390, 40, 91, 21))
        self.m18PosLabel.setStyleSheet(_fromUtf8("font: 63 16pt \"KacstArt\";\n"
"border : none;"))
        self.m18PosLabel.setObjectName(_fromUtf8("m18PosLabel"))
        self.m18TorqueLabel = QtGui.QLabel(self.m18SFrame)
        self.m18TorqueLabel.setGeometry(QtCore.QRect(80, 270, 141, 21))
        self.m18TorqueLabel.setStyleSheet(_fromUtf8("font: 63 16pt \"KacstArt\";\n"
"border : none;"))
        self.m18TorqueLabel.setObjectName(_fromUtf8("m18TorqueLabel"))
        self.m18TempLabel = QtGui.QLabel(self.m18SFrame)
        self.m18TempLabel.setGeometry(QtCore.QRect(370, 270, 131, 21))
        self.m18TempLabel.setStyleSheet(_fromUtf8("font: 63 16pt \"KacstArt\";\n"
"border : none;"))
        self.m18TempLabel.setObjectName(_fromUtf8("m18TempLabel"))
        self.m18ErrLabel = QtGui.QLabel(self.m18SFrame)
        self.m18ErrLabel.setGeometry(QtCore.QRect(260, 390, 61, 21))
        self.m18ErrLabel.setStyleSheet(_fromUtf8("font: 63 16pt \"KacstArt\";\n"
"border : none;"))
        self.m18ErrLabel.setObjectName(_fromUtf8("m18ErrLabel"))
        self.m18AngDial = QtGui.QDial(self.m18SFrame)
        self.m18AngDial.setGeometry(QtCore.QRect(100, 80, 91, 81))
        self.m18AngDial.setMinimum(-150)
        self.m18AngDial.setMaximum(150)
        self.m18AngDial.setTracking(True)
        self.m18AngDial.setWrapping(False)
        self.m18AngDial.setNotchTarget(50.0)
        self.m18AngDial.setNotchesVisible(True)
        self.m18AngDial.setObjectName(_fromUtf8("m18AngDial"))
        self.m18PosDial = QtGui.QDial(self.m18SFrame)
        self.m18PosDial.setGeometry(QtCore.QRect(380, 80, 91, 81))
        self.m18PosDial.setMinimum(0)
        self.m18PosDial.setMaximum(1023)
        self.m18PosDial.setTracking(True)
        self.m18PosDial.setWrapping(False)
        self.m18PosDial.setNotchTarget(100.0)
        self.m18PosDial.setNotchesVisible(True)
        self.m18PosDial.setObjectName(_fromUtf8("m18PosDial"))
        self.m18AngNum = QtGui.QLabel(self.m18SFrame)
        self.m18AngNum.setGeometry(QtCore.QRect(120, 200, 61, 21))
        self.m18AngNum.setStyleSheet(_fromUtf8("font: 63 16pt \"KacstArt\";\n"
"border : none;"))
        self.m18AngNum.setObjectName(_fromUtf8("m18AngNum"))
        self.m18PosNum = QtGui.QLabel(self.m18SFrame)
        self.m18PosNum.setGeometry(QtCore.QRect(400, 200, 61, 21))
        self.m18PosNum.setStyleSheet(_fromUtf8("font: 63 16pt \"KacstArt\";\n"
"border : none;"))
        self.m18PosNum.setObjectName(_fromUtf8("m18PosNum"))
        self.m18TorqueNum = QtGui.QLabel(self.m18SFrame)
        self.m18TorqueNum.setGeometry(QtCore.QRect(120, 320, 61, 21))
        self.m18TorqueNum.setStyleSheet(_fromUtf8("font: 63 16pt \"KacstArt\";\n"
"border : none;"))
        self.m18TorqueNum.setObjectName(_fromUtf8("m18TorqueNum"))
        self.m18ErrNum = QtGui.QLabel(self.m18SFrame)
        self.m18ErrNum.setGeometry(QtCore.QRect(260, 440, 61, 21))
        self.m18ErrNum.setStyleSheet(_fromUtf8("font: 63 16pt \"KacstArt\";\n"
"border : none;"))
        self.m18ErrNum.setObjectName(_fromUtf8("m18ErrNum"))
        self.m18TempNum = QtGui.QLabel(self.m18SFrame)
        self.m18TempNum.setGeometry(QtCore.QRect(400, 320, 61, 21))
        self.m18TempNum.setStyleSheet(_fromUtf8("font: 63 16pt \"KacstArt\";\n"
"border : none;"))
        self.m18TempNum.setObjectName(_fromUtf8("m18TempNum"))
        self.stackedWidget.addWidget(self.m18Page)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 25))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(0)
        #MyCode Start
        self.recs = []
        self.torquesOn()
        self.updateMotors()
        thread.start_new_thread(self.updateThread, ())

        #Shifting between pages Start
        self.mGoBtn.clicked.connect(self.forward)
        mHomeBtns = [self.m1HomeBtn, self.m2HomeBtn, self.m3HomeBtn, self.m4HomeBtn,
                     self.m5HomeBtn, self.m6HomeBtn, self.m7HomeBtn, self.m8HomeBtn,
                     self.m9HomeBtn, self.m10HomeBtn, self.m11HomeBtn, self.m12HomeBtn,
                     self.m13HomeBtn, self.m14HomeBtn, self.m15HomeBtn, self.m16HomeBtn,
                     self.m17HomeBtn, self.m18HomeBtn]
        for mhomeBtn in mHomeBtns:
            mhomeBtn.clicked.connect(self.backward)
        #Shifting between Pages Finish

        #Dialing Start
        self.m1AngDial.valueChanged.connect(lambda: self.updateAngDial(1))
        self.m2AngDial.valueChanged.connect(lambda: self.updateAngDial(2))
        self.m3AngDial.valueChanged.connect(lambda: self.updateAngDial(3))
        self.m4AngDial.valueChanged.connect(lambda: self.updateAngDial(4))
        self.m5AngDial.valueChanged.connect(lambda: self.updateAngDial(5))
        self.m6AngDial.valueChanged.connect(lambda: self.updateAngDial(6))
        self.m7AngDial.valueChanged.connect(lambda: self.updateAngDial(7))
        self.m8AngDial.valueChanged.connect(lambda: self.updateAngDial(8))
        self.m9AngDial.valueChanged.connect(lambda: self.updateAngDial(9))
        self.m10AngDial.valueChanged.connect(lambda: self.updateAngDial(10))
        self.m11AngDial.valueChanged.connect(lambda: self.updateAngDial(11))
        self.m12AngDial.valueChanged.connect(lambda: self.updateAngDial(12))
        self.m13AngDial.valueChanged.connect(lambda: self.updateAngDial(13))
        self.m14AngDial.valueChanged.connect(lambda: self.updateAngDial(14))
        self.m15AngDial.valueChanged.connect(lambda: self.updateAngDial(15))
        self.m16AngDial.valueChanged.connect(lambda: self.updateAngDial(16))
        self.m17AngDial.valueChanged.connect(lambda: self.updateAngDial(17))
        self.m18AngDial.valueChanged.connect(lambda: self.updateAngDial(18))

        self.m1PosDial.valueChanged.connect(lambda: self.updatePosDial(1))
        self.m2PosDial.valueChanged.connect(lambda: self.updatePosDial(2))
        self.m3PosDial.valueChanged.connect(lambda: self.updatePosDial(3))
        self.m4PosDial.valueChanged.connect(lambda: self.updatePosDial(4))
        self.m5PosDial.valueChanged.connect(lambda: self.updatePosDial(5))
        self.m6PosDial.valueChanged.connect(lambda: self.updatePosDial(6))
        self.m7PosDial.valueChanged.connect(lambda: self.updatePosDial(7))
        self.m8PosDial.valueChanged.connect(lambda: self.updatePosDial(8))
        self.m9PosDial.valueChanged.connect(lambda: self.updatePosDial(9))
        self.m10PosDial.valueChanged.connect(lambda: self.updatePosDial(10))
        self.m11PosDial.valueChanged.connect(lambda: self.updatePosDial(11))
        self.m12PosDial.valueChanged.connect(lambda: self.updatePosDial(12))
        self.m13PosDial.valueChanged.connect(lambda: self.updatePosDial(13))
        self.m14PosDial.valueChanged.connect(lambda: self.updatePosDial(14))
        self.m15PosDial.valueChanged.connect(lambda: self.updatePosDial(15))
        self.m16PosDial.valueChanged.connect(lambda: self.updatePosDial(16))
        self.m17PosDial.valueChanged.connect(lambda: self.updatePosDial(17))
        self.m18PosDial.valueChanged.connect(lambda: self.updatePosDial(18))
        #Dialing Finished

        #Ang Start
        self.m1AngleBtn.clicked.connect(lambda: self.updateAng(1))
        self.m2AngleBtn.clicked.connect(lambda: self.updateAng(2))
        self.m3AngleBtn.clicked.connect(lambda: self.updateAng(3))
        self.m4AngleBtn.clicked.connect(lambda: self.updateAng(4))
        self.m5AngleBtn.clicked.connect(lambda: self.updateAng(5))
        self.m6AngleBtn.clicked.connect(lambda: self.updateAng(6))
        self.m7AngleBtn.clicked.connect(lambda: self.updateAng(7))
        self.m8AngleBtn.clicked.connect(lambda: self.updateAng(8))
        self.m9AngleBtn.clicked.connect(lambda: self.updateAng(9))
        self.m10AngleBtn.clicked.connect(lambda: self.updateAng(10))
        self.m11AngleBtn.clicked.connect(lambda: self.updateAng(11))
        self.m12AngleBtn.clicked.connect(lambda: self.updateAng(12))
        self.m13AngleBtn.clicked.connect(lambda: self.updateAng(13))
        self.m14AngleBtn.clicked.connect(lambda: self.updateAng(14))
        self.m15AngleBtn.clicked.connect(lambda: self.updateAng(15))
        self.m16AngleBtn.clicked.connect(lambda: self.updateAng(16))
        self.m17AngleBtn.clicked.connect(lambda: self.updateAng(17))
        self.m18AngleBtn.clicked.connect(lambda: self.updateAng(18))

        #Ang Finished

        #Pos Start
        self.m1PositionBtn.clicked.connect(lambda: self.updatePos(1))
        self.m2PositionBtn.clicked.connect(lambda: self.updatePos(2))
        self.m3PositionBtn.clicked.connect(lambda: self.updatePos(3))
        self.m4PositionBtn.clicked.connect(lambda: self.updatePos(4))
        self.m5PositionBtn.clicked.connect(lambda: self.updatePos(5))
        self.m6PositionBtn.clicked.connect(lambda: self.updatePos(6))
        self.m7PositionBtn.clicked.connect(lambda: self.updatePos(7))
        self.m8PositionBtn.clicked.connect(lambda: self.updatePos(8))
        self.m9PositionBtn.clicked.connect(lambda: self.updatePos(9))
        self.m10PositionBtn.clicked.connect(lambda: self.updatePos(10))
        self.m11PositionBtn.clicked.connect(lambda: self.updatePos(11))
        self.m12PositionBtn.clicked.connect(lambda: self.updatePos(12))
        self.m13PositionBtn.clicked.connect(lambda: self.updatePos(13))
        self.m14PositionBtn.clicked.connect(lambda: self.updatePos(14))
        self.m15PositionBtn.clicked.connect(lambda: self.updatePos(15))
        self.m16PositionBtn.clicked.connect(lambda: self.updatePos(16))
        self.m17PositionBtn.clicked.connect(lambda: self.updatePos(17))
        self.m18PositionBtn.clicked.connect(lambda: self.updatePos(18))
        #Pos Finished

        #Insert Started
        self.inRecBtn.clicked.connect(self.insertRec)
        self.saveRecBtn.clicked.connect(self.saveRec)
        self.newRecBtn.clicked.connect(self.newRec)
        #Insert Finshed

        #MyCode Finish
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def insertRec(self):
        rec = []
        '''
        for cnt in range(len(mm)):
            try:
                recTup = (mm[cnt].get_servo_angle(), mm[cnt].get_servo_position() )
            except:
                recTup = ("None", "None")
            rec.append(recTup)
        '''
        try:
            recTup = ("1", str(motors.motors[0].get_servo_position()))
        except:
            recTup = ("1", "None")
        rec.append(recTup)

        try:
            recTup = ("2", str(motors.motors[1].get_servo_position()))
        except:
            recTup = ("2", "None")
        rec.append(recTup)

        try:
            recTup = ("3", str(motors.motors[2].get_servo_position()))
        except:
            recTup = ("3", "None")
        rec.append(recTup)

        try:
            recTup = ("4", str(motors.motors[3].get_servo_position()))
        except:
            recTup = ("4", "None")
        rec.append(recTup)

        try:
            recTup = ("5", str(motors.motors[4].get_servo_position()))
        except:
            recTup = ("5", "None")
        rec.append(recTup)

        try:
            recTup = ("6", str(motors.motors[5].get_servo_position()))
        except:
            recTup = ("6", "None")
        rec.append(recTup)

        try:
            recTup = ("7", str(motors.motors[6].get_servo_position()))
        except:
            recTup = ("7", "None")
        rec.append(recTup)

        try:
            recTup = ("8", str(motors.motors[7].get_servo_position()))
        except:
            recTup = ("8", "None")
        rec.append(recTup)

        try:
            recTup = ("9", str(motors.motors[8].get_servo_position()))
        except:
            recTup = ("9", "None")
        rec.append(recTup)

        try:
            recTup = ("10", str(motors.motors[9].get_servo_position()))
        except:
            recTup = ("10", "None")
        rec.append(recTup)

        try:
            recTup = ("11", str(motors.motors[10].get_servo_position()))
        except:
            recTup = ("11", "None")
        rec.append(recTup)

        try:
            recTup = ("12", str(motors.motors[11].get_servo_position()))
        except:
            recTup = ("12", "None")
        rec.append(recTup)

        try:
            recTup = ("13", str(motors.motors[12].get_servo_position()))
        except:
            recTup = ("13", "None")
        rec.append(recTup)

        try:
            recTup = ("14", str(motors.motors[13].get_servo_position()))
        except:
            recTup = ("14", "None")
        rec.append(recTup)

        try:
            recTup = ("15", str(motors.motors[14].get_servo_position()))
        except:
            recTup = ("15", "None")
        rec.append(recTup)

        try:
            recTup = ("16", str(motors.motors[15].get_servo_position()))
        except:
            recTup = ("16", "None")
        rec.append(recTup)

        try:
            recTup = ("17", str(motors.motors[16].get_servo_position()))
        except:
            recTup = ("17", "None")
        rec.append(recTup)

        try:
            recTup = ("18", str(motors.motors[17].get_servo_position()))
        except:
            recTup = ("18", "None")
        rec.append(recTup)

        self.recs.append(rec)
        recNum = int(self.recNumLabel.text())
        self.recNumLabel.setText(str(recNum + 1))
        print(self.recs)

    def newRec(self):
        del(self.recs[:])
        self.recNumLabel.setText('0')

    def saveRec(self):
        fileName = self.recNameInput.text()
        fileName = "Records/" + fileName + ".txt"
        file = open(fileName, 'a')
        for rec in self.recs:
            file.write(str(rec) + '\n')
        file.close()


    def updateThread(self):
        while(True):
            self.updateMotors()
            time.sleep(1)

    def torquesOn(self):
        try:
            for motor in motors.motors:
                motor.torque_on()
            print("Motors Torque on")
        except:
            print("Torque on err")

    def updateMotors(self):
        #motor 1
        try:
            self.m1Ang.setText(str(motors.motors[0].get_servo_angle()))
            self.m1Pos.setText(str(motors.motors[0].get_servo_position()))
            self.m1AngNum.setText(str(motors.motors[0].get_servo_angle()))
            self.m1PosNum.setText(str(motors.motors[0].get_servo_position()))
            self.m1AngDial.setValue(int(motors.motors[0].get_servo_angle()))
            self.m1PosDial.setValue(motors.motors[0].get_servo_position())
            self.m1TorqueNum.setText(str(motors.motors[0].get_torque_state()))
            self.m1TempNum.setText(str(motors.motors[0].get_servo_temperature()))
            self.m1ErrNum.setText(str(motors.motors[0].get_servo_status()))
        except:
            print("AN on motor 1")

        #motor2
        try:
            self.m2Ang.setText(str(motors.motors[1].get_servo_angle()))
            self.m2Pos.setText(str(motors.motors[1].get_servo_position()))
            self.m2AngNum.setText(str(motors.motors[1].get_servo_angle()))
            self.m2PosNum.setText(str(motors.motors[1].get_servo_position()))
            self.m2AngDial.setValue(int(motors.motors[1].get_servo_angle()))
            self.m2PosDial.setValue(motors.motors[1].get_servo_position())
            self.m2TorqueNum.setText(str(motors.motors[1].get_torque_state()))
            self.m2TempNum.setText(str(motors.motors[1].get_servo_temperature()))
            self.m2ErrNum.setText(str(motors.motors[1].get_servo_status()))
        except:
            print("AN on motor 2")

        #motor3
        try:
            self.m3Ang.setText(str(motors.motors[2].get_servo_angle()))
            self.m3Pos.setText(str(motors.motors[2].get_servo_position()))
            self.m3AngNum.setText(str(motors.motors[2].get_servo_angle()))
            self.m3PosNum.setText(str(motors.motors[2].get_servo_position()))
            self.m3AngDial.setValue(int(motors.motors[2].get_servo_angle()))
            self.m3PosDial.setValue(motors.motors[2].get_servo_position())
            self.m3TorqueNum.setText(str(motors.motors[2].get_torque_state()))
            self.m3TempNum.setText(str(motors.motors[2].get_servo_temperature()))
            self.m3ErrNum.setText(str(motors.motors[2].get_servo_status()))
        except:
            print("AN on motor 3")

        #motor 4
        try:
            self.m4Ang.setText(str(motors.motors[3].get_servo_angle()))
            self.m4Pos.setText(str(motors.motors[3].get_servo_position()))
            self.m4AngNum.setText(str(motors.motors[3].get_servo_angle()))
            self.m4PosNum.setText(str(motors.motors[3].get_servo_position()))
            self.m4AngDial.setValue(int(motors.motors[3].get_servo_angle()))
            self.m4PosDial.setValue(motors.motors[3].get_servo_position())
            self.m4TorqueNum.setText(str(motors.motors[3].get_torque_state()))
            self.m4TempNum.setText(str(motors.motors[3].get_servo_temperature()))
            self.m4ErrNum.setText(str(motors.motors[3].get_servo_status()))
        except:
            print("AN on motor 4")

        #motor5
        try:
            self.m5Ang.setText(str(motors.motors[4].get_servo_angle()))
            self.m5Pos.setText(str(motors.motors[4].get_servo_position()))
            self.m5AngNum.setText(str(motors.motors[4].get_servo_angle()))
            self.m5PosNum.setText(str(motors.motors[4].get_servo_position()))
            self.m5AngDial.setValue(int(motors.motors[4].get_servo_angle()))
            self.m5PosDial.setValue(motors.motors[4].get_servo_position())
            self.m5TorqueNum.setText(str(motors.motors[4].get_torque_state()))
            self.m5TempNum.setText(str(motors.motors[4].get_servo_temperature()))
            self.m5ErrNum.setText(str(motors.motors[4].get_servo_status()))
        except:
            print("AN on motor 5")

        #motor6
        try:
            self.m6Ang.setText(str(motors.motors[5].get_servo_angle()))
            self.m6Pos.setText(str(motors.motors[5].get_servo_position()))
            self.m6AngNum.setText(str(motors.motors[5].get_servo_angle()))
            self.m6PosNum.setText(str(motors.motors[5].get_servo_position()))
            self.m6AngDial.setValue(int(motors.motors[5].get_servo_angle()))
            self.m6PosDial.setValue(motors.motors[5].get_servo_position())
            self.m6TorqueNum.setText(str(motors.motors[5].get_torque_state()))
            self.m6TempNum.setText(str(motors.motors[5].get_servo_temperature()))
            self.m6ErrNum.setText(str(motors.motors[5].get_servo_status()))
        except:
            print("AN on motor 6")

        #motor 7
        try:
            self.m7Ang.setText(str(motors.motors[6].get_servo_angle()))
            self.m7Pos.setText(str(motors.motors[6].get_servo_position()))
            self.m7AngNum.setText(str(motors.motors[6].get_servo_angle()))
            self.m7PosNum.setText(str(motors.motors[6].get_servo_position()))
            self.m7AngDial.setValue(int(motors.motors[6].get_servo_angle()))
            self.m7PosDial.setValue(motors.motors[6].get_servo_position())
            self.m7TorqueNum.setText(str(motors.motors[6].get_torque_state()))
            self.m7TempNum.setText(str(motors.motors[6].get_servo_temperature()))
            self.m7ErrNum.setText(str(motors.motors[6].get_servo_status()))
        except:
            print("AN on motor 7")

        #motor8
        try:
            self.m8Ang.setText(str(motors.motors[7].get_servo_angle()))
            self.m8Pos.setText(str(motors.motors[7].get_servo_position()))
            self.m8AngNum.setText(str(motors.motors[7].get_servo_angle()))
            self.m8PosNum.setText(str(motors.motors[7].get_servo_position()))
            self.m8AngDial.setValue(int(motors.motors[7].get_servo_angle()))
            self.m8PosDial.setValue(motors.motors[7].get_servo_position())
            self.m8TorqueNum.setText(str(motors.motors[7].get_torque_state()))
            self.m8TempNum.setText(str(motors.motors[7].get_servo_temperature()))
            self.m8ErrNum.setText(str(motors.motors[7].get_servo_status()))
        except:
            print("AN on motor 8")

        #motor9
        try:
            self.m9Ang.setText(str(motors.motors[8].get_servo_angle()))
            self.m9Pos.setText(str(motors.motors[8].get_servo_position()))
            self.m9AngNum.setText(str(motors.motors[8].get_servo_angle()))
            self.m9PosNum.setText(str(motors.motors[8].get_servo_position()))
            self.m9AngDial.setValue(int(motors.motors[8].get_servo_angle()))
            self.m9PosDial.setValue(motors.motors[8].get_servo_position())
            self.m9TorqueNum.setText(str(motors.motors[8].get_torque_state()))
            self.m9TempNum.setText(str(motors.motors[8].get_servo_temperature()))
            self.m9ErrNum.setText(str(motors.motors[8].get_servo_status()))
        except:
            print("AN on motor 9")

        #motor 10
        try:
            self.m10Ang.setText(str(motors.motors[9].get_servo_angle()))
            self.m10Pos.setText(str(motors.motors[9].get_servo_position()))
            self.m10AngNum.setText(str(motors.motors[9].get_servo_angle()))
            self.m10PosNum.setText(str(motors.motors[9].get_servo_position()))
            self.m10AngDial.setValue(int(motors.motors[9].get_servo_angle()))
            self.m10PosDial.setValue(motors.motors[9].get_servo_position())
            self.m10TorqueNum.setText(str(motors.motors[9].get_torque_state()))
            self.m10TempNum.setText(str(motors.motors[9].get_servo_temperature()))
            self.m10ErrNum.setText(str(motors.motors[9].get_servo_status()))
        except:
            print("AN on motor 10")

        #motor 11
        try:
            self.m11Ang.setText(str(motors.motors[10].get_servo_angle()))
            self.m11Pos.setText(str(motors.motors[10].get_servo_position()))
            self.m11AngNum.setText(str(motors.motors[10].get_servo_angle()))
            self.m11PosNum.setText(str(motors.motors[10].get_servo_position()))
            self.m11AngDial.setValue(int(motors.motors[10].get_servo_angle()))
            self.m11PosDial.setValue(motors.motors[10].get_servo_position())
            self.m11TorqueNum.setText(str(motors.motors[10].get_torque_state()))
            self.m11TempNum.setText(str(motors.motors[10].get_servo_temperature()))
            self.m11ErrNum.setText(str(motors.motors[10].get_servo_status()))
        except:
            print("AN on motor 11")

        #motor 12
        try:
            self.m12Ang.setText(str(motors.motors[11].get_servo_angle()))
            self.m12Pos.setText(str(motors.motors[11].get_servo_position()))
            self.m12AngNum.setText(str(motors.motors[11].get_servo_angle()))
            self.m12PosNum.setText(str(motors.motors[11].get_servo_position()))
            self.m12AngDial.setValue(int(motors.motors[11].get_servo_angle()))
            self.m12PosDial.setValue(motors.motors[11].get_servo_position())
            self.m12TorqueNum.setText(str(motors.motors[11].get_torque_state()))
            self.m12TempNum.setText(str(motors.motors[11].get_servo_temperature()))
            self.m12ErrNum.setText(str(motors.motors[11].get_servo_status()))
        except:
            print("AN on motor 12")

        #motor 13
        try:
            self.m13Ang.setText(str(motors.motors[12].get_servo_angle()))
            self.m13Pos.setText(str(motors.motors[12].get_servo_position()))
            self.m13AngNum.setText(str(motors.motors[12].get_servo_angle()))
            self.m13PosNum.setText(str(motors.motors[12].get_servo_position()))
            self.m13AngDial.setValue(int(motors.motors[12].get_servo_angle()))
            self.m13PosDial.setValue(motors.motors[12].get_servo_position())
            self.m13TorqueNum.setText(str(motors.motors[12].get_torque_state()))
            self.m13TempNum.setText(str(motors.motors[12].get_servo_temperature()))
            self.m13ErrNum.setText(str(motors.motors[12].get_servo_status()))
        except:
            print("AN on motor 13")

        #motor 14
        try:
            self.m14Ang.setText(str(motors.motors[13].get_servo_angle()))
            self.m14Pos.setText(str(motors.motors[13].get_servo_position()))
            self.m14AngNum.setText(str(motors.motors[13].get_servo_angle()))
            self.m14PosNum.setText(str(motors.motors[13].get_servo_position()))
            self.m14AngDial.setValue(int(motors.motors[13].get_servo_angle()))
            self.m14PosDial.setValue(motors.motors[13].get_servo_position())
            self.m14TorqueNum.setText(str(motors.motors[13].get_torque_state()))
            self.m14TempNum.setText(str(motors.motors[13].get_servo_temperature()))
            self.m14ErrNum.setText(str(motors.motors[13].get_servo_status()))
        except:
            print("AN on motor 14")

        #motor15
        try:
            self.m15Ang.setText(str(motors.motors[14].get_servo_angle()))
            self.m15Pos.setText(str(motors.motors[14].get_servo_position()))
            self.m15AngNum.setText(str(motors.motors[14].get_servo_angle()))
            self.m15PosNum.setText(str(motors.motors[14].get_servo_position()))
            self.m15AngDial.setValue(int(motors.motors[14].get_servo_angle()))
            self.m15PosDial.setValue(motors.motors[14].get_servo_position())
            self.m15TorqueNum.setText(str(motors.motors[14].get_torque_state()))
            self.m15TempNum.setText(str(motors.motors[14].get_servo_temperature()))
            self.m15ErrNum.setText(str(motors.motors[14].get_servo_status()))
        except:
            print("AN on motor 15")

        #motor 16
        try:
            self.m16Ang.setText(str(motors.motors[15].get_servo_angle()))
            self.m16Pos.setText(str(motors.motors[15].get_servo_position()))
            self.m16AngNum.setText(str(motors.motors[15].get_servo_angle()))
            self.m16PosNum.setText(str(motors.motors[15].get_servo_position()))
            self.m16AngDial.setValue(int(motors.motors[15].get_servo_angle()))
            self.m16PosDial.setValue(motors.motors[15].get_servo_position())
            self.m16TorqueNum.setText(str(motors.motors[15].get_torque_state()))
            self.m16TempNum.setText(str(motors.motors[15].get_servo_temperature()))
            self.m16ErrNum.setText(str(motors.motors[15].get_servo_status()))
        except:
            print("AN on motor 16")

        #motor 17
        try:
            self.m17Ang.setText(str(motors.motors[16].get_servo_angle()))
            self.m17Pos.setText(str(motors.motors[16].get_servo_position()))
            self.m17AngNum.setText(str(motors.motors[16].get_servo_angle()))
            self.m17PosNum.setText(str(motors.motors[16].get_servo_position()))
            self.m17AngDial.setValue(int(motors.motors[16].get_servo_angle()))
            self.m17PosDial.setValue(motors.motors[16].get_servo_position())
            self.m17TorqueNum.setText(str(motors.motors[16].get_torque_state()))
            self.m17TempNum.setText(str(motors.motors[16].get_servo_temperature()))
            self.m17ErrNum.setText(str(motors.motors[16].get_servo_status()))
        except:
            print("AN on motor 17")

        #motor 18
        try:
            self.m18Ang.setText(str(motors.motors[17].get_servo_angle()))
            self.m18Pos.setText(str(motors.motors[17].get_servo_position()))
            self.m18AngNum.setText(str(motors.motors[17].get_servo_angle()))
            self.m18PosNum.setText(str(motors.motors[17].get_servo_position()))
            self.m18AngDial.setValue(int(motors.motors[17].get_servo_angle()))
            self.m18PosDial.setValue(motors.motors[17].get_servo_position())
            self.m18TorqueNum.setText(str(motors.motors[17].get_torque_state()))
            self.m18TempNum.setText(str(motors.motors[17].get_servo_temperature()))
            self.m18ErrNum.setText(str(motors.motors[17].get_servo_status()))
        except:
            print("AN on motor 18")

    def updateAngDial(self, mNum):
        if(mNum == 1):
            try:
                self.m1AngNum.setText(str(self.m1AngDial.value()))
                goalTime = self.m1GoalTSpin.value()
                goalAngle = self.m1AngDial.value()
                motors.motors[0].set_servo_angle(goalAngle, goalTime, 0x04 )
            except:
                print("Update Ang Dial m1")

        if(mNum == 2):
            try:
                self.m2AngNum.setText(str(self.m2AngDial.value()))
                goalTime = self.m2GoalTSpin.value()
                goalAngle = self.m2AngDial.value()
                motors.motors[1].set_servo_angle(goalAngle, goalTime, 0x04 )
            except:
                print("Update Ang Dial m2")

        if(mNum == 3):
            try:
                self.m3AngNum.setText(str(self.m3AngDial.value()))
                goalTime = self.m3GoalTSpin.value()
                goalAngle = self.m3AngDial.value()
                motors.motors[2].set_servo_angle(goalAngle, goalTime, 0x04 )
            except:
                print("Update Ang Dial m3")

        if(mNum == 4):
            try:
                self.m4AngNum.setText(str(self.m4AngDial.value()))
                goalTime = self.m4GoalTSpin.value()
                goalAngle = self.m4AngDial.value()
                motors.motors[3].set_servo_angle(goalAngle, goalTime, 0x04 )
            except:
                print("Update Ang Dial m4")

        if(mNum == 5):
            try:
                self.m5AngNum.setText(str(self.m5AngDial.value()))
                goalTime = self.m5GoalTSpin.value()
                goalAngle = self.m5AngDial.value()
                motors.motors[4].set_servo_angle(goalAngle, goalTime, 0x04 )
            except:
                print("Update Ang Dial m5")

        if(mNum == 6):
            try:
                self.m6AngNum.setText(str(self.m6AngDial.value()))
                goalTime = self.m6GoalTSpin.value()
                goalAngle = self.m6AngDial.value()
                motors.motors[5].set_servo_angle(goalAngle, goalTime, 0x04 )
            except:
                print("Update Ang Dial m6")

        if(mNum == 7):
            try:
                self.m7AngNum.setText(str(self.m7AngDial.value()))
                goalTime = self.m7GoalTSpin.value()
                goalAngle = self.m7AngDial.value()
                motors.motors[6].set_servo_angle(goalAngle, goalTime, 0x04 )
            except:
                print("Update Ang Dial m7")

        if(mNum == 8):
            try:
                self.m8AngNum.setText(str(self.m8AngDial.value()))
                goalTime = self.m8GoalTSpin.value()
                goalAngle = self.m8AngDial.value()
                motors.motors[7].set_servo_angle(goalAngle, goalTime, 0x04 )
            except:
                print("Update Ang Dial m8")

        if(mNum == 9):
            try:
                self.m9AngNum.setText(str(self.m9AngDial.value()))
                goalTime = self.m9GoalTSpin.value()
                goalAngle = self.m9AngDial.value()
                motors.motors[8].set_servo_angle(goalAngle, goalTime, 0x04 )
            except:
                print("Update Ang Dial m9")

        if(mNum == 10):
            try:
                self.m10AngNum.setText(str(self.m10AngDial.value()))
                goalTime = self.m10GoalTSpin.value()
                goalAngle = self.m10AngDial.value()
                motors.motors[9].set_servo_angle(goalAngle, goalTime, 0x04 )
            except:
                print("Update Ang Dial m10")

        if(mNum == 11):
            try:
                self.m11AngNum.setText(str(self.m11AngDial.value()))
                goalTime = self.m11GoalTSpin.value()
                goalAngle = self.m11AngDial.value()
                motors.motors[10].set_servo_angle(goalAngle, goalTime, 0x04 )
            except:
                print("Update Ang Dial m11")

        if(mNum == 12):
            try:
                self.m12AngNum.setText(str(self.m12AngDial.value()))
                goalTime = self.m12GoalTSpin.value()
                goalAngle = self.m12AngDial.value()
                motors.motors[11].set_servo_angle(goalAngle, goalTime, 0x04 )
            except:
                print("Update Ang Dial m12")

        if(mNum == 13):
            try:
                self.m13AngNum.setText(str(self.m13AngDial.value()))
                goalTime = self.m13GoalTSpin.value()
                goalAngle = self.m13AngDial.value()
                motors.motors[12].set_servo_angle(goalAngle, goalTime, 0x04 )
            except:
                print("Update Ang Dial m13")

        if(mNum == 14):
            try:
                self.m14AngNum.setText(str(self.m14AngDial.value()))
                goalTime = self.m14GoalTSpin.value()
                goalAngle = self.m14AngDial.value()
                motors.motors[13].set_servo_angle(goalAngle, goalTime, 0x04 )
            except:
                print("Update Ang Dial m14")

        if(mNum == 15):
            try:
                self.m15AngNum.setText(str(self.m15AngDial.value()))
                goalTime = self.m15GoalTSpin.value()
                goalAngle = self.m15AngDial.value()
                motors.motors[14].set_servo_angle(goalAngle, goalTime, 0x04 )
            except:
                print("Update Ang Dial m15")

        if(mNum == 16):
            try:
                self.m16AngNum.setText(str(self.m16AngDial.value()))
                goalTime = self.m16GoalTSpin.value()
                goalAngle = self.m16AngDial.value()
                motors.motors[15].set_servo_angle(goalAngle, goalTime, 0x04 )
            except:
                print("Update Ang Dial m16")

        if(mNum == 17):
            try:
                self.m17AngNum.setText(str(self.m17AngDial.value()))
                goalTime = self.m17GoalTSpin.value()
                goalAngle = self.m17AngDial.value()
                motors.motors[16].set_servo_angle(goalAngle, goalTime, 0x04 )
            except:
                print("Update Ang Dial m17")

        if(mNum == 18):
            try:
                self.m18AngNum.setText(str(self.m18AngDial.value()))
                goalTime = self.m18GoalTSpin.value()
                goalAngle = self.m18AngDial.value()
                motors.motors[17].set_servo_angle(goalAngle, goalTime, 0x04 )
            except:
                print("Update Ang Dial m18")

    def updateAng(self, mNum):
        if(mNum == 1):
            try:
                goalTime = self.m1GoalTSpin.value()
                goalAngle = self.m1AngleSpin.value()
                motors.motors[0].set_servo_angle(goalAngle, goalTime, 0x04 )
            except:
                print("Update Ang m1")

        if(mNum == 2):
            try:
                goalTime = self.m2GoalTSpin.value()
                goalAngle = self.m2AngleSpin.value()
                motors.motors[1].set_servo_angle(goalAngle, goalTime, 0x04 )
            except:
                print("Update Ang m2")

        if(mNum == 3):
            try:
                goalTime = self.m3GoalTSpin.value()
                goalAngle = self.m3AngleSpin.value()
                motors.motors[2].set_servo_angle(goalAngle, goalTime, 0x04 )
            except:
                print("Update Ang m3")

        if(mNum == 4):
            try:
                goalTime = self.m4GoalTSpin.value()
                goalAngle = self.m4AngleSpin.value()
                motors.motors[3].set_servo_angle(goalAngle, goalTime, 0x04 )
            except:
                print("Update Ang m4")

        if(mNum == 5):
            try:
                goalTime = self.m5GoalTSpin.value()
                goalAngle = self.m5AngleSpin.value()
                motors.motors[4].set_servo_angle(goalAngle, goalTime, 0x04 )
            except:
                print("Update Ang m5")

        if(mNum == 6):
            try:
                goalTime = self.m6GoalTSpin.value()
                goalAngle = self.m6AngleSpin.value()
                motors.motors[5].set_servo_angle(goalAngle, goalTime, 0x04 )
            except:
                print("Update Ang m6")

        if(mNum == 7):
            try:
                goalTime = self.m7GoalTSpin.value()
                goalAngle = self.m7AngleSpin.value()
                motors.motors[6].set_servo_angle(goalAngle, goalTime, 0x04 )
            except:
                print("Update Ang m7")

        if(mNum == 8):
            try:
                goalTime = self.m8GoalTSpin.value()
                goalAngle = self.m8AngleSpin.value()
                motors.motors[7].set_servo_angle(goalAngle, goalTime, 0x04 )
            except:
                print("Update Ang m8")

        if(mNum == 9):
            try:
                goalTime = self.m9GoalTSpin.value()
                goalAngle = self.m9AngleSpin.value()
                motors.motors[8].set_servo_angle(goalAngle, goalTime, 0x04 )
            except:
                print("Update Ang m9")

        if(mNum == 10):
            try:
                goalTime = self.m10GoalTSpin.value()
                goalAngle = self.m10AngleSpin.value()
                motors.motors[9].set_servo_angle(goalAngle, goalTime, 0x04 )
            except:
                print("Update Ang m10")

        if(mNum == 11):
            try:
                goalTime = self.m11GoalTSpin.value()
                goalAngle = self.m11AngleSpin.value()
                motors.motors[10].set_servo_angle(goalAngle, goalTime, 0x04 )
            except:
                print("Update Ang m11")

        if(mNum == 12):
            try:
                goalTime = self.m12GoalTSpin.value()
                goalAngle = self.m12AngleSpin.value()
                motors.motors[11].set_servo_angle(goalAngle, goalTime, 0x04 )
            except:
                print("Update Ang m12")

        if(mNum == 13):
            try:
                goalTime = self.m13GoalTSpin.value()
                goalAngle = self.m13AngleSpin.value()
                motors.motors[12].set_servo_angle(goalAngle, goalTime, 0x04 )
            except:
                print("Update Ang m13")

        if(mNum == 14):
            try:
                goalTime = self.m14GoalTSpin.value()
                goalAngle = self.m14AngleSpin.value()
                motors.motors[13].set_servo_angle(goalAngle, goalTime, 0x04 )
            except:
                print("Update Ang m14")

        if(mNum == 15):
            try:
                goalTime = self.m15GoalTSpin.value()
                goalAngle = self.m15AngleSpin.value()
                motors.motors[14].set_servo_angle(goalAngle, goalTime, 0x04 )
            except:
                print("Update Ang m15")

        if(mNum == 16):
            try:
                goalTime = self.m16GoalTSpin.value()
                goalAngle = self.m16AngleSpin.value()
                motors.motors[15].set_servo_angle(goalAngle, goalTime, 0x04 )
            except:
                print("Update Ang m16")

        if(mNum == 17):
            try:
                goalTime = self.m17GoalTSpin.value()
                goalAngle = self.m17AngleSpin.value()
                motors.motors[16].set_servo_angle(goalAngle, goalTime, 0x04 )
            except:
                print("Update Ang m17")

        if(mNum == 18):
            try:
                goalTime = self.m18GoalTSpin.value()
                goalAngle = self.m18AngleSpin.value()
                motors.motors[17].set_servo_angle(goalAngle, goalTime, 0x04 )
            except:
                print("Update Ang m18")

    def updatePosDial(self, mNum):
        if(mNum == 1):
            try:
                self.m1PosNum.setText(str(self.m1PosDial.value()))
                goalTime = self.m1GoalTSpin.value()
                goalPos = self.m1PosDial.value()
                motors.motors[0].set_servo_position(goalPos, goalTime, 0x04 )
            except:
                print("Update Pos Dial m1")

        if(mNum == 2):
            try:
                self.m2PosNum.setText(str(self.m2PosDial.value()))
                goalTime = self.m2GoalTSpin.value()
                goalPos = self.m2PosDial.value()
                motors.motors[1].set_servo_position(goalPos, goalTime, 0x04 )
            except:
                print("Update Pos Dial m2")

        if(mNum == 3):
            try:
                self.m3PosNum.setText(str(self.m3PosDial.value()))
                goalTime = self.m3GoalTSpin.value()
                goalPos = self.m3PosDial.value()
                motors.motors[2].set_servo_position(goalPos, goalTime, 0x04 )
            except:
                print("Update Pos Dial m3")

        if(mNum == 4):
            try:
                self.m4PosNum.setText(str(self.m4PosDial.value()))
                goalTime = self.m4GoalTSpin.value()
                goalPos = self.m4PosDial.value()
                motors.motors[3].set_servo_position(goalPos, goalTime, 0x04 )
            except:
                print("Update Pos Dial m4")

        if(mNum == 5):
            try:
                self.m5PosNum.setText(str(self.m5PosDial.value()))
                goalTime = self.m5GoalTSpin.value()
                goalPos = self.m5PosDial.value()
                motors.motors[4].set_servo_position(goalPos, goalTime, 0x04 )
            except:
                print("Update Pos Dial m5")

        if(mNum == 6):
            try:
                self.m6PosNum.setText(str(self.m6PosDial.value()))
                goalTime = self.m6GoalTSpin.value()
                goalPos = self.m6PosDial.value()
                motors.motors[5].set_servo_position(goalPos, goalTime, 0x04 )
            except:
                print("Update Pos Dial m6")

        if(mNum == 7):
            try:
                self.m7PosNum.setText(str(self.m7PosDial.value()))
                goalTime = self.m7GoalTSpin.value()
                goalPos = self.m7PosDial.value()
                motors.motors[6].set_servo_position(goalPos, goalTime, 0x04 )
            except:
                print("Update Pos Dial m7")

        if(mNum == 8):
            try:
                self.m8PosNum.setText(str(self.m8PosDial.value()))
                goalTime = self.m8GoalTSpin.value()
                goalPos = self.m8PosDial.value()
                motors.motors[7].set_servo_position(goalPos, goalTime, 0x04 )
            except:
                print("Update Pos Dial m8")

        if(mNum == 9):
            try:
                self.m9PosNum.setText(str(self.m9PosDial.value()))
                goalTime = self.m9GoalTSpin.value()
                goalPos = self.m9PosDial.value()
                motors.motors[8].set_servo_position(goalPos, goalTime, 0x04 )
            except:
                print("Update Pos Dial m9")

        if(mNum == 10):
            try:
                self.m10PosNum.setText(str(self.m10PosDial.value()))
                goalTime = self.m10GoalTSpin.value()
                goalPos = self.m10PosDial.value()
                motors.motors[9].set_servo_position(goalPos, goalTime, 0x04 )
            except:
                print("Update Pos Dial m10")

        if(mNum == 11):
            try:
                self.m11PosNum.setText(str(self.m11PosDial.value()))
                goalTime = self.m11GoalTSpin.value()
                goalPos = self.m11PosDial.value()
                motors.motors[10].set_servo_position(goalPos, goalTime, 0x04 )
            except:
                print("Update Pos Dial m11")

        if(mNum == 12):
            try:
                self.m12PosNum.setText(str(self.m12PosDial.value()))
                goalTime = self.m12GoalTSpin.value()
                goalPos = self.m12PosDial.value()
                motors.motors[11].set_servo_position(goalPos, goalTime, 0x04 )
            except:
                print("Update Pos Dial m12")

        if(mNum == 13):
            try:
                self.m13PosNum.setText(str(self.m13PosDial.value()))
                goalTime = self.m13GoalTSpin.value()
                goalPos = self.m13PosDial.value()
                motors.motors[12].set_servo_position(goalPos, goalTime, 0x04 )
            except:
                print("Update Pos Dial m13")

        if(mNum == 14):
            try:
                self.m14PosNum.setText(str(self.m14PosDial.value()))
                goalTime = self.m14GoalTSpin.value()
                goalPos = self.m14PosDial.value()
                motors.motors[13].set_servo_position(goalPos, goalTime, 0x04 )
            except:
                print("Update Pos Dial m14")

        if(mNum == 15):
            try:
                self.m15PosNum.setText(str(self.m15PosDial.value()))
                goalTime = self.m15GoalTSpin.value()
                goalPos = self.m15PosDial.value()
                motors.motors[14].set_servo_position(goalPos, goalTime, 0x04 )
            except:
                print("Update Pos Dial m15")

        if(mNum == 16):
            try:
                self.m16PosNum.setText(str(self.m16PosDial.value()))
                goalTime = self.m16GoalTSpin.value()
                goalPos = self.m16PosDial.value()
                motors.motors[15].set_servo_position(goalPos, goalTime, 0x04 )
            except:
                print("Update Pos Dial m16")

        if(mNum == 17):
            try:
                self.m17PosNum.setText(str(self.m17PosDial.value()))
                goalTime = self.m17GoalTSpin.value()
                goalPosition = self.m17PosDial.value()
                motors.motors[16].set_servo_position(goalPos, goalTime, 0x04 )
            except:
                print("Update Pos Dial m17")

        if(mNum == 18):
            try:
                self.m18PosNum.setText(str(self.m18PosDial.value()))
                goalTime = self.m18GoalTSpin.value()
                goalPos = self.m18PosDial.value()
                motors.motors[17].set_servo_position(goalPos, goalTime, 0x04 )
            except:
                print("Update Pos Dial m18")

    def updatePos(self, mNum):
        if(mNum == 1):
            try:
                goalTime = self.m1GoalTSpin.value()
                goalPos = self.m1PositionSpin.value()
                motors.motors[0].set_servo_position(goalPos, goalTime, 0x04 )
            except:
                print("Update Pos m1")

        if(mNum == 2):
            try:
                goalTime = self.m2GoalTSpin.value()
                goalPos = self.m2PositionSpin.value()
                motors.motors[1].set_servo_position(goalPos, goalTime, 0x04 )
            except:
                print("Update Pos m2")

        if(mNum == 3):
            try:
                goalTime = self.m3GoalTSpin.value()
                goalPos = self.m3PositionSpin.value()
                motors.motors[2].set_servo_position(goalPos, goalTime, 0x04 )
            except:
                print("Update Pos m3")

        if(mNum == 4):
            try:
                goalTime = self.m4GoalTSpin.value()
                goalPos = self.m4PositionSpin.value()
                motors.motors[3].set_servo_position(goalPos, goalTime, 0x04 )
            except:
                print("Update Pos m4")

        if(mNum == 5):
            try:
                goalTime = self.m5GoalTSpin.value()
                goalPos = self.m5PositionSpin.value()
                motors.motors[4].set_servo_position(goalPos, goalTime, 0x04 )
            except:
                print("Update Pos m5")

        if(mNum == 6):
            try:
                goalTime = self.m6GoalTSpin.value()
                goalPos = self.m6PositionSpin.value()
                motors.motors[5].set_servo_position(goalPos, goalTime, 0x04 )
            except:
                print("Update Pos m6")

        if(mNum == 7):
            try:
                goalTime = self.m7GoalTSpin.value()
                goalPos = self.m7PositionSpin.value()
                motors.motors[6].set_servo_position(goalPos, goalTime, 0x04 )
            except:
                print("Update Pos m7")

        if(mNum == 8):
            try:
                goalTime = self.m8GoalTSpin.value()
                goalPos = self.m8PositionSpin.value()
                motors.motors[7].set_servo_position(goalPos, goalTime, 0x04 )
            except:
                print("Update Pos m8")

        if(mNum == 9):
            try:
                goalTime = self.m9GoalTSpin.value()
                goalPos = self.m9PositionSpin.value()
                motors.motors[8].set_servo_position(goalPos, goalTime, 0x04 )
            except:
                print("Update Pos m9")

        if(mNum == 10):
            try:
                goalTime = self.m10GoalTSpin.value()
                goalPos = self.m10PositionSpin.value()
                motors.motors[9].set_servo_position(goalPos, goalTime, 0x04 )
            except:
                print("Update Pos m10")

        if(mNum == 11):
            try:
                goalTime = self.m11GoalTSpin.value()
                goalPos = self.m11PositionSpin.value()
                motors.motors[10].set_servo_position(goalPos, goalTime, 0x04 )
            except:
                print("Update Pos m11")

        if(mNum == 12):
            try:
                goalTime = self.m12GoalTSpin.value()
                goalPos = self.m12PositionSpin.value()
                motors.motors[11].set_servo_position(goalPos, goalTime, 0x04 )
            except:
                print("Update Pos m12")

        if(mNum == 13):
            try:
                goalTime = self.m13GoalTSpin.value()
                goalPos = self.m13PositionSpin.value()
                motors.motors[12].set_servo_position(goalPos, goalTime, 0x04 )
            except:
                print("Update Pos m13")

        if(mNum == 14):
            try:
                goalTime = self.m14GoalTSpin.value()
                goalPos = self.m14PositionSpin.value()
                motors.motors[13].set_servo_position(goalPos, goalTime, 0x04 )
            except:
                print("Update Pos m14")

        if(mNum == 15):
            try:
                goalTime = self.m15GoalTSpin.value()
                goalPos = self.m15PositionSpin.value()
                motors.motors[14].set_servo_position(goalPos, goalTime, 0x04 )
            except:
                print("Update Pos m15")

        if(mNum == 16):
            try:
                goalTime = self.m16GoalTSpin.value()
                goalPos = self.m16PositionSpin.value()
                motors.motors[15].set_servo_position(goalPos, goalTime, 0x04 )
            except:
                print("Update Pos m16")

        if(mNum == 17):
            try:
                goalTime = self.m17GoalTSpin.value()
                goalPosition = self.m17PositionSpin.value()
                motors.motors[16].set_servo_position(goalPos, goalTime, 0x04 )
            except:
                print("Update Pos m17")

        if(mNum == 18):
            try:
                goalTime = self.m18GoalTSpin.value()
                goalPos = self.m18PositionSpin.value()
                motors.motors[17].set_servo_position(goalPos, goalTime, 0x04 )
            except:
                print("Update Pos m18")

    def changeValDial(self):
        try:
            #self.m1PosNum.setText(str(self.m1PosDial.value()))
            self.m1PosNum.setText(str(motors.motors[0].get_model()))
        except:
            self.m1PosNum.setText("salam")

    def forward(self):
        motorSelect = str(self.mSelect.currentText()).split(' ')
        motorSelect = int(motorSelect[1])
        #motorSelect = int(motorSelect.split(' ')[1])
        self.stackedWidget.setCurrentIndex(self.stackedWidget.currentIndex() + motorSelect)

    def backward(self):
        self.stackedWidget.setCurrentIndex(0)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "AUT-Man", None))
        self.mId.setText(_translate("MainWindow", "ID", None))
        self.mAngle.setText(_translate("MainWindow", "Angle", None))
        self.mPos.setText(_translate("MainWindow", "Position", None))
        self.m1.setText(_translate("MainWindow", "1", None))
        self.m1Ang.setText(_translate("MainWindow", "None", None))
        self.m1Pos.setText(_translate("MainWindow", "None", None))
        self.m10.setText(_translate("MainWindow", "10", None))
        self.m10Ang.setText(_translate("MainWindow", "None", None))
        self.m10Pos.setText(_translate("MainWindow", "None", None))
        self.m2.setText(_translate("MainWindow", "2", None))
        self.m2Ang.setText(_translate("MainWindow", "None", None))
        self.label_4.setText(_translate("MainWindow", "None", None))
        self.m2Pos.setText(_translate("MainWindow", "None", None))
        self.m11.setText(_translate("MainWindow", "11", None))
        self.m11Pos.setText(_translate("MainWindow", "None", None))
        self.m11Ang.setText(_translate("MainWindow", "None", None))
        self.m3Ang.setText(_translate("MainWindow", "None", None))
        self.m3Pos.setText(_translate("MainWindow", "None", None))
        self.label_8.setText(_translate("MainWindow", "None", None))
        self.m3.setText(_translate("MainWindow", "3", None))
        self.m12.setText(_translate("MainWindow", "12", None))
        self.m12Pos.setText(_translate("MainWindow", "None", None))
        self.m12Ang.setText(_translate("MainWindow", "None", None))
        self.m4Ang.setText(_translate("MainWindow", "None", None))
        self.m4Pos.setText(_translate("MainWindow", "None", None))
        self.m4.setText(_translate("MainWindow", "4", None))
        self.m13.setText(_translate("MainWindow", "13", None))
        self.m13Pos.setText(_translate("MainWindow", "None", None))
        self.m13Ang.setText(_translate("MainWindow", "None", None))
        self.m5.setText(_translate("MainWindow", "5", None))
        self.m5Ang.setText(_translate("MainWindow", "None", None))
        self.m5Pos.setText(_translate("MainWindow", "None", None))
        self.m14.setText(_translate("MainWindow", "14", None))
        self.m14Pos.setText(_translate("MainWindow", "None", None))
        self.m14Ang.setText(_translate("MainWindow", "None", None))
        self.m6.setText(_translate("MainWindow", "6", None))
        self.m6Ang.setText(_translate("MainWindow", "None", None))
        self.m6Pos.setText(_translate("MainWindow", "None", None))
        self.m15.setText(_translate("MainWindow", "15", None))
        self.m15Pos.setText(_translate("MainWindow", "None", None))
        self.m15Ang.setText(_translate("MainWindow", "None", None))
        self.m7.setText(_translate("MainWindow", "7", None))
        self.m7Ang.setText(_translate("MainWindow", "None", None))
        self.m7Pos.setText(_translate("MainWindow", "None", None))
        self.m16.setText(_translate("MainWindow", "16", None))
        self.m16Pos.setText(_translate("MainWindow", "None", None))
        self.m16Ang.setText(_translate("MainWindow", "None", None))
        self.m8.setText(_translate("MainWindow", "8", None))
        self.m8Ang.setText(_translate("MainWindow", "None", None))
        self.m8Pos.setText(_translate("MainWindow", "None", None))
        self.m17.setText(_translate("MainWindow", "17", None))
        self.m17Pos.setText(_translate("MainWindow", "None", None))
        self.m17Ang.setText(_translate("MainWindow", "None", None))
        self.recSavedLabel.setText(_translate("MainWindow", "Records saved : ", None))
        self.recNumLabel.setText(_translate("MainWindow", "0", None))
        self.mUpdateBtn.setText(_translate("MainWindow", "Update Motors", None))
        self.m9.setText(_translate("MainWindow", "9", None))
        self.m9Ang.setText(_translate("MainWindow", "None", None))
        self.m9Pos.setText(_translate("MainWindow", "None", None))
        self.m18.setText(_translate("MainWindow", "18", None))
        self.m18Pos.setText(_translate("MainWindow", "None", None))
        self.m18Ang.setText(_translate("MainWindow", "None", None))
        self.mId_2.setText(_translate("MainWindow", "ID", None))
        self.mAngle_2.setText(_translate("MainWindow", "Angle", None))
        self.mPos_2.setText(_translate("MainWindow", "Position", None))
        self.inRecBtn.setText(_translate("MainWindow", "Insert Record", None))
        self.saveRecBtn.setText(_translate("MainWindow", "save Records", None))
        self.recNameInput.setText(_translate("MainWindow", "Rec Name", None))
        self.saveStatusLabel.setText(_translate("MainWindow", "Not Saved", None))
        self.newRecBtn.setText(_translate("MainWindow", "New Record", None))
        self.mSelect.setItemText(0, _translate("MainWindow", "Motor 1", None))
        self.mSelect.setItemText(1, _translate("MainWindow", "Motor 2", None))
        self.mSelect.setItemText(2, _translate("MainWindow", "Motor 3", None))
        self.mSelect.setItemText(3, _translate("MainWindow", "Motor 4", None))
        self.mSelect.setItemText(4, _translate("MainWindow", "Motor 5", None))
        self.mSelect.setItemText(5, _translate("MainWindow", "Motor 6", None))
        self.mSelect.setItemText(6, _translate("MainWindow", "Motor 7", None))
        self.mSelect.setItemText(7, _translate("MainWindow", "Motor 8", None))
        self.mSelect.setItemText(8, _translate("MainWindow", "Motor 9", None))
        self.mSelect.setItemText(9, _translate("MainWindow", "Motor 10", None))
        self.mSelect.setItemText(10, _translate("MainWindow", "Motor 11", None))
        self.mSelect.setItemText(11, _translate("MainWindow", "Motor 12", None))
        self.mSelect.setItemText(12, _translate("MainWindow", "Motor 13", None))
        self.mSelect.setItemText(13, _translate("MainWindow", "Motor 14", None))
        self.mSelect.setItemText(14, _translate("MainWindow", "Motor 15", None))
        self.mSelect.setItemText(15, _translate("MainWindow", "Motor 16", None))
        self.mSelect.setItemText(16, _translate("MainWindow", "Motor 17", None))
        self.mSelect.setItemText(17, _translate("MainWindow", "Motor 18", None))
        self.mGoBtn.setText(_translate("MainWindow", "Go", None))
        self.m1Label.setText(_translate("MainWindow", "Motor 1", None))
        self.m1AngLabel.setText(_translate("MainWindow", "Angle", None))
        self.m1PosLabel.setText(_translate("MainWindow", "Position", None))
        self.m1TorqueLabel.setText(_translate("MainWindow", "Torque Status", None))
        self.m1TempLabel.setText(_translate("MainWindow", "Temprature", None))
        self.m1ErrLabel.setText(_translate("MainWindow", "Error", None))
        self.m1AngNum.setText(_translate("MainWindow", "None", None))
        self.m1PosNum.setText(_translate("MainWindow", "None", None))
        self.m1TorqueNum.setText(_translate("MainWindow", "None", None))
        self.m1ErrNum.setText(_translate("MainWindow", "None", None))
        self.m1TempNum.setText(_translate("MainWindow", "None", None))
        self.m1GoalTLabel.setText(_translate("MainWindow", "Goal Time", None))
        self.m1UpdateBtn.setText(_translate("MainWindow", "Update Motor", None))
        self.m1AngleLabel.setText(_translate("MainWindow", "Angle", None))
        self.m1PositionLabel.setText(_translate("MainWindow", "Position", None))
        self.m1AngleBtn.setText(_translate("MainWindow", "Go Angle", None))
        self.m1PositionBtn.setText(_translate("MainWindow", "Go Position", None))
        self.m1HomeBtn.setText(_translate("MainWindow", "Back to Home", None))
        self.m2AngLabel.setText(_translate("MainWindow", "Angle", None))
        self.m2PosLabel.setText(_translate("MainWindow", "Position", None))
        self.m2TorqueLabel.setText(_translate("MainWindow", "Torque Status", None))
        self.m2TempLabel.setText(_translate("MainWindow", "Temprature", None))
        self.m2ErrLabel.setText(_translate("MainWindow", "Error", None))
        self.m2AngNum.setText(_translate("MainWindow", "None", None))
        self.m2PosNum.setText(_translate("MainWindow", "None", None))
        self.m2TorqueNum.setText(_translate("MainWindow", "None", None))
        self.m2ErrNum.setText(_translate("MainWindow", "None", None))
        self.m2TempNum.setText(_translate("MainWindow", "None", None))
        self.m2GoalTLabel.setText(_translate("MainWindow", "Goal Time", None))
        self.m2UpdateBtn.setText(_translate("MainWindow", "Update Motor", None))
        self.m2AngleLabel.setText(_translate("MainWindow", "Angle", None))
        self.m2PositionLabel.setText(_translate("MainWindow", "Position", None))
        self.m2AngleBtn.setText(_translate("MainWindow", "Go Angle", None))
        self.m2PositionBtn.setText(_translate("MainWindow", "Go Position", None))
        self.m2HomeBtn.setText(_translate("MainWindow", "Back to Home", None))
        self.m2Label.setText(_translate("MainWindow", "Motor 2", None))
        self.m3AngLabel.setText(_translate("MainWindow", "Angle", None))
        self.m3PosLabel.setText(_translate("MainWindow", "Position", None))
        self.m3TorqueLabel.setText(_translate("MainWindow", "Torque Status", None))
        self.m3TempLabel.setText(_translate("MainWindow", "Temprature", None))
        self.m3ErrLabel.setText(_translate("MainWindow", "Error", None))
        self.m3AngNum.setText(_translate("MainWindow", "None", None))
        self.m3PosNum.setText(_translate("MainWindow", "None", None))
        self.m3TorqueNum.setText(_translate("MainWindow", "None", None))
        self.m3ErrNum.setText(_translate("MainWindow", "None", None))
        self.m3TempNum.setText(_translate("MainWindow", "None", None))
        self.m3GoalTLabel.setText(_translate("MainWindow", "Goal Time", None))
        self.m3UpdateBtn.setText(_translate("MainWindow", "Update Motor", None))
        self.m3AngleLabel.setText(_translate("MainWindow", "Angle", None))
        self.m3PositionLabel.setText(_translate("MainWindow", "Position", None))
        self.m3AngleBtn.setText(_translate("MainWindow", "Go Angle", None))
        self.m3PositionBtn.setText(_translate("MainWindow", "Go Position", None))
        self.m3HomeBtn.setText(_translate("MainWindow", "Back to Home", None))
        self.m3Label.setText(_translate("MainWindow", "Motor 3", None))
        self.m4AngLabel.setText(_translate("MainWindow", "Angle", None))
        self.m4PosLabel.setText(_translate("MainWindow", "Position", None))
        self.m4TorqueLabel.setText(_translate("MainWindow", "Torque Status", None))
        self.m4TempLabel.setText(_translate("MainWindow", "Temprature", None))
        self.m4ErrLabel.setText(_translate("MainWindow", "Error", None))
        self.m4AngNum.setText(_translate("MainWindow", "None", None))
        self.m4PosNum.setText(_translate("MainWindow", "None", None))
        self.m4TorqueNum.setText(_translate("MainWindow", "None", None))
        self.m4ErrNum.setText(_translate("MainWindow", "None", None))
        self.m4TempNum.setText(_translate("MainWindow", "None", None))
        self.m4GoalTLabel.setText(_translate("MainWindow", "Goal Time", None))
        self.m4UpdateBtn.setText(_translate("MainWindow", "Update Motor", None))
        self.m4AngleLabel.setText(_translate("MainWindow", "Angle", None))
        self.m4PositionLabel.setText(_translate("MainWindow", "Position", None))
        self.m4AngleBtn.setText(_translate("MainWindow", "Go Angle", None))
        self.m4PositionBtn.setText(_translate("MainWindow", "Go Position", None))
        self.m4HomeBtn.setText(_translate("MainWindow", "Back to Home", None))
        self.m4Label.setText(_translate("MainWindow", "Motor 4", None))
        self.m5AngLabel.setText(_translate("MainWindow", "Angle", None))
        self.m5PosLabel.setText(_translate("MainWindow", "Position", None))
        self.m5TorqueLabel.setText(_translate("MainWindow", "Torque Status", None))
        self.m5TempLabel.setText(_translate("MainWindow", "Temprature", None))
        self.m5ErrLabel.setText(_translate("MainWindow", "Error", None))
        self.m5AngNum.setText(_translate("MainWindow", "None", None))
        self.m5PosNum.setText(_translate("MainWindow", "None", None))
        self.m5TorqueNum.setText(_translate("MainWindow", "None", None))
        self.m5ErrNum.setText(_translate("MainWindow", "None", None))
        self.m5TempNum.setText(_translate("MainWindow", "None", None))
        self.m5GoalTLabel.setText(_translate("MainWindow", "Goal Time", None))
        self.m5UpdateBtn.setText(_translate("MainWindow", "Update Motor", None))
        self.m5AngleLabel.setText(_translate("MainWindow", "Angle", None))
        self.m5PositionLabel.setText(_translate("MainWindow", "Position", None))
        self.m5AngleBtn.setText(_translate("MainWindow", "Go Angle", None))
        self.m5PositionBtn.setText(_translate("MainWindow", "Go Position", None))
        self.m5HomeBtn.setText(_translate("MainWindow", "Back to Home", None))
        self.m5Label.setText(_translate("MainWindow", "Motor 5", None))
        self.m6Label.setText(_translate("MainWindow", "Motor 6", None))
        self.m6GoalTLabel.setText(_translate("MainWindow", "Goal Time", None))
        self.m6UpdateBtn.setText(_translate("MainWindow", "Update Motor", None))
        self.m6AngleLabel.setText(_translate("MainWindow", "Angle", None))
        self.m6PositionLabel.setText(_translate("MainWindow", "Position", None))
        self.m6AngleBtn.setText(_translate("MainWindow", "Go Angle", None))
        self.m6PositionBtn.setText(_translate("MainWindow", "Go Position", None))
        self.m6HomeBtn.setText(_translate("MainWindow", "Back to Home", None))
        self.m6AngLabel.setText(_translate("MainWindow", "Angle", None))
        self.m6PosLabel.setText(_translate("MainWindow", "Position", None))
        self.m6TorqueLabel.setText(_translate("MainWindow", "Torque Status", None))
        self.m6TempLabel.setText(_translate("MainWindow", "Temprature", None))
        self.m6ErrLabel.setText(_translate("MainWindow", "Error", None))
        self.m6AngNum.setText(_translate("MainWindow", "None", None))
        self.m6PosNum.setText(_translate("MainWindow", "None", None))
        self.m6TorqueNum.setText(_translate("MainWindow", "None", None))
        self.m6ErrNum.setText(_translate("MainWindow", "None", None))
        self.m6TempNum.setText(_translate("MainWindow", "None", None))
        self.m7Label.setText(_translate("MainWindow", "Motor 7", None))
        self.m7GoalTLabel.setText(_translate("MainWindow", "Goal Time", None))
        self.m7UpdateBtn.setText(_translate("MainWindow", "Update Motor", None))
        self.m7AngleLabel.setText(_translate("MainWindow", "Angle", None))
        self.m7PositionLabel.setText(_translate("MainWindow", "Position", None))
        self.m7AngleBtn.setText(_translate("MainWindow", "Go Angle", None))
        self.m7PositionBtn.setText(_translate("MainWindow", "Go Position", None))
        self.m7HomeBtn.setText(_translate("MainWindow", "Back to Home", None))
        self.m7AngLabel.setText(_translate("MainWindow", "Angle", None))
        self.m7PosLabel.setText(_translate("MainWindow", "Position", None))
        self.m7TorqueLabel.setText(_translate("MainWindow", "Torque Status", None))
        self.m7TempLabel.setText(_translate("MainWindow", "Temprature", None))
        self.m7ErrLabel.setText(_translate("MainWindow", "Error", None))
        self.m7AngNum.setText(_translate("MainWindow", "None", None))
        self.m7PosNum.setText(_translate("MainWindow", "None", None))
        self.m7TorqueNum.setText(_translate("MainWindow", "None", None))
        self.m7ErrNum.setText(_translate("MainWindow", "None", None))
        self.m7TempNum.setText(_translate("MainWindow", "None", None))
        self.m8AngLabel.setText(_translate("MainWindow", "Angle", None))
        self.m8PosLabel.setText(_translate("MainWindow", "Position", None))
        self.m8TorqueLabel.setText(_translate("MainWindow", "Torque Status", None))
        self.m8TempLabel.setText(_translate("MainWindow", "Temprature", None))
        self.m8ErrLabel.setText(_translate("MainWindow", "Error", None))
        self.m8AngNum.setText(_translate("MainWindow", "None", None))
        self.m8PosNum.setText(_translate("MainWindow", "None", None))
        self.m8TorqueNum.setText(_translate("MainWindow", "None", None))
        self.m8ErrNum.setText(_translate("MainWindow", "None", None))
        self.m8TempNum.setText(_translate("MainWindow", "None", None))
        self.m8Label.setText(_translate("MainWindow", "Motor 8", None))
        self.m8GoalTLabel.setText(_translate("MainWindow", "Goal Time", None))
        self.m8UpdateBtn.setText(_translate("MainWindow", "Update Motor", None))
        self.m8AngleLabel.setText(_translate("MainWindow", "Angle", None))
        self.m8PositionLabel.setText(_translate("MainWindow", "Position", None))
        self.m8AngleBtn.setText(_translate("MainWindow", "Go Angle", None))
        self.m8PositionBtn.setText(_translate("MainWindow", "Go Position", None))
        self.m8HomeBtn.setText(_translate("MainWindow", "Back to Home", None))
        self.m9Label.setText(_translate("MainWindow", "Motor 9", None))
        self.m9GoalTLabel.setText(_translate("MainWindow", "Goal Time", None))
        self.m9UpdateBtn.setText(_translate("MainWindow", "Update Motor", None))
        self.m9AngleLabel.setText(_translate("MainWindow", "Angle", None))
        self.m9PositionLabel.setText(_translate("MainWindow", "Position", None))
        self.m9AngleBtn.setText(_translate("MainWindow", "Go Angle", None))
        self.m9PositionBtn.setText(_translate("MainWindow", "Go Position", None))
        self.m9HomeBtn.setText(_translate("MainWindow", "Back to Home", None))
        self.m9AngLabel.setText(_translate("MainWindow", "Angle", None))
        self.m9PosLabel.setText(_translate("MainWindow", "Position", None))
        self.m9TorqueLabel.setText(_translate("MainWindow", "Torque Status", None))
        self.m9TempLabel.setText(_translate("MainWindow", "Temprature", None))
        self.m9ErrLabel.setText(_translate("MainWindow", "Error", None))
        self.m9AngNum.setText(_translate("MainWindow", "None", None))
        self.m9PosNum.setText(_translate("MainWindow", "None", None))
        self.m9TorqueNum.setText(_translate("MainWindow", "None", None))
        self.m9ErrNum.setText(_translate("MainWindow", "None", None))
        self.m9TempNum.setText(_translate("MainWindow", "None", None))
        self.m10Label.setText(_translate("MainWindow", "Motor 10", None))
        self.m10GoalTLabel.setText(_translate("MainWindow", "Goal Time", None))
        self.m10UpdateBtn.setText(_translate("MainWindow", "Update Motor", None))
        self.m10AngleLabel.setText(_translate("MainWindow", "Angle", None))
        self.m10PositionLabel.setText(_translate("MainWindow", "Position", None))
        self.m10AngleBtn.setText(_translate("MainWindow", "Go Angle", None))
        self.m10PositionBtn.setText(_translate("MainWindow", "Go Position", None))
        self.m10HomeBtn.setText(_translate("MainWindow", "Back to Home", None))
        self.m10AngLabel.setText(_translate("MainWindow", "Angle", None))
        self.m10PosLabel.setText(_translate("MainWindow", "Position", None))
        self.m10TorqueLabel.setText(_translate("MainWindow", "Torque Status", None))
        self.m10TempLabel.setText(_translate("MainWindow", "Temprature", None))
        self.m10ErrLabel.setText(_translate("MainWindow", "Error", None))
        self.m10AngNum.setText(_translate("MainWindow", "None", None))
        self.m10PosNum.setText(_translate("MainWindow", "None", None))
        self.m10TorqueNum.setText(_translate("MainWindow", "None", None))
        self.m10ErrNum.setText(_translate("MainWindow", "None", None))
        self.m10TempNum.setText(_translate("MainWindow", "None", None))
        self.m11Label.setText(_translate("MainWindow", "Motor 11", None))
        self.m11GoalTLabel.setText(_translate("MainWindow", "Goal Time", None))
        self.m11UpdateBtn.setText(_translate("MainWindow", "Update Motor", None))
        self.m11AngleLabel.setText(_translate("MainWindow", "Angle", None))
        self.m11PositionLabel.setText(_translate("MainWindow", "Position", None))
        self.m11AngleBtn.setText(_translate("MainWindow", "Go Angle", None))
        self.m11PositionBtn.setText(_translate("MainWindow", "Go Position", None))
        self.m11HomeBtn.setText(_translate("MainWindow", "Back to Home", None))
        self.m11AngLabel.setText(_translate("MainWindow", "Angle", None))
        self.m11PosLabel.setText(_translate("MainWindow", "Position", None))
        self.m11TorqueLabel.setText(_translate("MainWindow", "Torque Status", None))
        self.m11TempLabel.setText(_translate("MainWindow", "Temprature", None))
        self.m11ErrLabel.setText(_translate("MainWindow", "Error", None))
        self.m11AngNum.setText(_translate("MainWindow", "None", None))
        self.m11PosNum.setText(_translate("MainWindow", "None", None))
        self.m11TorqueNum.setText(_translate("MainWindow", "None", None))
        self.m11ErrNum.setText(_translate("MainWindow", "None", None))
        self.m11TempNum.setText(_translate("MainWindow", "None", None))
        self.m12Label.setText(_translate("MainWindow", "Motor 12", None))
        self.m12GoalTLabel.setText(_translate("MainWindow", "Goal Time", None))
        self.m12UpdateBtn.setText(_translate("MainWindow", "Update Motor", None))
        self.m12AngleLabel.setText(_translate("MainWindow", "Angle", None))
        self.m12PositionLabel.setText(_translate("MainWindow", "Position", None))
        self.m12AngleBtn.setText(_translate("MainWindow", "Go Angle", None))
        self.m12PositionBtn.setText(_translate("MainWindow", "Go Position", None))
        self.m12HomeBtn.setText(_translate("MainWindow", "Back to Home", None))
        self.m12AngLabel.setText(_translate("MainWindow", "Angle", None))
        self.m12PosLabel.setText(_translate("MainWindow", "Position", None))
        self.m12TorqueLabel.setText(_translate("MainWindow", "Torque Status", None))
        self.m12TempLabel.setText(_translate("MainWindow", "Temprature", None))
        self.m12ErrLabel.setText(_translate("MainWindow", "Error", None))
        self.m12AngNum.setText(_translate("MainWindow", "None", None))
        self.m12PosNum.setText(_translate("MainWindow", "None", None))
        self.m12TorqueNum.setText(_translate("MainWindow", "None", None))
        self.m12ErrNum.setText(_translate("MainWindow", "None", None))
        self.m12TempNum.setText(_translate("MainWindow", "None", None))
        self.m13Label.setText(_translate("MainWindow", "Motor 13", None))
        self.m13GoalTLabel.setText(_translate("MainWindow", "Goal Time", None))
        self.m13UpdateBtn.setText(_translate("MainWindow", "Update Motor", None))
        self.m13AngleLabel.setText(_translate("MainWindow", "Angle", None))
        self.m13PositionLabel.setText(_translate("MainWindow", "Position", None))
        self.m13AngleBtn.setText(_translate("MainWindow", "Go Angle", None))
        self.m13PositionBtn.setText(_translate("MainWindow", "Go Position", None))
        self.m13HomeBtn.setText(_translate("MainWindow", "Back to Home", None))
        self.m13AngLabel.setText(_translate("MainWindow", "Angle", None))
        self.m13PosLabel.setText(_translate("MainWindow", "Position", None))
        self.m13TorqueLabel.setText(_translate("MainWindow", "Torque Status", None))
        self.m13TempLabel.setText(_translate("MainWindow", "Temprature", None))
        self.m13ErrLabel.setText(_translate("MainWindow", "Error", None))
        self.m13AngNum.setText(_translate("MainWindow", "None", None))
        self.m13PosNum.setText(_translate("MainWindow", "None", None))
        self.m13TorqueNum.setText(_translate("MainWindow", "None", None))
        self.m13ErrNum.setText(_translate("MainWindow", "None", None))
        self.m13TempNum.setText(_translate("MainWindow", "None", None))
        self.m14Label.setText(_translate("MainWindow", "Motor 14", None))
        self.m14GoalTLabel.setText(_translate("MainWindow", "Goal Time", None))
        self.m14UpdateBtn.setText(_translate("MainWindow", "Update Motor", None))
        self.m14AngleLabel.setText(_translate("MainWindow", "Angle", None))
        self.m14PositionLabel.setText(_translate("MainWindow", "Position", None))
        self.m14AngleBtn.setText(_translate("MainWindow", "Go Angle", None))
        self.m14PositionBtn.setText(_translate("MainWindow", "Go Position", None))
        self.m14HomeBtn.setText(_translate("MainWindow", "Back to Home", None))
        self.m14AngLabel.setText(_translate("MainWindow", "Angle", None))
        self.m14PosLabel.setText(_translate("MainWindow", "Position", None))
        self.m14TorqueLabel.setText(_translate("MainWindow", "Torque Status", None))
        self.m14TempLabel.setText(_translate("MainWindow", "Temprature", None))
        self.m14ErrLabel.setText(_translate("MainWindow", "Error", None))
        self.m14AngNum.setText(_translate("MainWindow", "None", None))
        self.m14PosNum.setText(_translate("MainWindow", "None", None))
        self.m14TorqueNum.setText(_translate("MainWindow", "None", None))
        self.m14ErrNum.setText(_translate("MainWindow", "None", None))
        self.m14TempNum.setText(_translate("MainWindow", "None", None))
        self.m15Label.setText(_translate("MainWindow", "Motor 15", None))
        self.m15GoalTLabel.setText(_translate("MainWindow", "Goal Time", None))
        self.m15UpdateBtn.setText(_translate("MainWindow", "Update Motor", None))
        self.m15AngleLabel.setText(_translate("MainWindow", "Angle", None))
        self.m15PositionLabel.setText(_translate("MainWindow", "Position", None))
        self.m15AngleBtn.setText(_translate("MainWindow", "Go Angle", None))
        self.m15PositionBtn.setText(_translate("MainWindow", "Go Position", None))
        self.m15HomeBtn.setText(_translate("MainWindow", "Back to Home", None))
        self.m15AngLabel.setText(_translate("MainWindow", "Angle", None))
        self.m15PosLabel.setText(_translate("MainWindow", "Position", None))
        self.m15TorqueLabel.setText(_translate("MainWindow", "Torque Status", None))
        self.m15TempLabel.setText(_translate("MainWindow", "Temprature", None))
        self.m15ErrLabel.setText(_translate("MainWindow", "Error", None))
        self.m15AngNum.setText(_translate("MainWindow", "None", None))
        self.m15PosNum.setText(_translate("MainWindow", "None", None))
        self.m15TorqueNum.setText(_translate("MainWindow", "None", None))
        self.m15ErrNum.setText(_translate("MainWindow", "None", None))
        self.m15TempNum.setText(_translate("MainWindow", "None", None))
        self.m16Label.setText(_translate("MainWindow", "Motor 16", None))
        self.m16GoalTLabel.setText(_translate("MainWindow", "Goal Time", None))
        self.m16UpdateBtn.setText(_translate("MainWindow", "Update Motor", None))
        self.m16AngleLabel.setText(_translate("MainWindow", "Angle", None))
        self.m16PositionLabel.setText(_translate("MainWindow", "Position", None))
        self.m16AngleBtn.setText(_translate("MainWindow", "Go Angle", None))
        self.m16PositionBtn.setText(_translate("MainWindow", "Go Position", None))
        self.m16HomeBtn.setText(_translate("MainWindow", "Back to Home", None))
        self.m16AngLabel.setText(_translate("MainWindow", "Angle", None))
        self.m16PosLabel.setText(_translate("MainWindow", "Position", None))
        self.m16TorqueLabel.setText(_translate("MainWindow", "Torque Status", None))
        self.m16TempLabel.setText(_translate("MainWindow", "Temprature", None))
        self.m16ErrLabel.setText(_translate("MainWindow", "Error", None))
        self.m16AngNum.setText(_translate("MainWindow", "None", None))
        self.m16PosNum.setText(_translate("MainWindow", "None", None))
        self.m16TorqueNum.setText(_translate("MainWindow", "None", None))
        self.m16ErrNum.setText(_translate("MainWindow", "None", None))
        self.m16TempNum.setText(_translate("MainWindow", "None", None))
        self.m17Label.setText(_translate("MainWindow", "Motor 17", None))
        self.m17GoalTLabel.setText(_translate("MainWindow", "Goal Time", None))
        self.m17UpdateBtn.setText(_translate("MainWindow", "Update Motor", None))
        self.m17AngleLabel.setText(_translate("MainWindow", "Angle", None))
        self.m17PositionLabel.setText(_translate("MainWindow", "Position", None))
        self.m17AngleBtn.setText(_translate("MainWindow", "Go Angle", None))
        self.m17PositionBtn.setText(_translate("MainWindow", "Go Position", None))
        self.m17HomeBtn.setText(_translate("MainWindow", "Back to Home", None))
        self.m17AngLabel.setText(_translate("MainWindow", "Angle", None))
        self.m17PosLabel.setText(_translate("MainWindow", "Position", None))
        self.m17TorqueLabel.setText(_translate("MainWindow", "Torque Status", None))
        self.m17TempLabel.setText(_translate("MainWindow", "Temprature", None))
        self.m17ErrLabel.setText(_translate("MainWindow", "Error", None))
        self.m17AngNum.setText(_translate("MainWindow", "None", None))
        self.m17PosNum.setText(_translate("MainWindow", "None", None))
        self.m17TorqueNum.setText(_translate("MainWindow", "None", None))
        self.m17ErrNum.setText(_translate("MainWindow", "None", None))
        self.m17TempNum.setText(_translate("MainWindow", "None", None))
        self.m18Label.setText(_translate("MainWindow", "Motor 18", None))
        self.m18GoalTLabel.setText(_translate("MainWindow", "Goal Time", None))
        self.m18UpdateBtn.setText(_translate("MainWindow", "Update Motor", None))
        self.m18AngleLabel.setText(_translate("MainWindow", "Angle", None))
        self.m18PositionLabel.setText(_translate("MainWindow", "Position", None))
        self.m18AngleBtn.setText(_translate("MainWindow", "Go Angle", None))
        self.m18PositionBtn.setText(_translate("MainWindow", "Go Position", None))
        self.m18HomeBtn.setText(_translate("MainWindow", "Back to Home", None))
        self.m18AngLabel.setText(_translate("MainWindow", "Angle", None))
        self.m18PosLabel.setText(_translate("MainWindow", "Position", None))
        self.m18TorqueLabel.setText(_translate("MainWindow", "Torque Status", None))
        self.m18TempLabel.setText(_translate("MainWindow", "Temprature", None))
        self.m18ErrLabel.setText(_translate("MainWindow", "Error", None))
        self.m18AngNum.setText(_translate("MainWindow", "None", None))
        self.m18PosNum.setText(_translate("MainWindow", "None", None))
        self.m18TorqueNum.setText(_translate("MainWindow", "None", None))
        self.m18ErrNum.setText(_translate("MainWindow", "None", None))
        self.m18TempNum.setText(_translate("MainWindow", "None", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

