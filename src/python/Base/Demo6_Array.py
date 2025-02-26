#列表=[元素1,元素2,....]列表用大括号
fans=[23,456,45,43,56,43,45,23,45,2,45,1,4,345,45]
print(fans)
for i in fans:
    i+=100
    print(i)
for i in range(len(fans)):
    fans[i]+=1000
    print(fans[i])

#元组用小括号
fa=()