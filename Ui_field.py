# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/mnt/centos/home/ralsina/Desktop/proyectos/ra-flip/field.ui'
#
# Created: Mon Apr 30 17:53:30 2007
#      by: PyQt4 UI code generator 4.1.1
#
# WARNING! All changes made in this file will be lost!

import sys
from PyQt4 import QtCore, QtGui

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(QtCore.QSize(QtCore.QRect(0,0,611,549).size()).expandedTo(Form.minimumSizeHint()))

        self.vboxlayout = QtGui.QVBoxLayout(Form)
        self.vboxlayout.setMargin(9)
        self.vboxlayout.setSpacing(6)
        self.vboxlayout.setObjectName("vboxlayout")

        self.splitter = QtGui.QSplitter(Form)
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setObjectName("splitter")

        self.layoutWidget = QtGui.QWidget(self.splitter)
        self.layoutWidget.setObjectName("layoutWidget")

        self.hboxlayout = QtGui.QHBoxLayout(self.layoutWidget)
        self.hboxlayout.setMargin(0)
        self.hboxlayout.setSpacing(6)
        self.hboxlayout.setObjectName("hboxlayout")

        self.vboxlayout1 = QtGui.QVBoxLayout()
        self.vboxlayout1.setMargin(0)
        self.vboxlayout1.setSpacing(6)
        self.vboxlayout1.setObjectName("vboxlayout1")

        self.zoomIn = QtGui.QToolButton(self.layoutWidget)
        self.zoomIn.setIcon(QtGui.QIcon(":/viewmag+.png"))
        self.zoomIn.setAutoRepeat(True)
        self.zoomIn.setObjectName("zoomIn")
        self.vboxlayout1.addWidget(self.zoomIn)

        self.zoomOut = QtGui.QToolButton(self.layoutWidget)
        self.zoomOut.setIcon(QtGui.QIcon(":/viewmag-.png"))
        self.zoomOut.setAutoRepeat(True)
        self.zoomOut.setObjectName("zoomOut")
        self.vboxlayout1.addWidget(self.zoomOut)

        self.play = QtGui.QToolButton(self.layoutWidget)
        self.play.setIcon(QtGui.QIcon(":/player_play.png"))
        self.play.setAutoRepeat(True)
        self.play.setObjectName("play")
        self.vboxlayout1.addWidget(self.play)

        self.stop = QtGui.QToolButton(self.layoutWidget)
        self.stop.setEnabled(False)
        self.stop.setIcon(QtGui.QIcon(":/player_stop.png"))
        self.stop.setAutoRepeat(True)
        self.stop.setObjectName("stop")
        self.vboxlayout1.addWidget(self.stop)

        self.pause = QtGui.QToolButton(self.layoutWidget)
        self.pause.setEnabled(False)
        self.pause.setIcon(QtGui.QIcon(":/player_pause.png"))
        self.pause.setCheckable(True)
        self.pause.setAutoRepeat(True)
        self.pause.setObjectName("pause")
        self.vboxlayout1.addWidget(self.pause)

        spacerItem = QtGui.QSpacerItem(20,40,QtGui.QSizePolicy.Minimum,QtGui.QSizePolicy.Expanding)
        self.vboxlayout1.addItem(spacerItem)
        self.hboxlayout.addLayout(self.vboxlayout1)

        self.field = QtGui.QGraphicsView(self.layoutWidget)
        self.field.setDragMode(QtGui.QGraphicsView.ScrollHandDrag)
        self.field.setObjectName("field")
        self.hboxlayout.addWidget(self.field)

        self.layoutWidget1 = QtGui.QWidget(self.splitter)
        self.layoutWidget1.setObjectName("layoutWidget1")

        self.hboxlayout1 = QtGui.QHBoxLayout(self.layoutWidget1)
        self.hboxlayout1.setMargin(0)
        self.hboxlayout1.setSpacing(6)
        self.hboxlayout1.setObjectName("hboxlayout1")

        self.vboxlayout2 = QtGui.QVBoxLayout()
        self.vboxlayout2.setMargin(0)
        self.vboxlayout2.setSpacing(6)
        self.vboxlayout2.setObjectName("vboxlayout2")

        self.label = QtGui.QLabel(self.layoutWidget1)
        self.label.setObjectName("label")
        self.vboxlayout2.addWidget(self.label)

        self.input = QtGui.QTextEdit(self.layoutWidget1)
        self.input.setObjectName("input")
        self.vboxlayout2.addWidget(self.input)

        self.label_2 = QtGui.QLabel(self.layoutWidget1)
        self.label_2.setObjectName("label_2")
        self.vboxlayout2.addWidget(self.label_2)

        self.output = QtGui.QTextBrowser(self.layoutWidget1)
        self.output.setObjectName("output")
        self.vboxlayout2.addWidget(self.output)
        self.hboxlayout1.addLayout(self.vboxlayout2)

        self.vboxlayout3 = QtGui.QVBoxLayout()
        self.vboxlayout3.setMargin(0)
        self.vboxlayout3.setSpacing(6)
        self.vboxlayout3.setObjectName("vboxlayout3")

        self.vboxlayout4 = QtGui.QVBoxLayout()
        self.vboxlayout4.setMargin(0)
        self.vboxlayout4.setSpacing(6)
        self.vboxlayout4.setObjectName("vboxlayout4")

        self.hboxlayout2 = QtGui.QHBoxLayout()
        self.hboxlayout2.setMargin(0)
        self.hboxlayout2.setSpacing(6)
        self.hboxlayout2.setObjectName("hboxlayout2")

        self.hwall = QtGui.QToolButton(self.layoutWidget1)
        self.hwall.setIcon(QtGui.QIcon(":/hwall.svg"))
        self.hwall.setCheckable(True)
        self.hwall.setObjectName("hwall")
        self.hboxlayout2.addWidget(self.hwall)

        self.vwall = QtGui.QToolButton(self.layoutWidget1)
        self.vwall.setIcon(QtGui.QIcon(":/vwall.svg"))
        self.vwall.setCheckable(True)
        self.vwall.setObjectName("vwall")
        self.hboxlayout2.addWidget(self.vwall)

        self.swall = QtGui.QToolButton(self.layoutWidget1)
        self.swall.setIcon(QtGui.QIcon(":/swall.svg"))
        self.swall.setCheckable(True)
        self.swall.setObjectName("swall")
        self.hboxlayout2.addWidget(self.swall)

        self.bswall = QtGui.QToolButton(self.layoutWidget1)
        self.bswall.setIcon(QtGui.QIcon(":/bswall.svg"))
        self.bswall.setCheckable(True)
        self.bswall.setObjectName("bswall")
        self.hboxlayout2.addWidget(self.bswall)
        self.vboxlayout4.addLayout(self.hboxlayout2)

        self.hboxlayout3 = QtGui.QHBoxLayout()
        self.hboxlayout3.setMargin(0)
        self.hboxlayout3.setSpacing(6)
        self.hboxlayout3.setObjectName("hboxlayout3")

        self.toolButton_5 = QtGui.QToolButton(self.layoutWidget1)
        self.toolButton_5.setIcon(QtGui.QIcon(":/lsluice.svg"))
        self.toolButton_5.setCheckable(True)
        self.toolButton_5.setObjectName("toolButton_5")
        self.hboxlayout3.addWidget(self.toolButton_5)

        self.toolButton_26 = QtGui.QToolButton(self.layoutWidget1)
        self.toolButton_26.setIcon(QtGui.QIcon(":/rsluice.svg"))
        self.toolButton_26.setCheckable(True)
        self.toolButton_26.setObjectName("toolButton_26")
        self.hboxlayout3.addWidget(self.toolButton_26)

        self.toolButton_27 = QtGui.QToolButton(self.layoutWidget1)
        self.toolButton_27.setIcon(QtGui.QIcon(":/usluice.svg"))
        self.toolButton_27.setCheckable(True)
        self.toolButton_27.setObjectName("toolButton_27")
        self.hboxlayout3.addWidget(self.toolButton_27)

        self.toolButton_28 = QtGui.QToolButton(self.layoutWidget1)
        self.toolButton_28.setIcon(QtGui.QIcon(":/dsluice.svg"))
        self.toolButton_28.setCheckable(True)
        self.toolButton_28.setObjectName("toolButton_28")
        self.hboxlayout3.addWidget(self.toolButton_28)
        self.vboxlayout4.addLayout(self.hboxlayout3)

        self.hboxlayout4 = QtGui.QHBoxLayout()
        self.hboxlayout4.setMargin(0)
        self.hboxlayout4.setSpacing(6)
        self.hboxlayout4.setObjectName("hboxlayout4")

        self.toolButton_29 = QtGui.QToolButton(self.layoutWidget1)
        self.toolButton_29.setIcon(QtGui.QIcon(":/processor.svg"))
        self.toolButton_29.setCheckable(True)
        self.toolButton_29.setObjectName("toolButton_29")
        self.hboxlayout4.addWidget(self.toolButton_29)

        self.toolButton_30 = QtGui.QToolButton(self.layoutWidget1)
        self.toolButton_30.setCheckable(True)
        self.toolButton_30.setObjectName("toolButton_30")
        self.hboxlayout4.addWidget(self.toolButton_30)

        self.toolButton_31 = QtGui.QToolButton(self.layoutWidget1)
        self.toolButton_31.setCheckable(True)
        self.toolButton_31.setObjectName("toolButton_31")
        self.hboxlayout4.addWidget(self.toolButton_31)

        self.toolButton_32 = QtGui.QToolButton(self.layoutWidget1)
        self.toolButton_32.setCheckable(True)
        self.toolButton_32.setObjectName("toolButton_32")
        self.hboxlayout4.addWidget(self.toolButton_32)
        self.vboxlayout4.addLayout(self.hboxlayout4)

        self.hboxlayout5 = QtGui.QHBoxLayout()
        self.hboxlayout5.setMargin(0)
        self.hboxlayout5.setSpacing(6)
        self.hboxlayout5.setObjectName("hboxlayout5")

        self.toolButton_33 = QtGui.QToolButton(self.layoutWidget1)
        self.toolButton_33.setIcon(QtGui.QIcon(":/always.svg"))
        self.toolButton_33.setCheckable(True)
        self.toolButton_33.setObjectName("toolButton_33")
        self.hboxlayout5.addWidget(self.toolButton_33)

        self.toolButton_34 = QtGui.QToolButton(self.layoutWidget1)
        self.toolButton_34.setCheckable(True)
        self.toolButton_34.setObjectName("toolButton_34")
        self.hboxlayout5.addWidget(self.toolButton_34)

        self.toolButton_35 = QtGui.QToolButton(self.layoutWidget1)
        self.toolButton_35.setCheckable(True)
        self.toolButton_35.setObjectName("toolButton_35")
        self.hboxlayout5.addWidget(self.toolButton_35)

        self.toolButton_36 = QtGui.QToolButton(self.layoutWidget1)
        self.toolButton_36.setCheckable(True)
        self.toolButton_36.setObjectName("toolButton_36")
        self.hboxlayout5.addWidget(self.toolButton_36)
        self.vboxlayout4.addLayout(self.hboxlayout5)

        self.hboxlayout6 = QtGui.QHBoxLayout()
        self.hboxlayout6.setMargin(0)
        self.hboxlayout6.setSpacing(6)
        self.hboxlayout6.setObjectName("hboxlayout6")

        self.toolButton_37 = QtGui.QToolButton(self.layoutWidget1)
        self.toolButton_37.setCheckable(True)
        self.toolButton_37.setObjectName("toolButton_37")
        self.hboxlayout6.addWidget(self.toolButton_37)

        self.toolButton_38 = QtGui.QToolButton(self.layoutWidget1)
        self.toolButton_38.setCheckable(True)
        self.toolButton_38.setObjectName("toolButton_38")
        self.hboxlayout6.addWidget(self.toolButton_38)

        self.toolButton_39 = QtGui.QToolButton(self.layoutWidget1)
        self.toolButton_39.setCheckable(True)
        self.toolButton_39.setObjectName("toolButton_39")
        self.hboxlayout6.addWidget(self.toolButton_39)

        self.toolButton_40 = QtGui.QToolButton(self.layoutWidget1)
        self.toolButton_40.setIcon(QtGui.QIcon(":/terminate.svg"))
        self.toolButton_40.setCheckable(True)
        self.toolButton_40.setObjectName("toolButton_40")
        self.hboxlayout6.addWidget(self.toolButton_40)
        self.vboxlayout4.addLayout(self.hboxlayout6)
        self.vboxlayout3.addLayout(self.vboxlayout4)

        spacerItem1 = QtGui.QSpacerItem(20,40,QtGui.QSizePolicy.Minimum,QtGui.QSizePolicy.Expanding)
        self.vboxlayout3.addItem(spacerItem1)
        self.hboxlayout1.addLayout(self.vboxlayout3)
        self.vboxlayout.addWidget(self.splitter)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtGui.QApplication.translate("Form", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.zoomIn.setText(QtGui.QApplication.translate("Form", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.zoomOut.setText(QtGui.QApplication.translate("Form", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.play.setText(QtGui.QApplication.translate("Form", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.stop.setText(QtGui.QApplication.translate("Form", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.pause.setText(QtGui.QApplication.translate("Form", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Form", "Input", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("Form", "Output", None, QtGui.QApplication.UnicodeUTF8))
        self.hwall.setText(QtGui.QApplication.translate("Form", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.vwall.setText(QtGui.QApplication.translate("Form", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.swall.setText(QtGui.QApplication.translate("Form", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.bswall.setText(QtGui.QApplication.translate("Form", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.toolButton_5.setText(QtGui.QApplication.translate("Form", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.toolButton_26.setText(QtGui.QApplication.translate("Form", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.toolButton_27.setText(QtGui.QApplication.translate("Form", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.toolButton_28.setText(QtGui.QApplication.translate("Form", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.toolButton_29.setText(QtGui.QApplication.translate("Form", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.toolButton_30.setText(QtGui.QApplication.translate("Form", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.toolButton_31.setText(QtGui.QApplication.translate("Form", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.toolButton_32.setText(QtGui.QApplication.translate("Form", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.toolButton_33.setText(QtGui.QApplication.translate("Form", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.toolButton_34.setText(QtGui.QApplication.translate("Form", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.toolButton_35.setText(QtGui.QApplication.translate("Form", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.toolButton_36.setText(QtGui.QApplication.translate("Form", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.toolButton_37.setText(QtGui.QApplication.translate("Form", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.toolButton_38.setText(QtGui.QApplication.translate("Form", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.toolButton_39.setText(QtGui.QApplication.translate("Form", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.toolButton_40.setText(QtGui.QApplication.translate("Form", "...", None, QtGui.QApplication.UnicodeUTF8))

import icons_rc


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    Form = QtGui.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
