# 1. 1 ~ 100까지 출력
num = 1
while num<=100 :
  print("{}".format(num))
  num+=1

# 2. -25 ~ 50까지 출력
print("==============")
num2 = -25
while num2<=50 :
  print("{}".format(num2))
  num2+=1

# 3. 1 ~ 100 까지 짝수만 출력
print("==============")
num3 = 1
while num3<=100:
  if num3%2==0:
    print("{}".format(num3))
  num3+=1

# 4. 100 ~ 200 사이의 홀수만 출력
print("==============")
num4 = 100
while num4<=200:
  if num4%2==1:
    print("{}".format(num4))
  num4+=1

# 5. 1 ~ 500 사이의 수 중 4의 배수만 출력
print("==============")
num5 = 1
while num5<=500:
  if num5%4==0:
    print("{}".format(num5))
  num5+=1

# 6. n과 m 사이의 수 중 k의 배수 출력
n = 10
m = 30
k = 3

nn=n
mm=m

while nn<=mm:
  if nn%k==0:
    print("{}".format(nn))
  nn+=1