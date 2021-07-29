# 딕셔너리 - 리스트 사용
# 회원 기능 - 로그인, 회원가입, 중복체크, 비밀번호 찾기
# 회원 - 아이디, 비밀번호, 이름

# 회원1 - hong123, h1234, 홍길동
# 회원2 - Lee123, L1234, 이순신
# 회원3 - Lim123, L4321, 임꺽정

hong = {"아이디" : "hong123", "비밀번호" : "h1234", "이름" : "홍길동"}
lee = {"아이디" : "Lee123", "비밀번호" : "L1234", "이름" : "이순신"}
lim = {"아이디" : "Lim123", "비밀번호" : "L4321", "이름" : "임꺽정"}

Memberlist = [hong, lee, lim]  # 현재 가입된 회원 목록

# 기능1 - 모든 회원 정보 보기
# 함수화
# 한명의 회원 정보 출력 함수
def printMember(member) :
  print("아이디 : {}".format(member["아이디"]))
  print("비밀번호 : {}".format(member["비밀번호"]))
  print("이름 : {}".format(member["이름"]))

# printMember(hong)
# printMember(lee)
# printMember(lim)

# 모든 회원 정보 출력 함수
def AllprintMember() :
  for member in Memberlist :
     printMember(member)


# 기능2 - 회원을 추가(회원가입)

def addMember() :
  loginid = input("아이디를 입력해주세요 : ")
  loginpw = input("비밀번호를 입력해주세요 : ")
  loginname = input("이름을 입력해주세요 : ")
  
  new={"아이디":loginid,"비밀번호":loginpw,"이름":loginname}
  Memberlist.append(new)


# 기능3 - 로그인 기능 추가

def login() :
    id=input("아이디를 입력해주세요 : ")
    pw=input("비밀번호를 입력해주세요 : ")
    flag = 1 # 1은 잘못된 정보 2는 성공
    for a in Memberlist :
        if id == a["아이디"] :
            flag = 2
            if pw == a["비밀번호"] :
                print("{}님 반갑습니다!!".format(a["이름"]))
            else :
                flag = 1
    if flag == 1 :
        print("잘못된 정보입니다.")
        

addMember()
AllprintMember()
login()