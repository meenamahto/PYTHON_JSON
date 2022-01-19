
import json
d={
    '4': 5, 
    '6': 7, 
    '1': 3, 
    '2': 4
    }
f=[]
for g in d:
    f.append(g)
# print(f)
i=0
while i<len(f):
    j=0
    while j<len(f)-1:
        if f[j]>f[j+1]:
            temp=f[j]
            f[j]=f[j+1]
            f[j+1]=temp
        j+=1
    i+=1
# print(f)
new={}
for j in f:
    for k in d:
        if j==k:
            new[j]=d[k]
# print(new)
java_data=json.dumps(new)
print(java_data)



## in second way:-


import json
j_str = {'4': 5, '6': 7, '1': 3, '2': 4}
print("Original String:")
print(j_str)
print("\nJSON data:")
print(json.dumps(j_str, sort_keys=True))

