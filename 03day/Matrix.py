# Matrix.py
# Matrix 표현
matrix_list     = [[3,6],[4,5]]
matrix_tuple    = [(3,6),(4,5)]
matrix_dict     = {(0,0):3,(0,1):6,(1,0):4,(1,1):5}

# Matrix 연산
ma = [[3,6],
      [4,5]]
mb = [[5,8],
      [6,7]]
#  ma + mb ==>  [[8,14],[10,12]]
# print(list(zip(ma,mb)))
mr1 = [t for t in zip(ma,mb)] ; print(mr1)
mr1 = [[row for row in zip(*t)] for t in zip(ma,mb)] ; print(mr1)
mr1 = [[sum(row) for row in zip(*t)] for t in zip(ma,mb)] ; print(mr1)

# any() : 하나라도 True 존재 , all() : 모두 True 인 경우
a1 = [False,False,False]; a2 = [False,True,False]
print(any(a1)); print(all(a1))
print(any(a2)); print(all(a2))
print("="*10)
a3 = [1,0,1]; a4 = [1,1,1]
print(any(a3)); print(all(a3))
print(any(a4)); print(all(a4))
# False <- 0, True <- 0을 제외한 음수, 양수
a5 = [-1,0,0]; print(any(a5))

# 행렬의 동치
mc = [1,1,1]
md = [2,1,1]

mr2 = [ t for t in zip(mc,md)]; print(mr2)
mr2 = [ t1==t2 for t1,t2 in zip(mc,md)]; print(mr2)

v1 = all([ t1==t2 for t1,t2 in zip(mc,md)])
print(v1) # ==> False
##############################
me = [[1,2],[3,4]]
mf = [[7,2],[3,4]]

# print(list(zip(me,mf)))
mr3 = [t for t in zip(me,mf)] ; print(mr3)
    # [([1, 2], [7, 2]), ([3, 4], [3, 4])]

mr3 = [[t for t in zip(*t)] for t in zip(me,mf)] ; print(mr3)
    # [[(1, 7), (2, 2)], [(3, 3), (4, 4)]]

mr3 = [row for t in zip(me,mf)
                for row in zip(*t) ] ; print(mr3)
    # [(1, 7), (2, 2), (3, 3), (4, 4)]
mr3 = [value for t in zip(me,mf)
                  for row in zip(*t)
                     for value in row] ; print(mr3)
# [1, 7, 2, 2, 3, 3, 4, 4]
mr3 = [(row,value) for t in zip(me,mf)
                  for row in zip(*t)
                     for value in row] ; print(mr3)
# [((1, 7), 1), ((1, 7), 7), ((2, 2), 2), ((2, 2), 2), ((3, 3), 3), ((3, 3), 3), ((4, 4), 4), ((4, 4), 4)]
mr3 = [row[0] == value for t in zip(me,mf)
                for row in zip(*t)
                    for value in row ] ; print(mr3)
# [True, False, True, True, True, True, True, True]
print(all(mr3))
##########################################################
mr4 = [(r1,r2) for t in zip(me,mf)
                  for r1,r2 in zip(*t)] ; print(mr4)
    # [(1, 7), (2, 2), (3, 3), (4, 4)]
mr4 = [(r1==r2) for t in zip(me,mf)
                  for r1,r2 in zip(*t)] ; print(mr4)
    # [False, True, True, True]
print(all(mr4))

# 전치행렬

mg = [[1,2,3],
      [4,5,6]]
print(list(zip(*mg)))
mh = [ [t1,t2] for t1,t2 in zip(*mg) ] ; print(mh)
# [[1,4],
#  [2,5],
#  [3,6]]

# 행렬 곱셈
'''
1,2,3    x   7,8
4,5,6        9,10
             11,12
'''
mx = [[1,2,3],[4,5,6]]
my = [[7,8],
      [9,10],
      [11,12]]

print([row_mx for row_mx in mx])
    # [[1, 2, 3], [4, 5, 6]]
print(list(zip(*my)))
    # [(7, 9, 11), (8, 10, 12)]
print([col_my for col_my in zip(*my)])
    # [(7, 9, 11), (8, 10, 12)]

mz = [[[z for z in zip(row_mx,col_my)]
                    for col_my in zip(*my)]
                        for row_mx in mx]
print(mz)
# [[[(1, 7), (2, 9), (3, 11)], [(1, 8), (2, 10), (3, 12)]], [[(4, 7), (5, 9), (6, 11)], [(4, 8), (5, 10), (6, 12)]]]

mz = [[[a*b for a,b in zip(row_mx,col_my)]
                    for col_my in zip(*my)]
                        for row_mx in mx]
print(mz)
# [[[7, 18, 33], [8, 20, 36]], [[28, 45, 66], [32, 50, 72]]]

mz = [[sum(a*b for a,b in zip(row_mx,col_my))
                    for col_my in zip(*my)]
                        for row_mx in mx]
print(mz)
    # [[58, 64], [139, 154]]

