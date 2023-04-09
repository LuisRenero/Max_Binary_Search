import math

x = int(input("ingresa el numero de valores a evaluar"))
y = x
#y = int(input("numero a encontrar"))
array_list = []
for i in range(x):
    array_list.append(i+1)

low = array_list[0]
high = array_list[x-1]
x = 0
while high != low:
    mid = math.floor((low + high)/2)
    if(y < array_list[mid]):
        high = array_list[mid] - 1
    elif(y > array_list[mid]):
        low = array_list[mid] - 1
    else:
        high = low
    x += 1

print(x)