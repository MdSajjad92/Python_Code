class Base:
    def __init__(self, name):
        self.name = name

    def getname(self):
        return self.name


class Child(Base):
    def __init__(self, name, age):
        Base.__init__(self, name)
        self.age = age

    def getage(self):
        return self.age


class GrandChild(Child):
    def __init__(self, name, age, address):
        Child.__init__(self, name, age)
        self.address = address

    def getaddress(self):
        return self.address


g = GrandChild("Geek1", 23, "Noida")
print(g.getname())
print(g.getage())
print(g.getaddress())
