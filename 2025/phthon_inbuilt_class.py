#phthon buit in class
#Enumeration

#'hello', 'world', 'python','class']
#b = list(enumerate(a))
#print(b)

# lambda function
#def add (num1, num2):
#    return num1 + num2

#add = lambda num1, num2: num1 + num2 # in lambda function, return is defined implicitly

#print(add(35, 65))

#map class 
#a = [1, 2, 3, 4, 5]
#[2, 4, 6, 8, 10] #expected output

#def multiply_by_two(num):
  #  return num * 2
 # multiply_by_two = lambda num: num * 2 
#print(list(map(multiply_by_two, a)))

#a = 2 
#b = 3
#a = 'A is greater than B' if a > b else 'B is greater than A'
#print(a)

# decorators (wrapper function)

#def hello (func):
 #       print("Hello, this is a decorator function")
        #        func()
        #        bye = "Goodbye, this is the end of the decorator function"
        #        print(bye)
            
        #@hello
        #def add():
        #        print(2+3)