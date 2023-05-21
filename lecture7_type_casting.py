## type casting is a way through which we can change the type of a variable to another variable

## constructor functions: int(), float(), str() etc

## example:

x = "3"
y = int(x)
print(type(y))

x = 3.8
y = str(x)
print(type(y))

# x = "Debmalya"
# y = int(x)

## Homework
num = 6.5

# string
num_str = str(num)
print(num_str)
print(type(num_str))

# integer
num_int = int(num_str) # This will give error! Because this covertion is not allowed in Python
print(num_int)
print(type(num_int))
