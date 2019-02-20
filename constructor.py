class person:
    name=""
    age=0

    def __init__(self,personname,personage):
        self.name=personname
        self.age=personage


    def showage(self):
         print(self.age)

    def showname(self):
        print(self.name)


person1=person("harsh",22)
person2=person("vishi",21)

person1.showage()
person1.showname()