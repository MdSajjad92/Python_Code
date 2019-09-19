"""super Method or class.method.In this method a child class can use the __init of parent using super.__init(self,a,b)
                               parent_class_name.__init(self,a,b) """

class Person:

    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname, self.lastname)

    def total_marsk(self,m1,m2,m3):
        self.Marsk1 = m1
        self.Marsk2 = m2
        self.Marsk3 = m3
        print("the roll no is {} and grade is {}".format(self.roll_no,self.grade))
        return (self.Marsk1+self.Marsk2+self.Marsk3)/3


class Student(Person):                                       #Student a child of Person using initial value from
    def __init__(self,fname,lname,roll,grade,*args):
        Person.__init__(self, fname, lname)
        self.roll_no = roll                                  #roll no is initialised inside child itself
        self.grade = grade                                   #grade is also initialsed inside class.
        self.result = 'passed'
        self.book = 'India wins freedom'
        self.switch = 'cisco 9k'
        self.router = 2900
        self.place = 'Bangalore'


x = Student("Mike", "Olsen",'98','A')
x.printname()
performance = x.total_marsk(98,75,85)
print("The percentage obtained is",performance)
print('the details of router is',x.router)

