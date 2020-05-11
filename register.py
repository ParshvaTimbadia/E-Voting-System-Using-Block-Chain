# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'register.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import cv2
import sqlite3
import cv2, sys, numpy, os
import hashlib
import smtplib
import socket
import requests
import json
from collections import Counter

class Ui_MainWindow(object):
    def openWindow(self):
        self.ui = Ui_MainWindowLogin()
        self.ui.setupUi(MainWindow2)
        MainWindow.hide()
        MainWindow2.showMaximized()

    def save_data(self):
        print("I am inside save Data")
        name = self.lineEdit.text()
        email = self.lineEdit_2.text()
        contact = self.lineEdit_3.text()
        dob = self.dateEdit.text()
        aadhar = self.lineEdit_4.text()
        address = self.plainTextEdit.toPlainText()
        if len(aadhar) != 0 and ".com" in email and len(contact) != 0:
            conn = sqlite3.connect('db.db')
            conn.execute("INSERT INTO REGISTER (NAME,EMAIL,CONTACT,DOB,AADHAR,ADDRESS) VALUES (?,?,?,?,?,?)",
                         (name, email, str(contact), str(dob), str(aadhar), address))
            ran = numpy.random.random_integers(100,25000)
            os.mkdir('datasets/' + str(ran))

            haar_file = 'haarcascade_frontalface_default.xml'

            # All the faces data will be
            #  present this folder
            datasets = 'datasets'

            # These are sub data sets of folder,
            # for my faces I've used my name you can
            # change the label here
            sub_data = str(ran)

            path = os.path.join(datasets, sub_data)
            if not os.path.isdir(path):
                os.mkdir(path)

            # defining the size of images
            (width, height) = (130, 100)

            # '0' is used for my webcam,
            # if you've any other camera
            #  attached use '1' like this
            face_cascade = cv2.CascadeClassifier(haar_file)
            webcam = cv2.VideoCapture(0)

            # The program loops until it has 30 images of the face.
            count = 1
            while count < 30:
                (_, im) = webcam.read()
                gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
                faces = face_cascade.detectMultiScale(gray, 1.3, 4)
                for (x, y, w, h) in faces:
                    cv2.rectangle(im, (x, y), (x + w, y + h), (255, 0, 0), 2)
                    face = gray[y:y + h, x:x + w]
                    face_resize = cv2.resize(face, (width, height))
                    cv2.imwrite('% s/% s.png' % (path, count), face_resize)
                count += 1

                cv2.imshow('OpenCV', im)
                key = cv2.waitKey(10)
                if key == 27:
                    break
            webcam.release()
            conn.commit()
            conn.close()
            QtWidgets.QMessageBox.information(MainWindow, "Message", "Voter Created Successfully")
            self.openWindow()
        else:
            QtWidgets.QMessageBox.information(MainWindow, "Message", "Please Fill All Values")

    def save_images(self):
        haar_file = 'haarcascade_frontalface_default.xml'

        # All the faces data will be
        #  present this folder
        datasets = 'datasets'

        # These are sub data sets of folder,
        # for my faces I've used my name you can
        # change the label here
        sub_data = 'vivek'

        path = os.path.join(datasets, sub_data)
        if not os.path.isdir(path):
            os.mkdir(path)

            # defining the size of images
        (width, height) = (130, 100)

        # '0' is used for my webcam,
        # if you've any other camera
        #  attached use '1' like this
        face_cascade = cv2.CascadeClassifier(haar_file)
        webcam = cv2.VideoCapture(0)

        # The program loops until it has 30 images of the face.
        count = 1
        while count < 30:
            (_, im) = webcam.read()
            gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
            faces = face_cascade.detectMultiScale(gray, 1.3, 4)
            for (x, y, w, h) in faces:
                cv2.rectangle(im, (x, y), (x + w, y + h), (255, 0, 0), 2)
                face = gray[y:y + h, x:x + w]
                face_resize = cv2.resize(face, (width, height))
                cv2.imwrite('% s/% s.png' % (path, count), face_resize)
            count += 1

            cv2.imshow('OpenCV', im)
            key = cv2.waitKey(10)
            if key == 27:
                break

    def clear(self):
        name = self.lineEdit.clear()
        email = self.lineEdit_2.clear()
        contact = self.lineEdit_3.clear()
        dob = self.dateEdit.clear()
        aadhar = self.lineEdit_4.clear()
        address = self.plainTextEdit.clear()


    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1360, 768)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 1361, 61))
        font = QtGui.QFont()
        font.setFamily("Monaco")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("background-color: rgb(17, 168, 198);\n"
"color: rgb(255, 255, 255);")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(410, 90, 551, 611))
        self.frame.setStyleSheet("background-color: rgb(211, 220, 207);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(86, 52, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.lineEdit = QtWidgets.QLineEdit(self.frame)
        self.lineEdit.setGeometry(QtCore.QRect(180, 40, 271, 51))
        self.lineEdit.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(3, 3, 3);")
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_2.setGeometry(QtCore.QRect(180, 110, 271, 51))
        self.lineEdit_2.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(3, 3, 3);")
        self.lineEdit_2.setText("")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(86, 122, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName("label_3")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_3.setGeometry(QtCore.QRect(180, 190, 271, 51))
        self.lineEdit_3.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(3, 3, 3);")
        self.lineEdit_3.setText("")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.label_4 = QtWidgets.QLabel(self.frame)
        self.label_4.setGeometry(QtCore.QRect(76, 202, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.frame)
        self.label_5.setGeometry(QtCore.QRect(76, 282, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_5.setObjectName("label_5")
        self.dateEdit = QtWidgets.QDateEdit(self.frame)
        self.dateEdit.setGeometry(QtCore.QRect(180, 270, 271, 61))
        self.dateEdit.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(3, 3, 3);")
        self.dateEdit.setCalendarPopup(True)
        self.dateEdit.setObjectName("dateEdit")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_4.setGeometry(QtCore.QRect(184, 360, 271, 51))
        self.lineEdit_4.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(3, 3, 3);")
        self.lineEdit_4.setText("")
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.label_6 = QtWidgets.QLabel(self.frame)
        self.label_6.setGeometry(QtCore.QRect(80, 372, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_6.setObjectName("label_6")
        self.label_12 = QtWidgets.QLabel(self.frame)
        self.label_12.setGeometry(QtCore.QRect(80, 442, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_12.setFont(font)
        self.label_12.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_12.setObjectName("label_12")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.frame)
        self.plainTextEdit.setGeometry(QtCore.QRect(190, 440, 261, 71))
        self.plainTextEdit.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(3, 3, 3);")
        self.plainTextEdit.setObjectName("plainTextEdit")

        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setGeometry(QtCore.QRect(190, 530, 121, 41))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.save_data)

        self.pushButton_2 = QtWidgets.QPushButton(self.frame)
        self.pushButton_2.setGeometry(QtCore.QRect(340, 530, 111, 41))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.openWindow)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1360, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Register"))
        self.label_2.setText(_translate("MainWindow", "Name: "))
        self.label_3.setText(_translate("MainWindow", "Email: "))
        self.label_4.setText(_translate("MainWindow", "Contact No.: "))
        self.label_5.setText(_translate("MainWindow", "D.O.B : "))
        self.label_6.setText(_translate("MainWindow", "Aadhar No.: "))
        self.label_12.setText(_translate("MainWindow", "Address: "))
        self.pushButton.setText(_translate("MainWindow", "Submit"))
        self.pushButton_2.setText(_translate("MainWindow", "Login"))


class Ui_MainWindowLogin(object):
    def openWindow(self):
        self.ui = Ui_MainWindow()
        self.ui.setupUi(MainWindow)
        MainWindow2.hide()
        MainWindow.showMaximized()

    def openWindow2(self):
        self.ui = Ui_MainWindowVote()
        self.ui.setupUi(MainWindow3)
        MainWindow2.hide()
        MainWindow3.showMaximized()



    def authenticate_aadhar(self):
        print("I am inside aadhar authentication")
        self.lineEdit.setVisible(True)
        self.pushButton_3.setVisible(True)
        self.pushButton.setVisible(True)
        self.pushButton_2.setVisible(True)

    def check(self):
        global user_email
        global aadhar_number
        aadhar_list = []
        name_list = []
        email_list = []
        aadhar = self.lineEdit.text()
        print("I am inside check")
        conn = sqlite3.connect('db.db')
        data = conn.execute('''Select * from Register''')
        for row in data:
            aadhar_list.append(row[5])
            name_list.append(row[1])
            email_list.append(row[2])

        if aadhar in aadhar_list:
            aadhar_number = aadhar
            index = aadhar_list.index(aadhar)
            user_email = email_list[index]
            print(email_list[index])
            self.verify()

        else:
            QtWidgets.QMessageBox.information(MainWindow, "Message", "No Records Found")


    def verify(self):
        import random
        global RandomNumber
        global user_email
        print("I am inside verify aadhar")
        self.lineEdit.setVisible(False)
        self.pushButton_3.setVisible(False)
        self.lineEdit_2.setVisible(True)
        self.pushButton_4.setVisible(True)
        self.pushButton_5.setVisible(True)

        numbers = range(1000, 9999)
        RandomNumber = random.choice(numbers)
        print(RandomNumber)

        s = smtplib.SMTP('smtp.gmail.com', 587)

        # start TLS for security
        s.starttls()

        # Authentication
        s.login("mradul.mishra@connekt.in", "m8982169105m")

        # message to be sent
        message = "This Your OTP: " + str(RandomNumber)
        print(message)
        # sending the mail
        s.sendmail("mradul.mishra@connekt.in", str(user_email), message)

        # terminating the session
        s.quit()
        print("Message Sent Successfully")

    def otp_check(self):
        global RandomNumber
        otp = self.lineEdit_2.text()

        if str(otp) == str(RandomNumber):
            self.openWindow2()


    def open_camera(self):
        capture = cv2.VideoCapture(0)

        while (True):

            ret, frame = capture.read()

            cv2.imshow('video', frame)

            if cv2.waitKey(1) == 27:
                break

        capture.release()
        cv2.destroyAllWindows()

    def vote_count(self):
        vote_list = []
        print("I am inside vote count")
        url = 'http://manaljain05.pythonanywhere.com/'
        result = requests.get(url=url)
        print(result.json())
        output = result.json()
        print(output['Result'])
        output = list(output['Result'])
        for i in range(len(output)):
            if output[i] == "]":
                vote_list.append(output[i-2])

        print(vote_list)
        vote_list = list(filter(lambda a: a != '"', vote_list))
        print(vote_list)
        final_list = []
        for i in vote_list:
            final_list.append(int(i))
        final_list.sort()
        print(final_list)

        print(Counter(final_list))
        text_final = ""
        for i in list(Counter(final_list).items()):
            a = 1
            label = "Candidate " + str(i[0]) + " " + "Vote " + str(i[1])
            text_final = text_final + label + "\n"
        print(text_final)
        self.label_2.setText(str((text_final)))







    def setupUi(self, MainWindow):

        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1360, 768)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(410, 90, 551, 300))
        self.frame.setStyleSheet("background-color: rgb(211, 220, 207);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")

        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setGeometry(QtCore.QRect(140, 80, 300, 41))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.authenticate_aadhar)
        self.pushButton.setStyleSheet("background-color: rgb(17, 168, 198);\n"
                                 "color: rgb(255, 255, 255);")

        self.pushButton_2 = QtWidgets.QPushButton(self.frame)
        self.pushButton_2.setGeometry(QtCore.QRect(140, 150, 300, 41))
        self.pushButton_2.setObjectName("pushButton")
        self.pushButton_2.clicked.connect(self.openWindow)
        self.pushButton_2.setStyleSheet("background-color: rgb(17, 168, 198);\n"
                                      "color: rgb(255, 255, 255);")
        self.pushButton_2.setText("Register")

        self.lineEdit = QtWidgets.QLineEdit(self.frame)
        self.lineEdit.setGeometry(QtCore.QRect(140, 80, 300, 41))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit.setPlaceholderText('Enter Aadhar Number')
        self.lineEdit.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                        "color: rgb(0, 0, 0);")
        self.lineEdit.setVisible(False)
        self.lineEdit.returnPressed.connect(self.check)

        self.lineEdit_2 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_2.setGeometry(QtCore.QRect(140, 80, 300, 41))
        self.lineEdit_2.setObjectName("lineEdit")
        self.lineEdit_2.setPlaceholderText('Enter OTP Sent on Email')
        self.lineEdit_2.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                    "color: rgb(0, 0, 0);")
        self.lineEdit_2.setVisible(False)
        self.lineEdit_2.returnPressed.connect(self.otp_check)


        self.pushButton_3 = QtWidgets.QPushButton(self.frame)
        self.pushButton_3.setGeometry(QtCore.QRect(140, 150, 300, 41))
        self.pushButton_3.setObjectName("pushButton")
        self.pushButton_3.setStyleSheet("background-color: rgb(17, 168, 198);\n"
                                        "color: rgb(255, 255, 255);")
        self.pushButton_3.setText("Submit Aadhar")
        self.pushButton_3.setVisible(False)
        self.pushButton_3.clicked.connect(self.check)



        self.pushButton_4 = QtWidgets.QPushButton(self.frame)
        self.pushButton_4.setGeometry(QtCore.QRect(140, 150, 300, 41))
        self.pushButton_4.setObjectName("pushButton")
        self.pushButton_4.setStyleSheet("background-color: rgb(17, 168, 198);\n"
                                        "color: rgb(255, 255, 255);")
        self.pushButton_4.setText("Submit OTP")
        self.pushButton_4.setVisible(False)
        self.pushButton_4.clicked.connect(self.otp_check)


        self.pushButton_5 = QtWidgets.QPushButton(self.frame)
        self.pushButton_5.setGeometry(QtCore.QRect(140, 220, 300, 41))
        self.pushButton_5.setObjectName("pushButton")
        self.pushButton_5.setStyleSheet("background-color: rgb(17, 168, 198);\n"
                                        "color: rgb(255, 255, 255);")
        self.pushButton_5.setText("Resend OTP")
        self.pushButton_5.setVisible(False)
        self.pushButton_5.clicked.connect(self.verify)


        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 1361, 61))
        font = QtGui.QFont()
        font.setFamily("Monaco")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("background-color: rgb(17, 168, 198);\n"
"color: rgb(255, 255, 255);")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")

        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(0, 450, 1360, 300))
        font = QtGui.QFont()
        font.setFamily("Monaco")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("background-color: rgb(17, 168, 198);\n"
                                 "color: rgb(255, 255, 255);")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")



        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1360, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.vote_count()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))

        self.pushButton.setText(_translate("MainWindow", "Login"))
        self.label.setText(_translate("MainWindow", "Login"))


