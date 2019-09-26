# Func06.py
fruits = {'사과':'apple','포도':'grape','바나나':'banana',
            '컵':'cup','물':'water'}

def pDict(**d): # 가변길이 매개 변수 --> dict
    for i in d.items(): print(i)

pDict(**fruits)
pDict(사과='apple',포도='grape',바나나='banana')
pDict(**{'컵':'cup','물':'water'})