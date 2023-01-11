# 소개팅
# 사람 관련 정보 뭐가 있을까요?

class Person:

    def __init__(self, name, age, mbti):
        self.name = name 
        self.age = age
        self.mbti = mbti

    def greeting(self):
        return f'{self.name}입니다. {self.mbti}이구요...'

    # print(p1 > p2)
    def __gt__(self, other):
        if self.age > other.age:
            return self 
        else:
            return other 

    def __str__(self):
        return f'{self.name} ({self.age})'

    def __len__(self):
        return self.age

    

p1 = Person('재용', 30, 'istp')
p2 = Person('유영', 28, 'enfj')
print(p1.name)
print(p1.greeting())
print(p1 > p2)
print(p1)
print(len(p1))
