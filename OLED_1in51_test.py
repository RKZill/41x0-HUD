#!/usr/bin/python
# -*- coding:utf-8 -*-

import sys
import os
picdir = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'pic')
libdir = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'lib')
if os.path.exists(libdir):
    sys.path.append(libdir)

import logging    
import time
import traceback
from waveshare_OLED import OLED_1in51
from PIL import Image,ImageDraw,ImageFont
logging.basicConfig(level=logging.DEBUG)

try:
    #outline function
    def outline(draw):
        draw.line([(0,0),(127,0)], fill = 0)
        draw.line([(0,0),(0,63)], fill = 0)
        draw.line([(0,63),(127,63)], fill = 0)
        draw.line([(127,0),(127,63)], fill = 0)
    
    def leftTurn(draw, distance):
        disp.clear()
        image1 = Image.new('1', (disp.width, disp.height), "WHITE")
        draw = ImageDraw.Draw(image1)
        #outline(draw)
        draw.line([(20,40),(100,40)], fill = 0) #thick line
        draw.polygon([(20,60),(20,20),(2,40)], fill=0) #head of triangle
        logging.info ("***Turn LEFT")
        draw.text((1,0), 'Turn Left '+distance, font = font1, fill = 0)
        image1 = image1.rotate(180) 
        disp.ShowImage(disp.getbuffer(image1))
        time.sleep(3)
        
    def rightTurn(draw, distance):
        disp.clear()
        image1 = Image.new('1', (disp.width, disp.height), "WHITE")
        draw = ImageDraw.Draw(image1)
        #outline(draw)
        draw.line([(0,40),(100,40)], fill = 0) #thick line
        draw.polygon([(100,60),(100,20),(120,40)], fill=0) #head of triangle
        logging.info ("***Turn Right")
        draw.text((2,0), 'Turn Right '+distance, font = font1, fill = 0)
        image1 = image1.rotate(180) 
        disp.ShowImage(disp.getbuffer(image1))
        time.sleep(3)
        
    def goStraight(draw, distance):
        disp.clear()
        image1 = Image.new('1', (disp.width, disp.height), "WHITE")
        draw = ImageDraw.Draw(image1)
        #outline(draw)
        draw.line([(60,30),(60,63)], fill = 0) #thick line
        draw.polygon([(40,40),(80,40),(60,20)], fill=0) #head of triangle
        logging.info ("***Turn LEFT")
        draw.text((1,0), 'Go Straight '+distance, font = font05, fill = 0)
        image1 = image1.rotate(180) 
        disp.ShowImage(disp.getbuffer(image1))
        time.sleep(3)
    
    
    
    disp = OLED_1in51.OLED_1in51()
    logging.info("\r1.51inch OLED ")
    # Initialize library.
    disp.Init()
    # Clear display.
    logging.info("clear display")
    disp.clear()
    # Create blank image for drawing.
    image1 = Image.new('1', (disp.width, disp.height), "WHITE")
    draw = ImageDraw.Draw(image1)
    font05 = ImageFont.truetype(os.path.join(picdir, 'Font.ttc'), 15)
    font1 = ImageFont.truetype(os.path.join(picdir, 'Font.ttc'), 18)
    font2 = ImageFont.truetype(os.path.join(picdir, 'Font.ttc'), 24)
    logging.info ("***draw line")
    
    leftTurn(draw, '100m')
    rightTurn(draw, '21km')
    goStraight(draw, '2km')
    
    #logging.info ("***draw image")
    #Himage2 = Image.new('1', (disp.width, disp.height), 255)  # 255: clear the frame
    #bmp = Image.open(os.path.join(picdir, 'right-arrow.bmp'))
    #Himage2.paste(bmp, (0,0))
    #Himage2=Himage2.rotate(180) 	
    #disp.ShowImage(disp.getbuffer(Himage2))
    #draw.text((10,0), '500m', font = font2, fill = 0)
    time.sleep(4)    
    disp.clear()
    
except IOError as e:
    logging.info(e)
    
except KeyboardInterrupt:    
    logging.info("ctrl + c:")
    OLED_1in51.config.module_exit()
    exit()