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

#for text recognition
tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

#all nicknames
list_of_nicknames = ['chepyshara', 'chepyshila', 'obezyana', 'Eto1og', 'Arkqa', 'AsiaCute', 'Baobabo',
                     'bignachalnik', 'BlerWor', 'bogusmake', 'boldandfrown', 'borodanagolove', 'Borodazefilitsa',
                     'Brodg', 'chebyrekValek', 'chernayachepyxa', 'Chernozem', 'chipuxa', 'CHUKBUSS',
                     'Chupika', 'clychitsa', 'debbygalagher', 'Detivpered', 'Dopingrij', 'ebaboroda', 'EJChype',
                     'Eldgei', 'eminandtemy', 'europegirl', 'FEIGYN', 'fionagalagher', 'fitzezra', 'Flopiflop',
                     'frankgalagher', 'Freek', 'gebataya', 'golyboiglaz', 'golyboyglaz', 'golybyshka',
                     'Greenland', 'gybastik', 'Irokezina', 'Jargeman', 'JediAnakin', 'Jepamoya', 'Jorapapajora',
                     'Kazachek', 'kevinbowl', 'Kosichik', 'Kryzjka', 'lysyui', 'Makalorster', 'Malsih',
                     'Mashadiga', 'mechom', 'monachal', 'Nepoedynikyda', 'Netzcop', 'Normpricheska', 'nosatyi',
                     'Nozdri', 'obezyana', 'obruch', 'oliverputnam', 'Pacanka', 'Peshkomdomoy', 'PITEGRU',
                     'poidynarydy', 'Popapo', 'pornoysiki', 'Posetor', 'Pyshkingey', 'ragulivna', 'rockmountain',
                     'serenawander', 'Shop', 'ShrekAnDonkey', 'shrekkek', 'stariu', 'steverodrigez', 'Strogayatetya',
                     'teamkono', 'Valekchebyrek', 'valekloshara', 'valekrealchel', 'ValkaMechta', 'Vasechkin',
                     'Vasyapetya', 'veronikabowl', 'Vgoroshek', 'Volohata', 'Volohatyi', 'volosisyshei',
                     'xochespatb', 'yca4', 'Ycatik', 'yhogorlonos', 'Zelenskiyglas', 'zybibolyat', 'Drono',
                     'vperednogami', 'arestovuch', 'kevinbowi', 'ariamontgomeri', 'Kotya', 'MIKEMAIERS', 'tobikawana',
                     'HannaMeryn', 'sliwkom', 'chipux']

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
       print(test)
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
    active_item = check(item, 1250, 280, 2000, 1400)
    win32api.SetCursorPos((active_item[0] + 100, active_item[1])) #we need to adjust x position
    time.sleep(.1)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(.2)
    smooth_move(2035, 440)
    time.sleep(.1)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

    
#1250, 280, 2000, 1400 - items
#2007, 722, 2500, 800 - buttons
#function to put all items                 
def put_all_items():
    print('start putting items')
    #put tolvium
    flux = check('Tolvium.png',1250, 280, 2000, 1400)
    time.sleep(.1)
    click(flux[0], flux[1])
    time.sleep(.1)
    Split = check('Split.png', 1250, 280, 2000, 1400)
    click(Split[0], Split[1])
    time.sleep(.1)
    inTrade = check('inTrade.png', 1250, 280, 2000, 1400)
    time.sleep(.1)
    double_click(inTrade[0], inTrade[1])
    time.sleep(.1)
    put_item_in_trade(1,0,'ReadyForTrade.png')
    
    #put flux in trade
    flux = check('flux.png', 1250, 280, 2000, 1400)
    time.sleep(.1)
    click(flux[0], flux[1])
    time.sleep(.1)
    Split = check('Split.png', 1250, 280, 2000, 1400)
    time.sleep(.1)
    click(Split[0], Split[1])
    time.sleep(.1)
    inTrade = check('inTrade.png', 1250, 280, 2000, 1400)
    time.sleep(.1)
    double_click(inTrade[0], inTrade[1])
    time.sleep(.1)
    put_item_in_trade(1,0,'ReadyForTrade.png')

    #put cinnabar
    flux = check('Cinnabar.png', 1250, 280, 2000, 1400)
    time.sleep(.1)
    click(flux[0], flux[1])
    time.sleep(.1)
    Split = check('Split.png', 1250, 280, 2000, 1400)
    time.sleep(.1)
    click(Split[0], Split[1])
    time.sleep(.1)
    inTrade = check('inTrade.png', 1250, 280, 2000, 1400)
    time.sleep(.1)
    double_click(inTrade[0], inTrade[1])
    time.sleep(.1)
    put_item_in_trade(1,0,'ReadyForTrade.png')

    #put charcoal
    flux = check('Charcoal.png', 1250, 280, 2000, 1400)
    time.sleep(.1)
    click(flux[0], flux[1])
    time.sleep(.1)
    Split = check('Split.png', 1250, 280, 2000, 1400)
    time.sleep(.1)
    click(Split[0], Split[1])
    time.sleep(.1)
    inTrade = check('inTrade.png', 1250, 280, 2000, 1400)
    time.sleep(.1)
    double_click(inTrade[0], inTrade[1])
    time.sleep(.1)
    put_item_in_trade(2,0,'ReadyForTrade.png')

    #put ingot
    flux = check('Ingot.png', 1250, 280, 2000, 1400)
    time.sleep(.1)
    click(flux[0], flux[1])
    time.sleep(.1)
    Split = check('Split.png', 1250, 280, 2000, 1400)
    time.sleep(.1)
    click(Split[0], Split[1])
    time.sleep(.1)
    inTrade = check('inTrade.png', 1250, 280, 2000, 1400)
    time.sleep(.1)
    double_click(inTrade[0], inTrade[1])
    time.sleep(.1)
    put_item_in_trade(5,0,'ReadyForTrade.png')

    
