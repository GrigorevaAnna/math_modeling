a=[1, 2, 3] #Создание строк
print(a[0]) #Вывод на экран нулевого элемента спска

b=[8, 10, 11]

c=a+b #Сложение списков
print(c)

c=a*3
print(c)

d=[]
d.append(a)
print(d)

d.append(b)
print(d)

d.append("Good")
print(d)

d.append(1)
print(d)

print(d[0])

print(d[0][0])

d[0]="Hello world"
print(d)
