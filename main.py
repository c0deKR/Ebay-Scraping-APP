from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import  QMessageBox,QFileDialog,QButtonGroup,QPlainTextEdit,QTextBrowser,QPushButton
import threading
import queue
import sys
from PyQt5.QtCore import QThread
#from AntiFrezzing import Worker
import webbrowser


class LogOutput(QtWidgets.QPlainTextEdit):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setReadOnly(True)
        self.setLineWrapMode(QPlainTextEdit.WidgetWidth)
        #self.setMaximumBlockCount(1000)  # Limit the number of displayed lines

    def write(self, text):
        self.insertPlainText(text)

    def flush(self):
        pass

class Ui_Dialog(object):
    def __init__(self,url,output_file,data_available):
        self.url = url
        self.output_file = output_file
        self.data_available = data_available
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1028, 759)
        Dialog.setWindowIcon(QtGui.QIcon("icons/ebay.png"))
    
        font = QtGui.QFont()
        font.setFamily("Cascadia Code")
        Dialog.setFont(font)
        self.gridLayout_6 = QtWidgets.QGridLayout(Dialog)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.frame = QtWidgets.QFrame(Dialog)
        self.frame.setMinimumSize(QtCore.QSize(681, 0))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.frame.setFont(font)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.frame)
        self.gridLayout_2.setObjectName("gridLayout_2")
        spacerItem = QtWidgets.QSpacerItem(20, 24, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem, 0, 1, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 28, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem1, 0, 2, 2, 1)
        self.url_label = QtWidgets.QLabel(self.frame)
        self.url_label.setMinimumSize(QtCore.QSize(121, 0))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.url_label.setFont(font)
        self.url_label.setObjectName("url_label")
        self.gridLayout_2.addWidget(self.url_label, 1, 1, 2, 1)
        spacerItem2 = QtWidgets.QSpacerItem(144, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem2, 2, 0, 1, 1)
        self.url_line_edit = QtWidgets.QLineEdit(self.frame)
        self.url_line_edit.setMinimumSize(QtCore.QSize(320, 0))
        self.url_line_edit.setObjectName("url_line_edit")
        self.gridLayout_2.addWidget(self.url_line_edit, 2, 2, 1, 2)
        spacerItem3 = QtWidgets.QSpacerItem(144, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem3, 2, 4, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(144, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem4, 3, 0, 1, 1)
        self.url_label_2 = QtWidgets.QLabel(self.frame)
        self.url_label_2.setMinimumSize(QtCore.QSize(121, 0))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.url_label_2.setFont(font)
        self.url_label_2.setObjectName("url_label_2")
        self.gridLayout_2.addWidget(self.url_label_2, 3, 1, 1, 1)
        self.output_frame = QtWidgets.QFrame(self.frame)
        self.output_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.output_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.output_frame.setObjectName("output_frame")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.output_frame)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.csv_rbutton = QtWidgets.QRadioButton(self.output_frame)
        self.csv_rbutton.setObjectName("csv_rbutton")
        self.gridLayout.addWidget(self.csv_rbutton, 0, 0, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(58, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem5, 0, 1, 1, 1)
        self.json_rbutton = QtWidgets.QRadioButton(self.output_frame)
        self.json_rbutton.setObjectName("json_rbutton")
        self.gridLayout.addWidget(self.json_rbutton, 0, 2, 1, 1)
        spacerItem6 = QtWidgets.QSpacerItem(48, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem6, 0, 3, 1, 1)
        self.xml_rbutton = QtWidgets.QRadioButton(self.output_frame)
        self.xml_rbutton.setObjectName("xml_rbutton")
        ############################################
        self.button_group = QButtonGroup()
        self.button_group.setObjectName("button_group")
        self.button_group.addButton(self.json_rbutton)
        self.button_group.addButton(self.csv_rbutton)
        self.button_group.addButton(self.xml_rbutton)
        
        self.gridLayout.addWidget(self.xml_rbutton, 0, 4, 1, 1)
        self.gridLayout_5.addLayout(self.gridLayout, 0, 0, 1, 1)
        self.gridLayout_2.addWidget(self.output_frame, 3, 2, 1, 2)
        spacerItem7 = QtWidgets.QSpacerItem(144, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem7, 3, 4, 1, 1)
        spacerItem8 = QtWidgets.QSpacerItem(144, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem8, 4, 0, 1, 1)
        self.url_label_3 = QtWidgets.QLabel(self.frame)
        self.url_label_3.setMinimumSize(QtCore.QSize(121, 0))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.url_label_3.setFont(font)
        self.url_label_3.setObjectName("url_label_3")
        self.gridLayout_2.addWidget(self.url_label_3, 4, 1, 1, 1)
        self.directory_line_edit = QtWidgets.QLineEdit(self.frame)
        self.directory_line_edit.setMinimumSize(QtCore.QSize(201, 0))
        self.directory_line_edit.setObjectName("directory_line_edit")
        self.gridLayout_2.addWidget(self.directory_line_edit, 4, 2, 1, 1)
        self.browse_button = QtWidgets.QPushButton(self.frame)
        self.browse_button.setMinimumSize(QtCore.QSize(91, 0))
        self.browse_button.setObjectName("browse_button")
        #################################################
        self.browse_button.clicked.connect(self.open_directory_dialog)
        self.gridLayout_2.addWidget(self.browse_button, 4, 3, 1, 1)
        spacerItem9 = QtWidgets.QSpacerItem(144, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem9, 4, 4, 1, 1)
        spacerItem10 = QtWidgets.QSpacerItem(20, 25, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem10, 5, 1, 1, 1)
        spacerItem11 = QtWidgets.QSpacerItem(20, 25, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem11, 5, 2, 1, 1)
        spacerItem12 = QtWidgets.QSpacerItem(20, 25, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem12, 5, 3, 1, 1)
        self.gridLayout_6.addWidget(self.frame, 1, 0, 2, 5)
        
        ##########################################################
        self.CMD_plainTextEdit = LogOutput(Dialog)
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(10)
        self.CMD_plainTextEdit.setStyleSheet("background-color: #333333; color: white;")
        self.CMD_plainTextEdit.setFont(font)
        self.CMD_plainTextEdit.setObjectName("CMD_plainTextEdit")
        self.gridLayout_6.addWidget(self.CMD_plainTextEdit, 3, 2, 1, 3)
        #self.CMD_plainTextEdit.setPlainText("Output will be displayed here")
        #Redirect sys.stdout and sys.stderr to the LogOutput widget
        """sys.stdout = self.CMD_plainTextEdit
        sys.stderr = self.CMD_plainTextEdit"""
        ##########################################################
        spacerItem13 = QtWidgets.QSpacerItem(20, 87, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_6.addItem(spacerItem13, 4, 2, 1, 1)
        spacerItem14 = QtWidgets.QSpacerItem(20, 87, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_6.addItem(spacerItem14, 4, 4, 1, 1)
        self.frame_4 = QtWidgets.QFrame(Dialog)
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame_4)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.github_button = QtWidgets.QPushButton(self.frame_4)
        self.github_button.setText("")
        self.github_button.setAutoDefault(True)
        self.github_button.setDefault(False)
        self.github_button.setFlat(True)
        self.github_button.setObjectName("github_button")
        self.horizontalLayout.addWidget(self.github_button)
        self.github_button.setIcon(QtGui.QIcon("icons/github.png"))
        self.github_button.clicked.connect(lambda:self.open_link("https://github.com/c0deKR"))
        self.line = QtWidgets.QFrame(self.frame_4)
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.horizontalLayout.addWidget(self.line)
        self.gmail_button = QtWidgets.QPushButton(self.frame_4)
        self.gmail_button.setText("")
        self.gmail_button.setFlat(True)
        self.gmail_button.setObjectName("gmail_button")
        self.gmail_button.clicked.connect(lambda:self.open_link("saadeddine.kerroum@gmail.com"))
        self.horizontalLayout.addWidget(self.gmail_button)
        self.gmail_button.setIcon(QtGui.QIcon("icons/gmail.png"))
        self.line_2 = QtWidgets.QFrame(self.frame_4)
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.horizontalLayout.addWidget(self.line_2)
        self.fiverr_button = QtWidgets.QPushButton(self.frame_4)
        self.fiverr_button.setText("")
        self.fiverr_button.setFlat(True)
        self.fiverr_button.setObjectName("fiverr_button")
        self.fiverr_button.clicked.connect(lambda:self.open_link("https://www.fiverr.com/s/kEx7Xg"))
        self.horizontalLayout.addWidget(self.fiverr_button)
        self.fiverr_button.setIcon(QtGui.QIcon("icons/fiverr.png"))
        self.gridLayout_6.addWidget(self.frame_4, 5, 1, 1, 2)
        spacerItem15 = QtWidgets.QSpacerItem(683, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_6.addItem(spacerItem15, 5, 3, 1, 1)
        self.execute_button = QtWidgets.QPushButton(Dialog)
        ###############################################################
        self.execute_button.clicked.connect(self.start_thread)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.execute_button.setFont(font)
        self.execute_button.setObjectName("execute_button")
        self.gridLayout_6.addWidget(self.execute_button, 5, 4, 1, 1)
        self.frame_2 = QtWidgets.QFrame(Dialog)
        self.frame_2.setMinimumSize(QtCore.QSize(671, 0))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.frame_2)
        self.gridLayout_4.setObjectName("gridLayout_4")
        spacerItem16 = QtWidgets.QSpacerItem(183, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem16, 1, 0, 1, 1)
        spacerItem17 = QtWidgets.QSpacerItem(182, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem17, 1, 3, 1, 1)
        self.label = QtWidgets.QLabel(self.frame_2)
        font = QtGui.QFont()
        font.setFamily("Goudy Old Style")
        font.setPointSize(40)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout_4.addWidget(self.label, 1, 1, 1, 1)
        self.gridLayout_6.addWidget(self.frame_2, 0, 1, 1, 4)
        self.retranslateUi(Dialog)
        #QtCore.QMetaObject.connectSlotsByName(Dialog)
    def open_link(self,url):
        webbrowser.open(url)
    def start_thread(self):
        
        self.retrieve_data()
        self.get_selected_radio_button()
        self.execute_button.setEnabled(False)
        self.data_available.set()
        # Step 2: Create a QThread object
        """self.thread = QThread()
        # Step 3: Create a worker object
        self.worker = Worker(self.data_available)
        # Step 4: Move worker to the thread
        self.worker.moveToThread(self.thread)
        # Step 5: Connect signals and slots
        self.thread.started.connect(self.worker.run)
        self.worker.finished.connect(self.thread.quit)
        self.worker.finished.connect(self.worker.deleteLater)
        self.thread.finished.connect(self.thread.deleteLater)
        self.thread.finished.connect(
            lambda: self.execute_button.setEnabled(True)
        )
        # Step 6: Start the thread
        self.thread.start()"""

        
    def thread_finished(self):
        print('Task completed!')
        self.execute_button.setEnabled(True)
    def get_selected_radio_button(self):
        self.selected_rbutton = self.button_group.checkedButton().text()
        self.output_file.put( f"ouput.{self.selected_rbutton.lower()}")
        if self.selected_rbutton:
            print("Selected Radio Button:", self.selected_rbutton)
            self.CMD_plainTextEdit.setPlainText("Selected Radio Button:"+self.selected_rbutton)
        else:
            self.show_warning_dialog("Warning", "Select the output file!")    
    
        
    def show_warning_dialog(self, title, message):
        warning_dialog = QMessageBox()
        warning_dialog.setIcon(QMessageBox.Warning)
        warning_dialog.setWindowTitle(title)
        warning_dialog.setText(message)
        warning_dialog.setStandardButtons(QMessageBox.Ok)
        warning_dialog.exec_()        
    def retrieve_data(self):
        self.url.put(self.url_line_edit.text())
        
        if self.url == "":
            self.show_warning_dialog("Warning", "Insert the URL!")
        elif self.directory_line_edit.text() == "":
            self.show_warning_dialog("Warning", "Please Select a Folder!")
        else:
            #print(f"URL:{self.url}")
            #self.CMD_plainTextEdit.setPlainText("URL:"+self.url)
            pass
    def open_directory_dialog(self):
        options = QFileDialog.Options()
        options |= QFileDialog.ReadOnly  # You can add more options if needed
        self.directory = QFileDialog.getExistingDirectory(None, 'Open Directory', '', options=options)
        self.directory_line_edit.setText(self.directory)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Ebay.com Scraper"))
        self.url_label.setText(_translate("Dialog", "Product URL"))
        self.url_label_2.setText(_translate("Dialog", "Output file "))
        self.csv_rbutton.setText(_translate("Dialog", "CSV"))
        self.json_rbutton.setText(_translate("Dialog", "JSON"))
        self.xml_rbutton.setText(_translate("Dialog", "XML"))
        self.url_label_3.setText(_translate("Dialog", "Directory"))
        self.browse_button.setText(_translate("Dialog", "Browse"))
        self.execute_button.setText(_translate("Dialog", "Execute"))
        self.label.setText(_translate("Dialog", "ebay.com scraper"))
    
        
def start_app(url,output_file,data_available):    
    if __name__ == "__main__":
        import sys
        app = QtWidgets.QApplication(sys.argv)
        Dialog = QtWidgets.QDialog()
        ui = Ui_Dialog(url,output_file,data_available)
        ui.setupUi(Dialog)
        Dialog.show()
        
        data_available.set()
        sys.exit(app.exec_())
        
def run_spider(url,output_file):
    from scrapy import cmdline

    # Replace 'project_name' and 'spider_name' with your actual project and spider names
    spider_name = 'ItemScraper'
    
    # Define any custom options as needed
    custom_options = [
        "-o", output_file, 
        "-a",f"URL={url}", # Save scraped data to a JSON file
        # Add other options here
    ]

    # Run the spider with custom options
    cmdline.execute(['scrapy', 'crawl', spider_name] + custom_options)
    print(['scrapy', 'crawl', spider_name] + custom_options)
    
while True:    
    url = queue.Queue()
    output_file = queue.Queue()
    data_is_available_event = threading.Event()
    print("Starting the app")
    start_app_thread = threading.Thread(target=start_app,args=(url,output_file,data_is_available_event))

    start_app_thread.start()
    print("App started")
    data_is_available_event.wait()
    run_spider(url.get(),output_file.get())
    print("done")
    Ui_Dialog.execute_button.setEnabled(True)
