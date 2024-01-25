# 这是一个输出分数等级的程序
# [90, 100]为A，[80, 90)为B，[70,80)为C，
# [0, 70)为D，如果不在[0,100]内输出error。

score = int(input("Please enter your score between 0-100:\n"))
if (score <= 100) & (score >= 90):
    grade = 'A'
    print("Your grade is: "+grade)
elif (score < 90) & (score >= 80):
    grade = 'B'
    print("Your grade is: "+grade)
elif (score < 80) & (score >= 70):
    grade = 'C'
    print("Your grade is: "+grade)
elif (score < 70) & (score >= 0):
    grade = 'D'
    print("Your grade is: "+grade)
else:
    print("Error")
