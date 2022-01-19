a=[['neelam','programer',24,2400,],['komal','trainer',24,20000],['anuradha','HR',25,40000],['Abhishek','manager',29,63000]]
b=[["name","degination","age","salary"],["name","degination","age","salary"],["name","degination","age","salary"],["name","degination","age","salary"]]
c=["emp1","emp2","emp3","emp4"]
d1={}
for i in range(len(a)):
    d={}
    for j in range(len(a[i])):
        d.update({b[i][j]:a[i][j]})
    d1.update({c[i]:d})
print(d1)


