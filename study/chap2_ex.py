# Q1
kor, eng, math = 80, 75, 55
result = (kor+eng+math)/3
print(f"평균 : {result}")
print('='*50)
# Q2
num = 13
if(num % 2 == 0):
    print(f"{num}은 짝수입니다.")
else:
    print(f"{num}은 홀수입니다.")
print('='*50)
# Q3
jumin = "951207-1111111"
fnum = jumin[:6]
lnum = jumin[7:]
print(fnum)
print(lnum)
print('='*50)
# Q4
pin = "881120-1068234"
sexNum = pin[7]
print(sexNum)
print('='*50)
# Q5
a = "a:b:c:d"
b = a.replace(":", "#")
print(b)
print('='*50)
# Q6
list = [1, 3, 5, 4, 2]
list.sort()
print(list)
list.reverse()
print(list)
print("="*50)
# Q7
list = " ".join(['Life', 'is', 'too', 'short'])
print(list)
print("="*50)
# Q8
tuple1 = (1, 2, 3)
tuple2 = (4,)
tuple1 = tuple1 + tuple2
print(tuple1)
print("="*50)
# Q9
a = dict()
a['name'] = 'python'
a[('a',)] = 'python'
print("# a[[1]] = 'python' 리스트는 딕셔너리의 key값이 될 수 없다.")
a[250] = 'python'
print("="*50)
# Q10
a = {'A': 90, 'B': 80, 'C': 70}
print(a.pop('B'))
print("="*50)
# Q11
a = [1, 1, 1, 2, 2, 3, 3, 3, 4, 4, 5]
list = set(a)
print(list)
print("="*50)
# Q12
a = b = [1, 2, 3]
a[1] = 4
print(b)
