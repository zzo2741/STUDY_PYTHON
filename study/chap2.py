# simple.py
languages = ['python', 'perl', 'c', 'java']

for lang in languages:
    if lang in ['python', 'perl']:
        print("%6s need interpreter" % lang)
    elif lang in ['c', 'java']:
        print("%6s need compiler" % lang)
    else:
        print("should not reach here")
print(3*3*3*3)
multiline = """
Leejunseung
26
handsome
"""
print(multiline)
print("="*50)
print("="*50)
a = len(multiline)
print(a)

a = "Life is too short, You need Python"
print(a[0:4])
print(a[0:3])
print(a[19:])
print(a[:19])
print("I eat %d apples." % 3)
print("I eat %s apples." % "five")

number = 10
day = "three"
print("I ate %d apples. so I was sick for %s days." % (number, day))
# print("Error is %d%." % 98) <- 오류 문법
print("Error is %d%%." % 98)
d = {'name': '홍길동', 'age': 30}
print(f'나의 이름은 {d["name"]}입니다. 나이는 {d["age"]}입니다.')
a = "Life is too short"
