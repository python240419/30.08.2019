import os
class DirectoryCreator:
    def __init__(self, wd):
        '''
        ctor
        :param wd: working directory
        '''
        self.wd = wd
    def safeCreateFolder(self, name):
        os.chdir(self.wd)
        try:
            os.mkdir(name)
            return True
        except Exception as e:
            print('---------- ERROR:')
            print(e)
            print('-----------------')
        return False

def main():
    pass

if __name__ == '__main__':
    main()
