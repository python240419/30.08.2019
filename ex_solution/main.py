from directoryapi import *

dc = DirectoryCreator('c:/itay')
while True:
    name = input("folder name? ")
    if dc.safeCreateFolder(name):
        break

print("Success!")
