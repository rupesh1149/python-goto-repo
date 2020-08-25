# this method encodes the data json
import json
import pickle

json_string = json.dumps([1,2,3,"a","b","c"]) #converting or python list into json string using dumps method
print(json.loads(json_string))

pickled_string = pickle.dumps([1,2,3,"a","b","c"])
print(pickle.loads(pickled_string))

# adding an key value pair to json object
import json

# fix this function, so it adds the given name
# and salary pair to salaries_json, and return it
def add_employee(salaries_json, name, salary):
    salaries = json.loads(salaries_json)
    salaries[name] = salary

    return json.dumps(salaries)

# test code
salaries = '{"Alfred" : 300, "Jane" : 400 }'
new_salaries = add_employee(salaries, "Me", 800)
decoded_salaries = json.loads(new_salaries)
print(decoded_salaries["Alfred"])
print(decoded_salaries["Jane"])
print(decoded_salaries["Me"])