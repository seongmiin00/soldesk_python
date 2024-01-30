# %% [markdown]
# ### 함수
# - 데이터를 전달 받는다 -> 전달 받은 데이터를 처리한다 -> 처리 결과를 리턴한다.
# - 한번의 코딩으로 반복적인 데이터 처리가 가능하다.

# %%
# 함수 선언 , 코드 실행시 함수가 메모리에 저장됨
def login():
    print('로그인 성공')

def logout():
    print('로그아웃 되었습니다.')

# %%
login()
logout()

# %%
def login(id):
    print(f'{id}님 로그인 성공')

def logout(id):
    print(f'{id}님 로그아웃 되었습니다.')

# %%
login('seongmin')
logout('seongmin')

# %%
def login(id,password):
    if id == 'user1' and password =='1234':
        print(f'{id}님 로그인 성공')
    else:
        print('로그인 실패')

def logout(id, password):
    if id == 'user1' and password =='1234':
        print(f'{id}님 로그아웃 되었습니다.')

# %%
def login(id,password):
    if id == 'user1' and password =='1234':
        return True
    else:
        return False

def logout(id, password):
    if id == 'user1' and password =='1234':
        print(f'{id}님 로그아웃 되었습니다.')

# %%
sw = login('user1','1234')
if sw == True:
    print('로그인성공')
else:
    print('로그인 실패')

# %%
if sw == True:
    print('댓글쓰기')
else:
    print('댓글쓰기 불가능')

# %%
11/3

# %%
def add(a,b):
    return a+b

def sub(a,b):
    return a-b

def mul(a,b):
    return a*b

def div(a,b):
    return a/b

def mok(a,b):
    return a//b

def nam(a,b):
    return a%b

# %%
a = 3
b = 6

print(add(a,b))
print(sub(a,b))
print(mul(a,b))
print(div(a,b))
print(mok(a,b))
print(nam(a,b))

# %%
def calc(a,b):
    sum = a+b
    min = a-b
    mul = a*b
    div = a/b
    mok = a//b
    nam = a%b
    return sum,min,mul,div,mok,nam

# %%
sum,min,mul,div,mok,nam = calc(5,3)
print(sum,min,mul,div,mok,nam)

# %%
def calc(a,b,c):
    if c == '+':
        return a+b
    elif c =='-':
        return a-b
    elif c =='*':
        return a*b
    elif c =='/':
        return a/b
    elif c =='//':
        return a//b
    elif c =='%':
        return a%b

# %%
# m²/ 3.3 = 평

# 원룸의 width를 입력하세요:6
# 원룸의 height를 입력하세요:4
# 원룸의 크기: 24 m²7.272727272727273 평

width = int(input('원룸의 width를 입력하세요:'))
height = int(input('원룸의 height를 입력하세요:'))
m2 = width * height # 함수 대상
py = m2 / 3.3       # 함수 대상

print(f'원룸의 크기: {m2}m²{py} 평')


# %%
def m2(width, height):
    return width * height

def py(m2):
    return m2 / 3.3

width = int(input('원룸의 width를 입력하세요:'))
height = int(input('원룸의 height를 입력하세요:'))

a = m2(width,height)
b = py(a)

print(f'원룸의 크기: {a}m² {b} 평')

# %%
def oneRoom(width, height):
    m2 = width * height
    return m2 , m2 / 3.3

width = int(input('원룸의 width를 입력하세요:'))
height = int(input('원룸의 height를 입력하세요:'))

m2,py = oneRoom(width,height)

print(f'원룸의 크기: {m2}m² {py} 평')

# %%
# 신체질량지수(BMI) = (몸무게(kg) / 신장의 제곱) * 10000

# 몸무게(kg):64
# 키(신장, cm):167
# BMI: 22.948115744558788

def calcbmi(cm, kg):
    bmi= kg / (cm**2) * 10000
    return bmi

cm = int(input("키를 입력하세요 :"))
kg = int(input("몸무게를 입력하세요:"))

bmi= calcbmi(cm, kg)
print(f'BMI: {bmi}')

# %%
# global 전역 변수의 사용
# 여러개의 함수가 값을 공유할 때 사용

tot=0 # 젼역 변수

def ibgo(item):
    global tot # 전역 변수 사용 선언, 생략시 에러 발생
    tot = tot + item
    print('입고 {0} -> 재고 {1}'.format(item, tot))

def chulgo(item):
    global tot
    tot = tot + item
    print('출고 {0} -> 재고 {1}'.format(item*-1, tot))

# %%
ibgo(1)
ibgo(2)
ibgo(3)

# %%
chulgo(3)
chulgo(2)
chulgo(1)

# %%
import random

data = [-3,-2,-1,1,2,3] #-1은 출고 1은 입고

su = random.choice(data)
print(su)

# %%
tot = 0

def ibgo(item):
    global tot # 전역 변수 사용 선언, 생략시 에러 발생
    tot = tot + item

def chulgo(item):
    global tot
    tot = tot - item

for i in range(1000):
    su = random.choice(data)
    
    if su < 0:
        chulgo(su*-1)
    else:
        ibgo(su)
print(f'총 재고 : {tot}')


