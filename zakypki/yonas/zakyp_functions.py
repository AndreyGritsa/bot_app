import pyautogui
import random
import time
import pytesseract
from PIL import ImageGrab, Image
import cv2
import numpy as nm
import datetime
import PIL
tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def check_count(item):
    return list(pyautogui.locateAllOnScreen(item,
                                            region=(1267, 17, 1908, 1030),
                                            grayscale=False, confidence=0.9))

def locate_all(item, distance=10):
    distance = pow(distance, 2)
    elements = []
    for element in pyautogui.locateAllOnScreen(item, region=(1267, 17, 1908, 1030),
                                               confidence=0.9):
        if all(map(lambda x: pow(element.left - x.left, 2) +
                   pow(element.top - x.top, 2) > distance, elements)):
            elements.append(element)
    return elements

#class for finding position of required item
#and do whatever we need with this info
class Check(object):

    def __init__(self, item, x, y, w, h):
        self.item = item
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        a = 0
        self.test =[]
        while a < 1:
            self.test = pyautogui.locateOnScreen(self.item, region=(self.x,
                                                                    self.y,
                                                                    self.w,
                                                                    self.h),
                                                 grayscale=True, confidence=0.9) 
            if self.test is not None:
                a = a + 1

    def just_check(self):
        if self.test is not None:
            return self.test       

    def check_f_click(self):        
        pyautogui.moveTo(self.test[0], self.test[1])
        time.sleep(1)
        pyautogui.click(clicks=2, interval=random.uniform(.2, .3))

    def check_click(self):
        pyautogui.moveTo(self.test[0], self.test[1])
        time.sleep(.1)
        pyautogui.click()

    def check_click_distance(self, distance):
        self.distance = distance
        pyautogui.moveTo(self.test[0]+distance, self.test[1])
        time.sleep(.1)
        pyautogui.click()

    def check_click_distance_y(self, distance):
        self.distance = distance
        pyautogui.moveTo(self.test[0], self.test[1]+distance)
        time.sleep(.1)
        pyautogui.click()

    def check_click_distance_y_double(self, distance):
        self.distance = distance
        pyautogui.moveTo(self.test[0], self.test[1]+distance)
        time.sleep(.1)
        pyautogui.click(clicks=2, interval=random.uniform(.1, .2))          

    def check_click_distance_double(self, distance):
        self.distance = distance
        pyautogui.moveTo(self.test[0]+distance, self.test[1])
        time.sleep(.1)
        pyautogui.click(clicks=2, interval=random.uniform(.1, .2))


def update_zakyp(item, rquired_amount, amount, price):
    amount = rquired_amount - amount
    if amount <= 0:
        with open('zakyp.py', 'r+') as f:
            data = f.readlines()
            f.seek(0)
            for i in data:
                if item in i:
                    i = f"#buy_item('{item}', {amount}, 'up_to_{price}')\n"
                f.write(i)
            f.close()
    else:
        with open('zakyp.py', 'r+') as f:
            data = f.readlines()
            f.seek(0)
            for i in data:
                if item in i:
                    i = f"buy_item('{item}', {amount}, 'up_to_{price}')\n"
                f.write(i)
            f.close()

def update_zakyp_count(item, requierd_amount, price):
    with open('zakyp_count.py', 'r+') as f:
        data = f.readlines()
        f.seek(0)
        for i in data:
            if item in i:
                i = f"#count_rotation('{item}', {requierd_amount}, {price})\n"
            f.write(i)
        f.close()

def update_zakyp_hesh(file, item):
    with open(file, 'r+') as f:
        data = f.readlines()
        f.seek(0)
        for i in data:
            if item in i:
                i = '#' + i 
            f.write(i)
        f.close()

