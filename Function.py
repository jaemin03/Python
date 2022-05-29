import random

def number_cases():
    num1 = int(input("첫번째 정수 입력 : "))
    num2 = int(input("두번째 정수 입력 : "))

    if num1 <= 10 and num2 <= 10:
        for i in range(1, num1 + 1):
            for j in range(1, num2 + 1):
                print(i, j)

def score():
    score = int(input("점수 입력 : "))

    if score >= 90 and score <= 100:
        print("A")
    elif score >= 70:
        print("B")
    elif score >= 40:
        print("C")
    else:
        print("D")

def rock_paper_scissors():
    while True:
        print("1. 가위 2. 바위 3. 보")
        user = int(input())
        com = random.randint(1, 3)
        print("유저 : ", user)
        print("컴퓨터 : ", com)
        if user == com:
            print("다시 시작")
            continue
        elif user == 1 and com == 3:
            print("유저 승리")
            break
        elif user == 2 and com == 1:
            print("유저 승리")
            break
        elif user == 3 and com == 2:
            print("유저 승리")
            break
        else:
            print("컴퓨터 승리")
            break

def random_baseball():
    def rand():
        while True:
            rand1 = random.randint(0, 9)
            rand2 = random.randint(0, 9)
            rand3 = random.randint(0, 9)
            if rand1 != rand2 != rand3:
                rand_list.append(str(rand1))
                rand_list.append(str(rand2))
                rand_list.append(str(rand3))
                break

    while True:

        rand_list = []
        rand()
        strike = 0
        ball = 0
        num = input("3자리 숫자 입력 : ")
        user = list(num)
        print(rand_list)
        print(user)

        for i in range(len(rand_list)):
            if user.count(rand_list[i]):
                if rand_list[i] == user[i]:
                    strike += 1
                else:
                    ball += 1

        print(strike)
        print(ball)

        if strike == 3:
            print("정답입니다.")

select_num=int(input("1.이중반복문, 2.성적, 3.가위바위보, 4.숫자야구\n실행할 함수 선택 : "))
if select_num==1:
    number_cases()
elif select_num==2:
    score()
elif select_num==3:
    rock_paper_scissors()
elif select_num==4:
    random_baseball()