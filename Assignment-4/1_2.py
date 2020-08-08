# Question - 1.2

# 1.2 Write a function filter_long_words() that takes a list of words and an integer n and returns
# the list of words that are longer than n.


# creating a function
def filter_long_words(lst,n):
    new_lst = []
    for i in lst:
        if len(i)>n:
            new_lst.append(i)
            
    return new_lst

# calling a function by passing some arguments
print('The list of words is : ',filter_long_words(['inueron','age','man','day','solid','datascience'],3))
    