def age_assignment(*args, **kwargs):
    result = ""
    for name in args:
        for key in kwargs:
            if name[0] == key:
                # kwargs[name] = kwargs.pop(key)
                kwargs[name] = kwargs[key]
                del kwargs[key]
                break
    for name, age in sorted(kwargs.items(), key= lambda x: x[0]):
        result += f"{name} is {age} years old.\n"
    return result


print(age_assignment("Peter", "George", G=26, P=19))
print(age_assignment("Amy", "Bill", "Willy", W=36, A=22, B=61))







'''Create a function called age_assignment() that receives a different number of names and a different number of key-value pairs. 
The key will be a single letter (the first letter of each name) and the value - a number (age). 
Find its first letter in the key-value pairs for each name and assign the age to the person's name.
Then, sort the names in ascending order (alphabetically) and return the information for each person on a new line in the format: 
"{name} is {age} years old."
Submit only the function in the judge system.'''