from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con, win32gui
from random import randint
import cv2 as cv
import pytesseract as tes
import pytesseract
from PIL import ImageGrab, Image
import cv2
import numpy as nm
import numpy

#812, 216, 980, 250 - Check name Full HD
#1695, 694, 1850, 800 - Check 'locked in' and 'confirmed' Full HD
#962, 165, 1403, 984 - items Full HD
#1498, 521, 1887, 617 - buttons Full HD
#1444, 322 - coordinates for putting items Full HD

#for text recognition
tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

#all nicknames
def list_of_nicknames(list):
      return    list    

#function for click into found item
def click(x,y):
    win32api.SetCursorPos((x,y))
    time.sleep(.1)
    pyautogui.click()
    
#function for double click
def double_click(x,y):
    win32api.SetCursorPos((x,y))
    time.sleep(.1)
    pyautogui.click()
    pyautogui.click()

    
#1250, 280, 2000, 1400 - items
#2007, 722, 2500, 800 - buttons
#1650, 0, 2500, 400 - step
#2184, 934, 2500, 1100 - for accept trade check of 'locked in' and 'confirmed'
#function for check if the item is on the screen
def check(item , x, y, w, h):
 a = 0
 test =[]
 while a < 1:
    test = pyautogui.locateOnScreen(item, region=(x, y, w, h), grayscale=True, confidence=0.9) 
    if test is not None:
       a = a + 1     
       return test
    

#function to avoid disconnect
def step(item , x, y, w, h):
    if pyautogui.locateOnScreen(item, region=(x, y, w, h), grayscale=True, confidence=0.9) !=None:
       pyautogui.press('w')
       

# Brazenhem algo
def draw_line(x1=0, y1=0, x2=0, y2=0):

    coordinates = []

    dx = x2 - x1
    dy = y2 - y1

    sign_x = 1 if dx > 0 else -1 if dx < 0 else 0
    sign_y = 1 if dy > 0 else -1 if dy < 0 else 0

    if dx < 0:
        dx = -dx
    if dy < 0:
        dy = -dy

    if dx > dy:
        pdx, pdy = sign_x, 0
        es, el = dy, dx
    else:
        pdx, pdy = 0, sign_y
        es, el = dx, dy

    x, y = x1, y1

    error, t = el / 2, 0

    coordinates.append([x, y])

    while t < el:
        error -= es
        if error < 0:
            error += el
            x += sign_x
            y += sign_y
        else:
            x += pdx
            y += pdy
        t += 1
        coordinates.append([x, y])

    return coordinates

# Smooth move mouse from current pos to xy
def smooth_move(x, y):
    flags, hcursor, (startX, startY) = win32gui.GetCursorInfo()
    coordinates = draw_line(startX, startY, x, y)
    x = 0
    for dot in coordinates:
        x += 1
        if x % 2 == 0 and x % 3 == 0:
            time.sleep(0.01)
        win32api.SetCursorPos((dot[0], dot[1]))   

#X: 2035 Y:  440 - position of the place to put an item
#function to put item in trade
def put_item_in_trade(x,y,item):
    pyautogui.press(str(x))
    pyautogui.press(str(y))
    active_item = check(item, 962, 165, 1403, 984)
    win32api.SetCursorPos((active_item[0] + 50, active_item[1])) #we need to adjust x position
    time.sleep(.1)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(.2)
    smooth_move(1444, 322)
    time.sleep(.1)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)


def put_item_in_trade_flux_and_charcoal(x,y,z,item):
    pyautogui.press(str(x))
    pyautogui.press(str(y))
    pyautogui.press(str(z))
    active_item = check(item, 962, 165, 1403, 984)
    win32api.SetCursorPos((active_item[0] + 50, active_item[1])) #we need to adjust x position
    time.sleep(.1)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(.2)
    smooth_move(1444, 322)
    time.sleep(.1)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

    
