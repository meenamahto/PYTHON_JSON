#create_json_file :-

import json
a=open("shopping_file.json","w")
a.write('{"shopping_list":\n{ \n"chaco":"15",\n"Biscuits":"50",\n"Diary_milk":"30",\n"ice_cream":"20"\n} }')
a.close()
b=open("shopping_file.json","r")
c=b.read()
print(c)




d={
    "shopping_list":
        { 
            "chaco":15,
            "Biscuits":50,
            "Diary_milk":30,
            "ice_cream":20,
        } 
} 
a=input("Enter your element name:")
b=int(input("Enter your number elements:"))
d1={}
d2={}
for i in d:
    for j in d[i]:
        if a==j:
            d1.update({j:d[i][j]-b})
        else:
            d1.update({j:d[i][j]})
    d2.update({i:d1})

print(d2) 


## to add element:-


c=input("Enter your element name:")
e=int(input("Enter your number of elements:"))
d3={}
d4={}
for k in d2:
    for p in d2[k]:
        if c==p:
            print(d2[k][p])
            d3.update({p:d2[k][p]+e})
        else:
            d3.update({p:d2[k][p]})
    d4.update({k:d3})
print(d4)
