# d=open("text_file.txt","w")
# d.write("Name Abhishek\n Designation CEO of navgurukul\n Gender male\n Age 29")
# d.close()
# c=open("text_file.txt","r")
# d=c.read()
# print(d)

import json
# file=open("text_file.json","w")
# file.write("Name Abhishek\nDesignation CEO of navgurukul\nGender male\nAge 29")
# file.close()
# e=open("text_file.json","r")
# f=e.read()
# print(f)
d="Name Abhishek Designation CEO of navgurukul Gender male Age 29"
d1=json.loads(d)
with open("text.json","w") as f:
    json.dump(d1,f)
print(f)
with open("text.json","r") as f:
    b=json.load(f)
print(b)


