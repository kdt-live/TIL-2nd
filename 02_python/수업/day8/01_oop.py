class Person:

    def greeting(self):
        return 'hi....'


iu = Person()
jimin = Person()

# Person 타입을 가짐
print(type(iu))
print(type(jimin))
print(type([1, 2, 3]))
print(type([]))

# 메서드를 호출할 수 있음
print(iu.greeting())

# 속성을 부여할 수 있음 
iu.name = '아이유'
jimin.name = 'BTS 지민'
print(iu.name)
print(jimin.name)
print(type(iu.name))
