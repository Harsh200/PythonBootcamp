def printmsg(msg):
    def printer():
        print(msg)

        return  printer()