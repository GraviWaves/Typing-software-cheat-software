# -*- coding: utf-8 -*-
"""
°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°
                    Keyboard Jump cheat software                         
                        Coded by Mirko Romano
°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°
"""

import pytesseract
import PIL.ImageOps 
from pynput.keyboard import Key, Listener, Controller
import time
import PIL.ImageGrab


#Set the word position coordinate (on my screen). Look if this coordinate are appropriate for you and in case, change them.
word_position = [688, 316, 1217, 380]
level = 0
loop = False
#-------------------------------------------------------
#                 KeyListener
#-------------------------------------------------------
def on_press(key):
    global loop
    #print('{0} pressed'.format(
        #key))
    if key == Key.esc:
        loop = False
        
       
def on_release(key):
    global loop
    
    #print('{0} release'.format(
       # key))
    
    if key == Key.backspace:
        loop = True
        lets_loop()
        
    if key == Key.esc:
        loop = False
        # Stop listener
        return False

#-------------------------------------------------------
#                 Keyboard Output
#-------------------------------------------------------
        
def lets_cheat(word):
    keyboard = Controller()
    time.sleep(1)

    #Give an imput from the keyboard as the same as by typing
    for char in word:
        keyboard.press(char)
        keyboard.release(char)
        time.sleep(0.04)


def take_that_word():
    #transform the screenshot in word
    screen = pytesseract.image_to_string('Images/fuckingGame.jpg')
    
    #Because pytesseract return, sometimes, upper case, transform all word in lower
    for c in screen:
        if c.isalpha():
            c.lower()
            
    print("The word is: ", screen)
    print("")
    
    lets_cheat(screen)

def take_and_convert_the_screen():
    image_mean = []
    
    #Take a screenshot of the screen (only the place where the word are in the game)
    im = PIL.ImageGrab.grab(bbox=(word_position[0], word_position[1], word_position[2], word_position[3])).convert('RGB')     
      
    #Analyze the pixel's rgb 
    width = im.width
    height = im.height
    
    image_mean.append(lets_do_the_mean(im, width, height))
    level = analyze_that_level(image_mean[0][0], image_mean[0][1], image_mean[0][2])
    
    print("Level: ", level)
    print("RGB mean: ", image_mean[0][0], image_mean[0][1], image_mean[0][2])
    
    for w in range(0, width):
        for h in range(0, height):
            current_color = im.getpixel((w,h))
            
            if level == 1:
                if current_color[0] >= 240 and current_color[1] >= 240 and current_color[2] >= 240:
                   new_color = (255, 255, 255)
                else:
                    new_color = (0, 0, 0)            
                    im.putpixel((w, h), new_color)

            elif level == 2:              
                if (current_color[0] >= 100 and current_color[0] <= 200) and (current_color[1] >= 110 and current_color[1] <= 250) and (current_color[2] >= 100 and current_color[2] <= 220):
                    new_color = (255, 255, 255)
                else:
                    new_color = (0, 0, 0)            
                    im.putpixel((w, h), new_color)    
           
            elif level == 3:
                if (current_color[0] >= 200 and current_color[0] <= 250) and (current_color[1] >= 200 and current_color[1] <= 250) and (current_color[2] >= 200 and current_color[2] <= 250):
                    new_color = (255, 255, 255)
                else:
                    new_color = (0, 0, 0)            
                    im.putpixel((w, h), new_color)  
            
            elif level == 4:

                if (current_color[0] >= 150 and current_color[0] <= 250) and (current_color[1] >= 180 and current_color[1] <= 260) and (current_color[2] >= 200 and current_color[2] <= 250):
                    new_color = (255, 255, 255)
                else:
                    new_color = (0, 0, 0)            
                    im.putpixel((w, h), new_color) 
               
                
            elif level == 5:
                if (current_color[0] >= 200 and current_color[0] <= 250) and (current_color[1] >= 210 and current_color[1] <= 260) and (current_color[2] >= 220 and current_color[2] <= 250):
                    new_color = (255, 255, 255)
                else:
                    new_color = (0, 0, 0)            
                    im.putpixel((w, h), new_color) 
            
            elif level == 6:
                if (current_color[0] >= 200 and current_color[0] <= 250) and (current_color[1] >= 210 and current_color[1] <= 260) and (current_color[2] >= 220 and current_color[2] <= 250):
                    new_color = (255, 255, 255)
                else:
                    new_color = (0, 0, 0)            
                    im.putpixel((w, h), new_color) 
                    
                
    
    #Picture color inverse (for read the word clearly)
    inverted_image = PIL.ImageOps.invert(im)
    
    #Save the pic for control if is ok or not
    inverted_image.save('Images/typinGame.jpg', quality=95)
    take_that_word()
    
def lets_do_the_mean(image, w, h):   
    R = 0
    G = 0
    B = 0
    pixelCount = 0
    mean = []
	
    #Taking the all pixels color mean (for determine the level of the game)          
    for x in range(0, w):
        for y in range(0, h):
           r, g, b = image.getpixel((x,y))
            
           R += r
           G += g
           B += b
           pixelCount += 1    
          
    #append in a list, the mean of picture        
    mean.append((int)(R/pixelCount))
    mean.append((int)(G/pixelCount))
    mean.append((int)(B/pixelCount))
        
    return mean

#Analyze the level number, by the colour determined by the mean
def analyze_that_level(r, g, b):
    global loop
    
    #Level 1
    if (r >= 110 and r <= 190) and (g >= 190 and g <= 230) and (b >= 210 and b<= 250):
        return 1
    #Level 2
    elif (r >= 25 and r <= 65) and (g >= 85 and g <= 180) and (b >= 45 and b<= 80):
        return 2
    #Level 3
    elif (r >= 60 and r <= 90) and (g >= 120 and g <= 160) and (b >= 130 and b<= 160):
        return 3
    #Level 4
    elif (r >= 210 and r <= 230) and (g >= 165 and g <= 190) and (b >= 135 and b<= 155):
        return 4
    #Level 5
    elif (r >= 60 and r <= 90) and (g >= 30 and g <= 55) and (b >= 60 and b<= 105):
        return 5
    #Level 6
    elif (r >= 210 and r <= 230) and (g >= 140 and g <= 170) and (b >= 170 and b<= 190):
        return 6
    else:
        loop = False
    

def lets_loop():
    global loop
  
    while loop:       
         print("Loop is: ", loop)  
         take_and_convert_the_screen()
         
    
#-------------------------------------------------------
#                 Program Start
#-------------------------------------------------------

with Listener(
    on_press=on_press,
    on_release=on_release) as listener:
    listener.join()
        
        