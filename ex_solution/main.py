from directoryapi import *

def main():
    dc = DirectoryCreator('c:/itay')
    while True:
        name = input("folder name? ")
        if dc.safeCreateFolder(name):
            break

    print("Success!")
main()
