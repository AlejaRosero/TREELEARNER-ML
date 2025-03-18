# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Ventana_Principal.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_VentanaPrincipal(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(838, 600)
        MainWindow.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"QPushButton {\n"
"    background-color: #6BA614;  /* Fondo más transparente */\n"
"    border-radius: 5px;  /* Bordes redondeados */\n"
"    padding: 5px 5px;  /* Espaciado interno */\n"
"    font: bold 12px \"Montserrat\";  /* Fuente moderna */\n"
"    color: white;  /* Texto en blanco */\n"
"    border: none;  /* Sin borde */\n"
"    box-shadow: 3px 3px 8px rgba(0, 0, 0, 0.2);  /* Sombra sutil */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #3A5A40;  /* Cambio de color al pasar el mouse */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #2C4A34;  /* Cambio de color al hacer clic */\n"
"    box-shadow: none;  /* Quita la sombra para efecto de presión */\n"
"}\n"
"")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridFrame = QtWidgets.QFrame(self.centralwidget)
        self.gridFrame.setStyleSheet("")
        self.gridFrame.setObjectName("gridFrame")
        self.gridLayout = QtWidgets.QGridLayout(self.gridFrame)
        self.gridLayout.setObjectName("gridLayout")
        self.frame_2 = QtWidgets.QFrame(self.gridFrame)
        self.frame_2.setStyleSheet("background-color: rgb(155, 124, 255);\n"
"background-color: rgb(255, 255, 255);")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame_3 = QtWidgets.QFrame(self.frame_2)
        self.frame_3.setStyleSheet("")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_3)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.LabelCamara = QtWidgets.QLabel(self.frame_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.LabelCamara.sizePolicy().hasHeightForWidth())
        self.LabelCamara.setSizePolicy(sizePolicy)
        self.LabelCamara.setMinimumSize(QtCore.QSize(0, 280))
        self.LabelCamara.setMaximumSize(QtCore.QSize(16777215, 280))
        self.LabelCamara.setStyleSheet("background-color: rgb(177, 217, 137);a")
        self.LabelCamara.setText("")
        self.LabelCamara.setObjectName("LabelCamara")
        self.verticalLayout_3.addWidget(self.LabelCamara, 0, QtCore.Qt.AlignTop)
        self.verticalLayout.addWidget(self.frame_3)
        self.frame_4 = QtWidgets.QFrame(self.frame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_4.sizePolicy().hasHeightForWidth())
        self.frame_4.setSizePolicy(sizePolicy)
        self.frame_4.setMinimumSize(QtCore.QSize(0, 100))
        self.frame_4.setStyleSheet("")
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.frame_4)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.BtnSubir = QtWidgets.QPushButton(self.frame_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.BtnSubir.sizePolicy().hasHeightForWidth())
        self.BtnSubir.setSizePolicy(sizePolicy)
        self.BtnSubir.setMinimumSize(QtCore.QSize(170, 25))
        self.BtnSubir.setMaximumSize(QtCore.QSize(170, 25))
        self.BtnSubir.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.BtnSubir.setStyleSheet("QPushButton {\n"
"    background-color: #6BA614;  /* Fondo más transparente */\n"
"    border-radius: 2px;  /* Bordes redondeados */\n"
"    padding: 5px 5px;  /* Espaciado interno */\n"
"    font: bold 12px \"Montserrat\";  /* Fuente moderna */\n"
"    color: white;  /* Texto en blanco */\n"
"    border: none;  /* Sin borde */\n"
"    box-shadow: 3px 3px 8px rgba(0, 0, 0, 0.2);  /* Sombra sutil */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #3A5A40;  /* Cambio de color al pasar el mouse */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #2C4A34;  /* Cambio de color al hacer clic */\n"
"    box-shadow: none;  /* Quita la sombra para efecto de presión */\n"
"}\n"
"")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("static/folder-upload.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.BtnSubir.setIcon(icon)
        self.BtnSubir.setObjectName("BtnSubir")
        self.gridLayout_3.addWidget(self.BtnSubir, 1, 2, 1, 1, QtCore.Qt.AlignHCenter)
        self.BarraProgreso = QtWidgets.QProgressBar(self.frame_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.BarraProgreso.sizePolicy().hasHeightForWidth())
        self.BarraProgreso.setSizePolicy(sizePolicy)
        self.BarraProgreso.setMinimumSize(QtCore.QSize(300, 25))
        self.BarraProgreso.setMaximumSize(QtCore.QSize(300, 25))
        self.BarraProgreso.setStyleSheet("QProgressBar {\n"
"    border: 1px solid #6BA614;  /* Borde sutil verde oscuro */\n"
"    border-radius: 2px;  /* Bordes más redondeados */\n"
"    background-color: #f0f0f0;  /* Fondo gris claro */\n"
"    text-align: center;  /* Texto centrado */\n"
"    font: bold 12px \"Montserrat\";  /* Fuente más elegante */\n"
"    color: #ffffff;  /* Color de texto oscuro */\n"
"    padding: 2px;  /* Espaciado interno */\n"
"}\n"
"\n"
"QProgressBar::chunk {\n"
"    background: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, \n"
"                                stop:0 #6BA614, stop:1 #B1D989); /* Degradado */\n"
"    border-radius: 6px;  /* Bordes redondeados en la barra */\n"
"    transition: background 0.3s ease-in-out;  /* Transición suave */\n"
"}\n"
"\n"
"/* Efecto hover para resaltar cuando se pase el mouse */\n"
"QProgressBar:hover::chunk {\n"
"    background: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, \n"
"                                stop:0 #5B900F, stop:1 #A3C873); /* Verde más oscuro */\n"
"}\n"
"")
        self.BarraProgreso.setProperty("value", 24)
        self.BarraProgreso.setObjectName("BarraProgreso")
        self.gridLayout_3.addWidget(self.BarraProgreso, 0, 2, 1, 1, QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.ImgDefecto = QtWidgets.QLabel(self.frame_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ImgDefecto.sizePolicy().hasHeightForWidth())
        self.ImgDefecto.setSizePolicy(sizePolicy)
        self.ImgDefecto.setMinimumSize(QtCore.QSize(150, 100))
        self.ImgDefecto.setMaximumSize(QtCore.QSize(150, 100))
        self.ImgDefecto.setStyleSheet("background-color: rgb(146, 226, 255);")
        self.ImgDefecto.setText("")
        self.ImgDefecto.setPixmap(QtGui.QPixmap("static/blog_placeholder.jpg"))
        self.ImgDefecto.setScaledContents(True)
        self.ImgDefecto.setObjectName("ImgDefecto")
        self.gridLayout_3.addWidget(self.ImgDefecto, 0, 0, 1, 1, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        spacerItem = QtWidgets.QSpacerItem(100, 100, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem, 0, 3, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem1, 0, 1, 1, 1)
        self.verticalLayout.addWidget(self.frame_4)
        self.gridLayout.addWidget(self.frame_2, 0, 0, 1, 1)
        self.frame = QtWidgets.QFrame(self.gridFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setMinimumSize(QtCore.QSize(200, 0))
        self.frame.setStyleSheet("\n"
"border-radius: 5px;  /* Bordes redondeados */\n"
"box-shadow: 3px 3px 8px rgba(0, 0, 0, 0.2); /* Sombra suave */\n"
"")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMinimumSize(QtCore.QSize(200, 90))
        self.label.setMaximumSize(QtCore.QSize(200, 90))
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setStyleSheet("QLabel {\n"
"    border: none;\n"
"}\n"
"")
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("static/IconoTesisAc.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.toolButton = QtWidgets.QToolButton(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.toolButton.sizePolicy().hasHeightForWidth())
        self.toolButton.setSizePolicy(sizePolicy)
        self.toolButton.setMinimumSize(QtCore.QSize(200, 0))
        self.toolButton.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.toolButton.setStyleSheet("QToolButton {\n"
"    background-color: #6BA614;  /* Color de fondo */\n"
"    border-radius: 5px;  /* Bordes redondeados */\n"
"    padding: 5px 20px;  /* Espaciado, ajustado para el icono */\n"
"    font: bold 10px \"Montserrat\";  /* Fuente moderna */\n"
"    color: white;  /* Texto en blanco */\n"
"    border: none;  /* Sin borde */\n"
"    box-shadow: 3px 3px 8px rgba(0, 0, 0, 0.2);  /* Sombra sutil */\n"
"}\n"
"\n"
"")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("static/tree.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton.setIcon(icon1)
        self.toolButton.setIconSize(QtCore.QSize(32, 15))
        self.toolButton.setToolButtonStyle(QtCore.Qt.ToolButtonTextBesideIcon)
        self.toolButton.setAutoRaise(False)
        self.toolButton.setObjectName("toolButton")
        self.verticalLayout_2.addWidget(self.toolButton, 0, QtCore.Qt.AlignHCenter)
        self.LabelNombre1 = QtWidgets.QLabel(self.frame)
        self.LabelNombre1.setStyleSheet("QLabel {\n"
"    font: bold 10px \"Georgia\", serif;  /* Fuente aún más elegante y con mayor estilo */\n"
"    background-color: #B1D989;  /* Fondo más transparente */\n"
"    border: none;  /* Sin bordes en los lados */\n"
"    border-radius: 5px;  /* Bordes más suaves */\n"
"    color: #2b2b2b;  /* Color del texto */\n"
"    padding: 5px 15px;  /* Espaciado más amplio */\n"
"    letter-spacing: 1.5px;  /* Espaciado entre letras más elegante */\n"
"    text-transform: capitalize;  /* Primera letra en mayúscula */\n"
"    text-align: center;  /* Centrar el texto */\n"
"  \n"
"}\n"
"")
        self.LabelNombre1.setObjectName("LabelNombre1")
        self.verticalLayout_2.addWidget(self.LabelNombre1)
        self.toolButton_2 = QtWidgets.QToolButton(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.toolButton_2.sizePolicy().hasHeightForWidth())
        self.toolButton_2.setSizePolicy(sizePolicy)
        self.toolButton_2.setMinimumSize(QtCore.QSize(200, 0))
        self.toolButton_2.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.toolButton_2.setStyleSheet("QToolButton {\n"
"    background-color: #6BA614;  /* Color de fondo */\n"
"    border-radius: 5px;  /* Bordes redondeados */\n"
"    padding: 5px 20px;  /* Espaciado, ajustado para el icono */\n"
"    font: bold 10px \"Montserrat\";  /* Fuente moderna */\n"
"    color: white;  /* Texto en blanco */\n"
"    border: none;  /* Sin borde */\n"
"    box-shadow: 3px 3px 8px rgba(0, 0, 0, 0.2);  /* Sombra sutil */\n"
"}\n"
"\n"
"")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("static/attribution-pencil.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_2.setIcon(icon2)
        self.toolButton_2.setToolButtonStyle(QtCore.Qt.ToolButtonTextBesideIcon)
        self.toolButton_2.setObjectName("toolButton_2")
        self.verticalLayout_2.addWidget(self.toolButton_2)
        self.LabelNombre2 = QtWidgets.QLabel(self.frame)
        self.LabelNombre2.setStyleSheet("QLabel {\n"
"    font: bold 10px \"Georgia\", serif;  /* Fuente aún más elegante y con mayor estilo */\n"
"    background-color: #B1D989;  /* Fondo más transparente */\n"
"    border: none;  /* Sin bordes en los lados */\n"
"    border-radius: 5px;  /* Bordes más suaves */\n"
"    color: #2b2b2b;  /* Color del texto */\n"
"    padding: 5px 15px;  /* Espaciado más amplio */\n"
"    letter-spacing: 1.5px;  /* Espaciado entre letras más elegante */\n"
"    text-transform: capitalize;  /* Primera letra en mayúscula */\n"
"    text-align: center;  /* Centrar el texto */\n"
"  \n"
"}\n"
"")
        self.LabelNombre2.setObjectName("LabelNombre2")
        self.verticalLayout_2.addWidget(self.LabelNombre2)
        self.toolButton_3 = QtWidgets.QToolButton(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.toolButton_3.sizePolicy().hasHeightForWidth())
        self.toolButton_3.setSizePolicy(sizePolicy)
        self.toolButton_3.setMinimumSize(QtCore.QSize(200, 0))
        self.toolButton_3.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.toolButton_3.setStyleSheet("QToolButton {\n"
"    background-color: #6BA614;  /* Color de fondo */\n"
"    border-radius: 5px;  /* Bordes redondeados */\n"
"    padding: 5px 20px;  /* Espaciado, ajustado para el icono */\n"
"    font: bold 10px \"Montserrat\";  /* Fuente moderna */\n"
"    color: white;  /* Texto en blanco */\n"
"    border: none;  /* Sin borde */\n"
"    box-shadow: 3px 3px 8px rgba(0, 0, 0, 0.2);  /* Sombra sutil */\n"
"}\n"
"\n"
"")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("static/earth.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_3.setIcon(icon3)
        self.toolButton_3.setToolButtonStyle(QtCore.Qt.ToolButtonTextBesideIcon)
        self.toolButton_3.setObjectName("toolButton_3")
        self.verticalLayout_2.addWidget(self.toolButton_3)
        self.LabelDistribucion = QtWidgets.QLabel(self.frame)
        self.LabelDistribucion.setStyleSheet("QLabel {\n"
"    font: bold 10px \"Georgia\", serif;  /* Fuente aún más elegante y con mayor estilo */\n"
"    background-color: #B1D989;  /* Fondo más transparente */\n"
"    border: none;  /* Sin bordes en los lados */\n"
"    border-radius: 5px;  /* Bordes más suaves */\n"
"    color: #2b2b2b;  /* Color del texto */\n"
"    padding: 5px 15px;  /* Espaciado más amplio */\n"
"    letter-spacing: 1.5px;  /* Espaciado entre letras más elegante */\n"
"    text-transform: capitalize;  /* Primera letra en mayúscula */\n"
"    text-align: center;  /* Centrar el texto */\n"
"  \n"
"}\n"
"")
        self.LabelDistribucion.setObjectName("LabelDistribucion")
        self.verticalLayout_2.addWidget(self.LabelDistribucion)
        self.toolButton_4 = QtWidgets.QToolButton(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.toolButton_4.sizePolicy().hasHeightForWidth())
        self.toolButton_4.setSizePolicy(sizePolicy)
        self.toolButton_4.setMinimumSize(QtCore.QSize(200, 0))
        self.toolButton_4.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.toolButton_4.setStyleSheet("QToolButton {\n"
"    background-color: #6BA614;  /* Color de fondo */\n"
"    border-radius: 5px;  /* Bordes redondeados */\n"
"    padding: 5px 20px;  /* Espaciado, ajustado para el icono */\n"
"    font: bold 10px \"Montserrat\";  /* Fuente moderna */\n"
"    color: white;  /* Texto en blanco */\n"
"    border: none;  /* Sin borde */\n"
"    box-shadow: 3px 3px 8px rgba(0, 0, 0, 0.2);  /* Sombra sutil */\n"
"}\n"
"\n"
"")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("static/massage.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_4.setIcon(icon4)
        self.toolButton_4.setToolButtonStyle(QtCore.Qt.ToolButtonTextBesideIcon)
        self.toolButton_4.setObjectName("toolButton_4")
        self.verticalLayout_2.addWidget(self.toolButton_4)
        self.LabelFloracion = QtWidgets.QLabel(self.frame)
        self.LabelFloracion.setStyleSheet("QLabel {\n"
"    font: bold 10px \"Georgia\", serif;  /* Fuente aún más elegante y con mayor estilo */\n"
"    background-color: #B1D989;  /* Fondo más transparente */\n"
"    border: none;  /* Sin bordes en los lados */\n"
"    border-radius: 5px;  /* Bordes más suaves */\n"
"    color: #2b2b2b;  /* Color del texto */\n"
"    padding: 5px 15px;  /* Espaciado más amplio */\n"
"    letter-spacing: 1.5px;  /* Espaciado entre letras más elegante */\n"
"    text-transform: capitalize;  /* Primera letra en mayúscula */\n"
"    text-align: center;  /* Centrar el texto */\n"
"  \n"
"}\n"
"")
        self.LabelFloracion.setObjectName("LabelFloracion")
        self.verticalLayout_2.addWidget(self.LabelFloracion)
        self.toolButton_5 = QtWidgets.QToolButton(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.toolButton_5.sizePolicy().hasHeightForWidth())
        self.toolButton_5.setSizePolicy(sizePolicy)
        self.toolButton_5.setMinimumSize(QtCore.QSize(200, 0))
        self.toolButton_5.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.toolButton_5.setStyleSheet("QToolButton {\n"
"    background-color: #6BA614;  /* Color de fondo */\n"
"    border-radius: 5px;  /* Bordes redondeados */\n"
"    padding: 5px 20px;  /* Espaciado, ajustado para el icono */\n"
"    font: bold 10px \"Montserrat\";  /* Fuente moderna */\n"
"    color: white;  /* Texto en blanco */\n"
"    border: none;  /* Sin borde */\n"
"    box-shadow: 3px 3px 8px rgba(0, 0, 0, 0.2);  /* Sombra sutil */\n"
"}\n"
"\n"
"")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("static/chart-tree.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_5.setIcon(icon5)
        self.toolButton_5.setIconSize(QtCore.QSize(18, 14))
        self.toolButton_5.setToolButtonStyle(QtCore.Qt.ToolButtonTextBesideIcon)
        self.toolButton_5.setObjectName("toolButton_5")
        self.verticalLayout_2.addWidget(self.toolButton_5)
        self.LabelFamiia = QtWidgets.QLabel(self.frame)
        self.LabelFamiia.setStyleSheet("QLabel {\n"
"    font: bold 10px \"Georgia\", serif;  /* Fuente aún más elegante y con mayor estilo */\n"
"    background-color: #B1D989;  /* Fondo más transparente */\n"
"    border: none;  /* Sin bordes en los lados */\n"
"    border-radius: 5px;  /* Bordes más suaves */\n"
"    color: #2b2b2b;  /* Color del texto */\n"
"    padding: 5px 15px;  /* Espaciado más amplio */\n"
"    letter-spacing: 1.5px;  /* Espaciado entre letras más elegante */\n"
"    text-transform: capitalize;  /* Primera letra en mayúscula */\n"
"    text-align: center;  /* Centrar el texto */\n"
"  \n"
"}\n"
"")
        self.LabelFamiia.setObjectName("LabelFamiia")
        self.verticalLayout_2.addWidget(self.LabelFamiia)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem2)
        self.BtnSalir = QtWidgets.QPushButton(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.BtnSalir.sizePolicy().hasHeightForWidth())
        self.BtnSalir.setSizePolicy(sizePolicy)
        self.BtnSalir.setMinimumSize(QtCore.QSize(140, 25))
        self.BtnSalir.setMaximumSize(QtCore.QSize(140, 25))
        self.BtnSalir.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.BtnSalir.setStyleSheet("QPushButton {\n"
"    background-color: #6BA614;  /* Fondo más transparente */\n"
"    border-radius: 2px;  /* Bordes redondeados */\n"
"    padding: 5px 5px;  /* Espaciado interno */\n"
"    font: bold 12px \"Montserrat\";  /* Fuente moderna */\n"
"    color: white;  /* Texto en blanco */\n"
"    border: none;  /* Sin borde */\n"
"    box-shadow: 3px 3px 8px rgba(0, 0, 0, 0.2);  /* Sombra sutil */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #3A5A40;  /* Cambio de color al pasar el mouse */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #2C4A34;  /* Cambio de color al hacer clic */\n"
"    box-shadow: none;  /* Quita la sombra para efecto de presión */\n"
"}\n"
"")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("static/logout.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.BtnSalir.setIcon(icon6)
        self.BtnSalir.setObjectName("BtnSalir")
        self.verticalLayout_2.addWidget(self.BtnSalir, 0, QtCore.Qt.AlignHCenter)
        self.gridLayout.addWidget(self.frame, 0, 1, 1, 1)
        self.gridLayout_2.addWidget(self.gridFrame, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 838, 18))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.BtnSubir.setText(_translate("MainWindow", "Subir Imagen"))
        self.toolButton.setWhatsThis(_translate("MainWindow", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        self.toolButton.setText(_translate("MainWindow", "Nombre Común"))
        self.LabelNombre1.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt;\">TextLabel</span></p></body></html>"))
        self.toolButton_2.setText(_translate("MainWindow", "Nombre Cientifico"))
        self.LabelNombre2.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt;\">cipress</span></p></body></html>"))
        self.toolButton_3.setText(_translate("MainWindow", "Distribución Geografica"))
        self.LabelDistribucion.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt;\">TextLabel</span></p></body></html>"))
        self.toolButton_4.setText(_translate("MainWindow", "Floración"))
        self.LabelFloracion.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt;\">TextLabel</span></p></body></html>"))
        self.toolButton_5.setText(_translate("MainWindow", "Familia"))
        self.LabelFamiia.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt;\">TextLabel</span></p></body></html>"))
        self.BtnSalir.setText(_translate("MainWindow", "Salir"))
