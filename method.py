class abc:

    def __init__(self,name,age):
        self.name=name
        self.age=age

        def xyz(self,song):
            return "{}is now singing".format(self.name,song)

        def ab(self):
            return "{} is now dancing".format(self.name)

a = abc("harsh",123)

print(a.xyz("'harsh'"))
print(a.qwe())

