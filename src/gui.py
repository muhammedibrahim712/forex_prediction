import pyqtgraph as pg
from PyQt5 import QtCore, QtGui, QtWidgets

class UiMainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 772)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/assets/logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("background-color: rgb(51, 51, 51);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.topHorizontalLayout = QtWidgets.QHBoxLayout()
        self.topHorizontalLayout.setObjectName("topHorizontalLayout")
        self.lineBeginDate = QtWidgets.QLineEdit(self.centralwidget)
        self.lineBeginDate.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineBeginDate.sizePolicy().hasHeightForWidth())
        self.lineBeginDate.setSizePolicy(sizePolicy)
        self.lineBeginDate.setMinimumSize(QtCore.QSize(64, 20))
        self.lineBeginDate.setMaximumSize(QtCore.QSize(96, 20))
        self.lineBeginDate.setAutoFillBackground(False)
        self.lineBeginDate.setStyleSheet("QLineEdit {\n"
"    background-color: rgb(34, 34, 34);\n"
"    color: rgb(227, 224, 224);\n"
"    border-color: none;\n"
"    padding: 4px;\n"
"}")
        self.lineBeginDate.setFrame(False)
        self.lineBeginDate.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.lineBeginDate.setObjectName("lineBeginDate")
        self.topHorizontalLayout.addWidget(self.lineBeginDate)
        self.btnBeginBrowser = QtWidgets.QPushButton(self.centralwidget)
        self.btnBeginBrowser.setMaximumSize(QtCore.QSize(20, 20))
        self.btnBeginBrowser.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/assets/calendar.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnBeginBrowser.setIcon(icon1)
        self.btnBeginBrowser.setFlat(True)
        self.btnBeginBrowser.setObjectName("btnBeginBrowser")
        self.topHorizontalLayout.addWidget(self.btnBeginBrowser)
        self.lineEndDate = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEndDate.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEndDate.sizePolicy().hasHeightForWidth())
        self.lineEndDate.setSizePolicy(sizePolicy)
        self.lineEndDate.setMinimumSize(QtCore.QSize(64, 20))
        self.lineEndDate.setMaximumSize(QtCore.QSize(96, 20))
        self.lineEndDate.setStyleSheet("QLineEdit {\n"
"    background-color: rgb(34, 34, 34);\n"
"    color: rgb(227, 224, 224);\n"
"    border-color: none;\n"
"    padding: 4px;\n"
"}")
        self.lineEndDate.setFrame(False)
        self.lineEndDate.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.lineEndDate.setReadOnly(False)
        self.lineEndDate.setPlaceholderText("")
        self.lineEndDate.setObjectName("lineEndDate")
        self.topHorizontalLayout.addWidget(self.lineEndDate)
        self.btnEndBrowser = QtWidgets.QPushButton(self.centralwidget)
        self.btnEndBrowser.setMaximumSize(QtCore.QSize(20, 20))
        self.btnEndBrowser.setText("")
        self.btnEndBrowser.setIcon(icon1)
        self.btnEndBrowser.setFlat(True)
        self.btnEndBrowser.setObjectName("btnEndBrowser")
        self.topHorizontalLayout.addWidget(self.btnEndBrowser)
        self.btnSetting = QtWidgets.QPushButton(self.centralwidget)
        self.btnSetting.setMinimumSize(QtCore.QSize(20, 20))
        self.btnSetting.setMaximumSize(QtCore.QSize(20, 20))
        self.btnSetting.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/assets/setting.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnSetting.setIcon(icon2)
        self.btnSetting.setFlat(True)
        self.btnSetting.setObjectName("btnSetting")
        self.topHorizontalLayout.addWidget(self.btnSetting)
        self.leftHeaderSpace = QtWidgets.QLabel(self.centralwidget)
        self.leftHeaderSpace.setText("")
        self.leftHeaderSpace.setObjectName("leftHeaderSpace")
        self.topHorizontalLayout.addWidget(self.leftHeaderSpace)
        self.tableFeed = QtWidgets.QTableWidget(self.centralwidget)
        self.tableFeed.setMinimumSize(QtCore.QSize(450, 40))
        self.tableFeed.setMaximumSize(QtCore.QSize(450, 40))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(150, 150, 150))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(150, 150, 150))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(150, 150, 150))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(150, 150, 150))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(150, 150, 150))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(150, 150, 150))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(150, 150, 150))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(150, 150, 150))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(150, 150, 150))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.tableFeed.setPalette(palette)
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.tableFeed.setFont(font)
        self.tableFeed.setAutoFillBackground(False)
        self.tableFeed.setStyleSheet("QTableWidget {\n"
"    background-color: rgb(0, 0, 0);\n"
"    gridline-color: rgb(26, 26, 26);\n"
"    border: 1px solid rgb(0, 0, 0);\n"
"    color: rgb(150, 150, 150);\n"
"}\n"
"\n"
"QHeaderView::section {\n"
"    spacing: 10px;\n"
"    background-color: rgb(34, 34, 34);\n"
"    border: 1px solid rgb(26, 26, 26);\n"
"    color: rgb(205, 97, 55);\n"
"}")
        self.tableFeed.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.tableFeed.setFrameShadow(QtWidgets.QFrame.Plain)
        self.tableFeed.setLineWidth(1)
        self.tableFeed.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.tableFeed.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.tableFeed.setAutoScroll(False)
        self.tableFeed.setGridStyle(QtCore.Qt.SolidLine)
        self.tableFeed.setCornerButtonEnabled(True)
        self.tableFeed.setRowCount(0)
        self.tableFeed.setObjectName("tableFeed")
        self.tableFeed.setColumnCount(5)
        item = QtWidgets.QTableWidgetItem()
        self.tableFeed.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableFeed.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableFeed.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableFeed.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableFeed.setHorizontalHeaderItem(4, item)
        self.tableFeed.horizontalHeader().setCascadingSectionResizes(True)
        self.tableFeed.horizontalHeader().setDefaultSectionSize(90)
        self.tableFeed.horizontalHeader().setMinimumSectionSize(60)
        self.tableFeed.horizontalHeader().setSortIndicatorShown(False)
        self.tableFeed.horizontalHeader().setStretchLastSection(True)
        self.tableFeed.verticalHeader().setVisible(False)
        self.tableFeed.verticalHeader().setDefaultSectionSize(20)
        self.tableFeed.verticalHeader().setMinimumSectionSize(20)
        self.topHorizontalLayout.addWidget(self.tableFeed)
        self.verticalLayout.addLayout(self.topHorizontalLayout)
        self.lblTradePanel = QtWidgets.QLabel(self.centralwidget)
        self.lblTradePanel.setEnabled(True)
        self.lblTradePanel.setMinimumSize(QtCore.QSize(0, 40))
        self.lblTradePanel.setMaximumSize(QtCore.QSize(16777215, 40))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(207, 103, 63))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(38, 38, 38))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(207, 103, 63))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(207, 103, 63))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(38, 38, 38))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(38, 38, 38))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(207, 103, 63))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(38, 38, 38))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(207, 103, 63))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(207, 103, 63))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(38, 38, 38))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(38, 38, 38))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(207, 103, 63))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(38, 38, 38))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(207, 103, 63))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(207, 103, 63))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(38, 38, 38))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(38, 38, 38))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.lblTradePanel.setPalette(palette)
        self.lblTradePanel.setAutoFillBackground(False)
        self.lblTradePanel.setStyleSheet("QLabel {\n"
"    background-color: rgb(38, 38, 38);\n"
"    color: rgb(207, 103, 63);\n"
"    border:none;\n"
"    padding: 4px\n"
"}")
        self.lblTradePanel.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.lblTradePanel.setFrameShadow(QtWidgets.QFrame.Plain)
        self.lblTradePanel.setObjectName("lblTradePanel")
        self.verticalLayout.addWidget(self.lblTradePanel)
        self.mediumHorizontalLayout = QtWidgets.QHBoxLayout()
        self.mediumHorizontalLayout.setObjectName("mediumHorizontalLayout")
        self.leftVerticalLayout = QtWidgets.QVBoxLayout()
        self.leftVerticalLayout.setSpacing(0)
        self.leftVerticalLayout.setObjectName("leftVerticalLayout")
        self.tabHistory = QtWidgets.QTabWidget(self.centralwidget)
        self.tabHistory.setStyleSheet("QTabWidget::pane {\n"
"    border-top: 2px solid #222222;\n"
"}\n"
"\n"
"QTabBar::tab {\n"
"    background-color: rgb(51, 51, 51);\n"
"    color: rgb(132, 130, 130);\n"
"}\n"
"\n"
"QTabBar::tab:selected {\n"
"    background: rgb(38, 38, 38);\n"
"}")
        self.tabHistory.setObjectName("tabHistory")
        self.tabHistoryDate = QtWidgets.QWidget()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabHistoryDate.sizePolicy().hasHeightForWidth())
        self.tabHistoryDate.setSizePolicy(sizePolicy)
        self.tabHistoryDate.setObjectName("tabHistoryDate")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.tabHistoryDate)
        self.verticalLayout_2.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayout_2.setContentsMargins(1, 1, 1, -1)
        self.verticalLayout_2.setSpacing(1)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.lblDateHistory = QtWidgets.QLabel(self.tabHistoryDate)
        self.lblDateHistory.setMinimumSize(QtCore.QSize(0, 20))
        self.lblDateHistory.setMaximumSize(QtCore.QSize(16777215, 20))
        self.lblDateHistory.setStyleSheet("QLabel {\n"
"    background-color: rgb(34, 34, 34);\n"
"    color: rgb(225, 225, 225);\n"
"    border: none;\n"
"}")
        self.lblDateHistory.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.lblDateHistory.setText("")
        self.lblDateHistory.setAlignment(QtCore.Qt.AlignCenter)
        self.lblDateHistory.setObjectName("lblDateHistory")
        self.verticalLayout_2.addWidget(self.lblDateHistory)
        self.tableHistory = QtWidgets.QTableWidget(self.tabHistoryDate)
        self.tableHistory.setMinimumSize(QtCore.QSize(0, 0))
        self.tableHistory.setStyleSheet("QTableWidget {\n"
"    background-color: rgb(0, 0, 0);\n"
"    gridline-color: rgb(26, 26, 26);\n"
"    border: 1px solid rgb(0, 0, 0);\n"
"    color: rgb(150, 150, 150);\n"
"}\n"
"\n"
"QScrollBar:horizontal, QScrollBar:verticall {\n"
"    background: #1c1c1c;\n"
"    height: 10px;\n"
"    width: 10px;\n"
"}\n"
"\n"
"QScrollBar:handle:horizontal, QScrollBar:handle:vertical {\n"
"    background-color: rgb(70, 70, 70);\n"
"}\n"
"\n"
"QHeaderView::section {\n"
"    spacing: 10px;\n"
"    background-color: rgb(34, 34, 34);\n"
"    border: 1px solid rgb(26, 26, 26);\n"
"    color: rgb(225, 225, 225);\n"
"    margin: 1px;\n"
"    font-family: arial;\n"
"    font-size:12px;\n"
"}")
        self.tableHistory.setObjectName("tableHistory")
        self.tableHistory.setColumnCount(10)
        self.tableHistory.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableHistory.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableHistory.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableHistory.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableHistory.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableHistory.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableHistory.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableHistory.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableHistory.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableHistory.setHorizontalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableHistory.setHorizontalHeaderItem(9, item)
        self.tableHistory.horizontalHeader().setCascadingSectionResizes(True)
        self.tableHistory.horizontalHeader().setDefaultSectionSize(100)
        self.tableHistory.horizontalHeader().setMinimumSectionSize(60)
        self.tableHistory.horizontalHeader().setSortIndicatorShown(False)
        self.tableHistory.verticalHeader().setCascadingSectionResizes(True)
        self.tableHistory.verticalHeader().setDefaultSectionSize(30)
        self.tableHistory.verticalHeader().setMinimumSectionSize(20)
        self.verticalLayout_2.addWidget(self.tableHistory)
        self.tabHistory.addTab(self.tabHistoryDate, "")
        self.tabHistoryFeed = QtWidgets.QWidget()
        self.tabHistoryFeed.setObjectName("tabHistoryFeed")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.tabHistoryFeed)
        self.horizontalLayout.setObjectName("horizontalLayout")
        # self.historyChart = QtWidgets.QGraphicsView(self.tabHistoryFeed)
        # self.scene = QtWidgets.QGraphicsScene(self.historyChart)
        # self.historyChart.setScene(self.scene)
        self.historyChart = pg.PlotWidget(self.tabHistoryFeed)
        self.historyChart.setStyleSheet("QGraphicsView {\n"
"    background-color: rgb(34, 34, 34);\n"
"    color: rgb(150, 150, 150);\n"
"    border: 1px solid rgb(12, 12, 12);\n"
"}")
        self.historyChart.setObjectName("historyChart")
        self.horizontalLayout.addWidget(self.historyChart)
        self.tabHistory.addTab(self.tabHistoryFeed, "")
        self.leftVerticalLayout.addWidget(self.tabHistory)
        self.tabTest = QtWidgets.QTabWidget(self.centralwidget)
        self.tabTest.setStyleSheet("QTabWidget::pane {\n"
"    border-top: 2px solid #222222;\n"
"}\n"
"\n"
"QTabBar::tab {\n"
"    background-color: rgb(51, 51, 51);\n"
"    color: rgb(132, 130, 130);\n"
"}\n"
"\n"
"QTabBar::tab:selected {\n"
"    background: rgb(38, 38, 38);\n"
"}")
        self.tabTest.setObjectName("tabTest")
        self.tabTestDate = QtWidgets.QWidget()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabTestDate.sizePolicy().hasHeightForWidth())
        self.tabTestDate.setSizePolicy(sizePolicy)
        self.tabTestDate.setObjectName("tabTestDate")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.tabTestDate)
        self.verticalLayout_3.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayout_3.setContentsMargins(1, 1, 1, -1)
        self.verticalLayout_3.setSpacing(1)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.lblDateTest = QtWidgets.QLabel(self.tabTestDate)
        self.lblDateTest.setMinimumSize(QtCore.QSize(0, 20))
        self.lblDateTest.setMaximumSize(QtCore.QSize(16777215, 20))
        self.lblDateTest.setStyleSheet("QLabel {\n"
"    background-color: rgb(34, 34, 34);\n"
"    color: rgb(225, 225, 225);\n"
"    border: none;\n"
"}")
        self.lblDateTest.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.lblDateTest.setText("")
        self.lblDateTest.setAlignment(QtCore.Qt.AlignCenter)
        self.lblDateTest.setObjectName("lblDateTest")
        self.verticalLayout_3.addWidget(self.lblDateTest)
        self.tableTest = QtWidgets.QTableWidget(self.tabTestDate)
        self.tableTest.setMinimumSize(QtCore.QSize(0, 0))
        self.tableTest.setStyleSheet("QTableWidget {\n"
"    background-color: rgb(0, 0, 0);\n"
"    gridline-color: rgb(26, 26, 26);\n"
"    border: 1px solid rgb(0, 0, 0);\n"
"    color: rgb(150, 150, 150);\n"
"}\n"
"\n"
"QScrollBar:horizontal, QScrollBar:verticall {\n"
"    background: #1c1c1c;\n"
"    height: 10px;\n"
"    width: 10px;\n"
"}\n"
"\n"
"QScrollBar:handle:horizontal, QScrollBar:handle:vertical {\n"
"    background-color: rgb(70, 70, 70);\n"
"}\n"
"\n"
"QHeaderView::section {\n"
"    spacing: 10px;\n"
"    background-color: rgb(34, 34, 34);\n"
"    border: 1px solid rgb(26, 26, 26);\n"
"    color: rgb(225, 225, 225);\n"
"    margin: 1px;\n"
"    font-family: arial;\n"
"    font-size:12px;\n"
"}")
        self.tableTest.setObjectName("tableTest")
        self.tableTest.setColumnCount(10)
        self.tableTest.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableTest.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableTest.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableTest.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableTest.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableTest.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableTest.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableTest.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableTest.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableTest.setHorizontalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableTest.setHorizontalHeaderItem(9, item)
        self.tableTest.horizontalHeader().setCascadingSectionResizes(True)
        self.tableTest.horizontalHeader().setMinimumSectionSize(60)
        self.tableTest.verticalHeader().setCascadingSectionResizes(True)
        self.tableTest.verticalHeader().setMinimumSectionSize(20)
        self.verticalLayout_3.addWidget(self.tableTest)
        self.tabTest.addTab(self.tabTestDate, "")
        self.tabTestGraph = QtWidgets.QWidget()
        self.tabTestGraph.setObjectName("tabTestGraph")
        self.tabTest.addTab(self.tabTestGraph, "")
        self.leftVerticalLayout.addWidget(self.tabTest)
        self.mediumHorizontalLayout.addLayout(self.leftVerticalLayout)
        self.rightVerticalLayout = QtWidgets.QVBoxLayout()
        self.rightVerticalLayout.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.rightVerticalLayout.setObjectName("rightVerticalLayout")
        self.cboSelect = QtWidgets.QComboBox(self.centralwidget)
        self.cboSelect.setMinimumSize(QtCore.QSize(88, 20))
        self.cboSelect.setMaximumSize(QtCore.QSize(100, 20))
        self.cboSelect.setStyleSheet("QComboBox {\n"
"    color: rgb(223, 155, 40);\n"
"    border: 1px solid rgb(34, 34, 34);\n"
"    border-radius: 3px;\n"
"    padding: 4px;\n"
"    min-width: 6em;\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"    border: 1px solid rgb(34, 34, 34);\n"
"\n"
"}\n"
"\n"
"QComboBox::down-arrow {\n"
"    image: url(:/assets/down.png);\n"
"}")
        self.cboSelect.setDuplicatesEnabled(False)
        self.cboSelect.setFrame(True)
        self.cboSelect.setObjectName("cboSelect")
        self.cboSelect.addItem("")
        self.rightVerticalLayout.addWidget(self.cboSelect)
        self.listSummaryHistory = QtWidgets.QListView(self.centralwidget)
        self.listSummaryHistory.setMinimumSize(QtCore.QSize(100, 0))
        self.listSummaryHistory.setMaximumSize(QtCore.QSize(100, 16777215))
        self.listSummaryHistory.setStyleSheet("QListView {\n"
"    background-color: rgb(34, 34, 34);\n"
"    color: rgb(150, 150, 150);\n"
"    border: 1px solid rgb(12, 12, 12);\n"
"}")
        self.listSummaryHistory.setObjectName("listSummaryHistory")
        self.rightVerticalLayout.addWidget(self.listSummaryHistory)
        self.listSummaryTest = QtWidgets.QListView(self.centralwidget)
        self.listSummaryTest.setMinimumSize(QtCore.QSize(100, 0))
        self.listSummaryTest.setMaximumSize(QtCore.QSize(100, 16777215))
        self.listSummaryTest.setStyleSheet("QListView {\n"
"    background-color: rgb(34, 34, 34);\n"
"    color: rgb(150, 150, 150);\n"
"    border: 1px solid rgb(12, 12, 12);\n"
"}")
        self.listSummaryTest.setObjectName("listSummaryTest")
        self.rightVerticalLayout.addWidget(self.listSummaryTest)
        self.mediumHorizontalLayout.addLayout(self.rightVerticalLayout)
        self.verticalLayout.addLayout(self.mediumHorizontalLayout)
        self.connectionCredential = QtWidgets.QHBoxLayout()
        self.connectionCredential.setObjectName("connectionCredential")
        self.btnConnectionLog = QtWidgets.QPushButton(self.centralwidget)
        self.btnConnectionLog.setMinimumSize(QtCore.QSize(128, 20))
        self.btnConnectionLog.setMaximumSize(QtCore.QSize(128, 20))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.btnConnectionLog.setFont(font)
        self.btnConnectionLog.setStyleSheet("QPushButton {\n"
"    color: rgb(223, 155, 40);\n"
"    background-color: rgb(70, 70, 70);\n"
"    border-radius: 6px;\n"
"}")
        self.btnConnectionLog.setFlat(False)
        self.btnConnectionLog.setObjectName("btnConnectionLog")
        self.connectionCredential.addWidget(self.btnConnectionLog)
        self.txtPassword = QtWidgets.QLineEdit(self.centralwidget)
        self.txtPassword.setMinimumSize(QtCore.QSize(0, 0))
        self.txtPassword.setMaximumSize(QtCore.QSize(128, 20))
        self.txtPassword.setStyleSheet("QLineEdit {\n"
"    background-color: rgb(34, 34, 34);\n"
"    color: rgb(150, 150, 150);\n"
"    border-radius: 6px;\n"
"    padding: 5px;\n"
"}")
        self.txtPassword.setEchoMode(QtWidgets.QLineEdit.Password)
        self.txtPassword.setObjectName("txtPassword")
        self.connectionCredential.addWidget(self.txtPassword)
        self.bottomSpace = QtWidgets.QLabel(self.centralwidget)
        self.bottomSpace.setMinimumSize(QtCore.QSize(0, 20))
        self.bottomSpace.setMaximumSize(QtCore.QSize(16777215, 20))
        self.bottomSpace.setText("")
        self.bottomSpace.setObjectName("bottomSpace")
        self.connectionCredential.addWidget(self.bottomSpace)
        self.verticalLayout.addLayout(self.connectionCredential)
        self.bottomHorizontalGroup = QtWidgets.QHBoxLayout()
        self.bottomHorizontalGroup.setObjectName("bottomHorizontalGroup")
        self.bottomLogGroup = QtWidgets.QVBoxLayout()
        self.bottomLogGroup.setSpacing(0)
        self.bottomLogGroup.setObjectName("bottomLogGroup")
        self.bottomHeader = QtWidgets.QHBoxLayout()
        self.bottomHeader.setSpacing(6)
        self.bottomHeader.setObjectName("bottomHeader")
        self.lblBroker = QtWidgets.QLabel(self.centralwidget)
        self.lblBroker.setMinimumSize(QtCore.QSize(102, 20))
        self.lblBroker.setMaximumSize(QtCore.QSize(102, 20))
        self.lblBroker.setStyleSheet("QLabel {\n"
"    color: rgb(223, 155, 40);\n"
"    background-color: rgb(70, 70, 70);\n"
"    border-radius: 4px;\n"
"}")
        self.lblBroker.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.lblBroker.setAlignment(QtCore.Qt.AlignCenter)
        self.lblBroker.setObjectName("lblBroker")
        self.bottomHeader.addWidget(self.lblBroker)
        self.statusIndicator = QtWidgets.QPushButton(self.centralwidget)
        self.statusIndicator.setMinimumSize(QtCore.QSize(20, 20))
        self.statusIndicator.setMaximumSize(QtCore.QSize(20, 20))
        self.statusIndicator.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/assets/red.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.statusIndicator.setIcon(icon3)
        self.statusIndicator.setFlat(True)
        self.statusIndicator.setObjectName("statusIndicator")
        self.bottomHeader.addWidget(self.statusIndicator)
        self.cboType = QtWidgets.QComboBox(self.centralwidget)
        self.cboType.setEnabled(True)
        self.cboType.setMinimumSize(QtCore.QSize(88, 20))
        self.cboType.setMaximumSize(QtCore.QSize(104, 20))
        self.cboType.setStyleSheet("QComboBox {\n"
"    color: rgb(223, 155, 40);\n"
"    border: 1px solid rgb(34, 34, 34);\n"
"    border-radius: 3px;\n"
"    padding: 4px;\n"
"    min-width: 6em;\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"    border: 1px solid rgb(34, 34, 34);\n"
"\n"
"}\n"
"\n"
"QComboBox::down-arrow {\n"
"    image: url(:/assets/down.png);\n"
"}")
        self.cboType.setFrame(True)
        self.cboType.setObjectName("cboType")
        self.cboType.addItem("")
        self.cboType.addItem("")
        self.bottomHeader.addWidget(self.cboType)
        self.btnConfig = QtWidgets.QPushButton(self.centralwidget)
        self.btnConfig.setMinimumSize(QtCore.QSize(20, 20))
        self.btnConfig.setMaximumSize(QtCore.QSize(20, 20))
        self.btnConfig.setText("")
        self.btnConfig.setIcon(icon2)
        self.btnConfig.setFlat(True)
        self.btnConfig.setObjectName("btnConfig")
        self.bottomHeader.addWidget(self.btnConfig)
        self.lblBeginDate = QtWidgets.QLineEdit(self.centralwidget)
        self.lblBeginDate.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lblBeginDate.sizePolicy().hasHeightForWidth())
        self.lblBeginDate.setSizePolicy(sizePolicy)
        self.lblBeginDate.setMinimumSize(QtCore.QSize(64, 20))
        self.lblBeginDate.setMaximumSize(QtCore.QSize(96, 20))
        self.lblBeginDate.setAutoFillBackground(False)
        self.lblBeginDate.setStyleSheet("QLineEdit {\n"
"    background-color: rgb(34, 34, 34);\n"
"    color: rgb(227, 224, 224);\n"
"    border-color: none;\n"
"    padding: 4px;\n"
"}")
        self.lblBeginDate.setFrame(False)
        self.lblBeginDate.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lblBeginDate.setObjectName("lblBeginDate")
        self.bottomHeader.addWidget(self.lblBeginDate)
        self.btnLogBeginBrowser = QtWidgets.QPushButton(self.centralwidget)
        self.btnLogBeginBrowser.setMaximumSize(QtCore.QSize(20, 20))
        self.btnLogBeginBrowser.setText("")
        self.btnLogBeginBrowser.setIcon(icon1)
        self.btnLogBeginBrowser.setFlat(True)
        self.btnLogBeginBrowser.setObjectName("btnLogBeginBrowser")
        self.bottomHeader.addWidget(self.btnLogBeginBrowser)
        self.lblEndDate = QtWidgets.QLineEdit(self.centralwidget)
        self.lblEndDate.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lblEndDate.sizePolicy().hasHeightForWidth())
        self.lblEndDate.setSizePolicy(sizePolicy)
        self.lblEndDate.setMinimumSize(QtCore.QSize(64, 20))
        self.lblEndDate.setMaximumSize(QtCore.QSize(96, 20))
        self.lblEndDate.setStyleSheet("QLineEdit {\n"
"    background-color: rgb(34, 34, 34);\n"
"    color: rgb(227, 224, 224);\n"
"    border-color: none;\n"
"    padding: 4px;\n"
"}")
        self.lblEndDate.setFrame(False)
        self.lblEndDate.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lblEndDate.setReadOnly(False)
        self.lblEndDate.setPlaceholderText("")
        self.lblEndDate.setObjectName("lblEndDate")
        self.bottomHeader.addWidget(self.lblEndDate)
        self.btnLogEndBrowser = QtWidgets.QPushButton(self.centralwidget)
        self.btnLogEndBrowser.setMaximumSize(QtCore.QSize(20, 20))
        self.btnLogEndBrowser.setText("")
        self.btnLogEndBrowser.setIcon(icon1)
        self.btnLogEndBrowser.setFlat(True)
        self.btnLogEndBrowser.setObjectName("btnLogEndBrowser")
        self.bottomHeader.addWidget(self.btnLogEndBrowser)
        self.typeSpace = QtWidgets.QLabel(self.centralwidget)
        self.typeSpace.setMinimumSize(QtCore.QSize(0, 20))
        self.typeSpace.setMaximumSize(QtCore.QSize(16777215, 20))
        self.typeSpace.setText("")
        self.typeSpace.setObjectName("typeSpace")
        self.bottomHeader.addWidget(self.typeSpace)
        self.bottomLogGroup.addLayout(self.bottomHeader)
        self.tableLog = QtWidgets.QTableWidget(self.centralwidget)
        self.tableLog.setMaximumSize(QtCore.QSize(16777215, 72))
        self.tableLog.setStyleSheet("QTableWidget {\n"
"    background-color: rgb(0, 0, 0);\n"
"    gridline-color: rgb(26, 26, 26);\n"
"    border: 1px solid rgb(51, 51, 51);\n"
"}\n"
"\n"
"QScrollBar:horizontal, QScrollBar:verticall {\n"
"    background: #1c1c1c;\n"
"    height: 10px;\n"
"    width: 10px;\n"
"}\n"
"\n"
"QScrollBar:handle:horizontal, QScrollBar:handle:vertical {\n"
"    background-color: rgb(70, 70, 70);\n"
"}")
        self.tableLog.setObjectName("tableLog")
        self.tableLog.setColumnCount(0)
        self.tableLog.setRowCount(0)
        self.bottomLogGroup.addWidget(self.tableLog)
        self.bottomHorizontalGroup.addLayout(self.bottomLogGroup)
        self.bottomButtonGroup = QtWidgets.QVBoxLayout()
        self.bottomButtonGroup.setObjectName("bottomButtonGroup")
        self.buttonSpace = QtWidgets.QLabel(self.centralwidget)
        self.buttonSpace.setMinimumSize(QtCore.QSize(80, 0))
        self.buttonSpace.setMaximumSize(QtCore.QSize(80, 16777215))
        self.buttonSpace.setText("")
        self.buttonSpace.setObjectName("buttonSpace")
        self.bottomButtonGroup.addWidget(self.buttonSpace)
        self.btnTest = QtWidgets.QPushButton(self.centralwidget)
        self.btnTest.setMinimumSize(QtCore.QSize(80, 20))
        self.btnTest.setMaximumSize(QtCore.QSize(80, 20))
        self.btnTest.setStyleSheet("QPushButton {\n"
"    border: 0px;\n"
"    border-radius: 4px;\n"
"    color: rgb(223, 155, 40);\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"        stop: 0 #424242, stop: 1 #363636);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"        stop: 0 #363636, stop: 1 #424242);\n"
"}")
        self.btnTest.setObjectName("btnTest")
        self.bottomButtonGroup.addWidget(self.btnTest)
        self.btnChart = QtWidgets.QPushButton(self.centralwidget)
        self.btnChart.setMinimumSize(QtCore.QSize(80, 20))
        self.btnChart.setMaximumSize(QtCore.QSize(80, 20))
        self.btnChart.setStyleSheet("QPushButton {\n"
"    border: 0px;\n"
"    border-radius: 4px;\n"
"    color: rgb(223, 155, 40);\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"        stop: 0 #424242, stop: 1 #363636);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"        stop: 0 #363636, stop: 1 #424242);\n"
"}")
        self.btnChart.setObjectName("btnChart")
        self.bottomButtonGroup.addWidget(self.btnChart)
        self.outputFormat = QtWidgets.QGroupBox(self.centralwidget)
        self.outputFormat.setMinimumSize(QtCore.QSize(80, 20))
        self.outputFormat.setMaximumSize(QtCore.QSize(80, 20))
        self.outputFormat.setStyleSheet("QGroupBox {\n"
"    border: 1px solid rgb(70, 70, 70);\n"
"    border-radius: 4px;\n"
"}")
        self.outputFormat.setTitle("")
        self.outputFormat.setObjectName("outputFormat")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.outputFormat)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.btnTxt = QtWidgets.QPushButton(self.outputFormat)
        self.btnTxt.setMinimumSize(QtCore.QSize(20, 20))
        self.btnTxt.setMaximumSize(QtCore.QSize(20, 20))
        self.btnTxt.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/assets/txt.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnTxt.setIcon(icon4)
        self.btnTxt.setFlat(True)
        self.btnTxt.setObjectName("btnTxt")
        self.horizontalLayout_2.addWidget(self.btnTxt)
        self.btnPdf = QtWidgets.QPushButton(self.outputFormat)
        self.btnPdf.setMinimumSize(QtCore.QSize(20, 20))
        self.btnPdf.setMaximumSize(QtCore.QSize(20, 20))
        self.btnPdf.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/assets/pdf.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnPdf.setIcon(icon5)
        self.btnPdf.setFlat(True)
        self.btnPdf.setObjectName("btnPdf")
        self.horizontalLayout_2.addWidget(self.btnPdf)
        self.btnXls = QtWidgets.QPushButton(self.outputFormat)
        self.btnXls.setMinimumSize(QtCore.QSize(20, 20))
        self.btnXls.setMaximumSize(QtCore.QSize(20, 20))
        self.btnXls.setText("")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/assets/xls.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnXls.setIcon(icon6)
        self.btnXls.setFlat(True)
        self.btnXls.setObjectName("btnXls")
        self.horizontalLayout_2.addWidget(self.btnXls)
        self.bottomButtonGroup.addWidget(self.outputFormat)
        self.bottomHorizontalGroup.addLayout(self.bottomButtonGroup)
        self.verticalLayout.addLayout(self.bottomHorizontalGroup)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setMaximumSize(QtCore.QSize(16777215, 20))
        self.statusbar.setStyleSheet("QStatusBar {\n"
"    color: rgb(255, 255, 255);\n"
"}")
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabHistory.setCurrentIndex(1)
        self.tabTest.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Forex Live Feed"))
        self.lineBeginDate.setText(_translate("MainWindow", "BEGIN DATE"))
        self.lineEndDate.setText(_translate("MainWindow", "END DATE"))
        item = self.tableFeed.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "SYMBOL"))
        item = self.tableFeed.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "TIME"))
        item = self.tableFeed.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "BID"))
        item = self.tableFeed.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "ASK"))
        item = self.tableFeed.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "SPREAD"))
        self.lblTradePanel.setText(_translate("MainWindow", "TRADES"))
        item = self.tableHistory.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "ORDER"))
        item = self.tableHistory.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "SYMBOL"))
        item = self.tableHistory.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "TIME IN"))
        item = self.tableHistory.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "PRICE IN"))
        item = self.tableHistory.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "TIME OUT"))
        item = self.tableHistory.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "PRICE OUT"))
        item = self.tableHistory.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "REASON"))
        item = self.tableHistory.horizontalHeaderItem(7)
        item.setText(_translate("MainWindow", "LOTS"))
        item = self.tableHistory.horizontalHeaderItem(8)
        item.setText(_translate("MainWindow", "COMMISSION"))
        item = self.tableHistory.horizontalHeaderItem(9)
        item.setText(_translate("MainWindow", "PROFIT"))
        self.tabHistory.setTabText(self.tabHistory.indexOf(self.tabHistoryDate), _translate("MainWindow", "SHOW DATE RANGE"))
        self.tabHistory.setTabText(self.tabHistory.indexOf(self.tabHistoryFeed), _translate("MainWindow", "LIVE FEED"))
        item = self.tableTest.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "ORDER"))
        item = self.tableTest.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "SYMBOL"))
        item = self.tableTest.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "TIME IN"))
        item = self.tableTest.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "PRICE IN"))
        item = self.tableTest.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "TIME OUT"))
        item = self.tableTest.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "PRICE OUT"))
        item = self.tableTest.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "REASON"))
        item = self.tableTest.horizontalHeaderItem(7)
        item.setText(_translate("MainWindow", "LOTS"))
        item = self.tableTest.horizontalHeaderItem(8)
        item.setText(_translate("MainWindow", "COMMISSION"))
        item = self.tableTest.horizontalHeaderItem(9)
        item.setText(_translate("MainWindow", "PROFIT"))
        self.tabTest.setTabText(self.tabTest.indexOf(self.tabTestDate), _translate("MainWindow", "SHOW DATE RANGE"))
        self.tabTest.setTabText(self.tabTest.indexOf(self.tabTestGraph), _translate("MainWindow", "NONE"))
        self.cboSelect.setItemText(0, _translate("MainWindow", "SELECT"))
        self.btnConnectionLog.setText(_translate("MainWindow", "CONNECTION LOG"))
        self.lblBroker.setText(_translate("MainWindow", "BROKER"))
        self.cboType.setCurrentText(_translate("MainWindow", "LIVE FEED"))
        self.cboType.setItemText(0, _translate("MainWindow", "LIVE FEED"))
        self.cboType.setItemText(1, _translate("MainWindow", "BACK TEST"))
        self.lblBeginDate.setText(_translate("MainWindow", "BEGIN DATE"))
        self.lblEndDate.setText(_translate("MainWindow", "END DATE"))
        self.btnTest.setText(_translate("MainWindow", "TEST"))
        self.btnChart.setText(_translate("MainWindow", "CHART"))

import resource

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = UiMainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

