class SmartInput():
    def __init__(self):
        pass
    def __str__(self):
        return 'methods: inputInt'
    def inputInt(self, msg):
        '''
        Get an int number from the user
        input number till valid
        int was receieved
        :return: int number
        '''
        while True:
            try:
                n = int(input(msg))
                return n
            except: # catch
                print("error, try again")
    def positiveFloat(self, msg):
        '''
        Get a float number from
        the user
        input number till valid
        float was receieved
        :param msg: show message
        :return: float positive
        '''
        while True:
            try:
                n = float(input(msg))
                if (n <= 0):
                    print('not positive')
                else:
                    return n
            except:  # catch
                print("error, try again")