class Ui_MainWindowVote(object):
    def openWindow(self):
        self.ui = Ui_MainWindowLogin()
        self.ui.setupUi(MainWindow)
        MainWindow3.hide()
        MainWindow.showMaximized()

    def authenticate_aadhar(self):
        print("I am inside aadhar authentication")
        self.lineEdit.setVisible(True)
        self.pushButton_3.setVisible(True)
        self.pushButton.setVisible(True)
        self.pushButton_2.setVisible(True)

    def check(self):
        aadhar_list = []
        name_list = []
        print("I am inside check")
        conn = sqlite3.connect('db.db')
        data = conn.execute('''Select * from Register''')
        for row in data:
            aadhar_list.append(row[5])
            name_list.append(row[1])

        print(aadhar_list)
        print(name_list)


    def vote(self):
        global aadhar_number
        aadhar_list = []
        conn = sqlite3.connect("db.db")
        cursor = conn.execute("SELECT ID, HASHBLOCK, AADHAR FROM VOTETABLE")
        conn.commit()
        for row in cursor:
            id = row[0]
            previous_block = row[1]
            aadhar_list.append(row[2])

        # Creating new block and hashing it
        hash_block = str(previous_block) + str(id + 1)
        hash_object = hashlib.md5(hash_block.encode()).hexdigest()

        print("This is aadhar list")
        print(aadhar_list)
        print(aadhar_number)
        if aadhar_number not in aadhar_list:
            conn = sqlite3.connect("db.db")

            # Storing new block
            conn.execute("INSERT INTO VOTETABLE (HASHBLOCK,PREVIOUSBLOCK,VOTE,AADHAR) VALUES (?,?,?,?)",
                         (str(hash_object), str(previous_block), self.comboBox.currentIndex(), str(aadhar_number)))
            conn.commit()
            hostname = socket.gethostname()
            IPAddr = socket.gethostbyname(hostname)
            print("Your Computer Name is:" + hostname)
            print("Your Computer IP Address is:" + IPAddr)

            url = 'http://manaljain05.pythonanywhere.com/'
            data = {
                'IP': str(IPAddr),
                'Aadhar': str(aadhar_number),
                'Vote': str(self.comboBox.currentIndex())
            }
            headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}

            result = requests.post(url=url, data=json.dumps(data), headers=headers)
            print(result)
            self.openWindow()
            QtWidgets.QMessageBox.information(MainWindow, "Message", "Vote Casted")

        else:
            self.openWindow()
            QtWidgets.QMessageBox.information(MainWindow, "Message", "Vote Already Casted")



    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1360, 768)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(410, 90, 551, 300))
        self.frame.setStyleSheet("background-color: rgb(211, 220, 207);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")


        self.comboBox = QtWidgets.QComboBox(self.frame)
        self.comboBox.setGeometry(QtCore.QRect(140, 80, 300, 41))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.setStyleSheet("background-color: rgb(17, 168, 198);\n"
                                 "color: rgb(255, 255, 255);")
        self.comboBox.addItem('Candidate 1')
        self.comboBox.addItem('Candidate 2')
        self.comboBox.addItem('Candidate 3')
        self.comboBox.addItem('Candidate 4')




        self.pushButton_2 = QtWidgets.QPushButton(self.frame)
        self.pushButton_2.setGeometry(QtCore.QRect(140, 150, 300, 41))
        self.pushButton_2.setObjectName("pushButton")
        self.pushButton_2.clicked.connect(self.vote)
        self.pushButton_2.setStyleSheet("background-color: rgb(17, 168, 198);\n"
                                      "color: rgb(255, 255, 255);")
        self.pushButton_2.setText("Submit")




        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 1361, 61))
        font = QtGui.QFont()
        font.setFamily("Monaco")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("background-color: rgb(17, 168, 198);\n"
"color: rgb(255, 255, 255);")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")


        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1360, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Caste Vote"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    MainWindow2 = QtWidgets.QMainWindow()
    MainWindow3 = QtWidgets.QMainWindow()



    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.showMaximized()
    sys.exit(app.exec_())

