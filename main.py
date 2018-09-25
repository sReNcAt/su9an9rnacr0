import pyautogui
import cv2
import numpy as np
#from matplotlib import pyplot as plt
#import imutils
import time, sys
import getpass
import ctypes
import requests,json

user32 = ctypes.windll.user32
screensize = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)
cutline_x=250
cutline_y=815
sys.setrecursionlimit(5000)
class cutline_init():
    def __init__(self):
        print("1")
        print(screensize)
        self.display_w,self.display_h = pyautogui.size()
        self.img = pyautogui.screenshot(region=(self.display_w/2,0,self.display_w/2,self.display_h))
        self.img = cv2.cvtColor(np.array(self.img), cv2.COLOR_RGB2BGR)
        self.img2 = self.img.copy()
        self.template = cv2.imread('cutline.png')
        self.c,self.w, self.h = self.template.shape[::-1]
        self.methods = ['cv2.TM_CCOEFF_NORMED']

    def search(self):
        global cutline_x
        global cutline_y
        for meth in self.methods:
            img = self.img2.copy()
            method = eval(meth)
            res = cv2.matchTemplate(img,self.template,method)
            min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
            if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
                top_left = min_loc
            else:
                top_left = max_loc
            bottom_right = (top_left[0] + self.w + self.display_w/2, top_left[1] + self.h)
            cutline_x=top_left[0]-150
            cutline_y=top_left[1]
            print("%s , %s"%(cutline_x,cutline_y))
        return None

class sugang():
    def __init__(self):
        print("1")
        print(screensize)
        self.display_w,self.display_h = pyautogui.size()
        self.img = pyautogui.screenshot(region=(self.display_w/2,0,self.display_w/2,self.display_h))
        self.img = cv2.cvtColor(np.array(self.img), cv2.COLOR_RGB2BGR)
        self.img2 = self.img.copy()
        self.template = cv2.imread('search.png')
        self.c,self.w, self.h = self.template.shape[::-1]
        self.methods = ['cv2.TM_CCOEFF_NORMED']
        #self.methods = ['cv2.TM_CCOEFF', 'cv2.TM_CCOEFF_NORMED', 'cv2.TM_CCORR','cv2.TM_CCORR_NORMED', 'cv2.TM_SQDIFF', 'cv2.TM_SQDIFF_NORMED']

    def search(self):
        for meth in self.methods:
            img = self.img2.copy()
            method = eval(meth)
            res = cv2.matchTemplate(img,self.template,method)
            min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
            if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
                top_left = min_loc
            else:
                top_left = max_loc
            bottom_right = (top_left[0] + self.w + self.display_w/2, top_left[1] + self.h)
            base_po=pyautogui.position()
            pyautogui.moveTo(top_left[0] + self.w/2 + self.display_w/2,top_left[1] + self.h/2)
            pyautogui.doubleClick()
            pyautogui.moveTo(base_po)
        return None

class search_learn():
    def __init__(self):
        self.display_w,self.display_h = pyautogui.size()
        self.img = pyautogui.screenshot(region=(0,self.display_h/2,self.display_w,self.display_h/2))
        self.img = cv2.cvtColor(np.array(self.img), cv2.COLOR_RGB2BGR)
        self.img2 = self.img.copy()
        self.template = cv2.imread('learn.png')
        self.c,self.w, self.h = self.template.shape[::-1]
        self.methods = ['cv2.TM_CCOEFF_NORMED']

    def search(self):
        for meth in self.methods:
            img = self.img2.copy()
            method = eval(meth)
            res = cv2.matchTemplate(img,self.template,method)
            min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
            if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
                top_left = min_loc
            else:
                top_left = max_loc
            bottom_right = (top_left[0] + self.w, top_left[1] + self.h)
            if(top_left[1] + self.h/2 + self.display_h/2<cutline_y and top_left[0] + self.w/2>cutline_x):
                pyautogui.moveTo(top_left[0] + self.w/2 ,top_left[1] + self.h/2 + self.display_h/2)
                pyautogui.doubleClick()
                time.sleep(1)
                pyautogui.moveTo(1085,605)
                pyautogui.doubleClick()
            print((top_left[0] + self.w/2 ,top_left[1] + self.h/2 + self.display_h/2))
        return None

def sugang_loop():
    gasang=cutline_init()
    gasang.search()
    j=1
    time.sleep(1.0)
    while True:
        print("%stry..."%j)
        gasang=sugang()
        gasang.search()
        time.sleep(0.1)
        start_time=time.time()
        i=1
        while True:
            if(time.time()-start_time>=5):
                break
            else:
                if(i<=10):
                    print("%stry search add (%s/s)"%(i,(time.time()-start_time)))
                    learn=search_learn()
                    learn.search()
                i+=1
        j+=1
if __name__ == '__main__':
    sugang_loop()
