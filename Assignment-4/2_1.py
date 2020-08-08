# Question - 2.1


# 2.1 Write a Python program using function concept that maps list of words into a list of integers
# representing the lengths of the corresponding words.
# Hint: If a list [ ab,cde,erty] is passed on to the python function output should come as [2,3,4]
# Here 2,3 and 4 are the lengths of the words in the list.
# 


# creating an function to convert string length into numbers
def convert_str_len_into_int(lst):
    new_lst = []
    for i in lst:
        new_lst.append(len(i))
        
    return new_lst

print('The new lenght list is : ',convert_str_len_into_int(['ineuron','age','man','day','data','Machine learning']))
