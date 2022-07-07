# import socket
#
# import pickle
#
# HEADER=64
# DISCONNECT_MESSAGE='DISCONNECT'
# s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# def creat_column(name,to):
#     return f'create column {name} to ahmed.{to};'
# def send(msg):
#     message=msg.encode('utf-8')
#     msg_len=len(message)
#     send_length=str(msg_len).encode('utf-8')
#
#     send_length+=b' ' * (HEADER -len(send_length))
#     s.send(send_length)
#     s.send(message)
#
# def recv_msg(conn):
#     msg_length=conn.recv(64).decode('utf-8')
#     if msg_length:
#         msg_length=int(msg_length)
#         return conn.recv(msg_length).decode('utf-8')
#     else:
#         return False
# #creat=creat_column(str(input()),str(input()))
#
#
#
# def sql(conn):
#     while True:
#         se = str(input('sql>'))
#         if se == 'exit':
#             send('exit')
#             conn.close()
#             break
#
#         send(se)
#         print(recv_msg(conn))
#
#
#
#
#
# def start():
#     s.connect((socket.gethostname(), 1515))
#
#
#
#     while True:
#
#         f_msg = recv_msg(s)
#
#         if f_msg=='login':
#
#             send("{'user':'root','pass':'beta','db':'ahmed'}")
#         elif f_msg =='sql':
#             sql(s)
#         elif f_msg =='exit':
#             s.close()
#
#
# start()

#####################################################################













# from PyQt5.QtWidgets import *
# from PyQt5.QtGui import *
# from PyQt5.QtCore import *
# import tkinter
# import sys



# class MyApp(QWidget):
#     qdw = QDesktopWidget()
#     s = qdw.screen()
#     layout=None
#     def __init__(self):
#         super.__init__()
#         self.windowWidth,self.windowHeight=int(self.s.width()/1.5),int(self.s.height()/1.5)
#         self.setMinimumSize(self.windowWidth,self.windowHeight)
#         self.setWindowTitle('Beta Sql')
#         layout=QVBoxLayout()
#         self.setLayout(layout)
#
#         self.editorCommand=QPlainTextEdit()
#         self.layout.addWidget(self.editorCommand)
#
#         self.editorOutput=QPlainTextEdit()
#         self.layout.addWidget(self.editorOutput)
#
#         buttonLayout=QBoxLayout()
#         self.layout.addLayout(buttonLayout)
#
#         self.buttonRun=QPushButton("Run Command")
#         buttonLayout.addWidget(self.buttonRun)
#         self.buttenClearn=QPushButton("clear")
#         buttonLayout.addLayout(self.buttenClearn)
#
#
#
#
#
# if __name__ =="__main__":
#     app = QApplication(sys.argv)
#     myApp=MyApp()
#     myApp.show()
#     sys.exit( app.exec_())
import random
import sys
import os


from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

#



# class MyApp(QWidget):
#     def __init__(self):
#         super().__init__()
#         self.window_width, self.window_height = 1000, 700
#         self.resize(self.window_width, self.window_height)
#
#         self.setWindowTitle('Command Line App')
#         layout = QVBoxLayout()
#         self.setLayout(layout)
#
#         self.editorCommand = QPlainTextEdit()
#
#
#
#
#         self.editorCommand.appendPlainText('aljladsfasdfsdklfjklasdjfklasdfasdf')
#         layout.addWidget(self.editorCommand, 3)
#
#         self.editorOutput = QPlainTextEdit()
#
#         self.editorOutput.setTextInteractionFlags ((Qt.LinksAccessibleByKeyboard
#                                     | Qt.LinksAccessibleByMouse
#                                     | Qt.TextBrowserInteraction
#                                     | Qt.TextSelectableByKeyboard
#                                     | Qt.TextSelectableByMouse))
#
#
#
#
#         layout.addWidget(self.editorOutput, 7)
#
#         buttonLayout = QHBoxLayout()
#         layout.addLayout(buttonLayout)
#
#         self.button_run = QPushButton('&Run Command', clicked=self.runCommand)
#         buttonLayout.addWidget(self.button_run)
#
#         self.button_clear = QPushButton('&Clear', clicked=lambda: self.editorOutput.clear())
#         buttonLayout.addWidget(self.button_clear)
#
#         # self.editorCommand.insertPlainText('dir')
#
#     def runCommand(self):
#         command_line = self.editorCommand.toPlainText().strip()
#         p = os.popen(command_line)
#         if p:
#             self.editorOutput.clear()
#             output = p.read()
#             self.editorOutput.insertPlainText(output)
# class MyWin(QMainWindow):
#     def __init__(self, df):
#         super().__init__()
#
#         centralWidget = QWidget()
#         self.setCentralWidget(centralWidget)
#         layout = QGridLayout(centralWidget)
#
#         self.tableWidget = self.build_table(df)
#
#         self.tableWidget.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)      # <---
#
#         self.tableWidget.setAlternatingRowColors(True)
#         self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
#
#         layout.addWidget(self.tableWidget)
#         layout.addWidget(QPushButton("Button"))
#
#     def build_table(self, df):
#
#         table = QTableWidget()
#         table.setColumnCount(len(df.columns))
#         table.setRowCount(len(df.index))
#         table.setHorizontalHeaderLabels(df.columns)
#
#         for row_num, row in enumerate(df.index):
#             for col_num, col in enumerate(df.columns):
#                 item = QTableWidgetItem(str(df.loc[row,col]))
#
#                 table.setItem(row_num, col_num, item)                              # +++
#
#                 item.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
#
#         table.resizeColumnsToContents()
#         table.resizeRowsToContents()
#         table.verticalHeader().setVisible(False)
# #        self.table.setSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)        # ---
#
#         return table                                                               # +++
#
#
# df = pd.DataFrame(
#     {'a': ['1','2','3','4','Mary','Jim','John'], 'b': ['3','4','1','2',100, 200, 300], 'c': ['1','2','3','4','a','b','c'],
#      'd': ['1','2','3','4','Mary','Jim','John'], 'e': ['1','2','3','4',100, 200, 300], 'f': ['1','2','3','4','a','b','c'],
#      'g': ['1','2','3','4','Mary','Jim','John'], 'h': ['1','2','3','4',100, 200, 300], 'j': ['1','2','3','4','a','b','c'],
#      'k': ['1','2','3','4','Mary','Jim','John'], 'l': ['1','2','3','4',100, 200, 300], 'm': ['1','2','3','4','a','b','c'],
#     })

# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     w = MyWin(df)
#     w.show()
#     sys.exit(app.exec_())

from te_cont import connect
import socket
import ast




class MainWindow(QMainWindow):
    DB_Cursor= None

    DB_Cursor1 = None
    login = False
    fl=None
    def __init__(self):
        # super().__init__()
        super(MainWindow, self).__init__()


        self.setWindowTitle("My App")

        self.window_width, self.window_height = 1000, 700
        self.resize(self.window_width, self.window_height)
        toolbar = QToolBar("My main toolbar")
        toolbar.setIconSize(QSize(24, 25))
        self.addToolBar(toolbar)

        button_action = QAction(QIcon("bullet.png"), "&Your button", self)


        button_action.triggered.connect(self.onMyToolBarButtonClick)
        toolbar.addAction(button_action)










        menu = self.menuBar()

        file_menu = menu.addMenu("&File")
        file_menu.addAction(button_action)
        file_menu.addSeparator()
        Edit = menu.addMenu("&Edit")
        Edit.addAction(button_action)
        Edit.addSeparator()
        Help = menu.addMenu("&Help")
        Help.addAction(button_action)
        Help.addSeparator()
        file_submenu = file_menu.addMenu("Submenu")


        layout = QVBoxLayout()

        self.w=QWidget()
        self.w.setLayout(layout)
        self.setCentralWidget(self.w)

        self.editorCommand = QPlainTextEdit()
        self.editorCommand.setStyleSheet('font-size:14pt')





        self.editorCommand.event
        layout.addWidget(self.editorCommand, 3)

        self.createTable()

        # Add box layout, add table to box layout and add box layout to widget

        layout.addWidget(self.tableWidget,7)
        self.statusBar().showMessage('connection')

    def onMyToolBarButtonClick(self,s):
        qury=self.editorCommand.toPlainText()

        if len(qury)>0:

            if qury[-1]==';':
                qury=qury[:-1]

            if 'select'==qury[0:6]:

                if 'column'==qury[7:13]:
                    selectColum=self.DB_Cursor.execute(qury)

                    print(self.DB_Cursor.execute(qury))
                    rowList=list(selectColum.fetchall())
                    if len(rowList)==1:
                        self.statusBar().showMessage("Null")

                    rowList.pop()

                    self.tableWidget.setRowCount(len(rowList))
                    self.tableWidget.setColumnCount(1)
                    cont=0
                    for i in rowList:
                        self.tableWidget.setItem(cont, 0, QTableWidgetItem(i))
                        cont+=1
                elif 'table'==qury[7:12]:
                    selectColum = self.DB_Cursor.execute(qury)

                    rowList = list(selectColum.fetchall())
                    print(rowList, "sss")
                    if len(rowList)==1:
                        self.statusBar().showMessage(rowList.pop())
                    elif len(rowList)>1:
                        rowList.pop()
                        res = ast.literal_eval(rowList[0])
                        keys=list(res.keys())



                        self.tableWidget.setRowCount(len(rowList))
                        self.tableWidget.setColumnCount(len(keys))
                        self.tableWidget.setHorizontalHeaderLabels(keys)

                        rowCont=0
                        for i in rowList:
                            i=ast.literal_eval(i)
                            columnCout=0
                            for j in keys:

                                self.tableWidget.setItem(rowCont, columnCout, QTableWidgetItem(i[j]))                          # +++
                                columnCout+=1
                            rowCont+=1





            else:
                self.statusBar().showMessage(str(self.DB_Cursor.exQuery(qury)))



    def createTable(self):
        # Create table
        self.tableWidget = QTableWidget()
        self.tableWidget.setAlternatingRowColors(True)
        self.tableWidget.setStyleSheet('font-size:14pt')

        header = self.tableWidget.horizontalHeader()

        header.setSectionResizeMode(QHeaderView.ResizeToContents)



        # self.tableWidget.setHorizontalHeaderLabels(['Name', 'Age', 'Sex', 'Add'])

        # self.tableWidget.setItem(0, 0, QTableWidgetItem("Cell (1,1)"))






    def fristDialog(self):

        Vlayout = QVBoxLayout()
        self.labErorr=QLabel('error connetion try agin')
        self.labErorr.setStyleSheet('color:red; font-size:14pt;')
        self.labErorr.setVisible(False)
        Vlayout.addWidget(self.labErorr)
        Hu=QHBoxLayout()
        self.Username = QLineEdit()
        LabUser=QLabel('أسم المستخدم')
        Hu.addWidget(self.Username)
        Hu.addWidget(LabUser)
        self.Username.setFixedWidth(250)

        Hp = QHBoxLayout()
        self.password = QLineEdit()
        self.password.setFixedWidth(250)
        LabPass = QLabel('كلمة المرور')
        Hp.addWidget(self.password)
        Hp.addWidget(LabPass)



        Ndb = QHBoxLayout()
        self.NameDb = QLineEdit()
        Ladb = QLabel('أسم قاعدة البيانات')
        Ndb.addWidget(self.NameDb)
        Ndb.addWidget(Ladb)
        self.NameDb.setFixedWidth(250)

        host = QHBoxLayout()
        self.nameHost = QLineEdit()
        Labh = QLabel('أسم المضيف')
        host.addWidget(self.nameHost)
        host.addWidget(Labh)
        self.nameHost.setFixedWidth(250)



        Hb = QHBoxLayout()

        Cansel = QPushButton("إلغا")

        def canselAcion():
            sys.exit()



        Cansel.clicked.connect(canselAcion)
        ok = QPushButton("موافق")
        ok.clicked.connect(self.okAction)
        Cansel.setMinimumSize(Cansel.sizeHint()*1.4)
        Cansel.setMaximumSize(Cansel.sizeHint()*1.4)
        ok.setMinimumSize(Cansel.sizeHint() * 1.4)
        ok.setMaximumSize(Cansel.sizeHint() * 1.4)
        Hb.addWidget(Cansel)
        Cansel.setAutoDefault(False)
        Hb.addWidget(ok)






        Vlayout.addLayout(Hu)
        Vlayout.addLayout(Hp)
        Vlayout.addLayout(Ndb)
        Vlayout.addLayout(host)
        Vlayout.addLayout(Hb)








        self.dlg = QDialog(self)
        self.dlg.setWindowFlags(
            Qt.Window |
            Qt.CustomizeWindowHint |
            Qt.WindowTitleHint |
            Qt.WindowMinimizeButtonHint

        )
        self.dlg.setWindowTitle("Connetion!")
        self.dlg.resize(350,200)
        self.dlg.setMaximumSize(self.dlg.size())
        self.dlg.setLayout(Vlayout)
        self.dlg.setStyleSheet('font-size:12pt')
        self.dlg.exec()


    n=0
    def okAction(self):
        textPass = "beta"  # self.password.text()
        textUser = "root"#self.Username.text()
        textDBname = "ahmed"#self.NameDb.text()
        textHost = self.nameHost.text()
        textport=''


        if len(textHost)>0 and ':' in textHost:
            textport=textHost[textHost.index(':')+1:]
        self.DB_Cursor = connect(hostname=textHost if len(textHost)>0 else socket.gethostname(),username=textUser if len(textUser)>0 else 'root',password=textPass if len(textPass)>0 else 'beta',dbname=textDBname if len(textDBname)>0 else 'beta',port=textport if len(textport)>0 else '1515')
        self.labErorr.setText(str(self.DB_Cursor))
        self.labErorr.setVisible(True)
        self.statusBar().showMessage(str(self.DB_Cursor))
        self.DB_Cursor=self.DB_Cursor.cursor()

        if self.DB_Cursor!=-1:
            print('ssss Window...')
            self.dlg.close()






if __name__ == '__main__':
    # don't auto scale when drag app to a different monitor.
    # QApplication.setAttribute(Qt.HighDpiScaleFactorRoundingPolicy.PassThrough)

    app = QApplication(sys.argv)

    m=MainWindow()
    m.show()

    m.fristDialog()

    try:
        sys.exit(app.exec_())
    except SystemExit:
        print('Closing Window...')









