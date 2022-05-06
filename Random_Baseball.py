import random

while True:
    rand1=random.randint(0,9)
    rand2=random.randint(0,9)
    rand3 = random.randint(0, 9)
    if rand1!=rand2!=rand3:
        break

rand=[]
rand.append(str(rand1))
rand.append(str(rand2))
rand.append(str(rand3))

strike=0
ball=0
num=input("3자리 숫자 입력 : ")
user=list(num)
print(rand)
print(user)

for i in range(len(rand)):
    if user.count(rand[i]):
        if rand[i]==user[i]:
            strike+=1
        else:
            ball+=1

print(strike)
print(ball)