def clean(file):
    with open(file, 'r+') as f:
        data = f.readlines()
        f.seek(0)
        for a in file:
            f.truncate()
        f.seek(0)
        for i in data:
            if '#' in i and not '#_' in i and not '-' in i:
                i = i.replace('#', '')
            elif 'clean' in i:
                i = '#' + i
            f.write(i)
            if '#_______________________________________' in i:
                break
        f.close()
        print('Cleaned')
    

def change_city(city, up_down):
    search = Check(r'C:\Python\projects\zakypki\screens\storage_location.png',
                   0, 0, 1920, 1080)
    search.check_click_distance_y(30)
    #1562, 434
    time.sleep(.2)
    pyautogui.moveTo(1562, 434)
    time.sleep(.1)
    pyautogui.scroll(up_down)
    time.sleep(.1)
    search = Check(f'C:\Python\projects\zakypki\screens\{city}.png',
                   0, 0, 1920, 1080)    
    search.check_click()
    
def count_rotation(item, requierd_amount, price):
    amount = 0
    change_city('ebonscale_reach', 900)    
    search = Check(r'C:\Python\projects\zakypki\screens\storage_shed.png',
                   0, 0, 1920, 1080)
    search.check_click_distance_y_double(65)
    if 'iron' in item:
        for_type = 'iron'
    elif 'orichalcum' in item:
        for_type = 'orichalcum'
    elif 'starmetal' in item:
        for_type = 'starmetal'
    else:
        for_type = item.replace('_', ' ')
    pyautogui.typewrite(for_type, interval=random.uniform(.1, .2))
    amount += count_amount(item)

    change_city('brightwood', 900)
    amount += count_amount(item)

    change_city('mourningdale', -900)
    amount += count_amount(item)

    change_city('weavers_fen', -900)
    amount += count_amount(item)

    change_city('restless_shore', -900)
    amount += count_amount(item)

    change_city('reekwater', -900)
    amount += count_amount(item)

    amount = int(amount)
    print(f'items in total: {amount}')

    update_zakyp(item, requierd_amount, amount, price)
    update_zakyp_count(item, requierd_amount, price)

def count_amount(item):
    a = []
    x = 0
    y = 0
    amount = 0
    time.sleep(1)
    box = locate_all(f'C:\Python\projects\zakypki\screens\{item}1.png')                  
    print(box)
    for i in box:
        for k in i:
            a.append(k)
            print(a)
    while len(a) != 0:
        count = 0
        x, y = a[0], a[1]
        print(x, y)
        del a[0:4]
        b = 0
        #im = cv2.cvtColor(nm.array(im), cv2.COLOR_BGR2GRAY)
        #im = Image.fromarray(im, 'RGB')
        pyautogui.moveTo(0, 1070)
        pyautogui.moveTo(x, y)
        search = Check(r'C:\Python\projects\zakypki\screens\weight.png',
                       0, 0, 1920, 1080)
        weight = search.just_check()
        x, y = weight[0], weight[1]
        im = ImageGrab.grab(bbox=(x-70, y, x-5, y+20))
        #im.save('im.png')
        try:
            while b == 0:
                #im = cv2.cvtColor(nm.array(im), cv2.COLOR_BGR2GRAY)
                im_for_check = pytesseract.image_to_string(im, config='--psm 7')
                im_for_check = ''.join((ch if ch in '0123456789.-e' else '')
                                        for ch in im_for_check)
                im_for_check = im_for_check.replace('\n', '')
                print(im_for_check)
                if float(im_for_check) > 3000 and not '.' in im_for_check:
                    im_for_check = im_for_check[:3] + '.' + im_for_check[3:]
                amount += float(im_for_check)
                print("amount: %d" % amount)
                if float(im_for_check):
                    b = 1
        except:
            time.sleep(.5)
            search = Check(r'C:\Python\projects\zakypki\screens\weight.png',
                           0, 0, 1920, 1080)
            weight = search.just_check()
            x, y = weight[0], weight[1]
            im = ImageGrab.grab(bbox=(x-56, y, x-5, y+20))
            im.save('im.png')
            im_for_check = pytesseract.image_to_string(im, config='--psm 13')
            im_for_check = ''.join((ch if ch in '0123456789.-e' else '')
                                    for ch in im_for_check)
            im_for_check = im_for_check.replace('\n', '')
            if float(im_for_check) > 3000 and not '.' in im_for_check:
                im_for_check = im_for_check[:3] + '.' + im_for_check[3:]
            print(im_for_check)
            amount += float(im_for_check)
            print("amount: %d" % amount)
    pyautogui.moveTo(0, 1070)
    if item == 'wirefiber' or (item == 'obsidian_flux' or
                               item == 'wireweave' or
                               item == 'aged_tannin' or
                               item == 'fibers' or
                               item == 'silk_threads' or
                               item == 'infused_silk'
                               ):
        return amount / 0.1
    elif item == 'tolvium' or (item == 'cinnabar' or
                               item == 'scarhide' or
                               item == 'smolderhide' or
                               item == 'scalecloth' or
                               item == 'blisterweave' or
                               item == 'orichalcum_ingot'
                                ):
        return amount / 0.3
        
    else:
        return amount / 0.2

