import os

#print(dir(os))
#print(os.getcwd())
#print(os.listdir())
#os.chdir('c:/itay')
#print(os.getcwd())
#print(os.listdir())

#print("life goes on...")

#try:
#    os.mkdir("3008/inner")
#except FileNotFoundError as e:
#    print(e)
#finally:
#    print("finished?")

#from inputapi import SmartInput
#import inputapi
#inputapi.SmartInput
from inputapi import *
si = SmartInput()
a = si.inputInt("Enter A:")
b = si.inputInt("Enter B:")
c = si.inputInt("Enter C:")