#function to check if name is true than press 'f1'
#and return list with last trade nickname included
#1080, 290, 1300, 330 - 2k resolution
def check_name():
    im = ImageGrab.grab(bbox=(1080, 290, 1300, 330))
    #time.sleep(.1)
    im_for_check = pytesseract.image_to_string(cv2.cvtColor(nm.array(im), cv2.COLOR_BGR2GRAY),lang ='eng')
    x = 0
    list_of_nicknames = ['chepyshara', 'chepyshila', 'obezyana', 'Eto1og', 'Arkqa', 'AsiaCute', 'Baobabo',
                     'bignachalnik', 'BlerWor', 'bogusmake', 'boldandfrown', 'borodanagolove', 'Borodazefilitsa',
                     'Brodg', 'chebyrekValek', 'chernayachepyxa', 'Chernozem', 'chipuxa', 'CHUKBUSS',
                     'Chupika', 'clychitsa', 'debbygalagher', 'Detivpered', 'Dopingrij', 'ebaboroda', 'EJChype',
                     'Eldgei', 'eminandtemy', 'europegirl', 'FEIGYN', 'fionagalagher', 'fitzezra', 'Flopiflop',
                     'frankgalagher', 'Freek', 'gebataya', 'golyboiglaz', 'golyboyglaz', 'golybyshka',
                     'Greenland', 'gybastik', 'Irokezina', 'Jargeman', 'JediAnakin', 'Jepamoya', 'Jorapapajora',
                     'Kazachek', 'kevinbowl', 'Kosichik', 'Kryzjka', 'lysyui', 'Makalorster', 'Malsih',
                     'Mashadiga', 'mechom', 'monachal', 'Nepoedynikyda', 'Netzcop', 'Normpricheska', 'nosatyi',
                     'Nozdri', 'obezyana', 'obruch', 'oliverputnam', 'Pacanka', 'Peshkomdomoy', 'PITEGRU',
                     'poidynarydy', 'Popapo', 'pornoysiki', 'Posetor', 'Pyshkingey', 'ragulivna', 'rockmountain',
                     'serenawander', 'Shop', 'ShrekAnDonkey', 'shrekkek', 'stariu', 'steverodrigez', 'Strogayatetya',
                     'teamkono', 'Valekchebyrek', 'valekloshara', 'valekrealchel', 'ValkaMechta', 'Vasechkin',
                     'Vasyapetya', 'veronikabowl', 'Vgoroshek', 'Volohata', 'Volohatyi', 'volosisyshei',
                     'xochespatb', 'yca4', 'Ycatik', 'yhogorlonos', 'Zelenskiyglas', 'zybibolyat', 'Drono',
                     'vperednogami', 'arestovuch', 'kevinbowi', 'ariamontgomeri', 'Kotya', 'MIKEMAIERS', 'tobikawana',
                     'HannaMeryn', 'sliwkom', 'chipux']
    list_for_check = im_for_check.split()
    while x < 1:
        check = any(item in list_of_nicknames for item in list_for_check)
        if check is True:            
            x = x + 1
            time.sleep(.1)
            pyautogui.press('f1')
            return list_for_check
        else:
            im = ImageGrab.grab(bbox=(1080, 290, 1300, 330))
            #time.sleep(.1)
            im_for_check = im_for_check = pytesseract.image_to_string(cv2.cvtColor(nm.array(im), cv2.COLOR_BGR2GRAY),lang ='eng')
            list_for_check = im_for_check.split()
            print('Right now I try to find name and I see:' %list_for_check)
            print(list_for_check)
            


#function to check color in settled pixel pos
#X: 2396 Y: 1010 RGB: (181, 181, 181) - white
#(35, 162, 121) - green
#1650, 0, 2500, 400 - step
def check_pixel_color(x, y , ra, ga, ba):
    a = 0
    while a < 1:
        r = pyautogui.pixel(x, y)
        if r == (ra, ga, ba):
            a = a + 1
            return True

#function for accepting trade
#2184, 934, 2500, 1100 - for accept trade check of 'locked in' and 'confirmed'
def accept_trade():
    check('LockedIn.png', 2184, 934, 2500, 1100)
    lockIn = check('Lockin.png', 2007, 722, 2500, 800)
    click(lockIn[0], lockIn[1])
    check('Confirmed.png', 2184, 934, 2500, 1100)
    Trade = check('Trade.png', 2007, 722, 2500, 800)
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
def full_rotation():
    a = []
    z = []
    while 1:
        print(hz(list_of_nicknames, a))
        z = check_name()
        a = a + z
        if hz(list_of_nicknames, a) >= 2: 
           print('Second trade I should recieve Asmodeum')
           accept_trade()
           a = []
           step('step.png', 1650, 0, 2500, 400)
        else:
           print('first trade I should give items and accept trade')
           put_all_items()
           accept_trade()


full_rotation()



