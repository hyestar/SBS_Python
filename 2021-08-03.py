# 문제 : 자동차 객체를 담을 변수를 만들어주세요.
# 자동차 객체를 변수에 담고 그 변수를 이용해 최고속력이 서로 다르게 만들어주세요.
class Car() :
  hv = 135
  def Carprint(self) :
    print("자동차가 최대속력 {}km로 달립니다.".format(self.hv))

c1 = Car()
c2 = Car()
c3 = Car()

c2.hv = 220
c3.hv = 250

c1.Carprint()
c2.Carprint()
c3.Carprint()
# 각 자동차가 자신의 최고속력으로 달리게 해주세요.




# 다음 코드가 동작하도록 class를 완성해주세요
class Person :
  name = "전혜성"
  age = 24
  def introduce(self) :
    print("안녕하세요 {}살 {}입니다.".format(self.age, self.name))

class Student :
  name = ""
  math = 0
  korean = 0
  english = 0
  def sum(self) :
    print("{}의 총점은 {}".format(self.name,self.math+self.korean+self.english))
  def avg(self) :
    print("{}의 평균은 {}".format(self.name,(self.math+self.korean+self.english)/3))


p1 = Person();
p1.name = "홍길동";
p1.age = 27;

p2 = Person();
p2.name = "홍길순";
p2.age = 25;

p1.introduce(); # 안녕하세요 27살 홍길동입니다.
p2.introduce(); # 안녕하세요 25살 홍길순입니다.

s1 = Student();
s1.name = "이순신";
s1.math = 90;
s1.korean = 87;
s1.english = 77;

s1.sum(); # 이순신의 총점은 254
s1.avg(); # 이순신의 평균은 84.6

s2 = Student();
s2.name = "임꺽정";
s2.math = 70;
s2.korean = 97;
s2.english = 75;

s2.sum(); # 임꺽정의 총점은 242
s2.avg(); # 임꺽정의 평균은 80.6