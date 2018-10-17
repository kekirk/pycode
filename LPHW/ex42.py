class TheThing(object):
    def __init__(self, number):
        self.number = number

    def some_function(self, call_who):
        print("%s got called." % call_who)

    def add_me_up(self, more):
        self.number += more
        return self.number


a = TheThing(17)
b = TheThing(26)

a.some_function('Ac')
b.some_function('Bc')

print(a.add_me_up(20))
print(a.add_me_up(15))
print(b.add_me_up(30))
print(b.add_me_up(25))

print(a.number)
print(b.number)
