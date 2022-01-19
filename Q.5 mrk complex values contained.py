import json
def is_complex_num(objct):
    if '__complex__' in objct:
        return complex(objct['real'], objct['img'])
    return objct

complex_object =json.loads('{"__complex__": true, "real": 4, "img": 5}', object_hook = is_complex_num)
simple_object =json.loads('{"real": 4, "img": 3}', object_hook = is_complex_num)
print("Complex_object: ",complex_object)
print("Without complex object: ",simple_object)



## in second way:-

import json
def check(o):
    if "_complex_" in o:
        return complex(o["real"],o["img"])
    return o
a=json.loads('{"_complex_":true,"real":3,"img":6}')
b=check(a)
c=json.loads('{"real":3,"img":6}')
d=check(c)
print("this is complex=",b)
print("this is not complex=",d)

