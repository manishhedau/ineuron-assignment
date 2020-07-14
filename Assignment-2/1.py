# 1. Create the below pattern using nested for loop in Python.
"""
*
* *
* * *
* * * *
* * * * *
* * * *
* * *
* *
*

"""

m = int(input('Enter the number of columns : '))
for i in range(1):
    for j in range(m):
        print('* '*j)
    for k in range(m):
        print('* '*(m-k-2))
    print()