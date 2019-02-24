class human:
    def sayhello(self,name=None):
        if name is not None:
            print("hello" + name)
        else:
            print("hello")


obj=human()
obj.sayhello()
obj.sayhello("harsh")
