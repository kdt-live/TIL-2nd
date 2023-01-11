class Person:

    # 생성자 메서드 
    def __init__(self, name):
        self.name = name

    def greeting(self):
        return f'안녕.. 난 {self.name}'

    # 소멸자 메서드
    def __del__(self):
        print('ㅠㅠ')

# 인스턴스 생성
p1 = Person('홍길동') # __init__메서드가 호출됨
print(p1.greeting()) # 직접 greeting을 호출!

# p2 = Person('뉴진스')
# print(p2.greeting())
# # print(Person.greeting(p2))