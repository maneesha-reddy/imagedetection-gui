# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'demo.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from imageai.Detection import ObjectDetection
import os
import tensorflow as tf
from keras import backend
from tensorflow.keras import backend

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QFileSystemModel, QTreeView, QWidget, QVBoxLayout,QMainWindow
from PyQt5 import QtGui,QtWidgets
from PyQt5.QtGui import QIcon
from os import listdir
from os.path import isfile, join


#from p import App
path=""
message=[]
x=''
k=0
class App(QWidget):

    def __init__(self):
        print("xx")
        #QMainWindow.__init__(self)
        super(App,self).__init__()
        #QtWidgets.QWidget.__init__(self)
        self.title = 'select file'
        self.left = 10
        self.top = 10
        self.width = 640
        self.height = 480
        self.initUI()
    
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        
        self.model = QFileSystemModel()
        self.model.setRootPath('')
        self.tree = QTreeView()
        self.tree.clicked.connect(self.onClicked)
        self.tree.setModel(self.model)
        self.fileSystemModel = QFileSystemModel(self.tree)
        self.fileSystemModel.setReadOnly(True)
        self.fileSystemModel.setRootPath('')
        
        self.tree.setAnimated(False)
        self.tree.setIndentation(20)
        self.tree.setSortingEnabled(True)
        
        self.tree.setWindowTitle("Dir View")
        self.tree.resize(640, 480)
        
        windowLayout = QVBoxLayout()
        windowLayout.addWidget(self.tree)
        self.setLayout(windowLayout)
        self.show()
    def onClicked(self, index):
        global path
        path = self.sender().model().filePath(index)
        #path1=self.sender().model().filePath()
        print(path)
        self.close()
        Ui_MainWindow.display1(self)
        #self.n = Ui_MainWindow(MainWindow)
        #self.n.display()
        
    



class Ui_MainWindow(object):
    def __init__(self):
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label= QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(190, 110, 541, 431))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("hello.png"))
        self.label.setObjectName("label_2")

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1047, 779)
        global x
        x=self
        self.openfolder = QtWidgets.QPushButton(self.centralwidget)
        self.openfolder.setGeometry(QtCore.QRect(20, 110, 121, 51))
        self.openfolder.setObjectName("openfolder")
        self.nextimage = QtWidgets.QPushButton(self.centralwidget)
        self.nextimage.setGeometry(QtCore.QRect(20, 230, 121, 51))
        self.nextimage.setObjectName("nextimage")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(20, 350, 121, 51))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(20, 470, 121, 51))
        self.pushButton_4.setObjectName("pushButton_4")
        #self.label = QtWidgets.QLabel(self.centralwidget)

        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(830, 530, 141, 51))
        self.pushButton.setObjectName("pushButton")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(750, 190, 271, 311))
        self.textEdit.setObjectName("textEdit")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1047, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
    

    def create_new(self):
        self.new_lib = App()
        self.new_lib.show()
        
        

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.openfolder.setText(_translate("MainWindow", "openfolder"))
        self.openfolder.clicked.connect(self.create_new)
        self.nextimage.setText(_translate("MainWindow", "nextImage"))
        self.nextimage.clicked.connect(self.image)
        self.pushButton_3.setText(_translate("MainWindow", "prev image"))
        self.pushButton_3.clicked.connect(self.imagepre)
        self.pushButton_4.setText(_translate("MainWindow", "save annotations"))
        self.pushButton.setText(_translate("MainWindow", "Detect"))
        self.pushButton.clicked.connect(self.imagedetection)

    def image(self):
        global path
        res = path.rsplit('/', 1)
        path1=res[1]
        res=res[0]
        print(res)
        images = [f for f in listdir(res) if isfile(join(res, f))]
        ind=images.index(path1)
        k=(ind+1)%len(images)
        p=res+"/"+images[k]
        print(p)
        self.label.setPixmap(QtGui.QPixmap(p))
        
        path=p
    def imagepre(self):
        global path
        res = path.rsplit('/', 1)
        path1=res[1]
        res=res[0]
        print(res)
        images = [f for f in listdir(res) if isfile(join(res, f))]
        ind=images.index(path1)
        k=(ind-1)%len(images)
        p=res+"/"+images[k]
        self.label.setPixmap(QtGui.QPixmap(p))
        
        path=p
        
    def display1(self):
        n = Ui_MainWindow()
        n.display()

    def display(self):
        #print("hurray")
        #print(self)
        #print(x)
        print(path)
        x.label.setPixmap(QtGui.QPixmap(path))

    def imagedetection(self):
        #print("egyg")
        #global message
        #message=[]
        res = path.rsplit('/', 1)
        path1=res[1]
        res=res[0]
        print(res)
        #images = [f for f in listdir(res) if isfile(join(res, f))]
        #print(images)
        #i=0
        #for image in images: 
        x=res+"/"+path1
        print(x)
        execution_path = os.getcwd()
        detector = ObjectDetection()
        detector.setModelTypeAsRetinaNet()
        detector.setModelPath( os.path.join(execution_path , "resnet50_coco_best_v2.0.1.h5"))
        detector.loadModel()
        y="imagenew.jpg"
        print(execution_path)
        detections, extracted_images = detector.detectObjectsFromImage(input_image=os.path.join(res ,path1), output_image_path=os.path.join(res , y), extract_detected_objects=True)

        print(extracted_images)
        path2=res+"/"+y
        print(self)
        self.label.setPixmap(QtGui.QPixmap(path2))
        c=""
        for eachObject in detections:
            print(eachObject["name"] , " : " , eachObject["percentage_probability"] )
            c=c+"\n"+eachObject["name"] + " : "+str(eachObject["percentage_probability"])
            print(c)
        self.textEdit.setText(c)
            
    

   


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
    app1 = QApplication(sys.argv)
    ex = App()
    sys.exit(app1.exec_())