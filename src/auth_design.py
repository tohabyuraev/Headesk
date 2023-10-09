# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'auth_design.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QDialog, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)
import files

class Ui_Auth(object):
    def setupUi(self, Auth):
        if not Auth.objectName():
            Auth.setObjectName(u"Auth")
        Auth.setWindowModality(Qt.NonModal)
        Auth.resize(325, 500)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Auth.sizePolicy().hasHeightForWidth())
        Auth.setSizePolicy(sizePolicy)
        Auth.setMinimumSize(QSize(325, 500))
        Auth.setMaximumSize(QSize(325, 500))
        self.verticalLayout = QVBoxLayout(Auth)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_icon = QLabel(Auth)
        self.label_icon.setObjectName(u"label_icon")
        self.label_icon.setPixmap(QPixmap(u":/icons/icon/nic.ico"))
        self.label_icon.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label_icon)

        self.label_title = QLabel(Auth)
        self.label_title.setObjectName(u"label_title")
        font = QFont()
        font.setFamilies([u"Century"])
        font.setPointSize(20)
        self.label_title.setFont(font)
        self.label_title.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label_title)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_3)

        self.label_lgn = QLabel(Auth)
        self.label_lgn.setObjectName(u"label_lgn")
        font1 = QFont()
        font1.setFamilies([u"Century"])
        font1.setPointSize(16)
        self.label_lgn.setFont(font1)
        self.label_lgn.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label_lgn)

        self.le_lgn = QLineEdit(Auth)
        self.le_lgn.setObjectName(u"le_lgn")
        sizePolicy.setHeightForWidth(self.le_lgn.sizePolicy().hasHeightForWidth())
        self.le_lgn.setSizePolicy(sizePolicy)
        self.le_lgn.setCursor(QCursor(Qt.IBeamCursor))
        self.le_lgn.setMaxLength(10)
        self.le_lgn.setCursorPosition(0)
        self.le_lgn.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.le_lgn, 0, Qt.AlignHCenter)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_2)

        self.label_pwd = QLabel(Auth)
        self.label_pwd.setObjectName(u"label_pwd")
        self.label_pwd.setFont(font1)
        self.label_pwd.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label_pwd)

        self.le_pwd = QLineEdit(Auth)
        self.le_pwd.setObjectName(u"le_pwd")
        sizePolicy.setHeightForWidth(self.le_pwd.sizePolicy().hasHeightForWidth())
        self.le_pwd.setSizePolicy(sizePolicy)
        self.le_pwd.setMaxLength(16)
        self.le_pwd.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.le_pwd, 0, Qt.AlignHCenter)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.label_error = QLabel(Auth)
        self.label_error.setObjectName(u"label_error")
        font2 = QFont()
        font2.setFamilies([u"Century"])
        font2.setPointSize(10)
        self.label_error.setFont(font2)
        self.label_error.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label_error)

        self.pb = QPushButton(Auth)
        self.pb.setObjectName(u"pb")
        sizePolicy.setHeightForWidth(self.pb.sizePolicy().hasHeightForWidth())
        self.pb.setSizePolicy(sizePolicy)

        self.verticalLayout.addWidget(self.pb, 0, Qt.AlignHCenter)


        self.retranslateUi(Auth)

        QMetaObject.connectSlotsByName(Auth)
    # setupUi

    def retranslateUi(self, Auth):
        Auth.setWindowTitle(QCoreApplication.translate("Auth", u"\u0412\u0445\u043e\u0434 \u0432 \u0441\u0438\u0441\u0442\u0435\u043c\u0443", None))
        self.label_icon.setText("")
        self.label_title.setText(QCoreApplication.translate("Auth", u"\u0410\u0432\u0442\u043e\u0440\u0438\u0437\u0430\u0446\u0438\u044f", None))
        self.label_lgn.setText(QCoreApplication.translate("Auth", u"\u0418\u043c\u044f \u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u044f", None))
        self.label_pwd.setText(QCoreApplication.translate("Auth", u"\u041f\u0430\u0440\u043e\u043b\u044c", None))
        self.le_pwd.setText("")
        self.label_error.setText("")
        self.pb.setText(QCoreApplication.translate("Auth", u"\u0412\u0445\u043e\u0434", None))
    # retranslateUi

