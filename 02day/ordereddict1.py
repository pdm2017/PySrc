# ordereddict1.py
fruits = {'사과':'apple','포도':'grape','바나나':'banana',
            '컵':'cup','물':'water'}
fruits['강'] = 'river'
print(fruits)

d = {}
d['x'] = 100
d['l'] = 500
d['y'] = 200
d['z'] = 300

for k, v in d.items():
    print(k, v)