#rotation to put order with item that's
#already found, we take amount and price
#as arguments
def rotation(amount, price):
    search = Check(r'C:\Python\projects\zakypki\screens\place_buy_order.png',
                   0, 0, 1920, 1080)
    search.check_click()

    search = Check(r'C:\Python\projects\zakypki\screens\arrow_down.png',
                   0, 0, 1920, 1080)
    search.check_click_distance(400)

    search = Check(r'C:\Python\projects\zakypki\screens\1_day.png',
                   0, 0, 1920, 1080)
    search.check_click()

    search = Check(r'C:\Python\projects\zakypki\screens\unit_price.png',
                   0, 0, 1920, 1080)
    search.check_click_distance_double(500)
    pyautogui.typewrite(str(price), interval=random.uniform(.1, .2))

    search = Check(r'C:\Python\projects\zakypki\screens\quantity.png',
                   0, 0, 1920, 1080)
    search.check_click_distance_double(400)
    pyautogui.typewrite(str(amount), interval=random.uniform(.1, .2))
    if float(price) - 0.01 <= price_check_secure() <= float(price) + 0.01:
        search = Check(r'C:\Python\projects\zakypki\screens\place_order.png',
                   0, 0, 1920, 1080)
        search.check_click()
    else:
        first_rotation_for_upto(amount, price)

#rotation for the first order, when we just
#have decided the price
def first_rotation_for_upto(amount, price):
    search = Check(r'C:\Python\projects\zakypki\screens\arrow_down.png',
                   0, 0, 1920, 1080)
    search.check_click_distance(400)

    search = Check(r'C:\Python\projects\zakypki\screens\1_day.png',
                   0, 0, 1920, 1080)
    search.check_click()

    search = Check(r'C:\Python\projects\zakypki\screens\unit_price.png',
                   0, 0, 1920, 1080)
    search.check_click_distance_double(500)
    pyautogui.typewrite(str(price), interval=random.uniform(.1, .2))

    search = Check(r'C:\Python\projects\zakypki\screens\quantity.png',
                   0, 0, 1920, 1080)
    search.check_click_distance_double(400)
    pyautogui.typewrite(str(amount), interval=random.uniform(.1, .2))
    if float(price) - 0.01 <= price_check_secure() <= float(price) + 0.01:
        search = Check(r'C:\Python\projects\zakypki\screens\place_order.png',
                       0, 0, 1920, 1080)
        search.check_click()
    else:
        first_rotation_for_upto(amount, price)

