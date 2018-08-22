name_to_age = {"Bill": 21, "Jane": 4, "Jack": 56}

name = str(input("name"))
age = int(input("age"))
name_to_age[name] = age

for name, age in name_to_age:
    print(name, age)
