import json
python_object={"name":"meena","roll no":32,"subject":"coding"}
java_string=json.dumps(python_object)
print(java_string)
print(type(java_string))



import json

def encode_complex(object):
    # check using isinstance method
    if isinstance(object, complex):
        return [object.real, object.imag]
    # raised error if object is not complex
    raise TypeError(repr(object) + " is not JSON serialized")

complex_obj = json.dumps(2 + 3j, default=encode_complex)
print(complex_obj) 