def amount_adjusted(item, amount, price):
      if amount > 10000:
            a = amount % 10000
            b = int(amount / 10000)
            c = 0
            while  c < b + 1:
                  if c == b:
                        amount = a
                        if amount == 0:
                              return None
                  else:
                        amount = 10000
                  c += 1
                  rotation(amount, price)
                  file_update(item, amount, price)
            return None
   
      rotation(amount, price)
      file_update(item, amount, price)

def amount_adjusted_for_upto(item, amount, price): #18 000
      if amount > 10000: #True
            first_rotation_for_upto('10000', price) #do
            file_update(item, '10000', price)
            a = amount % 10000 #8 000
            b = int(amount / 10000) #1
            c = 1
            while  c < b + 1: #1 < 1 + 1 #break
                  if c == b:
                        amount = a
                        if amount == 0:
                              return None
                  else:
                        amount = 10000
                  c += 1 #2
                  rotation(amount, price)
                  file_update(item, amount, price)
            return None
      
      first_rotation_for_upto(amount, price)
      file_update(item, amount, price)


def buy_item(item, amount, price):
    date()
    search = Check(r'C:\Python\projects\zakypki\screens\search.png',
                   0, 0, 1920, 1080)
    search.check_f_click()

    for_type = item.replace('_', ' ')
    pyautogui.typewrite(for_type, interval=random.uniform(.1, .2))
    search = Check(f'C:\Python\projects\zakypki\screens\{item}.png',
                   0, 0, 1920, 1080)
    search.check_click()

    try:
        if 'up_to' in price:
            maximum = ''.join((ch if ch in '0123456789.-e' else ' ')
                              for ch in price)
            search = Check(r'C:\Python\projects\zakypki\screens\place_buy_order.png',
                           0, 0, 1920, 1080)
            search.check_click()
            print("maximum is: " + str(maximum))
            try:
                price = float(price_check(float(maximum))) + 0.01
                if len(str(price)) > 5:
                      print("Price before change: " + str(price))
                      price = str(price)
                      price = price[0:5]
                      print("Price after change: " + price)
                print("price to put: " + str(price))
                amount_adjusted_for_upto(item, amount, price)
                update_zakyp_hesh('zakyp.py', item)
                return None
            except:
                pyautogui.hotkey('esc')
                return None
    except:
        print("I skipped up_to cause there is no in the price")

    amount_adjusted(item, amount, price)
    if float(price) > 0.01:
        update_zakyp_hesh('zakyp.py', item)
    else:
        update_zakyp_hesh('0.01.py', item)

#1275, 261, 1326, 298
def price_check(maximum):
    while True:
        search = Check(f'C:\Python\projects\zakypki\screens\price.png',
                       0, 0, 1920, 1080)
        search.just_check()
        time.sleep(.5)
        im = ImageGrab.grab(bbox=(1275, 261, 1326, 298))
        im_for_check = pytesseract.image_to_string(cv2.cvtColor\
                                                   (nm.array(im),
                                                    cv2.COLOR_BGR2GRAY),
                                                   lang ='eng',
                                                   config='--psm 7')
        print(im_for_check)
        if 'oul' in im_for_check:
            im_for_check = '0.11'
        im_for_check = ''.join((ch if ch in '0123456789.' else '')
                               for ch in im_for_check)
        im_for_check = im_for_check.replace(' ', '')       
        if ':' in im_for_check:
            im_for_check = im_for_check.replace(':', '.')
        if 'oO.' in im_for_check:
            im_for_check = '0.11'
        if 'O' in im_for_check:
            im_for_check = im_for_check.replace('O', '0')
        if ',' in im_for_check:
            im_for_check = im_for_check.replace(',', '')
        try:
            if float(im_for_check) and not '.' in im_for_check:
                print("I should add point(.) to the string")
                if len(im_for_check) <= 3:
                    im_for_check = im_for_check[:1] + '.' + im_for_check[1:]
                else:
                    im_for_check = im_for_check[:2] + '.' + im_for_check[2:]
            print("added point(.) to the string, string: %r" % im_for_check)
        except:
            print("Error occured while attemting to add point(.) to the string")
        try:
            if '.' in im_for_check:
                if float(im_for_check) > maximum:
                    return None
                else:
                    return float(im_for_check)
        except:
            print("I try to find the price")
            
