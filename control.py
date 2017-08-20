#!/usr/bin/python 
import RPi.GPIO as g
from time import sleep
import sys, os, random



def setup():
    #Setup Board
    g.setmode(g.BCM)
    g.setwarnings(False)
    #Setup Pins
    lightList = [4, 17, 18] 
    #4 bed #17 bath #18 Lounge
    for i in lightList: 
        g.setup(i, g.OUT) 

def switch(num):
    if (g.input(num) == 0):
      g.output(num,g.HIGH)
    else:
      g.output(num,g.LOW)
def disco():
    os.system('echo lets party | cowsay')
    lights = [4, 17, 18]
    for i in range(20):
        switch(lights[random.randint(0,2)])
        sleep(random.uniform(0, 0.5))
        
def main(name, user_input):
    setup()
    if user_input == 'bed':
        switch(4)
    elif user_input == 'bath':
        switch(17)
    elif user_input == 'beyond':
        switch(18)
    elif user_input == 'disco':
        disco()
    else:
       print("useage is ./control.py (bed/bath/beyond/disco)") 

if __name__ == '__main__':
    try:
        main(*sys.argv)
    except TypeError:
        print("useage is ./control.py (bed/bath/beyond/disco)")