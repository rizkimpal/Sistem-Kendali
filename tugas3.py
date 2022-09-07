# this code from : https://github.com/VishnuKrishnathu/RouthHurwitz/blob/main/routh.py

from pandas import DataFrame
def addzero(array, length):
    if len(array)!= length:
        for i in range(len(array), length):
            array.append(0)
    return array

order = input("berapa orde?: ")
equation = []
for i in range(int(order), -1, -1):
    equation.append(int(input("koefisien untuk s^" + str(i) + ": ")))
table = []
layer1 = []
for i in range(0, len(equation),2):
    layer1.append(equation[i])
table.append(layer1)
print(layer1)
print(table)
layer2 = []
for i in range(1, len(equation),2):
    layer2.append(equation[i])
layer2 = addzero(layer2, len(layer1))
table.append(layer2)
print(layer2)
print(table)
for i in range(2, len(equation)):
    layers = []
    for j in range(0, len(layer1)-1):
        if (table[i-1][0] == 0):
            table[i-1][0] = "E"
            layers.append((table[i - 1][0] +"*"+ str(table[i - 2][j + 1]) + "-" + str(table[i - 2][0] * table[i - 1][j + 1])+ "/"+table[i-1][0]))
        elif (table[i-1][0] == "E"):
            layers.append((table[i - 1][0] +"*"+ str(table[i - 2][j + 1]) + "-" + str(table[i - 2][0] * table[i - 1][j + 1])+ "/"+table[i-1][0]))
        elif(type(table[i-1][0])== str and table[i-1][0] != "E" ):
            layers.append((table[i - 1][0] + "*" + str(table[i - 2][j + 1]) + "-" + str(
                table[i - 2][0]) +"*" + str(table[i - 1][j + 1]) + "/" + table[i - 1][0]))
        else:
            layers.append(
                round((table[i - 1][0] * table[i - 2][j + 1] - table[i - 2][0] * table[i - 1][j + 1]) / table[i - 1][0],
                      2))
    layers = addzero(layers, len(layer1))
    table.append(layers)
print(DataFrame(table))