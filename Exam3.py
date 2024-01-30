import sys

def add(a, b):
    return a + b

def sub(a, b):
    return a - b

su1 = int(sys.argv[1]) # <- 콘솔 입력 (콘솔 실행시 입력값도 같이 보내줘야함)
su2 = int(sys.argv[2]) 

print(add(su1, su2))
print(sub(su1, su2))