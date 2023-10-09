# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'design.ui'
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
from PySide6.QtWebEngineWidgets import QWebEngineView
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QLabel,
    QMainWindow, QPushButton, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)
import files

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(914, 899)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMaximumSize(QSize(16777215, 16777215))
        MainWindow.setMouseTracking(False)
        MainWindow.setFocusPolicy(Qt.NoFocus)
        MainWindow.setAcceptDrops(False)
        icon = QIcon()
        icon.addFile(u":/icons/icon/nic.ico", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setDocumentMode(False)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy1)
        self.centralwidget.setMinimumSize(QSize(0, 0))
        self.centralwidget.setMaximumSize(QSize(16777215, 16777215))
        self.centralwidget.setMouseTracking(True)
        self.centralwidget.setAutoFillBackground(False)
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(8, 8, 8, 8)
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.btn_func1 = QPushButton(self.centralwidget)
        self.btn_func1.setObjectName(u"btn_func1")
        font = QFont()
        font.setFamilies([u"Century"])
        font.setPointSize(14)
        self.btn_func1.setFont(font)

        self.verticalLayout_2.addWidget(self.btn_func1)

        self.btn_func2 = QPushButton(self.centralwidget)
        self.btn_func2.setObjectName(u"btn_func2")
        self.btn_func2.setFont(font)

        self.verticalLayout_2.addWidget(self.btn_func2)


        self.verticalLayout.addLayout(self.verticalLayout_2)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_2)

        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(-1, 10, 0, 10)
        self.btn_app_ec = QPushButton(self.centralwidget)
        self.btn_app_ec.setObjectName(u"btn_app_ec")
        sizePolicy.setHeightForWidth(self.btn_app_ec.sizePolicy().hasHeightForWidth())
        self.btn_app_ec.setSizePolicy(sizePolicy)
        self.btn_app_ec.setFont(font)
        self.btn_app_ec.setCursor(QCursor(Qt.PointingHandCursor))
        icon1 = QIcon()
        icon1.addFile(u":/icons/icon/app/ec.ico", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_app_ec.setIcon(icon1)
        self.btn_app_ec.setIconSize(QSize(40, 40))

        self.gridLayout_2.addWidget(self.btn_app_ec, 1, 0, 1, 1)

        self.btn_app_chem = QPushButton(self.centralwidget)
        self.btn_app_chem.setObjectName(u"btn_app_chem")
        sizePolicy.setHeightForWidth(self.btn_app_chem.sizePolicy().hasHeightForWidth())
        self.btn_app_chem.setSizePolicy(sizePolicy)
        self.btn_app_chem.setCursor(QCursor(Qt.PointingHandCursor))
        icon2 = QIcon()
        icon2.addFile(u":/icons/icon/app/chem.ico", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_app_chem.setIcon(icon2)
        self.btn_app_chem.setIconSize(QSize(40, 40))

        self.gridLayout_2.addWidget(self.btn_app_chem, 1, 1, 1, 1)

        self.btn_app_bs = QPushButton(self.centralwidget)
        self.btn_app_bs.setObjectName(u"btn_app_bs")
        sizePolicy.setHeightForWidth(self.btn_app_bs.sizePolicy().hasHeightForWidth())
        self.btn_app_bs.setSizePolicy(sizePolicy)
        font1 = QFont()
        font1.setFamilies([u"Century"])
        font1.setPointSize(14)
        font1.setKerning(True)
        font1.setStyleStrategy(QFont.PreferDefault)
        self.btn_app_bs.setFont(font1)
        self.btn_app_bs.setCursor(QCursor(Qt.PointingHandCursor))
        icon3 = QIcon()
        icon3.addFile(u":/icons/icon/app/bs.ico", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_app_bs.setIcon(icon3)
        self.btn_app_bs.setIconSize(QSize(40, 40))

        self.gridLayout_2.addWidget(self.btn_app_bs, 2, 0, 1, 1)

        self.btn_app_emer = QPushButton(self.centralwidget)
        self.btn_app_emer.setObjectName(u"btn_app_emer")
        sizePolicy.setHeightForWidth(self.btn_app_emer.sizePolicy().hasHeightForWidth())
        self.btn_app_emer.setSizePolicy(sizePolicy)
        self.btn_app_emer.setCursor(QCursor(Qt.PointingHandCursor))
        icon4 = QIcon()
        icon4.addFile(u":/icons/icon/app/emer.ico", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_app_emer.setIcon(icon4)
        self.btn_app_emer.setIconSize(QSize(40, 40))

        self.gridLayout_2.addWidget(self.btn_app_emer, 2, 2, 1, 1)

        self.btn_app_dam = QPushButton(self.centralwidget)
        self.btn_app_dam.setObjectName(u"btn_app_dam")
        sizePolicy.setHeightForWidth(self.btn_app_dam.sizePolicy().hasHeightForWidth())
        self.btn_app_dam.setSizePolicy(sizePolicy)
        self.btn_app_dam.setCursor(QCursor(Qt.PointingHandCursor))
        icon5 = QIcon()
        icon5.addFile(u":/icons/icon/app/dam.ico", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_app_dam.setIcon(icon5)
        self.btn_app_dam.setIconSize(QSize(40, 40))

        self.gridLayout_2.addWidget(self.btn_app_dam, 1, 2, 1, 1)

        self.btn_app_toxi = QPushButton(self.centralwidget)
        self.btn_app_toxi.setObjectName(u"btn_app_toxi")
        sizePolicy.setHeightForWidth(self.btn_app_toxi.sizePolicy().hasHeightForWidth())
        self.btn_app_toxi.setSizePolicy(sizePolicy)
        self.btn_app_toxi.setCursor(QCursor(Qt.PointingHandCursor))
        icon6 = QIcon()
        icon6.addFile(u":/icons/icon/app/toxi.ico", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_app_toxi.setIcon(icon6)
        self.btn_app_toxi.setIconSize(QSize(40, 40))

        self.gridLayout_2.addWidget(self.btn_app_toxi, 2, 1, 1, 1)

        self.btn_app_tmp = QPushButton(self.centralwidget)
        self.btn_app_tmp.setObjectName(u"btn_app_tmp")
        sizePolicy.setHeightForWidth(self.btn_app_tmp.sizePolicy().hasHeightForWidth())
        self.btn_app_tmp.setSizePolicy(sizePolicy)
        self.btn_app_tmp.setCursor(QCursor(Qt.PointingHandCursor))
        icon7 = QIcon()
        icon7.addFile(u":/icons/icon/app/tmp.ico", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_app_tmp.setIcon(icon7)
        self.btn_app_tmp.setIconSize(QSize(40, 40))

        self.gridLayout_2.addWidget(self.btn_app_tmp, 3, 0, 1, 1)

        self.btn_app_ind = QPushButton(self.centralwidget)
        self.btn_app_ind.setObjectName(u"btn_app_ind")
        sizePolicy.setHeightForWidth(self.btn_app_ind.sizePolicy().hasHeightForWidth())
        self.btn_app_ind.setSizePolicy(sizePolicy)
        self.btn_app_ind.setCursor(QCursor(Qt.PointingHandCursor))
        icon8 = QIcon()
        icon8.addFile(u":/icons/icon/app/ind.ico", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_app_ind.setIcon(icon8)
        self.btn_app_ind.setIconSize(QSize(40, 40))

        self.gridLayout_2.addWidget(self.btn_app_ind, 3, 1, 1, 1)

        self.btn_app_ter = QPushButton(self.centralwidget)
        self.btn_app_ter.setObjectName(u"btn_app_ter")
        sizePolicy.setHeightForWidth(self.btn_app_ter.sizePolicy().hasHeightForWidth())
        self.btn_app_ter.setSizePolicy(sizePolicy)
        self.btn_app_ter.setCursor(QCursor(Qt.PointingHandCursor))
        icon9 = QIcon()
        icon9.addFile(u":/icons/icon/app/ter.ico", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_app_ter.setIcon(icon9)
        self.btn_app_ter.setIconSize(QSize(40, 40))

        self.gridLayout_2.addWidget(self.btn_app_ter, 3, 2, 1, 1)

        self.label_app = QLabel(self.centralwidget)
        self.label_app.setObjectName(u"label_app")
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.label_app.sizePolicy().hasHeightForWidth())
        self.label_app.setSizePolicy(sizePolicy2)
        self.label_app.setMaximumSize(QSize(16000, 16000))
        self.label_app.setFont(font)
        self.label_app.setLayoutDirection(Qt.LeftToRight)
        self.label_app.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.label_app, 0, 0, 1, 3)


        self.verticalLayout.addLayout(self.gridLayout_2)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.btn_marker = QPushButton(self.centralwidget)
        self.btn_marker.setObjectName(u"btn_marker")
        self.btn_marker.setEnabled(True)
        sizePolicy3 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.btn_marker.sizePolicy().hasHeightForWidth())
        self.btn_marker.setSizePolicy(sizePolicy3)
        self.btn_marker.setMaximumSize(QSize(16777215, 16777215))
        self.btn_marker.setFont(font)
        self.btn_marker.setLayoutDirection(Qt.LeftToRight)

        self.verticalLayout.addWidget(self.btn_marker)


        self.horizontalLayout.addLayout(self.verticalLayout)

        self.webview = QWebEngineView(self.centralwidget)
        self.webview.setObjectName(u"webview")
        sizePolicy1.setHeightForWidth(self.webview.sizePolicy().hasHeightForWidth())
        self.webview.setSizePolicy(sizePolicy1)
        self.webview.setUrl(QUrl(u"about:blank"))

        self.horizontalLayout.addWidget(self.webview)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Headesk", None))
        self.btn_func1.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0435\u0440\u0435\u0447\u0435\u043d\u044c \u0441\u043b\u0443\u0436\u0431", None))
        self.btn_func2.setText(QCoreApplication.translate("MainWindow", u"\u0410\u043d\u0430\u043b\u0438\u0437 \u0434\u0435\u0439\u0441\u0442\u0432\u0438\u0439", None))
#if QT_CONFIG(tooltip)
        self.btn_app_ec.setToolTip(QCoreApplication.translate("MainWindow", u"\u0420\u0430\u0441\u0447\u0435\u0442 \u0445\u0430\u0440\u0430\u043a\u0442\u0435\u0440\u0438\u0441\u0442\u0438\u043a \u0432\u0437\u0440\u044b\u0432\u0430", None))
#endif // QT_CONFIG(tooltip)
        self.btn_app_ec.setText("")
#if QT_CONFIG(tooltip)
        self.btn_app_chem.setToolTip(QCoreApplication.translate("MainWindow", u"\u0410\u0425\u041e\u0412", None))
#endif // QT_CONFIG(tooltip)
        self.btn_app_chem.setText("")
#if QT_CONFIG(tooltip)
        self.btn_app_bs.setToolTip(QCoreApplication.translate("MainWindow", u"\u041f\u0430\u0441\u043f\u043e\u0440\u0442 \u0431\u0435\u0437\u043e\u043f\u0430\u0441\u043d\u043e\u0441\u0442\u0438 \u0437\u0434\u0430\u043d\u0438\u044f", None))
#endif // QT_CONFIG(tooltip)
        self.btn_app_bs.setText("")
#if QT_CONFIG(tooltip)
        self.btn_app_emer.setToolTip(QCoreApplication.translate("MainWindow", u"\u0420\u0430\u0441\u0447\u0435\u0442 \u043f\u043b\u043e\u0449\u0430\u0434\u0438 \u043f\u043e\u0436\u0430\u0440\u0430", None))
#endif // QT_CONFIG(tooltip)
        self.btn_app_emer.setText("")
#if QT_CONFIG(tooltip)
        self.btn_app_dam.setToolTip(QCoreApplication.translate("MainWindow", u"\u0420\u0430\u0441\u0447\u0435\u0442 \u043f\u043b\u043e\u0442\u0438\u043d\u044b", None))
#endif // QT_CONFIG(tooltip)
        self.btn_app_dam.setText("")
#if QT_CONFIG(tooltip)
        self.btn_app_toxi.setToolTip(QCoreApplication.translate("MainWindow", u"Toxi", None))
#endif // QT_CONFIG(tooltip)
        self.btn_app_toxi.setText("")
#if QT_CONFIG(tooltip)
        self.btn_app_tmp.setToolTip(QCoreApplication.translate("MainWindow", u"\u0420\u0430\u0441\u0447\u0435\u0442 \u0438\u0437\u043c\u0435\u043d\u0435\u043d\u0438\u044f \u0442\u0435\u043c\u043f\u0435\u0440\u0430\u0442\u0443\u0440\u044b", None))
#endif // QT_CONFIG(tooltip)
        self.btn_app_tmp.setText("")
#if QT_CONFIG(tooltip)
        self.btn_app_ind.setToolTip(QCoreApplication.translate("MainWindow", u"\u0420\u0430\u0441\u0447\u0435\u0442 \u0437\u043e\u043d \u0432\u0437\u0440\u044b\u0432\u0430", None))
#endif // QT_CONFIG(tooltip)
        self.btn_app_ind.setText("")
#if QT_CONFIG(tooltip)
        self.btn_app_ter.setToolTip(QCoreApplication.translate("MainWindow", u"Strategy", None))
#endif // QT_CONFIG(tooltip)
        self.btn_app_ter.setText("")
        self.label_app.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u0438\u043b\u043e\u0436\u0435\u043d\u0438\u044f \u0434\u043b\u044f \u0440\u0430\u0441\u0447\u0435\u0442\u0430\n"
"\u0431\u0435\u0437\u043e\u043f\u0430\u0441\u043d\u043e\u0441\u0442\u0438 \u0437\u0434\u0430\u043d\u0438\u0439:", None))
        self.btn_marker.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c \u043c\u0430\u0440\u043a\u0435\u0440", None))
    # retranslateUi