#958, 283, 1013, 321
def price_check_secure():
    while True:
        im = ImageGrab.grab(bbox=(958, 283, 1013, 321))
        im_for_check = pytesseract.image_to_string(cv2.cvtColor\
                                                   (nm.array(im),
                                                    cv2.COLOR_BGR2GRAY),
                                                   lang ='eng',
                                                   config='--psm 7')
        im_for_check = ''.join((ch if ch in '0123456789.' else ' ')
                              for ch in im_for_check)
        print('I check price for security, price: %r' % im_for_check)
        im_for_check = im_for_check.replace(' ', '')
        if ':' in im_for_check:
            im_for_check = im_for_check.replace(':', '.')
        if 'oO.' in im_for_check:
            im_for_check = '0.11'
        if 'O' in im_for_check:
            im_for_check = im_for_check.replace('O', '0')
        if ',' in im_for_check:
            im_for_check = im_for_check.replace(',', '')
        if float(im_for_check) and not '.' in im_for_check:
            if len(im_for_check) <= 3:
                im_for_check = im_for_check[:1] + '.' + im_for_check[1:]
            else:
                im_for_check = im_for_check[:2] + '.' + im_for_check[2:]
        if 'A' in im_for_check:
            im_for_check = im_for_check.replace('A', '.')
        print('I check price for security(after changes), price: %r' % im_for_check)
        if float(im_for_check):
            return float(im_for_check)
    

def date():

      #if today's date and name of the server are already in file,
      #return none
      with open('order_history.txt', 'r') as f:
            data = f.readlines()
            today = datetime.datetime.today()
            date = today.strftime("%b-%d-%Y")
            try:
                  if data.index(date + '\n'): #and
                      #data.index(date + '\n')):
                        return None
            except:
                  pass

      #write today's date    
      with open('order_history.txt', 'a+') as f:
            today = datetime.datetime.today()
            d = today.strftime("%b-%d-%Y")
            f.seek(0)
            f.write('\n' + '-' * 10 + "Last session" +\
                    '-' * 10 + '\n' + d + #'\n' + str(server) +\
                    '\n' + '-' * 10 + '\n')
            f.close()

      #delete what's before first apperance of today's date     
      with open('order_history.txt') as f:
          data = list(f.readlines())
          date = today.strftime("%b-%d-%Y")
          count = data.index(date+'\n')
          del data[0:count - 1]
          with open('order_history.txt', 'w') as f:
              for i in data:
                  f.write(i)
          f.close()

def file_update(item, amount, price):
    with open('order_history.txt', 'r+') as f:
        f.readlines()
        if len(item) < 8:
            f.write('\n' + str(item) + '\t\t' + str(amount) + '\t' + str(price))
        else:
            f.write('\n' + str(item) + '\t' + str(amount) + '\t' + str(price))
        f.close()


#_____Functions for counting of final refining items_____
#________________________________________________________

