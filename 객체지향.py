# === 원뿔 계산 함수 클래스 ===
class Cone :
    def __init__(self, radius = 20, height = 30) :
        self.r = radius
        self.h = height

    def get_vol(self) :
        return 1/3 * 3.14 * self.r ** 2 * self.h
    
    def get_surf(self) :
        return 3.14 * self.r ** 2 + 3.14 * self.r * self.h


# === 이름, 나이, 몸무게, 키를 데이터 필드로 사용하는 BMI 클래스 ===
class BMI :
    def __init__(self, name, age, weight, height) :
        self.name = name
        self.age = age
        self.weight = weight
        self.height = height

    def get_BMI(self) :
        return self.weight / (self.height / 100) ** 2
    
    def get_status(self) :
        BMI = self.get_BMI()

        if BMI >= 25 :
            return "비만"
        elif BMI >= 23 and BMI < 25 :
            return "과체중"
        elif BMI >= 18.5 and BMI < 23 :
            return "정상"
        else :
            return "저체중"


# === 단위 원뿔과 반지름, 높이가 50, 100인 원뿔의 부피와 겉넓이를 출력하는 프로그램 ===
unit_cone = Cone()
big_cone = Cone(50, 100)

print("단위 원뿔의 부피와 겉넓이는", unit_cone.get_vol(), unit_cone.get_surf(), "입니다.")
print("큰 원뿔의 부피와 겉넓이는", big_cone.get_vol(), big_cone.get_surf(), "입니다.")


# === 가상의 이름, 나이, 몸무게, 키로 BMI 객체를 사용하는 프로그램 ===
person1 = BMI("홍길동", 40, 78, 182)

print(person1.name, "님(", str(person1.age), "세)의 BMI 수치는", person1.get_BMI(), "결과는", person1.get_status(), "입니다.")


# === 멤버 __r과 __h에 대한 접근자와 변경자를 갖는 원뿔 클래스를 작성하고 객체를 활용하는 프로그램 ===
class pCone :
    def __init__(self, radius = 20, height = 30) :
        if radius > 0 and height > 0 :
            self.__r = radius
            self.__h = height

    def get_vol(self) :
        return 1/3 * 3.14 * self.__r ** 2 * self.__h
    
    def get_surf(self) :
        return 3.14 * self.__r ** 2 + 3.14 * self.__r * self.__h
    
    def get_radius(self) :
        return self.__r
    
    def set_radius(self, radius) :
        if radius > 0 :
            self.__r = radius
    
perfect_cone = pCone(100, 200)
perfect_cone.get_surf()