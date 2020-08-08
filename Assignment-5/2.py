# Question - 2


# 2. Implement a Python program to generate all sentences where subject is in
# ["Americans", "Indians"] and verb is in ["Play", "watch"] and the object is in
# ["Baseball","cricket"].
# Hint: Subject,Verb and Object should be declared in the program as shown below.
# subjects=["Americans ","Indians"]
# verbs=["play","watch"]
# objects=["Baseball","Cricket"]
# Output should come as below:


# Americans play Baseball.
# Americans play Cricket.
# Americans watch Baseball.
# Americans watch Cricket.
# Indians play Baseball.
# Indians play Cricket.
# Indians watch Baseball.
# Indians watch Cricket



lst1 = ["Americans", "Indians"]
lst2 = ["Play", "watch"]
lst3 = ["Baseball","cricket"]

for country in lst1:
    for activity in lst2:
        for sports in lst3:
            print(country + ' '+activity + ' '+sports)
 