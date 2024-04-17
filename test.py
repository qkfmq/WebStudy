kor_score = [49, 80, 20, 100, 80]
math_score = [43, 60, 85, 30, 90]
eng_score = [49, 82, 48, 50, 100]
midterm_score = [ kor_score, math_ score, eng_score]

student_score = [0, 0, 0, 0, 0]






















'''
print("구구단 몇 단을 계산할까요(1~9)?")
x = 1
while (x is not 0):
    x = 7
    if x == 0: break
    if not(1 <= x <= 9):
        print("잘못 입력했습니다.", "1 부터 9 사이 숫자를 입력하세요.")
        continue
    else:
        print("구구단 " + str(x) + "단을 계산합니다.")
        for i in range(1,10):
            print(str(x) + " x " + str(i) + " = " + str(x*i))
        print("구구단 몇 단을 계산할까요(1~9)?")
print("구구단 게임을 종료합니다.")
'''



'''
age = int(input("태어난 년도를 입력하세요: "))
age = 2020 - age + 1
if age <= 26 and age >=20:
    rs = '대학생'
elif age < 20 and age >=17:
    rs = '고등학생'
elif age < 17 and age >=14:
    rs = '중학생'
elif age < 14 and age >=8:
    rs = '초등학생'
else :
    rs = '학생이 아닙니다'

print(rs)
'''



'''
score = int(input("Enter your score: "))

if score >= 90:
    grade = 'A'
elif score >= 80:
    grade = 'B'
elif score >= 70:
    grade = 'C'
elif score >= 60:
    grade = 'D'
else:
    grade = 'F'

print(grade)
'''