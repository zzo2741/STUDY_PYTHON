# Q1
from study.chap2_ex import result

a = "Life is too short, you need python"

if "wife" in a:
    print("wife")
elif "python" in a and "you" not in a:
    print("python")
elif "shirt" not in a:
    print("shirt")
elif "need" in a:
    print("need")
else:
    print("none")

# Q2
num = 0
result = 0
while num <= 1000:
    if(num % 3 ==0):
        result = result + num
    num = num + 1
print(result)

# Q3
num = 1;
while num<=5:
    print("*" * num)
    num = num + 1

# Q4
# 실습문제로 바로 넘어가기