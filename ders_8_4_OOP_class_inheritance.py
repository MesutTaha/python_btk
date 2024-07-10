# Innheritance (Kalıtım) Classların birbirlerinden miras alması


class Person:
    def __init__(self, fname, lname):
        print('person created')
        self.firstName = fname
        self.lastName= lname
    
    def what_am_I(self):
        print('I am a person')

    def ne_yices(self):
        print('karniyarik')


class Student(Person):# Class içinde Class***********************

    def __init__(self, fname, lname):
        Person.__init__(self, fname, lname) # Student Çağrılınca Person classı da cagrilmş olur
        print('Student Created')

    # override: aynı isimde fonk. varsa üstüne yazar. Yoksa Person classındaki yemek ismi yazdırılır("karniyarik").
    # def ne_yices(self):
    #     print('Musakka')

class Teacher(Person):# Class içinde Class***********************

    def __init__(self, fname, lname, branch):
        super().__init__(fname, lname) # Person.__init__(self, fname, lname) aynisi
        self.branch = branch
        
p1 = Person(fname='Mesut', lname='Dinleyici')
s1 = Student(fname='Taha', lname='Dinleyici')
t1 = Teacher(fname='kkkk',lname='skakkdas', branch='Math')

print(f'{p1.firstName} {p1.lastName} is created')
print(f'{s1.firstName} {s1.lastName} is created')
print(f'{t1.firstName} {t1.lastName} is created')

p1.what_am_I()
s1.what_am_I()

p1.ne_yices()
s1.ne_yices()
t1.ne_yices()