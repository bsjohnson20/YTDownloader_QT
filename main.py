import random


from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_YTDownloader(object):
    def setupUi(self, YTDownloader):
        if not YTDownloader.objectName():
            YTDownloader.setObjectName(u"YTDownloader")
        YTDownloader.resize(800, 600)
        self.openDB = QAction(YTDownloader)
        self.openDB.setObjectName(u"openDB")
        self.actionExportDB = QAction(YTDownloader)
        self.actionExportDB.setObjectName(u"actionExportDB")
        self.actionSettings = QAction(YTDownloader)
        self.actionSettings.setObjectName(u"actionSettings")
        self.actionYT_video = QAction(YTDownloader)
        self.actionYT_video.setObjectName(u"actionYT_video")
        self.actionYT_Video_s = QAction(YTDownloader)
        self.actionYT_Video_s.setObjectName(u"actionYT_Video_s")
        self.actionView_Items = QAction(YTDownloader)
        self.actionView_Items.setObjectName(u"actionView_Items")
        self.actionDelete_Items = QAction(YTDownloader)
        self.actionDelete_Items.setObjectName(u"actionDelete_Items")
        self.actionTest1 = QAction(YTDownloader)
        self.actionTest1.setObjectName(u"actionTest1")
        self.actionTest2 = QAction(YTDownloader)
        self.actionTest2.setObjectName(u"actionTest2")
        self.actionDownloader = QAction(YTDownloader)
        self.actionDownloader.setObjectName(u"actionDownloader")
        self.centralwidget = QWidget(YTDownloader)
        self.centralwidget.setObjectName(u"centralwidget")
        self.tableView = QTableView(self.centralwidget)
        self.tableView.setObjectName(u"tableView")
        self.tableView.setGeometry(QRect(0, 0, 801, 541))
        YTDownloader.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(YTDownloader)
        self.statusbar.setObjectName(u"statusbar")
        YTDownloader.setStatusBar(self.statusbar)
        self.menubar = QMenuBar(YTDownloader)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 30))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        self.menuAction = QMenu(self.menubar)
        self.menuAction.setObjectName(u"menuAction")
        self.menuDatabase = QMenu(self.menubar)
        self.menuDatabase.setObjectName(u"menuDatabase")
        self.menuTesting = QMenu(self.menubar)
        self.menuTesting.setObjectName(u"menuTesting")
        self.menuViews = QMenu(self.menubar)
        self.menuViews.setObjectName(u"menuViews")
        YTDownloader.setMenuBar(self.menubar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuAction.menuAction())
        self.menubar.addAction(self.menuDatabase.menuAction())
        self.menubar.addAction(self.menuTesting.menuAction())
        self.menubar.addAction(self.menuViews.menuAction())
        self.menuFile.addAction(self.openDB)
        self.menuFile.addAction(self.actionExportDB)
        self.menuFile.addAction(self.actionSettings)
        self.menuAction.addAction(self.actionYT_video)
        self.menuAction.addAction(self.actionYT_Video_s)
        self.menuDatabase.addAction(self.actionView_Items)
        self.menuDatabase.addAction(self.actionDelete_Items)
        self.menuTesting.addAction(self.actionTest1)
        self.menuTesting.addAction(self.actionTest2)
        self.menuViews.addSeparator()
        self.menuViews.addAction(self.actionDownloader)

        self.retranslateUi(YTDownloader)

        QMetaObject.connectSlotsByName(YTDownloader)
    # setupUi

    def retranslateUi(self, YTDownloader):
        YTDownloader.setWindowTitle(QCoreApplication.translate("YTDownloader", u"Luna's YT Downloader", None))
        self.openDB.setText(QCoreApplication.translate("YTDownloader", u"Open DB file", None))
        self.actionExportDB.setText(QCoreApplication.translate("YTDownloader", u"Export DB file", None))
        self.actionSettings.setText(QCoreApplication.translate("YTDownloader", u"Settings", None))
        self.actionYT_video.setText(QCoreApplication.translate("YTDownloader", u"YT Video", None))
        self.actionYT_Video_s.setText(QCoreApplication.translate("YTDownloader", u"YT Video(s)", None))
        self.actionView_Items.setText(QCoreApplication.translate("YTDownloader", u"View Items", None))
        self.actionDelete_Items.setText(QCoreApplication.translate("YTDownloader", u"Delete Items", None))
        self.actionTest1.setText(QCoreApplication.translate("YTDownloader", u"Test1", None))
        self.actionTest2.setText(QCoreApplication.translate("YTDownloader", u"Test2", None))
        self.actionDownloader.setText(QCoreApplication.translate("YTDownloader", u"Downloader", None))
        self.menuFile.setTitle(QCoreApplication.translate("YTDownloader", u"File", None))
        self.menuAction.setTitle(QCoreApplication.translate("YTDownloader", u"Add", None))
        self.menuDatabase.setTitle(QCoreApplication.translate("YTDownloader", u"Database", None))
        self.menuTesting.setTitle(QCoreApplication.translate("YTDownloader", u"Testing", None))
        self.menuViews.setTitle(QCoreApplication.translate("YTDownloader", u"Views", None))
    # retranslateUi
    
        # run printme on actionDownloader
        self.actionDownloader.triggered.connect(self.printme)
        
        # open file dialog for openDB
        self.openDB.triggered.connect(self.openingDB)
        
        # Export DB
        self.actionExportDB.triggered.connect(self.ExportDB)
        
        # test
        self.actionTest1.triggered.connect(self.test)
    
    def printme(self):
        # file dialog popup
        filename = QFileDialog.getOpenFileName()
        print(filename)
        
    def ExportDB(self):
        # file dialog popup
        filename = QFileDialog.getSaveFileName()
        
        if not filename[0]:
            return
        
        print(filename)
        
        # loop through table and write to file
        with open(filename[0], 'w+') as f:
            # get row count
            rowCount = self.tableView.model().rowCount()
            
            for i in range(rowCount):
                name = self.model.item(i, 0).text()
                channel = self.model.item(i, 1).text()
                duration = self.model.item(i, 2).text()
                url = self.model.item(i, 3).text()
                status = self.model.item(i, 4).text()
                
                f.write(f"{name},{channel},{duration},{url},{status}\n")
        
        
        
        
    def openingDB(self):
        # file dialog popup
        filename = QFileDialog.getOpenFileName()
        print(filename) 
        
    def test(self):
        # generate 50 rows of name, channel, duration, url
        for i in range(50):
            name = "Name" + str(i)
            channel = "Channel" + str(i)
            duration = random.randint(1, 1000)
            url = "https://www.youtube.com/watch?v=" + str(random.randint(1000, 9999))
            # print(name, channel, duration, url)
        # insert into table
        
        self.model = QStandardItemModel(50, 4)
        self.model.setHorizontalHeaderLabels(['Name', 'Channel', 'Duration', 'URL'])
        self.tableView.setModel(self.model)
        for i in range(50):
            self.model.setItem(i, 0, QStandardItem("Name" + str(i)))
            self.model.setItem(i, 1, QStandardItem("Channel" + str(i)))
            self.model.setItem(i, 2, QStandardItem(str(random.randint(1, 1000))))
            self.model.setItem(i, 3, QStandardItem("https://www.youtube.com/watch?v=" + str(random.randint(1000, 9999))))
            self.model.setItem(i, 4, QStandardItem("Not Downloaded"))
            
            
            
            # Add trigger for url to open in browser
            # self.tableView.doubleClicked.connect(self.openURL)
        # disable editing
        self.tableView.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableView.resizeColumnsToContents()
        self.tableView.resizeRowsToContents()
        self.tableView.show()
        
        print("TEST")
        

            
        
        
        
        
        

    
if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    YTDownloader = QMainWindow()
    ui = Ui_YTDownloader()
    ui.setupUi(YTDownloader)
    YTDownloader.show()
    sys.exit(app.exec_())
 