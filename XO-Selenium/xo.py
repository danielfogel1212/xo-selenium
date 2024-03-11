from selenium import webdriver
from random import randint
from webdriver_manager.chrome import ChromeDriverManager
import time
table = []
table2 = []
Ygame =  [[0,0,0],[0,0,0],[0,0,0]]
Xgame =  [[0,0,0],[0,0,0],[0,0,0]]
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://playtictactoe.org/')
def startGame():
    global table
    global table2
    x = 0
    y = 0
    while y < 10:
        y = y+1
        table.append('')
        table2.append('')
    while x < 9:
        x= x+1
        table[x] = "/html/body/div[3]/div[1]/div["+str(x)+"]"
        table2[x] = "/html/body/div[3]/div[1]/div["+str(x)+"]/div"
    start  = randint(1, 9)
    driver.find_element_by_xpath(table[start]).click()
    MoveX()
 
def insertYgame(y):
    global Ygame
    y = y-1
    if y >= 0 and y <=2:
        Ygame[0][int(y/1)] = 1
    elif y>=3 and y <=5:
        Ygame[1][y-3] = 1
    elif y>=6 and y<=8:
        Ygame[2][y-6] = 1
 
def insertXgame(y):
    global Xgame
    y = y-1
    if y >= 0 and y <=2:
        Xgame[0][int(y/1)] = 1
    elif y>=3 and y <=5:
        Xgame[1][y-3] = 1
    elif y>=6 and y<=8:
        Xgame[2][y-6] = 1
 
def checkY():
    global table2
    for t in range(1,10):
        if driver.find_element_by_xpath(table2[t]).get_attribute("class") == 'o':
            insertYgame(t)
 
def checkX():
    global table2
    for t in range(1,10):
        if driver.find_element_by_xpath(table2[t]).get_attribute("class") == 'x':
            insertXgame(t)
 
def convertY(y,x):
    if y == 0:
        x = x+1
    if y == 1:
        x = x+4
    if y == 2:
        x= x+7
    return x
 
def MoveX():
    global Ygame
    global table
    global table2
    checkY()
    checkX()
    convert1 = block()
    if convert1 == 100:
        for t in range(1,10):
            if not driver.find_element_by_xpath(table2[t]).get_attribute("class") == 'x':
                if not driver.find_element_by_xpath(table2[t]).get_attribute("class") == 'o':
                    driver.find_element_by_xpath(table[t]).click()
                    break
 
    elif convert1 >=1 and convert1 <=9:
        driver.find_element_by_xpath(table[convert1]).click()
 
    MoveX()
 
def block():
    y =0
    x =0
    checkY()
    checkX()
    global Ygame
    global Xgame
    time.sleep(1)
    convert =100
    while y < 3:
        while x < 3:
            Checker =(Ygame[y][0]) + (Ygame[y][1]) + (Ygame[y][2])
            if  Checker >=2:
                if Ygame[y][0] == 0 and Xgame[y][0]==0:
                    convert =convertY(y,0)
                    return convert
                elif Ygame[y][1] == 0 and Xgame[y][1]==0:
                    convert =convertY(y,1)
                    return convert
                elif Ygame[y][2] == 0 and Xgame[y][2]==0:
                    convert = convertY(y,2)
                    return convert
            x=x+1
        x=0
        y = y+1
    y =0
    x=0
    while y < 3:
        while x < 3:
            Checker = (Ygame[0][y]) +  (Ygame[1][y]) + (Ygame[2][y])
            if  Checker >=2:
                if Ygame[0][y] == 0 and Xgame[0][y]==0:
                    convert = convertY(0,y)
                    return convert
                elif  Ygame[1][y] == 0 and Xgame[1][y]==0:
                    convert =convertY(1,y)
                    return convert
                elif  Ygame[2][y] == 0 and Xgame[2][y]==0:
                    convert =  convertY(2,y)
                    return convert
            x = x+1
        x =0
        y = y+1
    y =0
    x=0
    Checker = (Ygame[0][0]) + (Ygame[1][1]) + (Ygame[2][2])
    if  Checker >=2:
        if Ygame[0][0] == 0 and Xgame[0][0]==0:
            convert =convertY(0,0)
            return convert
        elif Ygame[1][1] == 0 and Xgame[1][1]==0:
            convert = convertY(1,1)
            return convert
        elif  Ygame[2][2] == 0 and Xgame[2][2]==0:
            convert = convertY(2,2)
            return convert
    Checker = (Ygame[0][2]) + (Ygame[1][1]) + (Ygame[2][0])
    if  Checker >=2:
        if Ygame[0][2] == 0 and Xgame[0][2]==0:
            convert = convertY(0,2)
            return convert
        elif Ygame[1][1] == 0 and Xgame[1][1]==0:
            convert = convertY(1,1)
            return convert
        elif Ygame[2][0] == 0 and Xgame[2][0]==0:
            convert = convertY(2,0)
            return convert
    return convert
startGame()