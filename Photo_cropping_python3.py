#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 29 13:19:17 2020

@author: lion
"""

import argparse
import time
from time import sleep
from PIL import Image  
from natsort import natsorted
import progressbar
import os


# define the name of the directory to be created
bar = progressbar.ProgressBar(maxval=20, \
widgets=[progressbar.Bar('=', '[', ']'), ' ', progressbar.Percentage()])
path = "resized_images"
s = time.time()
f = time.time() #It gives you the time for processing in Second

try:
    os.mkdir(path)
except OSError:
    print ("Creation of the directory %s failed" % path)
else:
    print ("Successfully created the directory %s" % path)
   

def Crop_images(dataset):
    img_list= []
    resized_img= []
    img_list.clear()
    resized_img.clear() 
    print("Enter the left size:")
    left = int(input())
    print("Enter the top size:")
    top = int(input())
    print("Enter the right size:")
    right = int(input())
    print("Enter the bottom size:")
    bottom = int(input())

    for img in natsorted(os.listdir((dataset))):
        
        image1 = Image.open(dataset+img)
        img_list.append(image1)
        width, height = image1.size
        crop1 = image1.crop((left, top, right, bottom))
        resized_img.append(crop1)
        #cropp.show()
        print(img)
        print("Image format: {}".format(image1.format))
        print("image size: {}".format(crop1.size))
        print("image mode: {}".format(crop1.mode))
        
        #Bar progress    
        bar.start()
        for i in range(20):
            bar.update(i+1)
            sleep(0.001)
        bar.finish()
    
        for (i, new) in enumerate(resized_img):
            new.save("{}{}{}".format("resized_images/Image",i+1,".jpg"))

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Rescale images")
    parser.add_argument('-ds', '--dataset', type=str, required=True, help='Dataset containing the images')
    #parser.add_argument('-d', '--directory', type=str, required=True, help='Dataset saving the images')
    args = parser.parse_args()
    Crop_images(args.dataset)
    
Crop_images()
print(str(f-s) + " Second")
    