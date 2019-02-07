# 파일명 변경 금지
# 아래에 클래스를 Point와 Rectangle을 선언하세요.
class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y

class Rectangle:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def get_area(self):
        a = self.p2.x - self.p1.x #우측 하단 x값과 좌측 상단 x값의 차이
        b = self.p1.y - self.p2.y #좌측 상단 y값과 우측 하단 y값의 차이
        return a * b #면적

    def get_perimeter(self):
        a = self.p2.x - self.p1.x
        b = self.p1.y - self.p2.y
        return (a + b) * 2 #둘레의 길이

    def is_square(self):
        a = self.p2.x - self.p1.x
        b = self.p1.y - self.p2.y
        if a == b:
            return True #같으면 정사각형
        else:
            return False #정사각형이 아니다

# 아래의 코드는 수정하지마세요. 
if __name__ == '__main__':
    p1 = Point(1, 3)
    p2 = Point(3, 1)
    r1 = Rectangle(p1, p2)
    print(r1.get_area())
    print(r1.get_perimeter())
    print(r1.is_square())
    p3 = Point(2, 5)
    p4 = Point(8, 3)
    r2 = Rectangle(p3, p4)
    print(r2.get_area())
    print(r2.get_perimeter())
    print(r2.is_square())