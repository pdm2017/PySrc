# for06.py
a = [15,72,91,34,45,23,67,57,34]
# a 에서 짝수만 b 에 입력하세요
b = [ i for i in a if (i%2) ==0 ]
print(b)
# a 에서 3의 배수만 10을 곱해 c에 입력하세요
c = [ i*10 for i in a if (i%3) == 0 ]
print(c)
# a 에서 10으로 나눈 나머지가 홀수인 값을 d 에 입력하세요
d = [ i for i in a if (i%10)%2 == 1]
print(d)
# a 에서 10으로 나눈 나머지가 홀수인 값을 e 에 원래숫자: 나머지 를 입력하세요
e = { i: i%10 for i in a if (i%10)%2 == 1 }
print(e)