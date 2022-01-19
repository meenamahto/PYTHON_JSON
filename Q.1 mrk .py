import json


d='{"name": "David", "class": "I", "age": 6}'
a=json.loads(d)
print(a)
print(type(a),type(d))
for i in a:
    print(i)






import json
python_object='{"name": "David", "class": "I", "age": 6}'
json_object=json.loads(python_object)
print(json_object)



