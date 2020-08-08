# Question - 1.1
# 1.1 Write a Python Program(with class concepts) to find the area of the triangle using the below
# formula.
# area = (s*(s-a)*(s-b)*(s-c)) ** 0.5
# Function to take the length of the sides of triangle from user should be defined in the parent
# class and function to calculate the area should be defined in subclass.


#parent class
class AREA_OF_TRIANGLE():
    def __init__(self,s,a,b,c):
        self.s = s
        self.a = a
        self.b = b
        self.c = c


# derived class from parent class        
class derived_class(AREA_OF_TRIANGLE):
    def __init__(self,s,a,b,c):
        AREA_OF_TRIANGLE.__init__(self,s,a,b,c)
        
    def calculation(self):
        result = ((self.s*(self.s-self.a)*(self.s-self.b)*(self.s-self.c))*0.5)
        return result
    
# getting input from the user
s,a,b,c = input('Enter the s,a,b,c value : ').split(' ')

# creating an object of an derived class
obj = derived_class(int(s),int(a),int(b),int(c))
print('The Area of triangle : ',obj.calculation())