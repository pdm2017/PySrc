# test02.py

# Quiz01) z 에서 abc  가 아닌 문자는 무엇인가요? (중복제거)

z = 'abcxabxcyabzcazbybca'

#   입력변수 for 변수 in 대상 if 추출조건
y = {s for s in z if s not in 'abc' }
print(y)

x = 'Hello'
print('e' in x)

# Quiz02) 국어점수가 70이상이면 '합격',아니면 '불합격'
국어점수 = {'Tom':90,'Jane':60,'Alice':70}

r = {이름: '합격' if 국어점수[이름] >=70 else '불합격'
        for 이름 in 국어점수.keys() }
print(r)
#결과 ==> {'Tom': '합격', 'Jane': '불합격', 'Alice': '합격'}

점수 = [79,87,91,100,65]
결과 = '합격' if 점수[4] >= 70 else '불합격'
# true if 조건 else false

# 입력변수 if 입력조건 for 변수 in 대상
결과 = [ '합격' if p >= 70 else '불합격' for p in 점수 ]
print(결과)

# 입력변수 if 입력조건 for 변수 in 대상 if 추출조건

# Quiz 3 ) 수학 점수가 0이 아닌 학생들만 출력하세요
#          단, 70이상은 합격, 미만은 불합격 표시

수학점수 = {'Tom':90,'Jane':60,'Alice':0,'Hong':78,'Kim':45}
# 결과 ==> {'Tom':'합격','Jane':'불합격,'Hong':'합격','Kim':'불합격}

r = {이름: '합격' if 수학점수[이름] >=70 else '불합격'
        for 이름 in 수학점수 if 수학점수[이름] }
print(r)

