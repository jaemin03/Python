import random

def rand():
    while True:
        rand1 = random.randint(0,9)
        rand2 = random.randint(0,9)
        rand3 = random.randint(0,9)
        if rand1!=rand2!=rand3:
            rand_list.append(str(rand1))
            rand_list.append(str(rand2))
            rand_list.append(str(rand3))
            break

while True:

    rand_list=[]
    rand()
    strike=0
    ball=0
    num=input("3자리 숫자 입력 : ")
    user=list(num)
    print(rand_list)
    print(user)

    for i in range(len(rand_list)):
        if user.count(rand_list[i]):
            if rand_list[i]==user[i]:
                strike+=1
            else:
                ball+=1

    print(strike)
    print(ball)

    if strike==3:
        print("정답입니다.")
