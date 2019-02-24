def printmsg(msg):
    def printer():
        print(msg)

        return printer()


another = printmsg("this is printer")
another()
