# for05.py
a = []
# a 에 for문을 사용해서 1 ~ 10 까지 입력하세요

for i in range(10): a.append(i+1)
print(a) # 결과 ==> [1,2,3,4,5,6,7,8,9,10]
###########################################
fruits = {'사과':'apple','포도':'grape','바나나':'banana',
            '컵':'cup','물':'water'}
# fruits 에서 바나나가 존재하는지 확인해보세요
print('바나나' in fruits.keys())
# fruits 에서 grape가 존재하는지 확인해보세요
print('grape' not in fruits.values())

# fruits 의 value 에서 문자 e 가 들어가 있는 것만 g 에 담아보세요 {key,value}
g = { k:v for k,v in fruits.items() if 'e' in v}
print(g)
g = { k:fruits[k] for k in fruits.keys() if 'e' in fruits[k]}
print(g)
g = { f[0]:f[1] for f in fruits.items() if 'e' in f[1]}
print(g)

#####################################################