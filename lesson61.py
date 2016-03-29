# -*- coding:utf-8 -*-

import time
import urllib.request
import json
import re
import _thread
import sys
import PySide
from PySide.QtCore import *
from PySide.QtGui import *
from city import city
from lesson61UI import Ui_MainWindow
def __getCityWeather__():
    cityname = input('Enter the city name')
    end = __getCityWeatherApi__(cityname)
    print(end)

def __getCityWeatherApi__(cityname):    
    citycode = city.get(cityname)
    if citycode:
        try:
            web = urllib.request.urlopen('http://www.weather.com.cn/data/cityinfo/%s.html' % citycode)
            content = str(web.read(),'utf-8')
            data = json.loads(content)
            result = data['weatherinfo']
            str_temp = ('%s\n%s ~ %s')%(
                result['weather'],
                result['temp1'],
                result['temp2']
                )
            return str_temp
        except:
            return 'err'
    else:
        return 'no such city'

def __getMovieName__():
    for i in range(30):
        try:
           _thread.start_new_thread(__getContent__,(i,))
        except:
            print('process err')
    input('end')

def __getContent__(i):
    id = 1764796 +i
    url = 'https://api.douban.com/v2/movie/subject/%d' % id
    try:
        content = str(urllib.request.urlopen(url).read(),'utf-8')
        data = json.loads(content)
        str_temp = ('%s\n%s')%(
            data['title'],
            data['summary']
        )
        print('%s\n'%str_temp)
    except:
        print('http err')

def __getTextType__(): ##练习正则表达式
    id = 1764796 
    url = 'https://api.douban.com/v2/movie/subject/%d' % id
    try:
        content = urllib.request.urlopen(url).read().decode('UTF-8')
        print(re.match(r'id',content,re.M|re.I))
    except:
        print('http err')

def __readFile__():
    for line in open('example.txt'):
        print(line,end='')

def __askForNumber__():
    while True:
        try:
            return int(input('Please enter a number:'))
        except ValueError:
            pass

def __uiMain__():
    # Create App
    app = QApplication(sys.argv)
    # Create Window
    NewForm = Form()
    NewForm.show()
    # Create a Label
    #label = QLabel("<font color=red size=40>hello</font>")
    #label.show()
    #Create a simple dialog box
    #msgBox = QMessageBox()
    #msgBox.setText("Hello World - using PySide version"+PySide.__version__)
    #msgBox.exec_()
    # Exit
    sys.exit(app.exec_())

class Form(QMainWindow,Ui_MainWindow):
    def __init__(self,parent=None):
        super(Form,self).__init__(parent)
        self.setupUi(self)
        self.CurrentPlaceButton.clicked.connect(self.ui__getWeather)
    def ui__getWeather(self):
        ui_cityname = self.CurrentPlace.text()
        end = __getCityWeatherApi__(ui_cityname)
        self.CurrentWeather.setText(end)

def __work__():
    __uiMain__()

def __main__():
    starttime = time.time()
    __work__()
    endtime = time.time()
    print('\n used time %f sec'%(endtime-starttime))

__main__()