def count_rotation_last(item):
    amount = 0
    change_city('brightwood', 900)    
    search = Check(r'C:\Python\projects\zakypki\screens\storage_shed.png',
                   0, 0, 1920, 1080)
    search.check_click_distance_y_double(65)    
    for_type = item.replace('_', ' ')
    pyautogui.typewrite(for_type, interval=random.uniform(.1, .2))
    amount += count_amount(item)

    change_city('brimstone', 900)
    amount += count_amount(item)

    change_city('cleave', 900)
    amount += count_amount(item)

    change_city('cutlass', 900)
    amount += count_amount(item)

    change_city('eastburn', 900)
    amount += count_amount(item)

    change_city('ebonscale_reach', 900)
    amount += count_amount(item)

    change_city('everfall', 900)
    amount += count_amount(item)

    change_city('first', 900)
    amount += count_amount(item)

    change_city('last', 900)
    amount += count_amount(item)

    change_city('monarch', 900)
    amount += count_amount(item)

    change_city('mountainhome', 900)
    amount += count_amount(item)

    change_city('mountainrise', -900)
    amount += count_amount(item)

    change_city('mourningdale', -900)
    amount += count_amount(item)

    change_city('reekwater', -900)
    amount += count_amount(item)

    change_city('restless_shore', -900)
    amount += count_amount(item)

    change_city('taberna', -900)
    amount += count_amount(item)

    change_city('valor', -900)
    amount += count_amount(item)

    change_city('weavers_fen', -900)
    amount += count_amount(item)

    change_city('wikala', -900)
    amount += count_amount(item)

    change_city('windsward', -900)
    amount += count_amount(item)

    amount = int(amount)
    print(f'items in total: {amount}')

    return amount

#orichalcum ingot - (green wood - 7.36, flux - 2.58, iron ore - 7.56,
#                    starmetal ore - 5.64, orichalcum ore - 6.02)
#infused silk - (wireweave - 2.58, fibers - 10.08, silk threads - 5.64,
#                wirefiber - 6.02)
#infused leather - (aged tannin - 2.58, rawhide - 10.08, thick hide - 5.64,
#                   iron hide - 6.02)
def math(item, amount):
    DICT = {}
    if item == 'orichalcum_ingot':
        DICT['green_wood'] = int(amount * 7.36)
        DICT['obsidian_flux'] = int(amount * 2.58)
        DICT['iron_ore'] = int(amount * 7.56)
        DICT['starmetal_ore'] = int(amount * 5.64)
        DICT['orichalcum_ore'] = int(amount * 6.02)
        return DICT
    elif item == 'infused_silk':
        DICT['wireweave'] = int(amount * 2.58)
        DICT['fibers'] = int(amount * 10.08)
        DICT['silk_threads'] = int(amount * 5.64)
        DICT['wirefiber'] = int(amount * 6.02)
        return DICT
    elif item == 'infused_leather':
        DICT['aged_tannin'] = int(amount * 2.58)
        DICT['rawhide'] = int(amount * 10.08)
        DICT['thick_hide'] = int(amount * 5.64)
        DICT['iron_hide'] = int(amount * 6.02)
        return DICT
    else:
        return None

def f_update(items):
    with open('zakyp_count.py', 'r+') as f:
        data = f.readlines()
        f.seek(0)
        f.truncate()
        f.seek(0)
        for i in data:
            for key in items:
                if key in i:
                    price = float(i[i.index(')')-4:i.index(')')])
                    requierd_amount = items[key]
                    if requierd_amount <= 0:
                        i = (f"#count_rotation('{key}', {requierd_amount},"
                             f" {price})\n")
                    else:
                        i = (f"count_rotation('{key}', {requierd_amount},"
                             f" {price})\n")
            f.write(i)
            if '#_______________________________________' in i:
                break
            
        f.close()
        print("Updated")

def set_to(item, amount):
    if item == 'Asmodeum':
        item = 'orichalcum_ingot'
    elif item == 'Runic Leather':
        item = 'infused_leather'
    elif item == 'Phoenixweave':
        item = 'infused_silk'
    items = math(item, (amount  * 50) + 10)
    
    if items is not None:
        f_update(items)
    else:
        print("Items is None and I didn't update the file")

def count_and_set(amount):
    amount = int(amount / 3)
    amount1 = amount - count_rotation_last('orichalcum_ingot') / 50
    set_to('Asmodeum', amount1)
    
    amount2 = amount - count_rotation_last('infused_leather') / 50
    set_to('Runic Leather', amount2)
    
    amount3 = amount - count_rotation_last('infused_silk') / 50
    set_to('Phoenixweave', amount3)





