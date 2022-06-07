data1 = dict()
data1['사과'] = 'apple'
data1['배'] = 'pear'
data1['오렌지'] = 'orange'

print(data1)

data2 = {'기차': 'train', '차': 'car', '바이크': 'bike', 1: 2}
print(data2)

data1[1] = 2
print(data1)

print()

data3 = set([1, 2, 3, 4, 5, 5, 5])
print(data3)

data4 = [1, 2, 3, 4, 5, 5, 5, 3, 4, 3, 4, 2, 2, 2, 1, 1, 7]
print(data4.count(3))

a = 1

def func():
    global a
    a = 4
    a += 1

func()
print(a)