from datetime import date, timedelta

tup1 = (1, 2, 3)
list1 = [4, 5, 6, 7]
list2 = [list1, tup1]
print(list2)
tup2 = (tup1, list1)
print(tup2)

tup3 = ([1, 2, 3], 12, 13, (1, 2, 5))
print(tup3)
tup3[0][1] = 222
print(tup3)


# class review

# class Circle:
#     def __init__(self):
#         self.radius = 1
#
# acircle = Circle()
# print(2 * 3.14 * acircle.radius)
# print(type(acircle))
#
# acircle.color = "red"
# print(acircle.color)
#
# print(acircle.__dict__)
#

# class Demo:
#     def showobj(self):
#         print(self)
#
# ademo = Demo()
# print(ademo)
# ademo.showobj()
#
# class Sum:
#     def add(self, num):
#         if not hasattr(self, 'x'):
#             self.x = 0
#         self.x += num
#
# anobject = Sum()
# anobject.add(5)
# print(anobject.x)
# anobject.add(2)
# print(anobject.x)


# class Counter:
#     def setcnt(self, cnt):
#         if not isinstance(cnt, int):
#             raise TypeError('arg must be an int')
#         self.count = cnt
#     def getcnt(self):
#         return self.count
#     def addone(self):
#         self.count += 1
#
# cnt1 = Counter()
# cnt2 = Counter()
# cnt1.setcnt(5)
# cnt1.addone()
# print(cnt1.getcnt())
# cnt2.setcnt('one')

# class DemoCounter:
#     def __init__(self, initcount):
#         try:
#             initcount = int(initcount)
#         except ValueError:
#             initcount = 0
#         self.count = initcount
#
#     def addone(self):
#         self.count += 1
#
#     def getcnt(self):
#         return self.count
#
# cnt1 = DemoCounter(0)
# cnt2 = DemoCounter(5)
# cnt1.addone()
# cnt2.addone()
# cnt2.addone()
# print(cnt1.getcnt())
# print(cnt2.getcnt())

# class Animal:
#     def __init__(self, name):
#         self.name = name
#     def eat(self, food):
#         print(f'{self.name} eats {food}')
#
# class Dog(Animal):
#     def fetch(self, item):
#         print(f'{self.name} fetches the {item}')
#
#     def talk(self):
#         print(f'{self.name} does a bork!')
#
# class Cat(Animal):
#     def eat(self, food):
#         if food in ['cat food', 'fish']:
#             print(f'{self.name} eats {food}')
#         else:
#             print(f'{self.name} is hungry!')
#     def talk(self):
#         print(f'{self.name} says Meow!')
#
# adog = Dog("Skip")
# acat = Cat("Fluffy")
#
# adog.eat('gummy bears')
# acat.eat('dog food')
# acat.eat('cat food')
# acat.talk()
# adog.talk()

# date time timedelta review

# dobj = date(2018, 4, 23)
# print(dobj)
# tdobj = timedelta(days = 7)
# print(tdobj)
# dobj += tdobj
# print(type(dobj))
# print(type(tdobj))
#
# dobj2 = date.today()
# print(dobj2)
#
# dobj2 += timedelta(days = 1)
# print(dobj2)


# list function reviews
# x = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
#
# for row in x:
#     print()
#     for item in row:
#         print(item, end="")