#1250, 280, 2000, 1400 - items
#2007, 722, 2500, 800 - buttons
#function to put all items                 
def put_all_items():
    print('start putting items')
    #put tolvium
    flux = check('TolviumFullHD.png', 962, 165, 1403, 984)
    time.sleep(.1)
    click(flux[0], flux[1])
    time.sleep(.1)
    Split = check('SplitFullHD.png', 962, 165, 1403, 984)
    click(Split[0], Split[1])
    time.sleep(.1)
    inTrade = check('inTradeFullHD.png', 962, 165, 1403, 984)
    double_click(inTrade[0], inTrade[1])
    time.sleep(.1)
    put_item_in_trade(1,0,'ReadyForTradeFullHD.png')
    
    #put flux in trade
    flux = check('fluxFullHD.png', 962, 165, 1403, 984)
    time.sleep(.1)
    click(flux[0], flux[1])
    time.sleep(.1)
    Split = check('SplitFullHD.png', 962, 165, 1403, 984)
    time.sleep(.1)
    click(Split[0], Split[1])
    time.sleep(.1)
    inTrade = check('inTradeFullHD.png', 962, 165, 1403, 984)
    time.sleep(.1)
    double_click(inTrade[0], inTrade[1])
    time.sleep(.1)
    put_item_in_trade_flux_and_charcoal(1, 5, 0,'ReadyForTradeFullHD.png')

    #put cinnabar
    flux = check('CinnabarFullHD.png', 962, 165, 1403, 984)
    time.sleep(.1)
    click(flux[0], flux[1])
    time.sleep(.1)
    Split = check('SplitFullHD.png', 962, 165, 1403, 984)
    time.sleep(.1)
    click(Split[0], Split[1])
    time.sleep(.1)
    inTrade = check('inTradeFullHD.png', 962, 165, 1403, 984)
    time.sleep(.1)
    double_click(inTrade[0], inTrade[1])
    time.sleep(.1)
    put_item_in_trade(1,0,'ReadyForTradeFullHD.png')

    #put charcoal
    flux = check('CharcoalFullHD.png', 962, 165, 1403, 984)
    time.sleep(.1)
    click(flux[0], flux[1])
    time.sleep(.1)
    Split = check('SplitFullHD.png', 962, 165, 1403, 984)
    time.sleep(.1)
    click(Split[0], Split[1])
    time.sleep(.1)
    inTrade = check('inTradeFullHD.png', 962, 165, 1403, 984)
    time.sleep(.1)
    double_click(inTrade[0], inTrade[1])
    time.sleep(.1)
    put_item_in_trade_flux_and_charcoal(3, 0, 0, 'ReadyForTradeFullHD.png')

    #put ingot
    flux = check('IngotFullHD.png', 962, 165, 1403, 984)
    time.sleep(.1)
    click(flux[0], flux[1])
    time.sleep(.1)
    Split = check('SplitFullHD.png', 962, 165, 1403, 984)
    time.sleep(.1)
    click(Split[0], Split[1])
    time.sleep(.1)
    inTrade = check('inTradeFullHD.png', 962, 165, 1403, 984)
    time.sleep(.1)
    double_click(inTrade[0], inTrade[1])
    time.sleep(.1)
    put_item_in_trade(5,0,'ReadyForTradeFullHD.png')

    
#function to check if name is true than press 'f1'
#and return list with last trade nickname included
#1080, 290, 1300, 330 - 2k resolution
def check_name(y):
    im = ImageGrab.grab(bbox=(812, 216, 980, 250))
    im_for_check = pytesseract.image_to_string(cv2.cvtColor(nm.array(im), cv2.COLOR_BGR2GRAY),lang ='eng')
    x = 0
    list_for_check = im_for_check.split()
    while x < 1:
        check = any(item in list_of_nicknames(y) for item in list_for_check)
        if check is True:            
            x = x + 1
            time.sleep(.1)
            pyautogui.press('f1')
            return list_for_check
        else:
            im = ImageGrab.grab(bbox=(812, 216, 980, 250))
            im_for_check = im_for_check = pytesseract.image_to_string(cv2.cvtColor(nm.array(im), cv2.COLOR_BGR2GRAY),lang ='eng')
            list_for_check = im_for_check.split()
            print('Right now I try to find name and I see: $s' %list_for_check)
            #print(list_for_check)
            



#function for accepting trade
#2184, 934, 2500, 1100 - for accept trade check of 'locked in' and 'confirmed'
def accept_trade():
    check('LockedInFullHD.png', 1695, 694, 1850, 800)
    lockIn = check('LockinFullHD.png', 1498, 521, 1887, 617)
    click(lockIn[0], lockIn[1])
    check('ConfirmedFullHD.png', 1695, 694, 1850, 800)
    Trade = check('TradeFullHD.png', 1498, 521, 1887, 617)
    click(Trade[0], Trade[1])
    
    
#function to check 2 trades from 1 nickname
def hz(list1, list2):
    result = 0
    for x in list1:
        for y in list2:
            if x == y:
                result = result + 1
    return result


#function of full rotation
def full_rotation(y):
    a = []
    z = []
    while 1:
        print(hz(list_of_nicknames(y), a))
        z = check_name(y)
        a = a + z
        if hz(list_of_nicknames(y), a) >= 2: 
           print('Second trade I should recieve Asmodeum')
           accept_trade()
           a = []
           step('step.png', 1650, 0, 2500, 400)
        else:
           print(hz(list_of_nicknames(y), a))
           print('first trade I should give items and accept trade')
           put_all_items()
           accept_trade()




