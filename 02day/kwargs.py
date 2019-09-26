# kwargs.py
def kwargs_test(**kwargs):
    print(kwargs)
    print("First value is {first}".format(**kwargs))
    print("Second value is {second}".format(**kwargs))
    print("Third value is {third}".format(**kwargs))

kwargs_test(first = 3, second = 4, third = 5)

a = ['alice','jane','tom']
print("{2},{0}".format(*a))

fruits = {'사과':'apple','포도':'grape','바나나':'banana',
            '컵':'cup','물':'water'}
print("{컵},{사과},{물}".format(**fruits))
