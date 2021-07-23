def square(num) :
  return num * num

# 제곱한 값에대가 추가적인 연산

a = square(5)
print("a : {}".format(a/2))

b = square(5)
print("b : {}".format(b*2))

c = square(10)




# 문제 : 입력받은 2가지 정수 사이에 존재하는 3의 배수 중에서 홀수의 합을 리턴하는 함수 구현

# 어떤수가 홀수인지 아닌지 체크하는 함수
def is_odd(num) :
  if num%2==1 :
    return 1
  else :
    return 0

# # 어떤수가 3의 배수인지 아닌지 체크하는 함수
def is_three_multiple(num) :
  if num%3==0 :
    return 1
  else :
    return 0


# is_odd와 is_three_multiple 이용해서 완성해주세요.
def get_sum(n, m) :
  nn=n
  mm=m
  sum = 0
  while nn<=mm :
     if is_odd(nn) and is_three_multiple(nn) :
       sum+=nn
     nn+=1
  return sum


result = get_sum(50, 100)
print("결과 : {}".format(result));
# 출력 => 675